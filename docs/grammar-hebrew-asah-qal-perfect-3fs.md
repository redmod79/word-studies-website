# Qal Perfect 3fs of עָשָׂה (asah) (Hebrew)

## Definition

The Qal perfect 3fs of עָשָׂה (H6213, "to do, make, perform, practise") is the third-person feminine singular perfective form of the base-stem active verb. The form treats the action as a completed whole, viewed from a vantage point after its conclusion. Across the Hebrew Bible it appears in four broad functional clusters: narrative storyline, legal/performative accusation, theological identificational attribution, and prophetic/apocalyptic summary. It occurs 29× in Qal (plus 6× in Niphal passive counterpart נֶעֶשְׂתָה).

1. **Narrative Preterite** — completed past action by a feminine singular subject in storyline
2. **Performative / Legal** — the act itself constitutes the offense or established state
3. **Identificational / Theological** — attributing an action explicitly to the hand of YHWH
4. **Prophetic Summary** — compressed retrospective within prophetic or apocalyptic discourse

## Form Recognition

- **Root:** עשׂה (III-he strong verb, H6213)
- **Stem:** Qal (base active stem)
- **Tense:** Perfect (suffix conjugation, perfective aspect)
- **Person/Gender/Number:** 3rd person / feminine / singular
- **Unsuffixed form:** עָשְׂתָה (prototypical; accentuation and maqqef may shift vowel length: עָשָׂ֑תָה, עָ֣שְׂתָה, etc.)
- **Suffix-bearing form:** עָשָׂ֑תְנִי (Job 33:4, +1cs suffix)
- **Parser code:** `sp=verb vs=qal vt=perf gn=f` (ETCBC/BHSA tag: `Verb.Qal.Perf.3fs`)

## Functions with Examples

### 1. Narrative Preterite

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Gen 27:17 | עָשָׂ֑תָה | Qal.Perf.3fs | "she had prepared" |
| 2 Sam 13:10 | עָשָׂ֔תָה | Qal.Perf.3fs | "she had made" |
| Ruth 2:19 | עָשְׂתָה֙ | Qal.Perf.3fs | "she had wrought" |
| Esth 1:9 | עָשְׂתָ֖ה | Qal.Perf.3fs | "made" |
| Esth 5:5 | עָשְׂתָ֥ה | Qal.Perf.3fs | "had prepared" |

> **Gen 27:17** — "And she gave the savoury meat and the bread, which she had prepared, into the hand of her son Jacob."  
> **2 Sam 13:10** — "And Tamar took the cakes which she had made, and brought them into the chamber to Amnon her brother."

### 2. Performative / Legal

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Lev 5:17 | עָֽשְׂתָ֗ה | Qal.Perf.3fs | "commit... to be done" |
| Deut 22:21 | עָשְׂתָ֤ה | Qal.Perf.3fs | "she hath wrought folly" |
| Ezek 22:3 | עָשְׂתָ֧ה | Qal.Perf.3fs | "maketh idols" |

> **Deut 22:21** — "...because she hath wrought folly in Israel, to play the whore in her father's house..."  
> **Ezek 22:3** — "The city sheddeth blood in the midst of it, that her time may come, and maketh idols against herself to defile herself."

### 3. Identificational / Theological

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Isa 41:20 | עָ֣שְׂתָה | Qal.Perf.3fs | "hath done this" |
| Job 12:9 | עָ֣שְׂתָה | Qal.Perf.3fs | "hath wrought this" |
| Isa 66:2 | עָשָׂ֔תָה | Qal.Perf.3fs | "hath mine hand made" |

> **Isa 41:20** — "...that the hand of the LORD hath done this, and the Holy One of Israel hath created it."  
> **Job 12:9** — "Who knoweth not in all these that the hand of the LORD hath wrought this?"

### 4. Prophetic Summary

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Jer 3:6 | עָשְׂתָ֖ה | Qal.Perf.3fs | "hath done" |
| Jer 18:13 | עָשְׂתָ֣ה | Qal.Perf.3fs | "hath done a very horrible thing" |
| Jer 50:15 | עָשְׂתָ֖ה | Qal.Perf.3fs | "as she hath done" |
| **Dan 8:12** | **עָשְׂתָ֖ה** | **Qal.Perf.3fs** | **"it practised"** |

> **Jer 18:13** — "...the virgin of Israel hath done a very horrible thing."  
> **Dan 8:12** — "And an host was given him against the daily sacrifice by reason of transgression, and it cast down the truth to the ground; **and it practised, and prospered.**"

#### Daniel 8:12 — Parsing Verification and Implications

- **Verse parse** (`hebrew_parser.py --verse "Dan 8:12"`):  
  וְעָשְׂתָ֖ה — **Verb.Qal.Perf.3fs** of עשׂה, glossed "make."
- **Syntactic frame:** The verb is fronted by conjunctive waw (וְ) and coordinated with the following Hiphil perfect 3fs וְהִצְלִֽיחָה ("and it prospered"). The two perfectives form a tightly-bound couplet summarising the horn/host's sustained activity.
- **Subject:** The feminine antecedent is either צָבָא (host/army, masculine in form but possibly construed as collective feminine in the vision's grammar) or the implied apocalyptic power whose actions are being telescoped. The KJV supplies "it" (referring back to the horn power of v. 9).
- **Aspectual force:** The perfective treats the action as a completed whole from the visionary perspective, compressing ongoing historical activity into a single summary statement. This is characteristic of apocalyptic narrative, where perfectives function as visionary snapshots rather than punctiliar past-tense reports.
- **Lexical nuance:** KJV "practised" (following LXX ἐποίησε and Vulgate *faciet*) reflects a specialised sense of עָשָׂה — habitual, wilful, or cultic action — rather than the generic "made/did." The choice of Qal (not Piel intensive or Hiphil causative) presents the action as direct, unmediated agency.

## Contrast with Related Forms

| Form | Morphology | Function | Example |
|------|------------|----------|---------|
| Qal Perfect 3fs | עָשְׂתָה | Completed action (feminine subject) | Dan 8:12; Gen 27:17 |
| Qal Perfect 3ms | עָשָׂה | Completed action (masculine subject) | Gen 1:31 "God made" |
| Qal Perfect 2fs | עָשִׂית | Completed action (2nd-feminine addressee) | Gen 3:13 "What hast thou done?" |
| Qal Imperfect 3fs | תַּעֲשֶׂה | Imperfective / future / modal | Gen 6:16 "thou shalt make" |
| Niphal Perfect 3fs | נֶעֶשְׂתָה | Passive / reflexive / tolerative | Num 15:24 "it was done" |
| Piel Perfect 3fs | — | Intensive / factitive (not attested for עשׂה) | — |
| Hiphil Perfect 3fs | — | Causative (not attested for עשׂה) | — |

> **Active–Passive Pair:** Qal Perfect 3fs עָשְׂתָה (active) ↔ Niphal Perfect 3fs נֶעֶשְׂתָה (passive). The Niphal occurs 6× (Num 15:24; Deut 13:15; Deut 17:4; 2 Sam 17:23; Mal 2:11; Neh 6:16), consistently with the sense "it was done / it has been committed."

## Complete Inventory: Qal Perfect 3fs of עָשָׂה

| Reference | Hebrew | Gloss | Context |
|-----------|--------|-------|---------|
| Gen 27:17 | עָשָׂ֑תָה | make | Rebekah prepared savoury meat |
| Lev 5:17 | עָֽשְׂתָ֗ה | make | Soul commits unintentional sin |
| Lev 25:21 | עָשָׂת֙ | make | Land produces fruit for three years |
| Deut 20:12 | עָשְׂתָ֥ה | make | City makes no peace |
| Deut 21:12 | עָשְׂתָ֖ה | make | Captive woman performs mourning rites |
| Deut 22:21 | עָשְׂתָ֤ה | make | Damsel wrought folly in Israel |
| 2 Sam 13:5 | עָשְׂתָ֤ה | make | Tamar to dress meat |
| 2 Sam 13:10 | עָשָׂ֔תָה | make | Tamar made cakes |
| 2 Sam 21:11 | עָשְׂתָ֛ה | make | Rizpah did acts of mourning |
| 1 Kgs 15:13 | עָשְׂתָ֥ה | make | Maachah made an idol |
| Isa 41:20 | עָ֣שְׂתָה | make | Hand of YHWH hath done this |
| Isa 66:2 | עָשָׂ֔תָה | make | Mine hand hath made all these |
| Jer 3:6 | עָשְׂתָ֖ה | make | Backsliding Israel hath done |
| Jer 18:13 | עָשְׂתָ֣ה | make | Virgin of Israel hath done horrible thing |
| Jer 50:15 | עָשְׂתָ֖ה | make | As Babylon hath done |
| Jer 50:29 | עָשְׂתָ֖ה | make | As she hath done |
| Ezek 16:48 | עָֽשְׂתָה֙ | make | Sodom hath not done as thou |
| Ezek 22:3 | עָשְׂתָ֧ה | make | City maketh idols against herself |
| Job 12:9 | עָ֣שְׂתָה | make | Hand of YHWH hath wrought this |
| Job 33:4 | עָשָׂ֑תְנִי | make (+1cs) | Spirit of God hath made me |
| Prov 31:22 | עָֽשְׂתָה | make | Virtuous woman maketh coverings |
| Prov 31:24 | עָ֭שְׂתָה | make | She maketh fine linen |
| Ruth 2:19 | עָשְׂתָה֙ | make | With whom Ruth had wrought |
| Esth 1:9 | עָשְׂתָ֖ה | make | Vashti made a feast |
| Esth 1:15 | עָשְׂתָ֗ה | make | What Vashti had done |
| Esth 2:1 | עָשָׂ֔תָה | make | What Vashti had done |
| Esth 5:5 | עָשְׂתָ֥ה | make | Banquet Esther had prepared |
| Esth 5:12 | עָשָׂ֖תָה | make | Banquet Esther had prepared |
| Esth 6:14 | עָשְׂתָ֥ה | make | Banquet Esther had prepared |
| **Dan 8:12** | **עָשְׂתָ֖ה** | **make** | **Horn/host practised and prospered** |

---

*Generated from: hebrew_parser.py (--verse, --lemma, --search)*  
*Last updated: 2026-04-21*
