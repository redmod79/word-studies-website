# Day-Year Formula / Distributive Lamed of Ratio (Hebrew)

## Definition

The **day-year formula** (*yôm laššānāh*) is a fixed Hebrew idiom in which a duration counted in days is converted to a duration counted in years on a 1:1 ratio, using a **distributive/proportional lamed** (*lə-*) prefixed to the time unit that functions as the reckoning base. The formula occurs verbatim only twice in the Hebrew Bible — Num 14:34 and Ezek 4:6 — but the underlying distributive-lamed construction is a broader syntactic category.

1. **Distributive "for/per"** — *lə-* + noun = "for each X," "per X," "assigned to X"
2. **Ratio/conversion** — when two commensurable quantities flank the *lə-* construction, it encodes a fixed exchange rate between them
3. **Reduplication for emphasis** — repeating the phrase (*yôm laššānāh yôm laššānāh*) intensifies the distributive force and marks the ratio as fixed/deliberate

## Form Recognition

Typical shape in parsed text:

| Slot | Morphology | Gloss |
|------|-----------|-------|
| Unit counted (absolute) | Noun.ms.Abs | "a day" |
| Prep + article | `ל` Prep + `ה` Art | "to/for the" |
| Unit assigned (absolute) | Noun.fs.Abs | "year" |

- **Prep code:** `ל` (lamed) — in both canonical attestations it is **prefixed to the article** (לַ = lə- + haš-), giving definite `laššānāh` ("for the year") rather than indefinite `lə-šānāh`
- Parent numeric bracket: `אַרְבָּעִים יוֹם … אַרְבָּעִים שָׁנָה` ("forty days … forty years") frames the formula to make the 1:1 ratio explicit
- **Parser codes:** `sp=prep lex=ל` adjacent to `sp=art` + `Noun.fs.Abs lex=שׁנה`
- The construction is **not** a construct chain (no Cst form); both nouns stand in the absolute state, linked only by the preposition

## Functions with Examples

### 1. Day-for-Year Conversion (reckoning formula)

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Num 14:34 | יֹ֣ום לַשָּׁנָ֞ה יֹ֣ום לַשָּׁנָ֗ה | Noun.ms.Abs + Prep.+Art + Noun.fs.Abs (×2) | "each day for a year … for every day a year" |
| Ezek 4:6 | יֹ֧ום לַשָּׁנָ֛ה יֹ֥ום לַשָּׁנָ֖ה | Noun.ms.Abs + Prep.+Art + Noun.fs.Abs (×2) | "each day for a year … I have appointed thee a day for a year" |

Num 14:34 full context (tool output): `אַרְבָּעִים יוֹם … יוֹם לַשָּׁנָה יוֹם לַשָּׁנָה … אַרְבָּעִים שָׁנָה` — the reduplicated *yôm laššānāh* is the conversion key between the 40-day reconnaissance (Qal perf. *tartem* תור "you spied out") and the 40-year sentence (Qal yiqtol *tiśʾû* נשׂא "you shall bear"). Ezek 4:6 uses the identical formula to convert the prophet's 40-day right-side lying down into 40 years of Judah's iniquity, with the explicit performative *nətattîw lāk* ("I have appointed/given it to you").

### 2. Distributive Lamed in Non-Day-Year Contexts

The same syntactic pattern (prep. *lə-* + noun encoding "per/for each") is productive elsewhere:

| Reference | Hebrew | Function | KJV |
|-----------|--------|----------|-----|
| Gen 1:14 | לְאֹתֹת וּלְמוֹעֲדִים וּלְיָמִים וְשָׁנִים | *lə-* of purpose/assignment | "for signs, and for seasons, and for days, and years" |
| Num 28:3 | שְׁנַיִם לַיּוֹם | distributive ratio (two per day) | "two … day by day" |
| 1 Chr 27:1 | לְחֹדֶשׁ בַּחֹדֶשׁ | distributive "month by month" | "month by month" |
| Dan 12:11–12 | (numeric days, no *lə-šānāh*) | **bare day-count**, no formula | "thousand two hundred and ninety days" |

Note: Daniel's chapter-7/8/12 time-prophecies (מוֹעֵד מוֹעֲדִים וָחֵצִי, עֶרֶב בֹּקֶר, יָמִים) do **not** themselves carry the *yôm laššānāh* phrase — the formula as a hermeneutical tool is *imported* from Num 14 / Ezek 4 and applied to those texts by interpreters; the day-year formula entry here documents the grammar only.

## Contrast with Related Forms

| Form | Function | Example |
|------|----------|---------|
| *yôm laššānāh* (this formula) | 1:1 day-to-year conversion | Num 14:34; Ezek 4:6 |
| Accusative of duration | unmodified extent of time | Gen 7:4 "forty days and forty nights" |
| *bə-* + time noun | temporal "in/on" (point-in-time) | Gen 1:1 בְּרֵאשִׁית "in the beginning" |
| *lə-* + infinitive construct | purpose/result "in order to" | common; not a time-ratio construction |
| Construct chain X-of-Y | possession/qualification, not ratio | יְמֵי שָׁנָה "days of a year" (Lev 25:29) |

Related entries:
- [Distributive/temporal *lə-*](#) — not yet catalogued as a standalone entry
- [Accusative of extent of time](../greek/aorist-infinitive-accusative-of-duration.md) (Greek counterpart concept)

## Apocalyptic-Prophecy Usage Note (context-neutral)

The *yôm laššānāh* formula is cited by a long interpretive tradition (Jewish and Christian) as the grammatical warrant for rendering symbolic prophetic days as literal years in apocalyptic texts (e.g., Dan 7:25; 8:14; 9:24–27; 12:7, 11–12; Rev 11:2–3; 12:6, 14; 13:5). The grammar itself contains:

- A **definite preposition** (*laš-*, with article) indicating a *specified* reckoning base — the conversion is not open-ended
- **Numerical apposition** (*ʾarbāʿîm yôm ↔ ʾarbāʿîm šānāh*) demonstrating that the ratio is 1:1 and not metaphorical
- **Performative verbs** (*nātattî* Ezek 4:6; *tiśʾû* Num 14:34) framing the conversion as divine decree

What the grammar does **not** determine on its own:
- Whether the formula is *portable* from Num/Ezek (where the conversion is explicit in the immediate context) to apocalyptic texts (where it is not explicitly invoked)
- Whether apocalyptic time-spans (e.g., 2300 עֶרֶב בֹּקֶר, 1260 ἡμέραι, 42 μῆνες, καιρὸν καὶ καιροὺς καὶ ἥμισυ καιροῦ) are *symbolic* day-units awaiting conversion or *literal* day/month-units

Both questions are interpretive, handled by passage analyses and hermeneutical schools (historicist applies the formula; preterist / futurist generally do not; see passage files for Rev 11–13 and Dan 7–12).

## Common Collocations

| Element | Lemma | Strong's | Role in formula |
|---------|-------|----------|-----------------|
| יוֹם | יום | H3117 | counted unit (day) |
| שָׁנָה | שׁנה | H8141 | reckoning unit (year) |
| לְ | ל | H0 (prep) | distributive/ratio preposition |
| ה | ה | H0 (art) | definite article fused with *lə-* → *laš-* |
| אַרְבָּעִים | ארבע | H705 | framing cardinal ("forty") in both attestations |
| נָשָׂא עָוֹן | נשׂא / עון | H5375 / H5771 | idiom "bear iniquity" — the sentencing clause containing the formula |

---
*Generated from: hebrew_parser.py --verse "Num 14:34", "Eze 4:6"*
*Related passage analysis: [num-14-34](../passages/num-14-34.md)*
*Last updated: 2026-04-17*
