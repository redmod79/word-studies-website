# Grammar Analysis: Hebrews 6:13-18 (The Abrahamic Oath and the Two Immutable Things)

**Mode:** Passage unit analysis (context-neutral)
**Scope:** Heb 6:13-18 as a coherent discourse unit — God's oath to Abraham (vv.13-15) grounded in a general principle about human oaths (v.16) and culminating in the "two immutable things" argument (vv.17-18).
**Aim:** Verse-by-verse parsing, tense/mood/voice map, and documentation of the four load-bearing grammatical features: (a) the two-immutable-things logic, (b) the articular aorist infinitive ἐπιδεῖξαι, (c) ἐμεσίτευσεν (G3315) and the "middle-voice" question, (d) the adjective ἀμετάθετος (G276). Grammar only; interpretive theology is deferred to downstream studies.

---

## 1. Text (Nestle 1904 / parser output with KJV)

| v. | Greek (N1904) | KJV |
|----|---------------|-----|
| 13 | Τῷ γὰρ Ἀβραὰμ ἐπαγγειλάμενος ὁ Θεός, ἐπεὶ κατ' οὐδενὸς εἶχεν μείζονος ὀμόσαι, ὤμοσεν καθ' ἑαυτοῦ, | For when God made promise to Abraham, because he could swear by no greater, he sware by himself, |
| 14 | λέγων Εἰ μὴν εὐλογῶν εὐλογήσω σε καὶ πληθύνων πληθυνῶ σε· | Saying, Surely blessing I will bless thee, and multiplying I will multiply thee. |
| 15 | καὶ οὕτως μακροθυμήσας ἐπέτυχεν τῆς ἐπαγγελίας. | And so, after he had patiently endured, he obtained the promise. |
| 16 | ἄνθρωποι γὰρ κατὰ τοῦ μείζονος ὀμνύουσιν, καὶ πάσης αὐτοῖς ἀντιλογίας πέρας εἰς βεβαίωσιν ὁ ὅρκος· | For men verily swear by the greater: and an oath for confirmation is to them an end of all strife. |
| 17 | ἐν ᾧ περισσότερον βουλόμενος ὁ Θεὸς ἐπιδεῖξαι τοῖς κληρονόμοις τῆς ἐπαγγελίας τὸ ἀμετάθετον τῆς βουλῆς αὐτοῦ ἐμεσίτευσεν ὅρκῳ, | Wherein God, willing more abundantly to shew unto the heirs of promise the immutability of his counsel, confirmed it by an oath: |
| 18 | ἵνα διὰ δύο πραγμάτων ἀμεταθέτων, ἐν οἷς ἀδύνατον ψεύσασθαι Θεόν, ἰσχυρὰν παράκλησιν ἔχωμεν οἱ καταφυγόντες κρατῆσαι τῆς προκειμένης ἐλπίδος· | That by two immutable things, in which it was impossible for God to lie, we might have a strong consolation, who have fled for refuge to lay hold upon the hope set before us: |

---

## 2. Verse-by-Verse Parsing Tables (from `greek_parser.py`)

### Heb 6:13

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | Τῷ | ὁ | G3588 | T-DSM |
| 2 | γὰρ | γάρ | G1063 | Conj (inferential-explanatory) |
| 3 | Ἀβραὰμ | Ἀβραάμ | G11 | N-PRI (indecl.) Dat Sg M |
| 4 | ἐπαγγειλάμενος | ἐπαγγέλλομαι | G1861 | **V-ADP-NSM** (Aor **Mid** Ptcp Nom Sg M) |
| 5 | ὁ Θεός | θεός | G2316 | T-NSM + N-NSM (subject) |
| 6 | ἐπεὶ | ἐπεί | G1893 | Conj (causal — "since/because") |
| 7 | κατ' οὐδενὸς | κατά / οὐδείς | G2596/G3762 | Prep (+gen.) + A-GSM-N |
| 8 | εἶχεν | ἔχω | G2192 | **V-IAI-3S** (Impf Act Ind 3s — "he was having") |
| 9 | μείζονος | μέγας | G3173 | A-GSM-**C** (Gen Sg M **comparative** — "greater") |
| 10 | ὀμόσαι | ὀμνύω | G3660 | **V-AAN** (Aor Act Inf) |
| 11 | ὤμοσεν | ὀμνύω | G3660 | **V-AAI-3S** (Aor Act Ind 3s) |
| 12 | καθ' ἑαυτοῦ | κατά / ἑαυτοῦ | G2596/G1438 | Prep (+gen.) + F-3GSM (reflexive) |

**Verbal frame:** one aor.mid.ptcp (ἐπαγγειλάμενος) temporally framing the main verb; one impf.act.ind. (εἶχεν + inf. ὀμόσαι) in the parenthetical causal clause ἐπεί…; one aor.act.ind. finite (ὤμοσεν) as the main clause. Dat. recipient Τῷ Ἀβραάμ fronted. Imperfect εἶχεν with complementary aor.inf. ὀμόσαι expresses a durative modal state ("he had no one greater to swear by"). Reflexive καθ' ἑαυτοῦ echoes LXX Gen 22:16 κατ' ἐμαυτοῦ ὤμοσα.

**Middle voice in ἐπαγγειλάμενος:** aor.mid.dep. of ἐπαγγέλλομαι. Lexically deponent in the NT, but the middle morphology remains semantically apt: to make a promise *for one's own account* / *binding oneself*. Contrast with the action-noun ἐπαγγελία (vv.15, 17) and the passive sense found only rarely.

### Heb 6:14

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | λέγων | λέγω | G3004 | V-PAP-NSM (speech-introducing ptcp.) |
| 2 | Εἰ | εἰ | G1487 | Cond particle |
| 3 | μὴν | μήν (I) | G3375 | Asseverative particle |
| 4 | εὐλογῶν | εὐλογέω | G2127 | **V-PAP-NSM** (Pres Act Ptcp Nom Sg M) |
| 5 | εὐλογήσω | εὐλογέω | G2127 | **V-FAI-1S** (Fut Act Ind 1s) |
| 6 | σε | σύ | G4771 | P-2AS |
| 7 | καὶ | καί | G2532 | Conj |
| 8 | πληθύνων | πληθύνω | G4129 | **V-PAP-NSM** (Pres Act Ptcp Nom Sg M) |
| 9 | πληθυνῶ | πληθύνω | G4129 | **V-FAI-1S** (Fut Act Ind 1s) |
| 10 | σε | σύ | G4771 | P-2AS |

**Verbal frame:** classic Hebrew infinitive-absolute + finite-verb construction calqued into Greek via present participle + cognate future indicative (εὐλογῶν εὐλογήσω / πληθύνων πληθυνῶ). Source is LXX Gen 22:17. The Hellenistic combination εἰ μήν (distinct from classical ἦ μήν) is a Semitic-Greek oath-asseverative corresponding to Hebrew כִּי (see LXX Num 14:23, 28, 35; Job 27:5). See [greek/participle-legon-discourse](../greek/participle-legon-discourse.md) for the speech-introducing λέγων.

### Heb 6:15

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | καὶ οὕτως | καί / οὕτω | G2532/G3779 | Conj + Adv ("and so") |
| 2 | μακροθυμήσας | μακροθυμέω | G3114 | **V-AAP-NSM** (Aor Act Ptcp Nom Sg M — temporal/antecedent "after long-bearing") |
| 3 | ἐπέτυχεν | ἐπιτυγχάνω | G2013 | **V-2AAI-3S** (2-Aor Act Ind 3s — "obtained") |
| 4 | τῆς ἐπαγγελίας | ἐπαγγελία | G1860 | T-GSF + N-GSF (genitive object of ἐπιτυγχάνω) |

**Verbal frame:** antecedent aor.act.ptcp (μακροθυμήσας) + aor.act.ind. finite (ἐπέτυχεν). The 2-aor.ind. ἐπέτυχεν takes a partitive/objective genitive τῆς ἐπαγγελίας (classical syntax for "hit the mark of / attain"). The participle is time-sequential: enduring → obtaining.

### Heb 6:16

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | ἄνθρωποι | ἄνθρωπος | G444 | N-NPM (gnomic/generic subject) |
| 2 | γὰρ | γάρ | G1063 | Conj (explanatory) |
| 3 | κατὰ τοῦ μείζονος | κατά / ὁ / μέγας | G2596/G3588/G3173 | Prep + T-GSM + A-GSM-**C** |
| 4 | ὀμνύουσιν | ὀμνύω | G3660 | **V-PAI-3P** (Pres Act Ind 3p — gnomic present) |
| 5 | καὶ | καί | G2532 | Conj |
| 6 | πάσης αὐτοῖς ἀντιλογίας | πᾶς / αὐτός / ἀντιλογία | G3956/G846/G485 | A-GSF + P-DPM + N-GSF (partitive/attributive genitive) |
| 7 | πέρας | πέρας | G4009 | N-NSN (predicate nominative "end, termination") |
| 8 | εἰς βεβαίωσιν | εἰς / βεβαίωσις | G1519/G951 | Prep + N-ASF ("for confirmation") |
| 9 | ὁ ὅρκος | ὅρκος | G3727 | T-NSM + N-NSM (subject) |

**Verbal frame:** verbless nominal sentence (subject ὁ ὅρκος + predicate noun πέρας) with the prior finite verb ὀμνύουσιν governing the first half. Gnomic present ὀμνύουσιν states a standing custom ("men swear"). The predicate-nominative clause has no copula (classical/koine zero-copula) — "the oath *is* an end of all dispute." Dative αὐτοῖς is dative of reference/advantage ("for them").

**Logic:** v.16 is a **general maxim about human oaths** — it establishes the standard premise on which v.17's argument *a minore ad maius* depends (if human oaths terminate dispute, how much more God's).

### Heb 6:17

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | ἐν ᾧ | ἐν / ὅς | G1722/G3739 | Prep + R-DSM (anaphoric transition — "wherefore / in which circumstance") |
| 2 | περισσότερον | περισσός | G4053 | A-ASN-**C** (comparative neuter acc. as adv. — "more abundantly") |
| 3 | βουλόμενος | βούλομαι | G1014 | **V-PNP-NSM** (Pres M/P Ptcp Nom Sg M — deponent "willing, purposing") |
| 4 | ὁ Θεὸς | θεός | G2316 | T-NSM + N-NSM (subject) |
| 5 | ἐπιδεῖξαι | ἐπιδείκνυμι | G1925 | **V-AAN** (Aor Act Inf) — complement of βουλόμενος |
| 6 | τοῖς κληρονόμοις | κληρονόμος | G2818 | T-DPM + N-DPM (indirect obj. of ἐπιδεῖξαι) |
| 7 | τῆς ἐπαγγελίας | ἐπαγγελία | G1860 | T-GSF + N-GSF (attributive gen. to κληρονόμοις) |
| 8 | τὸ ἀμετάθετον | ἀμετάθετος | G276 | **T-ASN + A-ASN** (substantival articular adjective — "the immutability") |
| 9 | τῆς βουλῆς αὐτοῦ | βουλή / αὐτός | G1012/G846 | T-GSF + N-GSF + P-GSM (objective/subjective gen. + poss.) |
| 10 | ἐμεσίτευσεν | μεσιτεύω | G3315 | **V-AAI-3S** (Aor Act Ind 3s) — NT hapax |
| 11 | ὅρκῳ | ὅρκος | G3727 | N-DSM (dative of means/instrument — "by an oath") |

**Verbal frame:** one main finite verb (ἐμεσίτευσεν) with instrumental dative ὅρκῳ, governed by a circumstantial pres.mid.ptcp. (βουλόμενος) that takes an aor.act.inf. (ἐπιδεῖξαι) as its complement. The direct object of ἐπιδεῖξαι is the substantival articular adjective τὸ ἀμετάθετον τῆς βουλῆς αὐτοῦ. Comparative adverb περισσότερον modifies βουλόμενος ("more abundantly willing"). Dative τοῖς κληρονόμοις τῆς ἐπαγγελίας is indirect object of ἐπιδεῖξαι.

### Heb 6:18

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | ἵνα | ἵνα | G2443 | Conj (purpose — introducing subj.) |
| 2 | διὰ δύο πραγμάτων ἀμεταθέτων | διά / δύο / πρᾶγμα / ἀμετάθετος | G1223/G1417/G4229/G276 | Prep (+gen. means) + A-NUI + N-**GPN** + **A-GPN** (attributive) |
| 3 | ἐν οἷς | ἐν / ὅς | G1722/G3739 | Prep + R-DPN (relative pronoun, neuter pl. antecedent πραγμάτων) |
| 4 | ἀδύνατον | ἀδύνατος | G102 | A-NSN (predicate adj. "impossible") |
| 5 | ψεύσασθαι | ψεύδομαι | G5574 | **V-ADN** (Aor **Mid** Inf — deponent "to lie") |
| 6 | Θεόν | θεός | G2316 | N-ASM (acc. subject of inf.) |
| 7 | ἰσχυρὰν παράκλησιν | ἰσχυρός / παράκλησις | G2478/G3874 | A-ASF + N-ASF (direct obj. of ἔχωμεν) |
| 8 | ἔχωμεν | ἔχω | G2192 | **V-PAS-1P** (Pres Act Subj 1p — purpose after ἵνα) |
| 9 | οἱ καταφυγόντες | καταφεύγω | G2703 | T-NPM + **V-2AAP-NPM** (2-Aor Act Ptcp Nom Pl M — substantival "the ones having fled for refuge") |
| 10 | κρατῆσαι | κρατέω | G2902 | **V-AAN** (Aor Act Inf — purpose/epexegetical to καταφυγόντες) |
| 11 | τῆς προκειμένης | πρόκειμαι | G4295 | T-GSF + **V-PNP-GSF** (Pres M/P Ptcp Gen Sg F — attributive "the set-before-us") |
| 12 | ἐλπίδος | ἐλπίς | G1680 | N-GSF (gen. obj. of κρατῆσαι "to grasp hold of the hope") |

**Verbal frame:** purpose-clause skeleton ἵνα… ἔχωμεν (main pres.act.subj. 1p) with **four dependent infinitives/participles**: (a) aor.mid.inf. ψεύσασθαι under the impersonal predicate ἀδύνατον…Θεόν inside the ἐν οἷς relative clause, (b) 2-aor.act.ptcp καταφυγόντες in apposition to the subject "we," (c) aor.act.inf. κρατῆσαι as telic complement of καταφυγόντες, (d) pres.mid.ptcp προκειμένης as attributive modifier of ἐλπίδος.

**Logic of v.18:** the ἵνα-clause gives the purpose of God's swearing in v.17. Instrumental διά + genitive ("by means of") takes the phrase δύο πραγμάτων ἀμεταθέτων as its regime. The internal ἐν οἷς clause is a **characterizing relative**: "in which [two things] it is impossible for God to lie" — defining the two things as the very locus of divine truthfulness.

---

## 3. Four Load-Bearing Grammatical Features

### 3.1 The "Two Immutable Things" Logic (v.18 δύο πραγμάτων ἀμεταθέτων)

**Surface syntax.** `διά` + genitive plural `δύο πραγμάτων ἀμεταθέτων`, followed by the relative `ἐν οἷς ἀδύνατον ψεύσασθαι Θεόν`. Three grammatical elements combine:

1. **Cardinal + noun agreement** — `δύο` is indeclinable (A-NUI), but the noun `πραγμάτων` (N-GPN) + adjective `ἀμεταθέτων` (A-GPN) carry the case/number/gender. The pair is **neuter plural**, treating "things" abstractly (not "persons" or "acts" specifically).
2. **Attributive adjective in post-nominal position** — `πραγμάτων ἀμεταθέτων` is simple attributive (Smyth §1158; Wallace 306–309). No article on either element: the whole phrase is indefinite/qualitative ("two unchangeable things") inside the instrumental διά + gen. construction.
3. **Characterizing relative clause** — `ἐν οἷς ἀδύνατον ψεύσασθαι Θεόν`. The neuter plural relative `οἷς` (R-DPN) agrees with its antecedent `πραγμάτων`. ἀδύνατον is predicate adj. in an impersonal construction with the infinitive `ψεύσασθαι` (aor.mid.dep.) taking **accusative subject** `Θεόν`. This is the classic impersonal infinitive-with-accusative-subject pattern (Wallace 192–197, 600–601; BDF §§393, 408).

**How the argument hinges on two co-referents.** The argument-form is:

> Premise (v.16): a human oath by something greater is the πέρας ἀντιλογίας — it ends dispute.
> Premise (v.17): God, having nothing greater, swore καθ' ἑαυτοῦ (v.13), and did so to `ἐπιδεῖξαι τὸ ἀμετάθετον τῆς βουλῆς αὐτοῦ`.
> Conclusion (v.18): therefore διὰ δύο πραγμάτων ἀμεταθέτων we have strong consolation.

The grammar leaves the **identity of the two πράγματα** unspecified at the syntactic level (no appositional list, no named pair). The reader must recover the pair from the antecedent discourse. Two parsing-neutral observations:

- The adjective `ἀμεταθέτων` in v.18 repeats the neuter-singular substantival `τὸ ἀμετάθετον` of v.17. Grammatically, the repetition forms a **lexical bridge**: whatever was called "the unchangeable [thing]" in v.17 is now being pluralized to "two unchangeable things."
- The two most grammatically-available antecedents in vv.13-17 are: (1) God's promise / purpose / βουλή (ἐπαγγειλάμενος v.13, ἐπαγγελίας vv.15, 17, βουλῆς v.17), and (2) God's oath (ὤμοσεν v.13, ὅρκος v.16, ὅρκῳ v.17). The passage's surface grammar flags both as in-play without forcing the identification.

The internal ἐν οἷς ἀδύνατον ψεύσασθαι Θεόν clause frames both items as inhering in the divine truthfulness — `ἀδύνατον` + aor.inf. states an absolute impossibility (compare Heb 6:4; 10:4; 11:6; Matt 19:26 for the same impersonal skeleton).

### 3.2 Articular Aorist Infinitive ἐπιδεῖξαι (v.17)

**Morphology.** `ἐπιδεῖξαι` — V-AAN from `ἐπιδείκνυμι` (G1925). Root δεικ- + σ-aorist + infinitive suffix -αι. Augment absent (infinitives never take augment). Not strictly **articular** here (no τό governing the infinitive itself); rather it is a **complementary** (Wallace 598–599) infinitive functioning as the object/complement of the participle `βουλόμενος`.

**Why it looks "articular-like."** The immediate object of `ἐπιδεῖξαι` is the articular substantival adjective `τὸ ἀμετάθετον τῆς βουλῆς αὐτοῦ`. The neuter article τό thus precedes the complex — but governs the adjective, not the infinitive. A true articular infinitive (e.g. εἰς τὸ + inf.) is absent from this passage. This distinction matters: complementary aor.inf. + substantival adj. is different syntax from εἰς τὸ + inf. purpose frame.

**Aspectual force.** Aorist inf. views the showing/demonstrating as a single bounded event (BDF §§337–338; Wallace 554–557) — **not** progressive or repeated. The pres.mid.ptcp `βουλόμενος` supplies the durative subjective state ("being willed to…"); the aor.inf. `ἐπιδεῖξαι` supplies the punctiliar objective act ("to display [once]"). This tense-contrast is the standard Koine pattern for ptcp. + complement-inf.

**NT profile of ἐπιδείκνυμι.** From `greek_parser.py --lemma ἐπιδείκνυμι` (7 NT occurrences):

| Reference | Form | Parsing |
|-----------|------|---------|
| Matt 16:1 | ἐπιδεῖξαι | V-AAN |
| Matt 22:19 | ἐπιδείξατέ | V-AAM-2P |
| Matt 24:1 | ἐπιδεῖξαι | V-AAN |
| Luke 17:14 | ἐπιδείξατε | V-AAM-2P |
| Acts 9:39 | ἐπιδεικνύμεναι | V-PMP-NPF |
| Acts 18:28 | ἐπιδεικνὺς | V-PAP-NSM |
| **Heb 6:17** | **ἐπιδεῖξαι** | **V-AAN** |

The V-AAN form is the most frequent (3/7). Verb semantics across NT: "show / display / exhibit / point out to a witness" — a demonstration-verb, not a revelation-verb (contrast ἀποκαλύπτω, φανερόω). In v.17 the thing demonstrated is abstract (τὸ ἀμετάθετον) and the audience is dative (τοῖς κληρονόμοις); this is forensic-legal register: "to exhibit to the heirs the immutability."

### 3.3 ἐμεσίτευσεν (G3315) — Morphology and the "Middle-Voice" Question

**Morphology.** `ἐμεσίτευσεν` — V-AAI-3S from `μεσιτεύω`. ε-augment + μεσιτευ- stem + σ-aorist + -ε secondary 3s ending → **aorist ACTIVE indicative**, not middle. The parser (`greek_parser.py`) tags this unambiguously: `[V-AAI-3S] Aor Act Ind Sg thirdPers`.

**NT profile.** From `greek_parser.py --lemma μεσιτεύω`: **one** occurrence in the entire NT — Heb 6:17. It is a NT hapax legomenon.

**Why it is often labelled "middle-voice."** Two reasons:

1. **Lexical-semantic middle.** The verb μεσιτεύω ("to act as mediator / to interpose / to go between") belongs to a semantic class — verbs of personal intervention or agency-transfer — that Greek grammarians classify as *semantically* middle-ish (Robertson 802–804; BDF §316; Wallace 413–430). The related noun μεσίτης (G3316, Gal 3:19-20; 1 Tim 2:5; Heb 8:6; 9:15; 12:24) means "mediator/go-between." The semantic field of mediation is inherently reflexive: the subject inserts himself between parties. But **classification as semantic middle does not require middle-voice morphology**; μεσιτεύω takes active endings here.
2. **Translation tradition.** English translations sometimes render "God interposed himself with an oath" (RSV, ESV). The reflexive pronoun "himself" is a translator's addition to bring out the semantic force of mediation; it does not reflect a morphological middle. The KJV "confirmed it by an oath" chooses the active-causal rendering.

**Syntactic frame in v.17.** Three elements cluster around the finite verb:

- Subject: `ὁ Θεὸς` (N-NSM, left-displaced after the `ἐν ᾧ περισσότερον βουλόμενος` participial frame).
- Instrumental dative: `ὅρκῳ` (N-DSM) — dative of means (Wallace 162–163). "God mediated-by-an-oath" / "guaranteed-by-means-of-an-oath."
- No expressed direct object, but the logical object is the `τὸ ἀμετάθετον τῆς βουλῆς αὐτοῦ` displayed under ἐπιδεῖξαι. ἐμεσίτευσεν serves as the main-clause predicate expressing the mode (by-oath) in which the showing-forth is executed.

**Summary.** Morphologically active aorist indicative; semantically in a middle-voice *lexical field*. The parser's verdict (V-AAI-3S) is the disciplined reading; "middle-voice" labels attached to this verb by commentators are statements about the *Aktionsart* / *sense*, not about the parsing.

### 3.4 ἀμετάθετος (G276) — Alpha-Privative Verbal Adjective

**Formation.** `ἀ-` (alpha-privative negator) + `μετά-θε-τος` (verbal-adjective suffix from μετατίθημι "transpose, change, transfer"). The pattern is standard Greek: α- + verbal stem + -τος = "un-X-able / un-X-ed" (cf. ἀδύνατος G102 "un-able", ἀκατάπαυστος "un-resting", ἀμίαντος "un-defiled"). Translation range: "unchangeable, not-to-be-transposed, immutable."

**NT inventory (di-legomenon).** From `greek_parser.py --lemma ἀμετάθετος`:

| Reference | Form | Parsing | Syntactic role |
|-----------|------|---------|----------------|
| **Heb 6:17** | **ἀμετάθετον** | **A-ASN (Acc Sg N)** | **Substantival** — "the immutability" (with τό) |
| **Heb 6:18** | **ἀμεταθέτων** | **A-GPN (Gen Pl N)** | **Attributive** — modifying πραγμάτων |

The adjective occurs **nowhere else in the NT**. Both occurrences sit inside the present passage, which is itself unusual — the author deploys the term twice in consecutive verses with **contrasting syntactic roles**:

- v.17: `τὸ ἀμετάθετον` — neuter singular **with article** → **substantival** ("the immutable thing / immutability"). Wallace 294–295: articular adjective → abstract quality or substantive. The genitive modifier `τῆς βουλῆς αὐτοῦ` specifies whose immutability.
- v.18: `δύο πραγμάτων ἀμεταθέτων` — neuter plural **anarthrous** → **attributive** ("two unchangeable things"). Adjective follows its head noun in agreement; no article means qualitative/indefinite.

**Grammatical inflection from v.17 singular → v.18 plural.** Same adjective, same root sense, but shifted from abstract singular quality ("the immutability [of his counsel]") to concrete plural entities ("two immutable things"). This number-shift is the syntactic mechanism linking v.17 (one immutable quality of God's βουλή) to v.18 (two immutable entities jointly providing παράκλησις). The lexical repetition is carrying the argument's logical weight.

**Related lexical family (for cross-reference):** μετατίθημι (G3346 "transpose/change/translate" — Acts 7:16; Gal 1:6; Heb 7:12; 11:5; Jude 4); μετάθεσις (G3331 "a change/removal/translation" — Heb 7:12; 11:5; 12:27).

---

## 4. Tense/Mood/Voice Inventory for Heb 6:13-18

**Indicatives (finite main-line):**

| Verse | Form | Parsing | Lemma |
|-------|------|---------|-------|
| 13 | εἶχεν | V-IAI-3S | ἔχω |
| 13 | ὤμοσεν | V-AAI-3S | ὀμνύω |
| 14 | εὐλογήσω | V-FAI-1S | εὐλογέω |
| 14 | πληθυνῶ | V-FAI-1S | πληθύνω |
| 15 | ἐπέτυχεν | V-2AAI-3S | ἐπιτυγχάνω |
| 16 | ὀμνύουσιν | V-PAI-3P | ὀμνύω |
| 17 | ἐμεσίτευσεν | V-AAI-3S | μεσιτεύω |

**Subjunctive (purpose):** v.18 ἔχωμεν (V-PAS-1P).

**Infinitives (5 total):**

| Verse | Form | Parsing | Function |
|-------|------|---------|----------|
| 13 | ὀμόσαι | V-AAN | complement of εἶχεν ("had…to swear") |
| 17 | ἐπιδεῖξαι | V-AAN | complement of βουλόμενος |
| 18 | ψεύσασθαι | V-ADN (aor. mid. dep.) | subject of impersonal ἀδύνατον |
| 18 | κρατῆσαι | V-AAN | telic/epexegetical to καταφυγόντες |

**Participles (7 total):**

| Verse | Form | Parsing | Function |
|-------|------|---------|----------|
| 13 | ἐπαγγειλάμενος | V-ADP-NSM (aor. mid.) | temporal frame — "when having promised" |
| 14 | λέγων | V-PAP-NSM | speech-introducing |
| 14 | εὐλογῶν | V-PAP-NSM | Heb.-calque inf.-abs. (cognate with finite εὐλογήσω) |
| 14 | πληθύνων | V-PAP-NSM | Heb.-calque inf.-abs. (cognate with finite πληθυνῶ) |
| 15 | μακροθυμήσας | V-AAP-NSM | antecedent temporal — "having long-endured" |
| 17 | βουλόμενος | V-PNP-NSM (pres. dep.) | circumstantial — "willing / purposing" |
| 18 | καταφυγόντες | V-2AAP-NPM | substantival — "the ones having fled for refuge" |
| 18 | προκειμένης | V-PNP-GSF (pres. dep.) | attributive — "set-before-us" (hope) |

**Voice distribution:** active dominant (15 forms); middle/deponent concentrated in specific lexemes (ἐπαγγέλλομαι, βούλομαι, ψεύδομαι, πρόκειμαι). No true passive forms in the pericope.

---

## 5. Intertextual Note (Gen 22:16-17 LXX)

v.14 (εἰ μὴν εὐλογῶν εὐλογήσω σε καὶ πληθύνων πληθυνῶ σε) is a direct citation of LXX Gen 22:17 with the oath-asseverative adjustment `εἰ μήν` (N1904; TR `ἦ μήν` — textual variant; see Metzger). The Genesis context is the Aqedah oath: LXX Gen 22:16 `Κατ' ἐμαυτοῦ ὤμοσα, λέγει Κύριος`. Three grammatical continuities link Heb 6:13-18 to Gen 22:16-17 LXX:

1. Reflexive-oath prepositional frame: Gen 22:16 `κατ' ἐμαυτοῦ` ~ Heb 6:13 `καθ' ἑαυτοῦ` (case-shift from 1s to 3s reflex.).
2. Aor.act.ind. of ὀμνύω: Gen 22:16 `ὤμοσα` (1s) ~ Heb 6:13 `ὤμοσεν` (3s).
3. Hebrew inf.-abs. calque preserved: Gen 22:17 `εὐλογῶν εὐλογήσω … πληθύνων πληθυνῶ` ~ Heb 6:14 (identical).

These continuities are grammatical facts, not interpretive claims; the parser shows them without adjudicating the typology.

---

## 6. Cross-References

**Grammar reference library:**
- [greek/aorist-infinitive-accusative-of-duration](../greek/aorist-infinitive-accusative-of-duration.md) — for the aor.inf. aspectual profile
- [greek/paired-middle-participles](../greek/paired-middle-participles.md) — related middle-voice / semantic-middle discussion
- [greek/participle-legon-discourse](../greek/participle-legon-discourse.md) — for v.14 λέγων
- [greek/divine-passive](../greek/divine-passive.md) — cf. ἀδύνατον + ψεύσασθαι impersonal skeleton

**Word studies (not all may exist yet — create as needed):**
- G276-ametathetos (this passage's anchor adjective)
- G3315-mesiteuo (NT hapax)
- G1925-epideiknumi (7× NT)
- G3660-omnuo (26× NT)
- G3727-horkos (4× NT)
- G1012-boule, G1860-epangelia, G1861-epangellomai, G2818-kleronomos
- G3114-makrothumeo, G2703-katapheugo, G4295-prokeimai, G1680-elpis, G3874-paraklesis
- G4229-pragma, G5574-pseudomai, G951-bebaiosis, G485-antilogia, G4009-peras

---

## 7. Data Source Notes

- Greek text: Nestle 1904 (via `greek_parser.py`, Text-Fabric N1904 dataset).
- KJV: `D:/bible/tools/data/kjv.txt`.
- All parsings verified by `greek_parser.py --verse "HEB 6:13"` through `--verse "HEB 6:18"`.
- Lemma inventories verified by `greek_parser.py --lemma` for ἀμετάθετος, μεσιτεύω, ἐπιδείκνυμι, ὀμνύω.
- Supplementary grammar research via `semantic_grammar.py --greek` queries on articular infinitive, middle-voice mediation, and divine oath syntax; top hits include Wallace (*Basics of NT Syntax* pp.187, 266, 425–427), BDF §§316, 337–338, 393, 408, and Machen ch. XXII on articular infinitive.
