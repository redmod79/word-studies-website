# Grammar Analysis: Numbers 14:34

## Text

**Hebrew (BHS):**
בְּמִסְפַּ֨ר הַיָּמִ֜ים אֲשֶׁר־תַּרְתֶּ֣ם אֶת־הָאָרֶץ֮ אַרְבָּעִ֣ים יֹום֒ יֹ֣ום לַשָּׁנָ֞ה יֹ֣ום לַשָּׁנָ֗ה תִּשְׂאוּ֙ אֶת־עֲוֹנֹ֣תֵיכֶ֔ם אַרְבָּעִ֖ים שָׁנָ֑ה וִֽידַעְתֶּ֖ם אֶת־תְּנוּאָתִֽי׃

**Transliteration (key phrase):**
*bəmispar hayyāmîm ăšer-tartem ʾet-hāʾāreṣ ʾarbāʿîm yôm — yôm laššānāh yôm laššānāh — tiśʾû ʾet-ʿăwōnōtêkem ʾarbāʿîm šānāh wîdaʿtem ʾet-tənûʾātî.*

**KJV:** "After the number of the days in which ye searched the land, even forty days, each day for a year, shall ye bear your iniquities, even forty years, and ye shall know my breach of promise."

## Word-by-Word Parsing

Source: `hebrew_parser.py --verse "Num 14:34"` (ETCBC BHSA)

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | בְּ | ב | Prep | in / according to |
| 2 | מִסְפַּ֨ר | מספר | Noun.ms.Cst | number (of) |
| 3 | הַ | ה | Art | the |
| 4 | יָּמִ֜ים | יום | Noun.mp.Abs | days |
| 5 | אֲשֶׁר | אשׁר | Conj (relative) | which / that |
| 6 | תַּרְתֶּ֣ם | תור | Verb.Qal.Perf.2mp | ye searched / spied out |
| 7 | אֶת | את | Prep (obj. marker) | — |
| 8 | הָ | ה | Art | the |
| 9 | אָרֶץ֮ | ארץ | Noun.s.Abs | land |
| 10 | אַרְבָּעִ֣ים | ארבע | Noun.mp.Abs | forty |
| 11 | יֹום֒ | יום | Noun.ms.Abs | day |
| 12 | **יֹ֣ום** | **יום** | **Noun.ms.Abs** | **a day** |
| 13 | **לַ** | **ל** | **Prep (+ def. art.)** | **for the** |
| 14 | **שָּׁנָ֞ה** | **שׁנה** | **Noun.fs.Abs** | **year** |
| 15 | **יֹ֣ום** | **יום** | **Noun.ms.Abs** | **a day** |
| 16 | **לַ** | **ל** | **Prep (+ def. art.)** | **for the** |
| 17 | **שָּׁנָ֗ה** | **שׁנה** | **Noun.fs.Abs** | **year** |
| 18 | תִּשְׂאוּ֙ | נשׂא | Verb.Qal.Impf.2mp | ye shall bear |
| 19 | אֶת | את | Prep (obj. marker) | — |
| 20 | עֲוֹנֹ֣תֵיכֶ֔ם | עון | Noun.mp.Abs+2mp suf. | your iniquities |
| 21 | אַרְבָּעִ֖ים | ארבע | Noun.mp.Abs | forty |
| 22 | שָׁנָ֑ה | שׁנה | Noun.fs.Abs | year |
| 23 | וִֽ | ו | Conj (waw) | and |
| 24 | ידַעְתֶּ֖ם | ידע | Verb.Qal.Perf.2mp (weqatal) | ye shall know |
| 25 | אֶת | את | Prep (obj. marker) | — |
| 26 | תְּנוּאָתִֽי | תנואה | Noun.fs.Abs+1cs suf. | my opposition / alienation |

(Bolded rows = the *yôm laššānāh yôm laššānāh* formula.)

## Clause Structure

Source: `hebrew_parser.py --clause "Num 14:34"`

- **Clause 1 (xYq0, main):** `בְּמִסְפַּר הַיָּמִים … יֹום לַשָּׁנָה יֹום לַשָּׁנָה תִּשְׂאוּ אֶת־עֲוֹנֹתֵיכֶם אַרְבָּעִים שָׁנָה`
  - [Adju] Adjunct: "By the number of the days … forty days, a day for the year, a day for the year" (the entire time-equivalency phrase is classed as a single fronted adjunct).
  - [Pred] Predicate: *tiśʾû* ("ye shall bear") — **Qal yiqtol 2mp**.
  - [Objc] Object: *ʾet-ʿăwōnōtêkem* ("your iniquities").
  - [Time] Time adjunct: *ʾarbāʿîm šānāh* ("forty years") — the *computed* output of the conversion.
- **Clause 2 (xQt0, subordinate relative):** `אֲשֶׁר תַּרְתֶּם אֶת־הָאָרֶץ` — "which ye spied out the land." Relative clause modifying *hayyāmîm*.
- **Clause 3 (WQt0, weqatal):** `וִידַעְתֶּם אֶת־תְּנוּאָתִי` — "and ye shall know my opposition." Weqatal chained to the main yiqtol, continuing future/modal force ("and [so] ye shall come to know…").

No construct chain is present beyond *mispar hayyāmîm* ("number of [the] days"). All other nominals are absolute.

## Key Grammatical Features

### 1. The distributive formula *yôm laššānāh yôm laššānāh* (words 12–17) — pure conversion rubric

- **Form:** Two identical appositional cola, each composed of an absolute noun (*yôm*, "day") + lamed-preposition *le-* prefixed to the article (*la-* = *lə- + ha-*) + absolute noun (*šānāh*, "year"). No verb, no conjunction, no construct binding — just repeated juxtaposition.
- **Function — distributive lamed:** The preposition *lə-* on *šānāh* is the classic **distributive / ratio / "reckoning" lamed** (Joüon-Muraoka §133d; GKC §123c; Waltke–O'Connor §11.2.10d). It answers the question "at what rate?" / "per what unit?" — "a day *for / per / corresponding to* a year."
- **Function — reduplication for distributive-universalizing force:** Hebrew marks distribution by repeating the noun phrase (cf. GKC §123c–d; Joüon-Muraoka §135d). The doubling *yôm laššānāh yôm laššānāh* is not stylistic filler; it is the grammatical way of saying "each and every day counts as one year." The two cola together = a fixed **one-to-one mapping between two time-series**, not a poetic flourish.
- **Definite article on *šānāh*:** *laššānāh* (with article) vs. anarthrous *yôm* is a recognized idiom for expressing a **standard unit** ("the year" = "per year as a fixed measure"), parallel to English "a day to the year."
- **Significance:** The verse itself supplies the interpretive key in its surrounding arithmetic: forty *yôm* of spying (v. 34a) → forty *šānāh* of wandering (v. 34b). The middle formula is the explicit **conversion rule** that licenses the equation. This is the lexical/syntactic locus of the "day-for-year principle" cited in later prophetic chronology (cf. Ezek 4:6, which uses nearly identical syntax: *yôm laššānāh yôm laššānāh nətattîw lāk*).

### 2. *tartem* (word 6) — Qal perfect 2mp in a relative clause with past reference

- **Form:** `Verb.Qal.Perf.2mp` from תור ("to spy out, reconnoitre"). Perfect aspect in a relative clause headed by *ăšer* denotes an already-completed past action.
- **Significance:** Anchors the "forty days" as a historically completed event (the reconnaissance of Num 13) — the *known* quantity on the left side of the day→year equation.

### 3. *tiśʾû* (word 18) — Qal yiqtol 2mp as legal/sentencing imperfective

- **Form:** `Verb.Qal.Impf.2mp` from נשׂא ("to lift, carry, bear"). Idiom *nāśāʾ ʿāwōn* = "to bear / be accountable for iniquity" — standard priestly-legal phrase for *assuming the consequences* of guilt (cf. Lev 5:1, 17; 7:18; Num 14:33).
- **Function:** Yiqtol here has **modal/declarative future** force ("ye shall bear" = divine decree fixing future liability), not simple prediction. It is the sentence handed down.
- **Significance:** The main verb is what the distributive formula *modifies*: the duration of bearing iniquity is calibrated to the duration of the spying, via the day=year ratio.

### 4. *wîdaʿtem* (word 24) — weqatal continuation

- **Form:** `Verb.Qal.Perf.2mp` with prefixed waw (*wəqātal*). Despite the perfect *morphology*, its syntactic role after a future-modal yiqtol is to **continue the future/consequent sense**.
- **Function:** "And [as a result] ye shall know / come to experience." Consecutive weqatal often marks a logical or resultative next step.
- **Significance:** Links the sentence of forty years to an experiential outcome — the people will *come to know* YHWH's *tənûʾāh* ("opposition / frustration / alienation"). The chronological punishment is not merely durative; it is pedagogical.
- **Grammar reference:** `../hebrew/syntax-waw-conjunction.md`

### 5. Numerical apposition: *ʾarbāʿîm yôm … ʾarbāʿîm šānāh*

- **Form:** Cardinal number (ms plural form *ʾarbāʿîm*) + singular absolute noun (*yôm* / *šānāh*). Hebrew standardly pairs tens with the **singular** of the counted noun (GKC §134e).
- **Function:** Not a construct chain; pure numerical apposition. The parallel "forty days … forty years" brackets the verse and is the *a priori* / *a posteriori* of the conversion: input (40 days, empirically known) ↔ output (40 years, judicially imposed).
- **Significance:** The two "forty"-phrases are deliberately symmetric; the *yôm laššānāh yôm laššānāh* colon is the bridge that explains the symmetry rather than merely asserting it.

## The Day-for-Year Formula in Hebrew Syntax (Summary)

The construction `noun₁ + lə-(+art.) + noun₂` — reduplicated — encodes a **proportional substitution**:

    yôm     la-š-šānāh     yôm     la-š-šānāh
    day    for-the-year    day    for-the-year
    [unit A]  [rate marker: per unit B]   [reduplicated for distributive scope]

Reading grammatically, the formula says: "(take) one day → (assign) one year; (take) one day → (assign) one year" — i.e., a **fixed 1:1 conversion applied distributively** across the whole set of counted days. Nothing in the syntax limits this to the immediate Numbers-13/14 context; the formula is a reusable rule-expression, which is why Ezek 4:6 can redeploy it verbatim in a different prophetic-symbolic setting.

## Cross-References

- **Parallel formula:** Ezekiel 4:6 — `יֹום לַשָּׁנָה יֹום לַשָּׁנָה נְתַתִּיו לָךְ` ("a day for a year, a day for a year, I have appointed it to thee"), explicitly applying the same syntax to prophetic-symbolic day-counts.
- **Related idiom:** *nāśāʾ ʿāwōn* — "bear iniquity" (Lev 5:1; 7:18; Num 14:33; 18:1; Ezek 4:4–6 immediately pairs this idiom with the same distributive formula).
- **Grammar library:**
  - Waw conjunction / weqatal continuation: `../hebrew/syntax-waw-conjunction.md`
  - (Concept entry for distributive *lamed* and nominal reduplication — not yet in library; candidate for a new canonical entry, e.g. `hebrew/syntax-distributive-lamed.md`.)
- **Word studies:**
  - יוֹם / *yôm* — `../../word-studies/H3117-yowm.md`
  - שָׁנָה / *šānāh* — `../../word-studies/H8141-shaneh.md`
