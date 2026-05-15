# Hebrew Imperative Mood — Divine Command (2mp Direct Address & לֹא + Impf Prohibition)

## Definition

The **Hebrew imperative** (*ṣiwwûy*; ETCBC tag `vt=impv`) is the dedicated volitive verb-form used only in the **second person** (ms, fs, mp, fp), only in the **positive**, and only for the **addressee-now** (Waltke-O'Connor §34.4; GKC §110). Because the imperative has no negative counterpart in Biblical Hebrew, every **"thou shalt not"** command is morphologically a different form — either **לֹא + imperfect** (categorical / permanent prohibition) or **אַל + imperfect/jussive** (immediate / situational prohibition). In divine speech the 2mp imperative and the לֹא + 2ms/2mp imperfect together carry the apodictic-law register: YHWH directly addresses a human addressee (individual or community) with binding positive and negative commands.

1. **2mp positive command** — Qal/Piel/Hiphil/Hithpael Impv 2mp, prefix-less base stem, typically ending in ־וּ (qiṭlû / diršû / šûvû); addresses the covenant community.
2. **2ms positive command** — Impv 2ms (qeṭol / šemaʿ / dabbēr); addresses an individual (often a prophet or the nation personified as "Israel").
3. **לֹא + Impf 2ms/2mp** — categorical/eternal prohibition ("thou shalt never…"); the form of the Decalogue proscriptions and the Holiness Code.
4. **אַל + Impf 2ms/2mp** (often short/jussive form) — immediate/situational prohibition ("do not [now]…"); contrasts with לֹא in scope, not topic.

## Form Recognition

- **Imperative morphology (positive):** no person-prefix; built from the imperfect stem minus the prefix.
  - Qal 2ms qeṭōl / šemaʿ; 2mp qiṭlû / šimʿû
  - Piel 2ms dabbēr / qaddēš; 2mp dabberû / qaddəšû
  - Hiphil 2ms hakrēt / hāsēr; 2mp hakrîtû / hāsîrû
  - Hithpael 2mp hizzakkû (reflexive "purify yourselves")
- **Prohibition morphology (negated imperfect):**
  - **לֹא + Qal/Piel/Hiphil Impf 2ms/2mp** — categorical, always-binding ("thou shalt not / ye shall not")
  - **אַל + Qal/Piel/Hiphil Impf 2ms/2mp** (often apocopated jussive) — immediate, situational ("do not [now]")
- **Parser codes:**
  - Positive imperative: `sp=verb vt=impv ps=2 gn=m nu=pl` (2mp) or `nu=sg` (2ms)
  - Prohibition: the verb itself is tagged `vt=impf ps=2`; recognise the pattern by the preceding לא (`Neg`) or אל (`Neg`)

## Functions with Examples

### 1. 2mp Positive Imperative — Covenant Community Addressed

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Isa 1:16 | רַחֲצוּ֙ | Verb.Qal.Impv.2mp of רחץ | "Wash you" |
| Isa 1:16 | הִזַּכּ֔וּ | Verb.Hithpael.Impv.2mp of זכה | "make you clean" |
| Isa 1:16 | הָסִ֛ירוּ | Verb.Hiphil.Impv.2mp of סור | "put away" |
| Isa 1:16 | חִדְל֖וּ | Verb.Qal.Impv.2mp of חדל | "cease [to do evil]" |
| Joe 2:12 | שֻׁ֥בוּ | Verb.Qal.Impv.2mp of שׁוב | "turn ye" |
| Isa 55:6 | דִּרְשׁ֥וּ | Verb.Qal.Impv.2mp of דרשׁ | "Seek ye [the LORD]" |
| Isa 55:6 | קְרָאֻ֖הוּ | Verb.Qal.Impv.2mp of קרא (+3ms suffix) | "call ye upon him" |

Four of these (Isa 1:16) are stacked asyndetically (no waw-conjunctions between the first four imperatives) — a characteristic rhetorical cluster of the prophetic summons. Joe 2:12 is explicitly framed by נְאֻם־יְהוָ֔ה "saith the LORD," marking the command as divine first-person speech to a plural addressee.

### 2. 2ms Positive Imperative — Individual / Collective-Personified Addressee

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Lev 19:2 | דַּבֵּ֞ר | Verb.Piel.Impv.2ms of דבר | "Speak [unto all the congregation]" |
| Deu 4:1 | שְׁמַ֤ע | Verb.Qal.Impv.2ms of שׁמע | "hearken, O Israel" |

The 2ms form is standard when Moses or a prophet is directly commanded; it is also used when the nation is addressed as a single personified "Israel" (Deu 4:1 vocative יִשְׂרָאֵ֗ל + 2ms impv).

### 3. לֹא + Imperfect 2ms — Categorical / Permanent Prohibition ("Thou Shalt Not")

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Exo 20:13 | לֹ֥א תִּֿרְצָֽח | Neg + Verb.Qal.Impf.2ms of רצח | "Thou shalt not kill" |
| Exo 20:15 | לֹ֣א תִּֿגְנֹֽב | Neg + Verb.Qal.Impf.2ms of גנב | "Thou shalt not steal" |
| Exo 23:1 | לֹ֥א תִשָּׂ֖א | Neg + Verb.Qal.Impf.2ms of נשׂא | "Thou shalt not raise [a false report]" |

The Decalogue prohibitions are morphologically **imperfects**, not imperatives — Hebrew has no negative imperative. The לֹא + *yiqtol* frame expresses the absolute, non-time-bound force (Waltke-O'Connor §34.2.1b "non-specific command"; GKC §107o). English "shalt" translates the modal-volitive reading of the imperfect (cross-linked to [qal-imperfect](qal-imperfect.md) §3 "Modal / Volitive").

### 4. לֹא + Imperfect 2mp — Categorical Prohibition Addressed to the Community

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Lev 19:4 | לֹ֥א תַעֲשׂ֖וּ | Neg + Verb.Qal.Impf.2mp of עשׂה | "nor make to yourselves [molten gods]" |

### 5. אַל + Imperfect 2ms/2mp — Immediate / Situational Prohibition

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Exo 23:1 | אַל־תָּ֤שֶׁת | Neg + Verb.Qal.Impf.2ms of שׁית | "put not thine hand [with the wicked]" |
| Lev 19:4 | אַל־תִּפְנוּ֙ | Neg + Verb.Qal.Impf.2mp of פנה | "Turn ye not unto idols" |

Exo 23:1 and Lev 19:4 each juxtapose **both** negators in one verse — לֹא + Impf for the enduring principle and אַל + Impf for the concrete deed that instantiates it (Waltke-O'Connor §34.2.1b; GKC §109c). The אַל-form tends to be morphologically shorter (jussive) though the ETCBC parser tags both as `Impf.2ms/2mp`.

## Contrast with Related Forms

| Form | Function | Example |
|------|----------|---------|
| **Impv 2mp (positive)** | direct command to community | Isa 1:16 רַחֲצוּ "wash you" |
| **Impv 2ms (positive)** | direct command to individual/personified collective | Deu 4:1 שְׁמַע "hearken" |
| **לֹא + Impf 2ms/2mp** | categorical prohibition ("never") | Exo 20:13 לֹא תִרְצָח |
| **אַל + Impf 2ms/2mp** | immediate prohibition ("don't [now]") | Exo 23:1 אַל־תָּשֶׁת |
| **Cohortative 1cp** | divine self-exhortation ("let us…") | Gen 1:26 נַעֲשֶׂה |
| **Jussive 3ms** | third-person command ("let him / may he…") | Gen 1:3 יְהִי |
| **Inf.Abs. + finite** | intensified command | Deu 7:2 הַחֲרֵם תַּחֲרִים |

### Imperative vs. Imperfect-as-Command

Hebrew uses the **imperative** only for positive 2nd-person commands. The **imperfect** covers (a) all negative commands (לֹא / אַל + Impf), (b) 3rd-person commands via jussive (יְהִי, יִקְטֹל), and (c) 1st-person volition via cohortative (נַעֲשֶׂה). An imperfect with 2nd-person modal force without a negator is typically read as **future obligation** rather than imperative proper (e.g., Lev 19:2 קְדֹשִׁ֣ים תִּהְי֑וּ "ye shall be holy" — Qal.Impf.2mp, not Impv).

## Function Summary for Divine Command

| Register | Positive | Prohibition |
|----------|----------|-------------|
| Community (2mp) | Impv 2mp (Isa 1:16; Joe 2:12; Isa 55:6) | לֹא / אַל + Impf 2mp (Lev 19:4) |
| Individual / personified nation (2ms) | Impv 2ms (Lev 19:2; Deu 4:1) | לֹא / אַל + Impf 2ms (Exo 20:13, 15; Exo 23:1) |

## Related Library Entries

- [qal-imperfect](qal-imperfect.md) — the host form for all prohibitions (§3 Modal/Volitive lists Exo 20:13 as apodictic prohibition).
- [hiphil-imperfect](hiphil-imperfect.md) — Hiphil imperatives and Hiphil prohibitions in divine war / judgment language.
- [infinitive-absolute-intensification](infinitive-absolute-intensification.md) — Inf.Abs. + 2ms Impf intensifies prohibitions (Gen 2:17 מוֹת תָּמוּת; Gen 3:4 negated לֹא־מוֹת תְּמֻתוּן).
- [cohortative-1cp-divine-speech](cohortative-1cp-divine-speech.md) — 1cp volitive counterpart to the 2mp imperative.

## Reference Citations

- **Waltke-O'Connor, *IBHS*** §34.4 on the imperative; §34.2.1b on לֹא + non-perfective as categorical prohibition vs. אַל + jussive as immediate prohibition.
- **Gesenius-Kautzsch-Cowley, *GKC*** §110 on the imperative (positive only, 2nd person only); §107o on the imperfect of categorical/eternal command; §109c on jussive after אַל.
- **Joüon-Muraoka, *A Grammar of Biblical Hebrew*** §114 on volitives; §160 on negation, distinguishing לֹא (absolute / objective) from אַל (subjective / volitive).
- **Futato, *Beginning Biblical Hebrew*** Lesson 19 on the imperative paradigm; Lesson 14 on prohibitions.

---
*Generated from: hebrew_parser.py (--verse Isa 1:16, Joe 2:12, Isa 55:6, Lev 19:2, Deu 4:1, Exo 20:13, 20:15, 23:1, Lev 19:4), KJV via Grep*
*Last updated: 2026-04-18*
