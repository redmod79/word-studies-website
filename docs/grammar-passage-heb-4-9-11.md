# Grammar Analysis: Hebrews 4:9-11 (The Remaining Sabbath-Rest)

**Mode:** Passage unit analysis (context-neutral)
**Scope:** Heb 4:9-11 as a coherent discourse unit — the conclusion (`ἄρα`, v.9) drawn from the Heb 3:7-4:8 argument, the explanatory ground (`γάρ`, v.10), and the resulting exhortation (`οὖν`, v.11).
**Aim:** Verse-by-verse parsing, tense/mood/voice map, and documentation of the load-bearing grammatical features: (a) the present passive indicative `ἀπολείπεται` (v.9), (b) the three-word "rest" vocabulary across Heb 3-4 (`κατάπαυσις`, `σαββατισμός`, `καταπαύω`), (c) the lexical switch from `κατάπαυσις` to `σαββατισμός` at v.9, (d) the `ὥσπερ` comparison in v.10, (e) clause structure of vv.9-11. Grammar only; interpretive theology is deferred to downstream studies.

---

## 1. Text (Nestle 1904 / parser output with KJV)

| v. | Greek (N1904) | KJV |
|----|---------------|-----|
| 9 | ἄρα ἀπολείπεται σαββατισμὸς τῷ λαῷ τοῦ Θεοῦ. | There remaineth therefore a rest to the people of God. |
| 10 | ὁ γὰρ εἰσελθὼν εἰς τὴν κατάπαυσιν αὐτοῦ καὶ αὐτὸς κατέπαυσεν ἀπὸ τῶν ἔργων αὐτοῦ, ὥσπερ ἀπὸ τῶν ἰδίων ὁ Θεός. | For he that is entered into his rest, he also hath ceased from his own works, as God [did] from his. |
| 11 | Σπουδάσωμεν οὖν εἰσελθεῖν εἰς ἐκείνην τὴν κατάπαυσιν, ἵνα μὴ ἐν τῷ αὐτῷ τις ὑποδείγματι πέσῃ τῆς ἀπειθείας. | Let us labour therefore to enter into that rest, lest any man fall after the same example of unbelief. |

---

## 2. Verse-by-Verse Parsing Tables (from `greek_parser.py`)

### Heb 4:9

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | ἄρα | ἄρα | G686 | PRT (inferential particle — "therefore / so then") |
| 2 | ἀπολείπεται | ἀπολείπω | G620 | **V-PPI-3S** (Pres **Pass** Ind 3s — "is left / remains") |
| 3 | σαββατισμὸς | σαββατισμός | G4520 | **N-NSM** (Nom Sg M — grammatical subject; NT **hapax**) |
| 4 | τῷ λαῷ | ὁ / λαός | G3588/G2992 | T-DSM + N-DSM (dative of advantage — "for the people") |
| 5 | τοῦ Θεοῦ | ὁ / θεός | G3588/G2316 | T-GSM + N-GSM (possessive genitive — "of God") |

**Verbal frame:** a single finite verb (`ἀπολείπεται`, pres.pass.ind.) with `σαββατισμός` as nominative subject and `τῷ λαῷ` as dative of advantage. The clause is verb-initial after the inferential particle `ἄρα`, which fronts the conclusion. No expressed agent.

### Heb 4:10

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | ὁ … εἰσελθὼν | ὁ / εἰσέρχομαι | G3588/G1525 | T-NSM + **V-2AAP-NSM** (2-Aor Act Ptcp Nom Sg M — substantival "the one who has entered") |
| 2 | γὰρ | γάρ | G1063 | CONJ (explanatory — grounding v.9) |
| 3 | εἰς τὴν κατάπαυσιν | εἰς / ὁ / κατάπαυσις | G1519/G3588/G2663 | Prep + T-ASF + N-ASF (goal of εἰσέρχομαι) |
| 4 | αὐτοῦ | αὐτός | G846 | P-GSM (possessive genitive — "his [rest]") |
| 5 | καὶ αὐτὸς | καί / αὐτός | G2532/G846 | CONJ (adjunctive "also") + P-NSM (intensive pronoun) |
| 6 | κατέπαυσεν | καταπαύω | G2664 | **V-AAI-3S** (Aor Act Ind 3s — "ceased / rested") |
| 7 | ἀπὸ τῶν ἔργων αὐτοῦ | ἀπό / ὁ / ἔργον / αὐτός | G575/G3588/G2041/G846 | Prep (+gen. separation) + T-GPN + N-GPN + P-GSM |
| 8 | ὥσπερ | ὥσπερ | G5618 | ADV (comparative — "just as") |
| 9 | ἀπὸ τῶν ἰδίων | ἀπό / ὁ / ἴδιος | G575/G3588/G2398 | Prep (+gen.) + T-GPN + A-GPN (substantival "his own [works]") |
| 10 | ὁ Θεός | ὁ / θεός | G3588/G2316 | T-NSM + N-NSM (subject of the elided verb in the ὥσπερ clause) |

**Verbal frame:** one main finite verb (`κατέπαυσεν`, aor.act.ind.) with a fronted substantival 2-aor.act.ptcp (`ὁ εἰσελθών`) as its subject. The `ὥσπερ` clause is **verb-elliptical**: `ὥσπερ ἀπὸ τῶν ἰδίων ὁ Θεός` reuses `κατέπαυσεν` by gapping (the KJV supplies "[did]"). `αὐτός` (G846, nominative) is intensive — "he himself also."

### Heb 4:11

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | Σπουδάσωμεν | σπουδάζω | G4704 | **V-AAS-1P** (Aor Act Subj 1p — hortatory subjunctive "let us be diligent") |
| 2 | οὖν | οὖν | G3767 | CONJ (inferential — "therefore") |
| 3 | εἰσελθεῖν | εἰσέρχομαι | G1525 | **V-2AAN** (2-Aor Act Inf — complement of σπουδάσωμεν) |
| 4 | εἰς ἐκείνην τὴν κατάπαυσιν | εἰς / ἐκεῖνος / ὁ / κατάπαυσις | G1519/G1565/G3588/G2663 | Prep + D-ASF + T-ASF + N-ASF (goal — "into that rest") |
| 5 | ἵνα μὴ | ἵνα / μή | G2443/G3361 | CONJ + PRT-N (negative purpose clause) |
| 6 | ἐν τῷ αὐτῷ … ὑποδείγματι | ἐν / ὁ / αὐτός / ὑπόδειγμα | G1722/G3588/G846/G5262 | Prep + T-DSN + P-DSN + N-DSN ("in the same example") |
| 7 | τις | τὶς | G5100 | X-NSM (indefinite pronoun — "anyone," subject of πέσῃ) |
| 8 | πέσῃ | πίπτω | G4098 | **V-2AAS-3S** (2-Aor Act Subj 3s — verb of the ἵνα clause) |
| 9 | τῆς ἀπειθείας | ὁ / ἀπείθεια | G3588/G543 | T-GSF + N-GSF (genitive of quality/source modifying ὑποδείγματι — "of disobedience") |

**Verbal frame:** hortatory aor.act.subj. (`Σπουδάσωμεν`) + complementary 2-aor.act.inf. (`εἰσελθεῖν`), followed by a negative-purpose `ἵνα μή` clause whose verb is 2-aor.act.subj. (`πέσῃ`). The indefinite `τις` is the subject of `πέσῃ`. `ὑποδείγματι` is governed by `ἐν` and qualified by the genitive `τῆς ἀπειθείας` (separated from its head by hyperbaton — `ἐν τῷ αὐτῷ τις ὑποδείγματι`).

---

## 3. Load-Bearing Grammatical Features

### 3.1 `ἀπολείπεται` (v.9) — Present Passive Indicative

**Morphology.** `ἀπολείπεται` — V-PPI-3S from `ἀπολείπω` (G620), compound `ἀπό` + `λείπω` ("leave"). The form is **present tense, passive voice, indicative mood, 3rd singular**. The parser tags it unambiguously: `[V-PPI-3S] Pres Pass Ind Sg thirdPers`. (`ἀπολείπω` is not a deponent verb; the active occurs at 2 Tim 4:13, 20; Titus 1:5 — see §4 — so the passive morphology here is a genuine passive, not a middle-deponent.)

**Tense — present.** The Greek present indicative encodes **imperfective aspect**: the situation is portrayed as ongoing, in force, not completed. In a stative/existential predicate like "X remains," the imperfective present asserts a **currently-standing state of affairs** at the author's moment of writing — not a past event and not merely a future prospect. The translation "there remaineth" (KJV) / "there remains" (modern) captures this: the verb makes a present-time claim that something is still in effect.

**Voice — passive.** The passive of `ἀπολείπω` ("to be left") presents `σαββατισμός` as the **subject undergoing the leaving** — it is "left over / left remaining" rather than the author or anyone leaving it. The agent of the leaving is **unexpressed**: there is no `ὑπό`/`παρά`/`ἀπό` + genitive and no dative of means. An agent-less passive in a God-saturated argument is the formal pattern of the **divine passive** — see [greek/divine-passive](../greek/divine-passive.md); the leaving-remaining is something brought about and left standing by God, not by human decision. Grammatically the passive removes any human subject from the verb: the "rest" is not something the people produce or institute; it is **left for them** (`τῷ λαῷ`, dative of advantage).

**Combined force.** Present + passive + indicative = a factual assertion that a Sabbath-rest **stands left-over, in force, for God's people, as of the time of writing**. The imperfective present excludes a reading on which the thing had lapsed; the indicative mood makes it an assertion of fact rather than a wish or contingency. Compare the identical form `ἀπολείπεται` at Heb 4:6 (the entry "remains" for some to enter) and Heb 10:26 (no sacrifice "remains") — in all three the present passive of this verb states what is or is not still on hand. See [greek/aorist-passive-indicative](../greek/aorist-passive-indicative.md) for the contrasting aorist passive (bounded past event); the present passive here is deliberately **not** aorist — the author is not narrating a completed leaving but asserting a continuing one.

### 3.2 The Three "Rest" Words Across Hebrews 3-4

The argument of Heb 3:7-4:11 deploys **three distinct lexemes** in the semantic field of rest. They must be kept apart morphologically:

| Lemma | Strong's | Class | Gloss | Occurrences (NT) |
|-------|----------|-------|-------|------------------|
| `κατάπαυσις` | G2663 | Noun (3rd decl., fem.) | "rest, resting-place, repose" | 9× — Acts 7:49; **Heb 3:11, 18; 4:1, 3 (×2), 5, 10, 11** |
| `καταπαύω` | G2664 | Verb (denominative) | "cause to rest, give rest; (intr.) cease, rest" | 4× — Acts 14:18; **Heb 4:4, 8, 10** |
| `σαββατισμός` | G4520 | Noun (verbal, masc.) | "a sabbath-keeping, sabbath-rest, sabbath-observance" | **1× — Heb 4:9 only (hapax legomenon)** |

**(a) `κατάπαυσις` (G2663) — the running term.** This noun is the author's **default word for "rest" throughout the pericope**. Eight of its nine NT occurrences are in Heb 3-4. It is consistently feminine accusative singular (`κατάπαυσιν`), governed by `εἰς` as the goal of entering (`εἰσέρχομαι εἰς τὴν κατάπαυσιν`). It is the term in the OT quotation the author is expounding — Ps 95:11 LXX, cited at Heb 3:11 and re-cited at 4:3, 5: `εἰ εἰσελεύσονται εἰς τὴν κατάπαυσίν μου` ("they shall [not] enter into my rest"). `κατάπαυσις` is therefore the **inherited, quotation-anchored vocabulary**: the word the argument is given by its proof-text.

**(b) `καταπαύω` (G2664) — the cognate verb.** The verb cognate with `κατάπαυσις`. In Heb 3-4 it appears three times, each aorist active indicative 3rd singular (`κατέπαυσεν`):
- **4:4** — of God: `κατέπαυσεν ὁ Θεός … ἀπὸ … τῶν ἔργων αὐτοῦ` (citing Gen 2:2 LXX — God "rested/ceased" on the seventh day).
- **4:8** — of Joshua: `εἰ … αὐτοὺς Ἰησοῦς κατέπαυσεν` ("if Joshua had given them rest").
- **4:10** — of the believer: `καὶ αὐτὸς κατέπαυσεν ἀπὸ τῶν ἔργων αὐτοῦ`.
The verb and noun share a root, so `κατάπαυσις` is morphologically "the `καταπαύω`-state." The aorist `κατέπαυσεν` views the entering-into-rest / ceasing as a **bounded, completed act** (see [greek/aorist-passive-indicative](../greek/aorist-passive-indicative.md) for aorist aspect; here active).

**(c) `σαββατισμός` (G4520) — the hapax.** A **NT hapax legomenon** (one occurrence: Heb 4:9), confirmed by `greek_parser.py --lemma σαββατισμός`. It is a **verbal noun in -μός** built on the verb `σαββατίζω` ("to keep sabbath, observe a sabbath" — LXX Exod 16:30; Lev 23:32; 26:34-35; 2 Chr 36:21), itself denominative from `σάββατον` (G4521, "sabbath"). The Greek `-μός` suffix forms **action/process nouns** (cf. `βαπτισμός` "a washing," `ἁγιασμός` "a sanctifying," `ὀνειδισμός` "a reviling"). Morphologically, then, `σαββατισμός` denotes not merely a state of repose but **the activity/observance of sabbath-keeping** — "a sabbath-celebration." This nominal-formation fact is the chief grammatical datum of v.9.

### 3.3 The Vocabulary Switch — `κατάπαυσις` → `σαββατισμός` at v.9

At v.9 the author, having used `κατάπαυσις` seven times (3:11; 3:18; 4:1; 4:3 ×2; 4:5; and again at 4:10, 11 immediately after), **interrupts that lexical chain to use `σαββατισμός` once**, then **reverts to `κατάπαυσις` in vv.10 and 11**. The switch is local and deliberate, and is observable as plain morphological fact:

| Verse | Rest-word used |
|-------|----------------|
| 3:11 | `κατάπαυσις` |
| 3:18 | `κατάπαυσις` |
| 4:1 | `κατάπαυσις` |
| 4:3 (×2) | `κατάπαυσις` |
| 4:4 | `καταπαύω` (verb) |
| 4:5 | `κατάπαυσις` |
| 4:8 | `καταπαύω` (verb) |
| **4:9** | **`σαββατισμός`** ← switch |
| 4:10 | `κατάπαυσις` (noun) + `καταπαύω` (verb) |
| 4:11 | `κατάπαυσις` |

**Grammatical observations on the switch (context-neutral):**

1. **It is the conclusion-word.** The switch coincides with the inferential particle `ἄρα` ("so then, therefore"). `ἄρα` marks v.9 as the **drawn conclusion** of the preceding argument. The author changes the noun precisely at the point where he states the result — the new word carries the inference, while `κατάπαυσις` carried the cited premise (Ps 95).

2. **Suffix difference in meaning.** `κατάπαυσις` (`-σις`) and `σαββατισμός` (`-μός`) are both verbal nouns, but they are built on **different verbs** with different lexical content. `κατάπαυσις` < `καταπαύω` = "a ceasing, a state of rest/repose." `σαββατισμός` < `σαββατίζω` = "a sabbath-keeping, the observing of a sabbath." The `-μός` formation of `σαββατισμός` foregrounds **ongoing observance/celebration** rather than the bare state of repose denoted by `κατάπαυσις`. The author's word-choice thus shifts the nuance from "the rest [they failed to enter]" to "a sabbath-keeping [that remains]."

3. **Lexical bridge to the Gen 2 sabbath.** `σαββατισμός` is morphologically tied to `σάββατον` (the seventh-day sabbath) and to the LXX `κατέπαυσεν … τῇ ἡμέρᾳ τῇ ἑβδόμῃ` of v.4. The chosen word lexically connects the "rest" of the argument back to the **seventh-day sabbath of creation** quoted at v.4, in a way `κατάπαυσις` (a more generic "repose") does not. This is a grammatical/lexical fact about the word's stem; what the author intends to build on it is the downstream study's question.

4. **It is not a casual synonym.** Because `σαββατισμός` is a hapax — used nowhere else in the NT, and not used elsewhere even within this same pericope where `κατάπαυσις` was readily available — the single deployment is marked. An author who needed only a synonym for variety could have repeated `κατάπαυσις` (as he in fact does in vv.10-11). The introduction of an otherwise-unused, morphologically specific noun at the conclusion is a deliberate lexical signal.

### 3.4 The `ὥσπερ` Comparison in v.10

**Morphology and class.** `ὥσπερ` (G5618) is a **comparative adverb/conjunction**, a strengthened form of `ὡς` + the enclitic `-περ` ("even, precisely"). It introduces a clause of **comparison/manner**: "(just) exactly as, in the very way that." The `-περ` particle adds emphasis — `ὥσπερ` is a tighter, more exact comparative than plain `ὡς` ("the believer rests *precisely as* God rested," not merely "somewhat like").

**The comparison's two terms.** `ὥσπερ` in v.10 links two ceasings:

- **Protasis-equivalent (main clause):** `ὁ … εἰσελθὼν … καὶ αὐτὸς κατέπαυσεν ἀπὸ τῶν ἔργων αὐτοῦ` — "the one who has entered … himself also ceased from his works."
- **`ὥσπερ` clause:** `ὥσπερ ἀπὸ τῶν ἰδίων ὁ Θεός` — "just as God [ceased] from his own [works]."

**Verb-gapping (ellipsis).** The `ὥσπερ` clause has **no expressed verb**. `κατέπαυσεν` from the main clause is **gapped/elided** and must be supplied: `ὥσπερ [κατέπαυσεν] ἀπὸ τῶν ἰδίων ὁ Θεός`. The KJV marks the supplied verb with brackets: "as God [did] from his." This ellipsis is standard Greek comparative syntax — the shared verb is stated once and understood in the parallel member. The grammatical effect is to make the believer's `κατέπαυσεν` and God's (elided) `κατέπαυσεν` **the identical action**, not merely two similar actions: one verb, two subjects.

**Parallel prepositional phrases.** The comparison is reinforced by matched `ἀπό` + genitive phrases of separation:
- believer: `ἀπὸ τῶν ἔργων αὐτοῦ` ("from his works")
- God: `ἀπὸ τῶν ἰδίων` ("from his own [works]")

`τῶν ἰδίων` is the substantival adjective `ἴδιος` (G2398, "one's own") standing in for `τῶν ἰδίων ἔργων` — "his own works," with `ἔργων` itself gapped from the main clause. The parallel structure (entered-one : God :: ceased-from-works : ceased-from-own-works) is a balanced **A-B-A′-B′ comparison**: the syntax presents the believer's rest as patterned on, and of the same kind as, God's creation-rest.

**`καὶ αὐτὸς` — the intensive pronoun.** `αὐτός` here is nominative (`P-NSM`), agreeing with the subject `ὁ εἰσελθών`. In the nominative, agreeing with the subject, `αὐτός` is **intensive** ("he himself"), and with adjunctive `καί` it yields "**he himself also**." The pronoun underscores that the entered-one's ceasing is genuinely his own act, set in parallel with God's — strengthening the `ὥσπερ` comparison.

### 3.5 Clause Structure of Heb 4:9-11

The three verses form a **conclusion → ground → exhortation** sequence, each marked by its own discourse connective:

```
v.9   [ἄρα]  ── INFERENTIAL CONCLUSION
      ἀπολείπεται σαββατισμὸς τῷ λαῷ τοῦ Θεοῦ
      └ V-PPI-3S (main) + N-NSM subj. + dat. of advantage
      "So then: a sabbath-rest remains for the people of God."

v.10  [γάρ]  ── EXPLANATORY GROUND (why v.9 is true)
      ὁ … εἰσελθὼν … κατέπαυσεν ἀπὸ τῶν ἔργων αὐτοῦ
      │  └ subject = substantival ptcp (ὁ εἰσελθών, V-2AAP-NSM)
      │  └ main verb = κατέπαυσεν (V-AAI-3S)
      └ [ὥσπερ] ── COMPARATIVE SUB-CLAUSE (verb gapped)
            ἀπὸ τῶν ἰδίων ὁ Θεός
            "just as God [ceased] from his own."

v.11  [οὖν]  ── INFERENTIAL EXHORTATION (response to v.9-10)
      Σπουδάσωμεν … εἰσελθεῖν εἰς ἐκείνην τὴν κατάπαυσιν
      │  └ main verb = hortatory subj. Σπουδάσωμεν (V-AAS-1P)
      │  └ complementary inf. εἰσελθεῖν (V-2AAN)
      └ [ἵνα μή] ── NEGATIVE PURPOSE CLAUSE
            τις … πέσῃ τῆς ἀπειθείας
            └ verb = πέσῃ (V-2AAS-3S), subj. = indefinite τις
```

**Discourse connectives — the backbone:**

- **v.9 `ἄρα` (G686).** Inferential particle drawing a conclusion from 3:7-4:8. Placed clause-initially, it frames the whole of v.9 as a deduction. `ἄρα` typically signals a logical result ("so then, consequently").
- **v.10 `γάρ` (G1063).** Explanatory/causal conjunction. v.10 does not advance a new point; it **grounds v.9** — explaining *why* a sabbath-rest still remains (because the pattern of entering-rest is the cessation-from-works modeled by God).
- **v.11 `οὖν` (G3767).** Inferential conjunction. Where `ἄρα` drew a theological conclusion, `οὖν` draws a **practical/hortatory** one: given vv.9-10, "therefore let us be diligent."

**Verb hierarchy:**

| Verse | Verb | Parsing | Clause role |
|-------|------|---------|-------------|
| 9 | ἀπολείπεται | V-PPI-3S | main verb of the conclusion |
| 10 | εἰσελθών | V-2AAP-NSM | substantival ptcp = subject of κατέπαυσεν |
| 10 | κατέπαυσεν | V-AAI-3S | main verb of the ground clause |
| 10 | [κατέπαυσεν] | (gapped) | elided verb of the ὥσπερ clause |
| 11 | Σπουδάσωμεν | V-AAS-1P | main verb (hortatory subjunctive) |
| 11 | εἰσελθεῖν | V-2AAN | complementary infinitive to Σπουδάσωμεν |
| 11 | πέσῃ | V-2AAS-3S | verb of the ἵνα μή purpose clause |

**Notable syntactic points:**

1. **v.10 fronted substantival participle.** `ὁ … εἰσελθών` ("the one who has entered") is a substantival 2-aor.act.ptcp serving as the **subject** of `κατέπαυσεν`. The intervening `γάρ` splits the article from its participle (`ὁ γὰρ εἰσελθών`), standard Greek placement of the postpositive conjunction.
2. **v.10 verb-ellipsis in the `ὥσπερ` clause** — see §3.4.
3. **v.11 hortatory subjunctive.** `Σπουδάσωμεν` (1st pl. aor. subj.) is a **hortatory/cohortative subjunctive** — "let us …" — the standard Koine construction for a 1st-plural exhortation (no imperative exists for 1st person). The aorist aspect presents the diligence as a single, decisive resolve.
4. **v.11 `ἵνα μή` negative purpose.** `ἵνα` + `μή` + subjunctive (`πέσῃ`) is the regular negative-purpose construction ("so that … not / lest"). The subject of `πέσῃ` is the indefinite pronoun `τις` ("anyone").
5. **v.11 hyperbaton.** `ἐν τῷ αὐτῷ τις ὑποδείγματι` — the indefinite `τις` is inserted **between the modifier `τῷ αὐτῷ` and its head noun `ὑποδείγματι`**. This word-order separation (hyperbaton) is stylistic; the sense is "in the same example [of disobedience]." `τῆς ἀπειθείας` is a genitive (of quality/source) modifying `ὑποδείγματι`, likewise separated from its head.

---

## 4. Tense/Mood/Voice Inventory for Heb 4:9-11

**Indicatives (finite main-line):**

| Verse | Form | Parsing | Lemma |
|-------|------|---------|-------|
| 9 | ἀπολείπεται | V-PPI-3S | ἀπολείπω |
| 10 | κατέπαυσεν | V-AAI-3S | καταπαύω |

**Subjunctives:**

| Verse | Form | Parsing | Function |
|-------|------|---------|----------|
| 11 | Σπουδάσωμεν | V-AAS-1P | hortatory ("let us …") |
| 11 | πέσῃ | V-2AAS-3S | verb of ἵνα μή purpose clause |

**Infinitive:**

| Verse | Form | Parsing | Function |
|-------|------|---------|----------|
| 11 | εἰσελθεῖν | V-2AAN | complementary to Σπουδάσωμεν |

**Participle:**

| Verse | Form | Parsing | Function |
|-------|------|---------|----------|
| 10 | εἰσελθών | V-2AAP-NSM | substantival — subject of κατέπαυσεν |

**Voice distribution:** one passive (`ἀπολείπεται`, v.9 — the agent-less, theologically significant form); all other verbs active. No middle/deponent forms in the pericope.

**Aspect contrast worth noting:** the **present** `ἀπολείπεται` (imperfective — ongoing state) in v.9 stands against the **aorists** `κατέπαυσεν` / `εἰσελθών` / `εἰσελθεῖν` / `πέσῃ` (perfective — bounded events) in vv.10-11. The author asserts a *standing* state (rest remains) and then speaks of *entering* it and *resting* as completed/decisive acts.

---

## 5. Lemma Inventories (verified by `greek_parser.py --lemma`)

**`ἀπολείπω` (G620) — 7× NT:**

| Reference | Form | Parsing |
|-----------|------|---------|
| 2 Tim 4:13 | ἀπέλιπον | V-IAI-1S (Impf **Act**) |
| 2 Tim 4:20 | ἀπέλιπον | V-IAI-1S (Impf **Act**) |
| Titus 1:5 | ἀπέλιπόν | V-IAI-1S (Impf **Act**) |
| **Heb 4:6** | **ἀπολείπεται** | **V-PPI-3S** (Pres **Pass**) |
| **Heb 4:9** | **ἀπολείπεται** | **V-PPI-3S** (Pres **Pass**) |
| Heb 10:26 | ἀπολείπεται | V-PPI-3S (Pres **Pass**) |
| Jude 1:6 | ἀπολιπόντας | V-2AAP-APM (2-Aor **Act**) |

The three active forms (Paul, Titus) confirm `ἀπολείπω` is **not deponent**; the three present-passive forms are all in Hebrews (4:6, 4:9, 10:26) and all carry the sense "is left remaining."

**`κατάπαυσις` (G2663) — 9× NT:** Acts 7:49; Heb 3:11, 18; 4:1, 3 (×2), 5, 10, 11. (8 of 9 in Heb 3-4.)

**`καταπαύω` (G2664) — 4× NT:** Acts 14:18; Heb 4:4, 8, 10. (3 of 4 in Heb 4, all `κατέπαυσεν` V-AAI-3S.)

**`σαββατισμός` (G4520) — 1× NT:** Heb 4:9 only — **hapax legomenon**.

---

## 6. Cross-References

**Grammar reference library:**
- [greek/divine-passive](../greek/divine-passive.md) — for the agent-less passive `ἀπολείπεται` (§3.1)
- [greek/aorist-passive-indicative](../greek/aorist-passive-indicative.md) — for the aorist-aspect contrast against the present `ἀπολείπεται` (§3.1, §4)
- [greek/participle-perfect-passive-state](../greek/participle-perfect-passive-state.md) — for participle-as-state syntax, cf. the substantival ptcp `ὁ εἰσελθών`
- [passages/heb-6-13-18](./heb-6-13-18.md) — companion Hebrews passage analysis (oath/immutability discourse)

**Word studies (not all may exist yet — create as needed):**
- G4520-sabbatismos (the v.9 hapax — anchor word of the passage)
- G2663-katapausis (the running "rest" noun, 8× in Heb 3-4)
- G2664-katapauo (the cognate verb, 3× in Heb 4)
- G620-apoleipo (the "remains" verb, 3× present-passive in Hebrews)
- G1525-eiserchomai, G5618-hosper, G4704-spoudazo, G5262-hupodeigma, G543-apeitheia, G2992-laos

---

## 7. Data Source Notes

- Greek text: Nestle 1904 (via `greek_parser.py`, Text-Fabric N1904 dataset).
- KJV: `D:/bible/tools/data/kjv.txt`.
- All parsings verified by `greek_parser.py --verse "HEB 4:9"`, `"HEB 4:10"`, `"HEB 4:11"`, plus context verses `"HEB 3:11"`, `"HEB 4:3"`, `"HEB 4:4"`.
- Lemma inventories verified by `greek_parser.py --lemma` for ἀπολείπω, κατάπαυσις, καταπαύω, σαββατισμός.
- This is a context-neutral grammar analysis. Identification of the "two/three rest concepts" and any theological inference from the vocabulary switch or the divine passive are deferred to downstream studies.
