# Greek Grammatical Concord Shift — Neuter to Masculine

**Type:** Agreement / syntax
**Key text:** 2 Thessalonians 2:6–7 (τὸ κατέχον → ὁ κατέχων)
**Primary references:** Wallace, *Basics of NT Syntax* 331–345 (agreement); BDF §§132–137 (agreement, constructio ad sensum); Wallace 269–270 (participle agreement in gender/number/case).

---

## 1. The Default Rule: Concord in Gender, Number, Case

A Greek participle is a **verbal adjective**. From its verbal nature it has tense and voice; from its adjectival nature it has **gender, number, and case** (Wallace 269). The participle therefore agrees with its head noun (or implied referent) in all three categories, exactly as an ordinary adjective does.

BDF §132–134 frame this under the general heading of **agreement (Kongruenz)**: the governed word is normally drawn into the gender/number of the governing substantive. Deviations from strict grammatical concord fall into two broad families:

1. **Grammatical concord (constructio ad formam)** — agreement with the morphological gender/number of the head noun.
2. **Sense concord (constructio ad sensum, κατὰ σύνεσιν)** — agreement with the *logical* referent rather than the grammatical form (BDF §134). Classic examples: a neuter collective noun (τὸ πλῆθος, τὰ ἔθνη, τὸ παιδίον) taking a masculine/feminine plural verb or pronoun because the referent is a group of persons.

Greek writers routinely exploit the gap between these two modes.

---

## 2. What a Deliberate Gender Shift Signals

When a writer uses **two different genders for what appears to be the same referent** within adjacent clauses, interpreters have two main options:

**(a) Two different referents.** The shift marks a change of subject — the neuter term and the masculine term denote distinct entities.

**(b) One referent viewed from two perspectives.** The shift is rhetorical/conceptual:

- **Abstract / institutional (neuter) → personal / individual (masculine).** An office, principle, power, or corporate entity is first named in its abstract aspect, then personalized in its agent or representative.
- **Collective (neuter plural or neuter singular of a class) → personal (masculine).** A group or force is first described as a "thing," then as "the one" who acts.

BDF §134(1b) explicitly notes that shifts from grammatical to sense-concord often occur "when the idea of persons supersedes that of things." Wallace 331–345 treats noun–pronoun, noun–adjective, and subject–verb agreement, and gives multiple cases where personification or individuation drives a masculine form after a neuter antecedent.

**Important:** the grammar alone cannot decide which of (a) or (b) applies, nor *which* referent is in view if (b) holds. The form flags the shift; context supplies the identification.

---

## 3. The Form in 2 Thessalonians 2:6–7

Parser output (`greek_parser.py --verse "2TH 2:6"` / `"2TH 2:7"`):

**v.6:** καὶ νῦν **τὸ κατέχον** οἴδατε, εἰς τὸ ἀποκαλυφθῆναι αὐτὸν ἐν τῷ αὐτοῦ καιρῷ.
- κατέχον — κατέχω, V-PAP-ASN, **Pres Act Ptcp Acc Sg Neuter** (articular, functioning as substantive: "the restraining [thing]").

**v.7:** τὸ γὰρ μυστήριον ἤδη ἐνεργεῖται τῆς ἀνομίας· μόνον **ὁ κατέχων** ἄρτι ἕως ἐκ μέσου γένηται.
- κατέχων — κατέχω, V-PAP-NSM, **Pres Act Ptcp Nom Sg Masculine** (articular substantival: "the restraining [one]").

Same lemma, same tense (present), same voice (active), same aspect. **Only gender and case change.** The case change (ASN → NSM) is syntactic (object of οἴδατε → subject of an elided verb); the **gender change** (neuter → masculine) is the feature under study.

### Candidate Referents in the Literature

The list below is **context-neutral**: it catalogs the identifications proposed for the restrainer, each with the grammatical logic the proposal depends on. It does not adjudicate.

| # | Proposed Referent | Neuter (v.6) encodes | Masculine (v.7) encodes |
|---|-------------------|----------------------|--------------------------|
| 1 | **Holy Spirit** | πνεῦμα (neuter) — the Spirit in abstract/nominal form | the Spirit **as Person** (parallel to John 14:26; 16:13, where neuter τὸ πνεῦμα governs masculine ἐκεῖνος) |
| 2 | **Roman Empire / Roman Emperor** | *imperium* / τὸ κράτος / the state as institution (neuter) | the Emperor (masculine) as the institution's embodied head |
| 3 | **Angelic restrainer (Michael)** | the angelic *restraining power* / office (neuter, impersonal) | Michael as personal prince (cf. Dan 10:13, 21; 12:1 — ὁ ἄρχων ὁ μέγας) |
| 4 | **Gospel preaching / the preacher** | τὸ εὐαγγέλιον or τὸ κήρυγμα (neuter) — the proclamation as abstract message | the preacher — Paul himself, or Christ, or the church's herald (masculine) |
| 5 | **God's sovereign restraint / God as Person** | divine restraining purpose/power (neuter, abstract) | God as personal Restrainer (masculine) |
| 6 | **Self-restraint of the man of lawlessness** | the condition/fact of being held back (neuter, stative) | the man himself as the one held back until his own ἀποκάλυψις (masculine) |

Each proposal treats v.6/v.7 under mechanism (b) from §2 — same referent, abstract→personal — except view 6, which can be read as (a) (two referents: a neuter holding-force vs. a masculine held-back one) or as (b) with the lawless one himself viewed from two aspects.

The parser confirms a third possible feature of the passage: **αὐτὸν** in v.6 ("that *he* be revealed") is **P-ASM (Acc Sg Masculine)** — masculine already, referring ahead to the ἄνθρωπος τῆς ἀνομίας (v.3). So the pericope is already carrying masculine reference for the lawless one before v.7. This is a further datum any identification must accommodate.

---

## 4. Biblical Parallels Where Concord Shifts for Rhetorical Effect

These are tool-verified parallels (parser output for each). They show that neuter→masculine (or neuter→masculine-pronominal) shifts are a recognized Greek idiom, not a solecism.

### (a) John 14:26 — Paraclete/Spirit

Parser: `greek_parser.py --verse "JHN 14:26"`

> ὁ δὲ **Παράκλητος** [N-NSM], τὸ **Πνεῦμα** τὸ Ἅγιον [N-NSN] … **ἐκεῖνος** [D-NSM] ὑμᾶς διδάξει πάντα

Here the Spirit is named by a masculine noun (παράκλητος) appositively aligned with a neuter noun (πνεῦμα), and the subsequent demonstrative **ἐκεῖνος** is **masculine**, not the neuter ἐκεῖνο that strict concord with the nearest antecedent τὸ πνεῦμα would require. Sense-concord with the personal παράκλητος (and, many argue, with the Spirit-as-Person) drives the masculine.

### (b) John 16:13 — Spirit of Truth

Parser: `greek_parser.py --verse "JHN 16:13"`

> ὅταν δὲ ἔλθῃ **ἐκεῖνος** [D-NSM], τὸ **Πνεῦμα** τῆς ἀληθείας [N-NSN], ὁδηγήσει ὑμᾶς…

Masculine demonstrative precedes the neuter appositional clarification. The same idiom.

### (c) Revelation 17:16 — Ten Horns and Beast

Parser: `greek_parser.py --verse "REV 17:16"`

> καὶ τὰ δέκα **κέρατα** [N-NPN] ἃ εἶδες καὶ τὸ **θηρίον** [N-NSN], **οὗτοι** [D-NPM] μισήσουσιν τὴν πόρνην…

Two neuter subjects (horns, beast) — both grammatically impersonal — govern a **masculine plural** demonstrative οὗτοι. Constructio ad sensum: the horns and beast symbolize *persons* (kings, v.12), and John slides to masculine once personal agency (hating, burning, devouring) is predicated of them.

### (d) Collective nouns with sense-plurals

BDF §134 catalogues examples like τὸ πλῆθος (neuter) + plural verb/participle; τὰ ἔθνη (neuter) + masculine participle; ὁ ὄχλος (masculine) + plural verb. These are the same phenomenon in its commonest form: the abstract/collective form yields to the personal/plural sense.

---

## 5. How to Recognize the Pattern

Look for **all** of the following together:

1. **Same lemma or synonymous referent** appearing twice in close context.
2. **Gender shift** between the two occurrences — typically neuter → masculine or neuter → feminine when the referent is clearly a person or personal collective.
3. **No new grammatical head noun** introduced that would force the new gender mechanically.
4. **Rhetorical payoff** — personification, individuation, or the surfacing of a named agent.

If (1)–(3) are present but (4) is ambiguous, the passage is a candidate for the "two different referents" reading (mechanism a in §2).

---

## 6. What the Grammar Alone Does NOT Decide

- Which entity is the restrainer of 2 Thess 2:6–7.
- Whether mechanism (a) (two referents) or (b) (one referent, two aspects) obtains.
- Whether the masculine participle ὁ κατέχων is personal-individual (one man) or personal-collective (a personal institution).

These determinations belong to exegesis of the passage and its canonical/historical frame, not to the grammar reference.

---

## References

- Wallace, Daniel B. *The Basics of New Testament Syntax* (Zondervan, 2000), pp. 269–270 (participle as verbal adjective, agreement); pp. 331–345 (agreement: subject–verb, pronoun–antecedent, including constructio ad sensum).
- Blass, F., and A. Debrunner. *A Greek Grammar of the New Testament*, trans. R. W. Funk. §§132–137 (agreement, including §134 constructio ad sensum).
- Parser source: `D:/bible/tools/greek/greek_parser.py --verse "2TH 2:6"` / `"2TH 2:7"` / `"JHN 14:26"` / `"JHN 16:13"` / `"REV 17:16"`.
- Semantic grammar search: `D:/bible/tools/search/semantic_grammar.py "gender agreement participle" --greek` and `"agreement with sense meaning neuter masculine" --greek`.
