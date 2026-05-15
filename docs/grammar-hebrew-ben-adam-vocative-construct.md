# Ben-Adam Vocative Construct Chain (בֶּן־אָדָם)

## Definition
The construct chain **בֶּן־אָדָם** (*ben-ʾāḏām*, lit. "son of Adam / son of humanity") is a two-word noun phrase in which `בֵּן` ("son") stands in the construct state, bound to the absolute noun `אָדָם` ("human, humanity"). In the singular, the phrase denotes an individual human being, but functions in biblical Hebrew in three distinct syntactic-pragmatic roles:

1. **Vocative of address** — a speaker (divine or angelic) addresses a prophet as *ben-ʾāḏām*, foregrounding the addressee's creaturely humanity over against the divine speaker.
2. **Humbling contrastive parallelism** — paired with `אִישׁ` ("man") or `אֱנוֹשׁ` ("mortal") in poetic parallelism to emphasize human frailty vis-à-vis God.
3. **Titular / apocalyptic** — the Aramaic equivalent `בַּר אֱנָשׁ` (*bar ʾĕnāš*) in Dan 7:13 refers to a heavenly-enthroned figure; Dan 8:17 uses Hebrew *ben-ʾāḏām* as address to Daniel in an apocalyptic vision.

## Form Recognition
- Two nouns: `בֶּן` or `בֵּן` (ms.Cst) + `אָדָם` (ms.Abs), often joined by maqqef: `בֶּן־אָדָם`.
- Parser signature: `בן Noun.ms.Cst` immediately followed by `אדם Noun.ms.Abs`.
- **Vocative use** is recognized contextually: it follows a speech-introducer (typically `וַיֹּאמֶר אֵלַי`, "and he said to me") with no article, no preposition, no verb agreement — the phrase is in apposition/direct address to the 2ms addressee.
- **Plural** `בְּנֵי אָדָם` (*bənê ʾāḏām*, mp.Cst + ms.Abs) is NOT vocative; it denotes humankind collectively.
- **Aramaic equivalent:** `בַּר אֱנָשׁ` (*bar ʾĕnāš*) — Dan 7:13 uses it with the preposition `כְּ` ("like").

## Functions with Examples

### 1. Vocative Address (Prophet by Divine/Angelic Speaker)

| Reference | Hebrew | Parsing | Context |
|-----------|--------|---------|---------|
| Dan 8:17 | הָבֵן בֶּן־אָדָם | Hiph.Impv + Noun.ms.Cst + Noun.ms.Abs | Gabriel to Daniel: "Understand, O son of man" |
| Eze 2:1 | בֶּן־אָדָם עֲמֹד עַל־רַגְלֶיךָ | Noun.ms.Cst + Noun.ms.Abs + Qal.Impv.2ms | YHWH to Ezekiel: "Son of man, stand upon thy feet" |
| Eze 2:3 | בֶּן־אָדָם שֹׁולֵחַ אֲנִי אֹותְךָ | Noun.ms.Cst + Noun.ms.Abs + Ptcp + PersPron.1s | "Son of man, I send thee to the children of Israel" |
| Eze 3:1 | בֶּן־אָדָם אֵת אֲשֶׁר־תִּמְצָא אֱכֹול | Noun.ms.Cst + Noun.ms.Abs + Qal.Impv.2ms | "Son of man, eat that thou findest" |
| Eze 3:17 | בֶּן־אָדָם צֹפֶה נְתַתִּיךָ | Noun.ms.Cst + Noun.ms.Abs + Ptcp + Qal.Perf.1s.+2ms | "Son of man, I have made thee a watchman" |

Each example shows the consistent pattern: speech-introducer, then *ben-ʾāḏām* as unmarked vocative, then imperative or 2ms-directed verb/participle. The form has no special vocative marker — it is bare, in apposition to the addressee.

### 2. Humbling Contrastive Parallelism (Human vs. God)

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Num 23:19 | לֹא אִישׁ אֵל ... וּבֶן־אָדָם וְיִתְנֶחָם | Neg + Noun.ms.Abs + Noun.ms.Abs ... + Noun.ms.Cst + Noun.ms.Abs + Hith.Impf.3ms | "God is not a man, that he should lie; neither the son of man, that he should repent" |
| Psa 8:5 (EVV 8:4) | מָה־אֱנוֹשׁ ... וּבֶן־אָדָם כִּי תִפְקְדֶנּוּ | IntPron + Noun.ms.Abs ... + Noun.ms.Cst + Noun.ms.Abs + Conj + Qal.Impf.2ms.+3ms | "What is man ... and the son of man, that thou visitest him?" |
| Job 25:6 | אֱנוֹשׁ רִמָּה וּבֶן־אָדָם תּוֹלֵעָה | Noun.ms.Abs + Noun.fs.Abs + Noun.ms.Cst + Noun.ms.Abs + Noun.fs.Abs | "man, [that is] a worm? and the son of man, [which is] a worm?" |
| Job 35:8 | לְאִישׁ־כָּמוֹךָ ... וּלְבֶן־אָדָם צִדְקָתֶךָ | Prep+Noun.ms.Abs + Prep.+2ms ... + Prep+Noun.ms.Cst + Noun.ms.Abs + Noun.fs.Abs.+2ms | "a man as thou [art] ... the son of man" |

Note the recurring pairing: *ʾîš* / *ʾĕnôš* ∥ *ben-ʾāḏām*. The construct chain is the B-term of the parallelism, drawing out the creaturely-mortal aspect.

### 3. Apocalyptic Titular Use (Heavenly Figure / Visionary Address)

| Reference | Aramaic/Hebrew | Parsing | Context |
|-----------|----------------|---------|---------|
| Dan 7:13 | כְּבַר אֱנָשׁ אָתֵה הֲוָה | Prep + Noun.ms.Cst + Noun.ms.Abs + Peal.Ptcp.ms + Peal.Perf.3ms | Aramaic: "[one] like the Son of man came with the clouds of heaven" |
| Dan 8:17 | הָבֵן בֶּן־אָדָם כִּי לְעֶת־קֵץ הֶחָזוֹן | Hiph.Impv + Noun.ms.Cst + Noun.ms.Abs + Conj + Prep + Noun.s.Cst + Noun.ms.Abs + Art + Noun.ms.Abs | Vocative address to Daniel within apocalyptic vision linking the address form to eschatological revelation |

Dan 7:13 is not vocative but nominal predication with the simile particle `כְּ`; it fuses the construct chain with heavenly enthronement imagery. Dan 8:17 uses the Hebrew vocative address within the same visionary genre.

## Contrast with Related Forms

| Form | Function | Example |
|------|----------|---------|
| `בֶּן־אָדָם` (sg, Cst) | Vocative address; humbling parallel | Eze 2:1; Num 23:19 |
| `בְּנֵי אָדָם` (mp.Cst + Abs) | Humankind collectively (NOT vocative) | Psa 11:4; Psa 14:2 |
| `אִישׁ` (Noun.ms.Abs) | Ordinary "man" without humbling nuance | Num 23:19 (A-term) |
| `אֱנוֹשׁ` (Noun.ms.Abs) | Mortal, frail human | Psa 8:5; Job 25:6 |
| `בַּר אֱנָשׁ` (Aramaic Cst) | Apocalyptic titular / simile | Dan 7:13 |
| Vocative with `יָהּ`/`אֲדֹנָי` | Address of deity (inverse direction) | — |

Hebrew has no dedicated vocative case. Vocatives are marked contextually (often by optional `הָ` article or bare apposition). `בֶּן־אָדָם` in Ezekiel/Daniel is a bare-apposition vocative.

### Plural contrast (NOT vocative)

| Reference | Hebrew | Parsing | Function |
|-----------|--------|---------|----------|
| Psa 11:4 | יִבְחֲנוּ בְּנֵי אָדָם | Qal.Impf.3mp + Noun.mp.Cst + Noun.ms.Abs | "his eyelids try the children of men" — humanity in general, object |
| Psa 14:2 | הִשְׁקִיף עַל־בְּנֵי־אָדָם | Hiph.Perf.3ms + Prep + Noun.mp.Cst + Noun.ms.Abs | "looked down from heaven upon the children of men" |

The plural *bənê hā-ʾāḏām* / *bənê ʾāḏām* always refers to humankind as a class; it is never used as a vocative address to a single prophet.

## Distinguishing the Vocative from the Appellative

A single construct chain `בֶּן־אָדָם` can be:
- **Vocative:** follows speech-introducer `וַיֹּאמֶר אֵלַי`; directly addresses the hearer; the following verb is 2ms imperative or 2ms indicative. Default in Ezekiel (93+ times) and Dan 8:17.
- **Appellative/predicate:** appears in a declarative clause with 3ms subject-matter, often parallel to `אִישׁ`/`אֱנוֹשׁ`. Default in Num 23:19, Psa 8:5, Job 25:6, Job 35:8.

Only the first use is vocative. Both share the same morphology.

## Related Canonical Entries
- Word study: `H1121-ben.md` (construct uses of בֵּן)
- Related entries to create: `imperative-mood.md` (exists), `cohortative-1cp-divine-speech.md` (exists)

---
*Generated from: hebrew_parser.py (--verse)*
*Last updated: 2026-04-19*
