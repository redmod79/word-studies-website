# Reflexive-Object + ὅτι-Clause Display Construction (Greek)

## Definition

A Greek syntactic pattern in which a verb of showing, claiming, or presenting takes a **reflexive pronoun** (ἑαυτόν / σεαυτόν) as its direct object, with the **content of the display or claim** expressed either by a ὅτι-clause, an infinitive clause, or a predicate accusative. The paradigm text is 2 Thessalonians 2:4:

> ἀποδεικνύντα ἑαυτὸν ὅτι ἐστὶν Θεός
> "displaying himself (as the one) that he is God"

The structure has three slots:

1. **Display verb** — ἀποδείκνυμι, δείκνυμι, ἐπιδείκνυμι, φαίνω, ὁμολογέω, ποιέω (with a "make-out-to-be" sense), λέγω (with εἶναι)
2. **Reflexive accusative** — ἑαυτόν, σεαυτόν, ἐμαυτόν (object put on display by the subject)
3. **Content expression** — ὅτι + finite clause, or accusative + infinitive, or bare predicate accusative

**Critical semantic note:** The construction reports *what is claimed or displayed*, not *what is the case*. A verb like ἀποδείκνυμι here denotes the public act of proof-exhibition; it does **not** validate the truth of the exhibited proposition. "He displays himself as X" is fully compatible with "he is not in fact X."

## Form Recognition

Look for this cluster of morph tags in proximity:

- **Display verb**: often V-PAP-ASM / V-PAI-3S / V-AAI-3S (ἀποδείκνυμι G584, δείκνυμι G1166, ποιέω G4160, λέγω G3004)
- **Reflexive pronoun**: F-3ASM ἑαυτόν, F-2ASM σεαυτόν, F-1ASM ἐμαυτόν, F-3APM ἑαυτούς (Strong's G1438 / G4572 / G1683)
- **Content marker**: either CONJ ὅτι (G3754), or V-PAN εἶναι + acc. complement, or a bare predicate accusative (N-ASM)

**Parser search patterns:**
- `greek_parser.py --lemma ἀποδείκνυμι` / `--lemma δείκνυμι` / `--lemma ἐπιδείκνυμι`
- Scan the verse hits for adjacent F-3ASM / F-2ASM reflexive + ὅτι or εἶναι

## The Paradigm: 2 Thessalonians 2:4

| Word | Lemma | Strong's | Parsing | Slot |
|------|-------|----------|---------|------|
| ἀποδεικνύντα | ἀποδείκνυμι | G584 | V-PAP-ASM | display verb (Pres Act Ptcp) |
| ἑαυτὸν | ἑαυτοῦ | G1438 | F-3ASM | reflexive object |
| ὅτι | ὅτι | G3754 | CONJ | content-clause marker |
| ἔστιν | εἰμί | G1510 | V-PAI-3S | copula of content |
| Θεός | θεός | G2316 | N-NSM | predicate nominative of content |

The participle ἀποδεικνύντα agrees with the accusative subject αὐτόν of the preceding ὥστε-clause. The reflexive ἑαυτόν is its direct object. The ὅτι-clause unpacks the *content* of the display. KJV glosses the whole "shewing himself that he is God"; most modern versions render the ὅτι-clause as a predicate expansion: "proclaiming himself to be God" (ESV), "declaring himself to be God" (NASB).

## Variations of the Construction

### 1. Display verb + reflexive + ὅτι-clause (direct content)

| Reference | Greek | Construction |
|-----------|-------|--------------|
| 2 Thess 2:4 | ἀποδεικνύντα ἑαυτὸν ὅτι ἐστὶν Θεός | ἀποδείκνυμι + ἑαυτόν + ὅτι |
| John 19:7* | ὅτι Υἱὸν Θεοῦ ἑαυτὸν ἐποίησεν | ποιέω + ἑαυτόν + predicate acc. (the ὅτι here is causal, not content) |

*John 19:7 is a near-variant: the ὅτι is causal ("because he made himself Son of God"), but the internal clause itself uses the same reflexive + predicate-accusative display pattern (see §3 below).

### 2. Verb of saying + acc.-inf. with reflexive subject

| Reference | Greek | Construction |
|-----------|-------|--------------|
| Acts 5:36 | λέγων εἶναί τινα ἑαυτόν | λέγω + ἑαυτόν + εἶναι + pred. acc. |
| Acts 8:9 | λέγων εἶναί τινα ἑαυτὸν μέγαν | λέγω + ἑαυτόν + εἶναι + pred. acc. |
| Rev 2:9 | τῶν λεγόντων Ἰουδαίους εἶναι ἑαυτούς | λέγω + ἑαυτούς + εἶναι + pred. acc. |
| Rev 3:9 | τῶν λεγόντων ἑαυτοὺς Ἰουδαίους εἶναι | λέγω + ἑαυτούς + pred. acc. + εἶναι |

Both Rev 2:9 and Rev 3:9 explicitly append καὶ οὐκ εἰσίν ("and they are not") — the narrator's own correction that confirms the claim-vs-reality gap inherent to the construction.

### 3. ποιέω + reflexive + predicate accusative ("make oneself out to be X")

| Reference | Greek | KJV |
|-----------|-------|-----|
| John 8:53 | τίνα σεαυτὸν ποιεῖς; | "whom makest thou thyself?" |
| John 10:33 | ποιεῖς σεαυτὸν Θεόν | "makest thyself God" |
| John 19:7 | Υἱὸν Θεοῦ ἑαυτὸν ἐποίησεν | "he made himself the Son of God" |

This idiom is distinctly Johannine in the NT for the charge of self-exaltation. The verb ποιέω here has the sense "claim, present, set forth as" (BDAG ποιέω §2.h).

### 4. Reflexive + voice-based display (middle/passive participle)

| Reference | Greek | Parsing | Sense |
|-----------|-------|---------|-------|
| 2 Cor 11:13 | μετασχηματιζόμενοι εἰς ἀποστόλους Χριστοῦ | V-PMP-NPM | "transforming themselves into" (middle reflexive-force) |

Here the reflexive is built into the middle voice rather than expressed as a separate pronoun; the construction is functionally parallel (self-presentation as X).

## Grammatical Analysis

### Why ὅτι and not an infinitive?

Classical and Koine Greek offer two standard options for reporting the content of a cognitive or declarative verb:
- **Accusative + infinitive** — the older, more formal pattern
- **ὅτι-clause** — the later, more explicit pattern that gained ground in Hellenistic Greek (BDF §§396–397)

2 Thess 2:4 chooses ὅτι. BDF §397(2) notes that ὅτι-clauses after verbs of demonstrating, showing, and declaring are an expansion of the older indirect-discourse pattern into Koine prose. The ὅτι-clause here is **epexegetical** to the reflexive ἑαυτόν: it specifies the content of what is being displayed about himself. Wallace (*GGBB* 458–459) classifies such ὅτι-clauses as "direct object" or "content" clauses.

### Why the reflexive pronoun?

The reflexive accusative ἑαυτόν ensures that the display's object and the display's subject are the same referent — the subject exhibits **himself**, not a third party (Wallace 350–361 on reflexive pronouns; BDF §283). Without the reflexive, ἀποδεικνύντα αὐτόν could suggest another antecedent. With ἑαυτόν the self-directedness of the act is lexically guaranteed.

### Claim vs. reality

The construction is semantically neutral on the truth-value of the content clause. Three NT texts make this explicit by *refuting* the claim within the same sentence:

- **Rev 2:9**: λεγόντων Ἰουδαίους εἶναι ἑαυτούς, **καὶ οὐκ εἰσίν**
- **Rev 3:9**: λεγόντων ἑαυτοὺς Ἰουδαίους εἶναι, **καὶ οὐκ εἰσὶν ἀλλὰ ψεύδονται**
- **2 Cor 11:13**: the pseudo-apostles transform themselves into (μετασχηματιζόμενοι εἰς) apostles of Christ — the label ψευδαπόστολοι in the same verse overturns the claim.

The grammar, therefore, asserts a **public presentation** and leaves open whether the content is veridical. A construction of the form "X displays/declares himself that he is Y" can stand alongside "X is not in fact Y" without contradiction.

## Contrast with Related Constructions

| Construction | What it asserts | Example |
|--------------|-----------------|---------|
| Reflexive-object + ὅτι-clause display | X publicly *presents* himself as Y (truth-neutral) | 2 Thess 2:4 |
| Perfect passive of ἀποδείκνυμι + ἀπό + agent | X *has been* demonstrated by Y (result-state, agent-attested) | Acts 2:22 (Ἰησοῦν … ἀποδεδειγμένον ἀπὸ τοῦ Θεοῦ) |
| Copular predication εἰμί + nom. | X *is* Y (assertion of state) | John 1:1 (Θεὸς ἦν ὁ λόγος) |
| Indirect discourse with λέγω + ὅτι | X *says* that … (report of speech) | John 4:35 |

Acts 2:22 is a particularly instructive contrast: the same verb ἀποδείκνυμι appears as a perfect passive participle with ἀπὸ τοῦ Θεοῦ specifying divine agency — i.e., the attestation is *ratified by God*. In 2 Thess 2:4 there is no corresponding agent phrase; the subject is his own attestor, and the "proof" is self-issued.

## Parallel Verbs in the Display Field

Tool-verified NT occurrences (from `greek_parser.py --lemma`):

| Lemma | Strong's | Gloss | NT count | Notable forms |
|-------|----------|-------|----------|---------------|
| ἀποδείκνυμι | G584 | "show forth, demonstrate, exhibit" | 4 | V-PAP-ASM (2 Thess 2:4); V-RPP-ASM (Acts 2:22) |
| δείκνυμι | G1166 | "show, point out" | 33 | V-AAM-2S δεῖξον common (Matt 8:4; Luke 5:14) |
| ἐπιδείκνυμι | G1925 | "exhibit, display to someone" | 7 | V-PAP-NSM ἐπιδεικνύς (Acts 18:28) |
| φαίνω | G5316 | "shine, appear, be seen as" | 31 | V-PEI-3S φαίνεται (Matt 2:13); V-PPI-2P φαίνεσθε (Matt 23:28) |
| ὁμολογέω | G3670 | "confess, acknowledge, profess" | 26 | V-AAI-3S ὡμολόγησεν (Matt 14:7; John 1:20) |
| ποιέω (idiomatic) | G4160 | "make out to be, claim" | | V-PAI-2S ποιεῖς σεαυτόν (John 8:53; 10:33) |

Each of these verbs can host a reflexive accusative and a content expression (ὅτι, εἶναι-inf., or predicate accusative), forming the same family of self-display constructions.

## References

- **Wallace, *Greek Grammar Beyond the Basics*** 350–361 — reflexive pronouns; direct, intensive, and possessive uses of ἑαυτοῦ / σεαυτοῦ / ἐμαυτοῦ
- **BDF §283** — reflexive pronoun ἑαυτοῦ and its syntactic functions
- **BDF §396–397** — ὅτι-clauses after verbs of declaration, showing, demonstrating; competition with accusative-plus-infinitive

---
*Generated from: greek_parser.py (--verse, --lemma); cross-checked against BDAG entries for ἀποδείκνυμι, ποιέω, λέγω*
*Last updated: 2026-04-17*
