# Apocalyptic Time-Unit Grammar in Hebrew/Aramaic Prophecy

## Definition

A cluster of **lexical and syntactic signals** by which Hebrew/Aramaic apocalyptic prophecy codes its numerical time-spans *differently* from ordinary narrative duration. In narrative prose, durations are built on the default lexeme **יוֹם** *yôm* "day" (usually paired with its natural complement לַיְלָה *laylāh* "night"). In Daniel's visions, the counted unit is systematically displaced by **non-standard substitutes** — עֶרֶב בֹּקֶר *ʿereḇ bōqer* ("evening-morning"), שָׁבֻעִים *šāḇuʿîm* ("sevens/weeks"), Aramaic עִדָּן *ʿiddān* ("time/set-time") — and the span is embedded inside **register-marking co-text** (sealing commands, *ʿēṯ qēṣ* "time of the end," scope beyond any natural lifespan, symbolic-decoding frame).

1. **Counted-unit displacement** — the ordinary `yāmîm` is replaced by a non-standard, often compound, lexeme
2. **Anarthrous asyndetic pairing** — the replacement noun appears without article and without conjunction (no *wə-*), forming a fused symbolic unit
3. **Register co-text** — sealing imperatives (חָתַם / סָתַם), *ʿēṯ qēṣ* horizon, ratio-scale mismatch against historical time
4. **Aramaic lexical shift** — inside Dan 2:4b–7:28 the apocalyptic unit is עִדָּן, not יוֹם / יוֹמָא (the Aramaic cognate)

These signals together mark a span as *candidate* for symbolic decoding (by the day-year hermeneutic of Num 14:34 / Ezek 4:6, or otherwise). The grammar itself does not prove the conversion; it flags that the number is not raw calendar time.

## Form Recognition

Apocalyptic time-unit phrases have one of the following shapes in parsed text:

| Shape | Parser signature | Examples |
|-------|------------------|----------|
| Asyndetic anarthrous noun pair (construed as one symbolic unit) | Noun.ms.Abs + Noun.ms.Abs (no ה, no ו between) | Dan 8:14 עֶרֶב בֹּקֶר; Dan 8:26 הָעֶרֶב וְהַבֹּקֶר (contrast: when the SAME noun pair is re-cited with article + waw it refers to the vision event, not the counted unit) |
| Cognate-pluralized counter | Noun.mp.Abs + Noun.mp.Abs (same √ or plural-of-plurals) | Dan 9:24 שָׁבֻעִים שִׁבְעִים "sevens-seventy" (Noun.mp.Abs √שׁבע + Noun.mp.Abs √שׁבע) |
| Escalating-number Aramaic triple | Noun.ms.Abs + Noun.mp.Abs + Noun.ms.Cst פְּלַג + Noun.ms.Abs | Dan 7:25; 12:7 עִדָּן וְעִדָּנִין וּפְלַג עִדָּן (1 + plural + half) |
| Hebrew equivalent of the triple | Noun.ms.Abs + Noun.mp.Abs + Noun.ms.Abs חֵצִי | Dan 12:7 לְמוֹעֵד מוֹעֲדִים וָחֵצִי (same schema in Hebrew register) |

- **Parser codes:** for the Dan 8:14 pair: `lex=ערב sp=subs Noun.ms.Abs` immediately followed by `lex=בקר sp=subs Noun.ms.Abs` with **no `lex=ו Conj`** and **no `lex=ה Art`** between them
- **Diagnostic co-text:** look up-stream/down-stream for (a) סָתַם / חָתַם Qal.Impv.2ms "seal/stop up" (Dan 8:26; 12:4; 12:9), (b) עֵת קֵץ construct chain `Noun.s.Cst עת + Noun.ms.Abs קץ` (Dan 8:17, 19; 11:35, 40; 12:4, 9), (c) numeric scope that outruns any plausible lifespan of the seer

## Functions with Examples

### 1. Asyndetic Noun-Pair as Decoded Symbolic Unit — Dan 8:14

| Slot | Hebrew | Parsing | Gloss |
|------|--------|---------|-------|
| Preposition | עַד | Prep | "unto" |
| Unit part 1 | עֶרֶב | Noun.ms.Abs | "evening" |
| Unit part 2 | בֹּקֶר | Noun.ms.Abs | "morning" |
| Cardinal | אַלְפַּיִם | Noun.d.Abs | "two-thousand" (dual) |
| Connector | וּ | Conj | "and" |
| Cardinal (construct) | שְׁלֹשׁ | Noun.s.Cst | "three" |
| Cardinal (absolute) | מֵאוֹת | Noun.fp.Abs | "hundreds" |
| Outcome | וְנִצְדַּק קֹדֶשׁ | Conj + Niphal.Perf.3ms + Noun.ms.Abs | "then shall the sanctuary be vindicated/cleansed" |

Parser-verified shape: `עַד עֶרֶב בֹּקֶר אַלְפַּיִם וּשְׁלֹשׁ מֵאוֹת`. The two nouns stand in **asyndetic juxtaposition** — no ו, no construct chain, no article — and are counted *as one unit* by a single cardinal (the number modifies the pair, not either noun singly). This is *not* the ordinary Tamid-evening/morning liturgical pair, which in narrative use occurs with article + waw (`הָעֶרֶב וְהַבֹּקֶר`) and/or with the definite Tamid frame (Exo 29:39–41; Num 28:4). The omission of the default `yāmîm` (2300 *days*) in favor of *ʿereḇ bōqer* is the lexical displacement that marks the span as symbolic.

### 2. Cognate-Pluralized Counter — Dan 9:24 שָׁבֻעִים שִׁבְעִים

| Slot | Hebrew | Parsing | Gloss |
|------|--------|---------|-------|
| Counted unit | שָׁבֻעִים | Noun.mp.Abs (√שׁבוע) | "weeks / sevens" |
| Cardinal | שִׁבְעִים | Noun.mp.Abs (√שׁבע) | "seventy" |
| Main verb | נֶחְתַּךְ | Niphal.Perf.3ms √חתך | "was cut/determined" |

Parser-verified: `שָׁבֻעִים שִׁבְעִים נֶחְתַּךְ עַל־עַמְּךָ`. The counted unit is **שָׁבֻעַ (seven-period)**, not יוֹם. This is itself a lexical substitute for the ordinary day-count, and the root-identical stacking שָׁבֻעִים שִׁבְעִים ("sevens-seventy" = 70 × 7) creates a compound symbolic unit. Niphal *neḥtak* "is cut/decreed" is a hapax in the MT in this sense and is itself register-marked (sealing/apportionment vocabulary).

### 3. Escalating Aramaic Triple — Dan 7:25 עִדָּן וְעִדָּנִין וּפְלַג עִדָּן

| Slot | Aramaic | Parsing | Gloss |
|------|---------|---------|-------|
| Preposition | עַד | Prep | "until" |
| Unit 1 (singular) | עִדָּן | Noun.ms.Abs | "a time" |
| Connector | וְ | Conj | "and" |
| Unit 2 (plural) | עִדָּנִין | Noun.mp.Abs | "times" |
| Connector | וּ | Conj | "and" |
| Unit 3 (half) | פְלַג עִדָּן | Noun.ms.Cst + Noun.ms.Abs | "dividing-of-time" |

Parser-verified: `עַד־עִדָּן וְעִדָּנִין וּפְלַג עִדָּן`. The Aramaic counter is עִדָּן (H5732, "appointed time"), **not** יוֹם / יוֹמָא. The same three-part schema — *singular + plural + half* — recurs in Hebrew at Dan 12:7 `לְמוֹעֵד מוֹעֲדִים וָחֵצִי` (Noun.ms.Abs מועד + Noun.mp.Abs מועד + וָ + Noun.ms.Abs חֵצִי): both use a high-register time-lexeme (*ʿiddān* / *môʿēd*) rather than *yôm*, and both build an arithmetic progression (1 + 2 + ½) as a single opaque span.

### 4. The Partial Counter-Example — Dan 12:11 `יָמִים אֶלֶף מָאתַיִם וְתִשְׁעִים`

| Slot | Hebrew | Parsing | Gloss |
|------|--------|---------|-------|
| Counted unit | יָמִים | Noun.mp.Abs | "days" |
| Thousand | אֶלֶף | Noun.s.Abs | "thousand" |
| Two-hundred | מָאתַיִם | Noun.fd.Abs | "two-hundred" (dual) |
| Connector + ninety | וְתִשְׁעִים | Conj + Noun.mp.Abs | "and ninety" |

Parser-verified: `יָמִים אֶלֶף מָאתַיִם וְתִשְׁעִים`. Dan 12:11 (and 12:12 *ʾašrê ha-məḥakkeh wə-yaggîaʿ lə-yāmîm ʾelep̄ šəlōš mēʾôṯ šəlōšîm wə-ḥămiššāh*) **does** use יָמִים. This fits the grammar in three ways:

- The *presence* of יָמִים is itself notable because Dan 8:14 *avoids* it. If the author were using `yāmîm` as the generic apocalyptic counter throughout, 8:14 would read `אַלְפַּיִם וּשְׁלֹשׁ מֵאוֹת יָמִים`. The deliberate non-use in 8:14 vs. the deliberate use in 12:11 shows that the lexical choice is a compositional signal.
- Dan 12:11's `yāmîm` is nonetheless embedded in **full apocalyptic register**: preceded in 12:4 by סָתֹם הַדְּבָרִים וַחֲתֹם הַסֵּפֶר עַד־עֵת קֵץ (sealing imperative pair + *ʿēṯ qēṣ*), followed in 12:9 by a second sealing imperative. The sealing frame sustains the symbolic register even where the counted noun is *yāmîm*.
- Dan 8:26 confirms the Danielic author can and does use `yāmîm` within the same vision-complex when he wants to: וְאַתָּה סְתֹם הֶחָזֹון כִּי לְיָמִים רַבִּים ("seal the vision, for [it is] for many days") — here `yāmîm` is used in the sealing-frame remark *about* the vision, not as the counted unit of the vision's number. The 8:14 avoidance is therefore contrastive, not a gap in the author's vocabulary.

### 5. Ordinary Narrative Time-Unit (Contrast Baseline)

| Reference | Hebrew | Parsing | Register |
|-----------|--------|---------|----------|
| Gen 7:4 | אַרְבָּעִים יוֹם וְאַרְבָּעִים לָיְלָה | Noun.mp.Abs + Noun.ms.Abs + Conj + Noun.mp.Abs + Noun.ms.Abs | narrative, literal |
| Exo 24:18 | אַרְבָּעִים יוֹם וְאַרְבָּעִים לָיְלָה | same shape | narrative, literal |
| 1 Kgs 19:8 | אַרְבָּעִים יוֹם וְאַרְבָּעִים לָיְלָה | same shape | narrative, literal |

All three parser-verified. The default narrative shape is **cardinal + יוֹם + וְ + cardinal + לַיְלָה**: the counted unit is יוֹם, the complementary half-span is לַיְלָה, a conjunction ו links them, and the cardinal applies to each noun separately. None of the three contains a sealing command, an *ʿēṯ qēṣ* horizon, or a numeric scope beyond the seer's lifetime — they are literal 40-day durations anchored in the surrounding narrative's own calendar (Flood, Sinai, flight-to-Horeb).

## Register Markers Beyond the Counted Noun

Parser-verified co-text that accompanies Daniel's time-spans (*not* found in Gen 7 / Exo 24 / 1 Kgs 19):

| Marker | Reference | Form |
|--------|-----------|------|
| Sealing of the vision | Dan 8:26 | סְתֹם הֶחָזוֹן Qal.Impv.2ms √סתם + def. Noun.ms.Abs |
| Paired sealing of words + book | Dan 12:4 | סְתֹם הַדְּבָרִים וַחֲתֹם הַסֵּפֶר Qal.Impv.2ms √סתם + Qal.Impv.2ms √חתם |
| Re-sealing directive | Dan 12:9 | סְתֻמִים וַחֲתֻמִים הַדְּבָרִים (passive-state pair) |
| *ʿēṯ qēṣ* "time of the end" horizon | Dan 8:17; 11:35, 40; 12:4, 9 | עֵת קֵץ Noun.s.Cst + Noun.ms.Abs |
| Horizon-extension remark on the vision | Dan 8:26 | לְיָמִים רַבִּים "for many days" — *marking the vision's durability, not counting its span* |

These markers tell the reader: (a) the contents are sealed / encoded; (b) their referent lies past the seer's horizon, at the *ʿēṯ qēṣ*. Together with the lexical displacement of the counted unit, they constitute the grammar's signal that the span is not calendar-literal.

## Relation to the Day-Year Hermeneutic (Num 14:34; Ezek 4:6)

The day-year formula itself (*yôm laššānāh yôm laššānāh*, documented in [day-year-formula](day-year-formula.md)) does **not** appear inside any Daniel time-prophecy. What this entry documents is the *upstream grammatical flag* — the set of signals that *call for* a decoding rule. The interpretive step then is:

1. **Flagged span** — counted unit is not *yāmîm* (Dan 8:14 *ʿereḇ bōqer*; 9:24 *šāḇuʿîm*; 7:25, 12:7 *ʿiddān* / *môʿēd*), or *yāmîm* is present but wrapped in full sealing + *ʿēṯ qēṣ* register (Dan 12:11–12)
2. **Decoding key** — Num 14:34 / Ezek 4:6 establish *yôm laššānāh* as a lexically-warranted Hebrew ratio between days and years
3. **Application** — interpreters apply the Num/Ezek ratio to the Daniel spans, converting each counted unit to a year

The grammar catalogued here is silent on whether step 3 is portable across books (historicist schools apply it; preterist/futurist generally do not). What the grammar *does* establish is that **step 1 is real**: Daniel's chosen counters are morphologically and lexically distinct from the narrative default, and that distinction is not an artifact of translation — it is present in the parsed Hebrew/Aramaic text.

## Contrast with Related Forms

| Form | Function | Example |
|------|----------|---------|
| Default narrative duration (יוֹם + לַיְלָה) | literal calendar-days | Gen 7:4; Exo 24:18; 1 Kgs 19:8 |
| Asyndetic *ʿereḇ bōqer* + cardinal (this entry) | flagged symbolic span | Dan 8:14 |
| Articulated paired *hā-ʿereḇ wə-ha-bōqer* | anaphoric reference to vision-event | Dan 8:26 (same nouns, article + waw, referring back) |
| Cognate-root *šāḇuʿîm šiḇʿîm* | flagged symbolic span, weeks-of-years shape | Dan 9:24 |
| Aramaic triple *ʿiddān we-ʿiddānîn u-pəlag ʿiddān* | flagged symbolic span | Dan 7:25; 12:7 (Heb. parallel *môʿēd* triple) |
| *yāmîm* + sealing + *ʿēṯ qēṣ* frame | flagged even though lexeme is ordinary | Dan 12:11–12 |
| *lə-yāmîm rabbîm* | register remark on vision's durability, not on its number | Dan 8:26 |
| Day-year formula *yôm laššānāh* | ratio-conversion idiom, distinct construction | Num 14:34; Ezek 4:6 |

Cross-linked entries:
- [day-year-formula](day-year-formula.md) — the interpretive key that is *imported* when the apocalyptic flag is present
- [vision-introduction-formulas](vision-introduction-formulas.md) — genre-frame that co-occurs with these time-units
- [symbol-decoding-predicate-nominal](symbol-decoding-predicate-nominal.md) — parallel symbol-decoding pattern within the same Danielic vision-grammar

## Common Collocations

| Element | Lemma | Strong's | Role |
|---------|-------|----------|------|
| עֶרֶב | ערב | H6153 | Dan 8:14 displacement counter (part 1) |
| בֹּקֶר | בקר | H1242 | Dan 8:14 displacement counter (part 2) |
| שָׁבוּעַ | שׁבוע | H7620 | Dan 9:24 displacement counter (heptadic) |
| עִדָּן (Aram.) | עדן | H5732 | Dan 7:25; 12:7 Aramaic displacement counter |
| מוֹעֵד | מועד | H4150 | Dan 12:7 Hebrew parallel counter |
| פְּלַג (Aram.) | פלג | H6387 | "dividing/half" in escalating triple |
| חֵצִי | חצי | H2677 | Hebrew "half" in escalating triple |
| סָתַם | סתם | H5640 | Qal.Impv.2ms "seal/stop up" — sealing frame |
| חָתַם | חתם | H2856 | Qal.Impv.2ms "seal" — sealing frame |
| עֵת קֵץ | עת / קץ | H6256 / H7093 | "time of the end" horizon marker |
| יוֹם | יום | H3117 | *default narrative counter* — its absence flags displacement |

---
*Generated from: hebrew_parser.py --verse "Dan 8:14", "Dan 7:25", "Dan 12:7", "Dan 9:24", "Dan 12:11", "Dan 8:26", "Dan 12:4", "Gen 7:4", "Exo 24:18", "1Ki 19:8"*
*Related: [day-year-formula](day-year-formula.md), [vision-introduction-formulas](vision-introduction-formulas.md), [symbol-decoding-predicate-nominal](symbol-decoding-predicate-nominal.md)*
*Last updated: 2026-04-19*
