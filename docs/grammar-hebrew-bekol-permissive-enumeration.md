# Bet-Prefix + *Kol* + *ʾăšer* + Verb — Permissive Enumeration Construction (Hebrew)

## Definition
The fixed phrase **בְּ + כֹל + אֲשֶׁר + finite verb** — literally "in/for all-that (which) [verb]" — is a syntactic slot that converts an *open-ended* relative clause into a nominal PP adjunct modifying an imperatival/volitive main verb. The bet is not merely locative but **specifying/distributive** ("in the sphere of," "for the range of," "pertaining to"); *kōl* (const.) universalizes the relative's reference; *ʾăšer* heads a headless/free relative clause whose verb is typically a 2ms/3fs *yiqtol* of desire, movement, or seeking. When the matrix verb is imperatival (imperative, 2ms *yiqtol* of command, or *weqatal* of legal obligation), the whole PP functions as a **permissive enumeration** — authorizing the addressee's action across the full range opened by the embedded verb.

1. **Permissive-enumerative (with volitive/imperatival matrix)** — "for whatsoever X desires/asks/chooses"; grants covenant-addressee discretion within the law (Deut 12:15, 12:20–21, 14:26).
2. **Locative-universal (with verbs of going/turning)** — "wheresoever X goes/turns"; open-ended spatial quantification (Josh 1:7; 1 Sam 14:47; 1 Ki 2:3 construct variant).
3. **Descriptive-totalizing (with verbs of doing)** — "in everything X does"; summative, not permissive (Gen 39:3 without בְּ; 1 Ki 2:3 with אֵת instead of בְּ).

## Form Recognition
- Prefixed particle: **בְּ** (rarely בַּ־; with waw וּבְ־) — glossed "in" by parser; here marks *sphere/range*, not location.
- Universal quantifier: **כֹל** in construct state (`Noun.ms.Cst`) — never absolute, because אֲשֶׁר-clause is its *nomen rectum*.
- Relative: **אֲשֶׁר** (`Conj.`) tagged `<relative>` by parser; here headless — antecedent is the *content* of the embedded verb.
- Embedded verb: **prefix conjugation** (`Verb.*.Impf.*`), almost always 2ms / 3fs (subject = the soul / the addressee's desire), sometimes with pronominal object suffix.
- Maqqef: אֲשֶׁר frequently joined by maqqef to the following verb (אֲשֶׁר־תְּאַוֶּה) — diagnostic of tight binding.
- **Parser signature:** sequence `Prep(ב) + Noun.ms.Cst(כל) + Conj(אשר) + Verb.*.Impf.*`

## Morpheme-by-Morpheme Analysis (Deut 14:26 pivot)

**בְּכֹל֩ אֲשֶׁר־תְּאַוֶּ֨ה נַפְשְׁךָ֜**

| Morpheme | Form | Parsing | Function |
|----------|------|---------|----------|
| בְּ | ב | Prep | specifying/sphere-marker ("pertaining to") — *not* locative |
| כֹל | כל | Noun.ms.Cst | universal quantifier, construct-bound to the אֲשֶׁר-clause |
| אֲשֶׁר | אשׁר | Conj. `<relative>` | headless relative introducing the content-range |
| תְּאַוֶּה | אוה | Verb.Piel.Impf.3fs | embedded verb of desire — subject is נֶפֶשׁ |
| נַפְשְׁךָ | נפשׁ + 2ms | Noun.fs.Abs.+2ms | subject of embedded verb; the 2ms suffix ties the construction to the addressee |

The construct-chain logic is: **[sphere-marker] [all] [of-what] [your-soul-craves]** → "for-the-full-range-of-what-your-soul-craves." The matrix verb וְנָתַתָּה ("and thou shalt give/bestow," weqatal as legal-imperatival — see [weqatal-legal-imperatival](weqatal-legal-imperatival.md)) governs the silver-PP (הַכֶּסֶף) and receives the בְּכֹל־אֲשֶׁר PP as a *specification of disposition*. The addressee is commanded to spend the tithe-money, and the בְּכֹל־אֲשֶׁר clause defines the legally permitted object-domain.

## Functions with Examples

### 1. Permissive-Enumerative (imperatival matrix)

| Reference | Hebrew | Matrix Verb | KJV |
|-----------|--------|-------------|-----|
| Deut 14:26 | וְנָתַתָּה הַכֶּסֶף **בְּכֹל אֲשֶׁר־תְּאַוֶּה** נַפְשְׁךָ … **וּבְכֹל אֲשֶׁר** תִּשְׁאָלְךָ נַפְשֶׁךָ | וְנָתַתָּה Qal.Perf.2ms (*weqatal*-legal) | "thou shalt bestow that money for **whatsoever thy soul lusteth after** … or for **whatsoever thy soul desireth**" |
| Deut 12:20 | **בְּכָל־אַוַּת נַפְשְׁךָ** תֹּאכַל בָּשָׂר | תֹּאכַל Qal.Impf.2ms (permissive yiqtol) | "thou mayest eat flesh, **whatsoever thy soul lusteth after**" |
| Deut 12:21 | וְאָכַלְתָּ … **בְּכֹל אַוַּת נַפְשֶׁךָ** | וְאָכַלְתָּ Qal.Perf.2ms (*weqatal*-legal) | "and thou shalt eat … **whatsoever thy soul lusteth after**" |
| Deut 12:15 | **בְּכָל־אַוַּת נַפְשְׁךָ** תִּזְבַּח | תִּזְבַּח Qal.Impf.2ms (permissive yiqtol) | "thou mayest kill … **whatsoever thy soul lusteth after**" |

**Note on the Deut 12 variant:** 12:15, 12:20, 12:21 substitute the cognate noun **אַוַּת** (Noun.fs.Cst, from √אוה) for the finite-verb relative clause. Same semantic slot — אֲשֶׁר־תְּאַוֶּה ("that which [the soul] craves," Piel Impf.) is compressed into the construct noun אַוַּת נַפְשׁ ("craving-of soul"). Deut 14:26 is the *syntactically fullest* member of the set, where the relative clause is unfolded. The entire Deut 12–14 food-law paragraph thus contains **four iterations** of the same permissive frame, with 14:26 as the expanded climax.

### 2. Locative-Universal (verb-of-motion matrix)

| Reference | Hebrew | Embedded Verb | KJV |
|-----------|--------|---------------|-----|
| Josh 1:7 | תַּשְׂכִּיל **בְּכֹל אֲשֶׁר תֵּלֵךְ** | תֵּלֵךְ Qal.Impf.2ms (הלך) | "that thou mayest prosper **whithersoever thou goest**" |
| 1 Sam 14:47 | **וּבְכֹל אֲשֶׁר־יִפְנֶה** יַרְשִׁיעַ | יִפְנֶה Qal.Impf.3ms (פנה) | "**whithersoever he turned himself**, he vexed them" |

Same morphological skeleton (בְּ + כֹל + אֲשֶׁר + *yiqtol*), but because the embedded verb is motion/direction rather than desire, the universalized range is *spatial* ("wherever") rather than *object-of-desire* ("whatsoever"). The matrix verb is not necessarily imperatival in 1 Sam 14:47 (narrative Hiphil imperfect יַרְשִׁיעַ).

### 3. Descriptive-Totalizing (contrast — *not* permissive)

| Reference | Hebrew | Parsing note | KJV |
|-----------|--------|--------------|-----|
| Gen 39:3 | **וְכֹל אֲשֶׁר־הוּא עֹשֶׂה** יְהוָה מַצְלִיחַ | no בְּ prefix; כֹל is subject, not specification | "the LORD made **all that he did** to prosper" |
| 1 Ki 2:3 | תַּשְׂכִּיל **אֵת כָּל־אֲשֶׁר תַּעֲשֶׂה** וְאֵת כָּל־אֲשֶׁר תִּפְנֶה | direct-object marker אֵת, not בְּ | "thou mayest prosper **in all that thou doest, and whithersoever thou turnest**" (KJV "in" is supplied; MT has אֵת) |

In Gen 39:3 the כֹל אֲשֶׁר clause is the *subject* of a divine-causing Hiphil (מַצְלִיחַ) — totalizing but not permissive. In 1 Ki 2:3 the construction uses the direct-object marker **אֵת** instead of בְּ, marking the relative clause as a *direct object* of Hiphil תַּשְׂכִּיל ("prosper in/cause to understand"). The KJV's "in all that thou doest" adds a preposition not in the Hebrew; the construction is syntactically distinct from the Deut 12–14 permissive frame.

## Contrast with Related Forms

| Form | Function | Example |
|------|----------|---------|
| **בְּכֹל אֲשֶׁר + *yiqtol*** (this entry) | permissive/locative universal specification | Deut 14:26; Josh 1:7 |
| **בְּכָל־אַוַּת נַפְשׁ** | compressed construct variant (noun for rel.-clause) | Deut 12:15, 12:20, 12:21 |
| **אֵת כָּל־אֲשֶׁר + *yiqtol*** | direct-object universal; not specification | 1 Ki 2:3 |
| **כֹל אֲשֶׁר + finite verb** (no prep) | headless relative as subject/predicate nominal | Gen 39:3 |
| **כְּכֹל אֲשֶׁר + finite verb** | comparative "according to all that" | Josh 1:7a כְּכָל־הַתֹּורָה אֲשֶׁר |
| **אִישׁ כָּל־הַיָּשָׁר בְּעֵינָיו** | permissive idiom without כֹל אֲשֶׁר | Deut 12:8; Judg 17:6; 21:25 |

The Deuteronomic permissive-enumeration slot is one of several grammatical *devices for extending an imperatival verb over an open range*. It is distinguished by:
- the **בְּ**-prefix (specification, not object-marking, not subject-position),
- the **headless relative** (אֲשֶׁר without a nominal head — contrast construct-chain אַוַּת נַפְשׁ),
- **matrix-verb volitivity** (imperative, permissive *yiqtol*, or *weqatal*-legal — see [weqatal-legal-imperatival](weqatal-legal-imperatival.md)).

When all three features coincide, the PP grants the addressee discretionary latitude within the legal frame.

## Common Embedded Verbs in This Slot

| Verb | Strong's | Stem/Tense | Semantic class | Example |
|------|----------|------------|----------------|---------|
| אוה | H183 | Piel.Impf.3fs | desire | Deut 14:26 תְּאַוֶּה |
| שׁאל | H7592 | Qal.Impf.3fs.+2ms | ask/request | Deut 14:26 תִּשְׁאָלְךָ |
| הלך | H1980 | Qal.Impf.2ms | go/walk | Josh 1:7 תֵּלֵךְ |
| פנה | H6437 | Qal.Impf.3ms | turn | 1 Sam 14:47 יִפְנֶה |
| עשׂה | H6213 | Qal.Impf.2ms | do (descriptive variant with אֵת) | 1 Ki 2:3 תַּעֲשֶׂה |

## Cross-References
- [weqatal-legal-imperatival](weqatal-legal-imperatival.md) — the matrix-verb form (Deut 14:26 וְנָתַתָּה, וְאָכַלְתָּ) that carries the imperatival force the PP modifies.
- [imperative-mood](imperative-mood.md) — when the matrix verb is a true imperative (e.g., Josh 1:7 חֲזַק וֶאֱמַץ).
- [qal-imperfect](qal-imperfect.md) — permissive/modal *yiqtol* (Deut 12:15 תִּזְבַּח, 12:20 תֹּאכַל).

---
*Generated from: hebrew_parser.py --verse (Deut 14:26; 12:15; 12:20; 12:21; Josh 1:7; 1 Sam 14:47; 1 Ki 2:3; Gen 39:3)*
*Last updated: 2026-04-19*
