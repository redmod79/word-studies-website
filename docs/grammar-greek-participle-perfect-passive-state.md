# Greek Perfect Passive Participle (V-RPP)

## Definition

The Greek perfect passive participle describes a **state or condition** existing at the time of the reference verb, which resulted from a **prior completed action** done **to** the subject. Unlike the aorist (which summarizes a past event) or the present (ongoing action), the perfect foregrounds the **abiding resultant state**. The passive voice marks the subject as the recipient/patient of the action. Combined, V-RPP forms say: "having been X-ed (and so now standing in the state of having-been-X-ed)."

1. **Resultant-state (primary)** — past action whose effect persists at reference time
2. **Verbal-adjectival (attributive/substantival)** — functions as an adjective describing an enduring quality
3. **Circumstantial/predicative** — modifies the main verb by supplying a background state

## Aspect Theory

Grammarians differ on what "perfect" semantically encodes:

- **Fanning (*Verbal Aspect in NT Greek*, ch. 7)** — perfect = **stative aspect** combined with past action; "a present state resulting from a past action." The perfect passive participle is the purest grammatical expression of this combination.
- **Wallace (*GGBB* pp. 619–635)** — perfect participle typically indicates action antecedent to the main verb with resultant state contemporaneous with it; "intensive" / "consummative" perfects.
- **Porter (*Verbal Aspect*)** — treats perfect as **stative aspect** without committing to past-time reference; the form presents the subject as existing in a given state.
- **Campbell (*Verbal Aspect and Non-Indicative Verbs*)** — perfect as **imperfective + heightened proximity**; state-focused rather than action-focused.

Points of agreement across the schools: the perfect describes **STATE, not sequence**. The referent is being viewed *as currently bearing the condition*, not as *currently undergoing the action*.

See also: BDF §340–342 on the perfect participle's stative force and its use in periphrastic constructions.

## Form Recognition

- **Reduplication** of the initial consonant with ε (e.g., λύω → λελυμένος; γράφω → γεγραμμένος; σφάζω → ἐσφαγμένος — reduplication appears as ε- before σφ-)
- **Middle/passive morpheme** `-μεν-` attached to the verb stem
- **Adjectival endings** for gender/number/case (-ος/-η/-ον etc.)
- **Parser search:** `tense=perfect voice=passive mood=participle`
- **Morph code pattern:** `V-RPP-{CASE}{NUM}{GEN}` — e.g., `V-RPP-ASN` = perf pass ptcp, accusative singular neuter
- Second perfects tagged `V-2RPP-*` (e.g., ἐσπαρμένον at Matt 13:19 — σπείρω)

## Functions with Examples

### 1. Attributive — the state qualifies a noun

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Matt 5:32 | ἀπολελυμένην | V-RPP-ASF | "[her that is] divorced" (a put-away woman) |
| Matt 7:14 | τεθλιμμένη | V-RPP-NSF | "narrow [lit. having-been-compressed]" |
| Matt 13:44 | κεκρυμμένῳ | V-RPP-DSM | "hid [in the field]" |

The participle ascribes an enduring condition to the noun it modifies.

### 2. Predicative / Periphrastic — linked with εἰμί to form a compound tense

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| John 19:19 | ἦν … γεγραμμένον | V-RPP-NSN | "the writing was" (lit. "was having-been-written") |
| 2 Cor 3:2 | ἐνγεγραμμένη | V-RPP-NSF | "[ye are our epistle] written [in our hearts]" |
| Matt 10:26 | κεκαλυμμένον | V-RPP-NSN | "covered [that shall not be revealed]" |

Periphrastic perfects (εἰμί + perf. ptcp.) are the classic construction for "standing-as-having-been-done" — a state on display.

### 3. Circumstantial / Appositional — adds a background state to the main clause

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Matt 9:2 | βεβλημένον | V-RPP-ASM | "lying [on a bed]" (having-been-laid) |
| Matt 9:36 | ἐρριμμένοι | V-RPP-NPM | "scattered abroad" (having-been-thrown-down) |
| Matt 11:28 | πεφορτισμένοι | V-RPP-NPM | "heavy laden" (having-been-burdened) |

The main verb proceeds, while the participle gives the standing condition of the subject.

### 4. The Central Example Pair — σφάζω (G4969) in Revelation

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Rev 5:6 | Ἀρνίον … ὡς ἐσφαγμένον | V-RPP-ASN | "a Lamb as it had been slain" |
| Rev 13:3 | μίαν ἐκ τῶν κεφαλῶν … ὡς ἐσφαγμένην | V-RPP-ASF | "one of his heads as it were wounded to death" |

Same verb (σφάζω, "slaughter"), same tense/voice/mood (perfect passive participle), same marker (ὡς, "as"), and the same grammatical logic:

- **Rev 5:6** — the Lamb stands (ἑστηκὸς, V-RAP-ASN) yet bears the abiding state of **having been slain**. The slaying is past and complete; the state of slain-ness endures on a living, active figure. The perfect does not say "was recently killed" or "is being killed now" — it says "**carries the condition of one slain**."
- **Rev 13:3** — one head of the beast bears the abiding state of **having been slaughtered to death** (ἐσφαγμένην εἰς θάνατον), yet the death-wound is healed (ἐθεραπεύθη, aorist passive). Again the perfect marks not the moment of wounding, but the **visible, lasting condition** of mortal-woundedness worn by the beast.

The gender shift (ASN → ASF) simply agrees with the noun each participle modifies (Ἀρνίον neuter; κεφαλή feminine). The aspectual force is identical.

Grammarians who note the Rev 5:6 / Rev 13:3 symmetry often read the parallel as **deliberate ironic mirroring**: the wounded Lamb of God (life-giving death, redemption) vs. the wounded head of the beast (counterfeit resurrection, imitation of the slain-yet-living motif). The grammar itself does not establish this reading; it only establishes that John has used the **same stative construction** for both figures.

## Contrast with Related Forms

| Form | Aspect / Function | Example |
|------|-------------------|---------|
| Perfect passive ptcp. (V-RPP) | **State** resulting from prior action, subject as patient | Rev 5:6 ἐσφαγμένον |
| Aorist passive ptcp. (V-APP) | **Event** (past action viewed whole), no focus on resulting state | Rev 13:8 ἐσφαγμένου *[variant readings]* vs. aorist options |
| Present passive ptcp. (V-PPP) | **Ongoing** action being done to the subject | 2 Cor 3:2 γινωσκομένη "being known" |
| Perfect active ptcp. (V-RAP) | State resulting from prior action, subject as agent | Rev 5:6 ἑστηκὸς "standing" (having taken one's stand) |

The pairing in Rev 5:6 — ἑστηκὸς (V-RAP) "having taken its stand / standing" + ἐσφαγμένον (V-RPP) "having been slain" — stacks two perfects, each contributing its own resultant state to the same figure.

## Subtypes (syntactic uses of the participle)

| Subtype | Description | Example | Reference |
|---------|-------------|---------|-----------|
| Attributive | Modifies a noun (often with article) | ἀπολελυμένην | Matt 5:32 |
| Substantival | Functions as a noun | πεφορτισμένοι (the burdened ones) | Matt 11:28 |
| Predicative | Completes εἰμί (periphrastic perfect) | ἦν … γεγραμμένον | John 19:19 |
| Circumstantial | Background state to main verb | βεβλημένον | Matt 9:2 |
| Comparative with ὡς | State presented as apparent / characterizing | ἐσφαγμένον / ἐσφαγμένην | Rev 5:6; Rev 13:3 |

---

*Sources consulted: Wallace, *Greek Grammar Beyond the Basics*, pp. 619–635; BDF §340–342; Fanning, *Verbal Aspect in NT Greek*, ch. 7; Porter, *Verbal Aspect*; Campbell, *Verbal Aspect and Non-Indicative Verbs*.*
*Examples generated from: `greek_parser.py` (`--search tense=perfect voice=passive mood=participle`, `--verse`); concept search via `semantic_grammar.py "perfect passive participle" --greek`.*
*Last updated: 2026-04-17*
