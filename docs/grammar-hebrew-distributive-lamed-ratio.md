# Distributive Lamed Ratio Formula (Hebrew)

## Definition

The **distributive/proportional lamed** (*lə-*) is the prepositional construction in which *lə-* + a noun (typically definite: *laš-*, *lay-*, *lā-*) marks the noun as the **reckoning base** over which some other quantity is distributed. When two commensurable quantities flank a *lə-* phrase, the construction encodes a fixed **ratio / exchange rate** between them ("X per Y," "X for each Y").

The **day-year ratio formula** — *yôm laššānāh yôm laššānāh* "a day for a year, a day for a year" — is a specific (and reduplicated) instance of this broader grammatical category, attested verbatim only in Num 14:34 and Ezek 4:6, where YHWH declares the 1:1 day-to-year conversion as a hermeneutical key for reading the surrounding narrative/prophecy.

Core functions of distributive *lə-*:

1. **Per/for each** — *lə-* + noun = "per X," "for each X," "assigned to X"
2. **Ratio / exchange rate** — when a counted quantity stands in apposition to *lə-* + reckoning unit, the construction fixes a numeric conversion between the two
3. **Reduplication for fixity** — repeating the phrase (e.g., *yôm laššānāh yôm laššānāh*) marks the ratio as deliberate, formal, decreed

> A canonical entry for the specific day-year idiom lives at [`day-year-formula.md`](day-year-formula.md). This entry documents the broader *distributive lamed* grammatical category of which *yôm laššānāh* is the most theologically loaded instance.

## Form Recognition

The ratio construction appears as:

| Slot | Morphology | Role |
|------|-----------|------|
| Counted quantity (X) | Numeral or noun, `Abs` | "how many" |
| Preposition *lə-* (± article) | `Prep ל` (+ `Art ה` → *laš-*, *lay-*, *lā-*) | distributive link |
| Reckoning unit (Y) | Noun, `Abs` | "per what" |

- **Parser signature:** `Noun.*.Abs` + `Prep lex=ל` (often immediately followed by `Art.+NAN`) + `Noun.*.Abs`
- **Not** a construct chain (no Cst forms on either side); the two nouns are linked only by the preposition, so the second noun is not possessed by the first
- **Definite vs. indefinite lamed:** in *yôm laššānāh* the lamed fuses with the article (*lə- + haš-* → *laš-*). Indefinite *lə-yôm* / *lə-šānāh* also occurs (e.g., *lə-yôm ʾeḥāḏ* "for one day," 1 Kgs 5:2) with the same distributive force — the article specifies the reckoning unit as *the* year-unit in force, but does not itself create the ratio
- **Framing numeral:** in both Num 14:34 and Ezek 4:6 the formula is flanked by identical cardinals (*ʾarbāʿîm yôm* … *ʾarbāʿîm šānāh*) that make the 1:1 ratio arithmetically explicit
- **References:** GKC §143e (distributive *lə-* with repetition); Waltke-O'Connor §11.2.10d (prepositional *lə-* of specification / benefaction with ratio force); Joüon-Muraoka §133d

## Functions with Examples

### 1. Ratio / Conversion (the day-year formula)

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Num 14:34 | יֹ֣ום לַשָּׁנָ֞ה יֹ֣ום לַשָּׁנָ֗ה | Noun.ms.Abs + Prep.+Art + Noun.fs.Abs (×2) | "each day for a year" |
| Ezek 4:6 | יֹ֧ום לַשָּׁנָ֛ה יֹ֥ום לַשָּׁנָ֖ה | Noun.ms.Abs + Prep.+Art + Noun.fs.Abs (×2) | "I have appointed thee each day for a year" |

**Num 14:34** (tool-parsed): `בְּמִסְפַּר הַיָּמִים אֲשֶׁר־תַּרְתֶּם אֶת־הָאָרֶץ אַרְבָּעִים יוֹם — יוֹם לַשָּׁנָה יוֹם לַשָּׁנָה — תִּשְׂאוּ אֶת־עֲוֹנֹתֵיכֶם אַרְבָּעִים שָׁנָה.` The reduplicated *yôm laššānāh* links 40 days of spying (Qal perf. *tartem* תור) to 40 years of bearing sin (Qal yiqtol *tiśʾû* נשׂא).

**Ezek 4:6** (tool-parsed): `אַרְבָּעִים יוֹם — יוֹם לַשָּׁנָה יוֹם לַשָּׁנָה — נְתַתִּיו לָךְ.` Same formula, with Qal perfect 1cs *nəṯattîw* נתן ("I have given/appointed it") as the performative verb framing the ratio as divine decree for a prophetic sign.

### 2. Ratio in non-temporal contexts (same grammar, different domains)

The distributive *lə-* ratio is **productive beyond the day-year idiom**. When the reckoning base is not *šānāh*, the same grammar encodes other fixed rates:

| Reference | Hebrew | Ratio | KJV |
|-----------|--------|-------|-----|
| Exod 16:22 | שְׁנֵ֥י הָעֹ֖מֶר לָאֶחָ֑ד | two omers per one (person) | "two omers for one man" |
| Num 28:3 | שְׁנַ֥יִם לַיֹּ֖ום | two per day | "two … day by day" |
| 1 Kgs 5:2 (Heb) | לְיֹ֣ום אֶחָ֑ד + שְׁלֹשִׁ֥ים כֹּר סֹ֔לֶת | 30 kor (per) one day | "Solomon's provision for one day was thirty measures of fine flour" |

These parallels confirm that the 1:1 ratio in *yôm laššānāh* is produced by **three things operating together**, not by the lamed alone:
1. the distributive *lə-* (which supplies "per / for each")
2. the numerical apposition (both flanking cardinals = 40, making the ratio computable as 1:1)
3. the reduplication (which marks the ratio as formal / decreed, not ad hoc)

### 3. Non-ratio distributive *lə-* (assignment / purpose)

The same preposition marks dedication or assignment without necessarily implying a ratio:

| Reference | Hebrew | Function | KJV |
|-----------|--------|----------|-----|
| Gen 1:14 | לְאֹתֹ֖ת וּלְמֹ֣ועֲדִ֔ים | *lə-* of purpose / assignment | "for signs, and for seasons" |
| Gen 47:24 | חֲמִישִׁ֖ית לְפַרְעֹ֑ה | assignment ("a fifth to Pharaoh") | "give the fifth part unto Pharaoh" |

Grammatically continuous with §1–2 but without a paired reciprocal quantity; translation "for" not "per."

## Contrast with Related Forms

| Form | Preposition | Function | Example |
|------|-------------|----------|---------|
| *yôm laššānāh* (this entry) | *lə-* + def. | **fixed ratio / conversion** | Num 14:34; Ezek 4:6 |
| *šānâ bə-šānâ* | *bə-* | **iterative** ("year after year," recurrence) | Deut 15:20; 2 Chr 9:24 |
| *šānâ šānâ* | — (bare apposition) | distributive recurrence ("year by year") | Deut 14:22 |
| *miyyôm lə-yôm* / *mēḥōdeš lə-ḥōdeš* | *min … lə-* | sequential progression ("from … to …") | Esth 3:7 |
| *yəmê šānāh* | construct chain | "days of a year" (possession, not ratio) | Lev 25:29 |
| Accusative of duration | none | bare temporal extent | Gen 7:4 "forty days" |

**Why *lə-* and not *bə-*?** Tool parses confirm the two prepositions do distinct work:

- *bə-* (*šānâ ḇə-šānâ*, Deut 15:20; 1 Sam 7:16; 2 Chr 9:24) marks **temporal location** ("in a year, in a year") and, when repeated, generates an **iterative** reading ("year after year, every year"). It does not place one quantity into proportional correspondence with another; it simply repeats the time-frame.
- *lə-* (*yôm laššānāh*) marks the second noun as the **reckoning base for assigning** the first. The semantic contribution is directional: *day → year*, the day being *given to / paid against* the year. This is the preposition's standard dative/allative force, here specialized as a ratio.

**Linked entries:**
- [Day-year formula](day-year-formula.md) — specific theological/hermeneutical instance of this grammar
- [Waw-conjunction syntax](syntax-waw-conjunction.md) — for framing cardinals in the surrounding clauses

## Questions the Grammar Can and Cannot Answer

**Q1: Why does Num 14:34 / Ezek 4:6 use *lə-* + definite *šānâ* rather than a bare *šānāh*?**
The bare accusative-of-duration pattern (*ʾarbāʿîm šānāh*, "forty years," as in the surrounding frame) states a duration; it does not convert one duration into another. The lamed is needed precisely because *two* durations are in view and one must be specified as the reckoning base. The definite article (*laš-*) marks *the* year-unit as the specified / contextually anchored measure — the conversion operates against a determinate standard, not an open-ended one.

**Q2: Is the formula unique to these two verses, or does it occur elsewhere with other nouns?**
The *exact phrase* *yôm laššānāh* occurs only at Num 14:34 and Ezek 4:6 (doubly reduplicated in both). But the underlying grammar — distributive *lə-* producing a numerical ratio — is widely attested (Exod 16:22 *šənê hāʿōmer lāʾeḥāḏ*, Num 28:3 *šənayim layyôm*, 1 Kgs 5:2 *lə-yôm ʾeḥāḏ*). The formula is thus a **theologically weighted deployment of a common construction**, not a unique idiom.

**Q3: Is the 1:1 ratio force encoded in the grammar itself, or supplied by context?**
The lamed encodes **distributive assignment** ("per," "for each"). The **1:1 numeric value** is supplied by the *framing cardinals* (*ʾarbāʿîm yôm ↔ ʾarbāʿîm šānāh*): because both flanking quantities are 40, simple arithmetic yields 1:1. In Num 28:3 the same grammar yields 2:1 (*šənayim layyôm* = two per day). The grammar encodes *the ratio operator*; context encodes *the ratio value*.

**Q4: Does the grammar support extending the ratio to other prophetic time-units (e.g., *ʿereḇ bōqer laššānāh*)?**
Grammatically the construction is productive with any noun in the counted slot — one could, in principle, write *ʿereḇ bōqer laššānāh* "an evening-morning for a year" and the sentence would be well-formed Hebrew for a 1:1 evening-morning-to-year ratio. But the MT does **not** do this. Dan 8:14 uses *ʿereḇ bōqer* as a bare apposition with *ʾalpayim ûšəlōš mēʾôṯ* ("2,300") without any *lə-šānāh* rider; Dan 12:7 uses *mōʿēḏ mōʿăḏîm wāḥēṣî* with no *lə-* at all. Whether Num 14:34 / Ezek 4:6 licenses interpreters to **supply** a *laššānāh* conversion for apocalyptic time-units is a *hermeneutical* question (historicist schools answer yes; see passage files), not a grammatical one. The grammar permits the construction; the text does not contain it in Dan/Rev.

## Common Collocations in Ratio Constructions

| Counted slot | Reckoning slot | Ratio | Reference |
|--------------|----------------|-------|-----------|
| יוֹם (day) | לַשָּׁנָה (year) | 1 day : 1 year | Num 14:34; Ezek 4:6 |
| שְׁנַיִם (two) | לַיּוֹם (day) | 2 : 1 day | Num 28:3 |
| שְׁנֵי הָעֹמֶר (two omers) | לָאֶחָד (per person) | 2 omers : 1 person | Exod 16:22 |
| שְׁלֹשִׁים כֹּר (30 kor) | לְיוֹם אֶחָד (per one day) | 30 kor : 1 day | 1 Kgs 5:2 |
| חֲמִישִׁית (fifth) | לְפַרְעֹה (to Pharaoh) | 1/5 share assigned | Gen 47:24 |

---
*Generated from: hebrew_parser.py --verse "Num 14:34", "Eze 4:6", "Deu 14:22", "Deu 15:20", "1Sa 7:16", "Est 3:7", "2Ch 9:24", "1Ki 10:25", "Num 28:3", "1Ki 5:2", "Exo 16:22", "Dan 8:14", "Gen 47:24"*
*Related entries: [day-year-formula.md](day-year-formula.md)*
*Last updated: 2026-04-19*
