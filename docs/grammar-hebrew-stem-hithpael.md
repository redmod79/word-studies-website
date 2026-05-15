# Hithpael Stem (Hebrew)

## Definition
The **Hithpael** (הִתְפַּעֵל) is the tD-stem in Hebrew, formed by prefixing הִתְ (*hit-*) to the Piel base and doubling the middle radical. It is the primary **reflexive-iterative** stem, expressing action the subject performs on, for, or within itself, often with habitual, reciprocal, or estimative nuance. It stands as the reflexive counterpart of the Piel, just as the Niphal can serve as the reflexive/passive counterpart of the Qal.

Core functions:

1. **Reflexive (direct)** — subject performs the Piel-type action on itself ("sanctify oneself," "hide oneself," "cover oneself")
2. **Reciprocal** — two or more subjects act on each other ("look at one another," "intermarry with each other")
3. **Iterative / habitual** — subject engages in repeated or ongoing action ("walk about," "turn this way and that")
4. **Middle voice / indirect reflexive** — subject acts in its own interest or experiences an internal state ("pray" = intercede for oneself, "mourn," "console oneself")
5. **Estimative / pretend** — subject shows oneself to be X or pretends to be X ("feign another," "make oneself sick")
6. **Denominative reflexive** — verb derived from noun, subject does the noun-action to itself ("act as a prophet" from נָבִיא)

## Form Recognition

### Morphological markers
- **Perfect:** *hitqaṭṭēl* (הִתְקַטֵּל) — הִתְ prefix + doubled middle radical: הִתְקַדִּשׁ "he sanctified himself," הִתְהַלֶּךְ "he walked about," הִתְנַבֵּא "he prophesied"
- **Imperfect:** *yitqaṭṭēl* (יִתְקַטֵּל) — prefix conjugation with -ת- infixed after preformative: יִתְקַדָּשׁ "he will sanctify himself," יִתְפַּלֵּל "he will pray"
- **Wayyiqtol:** *wayyitqaṭṭēl* — narrative past: וַיִּתְהַלֵּךְ "and he walked about" (Gen 5:22), וַיִּתְחַבֵּא "and he hid himself" (Gen 3:8)
- **Participle:** *mitqaṭṭēl* (מִתְקַטֵּל) — מִתְ prefix: מִתְהַלֵּךְ "walking about" (Gen 3:8), מִתְקַדְּשִׁים "those sanctifying themselves" (Isa 66:17)
- **Imperative:** *hitqaṭṭēl* (הִתְקַטֵּל) — same as perfect base: הִתְקַדְּשׁוּ "sanctify yourselves" (Lev 20:7), הִתְהַלֵּךְ "walk about" (Gen 13:17)
- **Infinitive Construct:** *hitqaṭṭēl* — with or without preposition: הִתְקַדֶּשׁ (Isa 30:29), לְהִתְפַּלֵּל "to pray" (1 Sam 1:12)

### Phonological adjustments (metathesis and assimilation)
- When the first root consonant is a sibilant (שׂ, שׁ, צ, ס, ז), the ת of the prefix **transposes** (metathesis) with the sibilant: הִשְׁתַּמֵּר (not *הִתְשַׁמֵּר), מִשְׁתָּאֵה (Gen 24:21 from שׁאה)
- With צ the ת additionally assimilates to ט: הִצְטַדֵּק (not *הִתְצַדֵּק)
- With ד/ט/ת the ת assimilates to the dental: הִטַּהֵר (Gen 35:2 from טהר, not *הִתְטַהֵּר)

### Parser code
`sp=verb vs=hit` — any Hithpael form
`sp=verb vs=hit vt=perf` — Hithpael Perfect
`sp=verb vs=hit vt=impf` — Hithpael Imperfect
`sp=verb vs=hit vt=wayq` — Hithpael Wayyiqtol
`sp=verb vs=hit vt=impv` — Hithpael Imperative
`sp=verb vs=hit vt=infc` — Hithpael Infinitive Construct

## Functions with Examples

### 1. Reflexive / Direct Reflexive (most common)
The subject performs the action on itself. This is the core Hithpael function and the reflexive counterpart of the Piel factitive.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Lev 11:44 | וְהִתְקַדִּשְׁתֶּם | Hithpael.Perf.2mp of קדשׁ | "ye shall therefore sanctify yourselves" |
| Lev 20:7 | וְהִתְקַדִּשְׁתֶּם | Hithpael.Perf.2mp of קדשׁ | "Sanctify yourselves therefore" |
| Josh 3:5 | הִתְקַדָּשׁוּ | Hithpael.Impv.2mp of קדשׁ | "Sanctify yourselves" |
| Num 11:18 | הִתְקַדְּשׁוּ | Hithpael.Impv.2mp of קדשׁ | "Sanctify yourselves against to morrow" |
| Gen 3:8 | וַיִּתְחַבֵּא | Hithpael.Wayq.3ms of חבא | "hid themselves" (Adam hid himself) |
| Gen 24:65 | וַתִּתְכָּס | Hithpael.Wayq.3fs of כסה | "she... covered herself" (Rebekah with a veil) |
| Gen 35:2 | הִטַּהֲרוּ | Hithpael.Impv.2mp of טהר | "be clean" (purify yourselves) |

**Key diagnostic:** When the Piel is transitive-factitive ("make holy," "make clean"), the Hithpael reflexivizes the action back onto the subject ("make oneself holy," "make oneself clean"). The Piel/Hithpael contrast is especially clear in 2 Chr 29:5: הִתְקַדְּשׁוּ (Hithpael Impv.2mp) "sanctify **yourselves**" + וְקַדְּשׁוּ (Piel Impv.2mp) "and sanctify **the house of YHWH**" — same root, same tense, same addressees, but the Hithpael is self-directed and the Piel is object-directed.

### 2. Reciprocal
Two or more subjects perform the action on each other. Rare but grammatically distinct.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Gen 42:1 | תִּתְרָאוּ | Hithpael.Impf.2mp of ראה | "Why do ye look one upon another?" |
| Gen 34:9 | הִתְחַתְּנוּ | Hithpael.Impv.2mp of חתן | "make ye marriages with us" (intermarry with each other) |
| Gen 26:20 | הִתְעַשְּׂקוּ | Hithpael.Perf.3p of עשׂק | "they strove" (contended with each other) |

(Waltke-O'Connor IBHS §26.2g notes reciprocal Hithpael is rare but attested.)

### 3. Iterative / Habitual
The subject engages in the action repeatedly, habitually, or with ongoing duration. This function links to the tD-stem's frequentative force in cognate Semitic languages.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Gen 3:8 | מִתְהַלֵּךְ | Hithpael.Ptcp.ms of הלך | "walking [about] in the garden" (habitual/ongoing walking) |
| Gen 5:22 | וַיִּתְהַלֵּךְ | Hithpael.Wayq.3ms of הלך | "Enoch walked with God" (ongoing habitual relationship) |
| Gen 6:9 | הִתְהַלֶּךְ | Hithpael.Perf.3ms of הלך | "Noah walked with God" (habitual conduct) |
| Gen 13:17 | הִתְהַלֵּךְ | Hithpael.Impv.2ms of הלך | "walk through the land" (traverse, walk about in all directions) |
| Gen 3:24 | מִתְהַפֶּכֶת | Hithpael.Ptcp.fs of הפך | "which turned every way" (flaming sword turning continuously) |

**Note on הלך Hithpael:** This is the paradigmatic iterative Hithpael (Lambdin cites it as the primary example). The Qal of הלך means "go/walk" (single action); the Hithpael means "walk about, conduct oneself, go to and fro" (habitual conduct). The theological idiom "walked with God" (Gen 5:22, 24; 6:9) uses the Hithpael specifically to denote an ongoing pattern of life, not a single walk.

### 4. Middle Voice / Indirect Reflexive
The subject acts in its own interest, undergoes an internal experience, or enters a state. The action affects the subject internally rather than on its external surface. This corresponds to what Greek grammarians call the "middle voice."

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Gen 20:7 | יִתְפַּלֵּל | Hithpael.Impf.3ms of פלל | "he shall pray for thee" (intercede — act on one's own behalf before God) |
| 1 Sam 1:12 | לְהִתְפַּלֵּל | Hithpael.InfCon of פלל | "as she continued praying" (ongoing self-directed petition) |
| Gen 37:34 | וַיִּתְאַבֵּל | Hithpael.Wayq.3ms of אבל | "and mourned for his son" (entered state of mourning) |
| Gen 6:6 | וַיִּתְעַצֵּב | Hithpael.Wayq.3ms of עצב | "and it grieved him at his heart" (internal emotional state) |
| Psa 119:52 | וָאֶתְנֶחָם | Hithpael.Wayq.1s of נחם | "and have comforted myself" (consoled oneself) |
| Gen 27:42 | מִתְנַחֵם | Hithpael.Ptcp.ms of נחם | "doth comfort himself, purposing to kill thee" (consoling himself [through planned revenge]) |

**Note on פלל Hithpael:** The root פלל does not occur in the Piel ("judge/intervene") with prayer meaning. The Hithpael "pray" (הִתְפַּלֵּל) is a middle-voice formation: the subject undertakes the act of intercession in his own interest or on behalf of another. This is the standard Hebrew word for prayer — over 80 occurrences, all Hithpael.

### 5. Estimative / Pretend / Show Oneself as X
The subject displays, presents, or pretends to be in a state. This function treats the Hithpael as "act the part of X" or "show oneself to be X."

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| 1 Ki 14:5 | מִתְנַכֵּרָה | Hithpael.Ptcp.fs of נכר | "she shall feign herself to be another woman" (pretend-another) |
| 2 Sam 13:5 | וְהִתְחָל | Hithpael.Impv.2ms of חלה | "make thyself sick" (pretend to be sick) |
| Gen 37:18 | וַיִּתְנַכְּלוּ | Hithpael.Wayq.3mp of נכל | "they conspired against him" (acted cunningly toward him) |
| Isa 65:5 | קְדַשְׁתִּיךָ | (Qal.Perf.1s — *not* Hithpael; contrast with Isa 66:17 Hithpael) | "I am holier than thou" (self-declaration of holiness) |

**Diagnostic:** The estimative Hithpael is identifiable when the subject cannot genuinely perform the action but rather displays or claims the quality. 2 Sam 13:5 is the classic example: Amnon was not actually ill — the Hithpael of חלה means "make oneself appear sick."

### 6. Denominative Reflexive
A verb derived from a noun, with the subject performing the noun-action reflexively or entering the noun-state.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Ezra 5:1 (Aram.) | הִתְנַבִּי | Hithpael.Perf.3ms of נבא | "prophesied" (acted-as-prophet, from נָבִיא) |
| Gen 34:9 | הִתְחַתְּנוּ | Hithpael.Impv.2mp of חתן | "make ye marriages" (act-as-חֹתֵן "in-law") |

## Qadash (קדשׁ H6942) Hithpael — Focal Case Study

The Hithpael of קדשׁ is the reflexive of the Piel factitive "make holy." It means **"sanctify oneself" / "prepare oneself as holy"** — the subject undertakes the action of holiness-preparation upon himself.

### All Stem Contrasts for קדשׁ

| Stem | Function | Example | Reference |
|------|----------|---------|-----------|
| **Qal** | Be holy (stative) | קָדֹושׁ אָנִי "I am holy" | Lev 11:44b |
| **Niphal** | Be sanctified / show oneself holy (passive/tolerative) | וְנִקְדַּשְׁתִּי בָכֶם "I will be sanctified among you" | Lev 22:32; Ezek 20:41 |
| **Piel** | Make holy / consecrate (transitive factitive) | קַדֵּשׁ אֶת הָעָם "sanctify the people" | Josh 7:13a; Exo 19:10 |
| **Hiphil** | Devote / set apart as holy (causative) | לְהַקְדִּישׁ לַיהוָה "to sanctify unto YHWH" | 2 Chr 30:17b |
| **Hithpael** | Sanctify oneself (reflexive) | הִתְקַדְּשׁוּ "sanctify yourselves" | Lev 20:7; Josh 3:5 |

### Piel vs. Hithpael Diagnostic in Context

The distinction between Piel and Hithpael of קדשׁ is most clearly visible when both appear in the same passage:

- **Josh 7:13:** קַדֵּשׁ אֶת הָעָם (Piel.Impv.2ms) "sanctify the people" — Joshua acts as agent, people are the object. Then: הִתְקַדְּשׁוּ לְמָחָר (Hithpael.Impv.2mp) "sanctify **yourselves** against to morrow" — the people themselves are now both agent and patient.
- **2 Chr 29:5:** הִתְקַדְּשׁוּ (Hithpael.Impv.2mp) "sanctify **yourselves**" addressed to the Levites personally, followed by וְקַדְּשׁוּ אֶת בֵּית יְהוָה (Piel.Impv.2mp) "and sanctify **the house of YHWH**" — the same addressees first apply holiness to themselves, then apply it to the temple.
- **1 Sam 16:5:** הִתְקַדְּשׁוּ (Hithpael.Impv.2mp) "sanctify yourselves" — Samuel commands the people to prepare themselves, then: וַיְקַדֵּשׁ אֶת יִשַׁי (Piel.Wayq.3ms) "and he [Samuel] sanctified Jesse" — the external agent performs the consecration on another.

### Theological Significance: When God Uses the Hithpael of קדשׁ

In Ezek 38:23, YHWH uses the Hithpael of קדשׁ with himself as subject: וְהִתְקַדִּשְׁתִּי (Hithpael.Perf.1s) "and [I will] sanctify myself." Since God cannot be acted upon by an external agent for sanctification, this is not a direct reflexive in the physical sense. Rather, it is a **demonstrative/middle-voice Hithpael**: God will **show himself to be holy** / **manifest his holiness** in the sight of the nations. The parallel with Niphal וְנִקְדַּשְׁתִּי (Lev 22:32; Ezek 20:41; 28:25; 36:23) — "I will be sanctified / I will show myself holy" — confirms that both stems can express the tolerative/demonstrative function when the subject is YHWH, though the Hithpael emphasizes the subject's initiative and the Niphal emphasizes the passive reception of the action.

### Qadash Hithpael Inventory (parser-verified)

| Reference | Form | Parsing | KJV |
|-----------|------|---------|-----|
| Exo 19:22 | יִתְקַדָּשׁוּ | Hithpael.Impf.3mp | "let the priests... sanctify themselves" |
| Lev 11:44 | וְהִתְקַדִּשְׁתֶּם | Hithpael.Perf.2mp | "ye shall therefore sanctify yourselves" |
| Lev 20:7 | וְהִתְקַדִּשְׁתֶּם | Hithpael.Perf.2mp | "Sanctify yourselves therefore, and be ye holy" |
| Num 11:18 | הִתְקַדְּשׁוּ | Hithpael.Impv.2mp | "Sanctify yourselves against to morrow" |
| Josh 3:5 | הִתְקַדָּשׁוּ | Hithpael.Impv.2mp | "Sanctify yourselves: for to morrow the LORD will do wonders" |
| Josh 7:13 | הִתְקַדְּשׁוּ | Hithpael.Impv.2mp | "Sanctify yourselves against to morrow" |
| 1 Sam 16:5 | הִתְקַדְּשׁוּ | Hithpael.Impv.2mp | "sanctify yourselves, and come with me to the sacrifice" |
| Isa 30:29 | הִתְקַדֶּשׁ | Hithpael.InfCon.Cst | "as in the night when a holy solemnity is kept" (lit. "night of self-sanctifying a feast") |
| Isa 66:17 | הַמִּתְקַדְּשִׁים | Hithpael.Ptcp.mp | "They that sanctify themselves... in the gardens" |
| Ezek 38:23 | וְהִתְקַדִּשְׁתִּי | Hithpael.Perf.1s | "and [I will] sanctify myself" (YHWH as subject) |
| 2 Chr 29:5 | הִתְקַדְּשׁוּ | Hithpael.Impv.2mp | "sanctify now yourselves" |
| 2 Chr 29:34 | הִתְקַדָּשׁוּ (2x) | Hithpael.Perf.3p | "had sanctified themselves... to sanctify themselves" |
| 2 Chr 30:17 | הִתְקַדָּשׁוּ | Hithpael.Perf.3p | "that were not sanctified" (had not sanctified themselves) |

**Semantic range:** The Hithpael of קדשׁ consistently means "prepare/sanctify **oneself**" through ceremonial purification in preparation for encountering YHWH. The reflexive force is never passive ("was sanctified by another") but always self-directed — the subject takes responsibility for his own state of holiness. The Isa 66:17 occurrence is ironic/negative: the subjects "sanctify themselves" in pagan garden rites, applying the reflexive form to a false sanctification.

## Common Hithpael Verbs

| Root | Gloss in Hithpael | Function | Key References |
|------|--------------------|----------|----------------|
| הלך (*halak*) | walk about, conduct oneself | Iterative | Gen 3:8; 5:22; 6:9; 13:17; 17:1; 24:40 |
| פלל (*palal*) | pray, intercede | Middle voice | Gen 20:7, 17; 1 Sam 1:12; 2:1; 1 Ki 8:28 |
| קדשׁ (*qadash*) | sanctify oneself | Direct reflexive | Lev 11:44; 20:7; Josh 3:5; 2 Chr 29:5 |
| נחם (*nacham*) | comfort oneself, console oneself | Middle voice | Gen 27:42; 37:35; Psa 119:52 |
| חבא (*chaba*) | hide oneself | Direct reflexive | Gen 3:8; Josh 10:16 |
| אבל (*abal*) | mourn | Middle voice | Gen 37:34; 2 Sam 14:2 |
| ברך (*barak*) | bless oneself / be blessed (in someone) | Indirect reflexive | Gen 22:18; 26:4 |
| נכר (*nakar*) | disguise oneself, feign to be another | Estimative/pretend | 1 Ki 14:5; 22:30 |
| חלה (*chalah*) | make oneself sick | Estimative/pretend | 2 Sam 13:5, 6 |
| טהר (*taher*) | purify oneself | Direct reflexive | Gen 35:2; 2 Chr 30:18 |
| עצב (*atsab*) | grieve, be grieved | Middle voice | Gen 6:6; 34:7 |
| נבא (*naba*) | prophesy, act as prophet | Denominative | 1 Sam 10:6; Jer 14:14 |
| ראה (*ra'ah*) | look at one another | Reciprocal | Gen 42:1 |

## Contrast with Other Reflexive/Passive Stems

| Stem | Type | Function | Example with קדשׁ |
|------|------|----------|-------------------|
| **Niphal** | Simple passive/reflexive | Subject receives action or allows action upon self | נִקְדַּשְׁתִּי "I will be sanctified [among you]" (Lev 22:32) |
| **Piel** | Intensive factitive | Subject makes object enter a state | קַדֵּשׁ אֶת הָעָם "sanctify the people" (Josh 7:13) |
| **Pual** | Intensive passive | Subject receives intensified action | מְקֻדָּשׁ "sanctified" (passive of Piel) |
| **Hiphil** | Causative | Subject causes object to be holy | לְהַקְדִּישׁ לַיהוָה "to consecrate to YHWH" (2 Chr 30:17) |
| **Hithpael** | Reflexive/iterative | Subject acts on self, habitually | הִתְקַדְּשׁוּ "sanctify yourselves" (Lev 20:7) |

**Niphal vs. Hithpael reflexive:** Both stems can express reflexive action, but they differ in nuance. The Niphal reflexive tends toward the tolerative ("allows oneself to be X") while the Hithpael reflexive is volitional and self-directed ("makes oneself X"). Compare Niphal נִקְדַּשְׁתִּי (Ezek 20:41) "I will be sanctified / show myself holy" (allowing the action to be recognized) with Hithpael וְהִתְקַדִּשְׁתִּי (Ezek 38:23) "I will sanctify myself" (actively demonstrating holiness). The distinction is agency and initiative.

## Grammar Reference Citations

- **GKC §54:** The Hithpael (reflexive of Piel); formation by prefixing הִתְ + doubling of middle radical; metathesis and assimilation with sibilants and dentals
- **Waltke-O'Connor IBHS §26:** Hithpael stem — §26.2 functions (reflexive, reciprocal, iterative, estimative, passive); §26.1.2 comparative Semitic tD-stem proposals; §26.1.3 distribution
- **Joüon-Muraoka §53:** Hithpael conjugation; reflexive and reciprocal functions; denominative Hithpael
- **Futato, Lesson 39:** Hithpael as the seventh major verb pattern; reflexive and reciprocal meanings; phonological adjustments for sibilants
- **Barrick & Busenitz (BHSG):** Hithpael represents reflexive and reciprocal actions; distinguished by הִתְ prefix and doubled middle radical

---
*Generated from: hebrew_parser.py --search "sp=verb vs=hit", hebrew_parser.py --verse (multiple), semantic_grammar.py (Waltke-O'Connor, Futato, GKC, BHSG, BDB searches), KJV text*
*Parser-verified: Gen 3:8; 5:22; 6:6; 13:17; 17:1; 20:7; 24:65; 25:22; 27:42; 34:9; 35:2; 37:18; 37:34; 42:1; Exo 19:22; Lev 11:44; 20:7; Num 11:18; Josh 3:5; 7:13; 1 Sam 1:12; 16:5; 2 Sam 13:5; 1 Ki 14:5; Isa 30:29; 66:17; Ezek 38:23; Psa 119:52; 2 Chr 29:5; 29:34; 30:17*
*Last updated: 2026-05-08*
