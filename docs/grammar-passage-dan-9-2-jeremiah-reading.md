# Grammar Analysis: Daniel 9:2 — Daniel Reading Jeremiah's Seventy Years

## Text

**Hebrew (MT, BHSA):**

בִּשְׁנַ֤ת אַחַת֙ לְמָלְכֹ֔ו אֲנִי֙ דָּֽנִיֵּ֔אל בִּינֹ֖תִי בַּסְּפָרִ֑ים מִסְפַּ֣ר הַשָּׁנִ֗ים אֲשֶׁ֨ר הָיָ֤ה דְבַר־יְהוָה֙ אֶל־יִרְמִיָ֣ה הַנָּבִ֔יא לְמַלֹּ֛אות לְחָרְבֹ֥ות יְרוּשָׁלִַ֖ם שִׁבְעִ֥ים שָׁנָֽה׃

**Transliteration:** *bîšnaṯ ʾaḥaṯ lə-molḵô ʾănî Dāniyyēʾl bînōṯî ba-səp̄ārîm mispar ha-šānîm ʾăšer hāyāh dəḇar-YHWH ʾel-Yirməyāh han-nāḇîʾ lə-mallōʾṯ lə-ḥārəḇôṯ Yərûšālāim šiḇʿîm šānāh*

**KJV:** *In the first year of his reign I Daniel understood by books the number of the years, whereof the word of the LORD came to Jeremiah the prophet, that he would accomplish seventy years in the desolations of Jerusalem.*

---

## Word-by-Word Parsing (hebrew_parser.py)

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | בִּ | ב | Prep | in |
| 2 | שְׁנַ֤ת | שׁנה | Noun.fs.**Cst** | year |
| 3 | אַחַת֙ | אחד | Noun.fs.Abs | one |
| 4 | לְ | ל | Prep | to/of |
| 5 | מָלְכֹ֔ו | מלך | **Verb.Qal.InfCon +3ms** | be king (his reigning) |
| 6 | אֲנִי֙ | אני | PersPron.1s | I |
| 7 | דָּֽנִיֵּ֔אל | דניאל | PropN.ms | Daniel |
| 8 | בִּינֹ֖תִי | בין | **Verb.Qal.Perf.1s** | I understood |
| 9 | בַּ + ה | ב + ה | Prep + Art | in + the |
| 10 | סְּפָרִ֑ים | ספר | Noun.mp.Abs | scrolls/books |
| 11 | מִסְפַּ֣ר | מספר | Noun.ms.**Cst** | number |
| 12 | הַשָּׁנִ֗ים | ה + שׁנה | Art + Noun.fp.Abs | the years |
| 13 | אֲשֶׁ֨ר | אשׁר | Conj (relative) | which/whereof |
| 14 | הָיָ֤ה | היה | Verb.Qal.Perf.3ms | came/was |
| 15 | דְבַר | דבר | Noun.ms.**Cst** | word |
| 16 | יְהוָה֙ | יהוה | PropN.ms | YHWH |
| 17 | אֶל | אל | Prep | to |
| 18 | יִרְמִיָ֣ה | ירמיה | PropN.ms | Jeremiah |
| 19 | הַ + נָּבִ֔יא | ה + נביא | Art + Noun.ms.Abs | the prophet |
| 20 | לְ | ל | Prep | to/for |
| 21 | מַלֹּ֛אות | מלא | **Verb.Piel.InfCon** | to fill/fulfill |
| 22 | לְ | ל | Prep | to/for |
| 23 | חָרְבֹ֥ות | חרבה | Noun.fp.**Cst** | ruins/desolations |
| 24 | יְרוּשָׁלִַ֖ם | ירושׁלם | PropN | Jerusalem |
| 25 | שִׁבְעִ֥ים | שׁבע | Noun.mp.Abs | seventy |
| 26 | שָׁנָֽה | שׁנה | Noun.fs.Abs | year |

---

## Clause Structure (BHSA)

| # | Type | Domain | Function map |
|---|------|--------|--------------|
| 1 | **XQtl** (fronted-adjunct + qatal) | Q | [Time] בִּשְׁנַת אַחַת · [Subj] אֲנִי דָּנִיֵּאל · [Pred] בִּינֹתִי · [Cmpl] בַּסְּפָרִים |
| 2 | **InfC** | Q | [PreS] לְמָלְכֹו (subordinate to #1's time-phrase, identifying whose reign) |
| 3 | **NmCl** (verbless) | Q | [Subj] מִסְפַּר הַשָּׁנִים · [PreC] שִׁבְעִים שָׁנָה — "the number of the years [is] seventy years" |
| 4 | **xQtX** (relative + qatal) | Q | [Rela] אֲשֶׁר · [Pred] הָיָה · [Subj] דְבַר יְהוָה · [Cmpl] אֶל יִרְמִיָה הַנָּבִיא |
| 5 | **InfC** (purpose) | Q | [Pred] לְמַלֹּאות · [Cmpl] לְחָרְבֹות יְרוּשָׁלִַם |

Crucially, **Clause 3 is an independent verbless nominal clause**. The BHSA parser does not read *mispar ha-šānîm* as the object of *bînōṯî*; it reads it as a subject identified in equation with *šiḇʿîm šānāh*. In other words, the text is not merely saying "Daniel counted the years and got seventy"; it is saying **"the number of the years [of the Jeremiah oracle] = seventy years,"** as an independent predication that Daniel extracted from the books.

---

## Construct Chains (hebrew_parser.py --construct)

| Head (Cst) | Tail (Abs) | Force |
|------------|------------|-------|
| שְׁנַת (year.Cst) | אַחַת (one) | "year-of one" = "first year" |
| מִסְפַּר (number.Cst) | הַשָּׁנִים (the-years) | definite genitive: "**the** number of **the** years" — the specific, named count |
| דְבַר (word.Cst) | יְהוָה (YHWH) | classic prophetic-word formula |
| חָרְבֹות (ruins.Cst) | יְרוּשָׁלִַם (Jerusalem) | "ruins-of Jerusalem" — the desolation period of Jer 25/29 |

The definite article on הַשָּׁנִים anchors this as **the published, knowable count** — not an abstraction. The genre signal is historical-oracular: Jeremiah named a specific number; Daniel is reading that number as the number that it is.

---

## Key Grammatical Features

### 1. בִּינֹתִי — Qal Perfect 1cs of בין (H995)

- **Form:** Verb.**Qal.Perf.1cs** of בין ("discern, understand, perceive")
- **Significance:** *Qatal* of a cognitive verb in first-person autobiographical narrative = completed act of intellectual comprehension. Daniel is not reporting a vision, a dream, a *ḥāzôn*, or a *marʾeh* — he is reporting an act of **reading-comprehension**. The same prophet who elsewhere says *hinnēh ḥāzôn nirʾāh ʾēlay* ("behold, a vision appeared to me," 8:1) here says *bînōṯî* ("I understood"). The **genre register shifts with the verb**: visionary reception → scholarly reading.
- **Word study:** [H995-biyn](../../word-studies/H995-biyn.md)
- **Grammar reference:** The Qal perfect functions here as a discrete-event past ("I came to understand") rather than stative/characterizing; contrast with *bînōṯî* of 10:1 (same form, same speaker, about an opened vision).

### 2. בַּסְּפָרִים — Prep + Article + Noun.mp.Abs of סֵפֶר (H5612)

- **Form:** Prep בְּ + definite article ה + Noun.mp.Abs *səp̄ārîm* ("the scrolls/books/documents")
- **Significance:** The definite plural is emphatic and concrete. *səp̄ārîm* denotes **written, inscribed documents** — the same noun used of the *sēp̄er* of Moses (Josh 1:8), of royal chronicles (1 Kgs 14:19), and of Jeremiah's own written oracle (Jer 36). The **instrumental בְּ** ("by means of the books") makes Daniel's understanding **text-mediated**, not angel-mediated. This is the one place in the book of Daniel where Daniel's knowledge comes from *reading Scripture*, not from a heavenly messenger. Vv. 3–23 then show how *reading the books* triggers the *angelic* mode (Gabriel, v. 21) — but the angelic mode is triggered *by* the reading mode, not in place of it.
- **Contrast with 8:1–14, 26:** the 2,300 *ereḇ bōqer* come to Daniel *ḥāzôn* in vision; he is told *sətōm he-ḥāzôn* ("seal the vision," 8:26); he does NOT at that moment understand the number. In 9:2 by contrast, **because it is a sēp̄er (a published prophetic letter, Jer 29:1), not a ḥāzôn, the number is immediately legible.** This is the genre distinction working at the level of the text's own vocabulary.

### 3. מִסְפַּר הַשָּׁנִים … שִׁבְעִים שָׁנָה — Verbless Nominal Equation

- **Form:** Two construct/number phrases joined by a verbless NmCl predication (Clause 3 above):
  - Subject: מִסְפַּר הַשָּׁנִים ("the number of the years") — definite construct chain
  - Predicate: שִׁבְעִים שָׁנָה ("seventy year[-unit]") — cardinal+counted-noun singular per GKC §134g (numerals 11–19 take singular; 20+ normally pl. but שָׁנָה is idiomatic singular after tens in chronological formulae, cf. Gen 5:3, 6, etc.)
- **Significance:** The verbless nominal clause **equates** "the number of the years" with "seventy years." Hebrew nominal clauses assert **identity or essence**, not contingent fulfillment (Joüon §154). Grammatically, this is not "Daniel estimates roughly seventy" or "he considered it to be about seventy" — it is a flat predication: *the number is seventy*.
- **Word study:** [H8141-shaneh](../../word-studies/H8141-shaneh.md) — canonical Hebrew noun for **calendar year** (solar-lunar twelve-month cycle), distinct from שָׁבוּעַ ("week, sevened-unit," Dan 9:24), יוֹם ("day"), and עֶרֶב בֹּקֶר ("evening-morning," Dan 8:14). The lexical choice matters: when Hebrew means *a calendar year*, it uses שָׁנָה.
- **Absolute/Cardinal form:** The form שִׁבְעִים שָׁנָה (masc.pl. numeral + fem.sg. absolute counted noun) matches the chronological-accusative pattern of Gen 5, Exo 12:40–41, 1 Kgs 6:1 and — decisively for genre comparison — **Jer 25:11–12 and 29:10**, the very passages Daniel is reading. Daniel is not recoding Jeremiah into a new metric; he is reading Jeremiah's *šānāh* as *šānāh*.

### 4. לְמַלֹּאות לְחָרְבֹות יְרוּשָׁלִַם — Piel Infinitive Construct of Purpose

- **Form:** Prep ל + **Piel.InfCon** of מלא ("to fill, complete, fulfill") + ל+construct chain חָרְבֹות יְרוּשָׁלִַם
- **Significance:** Piel of מלא is factitive ("cause to be full"), here used of **completing a measured time-span** — parallel to Gen 29:27–28 (Laban on Leah's bridal week), Gen 50:3 (seventy days of mourning Jacob), Lam 4:18, and **programmatically Jer 25:12**: *wə-hāyāh ḵi-mlōʾṯ šiḇʿîm šānāh* ("and it shall come to pass, when seventy years are accomplished"). Daniel is using **Jeremiah's own verb** to describe Jeremiah's own oracle. The infinitive construct with לְ expresses purpose/result of the divine word: *the word came … in order to fulfill seventy years upon Jerusalem's ruins*.
- The doubled לְ (לְמַלֹּאות לְחָרְבֹות) is a purpose-plus-goal construction: "to fulfill [seventy years] for/upon the desolations of Jerusalem." Infinitive+indirect object stacking is standard Classical Hebrew (Joüon §124m).

### 5. דְבַר־YHWH אֶל־יִרְמִיָה הַנָּבִיא — Prophetic Oracular Formula

- **Form:** xQtX relative clause אֲשֶׁר הָיָה דְבַר־יְהוָה אֶל־Jeremiah הַנָּבִיא — "whereof the word of YHWH was/came to Jeremiah the prophet"
- **Significance:** This is the **classical prophetic messenger-formula** (Jer 1:2; Ezek 1:3; Hos 1:1; Jon 1:1; Mic 1:1 — cf. דְבַר־יְהוָה ‏אֲשֶׁר הָיָה אֶל־...). It identifies the source text as **oracular prophecy delivered historically to a named prophet** (Jeremiah) with a named audience (Jerusalem) for a named event (desolation-period). This genre has a conventional hermeneutic: **the numbers in this genre are the numbers they are**. Jeremiah did not receive the 70 years as a sealed vision (contrast Daniel in 8:14, 8:26, 12:4, 12:9). He was instructed to **write them in a letter** (Jer 29:1) and **publicly read them** (Jer 36). The genre marker is woven into Daniel's syntax itself.

---

## Genre-Distinction Baseline: Hermeneutic Grammar

Daniel 9:2 is the **controlled experiment** for biblical time-number hermeneutics. The same prophet — **the very prophet through whom day-for-year apocalyptic numbers are given** (2,300 ereḇ bōqer, 8:14; a time, times, and half a time, 7:25; 1,290 and 1,335 days, 12:11–12) — here, in 9:2, **reads another prophet's seventy-years oracle as literal calendar years**. The text-internal markers show why the two hermeneutics do not conflict but are grammatically distinguished:

| Axis | Dan 9:2 reads Jer 25:11 / 29:10 | Dan 8:14 / 7:25 / 12:7 / 12:11–12 |
|------|----------------------------------|--------------------------------------|
| **Source genre** | *sēp̄er* (written oracular letter, Jer 29:1) | *ḥāzôn* / *marʾeh* (apocalyptic vision) |
| **Reception verb** | *bînōṯî ba-səp̄ārîm* ("I understood by the books," 9:2) | *nirʾāh ʾēlay* ("appeared to me," 8:1); *ḥāzôn rāʾîṯî* ("vision I saw") |
| **Time-noun** | *šānāh* (calendar year) | *ereḇ bōqer* (evening-morning), *ʿiddān* (Aram.), *yāmîm* (days), *mōʿēd* |
| **Sealing** | NOT sealed — Jer 29:1 was a public letter | *sətōm he-ḥāzôn* ("seal the vision," 8:26); *stōm ha-dəḇārîm wə-ḥăṯōm ha-sēp̄er* ("shut the words and seal the book," 12:4) |
| **Immediate intelligibility** | Yes — Daniel "understood" in 9:2 | No — Daniel is *stunned* in 8:27, *still waiting* in 12:8 |
| **Requires decoding** | No — numeric face-value | Yes — see [day-year-formula](../hebrew/day-year-formula.md), Num 14:34, Ezek 4:4–6 |
| **Fulfillment verb** | *mlōʾṯ* (Piel: time-span completion, Jer 25:12) — *mallōʾṯ* reused Dan 9:2 | *stm/ḥtm* + *ʿēṯ qēṣ* / *mōʿēd qēṣ* (sealed till appointed end) |

**The distinction is text-intrinsic.** It is not a modern interpreter's grid imposed on the text. It is **Daniel's own grammar**. In 9:2 Daniel:

1. Uses the reading verb *bîn*, not the seeing verbs *ḥzh* / *rʾh*.
2. Names the source *sēp̄er* (book), not *ḥāzôn* (vision).
3. Preserves Jeremiah's noun *šānāh*, not substituting *yāmîm* or *ʿereḇ bōqer*.
4. Reuses Jeremiah's Piel *mlʾ* as the fulfillment verb — the ordinary language of chronological completion.
5. Treats the seventy as definite and known (מִסְפַּר הַשָּׁנִים, definite construct) — no sealed mystery.

Therefore Daniel 9:2 does **not** transpose Jeremiah's literal years into symbolic days. And conversely, when the *angelic* oracle of 9:24–27 answers Daniel's prayer, it switches back into **apocalyptic grammar** — the rare noun שָׁבֻעַ ("sevened-unit"), the hapax-legomenon *nḥtk* ("is decreed/cut off"), construct-heavy symbolic architecture (see [dan-9-24-27](dan-9-24-27.md)). **One prophet. Two registers. The register is signaled by the Hebrew itself.**

## Dan 9:2 as Hinge Verse of Daniel 9

The grammatical chain vv.2–3 shows *reading* producing *prayer*:

> v. 2: בִּינֹתִי בַּסְּפָרִים … (Qal.Perf.1cs) — "I understood by the books…"
>
> v. 3: וָאֶתְּנָה אֶת־פָּנַי אֶל־אֲדֹנָי הָאֱלֹהִים לְבַקֵּשׁ תְּפִלָּה וְתַחֲנוּנִים — "and I set my face to the Lord God to seek prayer and supplications…" (Qal.Wayq.1cs — **narrative-consecutive** continuation)

The *wayyiqtol* of v. 3 is the grammatical consequence of the *qatal* of v. 2. The wayyiqtol chain then runs continuously into the long prayer of vv. 4–19 and into Gabriel's arrival in vv. 20–23. Gabriel explicitly labels the **cause**: *ba-t'ḥillaṯ taḥănûnêḵā yāṣāʾ dāḇār* ("at the beginning of your supplications the word went forth," v. 23). The supplications began because of the reading. The reading was of the seventy years. Therefore the **seventy-weeks oracle of vv. 24–27 is delivered precisely because Daniel correctly read the seventy years of Jeremiah as literal years** — had he transposed them into a symbolic 25,550-year span, he would not have been praying in 537 BC for a return in 536 BC. The text's own internal logic requires the literal reading of Jer 25/29 at 9:2, and then generates the apocalyptic day-year oracle of 9:24–27 as the divine answer. The two hermeneutics meet in the same chapter **without collision** because the text flags each register with distinct vocabulary.

This makes Dan 9:2 the **calibrating verse** for the whole day-for-year discussion: it anchors one end of the hermeneutic scale (literal oracular-historical *šānîm*) while the vision numbers anchor the other end (symbolic apocalyptic day→year). The same prophet, the same book, the same chapter — but different genre registers and different grammar.

---

## Cross-References

### Grammar library
- [qal-imperfect](../hebrew/qal-imperfect.md) — Qal aspectual framework (contrast with perfect *bînōṯî* here)
- [infinitive-absolute-intensification](../hebrew/infinitive-absolute-intensification.md) — related InfAbs/InfCon functions (contrast; here only InfCon + לְ)
- [syntax-wx-qatal-circumstantial](../hebrew/syntax-wx-qatal-circumstantial.md) — cf. fronted-adjunct XQtl opening *bišnaṯ ʾaḥaṯ*
- [day-year-formula](../hebrew/day-year-formula.md) — the hermeneutic principle being **contrasted** here (Dan 9:2 does NOT deploy day-for-year; Num 14:34 / Ezek 4:4–6 show where it does)
- [vision-introduction-formulas](../hebrew/vision-introduction-formulas.md) — the formulas *absent* from 9:2 (marking its non-apocalyptic register)

### Passage library
- [dan-8-14](dan-8-14.md) — 2,300 *ereḇ bōqer*, asyndetic-indefinite time-phrase; genre: apocalyptic vision
- [dan-8-17-19](dan-8-17-19.md) — *ʿēṯ qēṣ* / *mōʿēd qēṣ*; genre: apocalyptic vision
- [dan-8-26](dan-8-26.md) — *sətōm he-ḥāzôn* sealing command; genre: apocalyptic
- [dan-8-23-25](dan-8-23-25.md) — little-horn recapitulation
- [dan-9-24-27](dan-9-24-27.md) — the 70-weeks oracle that comes *because* of Dan 9:2's correct reading; genre: apocalyptic (note contrast of שָׁבֻעַ vs. שָׁנָה lexis)
- [dan-11-36-37](dan-11-36-37.md), [dan-12-7-11-12](dan-12-7-11-12.md) — continuing apocalyptic register
- [gen-15-13-16](gen-15-13-16.md) — oracular *šānāh* count (400 years) with literal fulfillment; parallels Dan 9:2's reading of Jer
- [rev-11-12-time-markers](rev-11-12-time-markers.md) — NT apocalyptic time-formulas descending from Dan 7:25 / 12:7

### Word studies
- [H995-biyn](../../word-studies/H995-biyn.md) — *bîn*, "to discern/understand" — the verb that opens Dan 9:2
- [H8141-shaneh](../../word-studies/H8141-shaneh.md) — *šānāh*, "year" — the calendar-year noun used twice in 9:2
- [H3068-yhwh](../../word-studies/H3068-yhwh.md) — the divine name in דְבַר־יְהוָה
- Gaps flagged for word studies: **H5612 סֵפֶר** (*sēp̄er*, "book, scroll, letter"), **H4557 מִסְפָּר** (*mispār*, "number"), **H4390 מלא** (*mlʾ*, "fill, complete"), **H2723 חָרְבָּה** (*ḥorbāh*, "ruin, desolation"), **H5030 נָבִיא** (*nāḇîʾ*, "prophet"), **H1697 דָּבָר** (*dāḇār*, "word"), **H3414 יִרְמְיָה** (proper name Jeremiah)

### Parent oracle (Jer)
- Jer 25:11–12 — the original seventy-years oracle (*wə-ʿāḇḏû … šiḇʿîm šānāh* + *ki-mlōʾṯ šiḇʿîm šānāh*) — the text Daniel was reading
- Jer 29:10 — the letter to the exiles: *ki lə-p̄î mlōʾṯ lə-ḇāḇel šiḇʿîm šānāh ʾep̄qōḏ ʾeṯḵem* — explicitly *sēp̄er*-genre (Jer 29:1), addressed to Daniel's own cohort
- 2 Chr 36:21 — narrative fulfillment notice using the same *mlʾ* verb: *ʿaḏ-melʾōṯ šiḇʿîm šānāh*
- Ezra 1:1 — cyrus-edict fulfillment *liḵlōʾṯ dəḇar-YHWH mi-pî Yirməyāh* — confirms within-Scripture that Jeremiah's 70 *šānîm* ran literally 605/586→539/538 BC.
