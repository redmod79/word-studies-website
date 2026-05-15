# Aorist Passive Indicative (Greek)

## Definition

The aorist passive indicative reports a past event in which the grammatical subject is acted upon. Aspectually, the aorist presents the action perfectively — as a single, undivided whole viewed from the outside (external viewpoint), without comment on duration, repetition, or the state that follows. The indicative mood presents it as actual/historical (within the narrator's portrayal), and the passive voice foregrounds the subject as the recipient or patient of the action, while the agent may be named (ὑπό + gen.), implied, or deliberately suppressed.

1. **Simple/constative passive** — narrates a past event undergone by the subject, viewed as a whole
2. **Divine ("theological") passive** — agent suppressed; God (or a transcendent actor) understood as doer
3. **Permissive passive** — "was allowed to be X-ed"; the subject permits/submits to the action
4. **Deponent-looking passive** — passive form but active-like semantics (e.g., ἐφοβήθη "feared," ἐπορεύθη "went"); carried over from the middle in Koine
5. **Bounded-authorization passive** — with δίδωμι + inf. or acc. of duration, presents a past grant as a completed, bounded authorization (often narrated from a vantage after the span is set)

## Form Recognition

- Augment ἐ- prefixed to the stem (lost/contracted in compounds: e.g., ἀπ-εστάλη, παρ-εδόθη)
- Tense formative -θη- (first aorist passive) or bare -η- (second aorist passive, no -θ-)
- Secondary active endings: -ν, -ς, — (3S = -θη or -η), -μεν, -τε, -σαν
- Typical 3rd-sg shape: ἐ + stem + θη (ἐ-δό-θη, ἐ-θεραπεύ-θη, ἐ-πληρώ-θη); 3rd-pl: -θησαν or -ησαν
- **Parser search:** `tense=aorist mood=indicative voice=passive`
- **Morph code patterns:** `V-API-3S` (first aorist passive), `V-2API-3S` (second aorist passive, e.g., ἐτάφη, ἐφάνη), `V-AOI-3S` (aorist "deponent"/middle-passive form with active sense, e.g., ἐφοβήθη, ἐπορεύθη)

## Functions with Examples

### 1. Simple/Constative Passive — Past Event Undergone

Narrates a past event as a single whole; subject is patient; agent may be named or understood.

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Rev 13:3 | ἐθεραπεύθη | V-API-3S | "was healed" (the death-stroke) |
| Rev 13:3 | ἐθαυμάσθη | V-API-3S | "wondered" (whole earth "was caused to marvel") |
| Matt 2:3 | ἐταράχθη | V-API-3S | "he was troubled" |
| Matt 2:17 | ἐπληρώθη | V-API-3S | "was fulfilled" |
| Matt 8:13 | ἰάθη | V-API-3S | "was healed" |
| Matt 8:15 | ἠγέρθη | V-API-3S | "she arose" (was raised) |
| 1 Cor 15:4 | ἐτάφη | V-2API-3S | "he was buried" |

### 2. Divine ("Theological") Passive — Agent Suppressed, God Implied

Agent is omitted. In context (OT-citation formulas, covenantal or apocalyptic narration), God is the unnamed doer. Especially frequent with ἐρρέθη ("it was said"), ἐδόθη ("it was given"), παρεδόθη ("was delivered up"), ἠνεῴχθησαν ("were opened").

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Matt 5:21 | ἐρρέθη | V-API-3S | "it was said (by them of old)" |
| Matt 4:12 | παρεδόθη | V-API-3S | "(John) was cast into prison" |
| Matt 3:16 | ἠνεῴχθησαν | V-API-3P | "the heavens were opened" |
| Luke 1:26 | ἀπεστάλη | V-2API-3S | "the angel Gabriel was sent (by God)" |
| Matt 28:18 | Ἐδόθη | V-API-3S | "All power is given unto me" (by the Father) |

### 3. Permissive Passive — "Was Allowed To Be X-ed"

The subject permits/submits to the action; agent distinct from subject but action tolerated rather than resisted.

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Matt 1:19 | ἐβουλήθη | V-AOI-3S | "was minded (to put her away)" |
| 1 Cor 6:7 | ἀδικεῖσθε / ἀποστερεῖσθε (pres., cf. pattern) | — | "suffer yourselves to be defrauded" (pattern Wallace uses; same logic applies to aorist forms like ἐβαπτίσθη, ἐσυνεσταυρώθη) |

(Permissive force is read from context, not morphology alone; it is a pragmatic sub-category of the simple passive.)

### 4. "Deponent" Aorist Passive — Active Sense

Form is passive (-θη-/-η-), sense is active or middle. Koine has absorbed many verbs that classical Greek conjugated as middles into the -θη- aorist.

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Matt 1:19 | ἐβουλήθη | V-AOI-3S | "was minded" (willed, wanted) |
| Matt 2:9 | ἐπορεύθησαν | V-AOI-3P | "they departed" (went) |
| Matt 2:10 | ἐχάρησαν | V-2AOI-3P | "they rejoiced" |
| Matt 2:22 | ἐφοβήθη | V-AOI-3S | "he was afraid" |
| Matt 1:20 | ἐφάνη | V-2API-3S | "appeared (to him)" |

### 5. Bounded Authorization — ἐδόθη + Infinitive / Accusative of Duration

When δίδωμι governs an infinitive or accusative of extent, the aorist presents the grant as a completed, bounded authorization — the narrator summarizes a *delimited span* of permitted activity as a single package. The aorist's external viewpoint suits a retrospective or post-span vantage: the whole enabling act is in view, including its limits.

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Rev 13:5 | ἐδόθη αὐτῷ στόμα λαλοῦν μεγάλα | V-API-3S | "there was given unto him a mouth speaking great things" |
| Rev 13:5 | ἐδόθη αὐτῷ ἐξουσία ποιῆσαι μῆνας τεσσεράκοντα δύο | V-API-3S | "power was given unto him to continue forty and two months" |
| Rev 13:7 | ἐδόθη αὐτῷ ποιῆσαι πόλεμον μετὰ τῶν ἁγίων | V-API-3S | "it was given unto him to make war with the saints" |
| Rev 13:7 | ἐδόθη αὐτῷ ἐξουσία ἐπὶ πᾶσαν φυλὴν | V-API-3S | "power was given him over all kindreds" |

Note on Rev 13:5: the aorist ἐδόθη packages the entire forty-two-month allotment as one completed grant. The duration itself (μῆνας τεσσεράκοντα δύο as accusative of extent) is contained *within* the perfective viewpoint of ἐδόθη — the narrator stands at or after the issuance of the decree and reports the authorization in its totality, boundaries included. This is why English often renders such aorists with simple past + infinitive ("was given … to continue") rather than with a progressive.

## Contrast with Related Forms

| Form | Aspect | Typical Force | Example |
|------|--------|---------------|---------|
| **Aorist passive (V-API)** | Perfective — action as whole, external view | "X was done (to subject)" — past event, no comment on aftermath | Rev 13:3 ἐθεραπεύθη "was healed" |
| **Imperfect passive (V-IPI)** | Imperfective — internal view, in progress / iterative | "was being done," "kept being done" | Mark 9:31 παραδίδοται-pattern; Matt 3:6 ἐβαπτίζοντο "were being baptized" |
| **Perfect passive (V-RPI/RPP)** | Stative — completed past action with enduring present result | "has been done (and stands done)" | Rev 13:8 γέγραπται "has been written (and still stands written)"; Rev 13:8 ἐσφαγμένου (participle) "having been slain (and abiding in slain-state)" |
| **Present passive (V-PPI)** | Imperfective — ongoing/general | "is (being) done" | various |

**Illustrative contrast in Rev 13 itself:**

| Verse | Form | Parsing | Viewpoint |
|-------|------|---------|-----------|
| Rev 13:3 | ἐσφαγμένην | V-RPP-ASF (perfect pass. ptcp.) | enduring slain-state |
| Rev 13:3 | ἐθεραπεύθη | V-API-3S (aorist pass. ind.) | healing as a whole past event |
| Rev 13:5 | ἐδόθη | V-API-3S (aorist pass. ind.) | bounded grant, complete |
| Rev 13:8 | γέγραπται | V-RPI-3S (perfect pass. ind.) | written and remains written |

The aorist ≠ perfect: ἐθεραπεύθη does not by itself assert a lasting cure-state (that would be τεθεράπευται); it reports the healing *event*. Any continuing condition is inferred from context.

## Classical vs. Koine Usage

- **Classical Greek** maintained a sharper distinction between middle (-μην, -σο, -το … aorist in -σάμην) and passive (-θη-) voices. Many verbs had only a middle aorist with both reflexive and passive senses.
- **Koine** generalized the -θη- aorist. Many verbs classical authors conjugated as middle now appear with -θη- forms but active/reflexive meaning (the "deponent" or "active-sense passive" pattern in Function 4). This is why ἐφοβήθη, ἐπορεύθη, ἐβουλήθη, ἐχάρη look passive but translate actively.
- BDF §§76–78, 307–313 track the Koine drift from middle to -θη-; §§318–322 treat the aorist indicative specifically, including the ingressive, constative, and effective ("culminative") uses, all compatible with the passive voice.
- Wallace (*Greek Grammar Beyond the Basics* 554–565) organizes the passive semantically: (1) simple passive, (2) passive with stated agent ὑπό + gen., (3) passive with intermediate agent διά + gen., (4) passive with impersonal means (dat. of means or ἐν), (5) suppressed/divine passive, (6) permissive passive, (7) "reflexive" passive. Items 5–7 are the interpretive judgments applied to otherwise simple-looking ἐ-...-θη forms.

## Passive Voice — Semantic Nuances

- **Stated agent:** ὑπό + genitive (e.g., "by him"). Less than 1 in 8 NT passives names the agent (Wallace 431–438).
- **Suppressed agent / divine passive:** the absence of ὑπό-phrase is normal; context decides whether God, humans, or impersonal forces are in view. In apocalyptic Koine (Revelation especially), chains of agentless ἐδόθη draw attention away from the immediate giver and toward the unnamed ultimate authorizer.
- **Permissive:** best candidates are reflexive-capable verbs (βαπτίζω, ἀδικέω, ἀποστερέω, παραδίδωμι when subject-willed). Requires contextual warrant.
- **Reflexive passive:** subject acts on self (e.g., ἐβαπτίσθησαν "got themselves baptized"); overlaps with middle semantics and with Koine -θη- deponents.
- **Impersonal means** (not an agent): dative of means, ἐν + dative; these do not bear moral responsibility.

## Notes on Usage

- *Augment restriction:* the ἐ- augment appears only in the indicative. The aorist passive subjunctive, optative, imperative, infinitive, and participle drop it (βαπτισθῇ, βαπτισθείς, βαπτισθῆναι). V-API always carries the augment.
- *Two formations:* "first" aorist passive in -θη- is default; "second" aorist passive in -η- (no -θ-) is lexically restricted (ἐγράφη, ἐφάνη, ἐτάφη, ἐχάρη, ἐστράφη) and is morphologically identical in function.
- *"V-AOI" vs. "V-API" in parser output:* both code aorist passive indicative; V-AOI is used where the lexeme is conventionally "deponent" (middle/passive form, active sense, no true active form in use).
- *Textual/form note (Rev 13:8):* Rev 13:8 does not contain an aorist passive indicative of προσκυνέω in the critical text used by this parser. The main verb is **προσκυνήσουσιν** (G4352, V-FAI-3P, *future active indicative*) — "they shall worship." A form προσεκυνήσθησαν is not attested in NA28/SBLGNT here. The aorist-passive examples elsewhere in Rev 13 (ἐθεραπεύθη, ἐθαυμάσθη, ἐδόθη, ἐδόθη, ἐδόθη) are the genuine V-API instances in the chapter.
- *Bounded-grant logic is pragmatic, not purely morphological:* the aorist does not *mark* "bounded authorization" grammatically. The reading arises from (a) perfective aspect + (b) a complement of extent (accusative of time, purpose infinitive) + (c) narrative vantage. Other aorists without such complements do not carry this nuance.

## References

- Wallace, *Greek Grammar Beyond the Basics*, 554–565 (aorist passive and voice semantics); 431–441 (agent expressions); 555–557 (divine/theological passive); 427–428 (permissive).
- BDF §§318–322 (aorist indicative functions: constative, ingressive, effective); §§76–78, 307–313 (passive morphology and Koine -θη- generalization).
- Robertson, *A Grammar of the Greek New Testament in the Light of Historical Research*, 815–836 (aorist indicative); 817 (constative/summary); 820 (effective/culminative).

---
*Generated from: greek_parser.py (--verse, --search tense=aorist mood=indicative voice=passive); semantic_grammar.py (--greek "aorist passive indicative", "divine passive aorist")*
*Last updated: 2026-04-17*
