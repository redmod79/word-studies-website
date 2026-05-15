# Hiphil Stem (Hebrew)

## Definition
The **Hiphil** (הִפְעִיל) is the H-stem of the Hebrew verb — the primary **causative** stem. It is formed by prefixing he (ה) to the root and adds an external causer to the Qal action: what Qal says "happens," Hiphil says "is made to happen." It is the workhorse stem for nearly every Hebrew conquest, creation, and covenant-transfer verb ("smite," "devote," "destroy," "dispossess," "bring," "raise up," "beget").

Core functions:

1. **Causative-factitive** — subject causes the object to do or become the Qal action ("cause to ride," "raise up," "bring [= cause to come]")
2. **Productive / internal causative** — subject produces or enters a state ("bring forth," "multiply," "rain down")
3. **Declarative / estimative** — subject declares or treats the object as X ("pronounce righteous," "declare guilty")
4. **Denominative** — derives verbs from nouns ("give ear [listen]," "give rain," "yield fruit")

For the yiqtol conjugation specifically, see [hiphil-imperfect.md](hiphil-imperfect.md).

## Form Recognition

### Morphological markers
- **Perfect:** *hiqṭîl* (הִקְטִיל) — he-prefix with hiriq, long *î* theme vowel: הִכָּה "he smote," הֶחֱרִים "he devoted," הֶאֱבִיד "he destroyed"
- **Imperfect:** *yaqṭîl* (יַקְטִיל) — preformative vowel *a* (patach), ה elides: יַכֶּה "he will smite," יוֹרִישׁ "he will dispossess"
- **Wayyiqtol:** *wayyaqṭēl* — shortened theme vowel: וַיַּךְ "and he smote" (Exo 2:12), וַיַּכֵּם "and he smote them" (Gen 14:15)
- **Participle:** *maqṭîl* (מַקְטִיל) — mem-prefix: מַבְדִּיל "separating" (Gen 1:6), מַכֶּה "striker" (Gen 36:35, Exo 2:11)
- **Infinitive Construct:** *haqṭîl* (הַקְטִיל): הַכּוֹת "to strike" (Gen 4:15, 8:21), הַבְדִּיל "to separate" (Gen 1:14)
- **Infinitive Absolute:** *haqṭēl*: הַרְבָּה "multiplying" (Gen 3:16)
- **Imperative:** *haqṭēl*: הַאְזֵנָּה "give ear!" (Gen 4:23)

### Diagnostic features
- Long *î* (hiriq-yod) theme vowel in the "default" form (hence the stem name *hiphīl*)
- *a*-class preformative vowel in the Imperfect (יַ־, תַּ־, אַ־, נַ־) — contrasts with Qal's *i*-class (יִ־, תִּ־)
- He-prefix visible in Perfect, Infinitive, Imperative (but not Imperfect or Participle)

### Parser code
`sp=verb vs=hif` — any Hiphil form
`sp=verb vs=hif vt=perf` — Hiphil Perfect (*hiqṭîl*)
`sp=verb vs=hif vt=impf` — Hiphil Imperfect (*yaqṭîl*)
`sp=verb vs=hif vt=wayq` — Hiphil Wayyiqtol narrative past

## Functions with Examples

### 1. Causative-factitive (primary function)
The subject causes the object to perform the Qal action. An external agent enters the verbal frame.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Gen 14:15 | וַיַּכֵּם | Hiphil.Wayq.3ms+3mp of נכה | "and smote them" (*caused the stroke to fall on them*) |
| Gen 19:11 | הִכּוּ | Hiphil.Perf.3p of נכה | "they smote the men... with blindness" |
| Exo 2:12 | וַיַּךְ | Hiphil.Wayq.3ms of נכה | "and slew [smote] the Egyptian" |
| Gen 2:19 | וַיָּבֵא | Hiphil.Wayq.3ms of בוא | "and brought them" (*caused them to come*) |
| Gen 41:43 | וַיַּרְכֵּב | Hiphil.Wayq.3ms of רכב | "he made him to ride" |
| Deut 18:15 | יָקִים | Hiphil.Impf.3ms of קום | "the LORD... shall raise up [a prophet]" |

### 2. Conquest verbs — the causative grammar of Joshua/Deuteronomy
Nearly every divine-war verb in the conquest narratives is Hiphil. The stem itself encodes that YHWH "causes the destruction" through Israel as the instrumental agent.

| Reference | Hebrew | Parsing | KJV | Root meaning (Qal) |
|-----------|--------|---------|-----|--------------------|
| Deut 7:2 | וְהִכִּיתָם / הַחֲרֵם תַּחֲרִים | Hiphil.Perf.2ms+3mp of נכה; Hiphil.InfAbs + Hiphil.Impf.2ms of חרם | "thou shalt smite them... utterly destroy [devote] them" | — / חרם Hiphil gloss = "consecrate [to destruction], ban" |
| Deut 9:3 | יַשְׁמִידֵם... וְהֹורַשְׁתָּם | Hiphil.Impf.3ms+3mp of שׁמד; Hiphil.Perf.2ms+3mp of ירשׁ | "he shall destroy them... thou shalt drive them out" | שׁמד Qal unattested; ירשׁ Qal = "possess" |
| Jos 10:40 | הֶחֱרִים | Hiphil.Perf.3ms of חרם | "utterly destroyed all that breathed" | — |
| Jos 11:12 | וַיַּכֵּם... הֶחֱרִים | Hiphil.Wayq+Perf of נכה/חרם | "smote them... utterly destroyed them" | — |
| Deut 11:23 | וְהוֹרִישׁ | Hiphil.Perf.3ms of ירשׁ | "the LORD drive out all these nations" | ירשׁ Qal = "take possession" |
| Exo 34:24 | אוֹרִישׁ | Hiphil.Impf.1s of ירשׁ | "I will cast out the nations" | same — Hiphil inverts to "dispossess" |
| 1 Sam 15:3 | וְהַחֲרַמְתֶּם | Hiphil.Perf.2mp+cons of חרם | "utterly destroy all that they have" | — |

**Grammatical point.** The Qal of ירשׁ means "to take possession, inherit"; the Hiphil reverses the frame — "to cause [them] to lose possession" = "dispossess, drive out." This is a textbook Hiphil inversion: *yāraš* "possess" → *hôrîš* "cause-not-to-possess." The same pattern appears with ילד Qal "be born" → Hiphil "beget." The conquest verbs require the Hiphil precisely because the action is performed *on* someone by an external causer.

### 3. Productive / internal causative
The subject produces or enters a state; often renders as an intransitive English verb.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Gen 1:11 | תַּדְשֵׁא | Hiphil.Impf.3fs of דשׁא | "let the earth bring forth grass" |
| Gen 1:12 | תּוֹצֵא | Hiphil.Wayq.3fs of יצא | "the earth brought forth" (caused-to-go-out) |
| Gen 2:5 | הִמְטִיר | Hiphil.Perf.3ms of מטר | "the LORD God had... caused it to rain" |
| Gen 3:16 | אַרְבֶּה | Hiphil.Impf.1s of רבה | "I will greatly multiply thy sorrow" |
| Gen 1:15, 17 | הָאִיר | Hiphil.InfCon of אור | "to give light" (cause to be light) |

### 4. Declarative / estimative
The subject does not perform the action but pronounces the object to possess the quality.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| 1 Kgs 8:32 | הַרְשִׁיעַ / הַצְדִּיק | Hiphil.InfCon of רשׁע / צדק | "condemning... justifying" (*declare* guilty / righteous) |
| Gen 3:11 | הִגִּיד | Hiphil.Perf.3ms of נגד | "[who] told thee" (caused [it] to be set before) |

### 5. Denominative (verb from noun)
| Reference | Hebrew | Parsing | Gloss |
|-----------|--------|---------|-----|
| Gen 4:23 | הַאְזֵנָּה | Hiphil.Impv.2fp of אזן | "give ear!" (from אֹזֶן "ear") |
| Gen 2:5 | הִמְטִיר | Hiphil.Perf.3ms of מטר | "send rain" (from מָטָר "rain") |

## Contrast with Qal and Piel

The three stems most often confused are Qal (base), Piel (intensive/factitive), and Hiphil (causative). Only Qal is semantically "basic"; Piel and Hiphil both involve second-party effects but along different axes.

| Stem | Semantic axis | Typical gloss | Example root | Qal → Stem |
|------|---------------|---------------|--------------|------------|
| **Qal** | Basic action, subject performs | "do X" | קום | *qām* "he arose" |
| **Piel** | Factitive — brings about a **state** or result; intensifies result; plural/iterative action | "make X into Y" | קדשׁ | Qal "be holy" → Piel *qiddēš* "consecrate, sanctify" |
| **Hiphil** | Causative — introduces an external **causer** of the action | "cause to do X" | קום | Qal "arise" → Hiphil *hēqîm* "raise up, erect" |

### Worked contrasts

| Root | Qal | Piel | Hiphil |
|------|-----|------|--------|
| בוא | *bāʾ* "he came" | (rare) | *hēbîʾ* "he brought" (caused to come) |
| קום | *qām* "he arose / stood" | *qiyyēm* "he confirmed, fulfilled" (bring to realization) | *hēqîm* "he raised up, erected" |
| ילד | *yālad* "she bore" | *yillēd* "she assisted in birth [midwife]" | *hôlîd* "he begat, sired" |
| שׁוב | *šāb* "he returned" | *šiwwēb* "he brought back [poetic]" | *hēšîb* "he restored, brought back" |
| מלא | *mālēʾ* "he was full" | *millēʾ* "he filled [it]" (make full) | *himlîʾ* "he caused [it] to be full" |
| ראה | *rāʾāh* "he saw" | — | *herʾāh* "he showed" (caused to see) |
| גדל | *gādal* "he grew great" | *giddēl* "he raised [a child], brought up" (make-great) | *higdîl* "he magnified, made great" |
| ידע | *yādaʿ* "he knew" | — | *hôdîaʿ* "he made known, informed" |

**The Piel/Hiphil overlap.** Piel and Hiphil both introduce causation, but Piel focuses on **bringing about a state in the object** (result-oriented: "make full," "make holy," "make great"), while Hiphil focuses on **causing the object to perform the Qal action** (process-oriented: "cause to come," "cause to arise"). With verbs of *becoming* both are possible and the language often uses only one. With verbs of *action* (come, go, ride, eat, see, know) Hiphil is the standard causative and Piel is unattested or rare.

## Contrast with Other Stems

| Stem | Function | Example | Link |
|------|----------|---------|------|
| **Qal** | Basic G-stem | קָם "he arose" | — |
| **Niphal** | Simple passive / reflexive | נִכְרַת "he was cut off" | [stem-niphal.md](stem-niphal.md) |
| **Piel** | Factitive / intensive / resultative | קִדֵּשׁ "he consecrated" | — |
| **Pual** | Passive of Piel | קֻדַּשׁ "he was consecrated" | — |
| **Hiphil** | Active causative | הֵקִים "he raised up" | *(this entry)* |
| **Hophal** | Passive of Hiphil ("be caused to do") | הוּקַם "he was raised up" | — |
| **Hithpael** | Reflexive / iterative | הִתְקַדֵּשׁ "he sanctified himself" | — |

Hiphil and Hophal form a voice pair: Hiphil is the active causative, Hophal the passive of the same ("be made to arise," "be brought"). Niphal and Pual handle other passive relations (simple and intensive respectively).

## Common Hiphil Verbs in Conquest / Warfare Vocabulary

| Verb root | Qal meaning | Hiphil meaning | Representative reference |
|-----------|-------------|----------------|--------------------------|
| נכה (nakah) | *(Qal rare)* | **smite, strike, kill** (*hikkāh*) | Deut 7:2; Jos 11:12; 1 Sam 15:3 |
| חרם (charam) | *(denom. of חֵרֶם)* | **devote to destruction, utterly destroy** (*heḥĕrîm*) | Deut 7:2; Jos 10:40; 1 Sam 15:3 |
| שׁמד (shamad) | *(unattested)* | **destroy, exterminate** (*hišmîd*) | Deut 9:3 |
| אבד (avad) | "perish" | **destroy, cause to perish** (*heʾĕbîd*) | Deut 11:4; 2 Kgs 21:3 |
| ירשׁ (yarash) | "possess, inherit" | **dispossess, drive out** (*hôrîš*) | Deut 11:23; Exo 34:24 |
| נוס (nus) → נוּס | "flee" | *hēnîs* "put to flight" (rare) | Judg 20:32 |
| גרשׁ (garash) | "drive out" (Piel primarily) | — | *(Piel carries this sense)* |
| בוא (bo) | "come" | **bring [in]** | Deut 7:1; Jos 23:9 |
| קום (qum) | "arise" | **raise up** (a prophet, king, enemy) | Deut 18:15; 1 Kgs 14:10 |
| שׁוב (shub) | "return" | **bring back, restore** | 1 Kgs 13:6 |

**Other common Hiphils (non-warfare).** בדל (Hiphil only) "separate, divide" (Gen 1:4, 7); זרע "sow" (Gen 1:11 Hiphil "yield seed"); ילד "beget" (Hiphil); נגד "tell, declare" (Hiphil only); ידע "make known" (Hiphil); אור "give light" (Hiphil); מטר "send rain" (Hiphil, Gen 2:5); רבה "multiply" (Hiphil Gen 3:16, 22:17).

## Why conquest narratives are saturated with Hiphils

The theological point embedded in the grammar: Joshua and Deuteronomy rarely use Qal verbs for the destruction of the Canaanites. The verbs are almost uniformly Hiphil. This is not stylistic — the Hiphil stem *requires* an external causer. In Deut 7:2 the surface subject is "you" (Israel), but the grammar marks Israel as the instrumental agent of a causation whose ultimate source is named in the preceding clause: "when the LORD thy God shall deliver them before thee." Similarly Deut 9:3 names YHWH as the one who *yašmîdēm* "will destroy them"; Israel's *wəhôraštām* "thou shalt dispossess them" is the Hiphil executed through the human instrument. The conquest is grammatically a **Hiphil event**: YHWH is the causer, Israel the means.

## Grammar Citations

- **GKC §53** — Hiphil conjugation, meaning, paradigm
- **Joüon-Muraoka §54** — Hiphil as causative H-stem
- **Waltke-O'Connor (IBHS) §27** — The Causative Stems: Hiphil and Hophal (pp. 433–452); §27.2 on causative-factitive, declarative-estimative, denominative
- **van der Merwe-Naudé-Kroeze §16.5** — Hiphil functions with examples
- **Jenni, *Das hebräische Piʿel* (1968)** — classic work distinguishing Piel's factitive focus from Hiphil's causative focus
- **BDB / HALOT** s.v. נכה, חרם, שׁמד, ירשׁ — verbs attested almost exclusively in Hiphil

---
*Generated from: hebrew_parser.py --search "sp=verb vs=hif" (40+ results), --lemma "נכה" (15 results), KJV text for conquest verses (Deut 7:2, 9:3; Jos 10:40, 11:12; 1 Sam 15:3; Exo 34:24)*
*Last updated: 2026-04-18*
