# Directional / Locative Heh (-âh) (Hebrew)

## Definition

The directional heh (Hebrew *heh ha-meggammāh*, also called *heh directionis* / *heh locale*) is the suffix **-âh** (ָה) added to nouns to indicate **motion toward** or **direction into** a place. It functions as a morphological locative marker, often equivalent to the prepositions "to," "toward," or "into."

1. **Motion toward a common noun location** — indicates movement into or toward a place designated by a common noun.
2. **Motion toward a proper noun / place name** — same directional function with proper names.
3. **Cardinal and ordinal directionals** — on compass points, creates adverbials meaning "-ward" (northward, southward, etc.).
4. **Locative extension on place adverbs** — intensifies or extends the locative force of adverbs like *šām*.

## Form Recognition

- The suffix is spelled **heh** (ה) with qāmeṣ (ָה) in the unpointed form, producing the ending **-âh**.
- The parser tags heh-final forms with the univalent-final feature: **`uvf=H`**.
- **Important:** `uvf=H` captures **all** words ending in heh, including intrinsic heh-final nouns (e.g., מַעְלָה "top," גְרָרָה "Gerar"). The directional suffix must be identified by context: the base noun does not intrinsically end in -âh, and the context indicates motion toward the referent.
- The parsing string itself **does not** mark the directional suffix separately; it shows the normal noun parsing (e.g., `Noun.ms.Abs`, `PropN.s.Abs.+NAN`).

**Parser search:**
```bash
cd D:/bible/tools/hebrew && python hebrew_parser.py --search "uvf=H" --limit 50
```

## Functions with Examples

### 1. Motion toward a common noun location

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Gen 12:8 | הָרָה | Noun.ms.Abs | "unto a mountain" |
| Gen 19:10 | בָּיְתָה | Noun.ms.Abs | "into the house" |
| Gen 18:6 | אֹהֱלָה | Noun.ms.Abs | "into the tent" |

In these cases the directional heh marks the destination of movement. The noun stands without an explicit preposition of direction (though prepositions of person or purpose may co-occur).

### 2. Motion toward a proper noun / place name

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Gen 12:10 | מִצְרַיְמָה | PropN.s.Abs.+NAN | "into Egypt" |
| Gen 19:1 | סְדֹמָה | PropN.s.Abs.+NAN | "to Sodom" |
| Gen 18:22 | סְדֹמָה | PropN.s.Abs.+NAN | "toward Sodom" |

Proper names of places frequently take the directional heh in narrative motion formulas (e.g., "went down into Egypt," "came to Sodom").

### 3. Cardinal and ordinal directionals

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Gen 12:9 | הַנֶּגְבָּה | Noun.ms.Abs | "toward the south" |
| Gen 13:14 | צָפֹנָה | Noun.fs.Abs | "northward" |
| Gen 13:14 | קֵדְמָה | Noun.ms.Abs | "eastward" |
| Gen 13:14 | יָמָּה | Noun.ms.Abs | "westward" (lit. "seaward") |

With compass points the suffix produces adverbial directionals. The directional heh here is lexicalized and extremely productive across Hebrew narrative and legal texts.

### 4. Locative extension on place adverbs

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Gen 19:20 | שָׁמָּה | Adv.+NAN | "thither" |

On the adverb *šām* ("there"), the directional heh produces *šāmmâ* ("thither, to that place"), extending the locative force with explicit motion.

## Contrast with Related Forms

| Form | Function | Example |
|------|----------|---------|
| Directional heh (-âh) | motion toward; replaces or accompanies directional preposition | Gen 12:10 מִצְרַיְמָה "into Egypt" |
| Normal noun (no suffix) | static reference to place | Gen 13:10 מִצְרַיִם "Egypt" |
| Preposition אֶל + noun | explicit "to/toward" (person or place) | Gen 12:1 אֶל־הָאָרֶץ "unto the land" |
| Preposition לְ + infinitive | purpose/direction frame; may co-occur with heh | Gen 11:31 לָלֶכֶת אַרְצָה "to go unto the land" |

The directional heh frequently stands alone without אֶל or לְ (e.g., יָרַד מִצְרַיְמָה "went down to Egypt"), but it can also co-occur with prepositions of person or purpose.

## Common Words in This Form

Top lemmas attested with the directional heh in the Hebrew Bible (from parser search `uvf=H` and lemma verification):

| Lemma | Gloss | Directional Form | Occurrences |
|-------|-------|------------------|-------------|
| מִצְרַיִם | Egypt | מִצְרַיְמָה | frequent |
| בַּיִת | house | בָּיְתָה | frequent |
| הַר | mountain | הָרָה | frequent |
| אֶרֶץ | earth/land | אַרְצָה | frequent |
| חוּץ | outside | חוּצָה | frequent |
| אֹהֶל | tent | אֹהֱלָה | several |
| נֶגֶב | south | נֶגְבָּה | frequent |
| קֶדֶם | east/front | קֵדְמָה | frequent |
| צָפוֹן | north | צָפֹנָה | frequent |
| יָם | sea/west | יָמָּה | frequent |
| סְדֹם | Sodom | סְדֹמָה | several |
| שָׁם | there | שָׁמָּה | very frequent |

---
*Generated from: hebrew_parser.py (--search uvf=H, --lemma)*
*Last updated: 2026-04-21*
