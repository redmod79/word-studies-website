/**
 * Auto-links Strong's numbers (H1234, G5678, A1234) and word study
 * references (TR-*, WG-*) to their corresponding pages.
 *
 * Runs after page load, scans text nodes in .md-content, and wraps
 * unlinked references in <a> tags.
 */
(function () {
  "use strict";

  // Build lookup of known pages from the nav sidebar
  function buildPageIndex() {
    var index = {};
    // Scan all nav links for Strong's-numbered pages
    document.querySelectorAll("a.md-nav__link").forEach(function (a) {
      var href = a.getAttribute("href");
      if (!href) return;

      // Extract filename from href (e.g., "../../H3722-kaphar/" -> "H3722")
      var match = href.match(/([HAG]\d+)-/);
      if (match) {
        index[match[1]] = href;
      }
    });
    return index;
  }

  // Get the current page's Strong's number to avoid self-links
  function getCurrentPageId() {
    var path = window.location.pathname;
    var match = path.match(/([HAG]\d+)-/);
    return match ? match[1] : null;
  }

  function autoLink() {
    var pageIndex = buildPageIndex();
    var currentId = getCurrentPageId();

    // If no pages indexed, try a simpler approach: construct URLs directly
    // MkDocs Material with flat structure: /word-studies-website/H3722-kaphar/
    var content = document.querySelector(".md-content");
    if (!content) return;

    // Pattern: standalone Strong's numbers like H3722, G1785, A5732
    // Must not already be inside a link
    var pattern = /\b([HAG])(\d{1,5})\b/g;

    var walker = document.createTreeWalker(
      content,
      NodeFilter.SHOW_TEXT,
      null,
      false
    );

    var nodesToProcess = [];
    var node;
    while ((node = walker.nextNode())) {
      // Skip if inside an anchor, code, or pre element
      var parent = node.parentNode;
      if (!parent) continue;
      var tag = parent.tagName;
      if (tag === "A" || tag === "CODE" || tag === "PRE" || tag === "SCRIPT")
        continue;

      // Also skip if any ancestor is an anchor
      var ancestor = parent;
      var insideLink = false;
      while (ancestor && ancestor !== content) {
        if (ancestor.tagName === "A") {
          insideLink = true;
          break;
        }
        ancestor = ancestor.parentNode;
      }
      if (insideLink) continue;

      if (pattern.test(node.textContent)) {
        nodesToProcess.push(node);
      }
      pattern.lastIndex = 0;
    }

    // Process collected nodes (can't modify DOM during tree walk)
    nodesToProcess.forEach(function (textNode) {
      var text = textNode.textContent;
      var parts = [];
      var lastIndex = 0;
      var match;

      pattern.lastIndex = 0;
      while ((match = pattern.exec(text)) !== null) {
        var strongsId = match[1] + match[2];

        // Don't self-link
        if (strongsId === currentId) {
          continue;
        }

        // Add text before match
        if (match.index > lastIndex) {
          parts.push(document.createTextNode(text.slice(lastIndex, match.index)));
        }

        // Check if we know this page exists via nav index
        if (pageIndex[strongsId]) {
          var a = document.createElement("a");
          a.href = pageIndex[strongsId];
          a.textContent = match[0];
          a.title = strongsId + " word study";
          a.style.textDecoration = "none";
          a.style.borderBottom = "1px dotted";
          parts.push(a);
        } else {
          // Just leave as text if page doesn't exist in nav
          parts.push(document.createTextNode(match[0]));
        }

        lastIndex = match.index + match[0].length;
      }

      // Only replace if we found matches
      if (parts.length > 0) {
        // Add remaining text
        if (lastIndex < text.length) {
          parts.push(document.createTextNode(text.slice(lastIndex)));
        }

        var frag = document.createDocumentFragment();
        parts.forEach(function (p) {
          frag.appendChild(p);
        });
        textNode.parentNode.replaceChild(frag, textNode);
      }
    });
  }

  // Run on page load and on MkDocs instant navigation
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      setTimeout(autoLink, 100);
    });
  } else {
    setTimeout(autoLink, 100);
  }

  // MkDocs Material instant loading support
  if (typeof document$ !== "undefined") {
    document$.subscribe(function () {
      setTimeout(autoLink, 100);
    });
  }
})();
