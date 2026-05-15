# Aorist Active Indicative Narrative Chain (Greek)

## Definition

An aorist active indicative narrative chain is a sequence of finite aorist active indicative verbs, often linked by καί, that advances a narrative through bounded actions. The aorist indicative presents each action as a whole event; the active voice keeps the grammatical subject as the doer of each event; the repeated finite forms create the event-line.

1. **Sequential event-line** - each finite aorist advances the narrative by one bounded action.
2. **Coordinated action cluster** - καί links multiple verbs under the same discourse subject or tightly connected subjects.
3. **Perfective summary** - the chain reports what happened without marking internal duration.

## Form Recognition

- Finite verb with aorist tense, active voice, indicative mood.
- Morph codes commonly include `V-AAI-3S`, `V-2AAI-3S`, `V-AAI-1S`, `V-2AAI-1S`.
- Repeated verbs may be joined by καί: `καὶ + V-AAI` / `καὶ + V-2AAI`.
- **Parser search:** `tense=aorist voice=active mood=indicative`
- **Pattern searches:** `CONJ V-AAI-3S CONJ V-AAI-3S`; `V-AAI-3S CONJ V-AAI-3S CONJ V-AAI-3S`

## Functions with Examples

### 1. Mainline Narrative Sequence

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Luke 6:48 | ἔσκαψεν καὶ ἐβάθυνεν καὶ ἔθηκεν | V-AAI-3S + CONJ + V-AAI-3S + CONJ + V-AAI-3S | "digged deep, and laid the foundation" |
| John 20:8 | εἶδεν καὶ ἐπίστευσεν | V-2AAI-3S + CONJ + V-AAI-3S | "he saw, and believed" |
| Rev 20:3 | ἔβαλεν ... καὶ ἔκλεισεν καὶ ἐσφράγισεν | V-2AAI-3S + CONJ + V-AAI-3S + CONJ + V-AAI-3S | "cast ... and shut ... and set a seal" |

The chain is not a special tense form; it is a discourse use of repeated finite aorists. The perfective aspect packages each event as complete for narrative purposes.

### 2. Coordinated Result Cluster

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Eph 2:6 | καὶ συνήγειρεν καὶ συνεκάθισεν | CONJ + V-AAI-3S + CONJ + V-AAI-3S | "raised [us] up together, and made [us] sit together" |
| Rev 20:2 | ἐκράτησεν ... καὶ ἔδησεν | V-AAI-3S + CONJ + V-AAI-3S | "laid hold ... and bound" |

The coordinated aorists may describe distinct but closely related actions in one scene. The grammar itself does not decide whether the actions are simultaneous or strictly sequential; that comes from lexical order and context.

## Contrast with Related Forms

| Form | Aspect/Function | Example |
|------|-----------------|---------|
| Aorist active indicative chain | bounded finite events advancing narrative | Rev 20:2-3 ἐκράτησεν ... ἔδησεν ... ἔβαλεν ... ἔκλεισεν ... ἐσφράγισεν |
| Present active participle | attendant/background description, not main finite event-line | Rev 20:1 καταβαίνοντα, ἔχοντα |
| Aorist passive indicative | subject undergoes the event; agent may be suppressed | Rev 9:15 ἐλύθησαν |
| Perfect indicative | completed act with continuing state/result | John 19:30 Τετέλεσται |

## Rev 20:2-3 Parser-Verified Chain

| Word | Lemma | Strong | Parsing |
|------|-------|--------|---------|
| ἐκράτησεν | κρατέω | G2902 | V-AAI-3S |
| ἔδησεν | δέω | G1210 | V-AAI-3S |
| ἔβαλεν | βάλλω | G906 | V-2AAI-3S |
| ἔκλεισεν | κλείω | G2808 | V-AAI-3S |
| ἐσφράγισεν | σφραγίζω | G4972 | V-AAI-3S |

These five verbs form the bounded action-chain of Rev 20:2-3. The grammar marks the actions as finite, active, indicative events; it does not by itself settle theological questions about referents or fulfillment.

---
*Generated from: greek_parser.py (--verse, --search, --pattern)*
*Last updated: 2026-05-07*
