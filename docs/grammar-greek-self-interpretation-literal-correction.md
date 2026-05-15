# Self-Interpretation / Literal-Correction Pattern (Greek NT Didactic Discourse)

## Definition

A recurring narrative-rhetorical pattern in the didactic New Testament (Gospels and Revelation) in which a speaker's utterance is **first heard literally** by its audience (or by the reader), the literal reading is **shown to contradict** the speaker's intent (either by an explicit objection, a miscomprehension, or a transparently false sense), and the **text itself supplies the correct non-literal referent**, either through:

1. **Narrator aside** — the evangelist/seer steps out of the scene and glosses the utterance for the reader.
2. **Speaker self-interpretation** — the same speaker re-explains the utterance to the dull audience.
3. **In-text identification formula** — a symbol is paired with its referent by a copula (X = Y).

The paradigm texts are **John 2:19–21** (temple = body), **John 3:3–5** (born ἄνωθεν = born of water and Spirit), **Matthew 16:6–12** (leaven = teaching), and **Revelation 1:20** (seven stars = angels; seven lampstands = churches).

The pattern is a **hermeneutical signal built into the text**: the inspired narrator is training the reader's ear away from a strict literal reading in contexts where literal reading would produce absurdity, contradiction, or miscomprehension.

## Form Recognition

Three structural slots, realised by distinct grammatical devices.

| Slot | Function | Typical Greek Markers |
|------|----------|----------------------|
| **(1) Figurative utterance** | Speaker issues a saying whose surface sense is a concrete referent (temple, birth, leaven, stars) | Imperative (Λύσατε, Ὁρᾶτε, προσέχετε), conditional (ἐὰν μή … γεννηθῇ), vision-report object (οὓς εἶδες) |
| **(2) Literal (mis)reading** | Audience objects, questions, or rationalises on literal terms — OR the literal reading produces visible absurdity | οὖν / δέ transitional; πῶς δύναται + infinitive (John 3:4; 4:11; 6:52); διαλογίζομαι ἐν ἑαυτοῖς "reason among themselves" (Matt 16:7) |
| **(3) Correction** | Text supplies the real referent | (a) narrator aside ἐκεῖνος δὲ ἔλεγεν περὶ + genitive (John 2:21); (b) speaker follow-up (John 3:5; Matt 16:11–12); (c) copular identification X εἰσίν / ἐστίν Y (Rev 1:20) |

### Diagnostic grammatical markers across all four paradigms

- **περί + genitive** for narrator's "he was speaking *about*" — John 2:21 περὶ τοῦ ναοῦ τοῦ σώματος αὐτοῦ; John 7:39 περὶ τοῦ Πνεύματος; John 12:33 περὶ ποίου θανάτου.
- **τότε συνῆκαν ὅτι …** recognition-formula — Matt 16:12; Matt 17:13; Luke 24:45-style "then they understood that …" clauses often introducing a **non-literal ἀλλά-contrast**.
- **Copular εἰσίν / ἐστίν** with third-person subject and third-person predicate, both in the same gender-number, giving a symbol→referent equation — Rev 1:20; Matt 13:38–39; Luke 8:11; Gal 4:24 ἅτινά ἐστιν ἀλληγορούμενα.
- **πῶς δύναται / πῶς + interrogative + potential objection** flagging the literal misreading — John 3:4, 3:9; 4:11; 6:52.
- **ἀλλά-disjunction** after a negated literal reading (οὐ … ἀλλά) — Matt 16:12 οὐκ εἶπεν προσέχειν ἀπὸ τῆς ζύμης τῶν ἄρτων, **ἀλλὰ ἀπὸ τῆς διδαχῆς**.

### Parser search handles
- `greek_parser.py --verse "JHN 2:21"` shows the prototypical περί + gen. narrator aside.
- `greek_parser.py --lemma συνίημι` (G4920) hits 26× NT; the formulaic τότε συνῆκαν ὅτι is concentrated in Matt.
- `greek_parser.py --lemma μυστήριον` (G3466) 27× NT; Rev 1:20, 17:7 use it to flag a key-unlock moment.

## The Four Paradigm Passages

### 1. John 2:19–21 — The Temple Saying

**v.19 — figurative utterance (speaker: Jesus)**

| Word | Lemma | Strong's | Parsing |
|------|-------|----------|---------|
| Λύσατε | λύω | G3089 | V-AAM-2P (Aor Act Impv 2P) |
| τὸν ναὸν τοῦτον | ναός | G3485 | N-ASM + D-ASM |
| ἐγερῶ | ἐγείρω | G1453 | V-FAI-1S (Fut Act Ind 1S) |

**v.20 — literal misreading (audience: οἱ Ἰουδαῖοι)**

| Word | Lemma | Strong's | Parsing | Function |
|------|-------|----------|---------|----------|
| Τεσσεράκοντα καὶ ἓξ ἔτεσιν | ἔτος | G2094 | N-DPN dat. of time | literal-reference cue — the Herodian stone building |
| οἰκοδομήθη | οἰκοδομέω | G3618 | V-API-3S | aorist passive anchoring the saying to the physical structure |
| ὁ ναὸς οὗτος | ναός | G3485 | N-NSM + D-NSM | same lexeme as v.19, read literally |

**v.21 — narrator correction (Evangelist's aside)**

| Word | Lemma | Strong's | Parsing | Function |
|------|-------|----------|---------|----------|
| ἐκεῖνος δέ | ἐκεῖνος | G1565 | D-NSM | emphatic contrast with the crowd of v.20 |
| ἔλεγεν | λέγω | G3004 | V-IAI-3S | **imperfect** — the habitual/background sense of the saying, retrospectively understood |
| περὶ τοῦ ναοῦ | ναός | G3485 | PREP + N-GSM | "concerning the temple" — the figurative referent |
| τοῦ σώματος αὐτοῦ | σῶμα | G4983 | **genitive of apposition** | "the temple, namely (=that is) his body" |

Grammatically, τοῦ ναοῦ τοῦ σώματος αὐτοῦ is a **genitive of apposition / epexegetical genitive** (Wallace 94–100): the second articular genitive specifies what the first one actually designates. See the library entry [genitive-of-quality-apposition](genitive-of-quality-apposition.md).

### 2. John 3:3–5 — Born ἄνωθεν

**v.3 — figurative utterance**

| Word | Lemma | Strong's | Parsing |
|------|-------|----------|---------|
| ἐὰν μή … γεννηθῇ | γεννάω | G1080 | V-APS-3S (Aor Pass Subj 3S) in 3rd-class cond. |
| ἄνωθεν | ἄνωθεν | G509 | ADV — **lexically ambiguous**: "from above" / "again" / "anew" (BDAG §§1–3) |

The ambiguity of ἄνωθεν is the hinge. Nicodemus takes it **temporally** ("again"); Jesus meant it **locatively/causally** ("from above, from God"). Greek discourse exploits this double sense.

**v.4 — literal misreading (speaker: Nicodemus)**

| Word | Lemma | Strong's | Parsing | Function |
|------|-------|----------|---------|----------|
| πῶς δύναται | δύναμαι | G1410 | ADV-I + V-PNI-3S | diagnostic objection-formula |
| ἄνθρωπος γεννηθῆναι | γεννάω | G1080 | N-NSM + V-APN | generic "a man be born" |
| γέρων ὤν | γέρων / εἰμί | G1088/G1510 | N-NSM + V-PAP-NSM | causal ptcp: "being old" |
| εἰς τὴν κοιλίαν τῆς μητρὸς αὐτοῦ δεύτερον εἰσελθεῖν | κοιλία / εἰσέρχομαι | G2836/G1525 | PREP + N-ASF + ADV + V-2AAN | literal-biological expansion |

Nicodemus's response mobilises all the concrete imagery of physical re-entry into a womb — transparently absurd, forcing the figurative reading.

**v.5 — speaker self-interpretation**

| Word | Lemma | Strong's | Parsing | Function |
|------|-------|----------|---------|----------|
| ἐὰν μή τις γεννηθῇ | γεννάω | G1080 | V-APS-3S | restates v.3's conditional with identical form |
| ἐξ ὕδατος καὶ Πνεύματος | ὕδωρ / πνεῦμα | G5204/G4151 | PREP + N-GSN + N-GSN | **replaces ἄνωθεν** with the twofold source genitive |

The substitution ἄνωθεν (v.3) → ἐξ ὕδατος καὶ Πνεύματος (v.5) is the self-correction: Jesus himself supplies the non-literal content that ἄνωθεν concealed. The preposition **ἐκ + genitive of source** makes explicit the "from above" sense that the adverb left ambiguous.

### 3. Matthew 16:6–12 — The Leaven Saying

**v.6 — figurative utterance**

| Word | Lemma | Strong's | Parsing |
|------|-------|----------|---------|
| Ὁρᾶτε καὶ προσέχετε | ὁράω / προσέχω | G3708/G4337 | V-PAM-2P (twin pres. impv.) |
| ἀπὸ τῆς ζύμης | ζύμη | G2219 | PREP + N-GSF |
| τῶν Φαρισαίων καὶ Σαδδουκαίων | | | gen. of source/origin |

**v.7 — literal misreading (disciples, internal monologue)**

| Word | Lemma | Strong's | Parsing | Function |
|------|-------|----------|---------|----------|
| διελογίζοντο ἐν ἑαυτοῖς | διαλογίζομαι | G1260 | V-INI-3P + F-2DPM | imperfect: sustained internal reasoning |
| λέγοντες ὅτι | λέγω | G3004 | V-PAP-NPM + CONJ | speech-introducing ptcp with recitative ὅτι |
| Ἄρτους οὐκ ἐλάβομεν | ἄρτος / λαμβάνω | G740/G2983 | N-APM + V-2AAI-1P | literal: "we forgot bread" |

The shift from ζύμη (leaven) to ἄρτοι (loaves) is the disciples' literalizing slide.

**vv.8–11 — speaker self-interpretation (rebuke-form)**

Jesus (v.8 γνοὺς … εἶπεν) first rebukes the literal reading (ὀλιγόπιστοι), reminds them of the feeding miracles as evidence that bread-supply is not the issue (vv.9–10), then in v.11 **repeats the figurative utterance verbatim** (προσέχετε ἀπὸ τῆς ζύμης τῶν Φαρισαίων καὶ Σαδδουκαίων) with the rhetorical πῶς οὐ νοεῖτε ὅτι οὐ περὶ ἄρτων εἶπον ὑμῖν. Note **περὶ ἄρτων** as explicit disclaimer — the same περί + gen. construction that in John 2:21 introduced the real referent is here used negatively to exclude the literal one.

**v.12 — narrator correction (recognition-formula)**

| Word | Lemma | Strong's | Parsing | Function |
|------|-------|----------|---------|----------|
| τότε συνῆκαν ὅτι | τότε / συνίημι | G5119/G4920 | ADV + V-AAI-3P + CONJ | Matthean recognition-formula |
| οὐκ εἶπεν προσέχειν ἀπὸ τῆς ζύμης τῶν ἄρτων | | | negated literal |
| ἀλλὰ ἀπὸ τῆς διδαχῆς | ἀλλά / διδαχή | G235/G1322 | CONJ + PREP + N-GSF | corrective: the true referent is **teaching** |

The οὐκ … ἀλλά contrast disjunction is the narrator's formal identification: leaven ≠ bread; leaven = teaching. Grammatically the structure is a **negated infinitival indirect discourse** (οὐκ εἶπεν προσέχειν ἀπὸ X) followed by an **elliptical ἀλλά-clause** supplying the corrected prepositional phrase.

### 4. Revelation 1:20 — Stars and Lampstands

**v.20 — figurative utterance + immediate self-interpretation in one verse**

The μυστήριον-formula front-loads the verse and signals that the decoding is about to occur.

| Segment | Greek | Parsing | Function |
|---------|-------|---------|----------|
| τὸ μυστήριον τῶν ἑπτὰ ἀστέρων οὓς εἶδες | N-NSN + gen. + rel. cl. | anaphoric head — "the mystery of the seven stars which you saw" |
| καὶ τὰς ἑπτὰ λυχνίας τὰς χρυσᾶς | acc. (pendant accusative) | second anaphoric head (casus pendens w/out verb), resumed by αἱ λυχνίαι below |
| **οἱ ἑπτὰ ἀστέρες ἄγγελοι τῶν ἑπτὰ ἐκκλησιῶν εἰσίν** | N-NPM + N-NPM + V-PAI-3P | copular identification — **symbol = referent** |
| **αἱ λυχνίαι αἱ ἑπτὰ ἑπτὰ ἐκκλησίαι εἰσίν** | N-NPF + N-NPF + V-PAI-3P | copular identification — **symbol = referent** |

Two parallel **X εἰσίν Y** equations where (a) the grammatical subject X is the vision-symbol (stars, lampstands) and (b) the predicate nominative Y is the referent (angels of the churches, churches). The plural present **εἰσίν** is the standard identification-copula; the symbol and its referent are parsed in identical case (nom.–nom.), number (pl.–pl.), and each half has matched definiteness.

This is the most **formally explicit** of the four patterns: the text literally writes out "X = Y" twice without any intervening misreading stage, because the seer is being *instructed*, not corrected. The two other patterns (narrator aside; speaker self-interpretation) compress into this single copular announcement when the audience is the seer/reader directly.

## Structural Inventory of the Pattern (All Four)

| Passage | Figurative utterance | Literal misreading slot | Corrective mechanism |
|---------|---------------------|------------------------|---------------------|
| John 2:19–21 | Λύσατε τὸν ναὸν τοῦτον | v.20 objection by οἱ Ἰουδαῖοι citing 46-year building | **narrator aside**: ἐκεῖνος δὲ ἔλεγεν περὶ τοῦ ναοῦ τοῦ σώματος αὐτοῦ |
| John 3:3–5 | ἐὰν μή τις γεννηθῇ ἄνωθεν | v.4 Nicodemus literalises into physical rebirth | **speaker self-interpretation**: ἐξ ὕδατος καὶ Πνεύματος (v.5) |
| Matt 16:6–12 | προσέχετε ἀπὸ τῆς ζύμης … | v.7 disciples reason about forgotten ἄρτοι | **speaker rebuke (vv.8–11) + narrator recognition-formula (v.12)**: ἡ ζύμη = ἡ διδαχή |
| Rev 1:20 | ἑπτὰ ἀστέρες + ἑπτὰ λυχνίαι in the vision | (slot collapsed — reader is direct addressee) | **copular identification formula**: X εἰσίν Y twice |

## Related NT Specimens (Same Pattern, Lesser or Partial Realisations)

Tool-verified from greek_parser.py:

| Reference | Figurative utterance | Literal miscomprehension | Correction |
|-----------|---------------------|--------------------------|-----------|
| John 4:10–14 | ὕδωρ ζῶν (water of life) | v.11 πόθεν οὖν ἔχεις τὸ ὕδωρ τὸ ζῶν (Samaritan woman on well-logistics) | v.13–14 Jesus: ὃς δ' ἂν πίῃ … πηγὴ ὕδατος ἁλλομένου εἰς ζωὴν αἰώνιον |
| John 4:31–34 | βρῶσιν ἔχω φαγεῖν | v.33 disciples ask whether someone brought him food | v.34 ἐμὸν βρῶμά ἐστιν ἵνα ποιήσω τὸ θέλημα (copula of identification) |
| John 6:32–58 | ὁ ἄρτος ὁ ζῶν / σάρξ | v.52 Πῶς δύναται οὗτος ἡμῖν δοῦναι τὴν σάρκα φαγεῖν; | discourse self-interpretation esp. v.63 (τὸ πνεῦμά ἐστιν τὸ ζωοποιοῦν) |
| John 7:37–39 | ποταμοὶ … ὕδατος ζῶντος | (no audience objection stage) | **narrator aside**: v.39 τοῦτο δὲ εἶπεν περὶ τοῦ Πνεύματος |
| John 11:11–14 | Λάζαρος … κεκοίμηται | v.12 disciples: "if he sleeps he will recover" (literal) | v.14 narrator-cued speaker correction: τότε … παρρησίᾳ Λάζαρος ἀπέθανεν |
| John 12:32–33 | ὑψωθῶ ἐκ τῆς γῆς | (no explicit objection) | **narrator aside**: v.33 τοῦτο δὲ ἔλεγεν σημαίνων ποίῳ θανάτῳ |
| John 21:20–23 | ἐὰν αὐτὸν θέλω μένειν | brethren spread rumour Beloved Disciple won't die | v.23 narrator aside: καὶ οὐκ εἶπεν δὲ αὐτῷ ὁ Ἰησοῦς ὅτι οὐκ ἀποθνῄσκει |
| Matt 13:36–43 | parable of tares | (disciples request explanation) | v.37–39 string of copular identification: ὁ σπείρων … ἐστίν, ὁ ἀγρός ἐστιν, τὸ καλὸν σπέρμα εἰσίν, τὰ ζιζάνιά εἰσιν — identical to Rev 1:20 copular-pairing formula |
| Luke 8:11 | ὁ σπόρος | (parable of sower) | ἔστιν δὲ αὕτη ἡ παραβολή· ὁ σπόρος ἐστὶν ὁ λόγος τοῦ Θεοῦ |
| Rev 17:7–18 | γυνὴ + θηρίον + ἑπτὰ κεφαλαί + δέκα κέρατα | (seer addressed directly) | v.9 αἱ ἑπτὰ κεφαλαὶ ὄρη εἰσίν … v.12 τὰ δέκα κέρατα … βασιλεῖς εἰσιν … v.18 ἡ γυνὴ … ἐστὶν ἡ πόλις — sustained copular identification formula, Rev 1:20 writ large |
| Gal 4:24 | Hagar and Sarah | (rhetorical) | ἅτινά ἐστιν ἀλληγορούμενα — explicit genre-labelling |

## Grammar of the Three Correction Mechanisms

### (a) Narrator Aside: περί + genitive + imperfect ἔλεγεν / εἶπεν

The evangelist uses a **background-imperfect** (ἔλεγεν, John 2:21 / 7:39 / 21:23 / 8:27) or aorist εἶπεν with περί + genitive to identify the intended referent. The imperfect is common in Johannine commentary clauses because it describes the sustained or habitual force of the saying rather than a single punctiliar utterance. Wallace 540–544 on the **descriptive/customary imperfect** in narrative parentheses.

The prepositional phrase περί + gen. ("concerning X") grammatically **substitutes the true referent for the ostensive one** without requiring a copula: the speaker said Y on the surface but was speaking περί X.

### (b) Speaker Self-Interpretation: restatement + substitution

The same speaker reformulates the utterance. The grammatical hallmark is:
- **Same main-verb construction** preserved (ἐὰν μή τις γεννηθῇ in John 3:3 and 3:5),
- **One element swapped** for its non-literal equivalent (ἄνωθεν → ἐξ ὕδατος καὶ Πνεύματος).

The retained frame signals to the reader that v.5 is a re-utterance of v.3, not a new teaching; the swap identifies which element was figurative.

### (c) Copular Identification: X εἰσίν / ἐστίν Y

A present-indicative form of εἰμί (V-PAI-3S / V-PAI-3P) with matching case, number, and gender on both flanks. In Greek equational copular clauses the subject is usually the **articular** noun and the predicate nominative the **anarthrous** (Wallace 42–46, BDF §273), but in identification contexts (Rev 1:20; Matt 13:38–39; Rev 17:9, 12, 18) **both may be articular** — this is the "convertible proposition" (Wallace 41): A = B where both are unique definite referents.

## Contrast with Superficially Similar Patterns

| Pattern | What it does | Distinction from self-interpretation |
|---------|--------------|-------------------------------------|
| **Simile with ὡς / ὥσπερ / ὁμοίως** (Rev 1:13 ὅμοιον υἱὸν ἀνθρώπου; Matt 13:31 ὁμοία ἐστίν) | Speaker openly flags the comparison | No literal-misreading slot; no hidden figure to decode |
| **Parable followed by no interpretation** (many Synoptic parables) | Leaves the figure opaque | No in-text decoding supplied |
| **Rhetorical question with obvious answer** (Matt 12:26; John 11:9) | Elicits audience's own inference | No audience miscomprehension corrected |
| **Proverb quotation** (Matt 15:14 τυφλοὶ τυφλῶν ὁδηγοί) | Generic wisdom, not a specific figurative referent | No in-text X = Y unlock |
| **Apocalyptic-narrative prolepsis** ([apocalyptic-narrative-prolepsis](apocalyptic-narrative-prolepsis.md)) | Re-narration of one scene under different aspect | Not a figurative/literal divide but a temporal-aspectual one |

## Hermeneutical Implication (Context-Neutral)

Where a NT didactic text (a) uses a concrete term, (b) triggers a literal-reading objection or absurdity within the same pericope, and (c) supplies a non-literal referent via one of the three mechanisms above, the text has **performed its own interpretation**. Any reading that retains the strictly-literal sense for the original utterance after the in-text correction has to explain why the correction clause exists. Conversely, readings that apply the non-literal referent to cognate imagery elsewhere (other "temple" sayings, other "leaven" sayings, other "star"/"lampstand" imagery) do so on an **analogical**, not a **grammatical**, basis — the self-correction is given for the single utterance in which it appears, and its extension to parallels is a separate interpretive step.

This library entry documents the grammatical phenomenon; it does not adjudicate which extensions are warranted.

## References

- **Wallace, *Greek Grammar Beyond the Basics***
  - 40–48 — subject / predicate nominative in copular sentences; convertible propositions
  - 94–100 — genitive of apposition / epexegetical genitive (John 2:21 τοῦ ναοῦ τοῦ σώματος αὐτοῦ)
  - 458–463 — ὅτι-clause as content clause after cognitive / declarative verbs
  - 540–544 — descriptive / customary imperfect in narrative aside
- **BDF §§273** — article on subject vs. predicate nominative
- **BDF §§396–397** — ὅτι-clauses in Koine indirect discourse
- **BDAG ἄνωθεν** §§1–3 — dual sense "from above" / "again"
- **BDAG ζύμη / μυστήριον / ναός / γεννάω** — lexical range of the four paradigm terms
- **Culpepper, *Anatomy of the Fourth Gospel*** (1983) — chapter on Johannine misunderstanding as narrative device (the φιλολογικὴ δικότησις convention)

## Related Library Entries

- [genitive-of-quality-apposition](genitive-of-quality-apposition.md) — the Johannine aside in 2:21 uses genitive of apposition
- [participle-legon-discourse](participle-legon-discourse.md) — speech-introducing participle in Matt 16:7 λέγοντες ὅτι
- [reflexive-hoti-display](reflexive-hoti-display.md) — cognate content-ὅτι construction (display-content vs. here, figure-decoding)
- [apocalyptic-narrative-prolepsis](apocalyptic-narrative-prolepsis.md) — different Revelation hermeneutical pattern (temporal, not symbol-to-referent)

---
*Generated from: greek_parser.py (--verse) on JHN 2:19–21, JHN 3:3–5, JHN 4:10–14, JHN 6:52, MAT 16:6–12, REV 1:20*
*Last updated: 2026-04-18*
