# Grammar Analysis: Leviticus 16:30

## Text

**Hebrew:** כִּֽי־בַיֹּ֥ום הַזֶּ֛ה יְכַפֵּ֥ר עֲלֵיכֶ֖ם לְטַהֵ֣ר אֶתְכֶ֑ם מִכֹּל֙ חַטֹּ֣אתֵיכֶ֔ם לִפְנֵ֥י יְהוָ֖ה תִּטְהָֽרוּ׃

**KJV:** For on that day shall [the priest] make an atonement for you, to cleanse you, [that] ye may be clean from all your sins before the LORD.

## Word-by-Word Parsing

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | כִּֽי | כי | Conj | that/for |
| 2 | בַ | ב | Prep | in |
| 3 | (article) | ה | Art | the |
| 4 | יֹּ֥ום | יום | Noun.ms.Abs | day |
| 5 | הַ | ה | Art | the |
| 6 | זֶּ֛ה | זה | DemPron.ms | this |
| 7 | יְכַפֵּ֥ר | כפר | **Verb.Piel.Impf.3ms** | cover/atone |
| 8 | עֲלֵיכֶ֖ם | על | Prep.+2mp | upon you |
| 9 | לְ | ל | Prep | to |
| 10 | טַהֵ֣ר | טהר | **Verb.Piel.InfCon.Abs** | cleanse |
| 11 | אֶתְכֶ֑ם | את | Prep.+2mp | you (obj.) |
| 12 | מִ | מן | Prep | from |
| 13 | כֹּל֙ | כל | Noun.ms.Cst | all/whole of |
| 14 | חַטֹּ֣אתֵיכֶ֔ם | חטאת | Noun.fp.Abs.+2mp | your sins |
| 15 | לִ | ל | Prep | to/before |
| 16 | פְנֵ֥י | פנה | Noun.mp.Cst | face of |
| 17 | יְהוָ֖ה | יהוה | PropN.ms.Abs | YHWH |
| 18 | תִּטְהָֽרוּ | טהר | **Verb.Qal.Impf.2mp** | you shall be clean |

*Source: hebrew_parser.py --verse "Lev 16:30"*

## Clause Structure

The verse divides into three clauses (ETCBC analysis):

```
Clause 1 (xYq0, Q):  כִּי בַיֹּום הַזֶּה יְכַפֵּר עֲלֵיכֶם
  [Conj] כִּי
  [Time] בַיֹּום הַזֶּה
  [Pred] יְכַפֵּר
  [Cmpl] עֲלֵיכֶם

Clause 2 (InfC, Q):   לְטַהֵר אֶתְכֶם
  [Pred] לְטַהֵר
  [Objc] אֶתְכֶם

Clause 3 (xYq0, Q):   מִכֹּל חַטֹּאתֵיכֶם לִפְנֵי יְהוָה תִּטְהָרוּ
  [Cmpl] מִכֹּל חַטֹּאתֵיכֶם
  [Adju] לִפְנֵי יְהוָה
  [Pred] תִּטְהָרוּ
```

*Source: hebrew_parser.py --clause "Lev 16:30"*

## Construct Chain Analysis

Two construct chains in the verse:

1. **כֹּל חַטֹּאתֵיכֶם** — כֹּל (whole, CONSTRUCT) + חַטֹּאתֵיכֶם (your sins, ABSOLUTE) — "all of your sins"
2. **פְנֵי יְהוָה** — פְנֵי (face of, CONSTRUCT) + יְהוָה (YHWH, ABSOLUTE) — "the face of YHWH" = "before YHWH"

*Source: hebrew_parser.py --construct "Lev 16:30"*

## Key Grammatical Features

### 1. The Kaphar-Taher Formula: A Three-Verb Sequence Unique to Leviticus 16:30

The verse deploys three verbs from two roots in a tightly structured chain:

| Position | Hebrew | Root | Stem | Conjugation | Function |
|----------|--------|------|------|-------------|----------|
| 1st | יְכַפֵּר | כפר (kaphar) | **Piel** | Imperfect 3ms | Main predicate — the priestly atoning action |
| 2nd | לְטַהֵר | טהר (taher) | **Piel** | Infinitive Construct | Purpose/result clause — what the atonement accomplishes |
| 3rd | תִּטְהָרוּ | טהר (taher) | **Qal** | Imperfect 2mp | Independent clause — the people's resulting state |

This three-verb formula appears only here in the Hebrew Bible. The progression tracks a complete movement from priestly action to accomplished state:

- **יְכַפֵּר** (Piel imperfect) — the priest performs the atoning action. The Piel of כפר is factitive/resultative: "he shall effect atonement upon you." The imperfect (yiqtol) within a כִּי-clause functions as a future/predictive: this is what the day accomplishes.
- **לְטַהֵר** (Piel infinitive construct with ל) — the purpose infinitive states the intended result of the atonement: "in order to cleanse you." The Piel of טהר is factitive — it causes the state of cleanness. Paired with the direct object marker אֶתְכֶם, it specifies the people as the ones being brought into a state of cleanness.
- **תִּטְהָרוּ** (Qal imperfect 2mp) — the final verb shifts both stem and person. The Qal of טהר is stative/intransitive: "you shall be clean." The subject shifts from third-person priestly action to second-person congregational state. The Qal imperfect here is future/resultative: it describes the achieved condition, not an ongoing action.

**Stem shift significance:** The movement from Piel to Qal within the same root (טהר) carries a precise grammatical distinction. Piel טהר = transitive, causative-of-state ("cause to be clean"); Qal טהר = intransitive stative ("be clean"). The Piel infinitive describes what the priest effects upon the people; the Qal imperfect describes what the people become. The grammar encodes that cleanness is both externally conferred (Piel) and internally realized (Qal).

### 2. יְכַפֵּ֥ר — Piel Imperfect 3ms of כפר

- **Form:** Piel imperfect 3ms. The Piel stem of כפר is its dominant form (92 of 102 occurrences — see [H3722-kaphar](../../word-studies/H3722-kaphar.md)). The dagesh forte in the pe (כַפֵּר) and the yod prefix (יְ) mark the Piel imperfect.
- **Significance:** The Piel of כפר is a "common Piel-only verb" (see [stem-piel](../hebrew/stem-piel.md), section on Piel-only verbs) — the cultic sense of "make atonement" exists almost exclusively in this stem. The imperfect tense within a כִּי-clause gives it predictive/prescriptive force: "for on that day he shall make atonement." No explicit subject noun appears (the priest is implied from context), giving the verb a quasi-impersonal quality — the day itself is foregrounded as the grammatical anchor (בַיֹּום הַזֶּה), not the priestly agent.
- **Grammar reference:** [stem-piel](../hebrew/stem-piel.md), [qal-imperfect](../hebrew/qal-imperfect.md)
- **Word study:** [H3722-kaphar](../../word-studies/H3722-kaphar.md)

### 3. לְטַהֵ֣ר — Piel Infinitive Construct of טהר with Lamed of Purpose

- **Form:** Piel infinitive construct (Abs state per parser), prefixed with the preposition ל. The Piel vowel pattern (qattēl → ṭahēr) with the doubled middle consonant (dagesh in ה) identifies the stem. The infinitive construct is the verbal noun form — it functions syntactically as the predicate of a subordinate purpose clause.
- **Significance:** The ETCBC clause analyzer brackets this as an independent infinitive construct clause (type InfC) with its own predicate [Pred] and object [Objc]. The ל prefix conveys purpose or intended result: "in order to cleanse you." This makes the Piel infinitive the grammatical hinge of the verse — it links the priestly action (kaphar) to the congregational result (titharu).
- **Piel function here:** The Piel of טהר can be either factitive ("cause to be clean") or declarative-estimative ("pronounce clean") depending on context. In the Leviticus 13 skin-disease passages, Piel טהר is declarative: the priest pronounces someone clean after observing that healing has occurred (Lev 13:6, 13:13, 14:7 — see [stem-piel](../hebrew/stem-piel.md), declarative-estimative section). But in Lev 16:30, the Piel infinitive is factitive: the atonement *causes* the state of cleanness, it does not merely declare a pre-existing condition. The direct object marker אֶתְכֶם ("you") receives the action — the people are being brought into the state of clean.
- **Grammar reference:** [stem-piel](../hebrew/stem-piel.md)
- **Word study:** [H2891-taher](../../word-studies/H2891-taher.md)

### 4. תִּטְהָֽרוּ — Qal Imperfect 2mp of טהר

- **Form:** Qal imperfect 2mp. Prefix תִּ (2nd person) + root טהר + suffix וּ (masculine plural). The Qal stem is the base/simple stem — for stative roots like טהר, it means "be in the state of clean."
- **Significance:** This is the climactic verb of the verse, placed last for emphasis. Three things shift simultaneously from the previous verb:
  1. **Stem:** Piel → Qal (transitive/causative → intransitive/stative)
  2. **Person:** 3ms → 2mp (he/priest → you/congregation)
  3. **Clause type:** dependent infinitive → independent finite clause
  
  The effect is a grammatical transition from action done *to* the people to a state realized *in* the people. The Qal imperfect of a stative verb functions as future/resultative: "you shall be clean." The complement מִכֹּל חַטֹּאתֵיכֶם ("from all your sins") specifies the source from which cleanness separates them.
- **Grammar reference:** [qal-imperfect](../hebrew/qal-imperfect.md)

### 5. לִפְנֵ֥י יְהוָ֖ה — "Before the Face of YHWH"

- **Form:** The preposition ל + construct chain פְנֵי יְהוָה. The construct noun פְנֵי is the masculine plural construct of פנה ("face"), and יְהוָה is the absolute proper noun completing the chain.
- **Syntactic placement:** The ETCBC clause parser brackets לִפְנֵי יְהוָה as an adjunct [Adju] within the third clause, modifying the predicate תִּטְהָרוּ. This placement is grammatically significant: it attaches to the *result* clause, not to the *action* clause. The people shall be clean *before YHWH* — the cleanness is defined in reference to God's presence, not merely in reference to a ritual procedure.
- **Significance in context:** The phrase לִפְנֵי יְהוָה appears throughout Leviticus 16 to locate actions within the sanctuary/divine-presence sphere (Lev 16:1, 2, 12, 13, 18). But in v.30, it modifies the people's achieved state rather than the priest's ritual action. The people's cleanness exists "before the face of YHWH" — that is, it is valid and recognized in the sphere of the divine presence. This transforms cleanness from a ritual status into a relational condition.

## Formula Comparison: Kaphar → Taher vs. Kaphar → Salach

Leviticus employs two distinct post-atonement formulas. They never overlap in the same verse, and they appear in different ritual contexts:

### Formula A: Kaphar → Salach (Daily/Regular Offerings)

```
וְכִפֶּר עֲלֵהֶם הַכֹּהֵן וְנִסְלַח לָהֶם
"and the priest shall make atonement for them, and it shall be forgiven them"
```

Parser-verified occurrences: Lev 4:20, 4:26, 4:31, 4:35, 5:10, 5:13, 5:16, 5:18, 5:26, 19:22; Num 15:25, 15:26, 15:28.

| Feature | Kaphar → Salach |
|---------|-----------------|
| Verb 1 | כִפֶּר — Piel **perfect** 3ms |
| Verb 2 | נִסְלַח — **Niphal** perfect 3ms |
| Conjunction | וְ (waw-consecutive) |
| Agent of V2 | **None stated** — divine passive ("it shall be forgiven him") |
| Subject of salach | **God** (exclusively — salach is never predicated of a human agent) |
| Object | **Individual** — "for him" (לוֹ) or "for them" (לָהֶם) |
| Context | Individual sin offerings (Lev 4-5), trespass offerings, regular sin-purification |

### Formula B: Kaphar → Taher (Day of Atonement)

```
יְכַפֵּר עֲלֵיכֶם לְטַהֵר אֶתְכֶם ... תִּטְהָרוּ
"he shall make atonement for you, to cleanse you ... you shall be clean"
```

Occurs in Leviticus 16:30 only in this full three-verb form.

| Feature | Kaphar → Taher |
|---------|----------------|
| Verb 1 | יְכַפֵּר — Piel **imperfect** 3ms |
| Verb 2 | לְטַהֵר — Piel **infinitive construct** |
| Verb 3 | תִּטְהָרוּ — **Qal** imperfect 2mp |
| Conjunction | ל (purpose preposition, not waw) |
| Agent of V2 | **Implicit** — same agent as V1 (priest/atonement) |
| Subject of V3 | **The people themselves** — 2mp "you shall be clean" |
| Object | **Corporate** — "for you" (עֲלֵיכֶם) = all Israel |
| Scope | מִכֹּל חַטֹּאתֵיכֶם — "from ALL your sins" |
| Context | Annual Day of Atonement — comprehensive, not individual |

### Structural Differences

1. **Tense pattern.** Formula A uses the perfect (completed action: "the priest atoned... and he was forgiven"). Formula B uses the imperfect (prescriptive/future: "he shall atone... you shall be clean"). The perfect in Formula A presents atonement and forgiveness as accomplished facts within the ritual narrative. The imperfect in Formula B presents the Day of Atonement as a recurring, prospective institution.

2. **Stem of the result verb.** Formula A ends in the **Niphal** of סלח — a divine passive. No agent is named; forgiveness happens to the offerer. Formula B ends in the **Qal** of טהר — a stative describing the people's condition. The people are the grammatical subject of their own cleanness.

3. **Purpose clause.** Formula A has no purpose clause — the forgiveness follows the atonement with a simple waw-consecutive. Formula B inserts a purpose infinitive (לְטַהֵר) between the atonement and the result, making the logical connection explicit: atonement *for the purpose of* cleansing.

4. **Scope markers.** Formula A addresses individual offerers and specific sins. Formula B addresses the entire congregation (עֲלֵיכֶם, 2mp) and specifies "from ALL your sins" (מִכֹּל חַטֹּאתֵיכֶם). The כֹּל + construct chain functions as a comprehensive scope marker.

5. **The third verb.** Formula A is a two-verb formula (kaphar + salach). Formula B is a three-verb formula (kaphar + taher [Piel inf.] + taher [Qal impf.]). The added third verb in Formula B brings the congregation into the grammar as active subjects — they are not merely recipients of forgiveness (passive, Formula A) but become grammatically clean (stative, Formula B).

### Related Kaphar + Taher Pairings Elsewhere in Leviticus

The kaphar → taher sequence (without the full three-verb formula) appears in several purification contexts:

- **Lev 12:7** — וְכִפֶּר עָלֶיהָ ... **וְטָהֲרָה** — "and [the priest] shall make atonement for her, **and she shall be clean**" (Piel.Perf.3ms + Qal.Perf.3fs). Two-verb sequence in the postpartum purification law. The Qal perfect (taharah) states the achieved state directly.
- **Lev 14:20** — וְכִפֶּר עָלָיו הַכֹּהֵן **וְטָהֵר** — "the priest shall make atonement for him, **and he shall be clean**" (Piel.Perf.3ms + Qal.Perf.3ms). Leper cleansing ritual. Same two-verb kaphar → Qal-taher pattern.
- **Lev 16:19** — וְטִהֲרוֹ **וְקִדְּשׁוֹ** — "and [he shall] **cleanse it and consecrate it**" (Piel.Perf.3ms+3ms of טהר + Piel.Perf.3ms+3ms of קדשׁ). Here taher is Piel (factitive — actively cleansing the altar), and it is paired with a second Piel (qiddesh) rather than with kaphar.

These comparison verses show that the two-verb kaphar + Qal-taher sequence exists as a shorter pattern in individual purification contexts. Leviticus 16:30 expands this by inserting the Piel infinitive between kaphar and Qal-taher, creating the unique three-stage formula.

## Cross-References

- **Grammar library:**
  - [stem-piel](../hebrew/stem-piel.md) — Piel factitive, declarative-estimative, and Piel-only verbs
  - [qal-imperfect](../hebrew/qal-imperfect.md) — Qal imperfect functions (future/predictive, resultative)
  - [construct-state](../hebrew/construct-state.md) — construct chain פְנֵי יְהוָה and כֹּל חַטֹּאתֵיכֶם
- **Word studies:**
  - [H3722-kaphar](../../word-studies/H3722-kaphar.md) — kaphar verb, Piel dominance, ritual atonement
  - [H2891-taher](../../word-studies/H2891-taher.md) — taher verb, Qal/Piel/Hithpael stem distribution, purity system
  - [H5545-calach](../../word-studies/H5545-calach.md) — salach verb, Niphal divine-passive in sacrificial formula
- **Related passage analyses:**
  - [lev-16-20-22](lev-16-20-22.md) — live-goat ritual sequence after completed atonement
  - [lev-16-21-sin-terms](lev-16-21-sin-terms.md) — coordinated sin terms in confession formula
