# Grammar Analysis: Daniel 12:9 — The Second Sealing Declaration

## Scope

Daniel 12:9 is the angelic reply to Daniel's question in v.8 (*"what shall be the end of these things?"*). It restates, in **passive-participial / stative form**, the **command** that had already been issued in v.4 in **active imperative form**. The analysis compares:

- **v.4** — active `Qal impv. 2ms` pair: סְתֹם / חֲתֹם ("shut up / seal") addressed to Daniel
- **v.9** — `Qal passive participle mp.Abs` pair: סְתֻמִים / חֲתֻמִים ("[are] shut up / sealed") predicated of הַדְּבָרִים

This reframing coincides with the hinge between Daniel's inquiry (v.8) and the subsequent day-count disclosures (vv.11–12), and is paired with the explicit temporal boundary עַד־עֵת קֵץ (shared verbatim with v.4).

This analysis is **context-neutral**: it catalogs the morphological data, the clause-level syntax, and the major interpretive positions without endorsement.

---

## Text — Daniel 12:9

**Hebrew (BHSA / Leningrad):**
וַיֹּ֖אמֶר לֵ֣ךְ דָּנִיֵּ֑אל כִּֽי־סְתֻמִ֧ים וַחֲתֻמִ֛ים הַדְּבָרִ֖ים עַד־עֵ֥ת קֵֽץ׃

**Transliteration (with cantillation-stress):**
*wayyōʾmer lēḵ Dāniyyēʾl kî-sətumîm wa-ḥăṯumîm had-dəḇārîm ʿaḏ-ʿēṯ qēṣ*

**KJV:** "And he said, Go thy way, Daniel: for the words [are] closed up and sealed till the time of the end."

---

## Immediate Context (vv.4, 8, 10–13)

| v. | Hebrew (key) | KJV |
|----|-------------|-----|
| 4 | וְאַתָּה דָנִיֵּאל **סְתֹם** הַדְּבָרִים **וַחֲתֹם** הַסֵּפֶר עַד־עֵת קֵץ | "But thou, O Daniel, shut up the words, and seal the book, [even] to the time of the end" |
| 8 | וַאֲנִי שָׁמַעְתִּי וְלֹא אָבִין וָאֹמְרָה אֲדֹנִי מָה אַחֲרִית אֵלֶּה | "And I heard, but I understood not: then said I, O my Lord, what [shall be] the end of these [things]?" |
| **9** | **וַיֹּאמֶר לֵךְ דָּנִיֵּאל כִּי סְתֻמִים וַחֲתֻמִים הַדְּבָרִים עַד־עֵת קֵץ** | **"And he said, Go thy way, Daniel: for the words [are] closed up and sealed till the time of the end"** |
| 10 | יִתְבָּרֲרוּ וְיִתְלַבְּנוּ וְיִצָּרְפוּ רַבִּים … וְלֹא יָבִינוּ כָּל־רְשָׁעִים וְהַמַּשְׂכִּלִים יָבִינוּ | "Many shall be purified, and made white, and tried … none of the wicked shall understand; but the wise shall understand" |
| 11 | וּמֵעֵת הוּסַר הַתָּמִיד … יָמִים אֶלֶף מָאתַיִם וְתִשְׁעִים | "1,290 days" |
| 12 | אַשְׁרֵי הַמְחַכֶּה … יָמִים אֶלֶף שְׁלֹשׁ מֵאוֹת שְׁלֹשִׁים וַחֲמִשָּׁה | "1,335 days" |
| 13 | וְאַתָּה לֵךְ לַקֵּץ וְתָנוּחַ … לְקֵץ הַיָּמִין | "But go thou thy way till the end [be] … at the end of the days" |

---

## Word-by-Word Parsing — Dan 12:9 (from `hebrew_parser.py --verse "Dan 12:9"`)

| # | Hebrew | Lemma | Parsing (BHSA/ETCBC) | Gloss |
|---|--------|-------|-----------------------|-------|
| 1 | וַ | ו | Conj | and |
| 2 | יֹּ֖אמֶר | אמר | Verb.**Qal.Wayq.3ms** | (he) said |
| 3 | לֵ֣ךְ | הלך | Verb.**Qal.Impv.2ms** | go! (walk) |
| 4 | דָּנִיֵּ֑אל | דניאל | PropN.ms.Abs | Daniel |
| 5 | כִּֽי | כי | Conj | for / because / that |
| 6 | סְתֻמִ֧ים | סתם | Verb.**Qal.Ptcp.unknown.mp.Abs** (Qal passive ptcp. *qᵊtul* pattern) | (are) shut-up / closed-up |
| 7 | וַ | ו | Conj | and |
| 8 | חֲתֻמִ֛ים | חתם | Verb.**Qal.Ptcp.unknown.mp.Abs** (Qal passive ptcp. *qᵊtul* pattern) | (are) sealed |
| 9 | הַ | ה | Art | the |
| 10 | דְּבָרִ֖ים | דבר | Noun.mp.Abs | words |
| 11 | עַד | עד | Prep | until |
| 12 | עֵ֥ת | עת | Noun.s.**Cst** | time-of |
| 13 | קֵֽץ | קץ | Noun.ms.Abs | end |

**Morphological note on ETCBC tag `Ptcp.unknown`:** The BHSA morphology marks a Qal-stem participle, `mp.Abs`, but labels the voice/gender feature slot "unknown" because the **vocalization pattern** is *qᵊtul* (CəCuC) — the morphologically distinct **Qal passive participle** (GKC §50f, §84a l, Joüon §58a, IBHS §22.6, §37.3). This is the same pattern as אָרוּר "cursed," בָּרוּךְ "blessed," יָדוּעַ "known," לָקוּחַ "taken." The active Qal participle of these verbs would be סֹתֵם / חֹתֵם (*qōtēl*), not סְתֻמִים / חֲתֻמִים.

---

## Word-by-Word Parsing — Dan 12:4 (parallel, from `hebrew_parser.py --verse "Dan 12:4"`)

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | וְ | ו | Conj | and / but |
| 2 | אַתָּ֣ה | אתה | PersPron.2ms | thou |
| 3 | דָֽנִיֵּ֗אל | דניאל | PropN.ms.Abs | Daniel |
| 4 | **סְתֹ֧ם** | סתם | Verb.**Qal.Impv.2ms** | shut up! |
| 5 | הַ | ה | Art | the |
| 6 | דְּבָרִ֛ים | דבר | Noun.mp.Abs | words |
| 7 | וַ | ו | Conj | and |
| 8 | **חֲתֹ֥ם** | חתם | Verb.**Qal.Impv.2ms** | seal! |
| 9 | הַ | ה | Art | the |
| 10 | סֵּ֖פֶר | ספר | Noun.ms.Abs | book/scroll |
| 11 | עַד | עד | Prep | until |
| 12 | עֵ֣ת | עת | Noun.s.Cst | time-of |
| 13 | קֵ֑ץ | קץ | Noun.ms.Abs | end |
| 14 | יְשֹׁטְט֥וּ | שׁוט | Verb.Piel.Impf.3mp | (shall) rove-about |
| 15 | רַבִּ֖ים | רב | Adj.mp.Abs | many |
| 16 | וְ | ו | Conj | and |
| 17 | תִרְבֶּ֥ה | רבה | Verb.Qal.Impf.3fs | (shall) become-many |
| 18 | הַ | ה | Art | the |
| 19 | דָּֽעַת | דעת | Noun.fs.Abs | knowledge |

---

## Clause Structure — Dan 12:9 (from `hebrew_parser.py --clause "Dan 12:9"`)

| # | Clause Type | Domain | Text (translit.) | Function |
|---|-------------|--------|-------------------|----------|
| 1 | **Way0** | N (narrative) | *wayyōʾmer* | "And he said" — narrative speech-frame |
| 2 | **ZIm0** (zero-subject imperative) | Q (speech) | *lēḵ* | "Go!" — bare Qal impv. to Daniel |
| 3 | **Voct** (vocative-only clause) | Q | *Dāniyyēʾl* | "Daniel!" — stand-alone vocative |
| 4 | **Ptcp** (participial predicate clause) | Q | *kî sətumîm* | "for [they are] shut up" |
| 5 | **Ptcp** (participial predicate clause) | Q | *wa-ḥăṯumîm had-dəḇārîm ʿaḏ ʿēṯ qēṣ* | "and [are] sealed, the words, until the time of the end" |

The angel's reply is a **five-clause turn**: one narrative-domain speech-frame + four speech-domain clauses (command / vocative / twin stative-participial predications). The stative-participial pair (clauses 4–5) functions as the **causal ground** (כִּי) of the dismissal-command (clause 2, *lēḵ*). Subject הַדְּבָרִים appears only once (clause 5); clause 4 shares it by ellipsis.

The ETCBC tag **Ptcp** (as opposed to NmCl) signals that the participle is being parsed as the **predicate of a verbless clause** — i.e., a stative copular construction: *"The words [copula] sealed."* No finite copula is needed; Hebrew participial predication in Q-domain is inherently timeless/stative with context supplying tense.

---

## Construct Chain

`עֵת קֵץ` — singular noun in construct state (עֵת, `s.Cst`) + absolute noun (קֵץ, `ms.Abs`): "time-of end / appointed-time of the-end." This is the **same** construct chain as Dan 12:4 and Dan 8:17 (לְעֶת־קֵץ); a variant with מוֹעֵד appears at Dan 8:19 (לְמוֹעֵד קֵץ), 11:27, 11:35. See [dan-8-17-19](dan-8-17-19.md) for the עֵת / מוֹעֵד escalation discussion.

(The parser's construct-chain tool errored out during this run with a Text-Fabric memory fault; the construct identification above is read directly from the `Noun.s.Cst` + `Noun.ms.Abs` morphology tags in the word-by-word parse.)

---

## Key Grammatical Features

### 1. סְתֻמִים וַחֲתֻמִים — **Dual Qal Passive Participles** (the core shift)

**Morphology:**

- **סְתֻמִים** — lemma סתם ([H5640-catham](../../word-studies/H5640-catham.md)). Qal passive participle, masc.pl.Abs. Vocalic pattern **səC₁uC₂îm** = the *qᵊtul* Qal-passive ptcp. pattern (GKC §50f, §84a l; Joüon §58a; IBHS §37.3). Root-meaning "stop up, close up, shut up"; participial sense "[something that is] closed-up / shut-up / kept-secret."
- **חֲתֻמִים** — lemma חתם ([H2856-chatham](../../word-studies/H2856-chatham.md)). Qal passive participle, masc.pl.Abs. Same *qᵊtul* pattern (with *ḥateph-pataḥ* under guttural ח). Root-meaning "seal, close up with a seal"; participial sense "[something that is] sealed."

**Function of the Qal passive participle (*qᵊtul*):**

1. **Stative-resultative:** describes the **settled state** that results from a prior action. Contrast with the active Qal participle (*qōtēl*, e.g., סֹתֵם "one-who-is-stopping-up") which expresses **ongoing agency**. The *qᵊtul* form says **"the-thing-is-in-the-state-of-having-been-Xed"** — not that an agent is currently Xing it.
2. **Agent-suppressed:** like the Niphal, the Qal passive participle leaves the agent unspecified. In v.4 the agent is explicit (Daniel, commanded by the 2ms imperative); in v.9 the agent is invisible, and the focus is wholly on the condition of the patient (הַדְּבָרִים).
3. **Predicative use in verbless (Ptcp) clauses:** when in PreC slot of a Ptcp-clause (as here — ETCBC clause-types 4 and 5), it functions as the **predicate of a stative copular clause**: "X [is/are] Y-ed." Parallel examples of Qal passive ptcp. in predicative position: גֵּר יִהְיֶה זַרְעֲךָ (Gen 15:13 Qal.Ptcp.ms from גור); אָרוּר כְּנָעַן (Gen 9:25 Qal.Ptcp.ms from ארר); בָּרוּךְ יְהוָה (Gen 9:26 Qal.Ptcp.ms from ברך); הַזֶּה אֲשֶׁר אָתָה נְטוּעַ (Jer 1:10 analogue-class); Dan 7:9 יְתִב וּלְבוּשֵׁהּ … חִוָּר (Aramaic peal-passive-ptcp. cognate).

**The shift from v.4 → v.9:**

| v.4 | v.9 |
|-----|-----|
| **Active Qal imperatives 2ms** סְתֹם / חֲתֹם | **Qal passive participles mp.Abs** סְתֻמִים / חֲתֻמִים |
| Addressee: **you** (Daniel) | Subject: **the words** |
| Frame: **command to act** | Frame: **declaration of state** |
| Agency: Daniel closes / seals | Agency: suppressed (the words are-closed) |
| Object: הַדְּבָרִים + הַסֵּפֶר | Subject: הַדְּבָרִים (only) |
| Mode: deontic (must-do) | Mode: descriptive (are-so) |

The **lexeme-pair is identical** (סתם + חתם); only the **stem-form**, **voice**, and **clause-role** change. This kind of imperative→passive-participle restatement is rare in Biblical Hebrew; the closest analogues are:

- **Isa 6:9–10** active imperative הַשְׁמֵן / הַכְבֵּד / הָשַׁע ↔ v.11 פַּן … וְשָׁב וְרָפָא (modal-passive of reversal)
- **Jer 36** active impv. חֲתֻמִים analogue in the Jeremiah-scroll drama
- **Rev 10:4** σφράγισον … μὴ γράψῃς ↔ Rev 22:10 μὴ σφραγίσῃς — **Greek NT mirror-pair** reversing the command

**Grammar reference for Qal passive participle:** *no dedicated canonical entry yet* — [gap flagged](#gaps-for-library).

---

### 2. כִּי + Participial Clause — **Causal Ground**

**Parsing:** כִּי (Conj) introducing clauses 4–5 of the reply.

**Function:** כִּי with a **participial predicate-clause** (ETCBC Ptcp clause-type) typically marks **causal-ground** ("because, for") — supplying the reason for a preceding command or statement (Joüon §170d; Williams §444; IBHS §38.4a). The syntax is:

- *lēḵ Dāniyyēʾl* (clause 2–3 — the command + vocative)
- כִּי *sətumîm wa-ḥăṯumîm had-dəḇārîm …* (clauses 4–5 — the ground)

= **"Go thy way, Daniel — because the words [are in a state of being] shut-up and sealed until the time of the end."**

The כִּי does **not** introduce the content of what was said (content-כִּי would be rendered "that"); it introduces **why further inquiry is futile**. The angel dismisses Daniel with a causal ground, not a further revelation.

Parallel: Dan 8:26 כִּי לְיָמִים רַבִּים ("for [it pertains] to many days") — also a causal NmCl backing up a sealing imperative (סְתֹם הֶחָזוֹן). See [dan-8-26](dan-8-26.md).

---

### 3. לֵךְ (Qal impv. 2ms of הלך) — **Dismissal-Formula**

**Parsing:** Qal.Impv.2ms of הלך ("walk, go"), bare (no object, no directional particle, no pronominal suffix).

**Function:** `lēḵ` as an independent imperative-clause is a **dismissal-formula** — "go (and do no more)" / "go thy way" (KJV, Tyndale). It functions pragmatically to **close a speech-act**, not to direct literal locomotion. Parallel uses:

- **Dan 12:13** וְאַתָּה לֵךְ לַקֵּץ — the book's final word to Daniel: "go thou thy way until the end." This re-invokes the לֵךְ of v.9, extending it to the end of Daniel's own life ("thou shalt rest, and stand in thy lot at the end of the days").
- **Gen 12:1** לֶךְ־לְךָ — enhanced with ethical dative לְךָ, a calling-forth.
- **1 Sam 20:22** וְלֵךְ — dismissal with a purpose-particle.
- **2 Kings 5:19** לֵךְ לְשָׁלוֹם — peaceful-dismissal formula.

In Dan 12:9 the *bare* לֵךְ + vocative דָּנִיֵּאל is a stark dismissal. The angel is closing the question, not opening a destination. Dan 12:13's לֵךְ לַקֵּץ then reopens the dismissal with a terminus ("until the end"), framing the whole interval between v.9 and v.13 as the "go" — Daniel's remaining life.

See [imperative-mood](../hebrew/imperative-mood.md) for the general function of the Hebrew imperative.

---

### 4. הַדְּבָרִים — **The Subject (Definite Plural "The Words")**

**Parsing:** Art + Noun.mp.Abs — "the words," the definite plural of דָּבָר ([TR-dabar-laleo](../../word-studies/TR-dabar-laleo.md)). Masculine plural, definite by prefixed article ה.

**Antecedent question:** Which "words"? Three options the grammar permits:

1. **All of Daniel 10–12** (the entire long-vision revelation beginning at 10:1). The דְּבָרִים are what Daniel received in the vision of Hiddekel. Supported by v.4 where הַדְּבָרִים is paired with הַסֵּפֶר (the whole scroll/book of the vision). This is the majority reading.
2. **The specific oath-content of v.7** (time, times, half) — the most recent content of the reply Daniel just asked about.
3. **The content of vv.1–4** (resurrection oracle) — i.e., the eschatological kernel.

The grammar does not force a choice; the definite plural with no modifier simply anaphorically points to the prior content of the conversation. Note that the subject in v.4 is also הַדְּבָרִים (paired with הַסֵּפֶר) — making option 1 the most continuous reading: v.9 is restating what v.4 had commanded regarding the **same referent**.

**No book (הַסֵּפֶר) in v.9:** In v.4 Daniel is told to seal **both** the words and the book; in v.9 only **the words** are declared sealed. This is an **asymmetric recapitulation** — grammatically harmless (the plural הַדְּבָרִים can include the written record) but worth noting.

---

### 5. עַד־עֵת קֵץ — **Temporal Boundary (shared verbatim with v.4)**

**Parsing:** Prep עַד + construct chain עֵת קֵץ.

- עֵת — Noun.s.Cst (time-of), feminine singular construct of עֵת (H6256).
- קֵץ — Noun.ms.Abs (end), absolute masculine singular of קֵץ (H7093).

**Function:** Prepositional phrase functioning as **Time-adjunct** in the clause (ETCBC tag `[Time]` on clause 5). It provides the **terminus ad quem** — the time-boundary beyond which the sealed-state no longer holds. The absolute noun קֵץ is **indefinite** (no article, no suffix), which in construct-chain syntax usually **leaves the whole chain indefinite** ("a time-of end") — except that the eschatological usage of עֵת קֵץ across Daniel (8:17, 8:19 with מוֹעֵד, 11:35, 11:40, 12:4, 12:9) functions as a **quasi-definite technical term** through reference-cohesion, not through morphological definiteness.

The **preposition עַד** takes its object (the construct phrase) as the endpoint. עַד can be:
- **Inclusive** ("up to and including")
- **Exclusive** ("up to, not-beyond")

Grammar alone does not settle which. In context, the temporal limit עַד עֵת קֵץ implies the sealing **ceases at** the time of the end — i.e., at that point the words will no longer be סְתֻמִים וַחֲתֻמִים. This is confirmed by the NT mirror-pair: **Rev 22:10** μὴ σφραγίσῃς τοὺς λόγους τῆς προφητείας τοῦ βιβλίου τούτου, ὁ καιρὸς γὰρ ἐγγύς ἐστιν — explicitly reversing the Daniel-seal when the time-of-end is at hand.

See [dan-8-17-19](dan-8-17-19.md) for the עֵת / מוֹעֵד / קֵץ terminology cluster; [dan-12-7-11-12](dan-12-7-11-12.md) for the full Daniel-12 time-formula architecture.

---

## Syntactic-Rhetorical Analysis: Why Restate v.4 in v.9?

The v.4 → v.9 restatement is not redundancy; it is a **grammatical-pragmatic shift** triggered by Daniel's v.8 inquiry. Three observations hold at the grammar level:

### (a) Daniel's v.8 question re-opens what v.4 had closed

In v.4, the angel commanded Daniel to close the matter (active imperative). In v.8 Daniel, having *heard* (שָׁמַעְתִּי) but not *understood* (וְלֹא אָבִין, Qal impf. 1cs of בין ), explicitly re-opens the question: *"what [shall be] the end of these [things]?"* (מָה אַחֲרִית אֵלֶּה). The interrogative **מָה + Noun.fs.Cst אַחֲרִית + DemPron.p אֵלֶּה** is grammatically an inquiry for further revelation.

### (b) The angel's v.9 reply does NOT answer the question directly

The v.9 reply contains **zero new predictive content**. It has (i) dismissal (*lēḵ*), (ii) vocative (*Dāniyyēʾl*), (iii) causal ground (*kî* + twin passive-participles). The causal clause does not tell Daniel *what the end is*; it tells him *why he cannot know it further* — **because the words are already [in a state of being] sealed until the time of the end**.

### (c) The shift from impv. to passive ptcp. **re-asserts the closure as a settled state, not a fresh command**

If the angel had repeated the active imperatives (סְתֹם וַחֲתֹם), this would be a renewed command to Daniel — still actionable. The shift to Qal passive participle does two things:

1. **Removes Daniel's agency from the frame.** The words are no longer awaiting Daniel's sealing-action; they *are already* sealed. The command of v.4 has been executed (by whom is left open — by Daniel's reception of the vision, by the angel, by God).
2. **Predicates permanence-until-terminus on the state.** *qᵊtul* ptcp. + עַד-phrase constructs a **bounded-durative state**: "they are [and remain] sealed, until." The angel is not re-commanding; he is **describing a completed-and-ongoing condition**.

The pragmatic force is therefore a **grammaticalized refusal to answer** — the form "case closed" is built into the morphology. The imperative could be disobeyed; the passive-participial predication about a settled state cannot be "disobeyed," only *waited out*.

---

## The Relationship to vv.10–12: Are 1,290 / 1,335 the Sealed Words?

This is the principal interpretive crux generated by the v.9 grammar. Four grammatical facts constrain (without fully settling) the question:

### Fact 1 — The day-numbers in vv.11–12 come AFTER the sealing-declaration

Verse 9 says the words are sealed עַד עֵת קֵץ. Verses 11–12 immediately follow with two exact cardinal day-counts. **Grammatically, there is no barrier** to the angel continuing to speak after the sealing-declaration — the declaration is not a literary "end of speech" marker; the discourse continues through v.13.

### Fact 2 — v.10 intervenes with a statement on who will/will-not understand

Between v.9's seal and v.11's number comes v.10: יִתְבָּרֲרוּ וְיִתְלַבְּנוּ וְיִצָּרְפוּ רַבִּים (*"many shall be purified, made white, and tried"* — Hithpael impf. 3mp triad) — וְלֹא יָבִינוּ כָּל־רְשָׁעִים וְהַמַּשְׂכִּלִים יָבִינוּ (*"none of the wicked shall understand; but the wise [Hiphil ptcp. of שׂכל] shall understand"*). The **Qal impf. 3mp יָבִינוּ** (from בין, same root as v.8's אָבִין) is pointed at the same understanding-faculty Daniel just confessed he lacked. Grammatically, v.10 **forecasts a future understanding** — limited to הַמַּשְׂכִּלִים ("the wise/the insight-bearers"), withheld from רְשָׁעִים.

### Fact 3 — The day-numbers are given without interpretation

Vv.11–12 supply:
- **1,290 days** — counted from מֵעֵת הוּסַר הַתָּמִיד (Hophal perf. 3ms "from the time that the תָּמִיד was-caused-to-be-removed") + וְלָתֵת שִׁקּוּץ שֹׁמֵם (Qal InfCst "and the giving/setting up of an abomination making-desolate").
- **1,335 days** — blessing-span for הַמְחַכֶּה (Piel ptcp. "the one who waits").

The numbers are **morphologically exact cardinal numerals** — no symbolic tagging, no interpretive gloss — see [dan-12-7-11-12](dan-12-7-11-12.md) for full morphology. This **stands in tension** with v.9's sealing declaration: the angel appears to give *more* information *after* declaring the matter sealed.

### Fact 4 — No grammatical marker distinguishes "sealed" from "unsealed" content

There is no particle, discourse-marker, or syntactic break that tells the reader: "the words-before-v.9 are sealed; the words-after-v.10 are not." The whole of chapters 10–12 is delivered as a single continuous speech-event (one *dibber-bbo* frame opened in 10:11).

### Four Interpretive Positions the Grammar Leaves Open

**Option A — The numbers are PART of what is sealed.**
Grammar-support: The continuity of הַדְּבָרִים across 10:1 → 12:9 → 12:13 is unbroken. The angel's "sealing-declaration" can cover *all* the content, including what follows, because in Hebrew narrative a sealing-formula can be retrospective over the whole utterance (cf. Isa 8:16 חֲתוֹם תּוֹרָה בְּלִמֻּדָי "seal the instruction [given] to my disciples" — sealing the already-given teaching). On this reading v.10 + vv.11–12 are **part of the sealed material**, to be understood by הַמַּשְׂכִּלִים only at the time of the end (v.10 תַּבִּין semantics). — Historicist tradition, Adventist expositors (Andrews, Haskell), some patristic (Hippolytus).

**Option B — The numbers are a PARTIAL UNSEALING / concession to Daniel's question.**
Grammar-support: Question-answer adjacency-pair pragmatics — Daniel asks *what is the end*, receives a dismissal (v.9) but then receives **quantitative information** (vv.11–12) that does measure toward an end. The seal is real but not absolute; the angel grants a bounded numerical disclosure within the sealed envelope. Rev 10 "open little scroll" typologically supports a partial-unsealing rhythm. — Some Reformed (Calvin), some early Adventist (Miller bridge).

**Option C — The numbers are PROTECTED by the seal (understood only at time-of-end).**
Grammar-support: v.9's sealing and v.10's *and-none-of-the-wicked-shall-understand / but-the-wise-shall-understand* are paired. The grammar presents understanding as **agent-distributed** (רְשָׁעִים ↔ הַמַּשְׂכִּלִים) not **content-distributed**. So vv.11–12 are given in plain cardinal form, but their **meaning** is sealed until the time-of-end when הַמַּשְׂכִּלִים will penetrate them. — Classical historicist day-year view (see [day-year-formula](../hebrew/day-year-formula.md)), Keil, Young, Hengstenberg.

**Option D — Vv.11–12 are not what the seal targets.**
Grammar-support: The most recent antecedent of הַדְּבָרִים may be the immediately-prior oath (v.7) or the resurrection oracle (vv.1–3) or chs.10–11 war-chronicle — with vv.11–12 *post-seal* as new material given after and outside the sealed corpus. The grammar does not prevent this, because הַדְּבָרִים has no modifier constraining its scope. — Futurist dispensational and some preterist readings.

All four positions are **grammatically licensed**. The morphology of סְתֻמִים / חֲתֻמִים establishes the state; it does not specify the state's content-scope.

---

## Settled-State Question: Does the Qal Passive Ptcp. Bar Further Inquiry?

The question raised in the intake was: *Does the passive participle express a settled state that Daniel cannot penetrate, effectively a "case closed" on inquiry until עֵת קֵץ?*

**Grammatically — yes, for Daniel.** Three factors converge:

1. **Stative-resultative aspect of *qᵊtul*** — the state has been established; the agent-slot is closed; the form resists being "undone" by further request.
2. **כִּי-causal clause backing *lēḵ*** — the sealing-state is offered as the **reason** Daniel must depart without more answers, not as a temporary obstacle to be negotiated.
3. **עַד-boundary deferring the unsealing to עֵת קֵץ** — the unsealing is future-indexed to a time Daniel does not inhabit (cf. 12:13 "thou shalt rest … at the end of the days").

**But not for all time.** The *qᵊtul* state is bounded by the עַד-phrase: at the time-of-end the state dissolves. The grammar thus creates a **temporally bounded hermeneutical darkness** — opaque to Daniel and his generation, transparent to the generation living at עֵת קֵץ. This is reinforced by v.10's agent-distribution (*"the wise shall understand"*, future tense), positioning comprehension on the far side of the seal.

The **NT mirror** makes this explicit:
- Dan 12:9 סְתֻמִים וַחֲתֻמִים הַדְּבָרִים עַד עֵת קֵץ
- Rev 22:10 μὴ σφραγίσῃς τοὺς λόγους … ὁ καιρὸς γὰρ ἐγγύς

The "seal" is **grammatically binding on inquiry during the interval** and **grammatically null at the interval's end**.

---

## Cross-References

### Grammar library
- [imperative-mood](../hebrew/imperative-mood.md) — general function of the Hebrew imperative (relevant to v.4 active impv.)
- [stem-niphal](../hebrew/stem-niphal.md) — the other main Hebrew passive-voice mechanism (contrast with Qal passive ptcp.)
- [qal-imperfect](../hebrew/qal-imperfect.md) — modal/tense reference for related Daniel forms
- [day-year-formula](../hebrew/day-year-formula.md) — relevant to interpretive options on vv.11–12

### Passage library
- [dan-12-7-11-12](dan-12-7-11-12.md) — the time-formulas (v.7 "time, times, half" + vv.11–12 1,290 / 1,335 day counts) that surround v.9 on both sides
- [dan-8-17-19](dan-8-17-19.md) — the עֵת קֵץ / מוֹעֵד קֵץ terminology cluster
- [dan-8-26](dan-8-26.md) — the **first** sealing imperative (סְתֹם הֶחָזוֹן) + parallel כִּי-causal NmCl + the סתם / חתם lexical-distinction discussion
- [dan-9-24-27](dan-9-24-27.md) — the seventy-weeks oracle using a different set of "seal" verbs (חתם + חתך + חרץ)
- [dan-11-36-37](dan-11-36-37.md) — the chapter-11 predictive-prose leading into ch.12
- [rev-13-5](rev-13-5.md) / [mat-24-15-mk-13-14-abomination](mat-24-15-mk-13-14-abomination.md) — NT re-use of the Daniel time-of-end / abomination cluster

### Word studies
- [H5640-catham](../../word-studies/H5640-catham.md) — **סתם** full lexical profile (17 tokens, 14 verses, figurative "shut up / closed up" cluster in Daniel)
- [H2856-chatham](../../word-studies/H2856-chatham.md) — **חתם** full lexical profile (26 tokens, seal-cluster in Daniel, Esther, Job, Isaiah)
- [WG-sealing](../../word-studies/WG-sealing.md) — thematic cross-testament sealing word-group study (Hebrew חתם / סתם ↔ Greek σφραγίζω / σφραγίς)
- [TR-dabar-laleo](../../word-studies/TR-dabar-laleo.md) — דָּבָר ↔ λόγος translation-relation, relevant to הַדְּבָרִים → οἱ λόγοι of Rev 22:10

---

## Gaps for Library

Entries flagged for future grammar-reference canonicalization:

- **qal-passive-participle.md** (`hebrew/`) — the *qᵊtul* morphological pattern, its stative-resultative function, contrast with Niphal passive, and predicative use in Ptcp-clauses. Currently explained inline in multiple passage-analyses (Gen 9:25 ארור, Dan 12:9 סתמים/חתמים, Isa 53:5 candidates). Central enough to warrant a canonical entry.
- **ki-causal-clause.md** (`hebrew/`) — the כִּי-causal-ground syntax as distinct from כִּי-content ("that"), כִּי-temporal ("when"), כִּי-adversative ("but").
- **dismissal-lek-formula.md** (`hebrew/`) — the bare לֵךְ + vocative as a pragmatic dismissal speech-act (Dan 12:9, 12:13; Gen 12:1; 2 Kgs 5:19 etc.).

---

## Summary (grammar-level only)

Daniel 12:9 is a five-clause angelic reply whose grammatical signature is the **shift from active Qal imperative (v.4 סְתֹם / חֲתֹם) to Qal passive participle (v.9 סְתֻמִים / חֲתֻמִים)**. The shift converts a **command to act** into a **declaration of a settled state**, closes Daniel's agency in the sealing, suppresses the agent entirely, and binds the state to a temporal terminus (עַד עֵת קֵץ) identical to v.4's. The כִּי-clause functions as causal ground for the dismissal-imperative לֵךְ, and the whole structure grammatically refuses Daniel's v.8 inquiry. Whether vv.11–12's day-numbers fall inside or outside the sealed corpus is **not resolved by the grammar** — four interpretive options remain open, constrained only by the continuity of הַדְּבָרִים as a plural-definite anaphor and by v.10's agent-distributed future-understanding formula.
