# Grammar Analysis: Daniel 12:4 — The Seal-Book Command

**Context-neutral passage analysis.** This entry describes the Hebrew morphology and clause architecture of Daniel 12:4 — the closing command of the final Danielic oracle in which Gabriel/the-angelic-messenger directs the seer to seal the finished text until "the time of end," appended with a twofold prediction about activity-and-knowledge in that future era. Three grammatical features drive the exegesis:

1. **Dual Qal imperative pair** סְתֹם … וַחֲתֹם — two parallel 2ms imperatives governing two different objects (הַדְּבָרִים "the words" / הַסֵּפֶר "the book/scroll") — *not* the single-verb form of Dan 8:26, *not* the two-infinitive form of Dan 9:24, and *not* the paired-passive-participle form of Dan 12:9. The verse uniquely deploys both sealing verbs in the imperative mood simultaneously.
2. **Temporal boundary** עַד־עֵת קֵץ — preposition עַד ("until, up to") + construct chain עֵת־קֵץ ("time of end"), establishing not just a long duration (cf. יָמִים רַבִּים of 8:26) but a specific terminus after which the sealed condition no longer obtains.
3. **Post-boundary coda** יְשֹׁטְטוּ רַבִּים וְתִרְבֶּה הַדָּעַת — Piel imperfect 3mp of שׁוט ("rove about") + Qal imperfect 3fs of רבה ("be/become many, increase"), two parallel imperfects describing activity that follows, or is triggered by, the reaching of the temporal boundary.

Interpretive schools (sealed-until-hidden / sealed-until-authenticated / both-and) are catalogued in §Interpretive Options, not adjudicated.

---

## Text

**Hebrew (BHS/ETCBC):**

וְאַתָּ֣ה דָֽנִיֵּ֗אל סְתֹ֧ם הַדְּבָרִ֛ים וַחֲתֹ֥ם הַסֵּ֖פֶר עַד־עֵ֣ת קֵ֑ץ יְשֹׁטְט֥וּ רַבִּ֖ים וְתִרְבֶּ֥ה הַדָּֽעַת׃

**KJV:** But thou, O Daniel, shut up the words, and seal the book, [even] to the time of the end: many shall run to and fro, and knowledge shall be increased.

---

## Word-by-Word Parsing

*Morphological data below from direct `hebrew_parser.py --verse "Dan 12:4"` call (ETCBC/BHSA 2021).*

| #  | Word         | Lemma  | Parsing                  | Gloss        |
|----|--------------|--------|--------------------------|--------------|
| 1  | וְ           | ו      | Conj                     | and          |
| 2  | אַתָּה        | אתה    | PersPron.2ms             | you          |
| 3  | דָנִיֵּאל    | דניאל  | PropN.ms.Abs             | Daniel       |
| 4  | סְתֹם        | סתם    | **Verb.Qal.Impv.2ms**    | stop up      |
| 5  | הַ           | ה      | Art                      | the          |
| 6  | דְּבָרִים    | דבר    | Noun.mp.Abs              | words        |
| 7  | וַ           | ו      | Conj                     | and          |
| 8  | חֲתֹם        | חתם    | **Verb.Qal.Impv.2ms**    | seal         |
| 9  | הַ           | ה      | Art                      | the          |
| 10 | סֵּפֶר       | ספר    | Noun.ms.Abs              | book/scroll  |
| 11 | עַד          | עד     | Prep                     | unto/until   |
| 12 | עֵת          | עת     | Noun.s.Cst               | time (of)    |
| 13 | קֵץ          | קץ     | Noun.ms.Abs              | end          |
| 14 | יְשֹׁטְטוּ   | שׁוט   | **Verb.Piel.Impf.3mp**   | rove about   |
| 15 | רַבִּים      | רב     | Adj.mp.Abs (subst.)      | many         |
| 16 | וְ           | ו      | Conj                     | and          |
| 17 | תִרְבֶּה     | רבה    | **Verb.Qal.Impf.3fs**    | be many/increase |
| 18 | הַ           | ה      | Art                      | the          |
| 19 | דָּעַת       | דעת    | Noun.fs.Abs              | knowledge    |

---

## Clause Structure (ETCBC)

| # | Type | Domain | Function / Text |
|---|------|--------|-----------------|
| 1 | **WXIm** (Waw + X + Impv.) | Q (angelic quotation) | וְאַתָּה סְתֹם הַדְּבָרִים — "and (as for) you — shut up the words" <br>• [Conj] וְ  • [Subj] אַתָּה  • [Pred] סְתֹם  • [Objc] הַדְּבָרִים |
| 2 | **Voct** (vocative) | Q | דָנִיֵּאל — "O Daniel" (stand-alone vocative clause inserted between clause 1's subject/predicate and clause 3) |
| 3 | **WIm0** (Waw + Impv. + zero subject) | Q | וַחֲתֹם הַסֵּפֶר עַד־עֵת קֵץ — "and seal the book, until the time of end" <br>• [Conj] וַ  • [Pred] חֲתֹם  • [Objc] הַסֵּפֶר  • [Time] עַד־עֵת קֵץ |
| 4 | **ZYqX** (Zero-conj + Yiqtol + X-subject) | Q | יְשֹׁטְטוּ רַבִּים — "many shall rove about" <br>• [Pred] יְשֹׁטְטוּ  • [Subj] רַבִּים |
| 5 | **WYqX** (Waw + Yiqtol + X-subject) | Q | וְתִרְבֶּה הַדָּעַת — "and the knowledge shall increase" <br>• [Conj] וְ  • [Pred] תִרְבֶּה  • [Subj] הַדָּעַת |

**Architectural summary.** Five clauses form a tight chiastic / bipartite structure:

- **(1–3) Command triad:** topic-marker clause (וְאַתָּה סְתֹם …) / vocative (דָנִיֵּאל) / second imperative clause (וַחֲתֹם … עַד־עֵת קֵץ). The vocative is wedged between the two imperatives — it names the addressee at the hinge, making clear that *both* imperatives share the same 2ms subject.
- **(4–5) Prediction pair:** two yiqtol clauses (ZYqX + WYqX) describing a future state of affairs that obtains at, or after, the terminus marked in clause 3.

Clauses 4–5 are **asyndetically joined to clauses 1–3** — there is no waw or כִּי linking יְשֹׁטְטוּ to the preceding imperative. The asyndeton is syntactically significant: BH can join two propositions with waw (continuous/sequential), with כִּי (causal), or asyndetically (juxtapositional). The asyndetic juxtaposition leaves open whether clauses 4–5 give the *reason* for sealing (causal: "seal, because many will run to and fro …"), the *result* of reaching the terminus (consequential: "seal until end; [then] many shall run …"), or a *concurrent characterization of the many-days interval* (circumstantial: "seal … while many rove, and knowledge grows"). English translations that insert "[even]" (KJV) or ":" (RSV) conceal this open-endedness.

See [syntax-waw-conjunction](../hebrew/syntax-waw-conjunction.md) on the topic-shifting waw in וְאַתָּה and the sequential waw in וַחֲתֹם; see [qal-imperfect](../hebrew/qal-imperfect.md) for the yiqtol forms in clauses 4–5.

---

## Construct Chain

| Construct | Absolute | Gloss |
|-----------|----------|-------|
| עֵת | קֵץ | "time of [the] end" |

**Notes on the chain.** עֵת־קֵץ is a two-term construct chain with the construct noun עֵת (fs, lemma עת, H6256 "time, appointed moment") governing the absolute קֵץ (ms, lemma קץ, H7093 "end, limit, terminus"). The chain is anarthrous (neither noun is articled), which in BH construct chains typically leaves definiteness indeterminate — the phrase can mean "(a/the) time of (an/the) end." Because קֵץ in Daniel's eschatological vocabulary is a *technical term* (cf. 8:17, 19; 11:35, 40; 12:4, 6, 9, 13), the anarthrous form does not diminish its specificity: in Danielic idiom עֵת קֵץ designates *the* eschatological end-time without requiring the article (a known pattern where technical terms achieve definiteness via genre/semantics, not morphology — Joüon-Muraoka §137n; Waltke-O'Connor §13.4).

**Preposition עַד + construct chain.** עַד takes the following noun phrase as its object; here it governs the whole chain עֵת־קֵץ: "*until* [the] time of [the] end." עַד denotes a terminus ad quem — the reaching of which ends the preceding state (here: the sealed-up condition). It differs from לְ (as in 8:26 לְיָמִים רַבִּים) in that עַד specifies a *boundary* after which the state terminates, while לְ specifies *duration/orientation* without an explicit termination event. The Dan 12:4 grammar is therefore more decisive than Dan 8:26: v. 4 marks an end-point, v. 8:26 marks an extent.

---

## Key Grammatical Features

### 1. The dual Qal imperatives סְתֹם … וַחֲתֹם — double-verb sealing command

**Morphology.**
- סְתֹם — Qal imperative 2ms (`Verb.Qal.Impv.2ms`) of סתם (H5640), basic sense "stop up, shut up, close, keep secret, conceal." Unexpanded imperative (no לֹ/ה-suffix for emphasis/politeness), carrying direct-command force.
- וַחֲתֹם — waw-conjunctive + Qal imperative 2ms (`Verb.Qal.Impv.2ms`) of חתם (H2856), basic sense "affix a seal, seal with a seal, seal up [a document]." The waw here is coordinative (linking two imperatives of equal force), not consecutive (which would be weqatal with a perfect form). Both verbs share the same 2ms subject (Daniel) and share the same temporal modifier עַד־עֵת קֵץ, though the time-phrase is syntactically attached to the second verb's clause.

**Why two verbs rather than one.** The use of both סתם and חתם — rather than either alone — is distinctive to Dan 12:4 and 12:9. The two verbs are not synonymous:

| Verb | H# | Basic sense | Emphasis |
|------|----|-------------|----------|
| סתם | H5640 | stop up, close, shut, keep secret | **Concealment / preventing access to content** |
| חתם | H2856 | affix seal, seal (a document, letter, decree) | **Authentication / formalizing the document's integrity** |

In ANE legal-documentary practice, a deed or letter was often *written* on papyrus or parchment, then *rolled or folded*, then *sealed* with a clay or wax seal-impression. The seal did two things simultaneously: (i) it *prevented opening* without evidence of tampering (the concealment function), and (ii) it *authenticated authorship* by the imprint of the signer's personal seal (the authentication function). In fact most ANE legal documents were "double-sealed" — written twice, with one copy left open for consultation and one sealed copy kept for tamper-evident verification (e.g., Jer 32:9–14, הַסֵּפֶר הֶחָתוּם … וְאֶת־הַגָּלוּי "the sealed document … and the open one"). The pair סתם + חתם captures both functions:

- **סְתֹם הַדְּבָרִים** — "close up *the words*" (the content, the speech-events, what was said) — **conceal the meaning / prevent access to interpretation**.
- **חֲתֹם הַסֵּפֶר** — "seal *the book/scroll*" (the physical document) — **authenticate the record / guarantee its integrity as Daniel's writing**.

The *objects* are different as well as the *verbs*. Hebrew sometimes uses parallel verbs with the same object (one object governed by both); here Hebrew uses parallel verbs each with its own object, a more deliberate construction. The two objects are:

- **הַדְּבָרִים** — "the words" (mp, lemma דבר, H1697). In Daniel the דְּבָרִים are the angelic/prophetic speech-content — the oracular material just delivered (cf. 10:9, 11, 12; 12:9 repeats הַדְּבָרִים). The noun has both a speech-dimension (things said) and a content-dimension (matters, affairs) — see [TR-dabar-laleo](../../word-studies/TR-dabar-laleo.md).
- **הַסֵּפֶר** — "the book/scroll" (ms, lemma ספר, H5612). The physical writing-artifact. In Dan 12 it is the scroll of Daniel's own prophecy — the finished written record, not merely an abstract message. Elsewhere in Daniel סֵפֶר refers to books of inquiry/record (9:2 בַּסְּפָרִים "in the books" — Jeremiah's writings) and to heavenly books (7:10 סִפְרִין פְּתִיחוּ "books were opened" — Aramaic).

The pairing therefore distinguishes the *signified* (דְּבָרִים = the oracle's semantic content) from the *signifier* (סֵפֶר = the physical manuscript). Concealing the words and sealing the book together perform a comprehensive closure: both *what is said* and *the medium in which it is preserved* are placed in a tamper-evident, interpretation-deferred state.

**Contrast with Dan 8:26, 9:24, and 12:9.** The sealing-family in Daniel deploys different morphological configurations, each with its own grammatical force:

| Reference | Construction | Verbs | Objects | Tense/Mood |
|-----------|--------------|-------|---------|------------|
| Dan 8:26 | `סְתֹם הֶחָזוֹן` | only סתם (H5640) | הֶחָזוֹן ("the vision") | Qal Impv. 2ms (command) — **single verb, single object** |
| Dan 9:24 | `לַחְתֹּם חָזוֹן וְנָבִיא` | only חתם (H2856) | חָזוֹן וְנָבִיא ("vision and prophet") | Qal InfCst with לְ (purpose / one of 6 coordinated purpose-infinitives) — **single verb, coordinated objects, infinitival mood** |
| Dan 12:4 | `סְתֹם הַדְּבָרִים וַחֲתֹם הַסֵּפֶר` | **both** סתם + חתם | הַדְּבָרִים ("words") + הַסֵּפֶר ("book") | Qal Impv. 2ms pair (command) — **double verb, double object** |
| Dan 12:9 | `סְתֻמִים וַחֲתֻמִים הַדְּבָרִים` | **both** סתם + חתם | הַדְּבָרִים ("words") alone | Qal **passive participle** mp pair (state-report) — **double verb, single object** |

The progression across the book is pointed:

1. **8:26** commands concealment only (סתם), for a long but unspecified duration (יָמִים רַבִּים).
2. **9:24** mentions sealing (חתם) alone, but within an infinitival purpose clause embedded in the Seventy-Weeks decree — it is one of six things that "are determined upon your people," and its object is the *visionary-prophetic content itself* (חָזוֹן וְנָבִיא) as a theological category, not the book-qua-document. The infinitival construction (*to seal up vision and prophecy*) describes a prophetic-fulfillment/cessation rather than a concealment-until-time act.
3. **12:4** commands *both* concealment and sealing, with distinct objects (words / book), with a definite boundary (עַד־עֵת קֵץ).
4. **12:9** reports back the *completed state* — both concealment and sealing have been applied; the verbs are now passive participles (סְתֻמִים "are-closed-up" / חֲתֻמִים "are-sealed"), declaring a static-resultative condition. The single shared object (הַדְּבָרִים) in 12:9 telescopes the two objects of 12:4 — the sealed book *is* the words-in-their-preserved-form.

Thus the four passages trace a trajectory: 8:26 (conceal, command) → 9:24 (seal, infinitival-purpose, different sense) → 12:4 (conceal+seal, command, two objects) → 12:9 (concealed+sealed, state, one object). The commands of 8:26 and 12:4 are fulfilled by the state reported in 12:9; the infinitival-purpose of 9:24 belongs to a different theological grammar (the *cessation/fulfillment* of prophecy rather than its *custodial concealment*). See [dan-8-26](dan-8-26.md) for the first-step command; [dan-9-24-27](dan-9-24-27.md) for the Seventy-Weeks infinitival purposes; [dan-12-7-11-12](dan-12-7-11-12.md) for the surrounding time-markers of Dan 12.

**Why Daniel is the addressee.** As in 8:26, the imperative is 2ms singular with explicit pronoun וְאַתָּה ("and *you*"). The pronoun is pragmatically redundant (the 2ms imperative ending already encodes the subject) but functions as a topic-shift marker: it pivots from the preceding angelic speech about the end-time to a direct address to Daniel personally. This same topic-shift pattern opens 8:26 (וְאַתָּה סְתֹם) and is a feature of direct angelic commissioning. The vocative דָנִיֵּאל wedged between the two imperatives makes the personal address doubly explicit — Daniel is named at the hinge of the dual command. See [imperative-mood](../hebrew/imperative-mood.md) for the general functions of BH imperatives.

For the full verbal fields see [H5640-catham](../../word-studies/H5640-catham.md) and [H2856-chatham](../../word-studies/H2856-chatham.md); for the objects see דבר / ספר (candidates for future word-study entries).

---

### 2. עַד־עֵת קֵץ — "until time of end" — the temporal boundary

**Morphology.**
- עַד — preposition, "unto, as far as, until, up to." Takes a noun phrase as complement. Unlike לְ (which indicates orientation or duration-toward), עַד marks a *terminus ad quem* — a boundary that *ends* the preceding state. With temporal complements עַד specifies the moment *after which* the state no longer obtains.
- עֵת — Noun.s.Cst (lemma עת, H6256), construct form of עֵת "time, season, appointed moment." In Daniel's eschatological vocabulary עֵת carries the sense of a *definite, ordained moment* rather than generic "time" (Greek χρόνος) — closer to καιρός.
- קֵץ — Noun.ms.Abs (lemma קץ, H7093), "end, limit, terminus, termination." In Daniel (8:17, 19; 9:26; 11:6, 13, 27, 35, 40, 45; 12:4, 6, 9, 13) קֵץ is a technical term for the eschatological termination of the vision's reach.

**The preposition's exegetical force.** עַד-with-temporal-terminus carries semantic content that is not interchangeable with לְ or בְּ:

- **עַד X** — the state/action continues *until* X, *and then terminates*. E.g., Gen 3:19 עַד שׁוּבְךָ אֶל־הָאֲדָמָה "until your return to the ground" (and then the state changes — you become dust); Dan 7:22 עַד־אֲתָה עַתִּיק יוֹמַיָּא "until the Ancient of Days came" (and then a change: judgment was rendered).
- **לְ X** — the state is *for/unto* X, without necessarily ending at X. E.g., Dan 8:26 לְיָמִים רַבִּים "for many days" — the vision *pertains to* many days, without specifying that its sealed condition terminates at their conclusion.
- **בְּ X** — the state obtains *in/at* X. E.g., Dan 11:40 וּבְעֵת קֵץ "and in the time of end" — at that temporal locus (not before, not after, without implying termination of a prior state).

Dan 12:4's choice of **עַד** is therefore stronger than Dan 8:26's **לְ**. The 8:26 command-grammar leaves open whether, and when, the sealed condition lifts; the 12:4 grammar specifies that the sealed condition *has a terminus*, namely עֵת־קֵץ. This difference in preposition is exegetically decisive: something that is sealed עַד־עֵת קֵץ is, by the semantics of the preposition alone, *no longer sealed after* that boundary is crossed.

**The construct chain עֵת־קֵץ as technical term.** In Daniel the bare phrase עֵת קֵץ (or its synonym מוֹעֵד קֵץ 8:19) functions as a technical designation for the eschatological end-period — distinct from:

- יָמִים רַבִּים (8:26) — "many days," a quantitative long duration without a defined terminus-event
- אַחֲרִית הַיָּמִים (2:28; 10:14) — "latter days," the generic canonical eschatological period
- מוֹעֵד (8:19; 11:27, 29, 35; 12:7) — "appointed time," a determined-moment formula
- קֵץ הַיָּמִים / קֵץ הַיָּמִין (12:13) — "end of the days / end of [your] days"

The six occurrences of עֵת קֵץ in Daniel (8:17, 19 [מוֹעֵד קֵץ]; 11:35, 40; 12:4, 9) bracket the book's two major eschatological arcs: the 2,300-evening-morning oracle (ch. 8) and the time-of-end oracle (chs. 11–12). In both arcs, עֵת קֵץ names the same horizon — the period in which the prophecy's fulfillment is manifestly consummated.

See [dan-8-26](dan-8-26.md) for the contrast with יָמִים רַבִּים and for the table of Daniel's "long-time" idioms; see [dan-12-7-11-12](dan-12-7-11-12.md) for the specific day-counts (1290, 1335) associated with the עֵת קֵץ region.

---

### 3. יְשֹׁטְטוּ רַבִּים — "many shall rove about"

**Morphology.**
- יְשֹׁטְטוּ — **Piel imperfect 3mp** (`Verb.Piel.Impf.3mp`) of שׁוט (H7751), "rove, roam, run to and fro, go about." The Piel is intensive/iterative: in Qal שׁוט is attested for "roving" motion (Num 11:8); in Piel the nuance is "go eagerly to and fro, roam intensively, range widely." See [stem-piel](../hebrew/stem-piel.md) (if present) for the Piel's general iterative/intensive functions.
- רַבִּים — Adj.mp.Abs (lemma רב, H7227) "many, numerous, great." Here substantivized — functioning as the subject of יְשֹׁטְטוּ ("many [ones]"). BH substantivizes adjectives freely, especially in plural.

**The verb שׁוט (Piel) — what kind of "roving"?** The root appears in Qal (Num 11:8; 2 Sam 24:2, 8; Job 1:7; 2:2; Jer 5:1; Ezek 27:8, 26; Zech 4:10), in Polel (not present here), and in Piel (Dan 12:4; Jer 49:3 uncertain; 2 Sam 24:2 in some witnesses). Semantic range:

- **Survey-motion.** 2 Sam 24:2, 8 שׁוּטוּ־נָא בְּכָל־שִׁבְטֵי יִשְׂרָאֵל — "go to and fro through all the tribes" for census.
- **Search-motion.** Jer 5:1 שׁוֹטְטוּ בְּחוּצוֹת יְרוּשָׁלִַם … וְחַפְּשׂוּ־נָא בִרְחוֹבוֹתֶיהָ אִם־תִּמְצְאוּ אִישׁ — "go to and fro through the streets of Jerusalem … and search in her squares; see if you can find a man [who does justice]" (roving + searching conjoined).
- **Investigative-motion.** Job 1:7; 2:2 מִשּׁוּט בָּאָרֶץ — the Satan "from roving in the earth" (reconnaissance).
- **Divine-surveillance-motion.** Zech 4:10 עֵינֵי יְהוָה הֵמָּה מְשׁוֹטְטִים בְּכָל־הָאָרֶץ — "the eyes of YHWH … roam through all the earth" (comprehensive divine inspection).

In none of these cases does שׁוט mean "ignorant rushing" or "aimless wandering." The verb consistently denotes *purposeful, searching, investigative motion* — roving for the sake of finding. This bears on the exegesis of Dan 12:4: the many who "rove to and fro" are not depicted as confused or chaotic; they are depicted as *searching*. The Piel intensive stem further strengthens the iterative, searching nuance: they rove *intensively* or *repeatedly*.

**An alternative reading tradition.** Some modern translations render יְשֹׁטְטוּ as "run to and fro" in the sense of hurried movement (KJV, RSV, ESV). Others render it as "search" or "study carefully" (several Jewish-tradition glosses and Adventist-historicist readings). The verb's semantic field supports both surface-reading ("roam, run") and deeper-reading ("investigate, search"). The Piel stem favors the intensive reading; the context (paired with וְתִרְבֶּה הַדָּעַת "and knowledge shall increase") favors the investigative reading, since the result of intensified investigation is naturally *increased knowledge*. The LXX renders ἕως διδαχθῶσιν πολλοὶ καὶ πληθυνθῇ ἡ γνῶσις "until many be taught and knowledge be multiplied" — a reading-tradition that interprets יְשֹׁטְטוּ as *searching/learning activity* rather than mere physical roving. (Theodotion has ἕως διδαχθῶσιν πολλοί.) The grammar of the verb by itself does not force a choice; it permits either literal-motion or metaphorical-search readings.

**Subject רַבִּים — "many" — who are they?** The substantivized adjective is indefinite: "many [people]." It does not specify *which* many. The construction parallels the רַבִּים of the Fourth Servant Song (Isa 52:14, 15; 53:11, 12) and of Dan 11:33, 39; 12:2, 3 (הַמַּצְדִּיקִים הָרַבִּים "those who bring the many to righteousness"), where רַבִּים designates a generalized large group — often the recipients of teaching or the participants in eschatological outcomes. In Dan 12:2 the רַבִּים who rise from the dust "to everlasting life" are the raised many; in 12:3 the wise lead "the many" (הָרַבִּים) to righteousness. The רַבִּים of 12:4 echo this vocabulary: many [are the ones who] search / rove.

---

### 4. וְתִרְבֶּה הַדָּעַת — "and the knowledge shall increase"

**Morphology.**
- וְ — coordinating conjunction joining clause 5 to clause 4. Because clause 4 is a yiqtol (imperfect) form and clause 5 is also yiqtol, the waw here is a standard coordinative waw (not weqatal converted-future), linking two parallel future-oriented predictions.
- תִרְבֶּה — **Qal imperfect 3fs** (`Verb.Qal.Impf.3fs`) of רבה (H7235), "be/become many, multiply, increase, grow numerous." The III-ה class (weak third-radical he) collapses the ending to -ֶה; the 3fs prefix is ת־ with a segolate pattern on the stem. The Qal of רבה is intransitive ("become many"), not transitive ("make many" — that is the Hiphil הִרְבָּה). Therefore the clause is: "and knowledge *shall-grow-many*" / "*shall-increase*" — knowledge is the grammatical subject, the one becoming numerous. See [qal-imperfect](../hebrew/qal-imperfect.md) for the general yiqtol functions (predictive, habitual, modal).
- הַ — definite article.
- דָּעַת — Noun.fs.Abs (lemma דעת, H1847) "knowledge, skill, discernment, knowing." The article renders this *the* knowledge — anaphoric or generic-definite ("knowledge [in general / at-that-time]"). Distinguish from lemma יָדַע (H3045) "know [the verb]," from which דַּעַת is morphologically derived (infinitive-construct form functioning substantivally).

**What kind of "knowledge"?** דַּעַת is Biblical Hebrew's general-purpose noun for "knowledge, knowing, discernment." It covers:

- **Knowledge of facts.** Prov 2:10 כִּי־תָבוֹא חָכְמָה בְלִבֶּךָ וְדַעַת לְנַפְשְׁךָ יִנְעָם — "when wisdom enters your heart, and knowledge becomes pleasant to your soul."
- **Knowledge of YHWH.** Hos 4:1, 6 אֵין־דַּעַת אֱלֹהִים בָּאָרֶץ … נִדְמוּ עַמִּי מִבְּלִי הַדָּעַת — "there is no knowledge of God in the land … my people perish for lack of knowledge."
- **Eschatological-knowledge.** Isa 11:9 כִּי־מָלְאָה הָאָרֶץ דֵּעָה אֶת־יְהוָה (cognate form דֵּעָה) — "for the earth shall be full of the knowledge of YHWH."
- **Wisdom-school learning.** Prov 1:4, 7, 22, 29; 2:5, 6; 3:20; 8:9, 10, 12; 9:10; 10:14; 11:9; 12:1; 13:16; 14:6, 7, 18; 15:2, 7, 14; 17:27; 18:15 — knowledge as the fruit of instruction.

The noun is semantically broad. In Dan 12:4 the grammar leaves the content of "knowledge" unspecified: it is simply "(the) knowledge" that will increase. Possible referents are:

- Knowledge of the sealed oracle itself (the one just sealed) — resolving the concealment of clauses 1–3 at the terminus marked by עַד־עֵת קֵץ.
- Knowledge in general (secular/scientific/technological) — a broad eschatological expansion of human knowing coincident with the end.
- Knowledge of eschatological realities (the "time of end" becoming recognizable) — the oracle's *fulfillment* becoming perceivable.
- Knowledge of God / prophetic-understanding among the searchers — parallel to Isa 11:9 and Hab 2:14.

Grammatically these are indistinguishable; the article הַ does not specify which knowledge. Context (the sealing command, the roving/searching of רַבִּים, the terminus עֵת קֵץ) invites correlation with the sealed oracle itself, but the grammar does not compel that reading.

**The parallelism of clauses 4 and 5.** The two clauses are *chiastically parallel*:

- Clause 4: [Pred] יְשֹׁטְטוּ (Piel impf.) + [Subj] רַבִּים (substantivized adj., grammatically indefinite)
- Clause 5: [Conj] וְ + [Pred] תִרְבֶּה (Qal impf.) + [Subj] הַדָּעַת (definite noun)

The subjects move from *indefinite-substantivized-adjective* (רַבִּים) to *definite-noun* (הַדָּעַת), and the predicates move from *Piel iterative* (יְשֹׁטְטוּ) to *Qal intransitive stative-becoming* (תִרְבֶּה). The two verbs are linked semantically: roving/searching → knowledge-increasing. That is the natural epistemological chain: intensive search produces increased knowledge. The clause pair does not make this a causal claim grammatically (there is no "because" or "so that"), but the juxtaposition is semantically obvious: the searchers' work and the growth of knowledge are correlated events in the "time of end" region.

**The temporal location of clauses 4–5.** Both verbs are yiqtol (imperfect), which in BH narration locates actions in the *non-past-completed* domain — future, habitual, modal, or gnomic. Because clauses 4–5 follow the עַד־עֵת קֵץ of clause 3, the most natural reading is that יְשֹׁטְטוּ and תִרְבֶּה describe what happens *at or after* the terminus. The grammar admits three nuances (in descending order of likelihood given the asyndeton):

1. **Consequential-sequential** — "seal it until the time-of-end; [then, at that terminus] many shall rove and knowledge shall increase." The sealed condition is lifted at the terminus, and the revealed content feeds the increased knowledge.
2. **Circumstantial** — "seal it until the time-of-end, [while] many rove and knowledge increases." The searching-and-increasing is concurrent with the sealed-until interval (i.e., through the intermediate period, not only at its end).
3. **Causal/justificatory** — "seal it until the time-of-end, [because] many shall rove and knowledge shall increase." The sealing is undertaken in view of a future era of intensified search, against which moment the sealed content will be revealed.

The asyndeton leaves these open. The parallel in Amos 8:12 וְנָעוּ מִיָּם עַד־יָם … יְשׁוֹטְטוּ לְבַקֵּשׁ אֶת־דְּבַר־יְהוָה וְלֹא יִמְצָאוּ ("they shall stagger from sea to sea … they shall rove to seek the word of YHWH and shall not find [it]") uses the same Piel יְשׁוֹטְטוּ as Dan 12:4, paired there with the infinitive purpose לְבַקֵּשׁ ("to seek"). Amos portrays a famine-of-the-word era in which roving/searching yields no finding; Dan 12:4 portrays a roving/searching era in which knowledge *does* increase. The two passages use the same verb for the same searching activity but report opposite outcomes — which suggests that שׁוט + search is a fixed prophetic idiom for intensified investigation of prophetic content, with the outcome (fruitful or famine) being a separate matter.

---

## Intra-Danielic Placement

Dan 12:4 stands at the closing of the final extended oracle (chs. 10–12). The verse marks a *discourse-boundary*: after v. 4, the narrative resumes with Daniel seeing two more angelic figures (v. 5) and asking "how long?" (v. 6–7), to which v. 7 gives the "time, times, and a half" answer. Then v. 8 reports Daniel's incomprehension, v. 9 gives the angelic reply (the sealed-state report: סְתֻמִים וַחֲתֻמִים), vv. 10–12 provide the day-count markers (1290 / 1335), and v. 13 closes with the personal promise.

| Pericope | Content | Verbal spine |
|----------|---------|--------------|
| 10:1–11:1 | Daniel's vision by the Tigris; angelic appearance | Wayyiqtol narration |
| 11:2–35 | Persia-Greece-Seleucid oracle through "time of end" (11:35) | Predictive weqatal/x-yiqtol sequence |
| 11:36–45 | The self-exalting king through his "end" (קִצּוֹ) | Continued weqatal/x-yiqtol (see [dan-11-36-37](dan-11-36-37.md)) |
| 12:1–3 | Michael's rising; resurrection; the wise who shine | x-yiqtol + perf./impf. mix |
| **12:4** | **Sealing command + post-terminus prediction** | **WXIm + Voct + WIm0 + ZYqX + WYqX** |
| 12:5–7 | Angelic dialogue; "time, times, half" | Wayyiqtol + direct speech (see [dan-12-7-11-12](dan-12-7-11-12.md)) |
| 12:8–9 | Daniel's incomprehension; the sealed-state report | Wayyiqtol + verbless report (סְתֻמִים וַחֲתֻמִים …) |
| 12:10–12 | The wise shall understand; 1290 / 1335 day-counts | Hithpael/Hiphil impf. + numerical markers (see [dan-12-7-11-12](dan-12-7-11-12.md)) |
| 12:13 | Personal promise to Daniel | Qal impv. + wayyiqtol future |

Verse 4 therefore occupies a *hinge* position: it closes the oracle-proper (chs. 10–12:3) and opens the epilogue (12:5–13). Its grammar performs a double function — it seals the content (retrospectively closing the oracle) and forecasts the era of unsealing (prospectively opening what comes next). The vocative דָנִיֵּאל at the hinge-within-the-hinge (clause 2) emphasizes the personal commissioning character of the act.

**Inclusio with Dan 8:26.** Dan 8:26 and Dan 12:4 form an inclusio around the book's eschatological material:

- **Dan 8:26** — single sealing verb (סתם), single object (חָזוֹן), durational preposition (לְ + יָמִים רַבִּים). Closing command of the 2,300-evening-morning oracle.
- **Dan 12:4** — paired sealing verbs (סתם + חתם), paired objects (דְּבָרִים + סֵפֶר), terminating preposition (עַד + עֵת קֵץ). Closing command of the time-of-end oracle.

The progression from 8:26 to 12:4 tightens the sealing construction (single → double), specifies the objects (vision → words + book), and shifts the temporal semantics from duration to terminus. The two passages belong to the same theological project — deferred disclosure of eschatological content — but 12:4 is more *bounded* (both objects and termini specified) than 8:26 (still open-ended).

**Resolution in Dan 12:9.** The sealed-state report of Dan 12:9 explicitly confirms that the commands of 12:4 have been executed. The passive participles סְתֻמִים וַחֲתֻמִים are the resultative of the imperatives סְתֹם וַחֲתֹם. The 12:9 reply to Daniel's "what shall be the end?" (12:8) is not "I shall tell you" but "the words are sealed" — i.e., the same fact already commanded in 12:4 is invoked as the reason further explanation is not forthcoming to Daniel personally. The 12:9 grammar shifts the temporal clause from עַד־עֵת קֵץ (12:4, future-bounded) to עַד־עֵת קֵץ (12:9, same phrase) — confirming that 12:4's terminus is still future at 12:9's moment of speaking.

---

## Interpretive Options for "Sealed-Until-Time-of-End"

**The grammar permits — and in some cases differentially favors — multiple hermeneutical schemes.** The following positions are represented in historical commentary. This entry catalogs them without adjudicating, but notes where the grammar tilts one way or another.

### A. Hidden-until-future-point (concealment reading)

**Core claim.** The sealed content is *inaccessible to understanding* until a specific future moment (עֵת קֵץ), at which it becomes intelligible.

**Grammatical fit.**
- The dual command (סתם + חתם) maps well to *concealment-for-preservation*: the words are closed up (semantic inaccessibility) *and* the book is sealed (physical tamper-evidence). The concealment function of סתם is the primary grammatical lexeme here.
- The preposition עַד marks a terminus — after which the concealment ceases.
- The post-terminus clauses 4–5 (יְשֹׁטְטוּ רַבִּים / תִרְבֶּה הַדָּעַת) describe the era *after* unsealing, when search activity intensifies and knowledge grows — fitting a reading where the unsealed content is precisely what feeds the increased knowledge.
- Dan 12:8–10 corroborates: Daniel personally does not understand (v. 8 וְלֹא אָבִין), and the "wise" (v. 10 וְהַמַּשְׂכִּלִים יָבִינוּ) will understand *at that future time* but not before.

**Grammatical strain.**
- "Hidden" is too strong for חתם alone, which primarily denotes *authentication* rather than *concealment*. The reading must rest on the סתם-dimension rather than the חתם-dimension. This makes the dual-verb construction somewhat redundant if *both* verbs are read as concealment.
- The Qumran / Second Temple reception already found much of Daniel intelligible (4QDan fragments, 1 Macc allusions); a fully-hidden reading has to explain why pre-end Jewish communities interpreted Daniel at all.

### B. Authenticated-awaiting-fulfillment (custodial reading)

**Core claim.** The sealed content is *preserved in authenticated form* so that when the events occur, the record can be verified against the prior prediction. The sealing is not concealment but *guarantee of authorship and integrity*.

**Grammatical fit.**
- חתם is the primary grammatical lexeme here — it is *the* verb for affixing a seal to authenticate a document. The ANE legal-documentary background (Jer 32:9–14) fits: a witnessed and sealed document is preserved for future verification.
- The object הַסֵּפֶר (the book/document) aligns with this: sealing the *book* is a documentary act, not a content-hiding act.
- The post-terminus clauses fit: knowledge will increase *as the prediction is verified against history* — the searchers rove through the records, and the fit between prediction and fulfillment feeds growing confidence.
- This reading is consistent with Isa 8:16 חֲתוֹם תּוֹרָה ("seal the teaching") where the sealing preserves the teaching-testimony for later vindication (Isa 8:17 "I will wait for YHWH").

**Grammatical strain.**
- סתם (the *concealment* verb) is harder to accommodate on a purely custodial reading. If the content is merely "preserved but readable," why say the words are "stopped up"? A purely-custodial reading tends to downplay the סתם-dimension.
- Dan 12:9's explicit statement that "the words are sealed" *as the reason Daniel is not told more* is easier on a concealment reading than a custodial one (custody would not preclude further explanation).

### C. Both-and (progressive unsealing)

**Core claim.** The sealed content is *concurrently* (i) concealed in its fuller eschatological meaning (סתם) and (ii) authenticated as a fixed document (חתם). The sealed-state is progressively lifted as the end approaches, with partial understanding available to Daniel's initial audience, fuller understanding available to each successive generation as fulfillment unfolds, and complete understanding arriving at עֵת קֵץ.

**Grammatical fit.**
- Honors both verbs: סתם accounts for the partial concealment, חתם accounts for the documentary preservation-and-authentication. The dual construction is non-redundant because each verb does a distinct work.
- Accounts for the dual objects: הַדְּבָרִים (the words — the semantic content, partially concealed) are closed-up, while הַסֵּפֶר (the book — the physical document) is sealed. Two operations on two objects.
- Accounts for the post-terminus predictions: יְשֹׁטְטוּ רַבִּים (iterative Piel — ongoing, intensifying investigation) and תִרְבֶּה הַדָּעַת (Qal stative-becoming — gradual increase) both imply *progressive* rather than *instantaneous* processes. Both yiqtol forms are imperfective aspect — unbounded, ongoing action.
- Fits the Dan 12:10 distinction between those-who-understand (הַמַּשְׂכִּלִים) and the wicked (הָרְשָׁעִים): understanding is available but selective — not universally-concealed and not universally-manifest.

**Grammatical consideration.**
- The aspectual force of יְשֹׁטְטוּ (Piel iterative imperfect) and תִרְבֶּה (Qal imperfective imperfect) favors *progressive/ongoing* over *instantaneous* reading. If the sealing were merely a switch — fully hidden then fully revealed — the verbs would be more likely perfective or telic. The imperfective unfolding of both clauses 4 and 5 supports a progressive unsealing reading.
- The combination of עַד ("until") + imperfective clauses gives an interpretive structure in which the terminus עֵת קֵץ is *the moment when* increased search and knowledge reach their climax, not merely the moment when hidden content is flipped to revealed.

### What the grammar constrains — summary

**What the grammar decides.**
- The sealing involves *both* concealment and authentication — the dual-verb construction is non-redundant.
- The sealing has *two objects* — the words (semantic content) and the book (physical document).
- The sealed condition *has a terminus* — the construction עַד־עֵת קֵץ is not indefinite.
- The post-terminus era is characterized by *intensified search activity* (Piel יְשֹׁטְטוּ) and *growing knowledge* (Qal תִרְבֶּה הַדָּעַת) — both verbs are imperfective (ongoing/progressive), not perfective (instantaneous).
- The commands are addressed to *Daniel personally* (2ms + topic-pronoun + vocative), making him the custodian-figure.

**What the grammar does not decide.**
- *Which* "end" is meant — the grammar alone does not specify Maccabean / Roman / papal / future-eschaton referents.
- *What content* is sealed — whether the whole book, the time-of-end oracle only, or specific time-markers (1290/1335, time-times-half).
- *Who* the רַבִּים are — the adjective is generic-indefinite.
- *Which* knowledge increases — the article is anaphoric-or-generic, not specifying content.
- *How* the unsealing happens — instantaneously at the terminus, or progressively approaching it, or retrospectively after events unfold.

The grammar supports reading (a) *concealment*, (b) *authentication-preservation*, or (c) *both-and progressive unsealing*. Among these, reading (c) coheres most smoothly with the dual-verb + dual-object construction and the imperfective aspect of the post-terminus predictions. Readings (a) and (b) each foreground one of the two verbs; (c) honors both.

---

## Cross-References

### Grammar library
- [imperative-mood](../hebrew/imperative-mood.md) — general functions of BH Qal imperatives (command, permission, request, commissioning)
- [qal-imperfect](../hebrew/qal-imperfect.md) — yiqtol forms in clauses 4 and 5 (predictive/imperfective future)
- [syntax-waw-conjunction](../hebrew/syntax-waw-conjunction.md) — topic-shifting waw (וְאַתָּה) and coordinative waw (וַחֲתֹם, וְתִרְבֶּה)
- [stem-niphal](../hebrew/stem-niphal.md) — reference for the passive-stem family into which the 12:9 participles fall
- [hiphil-imperfect](../hebrew/hiphil-imperfect.md) — reference category for intensified-verbal-action (Piel of שׁוט shares intensification semantics with Hiphil)

### Passage library
- [dan-8-26](dan-8-26.md) — the *first* sealing command in Daniel (single verb, vision-object, durational preposition לְ + יָמִים רַבִּים); forms an inclusio with 12:4
- [dan-9-24-27](dan-9-24-27.md) — the Seventy-Weeks oracle with its own infinitival לַחְתֹּם חָזוֹן וְנָבִיא (sealing vision and prophet) in a different grammatical register
- [dan-12-7-11-12](dan-12-7-11-12.md) — the surrounding time-markers (time-times-half; 1290; 1335) of the epilogue that 12:4 opens
- [dan-11-36-37](dan-11-36-37.md) — the immediately-preceding oracle's grammar (self-exalting king through "his end")
- [dan-8-14](dan-8-14.md) — the 2,300-evening-morning oracle that 8:26 sealed; part of the same sealing-theology arc

### Word studies (shared library)
- [H5640-catham](../../word-studies/H5640-catham.md) — "stop up, shut up, keep secret" (concealment verb; v. 4 clause 1)
- [H2856-chatham](../../word-studies/H2856-chatham.md) — "seal (a document)" (authentication verb; v. 4 clause 3)
- [H2377-chazon](../../word-studies/H2377-chazon.md) — "vision" (the object of sealing in 8:26 and 9:24, parallel to דְּבָרִים in 12:4)
- [TR-dabar-laleo](../../word-studies/TR-dabar-laleo.md) — LXX/NT mapping of דָּבָר (the word-object in v. 4 clause 1)
- [TR-chazon-horasis](../../word-studies/TR-chazon-horasis.md) — LXX/NT mapping of חָזוֹן (parallel semantic field for oracular content)

### Gaps (no entry yet — candidates for future study)
- H5612 סֵפֶר — "book, scroll, document" (v. 4 clause 3; the physical manuscript sealed)
- H1697 דָּבָר — "word, matter, thing said" (v. 4 clause 1; the semantic content sealed)
- H6256 עֵת — "time, appointed moment" (v. 4 clause 3; the construct of עֵת־קֵץ)
- H7093 קֵץ — "end, terminus, limit" (v. 4 clause 3; the absolute of עֵת־קֵץ; Daniel's technical eschatological noun)
- H7751 שׁוט — "rove, go to and fro, search" (v. 4 clause 4; the Piel intensive of investigation)
- H1847 דַּעַת — "knowledge" (v. 4 clause 5; the subject that increases)
- H7235 רבה — "be/become many, increase" (v. 4 clause 5; Qal stative-becoming)
- passage entry for Dan 12:9 (companion state-report of the sealing; the passive-participle duplex)
- passage entry for Rev 22:10 (NT reversal: μὴ σφραγίσῃς "do not seal")
- passage entry for Rev 10:4 (NT parallel sealing: σφράγισον "seal them")

---

*Generated from: `hebrew_parser.py --verse/--clause/--construct "Dan 12:4"` (ETCBC/BHSA 2021); KJV text from `D:/bible/tools/data/kjv.txt`; LXX-Old-Greek and Theodotion glosses for יְשֹׁטְטוּ from standard LXX editions; standard BH reference grammars (Joüon-Muraoka, GKC, Waltke-O'Connor).*
*Last updated: 2026-04-19*
