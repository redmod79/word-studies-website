# Grammar Analysis: Daniel 11:36-37

## Text

**Hebrew (MT, v.36):** וְעָשָׂ֨ה כִרְצוֹנ֜וֹ הַמֶּ֗לֶךְ וְיִתְרוֹמֵ֤ם וְיִתְגַּדֵּל֙ עַל־כָּל־אֵ֔ל וְעַל֙ אֵ֣ל אֵלִ֔ים יְדַבֵּ֖ר נִפְלָא֑וֹת וְהִצְלִ֨יחַ֙ עַד־כָּ֣לָה זַ֔עַם כִּ֥י נֶחֱרָצָ֖ה נֶעֱשָֽׂתָה׃

**Hebrew (MT, v.37):** וְעַל־אֱלֹהֵ֤י אֲבֹתָיו֙ לֹ֣א יָבִ֔ין וְעַל־חֶמְדַּ֥ת נָשִׁ֛ים וְעַֽל־כָּל־אֱל֖וֹהַּ לֹ֣א יָבִ֑ין כִּ֥י עַל־כֹּ֖ל יִתְגַּדָּֽל׃

**KJV (v.36):** And the king shall do according to his will; and he shall exalt himself, and magnify himself above every god, and shall speak marvellous things against the God of gods, and shall prosper till the indignation be accomplished: for that that is determined shall be done.

**KJV (v.37):** Neither shall he regard the God of his fathers, nor the desire of women, nor regard any god: for he shall magnify himself above all.

---

## Word-by-Word Parsing (from `hebrew_parser.py`)

### Daniel 11:36

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | וְ | ו | Conj | and |
| 2 | עָשָׂה | עשׂה | Verb.Qal.Perf.3ms | do/make |
| 3 | כִ | כ | Prep | as / according to |
| 4 | רְצוֹנוֹ | רצון | Noun.ms.Abs + 3ms sfx | his will/pleasure |
| 5 | הַמֶּלֶךְ | מלך | Art + Noun.ms.Abs | the king |
| 6 | וְ | ו | Conj | and |
| 7 | יִתְרוֹמֵם | רום | **Verb.Hithpolel.Impf.3ms** | exalt himself |
| 8 | וְ | ו | Conj | and |
| 9 | יִתְגַּדֵּל | גדל | **Verb.Hithpael.Impf.3ms** | magnify himself |
| 10 | עַל | על | Prep | upon / against / above |
| 11 | כָּל | כל | Noun.ms.Cst | every |
| 12 | אֵל | אל | Noun.ms.Abs | god |
| 13 | וְ | ו | Conj | and |
| 14 | עַל | על | Prep | against |
| 15 | אֵל | אל | Noun.ms.Cst | God of |
| 16 | אֵלִים | אל | Noun.mp.Abs | gods |
| 17 | יְדַבֵּר | דבר | Verb.Piel.Impf.3ms | shall speak |
| 18 | נִפְלָאוֹת | פלא | Verb.Niphal.Ptcp.fp.Abs | marvellous things |
| 19 | וְ | ו | Conj | and |
| 20 | הִצְלִיחַ | צלח | **Verb.Hiphil.Perf.3ms** | he shall prosper |
| 21 | עַד | עד | Prep | until |
| 22 | כָּלָה | כלה | Verb.Qal.Perf.3ms | is completed |
| 23 | זַעַם | זעם | Noun.ms.Abs | indignation / wrath |
| 24 | כִּי | כי | Conj | for / because |
| 25 | נֶחֱרָצָה | חרץ | Verb.Niphal.Ptcp.fs.Abs | determined / decreed |
| 26 | נֶעֱשָׂתָה | עשׂה | Verb.Niphal.Perf.3fs | is done |

> **Parser note:** BHSA tags יִתְרוֹמֵם under *rwm* as "Hithpael"; the actual binyan of רום for a hollow root producing the doubled-middle reflexive is the **Hithpolel** (יִתְרוֹמֵם, not \*יִתְרַוֵּם). Hollow roots cannot form a standard Hithpael (no doubled middle radical), so they use the Polel/Hithpolel paradigm with reduplication of the third radical. Treat this form as Hithpolel for morphological purposes.

### Daniel 11:37

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | וְ | ו | Conj | and |
| 2 | עַל | על | Prep | concerning |
| 3 | אֱלֹהֵי | אלהים | Noun.mp.Cst | God(s) of |
| 4 | אֲבֹתָיו | אב | Noun.mp.Abs + 3ms sfx | his fathers |
| 5 | לֹא | לא | Neg | not |
| 6 | יָבִין | בין | Verb.Qal.Impf.3ms | he shall understand/regard |
| 7 | וְ | ו | Conj | and |
| 8 | עַל | על | Prep | upon |
| 9 | חֶמְדַּת | חמדה | Noun.fs.Cst | desire of |
| 10 | נָשִׁים | אשׁה | Noun.fp.Abs | women |
| 11 | וְ | ו | Conj | and |
| 12 | עַל | על | Prep | upon |
| 13 | כָּל | כל | Noun.ms.Cst | any |
| 14 | אֱלוֹהַּ | אלוה | Noun.ms.Abs | god |
| 15 | לֹא | לא | Neg | not |
| 16 | יָבִין | בין | Verb.Qal.Impf.3ms | he shall regard |
| 17 | כִּי | כי | Conj | for |
| 18 | עַל | על | Prep | above |
| 19 | כֹּל | כל | Noun.ms.Abs | all |
| 20 | יִתְגַּדָּל | גדל | **Verb.Hithpael.Impf.3ms** | he shall magnify himself |

---

## Clause Structure (from `hebrew_parser.py --clause`)

### v.36 — 7 clauses, domain Q (quotation/prophetic discourse)

| # | Type | Text | Syntactic roles |
|---|------|------|-----------------|
| 1 | **WQtX** | וְעָשָׂה כִרְצוֹנוֹ הַמֶּלֶךְ | Conj+Pred+Adju+Subj — *weqatal* opens prophetic sequence |
| 2 | **WYq0** | וְיִתְרוֹמֵם | Conj+Pred — weyiqtol continuation |
| 3 | **WYq0** | וְיִתְגַּדֵּל עַל־כָּל־אֵל | Conj+Pred+Cmpl |
| 4 | **WxY0** | וְעַל־אֵל אֵלִים יְדַבֵּר נִפְלָאוֹת | Conj+Cmpl+Pred+Objc — fronted complement for emphasis |
| 5 | **WQt0** | וְהִצְלִיחַ | Conj+Pred — *weqatal* resumes prophetic-perfect chain |
| 6 | **xQtX** | עַד כָּלָה זַעַם | Conj(עַד)+Pred+Subj — temporal-terminal subordinate clause |
| 7 | **XQtl** | כִּי נֶחֱרָצָה נֶעֱשָׂתָה | Conj+Subj+Pred — causal participle-subject + Niphal finite predicate |

### v.37 — 4 clauses

| # | Type | Text | Syntactic roles |
|---|------|------|-----------------|
| 1 | **WxY0** | וְעַל אֱלֹהֵי אֲבֹתָיו לֹא יָבִין | Conj+Cmpl+Neg+Pred — complement fronted before negated yiqtol |
| 2 | **NmCl** | וְעַל חֶמְדַּת נָשִׁים | Verbless / gapped — continuation under ellipsis of לֹא יָבִין |
| 3 | **WxY0** | וְעַל כָּל־אֱלוֹהַּ לֹא יָבִין | Conj+Cmpl+Neg+Pred — repeated frame closes inclusio |
| 4 | **xYq0** | כִּי עַל־כֹּל יִתְגַּדָּל | Conj+Cmpl+Pred — causal clause giving the *reason* for the triple refusal |

**Macro-shape:** v.36 opens with *weqatal* (וְעָשָׂה), chains two *weyiqtol* (וְיִתְרוֹמֵם / וְיִתְגַּדֵּל), fronts a complement for prominence (וְעַל־אֵל אֵלִים יְדַבֵּר), resumes with *weqatal* (וְהִצְלִיחַ), and closes with a Niphal-participle causal clause. v.37 builds a triple עַל-fronted complement pattern capped by a causal כִּי עַל־כֹּל יִתְגַּדָּל — structurally echoing v.36's vertical-elevation motif (עַל …עַל …עַל …עַל־כֹּל).

---

## Key Grammatical Features

### 1. וְעָשָׂה כִרְצוֹנוֹ הַמֶּלֶךְ — Qal *weqatal* opening a prophetic sequence

- **Form:** וְ + עָשָׂה (Qal Perfect 3ms) with prefixed וְ = *weqatal* / waw-consecutive perfect.
- **Syntax:** Clause type WQtX (weqatal + X), domain Q (prophetic discourse). Subject הַמֶּלֶךְ postposed after predicate + adjunct כִרְצוֹנוֹ ("according to his will/pleasure").
- **Function:** In prophetic-future discourse, *weqatal* carries future-sequential force ("he will act / he shall do"). The chain וְעָשָׂה … וְיִתְרוֹמֵם … וְיִתְגַּדֵּל … וְהִצְלִיחַ is a mixed *weqatal / weyiqtol* future sequence — a standard Classical Biblical Hebrew prophetic device.
- **Semantics of כִרְצוֹנוֹ:** The phrase "according to his will" reprises earlier uses in the same oracle — Dan 8:4 וְעָשָׂה כִרְצֹנוֹ (the ram), Dan 11:3 וְעָשָׂה כִרְצוֹנוֹ (the mighty king = Alexander), Dan 11:16 וְיַעַשׂ הַבָּא אֵלָיו כִּרְצוֹנוֹ. The idiom marks **unchecked autonomous sovereignty** — doing what one pleases with no external restraint. Its fourth appearance here, at the climax of the prophecy, reactivates the earlier pattern.

### 2. וְיִתְרוֹמֵם וְיִתְגַּדֵּל — Hithpolel + Hithpael (reflexive-intensive)

- **Forms:**
  - יִתְרוֹמֵם — root רום (hollow root), **Hithpolel** Imperfect 3ms. Because רום cannot form a standard Hithpael (it has no doubled middle radical), the Polel/Hithpolel substitutes: third radical reduplicates, giving the pattern yiṯ-rô-mēm.
  - יִתְגַּדֵּל — root גדל, **Hithpael** Imperfect 3ms. Normal strong-root Hithpael with assimilated ת in the prefix.
- **Voice:** Both are **reflexive** (subject acts on himself) and/or **ingressive-reflexive** ("cause oneself to be exalted / magnified"). Classic middle-reflexive function of the Ht-stem: the king's aggrandizement is self-initiated, not divinely granted.
- **Rhetorical pairing:** The doublet רום + גדל is formulaic for arrogant self-elevation (cf. Isa 10:15; Ezek 38:23). The collocation יִתְרוֹמֵם עַל / יִתְגַּדֵּל עַל ("exalt himself / magnify himself **over**") takes עַל as a **complement of elevation-against**, not mere physical "upon."
- **Link:** See reflexive/middle function discussion parallel to Niphal tolerative/reflexive — [stem-niphal](../hebrew/stem-niphal.md). *(No dedicated Hithpael reference entry exists yet — gap flagged.)*

### 3. וְעַל־אֵל אֵלִים יְדַבֵּר נִפְלָאוֹת — fronted complement + Piel of דבר + Niphal participial substantive

- **Clause type:** WxY0 — waw + non-verb X (עַל־אֵל אֵלִים) + yiqtol. Fronting the prepositional complement before the verb pulls the target of speech into focus: *"and **against the God of gods** he shall speak marvelous-things."*
- **אֵל אֵלִים — "God of gods":** Superlative genitive construct chain; intensifies אֵל alone in v.36a. The sequence *"every god"* (v.36a) → *"God of gods"* (v.36b) escalates rather than duplicates: the blasphemy targets not just pagan deities but the supreme God.
- **יְדַבֵּר נִפְלָאוֹת:** Piel imperfect of דבר + Niphal participle *fp abs* of פלא functioning as substantival direct object ("marvelous-things / astonishing things / monstrous utterances"). The Niphal participle נִפְלָאוֹת is normally **positive** in the Psalms ("the wonders of YHWH," Ps 9:2; 26:7) — here it is **darkly ironic**: wonders *against* the true God. Same form-word used positively of YHWH's deeds is here predicated of the blasphemer's speech.
- **Semantic register:** The root דבר + נִפְלָאוֹת functions as a technical idiom for blasphemous boast — Dan 7:8, 11, 20, 25 parallels: *memalel rabrebān* ("speaking great things") in Aramaic. Dan 11:36 is the Hebrew counterpart; Dan 7:25 Aramaic *ûmillîn lĕṣad ʿillāyāʾ yĕmallēl* ("he shall speak words against the Most High") is the closest lexical sibling.

### 4. וְהִצְלִיחַ עַד־כָּלָה זַעַם — Hiphil *weqatal* bounded by a temporal terminus

- **Form:** הִצְלִיחַ — Hiphil Perfect 3ms of צלח ("succeed, prosper, be able-to-succeed"). With prefixed וְ = *weqatal* resuming the prophetic-future chain.
- **Terminus clause:** עַד־כָּלָה זַעַם = preposition עַד ("until") + Qal Perfect 3ms of כלה ("be complete, come to an end") + Subj זַעַם ("indignation, wrath"). Clause type xQtX — עַד + predicate + subject — a standard *"until X is completed"* construction.
- **Crucial datum — "a set term":** The prospering is **explicitly time-bounded**. The verb is Hiphil (causative — "he shall cause success"), not indefinite; the עַד-clause sets a hard terminus. The grammar imposes a **fixed, non-negotiable limit** on the king's success.
- **נֶחֱרָצָה נֶעֱשָׂתָה:** Niphal Participle fs + Niphal Perfect 3fs — "**what is determined/decreed** is/shall-be done." *Divine passive* — YHWH as unexpressed agent. The Niphal of חרץ ("cut, decide, determine") denotes irrevocable divine decree (cf. Isa 10:23, 28:22, Dan 9:27 where *neḥĕrāṣâ* closes the 70-weeks prophecy — the same lexeme explicitly marks divine pre-limitation in both Daniel passages). The grammatical force: the indignation has a **pre-set duration that YHWH has already fixed**. Cf. the conceptually parallel accusatives-of-duration in Dan 7:25 / 12:7 and their Greek reflexes (Rev 13:5; Dan 11:35 עַד־עֵת קֵץ).
- **Link:** Divine-passive semantics parallel [divine-passive](../greek/divine-passive.md) entry on reverential agent-obscuring.

### 5. v.37 — Triple negation בֹא יָבִין + climactic יִתְגַּדָּל

- **Form:** יָבִין — Qal Imperfect 3ms of בין ("discern, regard, consider"). With לֹא = "he shall not regard." Repeated twice; the middle clause is verbless (NmCl) continuing under ellipsis.
- **Triple עַל-fronting:** עַל־אֱלֹהֵי אֲבֹתָיו / עַל־חֶמְדַּת נָשִׁים / עַל־כָּל־אֱלוֹהַּ — three fronted complements repeat the v.36 עַל-motif from "above" (arrogance) to "regarding" (contempt). The three objects of non-regard are **(a)** ancestral deity, **(b)** desire-of-women, **(c)** any god whatsoever.
- **חֶמְדַּת נָשִׁים:** Construct chain, noun.fs.cst of חמדה + noun.fp.abs of אשׁה. The construct is grammatically **ambiguous**:
  - *Objective genitive:* "the-thing-women-desire" → what women long for (a person, deity, or object women revere).
  - *Subjective genitive:* "desire-exercised-by-women" → women's affection/love (i.e., he has no natural love for women).
  - *Appositive/epexegetical:* "the-desirable-one-[who-is]-women" → women as such, as objects of desire.
  - The form itself does not decide among these; only context does.
- **Causal כִּי עַל־כֹּל יִתְגַּדָּל:** The final clause explains all three refusals: *"because above all he shall magnify himself."* Hithpael imperfect of גדל returns — inclusio with v.36 יִתְגַּדֵּל עַל־כָּל־אֵל. The king's self-magnification is presented as the **cause** of his religious indifference — not atheism per se, but self-deification crowding out prior loyalties. עַל־כֹּל ("above all/everything") is absolute: no exception, no reservation.

---

## LXX-Theodotion ↔ 2 Thessalonians 2:4 — Verbal Parallel

### Dan 11:36 Theodotion

> καὶ ποιήσει κατὰ τὸ θέλημα αὐτοῦ ὁ βασιλεὺς καὶ **ὑψωθήσεται καὶ μεγαλυνθήσεται ἐπὶ πάντα θεὸν** καὶ λαλήσει ὑπέρογκα…

### 2 Thessalonians 2:4 (parsed above)

> ὁ ἀντικείμενος καὶ **ὑπεραιρόμενος ἐπὶ πάντα λεγόμενον θεὸν ἢ σέβασμα** …

### Lexical correspondence table

| Element | Dan 11:36 MT | Dan 11:36 Theod. | 2 Thess 2:4 |
|---------|-------------|------------------|-------------|
| "exalt himself" | יִתְרוֹמֵם (Hithpolel) | ὑψωθήσεται (Fut Pass Ind of ὑψόω) | ὑπεραιρόμενος (Pres M/P Ptcp of ὑπεραίρω) |
| "magnify himself" | יִתְגַּדֵּל (Hithpael) | μεγαλυνθήσεται (Fut Pass Ind of μεγαλύνω) | — |
| "above every god" | עַל־כָּל־אֵל | **ἐπὶ πάντα θεόν** | **ἐπὶ πάντα λεγόμενον θεόν** |
| "speak marvelous/outrageous things" | יְדַבֵּר נִפְלָאוֹת | λαλήσει ὑπέρογκα | — |
| "or object of worship" | — | — | ἢ σέβασμα (extension) |

### Grammatical observations on the parallel

1. **Preposition + accusative match:** Theodotion's ἐπὶ πάντα θεόν exactly matches Paul's ἐπὶ πάντα … θεόν. ἐπί + accusative here renders Hebrew עַל ("above / against"), not spatial "upon." Paul retains both the preposition and the case.
2. **Substantival πᾶς + θεός:** Both texts use the universal quantifier πᾶς in the accusative singular with θεόν — a verbatim lexical triplet (ἐπὶ / πάντα / θεόν).
3. **Paul's additions:**
   - **λεγόμενον** — Present Passive Participle of λέγω, "so-called, called-[a-god]," broadens the scope from *actual* gods to anything *designated* as god.
   - **ἢ σέβασμα** — "or object-of-worship," extends the target still further. σέβασμα (Acts 17:23 Paul uses the same word of Athenian devotional objects) broadens beyond θεός to any *cultic veneration*.
4. **Reflexive semantics preserved:** Hebrew Hithpolel/Hithpael (self-exaltation, self-magnification) → Theodotion future passive with reflexive/middle force ὑψωθήσεται / μεγαλυνθήσεται → Paul converts to Present Middle/Passive Participle ὑπεραιρόμενος (ὑπεραίρω, "lift-oneself-above-measure"). The Greek voice chain preserves the Hebrew reflexive force throughout.
5. **Verbal compounding:** Paul intensifies with ὑπερ- prefix (ὑπεραίρω) — a Pauline compound-verb technique; the preposition ὑπερ- "above" is built into the verb, while the separate ἐπί preposition still carries the *comparative-over* sense. The effect is emphatic redundancy: "lifting-himself-**over**-**above** every so-called god."
6. **Direction of dependency:** ὑπεραίρω occurs only twice in the NT (2 Cor 12:7 ×2 of Paul's own danger of self-exaltation; 2 Thess 2:4 of the eschatological figure). The specific phrase ἐπὶ πάντα … θεόν is not a generic LXX formula; it is distinctive to Dan 11:36 Theodotion. Its reappearance in Paul is therefore the **strongest lexical evidence** that 2 Thess 2:4 is reading Dan 11:36 directly (via Theodotion or proto-Theodotionic readings, rather than Old Greek which renders the same clause differently). Word studies at [TR-gadal-megaluno](../../word-studies/TR-gadal-megaluno.md) and [TR-gadal-megalyno](../../word-studies/TR-gadal-megalyno.md) document the Hebrew-Greek pairing.

---

## v.37 — Does the Grammar Narrow the Identification?

The question: does the cluster of (a) אֱלֹהֵי אֲבֹתָיו "God of his fathers" (b) חֶמְדַּת נָשִׁים "desire of women" (c) לֹא יָבִין + לֹא יָבִין (d) עַל־כֹּל יִתְגַּדָּל — grammatically constrain *which* historical figure this describes?

### What the grammar alone yields

| Datum | Grammatical fact | Interpretive force |
|-------|------------------|---------------------|
| אֱלֹהֵי אֲבֹתָיו | Noun.mp.Cst + 3ms possessive suffix | Establishes that the king *has* ancestral religion(s); he is therefore an apostate or religiously-unrooted, not a foreigner to the YHWH-worshipping tradition *per se*. The plural אֱלֹהֵי is formally ambiguous (plural-of-majesty = "God," or true plural "gods"); both readings are grammatical. |
| חֶמְדַּת נָשִׁים | fs.Cst + fp.Abs construct chain | Grammatical ambiguity (objective vs. subjective genitive) **is irreducible** from morphology alone. |
| לֹא יָבִין ×2 | Qal Impf of בין + neg — "not regard / not discern" | Marks deliberate refusal or moral incapacity, not mere ignorance. Strong verb; active negation. |
| כִּי עַל־כֹּל יִתְגַּדָּל | causal כִּי + Hithpael Impf 3ms | The clause **subordinates** all religious refusal to self-magnification. This is the interpretive anchor: whatever else is true of this figure, his religious stance is a function of self-deification. |

### Conclusion on grammatical narrowing

The morphology and syntax **do not uniquely identify** any historical figure. They describe a *type*: an apostate sovereign whose religious indifference is grounded in self-deification and whose career is divinely time-bounded (v.36 עַד־כָּלָה זַעַם). Historical identification must come from **extra-textual correlation**, not from grammar alone. Every serious interpretive tradition has read the same Hebrew forms and reached different referents.

---

## Five Interpretive Positions on Dan 11:36-45

Each position below is documented by the Hebrew-grammatical data it emphasizes, **without endorsement**.

### Position 1 — Antiochus IV Epiphanes (Preterist)

- **Anchor texts:** Dan 11:21-35 is widely agreed to describe Antiochus (the "contemptible person," desecration of the sanctuary in 11:31, the abomination). Preterist reading extends this into 11:36-45.
- **Grammatical support claimed:**
  - *Continuity of referent:* the *weqatal* / *weyiqtol* chain from v.21 onward is **unbroken by any speaker-marker or vision-shift**. There is no clause like וְאַחֲרֵי זֶה ("and after this…") or הִנֵּה ("behold") signaling a new figure. Grammatically, הַמֶּלֶךְ in v.36 has its nearest antecedent in the Antiochus material.
  - *Self-exaltation lexicon:* יִתְרוֹמֵם / יִתְגַּדֵּל + ἐπὶ πάντα θεόν is consistent with Antiochus's epithet *Θεὸς Ἐπιφανής* ("God Manifest") on his coinage.
  - *חֶמְדַּת נָשִׁים:* read as "Tammuz" or "Adonis" (a deity "desired by women") — whose cult Antiochus is attested to have disregarded or suppressed. Or: read as general licentiousness.
  - *עַד־כָּלָה זַעַם:* Antiochus died in 164 BCE while campaigning in Persia (Polybius 31.9; 1 Macc 6:1-16; 2 Macc 9) — a bounded terminus.
- **Grammatical difficulties:**
  - Verses 40-45 describe a *final* campaign with geographic sweep (Egypt, Libya, Ethiopia, pitching tents between seas and the *holy mountain*) that does not match the historical Antiochus's last campaign eastward.
  - הַמֶּלֶךְ in v.40 is specified as clashing with "the king of the south," implying he is *not* himself the Seleucid king of the north — some read this as a *shift* of referent mid-chain.

### Position 2 — Roman Emperor (Historicist-Roman)

- **Anchor texts:** Some readers see a transition from Seleucid to Roman power somewhere between v.30 ("ships of Kittim") and v.36; הַמֶּלֶךְ in v.36 becomes a generic "the king (that shall come)."
- **Grammatical support claimed:**
  - *Absolute article:* הַמֶּלֶךְ with definite article but *without* qualifier ("the king of the north / south") marks a category-shift — a king simpliciter, distinct from the bipolar northern/southern frame dominating vv.5-35.
  - *ἐπὶ πάντα θεόν:* Roman emperors (Caligula, Domitian, etc.) demanded universal cult ("dominus et deus") above all gods — matches the superlative עַל־כָּל־אֵל / עַל־כֹּל.
  - *לֹא יָבִין עַל אֱלֹהֵי אֲבֹתָיו:* Roman state cult abandoned traditional religion in favor of emperor worship.
- **Grammatical difficulties:**
  - No explicit narrative marker (like the "ships of Kittim" in v.30) signals the shift at v.36. The linkage depends on reading הַמֶּלֶךְ as generic rather than continuative.

### Position 3 — Papal Power (Historicist-Protestant)

- **Anchor texts:** The Reformation-era historicist tradition reads Dan 7 (little horn), Dan 8 (little horn), Dan 11:36-45, 2 Thess 2:3-8, and Rev 13 as a coordinated description of the papacy.
- **Grammatical support claimed:**
  - *Paul's direct citation* of Dan 11:36 Theodotion in 2 Thess 2:4 identifies the referents as the same figure. 2 Thess 2:4 describes the *ἄνθρωπος τῆς ἀνομίας* "sitting in the temple of God, proclaiming himself to be God" — precisely the יִתְגַּדֵּל עַל־כָּל־אֵל / עַל־כֹּל יִתְגַּדָּל clause.
  - *לֹא יָבִין עַל אֱלֹהֵי אֲבֹתָיו:* reads "God of his fathers" as Christian apostolic faith departed from.
  - *חֶמְדַּת נָשִׁים:* enforced clerical celibacy (1 Tim 4:3 "forbidding to marry").
  - *Niphal-participle "marvelous-things" = blasphemy:* parallel to Dan 7:8, 20, 25 *memalel rabrebān* → Rev 13:5 *στόμα λαλοῦν μεγάλα καὶ βλασφημίας*.
  - *עַד־כָּלָה זַעַם:* bounded terminus parallels Dan 7:25 accusative-of-duration formula (time + times + half-time = 1260 day-years in year-day reading).
- **Grammatical difficulties:**
  - The year-day principle is *lexical-theological*, not morphological; it is not encoded in any particular Hebrew verb form. The grammar permits both literal-day and extended readings.
  - The identification of חֶמְדַּת נָשִׁים with clerical celibacy is an interpretive choice among three grammatically-available options.

### Position 4 — Future Antichrist (Futurist-Dispensational)

- **Anchor texts:** Dan 11:36-45 describes a single, individual end-time figure often identified with the "man of lawlessness" (2 Thess 2:3-8), "beast from the sea" (Rev 13), "little horn" (Dan 7). Paul's direct citation of Dan 11:36 in 2 Thess 2:4 is taken to place the fulfillment in the same eschatological context as the Parousia (2 Thess 2:1, 8).
- **Grammatical support claimed:**
  - *Single-individual subject:* all third-masculine-singular verbs through vv.36-45 (יִתְרוֹמֵם, יִתְגַּדֵּל, יְדַבֵּר, הִצְלִיחַ, יָבִין, יִתְגַּדָּל) refer to one person.
  - *עַד עֵת קֵץ / עַד־כָּלָה זַעַם:* terminal markers in vv.35, 40 ("time of the end") relocate the scene to the eschaton. If vv.35-40 are eschatological, הַמֶּלֶךְ in v.36 is future.
  - *2 Thess 2:4 parallel:* Paul's *eschatological* framing of ὑπεραιρόμενος ἐπὶ πάντα λεγόμενον θεόν (set alongside the Parousia in 2:8) is taken as inspired commentary locating Dan 11:36 at the *end*.
  - *לֹא יָבִין עַל אֱלֹהֵי אֲבֹתָיו:* read as total apostasy of the final figure.
- **Grammatical difficulties:**
  - The chain of verbs from v.21 through v.45 is *unbroken grammatically* — insisting on a referent shift at v.36 requires extra-grammatical justification. The futurist typically responds that עֵת קֵץ in v.35 is that justification.

### Position 5 — Recapitulating Composite (Typological / Apocalyptic-Composite)

- **Thesis:** The figure in Dan 11:36-45 is deliberately *composite*, layering features of multiple historical and eschatological figures (Antiochus, Rome, papacy, final Antichrist) — in line with the apocalyptic genre convention of "prolepsis" or "typological recursion" (see [apocalyptic-narrative-prolepsis](../greek/apocalyptic-narrative-prolepsis.md)).
- **Grammatical support claimed:**
  - *Unbroken weqatal/weyiqtol chain with shifting historical textures:* the grammar itself offers no hard break, which suits a composite reading — the same grammatical subject can be filled by multiple historical instantiations.
  - *עַד־כָּלָה זַעַם* + *נֶחֱרָצָה נֶעֱשָׂתָה:* the Niphal "determined/decreed" formula echoes Dan 9:27 (also of an eschatological consummation). The grammar ties each instantiation to the same divine terminus.
  - *ἐπὶ πάντα θεόν → ἐπὶ πάντα λεγόμενον θεόν ἢ σέβασμα:* Paul's expansion of the Daniel clause is itself a recapitulation — he reads Dan 11:36 as a principle instantiated in his own near-future expectation, not a single historical referent.
  - *Hithpolel + Hithpael formula:* the self-exaltation lexicon is not historically-indexed; it appears across Isaiah (14:13-14 of Babylon), Ezekiel (28 of Tyre), Daniel (both little-horns), and Paul (2 Thess 2:4). The grammar tolerates multiple filters.
- **Grammatical difficulties:**
  - A composite reading cannot be *forced* by grammar alone — it is a hermeneutical posture that the grammar permits but does not require.

---

## Summary of Exegetically-Decisive Grammatical Data

1. **Self-exaltation is reflexive, not divinely-granted.** Hithpolel (יִתְרוֹמֵם) + Hithpael (יִתְגַּדֵּל ×2) → the king's elevation is self-caused. Contrast divine passive נֶחֱרָצָה נֶעֱשָׂתָה where God is the unspoken agent.
2. **Speech is framed as blasphemy.** Piel of דבר + Niphal participle נִפְלָאוֹת + directional עַל ("against") + superlative אֵל אֵלִים = technical blasphemy-idiom.
3. **Success is time-bounded.** עַד־כָּלָה זַעַם + כִּי נֶחֱרָצָה נֶעֱשָׂתָה = divinely-fixed terminus. The grammar guarantees the king's career ends on schedule.
4. **Religious rejection is causally downstream of self-deification.** כִּי עַל־כֹּל יִתְגַּדָּל (v.37 final clause) subordinates all of v.37's negations to the Hithpael of גדל — the same verb used in v.36.
5. **The LXX-Theodotion → 2 Thess 2:4 lexical bridge is verbatim.** ἐπὶ πάντα θεόν survives intact into Paul; Paul extends with λεγόμενον and σέβασμα but preserves the Danielic phrase. This is the strongest intertextual link between Daniel 11:36 and the NT "man of lawlessness" material.
6. **The grammar does not decide the historical referent.** The same forms support Antiochus, Roman, papal, futurist, and composite readings; historical identification is an exegetical move layered on top of morphologically-stable data.

---

## Cross-References

### Grammar Library
- [stem-niphal](../hebrew/stem-niphal.md) — Niphal functions (relevant for נֶחֱרָצָה, נֶעֱשָׂתָה, נִפְלָאוֹת)
- [syntax-waw-conjunction](../hebrew/syntax-waw-conjunction.md) — waw forms in the weqatal/weyiqtol chain
- [aorist-infinitive-accusative-of-duration](../greek/aorist-infinitive-accusative-of-duration.md) — parallel bounded-span grammar (Rev 13:5 ‖ Dan 7:25)
- [divine-passive](../greek/divine-passive.md) — agent-obscuring grammar (νֶחֱרָצָה נֶעֱשָׂתָה)
- [apocalyptic-narrative-prolepsis](../greek/apocalyptic-narrative-prolepsis.md) — composite/recursive reading convention
- [textual-variant-2thess-2-3](../greek/textual-variant-2thess-2-3.md) — textual data on the 2 Thess 2 parallel passage
- **GAP:** No dedicated Hithpael/Hithpolel entry yet — candidate for future creation.

### Word Studies
- [H1431-gadal](../../word-studies/H1431-gadal.md) — root גדל (used twice in v.36, once in v.37)
- [H2195-zaam](../../word-studies/H2195-zaam.md) — זַעַם "indignation/wrath"
- [H2782-charats](../../word-studies/H2782-charats.md) — root חרץ "decree/determine"
- [TR-gadal-megaluno](../../word-studies/TR-gadal-megaluno.md) — Hebrew-Greek pairing גדל ↔ μεγαλύνω
- [TR-gadal-megalyno](../../word-studies/TR-gadal-megalyno.md) — further Hebrew-Greek pairing
- [TR-dabar-laleo](../../word-studies/TR-dabar-laleo.md) — דבר ↔ λαλέω pairing (v.36 יְדַבֵּר)

### Adjacent Passage Analyses
- [dan-7-25-26](dan-7-25-26.md) — Aramaic parallel: "speaking great things against the Most High" + time-bounded decree
- [rev-13-1-10](rev-13-1-10.md) — στόμα λαλοῦν μεγάλα καὶ βλασφημίας; ἐδόθη + acc-of-duration μῆνας 42
- [rev-11-12-time-markers](rev-11-12-time-markers.md) — prophetic time-bounding formulae

---

*Context-neutral analysis. Interpretive positions documented without endorsement.*
