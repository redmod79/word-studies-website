# Articular Infinitive of Purpose/Result (Greek)

## Definition

The Greek articular infinitive is an infinitive governed by the neuter singular
article. The article lets the infinitive function like a verbal noun, while the
case of the article and any governing preposition mark its syntactic relation.
For purpose/result, the common forms are **εἰς τὸ + infinitive**, **πρὸς τὸ +
infinitive**, and sometimes the genitive **τοῦ + infinitive**.

1. **Purpose / intended result** - the infinitive names the aim toward which the
   controlling action is directed.
2. **Actual result / consequence** - the infinitive names the outcome produced
   by the preceding clause.
3. **Genitive purpose** - τοῦ + infinitive can mark the intended purpose of a
   preceding action, verb, or verbal idea.

Purpose and result are contextual labels. The construction itself marks a
directed verbal idea; surrounding verbs, discourse flow, and translation choices
determine whether the sense is best described as aim, intended result, or actual
result.

## Form Recognition

- **Article + infinitive:** neuter singular article before an infinitive:
  τὸ, τοῦ, or τῷ followed by a verb tagged `V-...N`.
- **Accusative articular infinitive:** usually `T-ASN` + infinitive; often
  governed by εἰς or πρός for purpose/result.
- **Genitive articular infinitive:** `T-GSN` + infinitive; often marks purpose,
  especially after a verb or verbal idea.
- **Infinitive morph codes:** `V-PAN` (present active infinitive), `V-AAN`
  (aorist active infinitive), `V-APN` (aorist passive infinitive), `V-2AAN`
  (second aorist active infinitive), `V-2ADN` (second aorist middle infinitive).
- **Possible accusative subject:** the infinitive may have its own accusative
  subject, as in `εἰς τὸ εἶναι αὐτὸν` (Rom 3:26).
- **Parser searches:** `mood=infinitive`; pattern `PREP T-ASN V-*`; pattern
  `T-GSN V-*`. The pattern searches include participles too, so filter results
  manually for infinitive morph codes ending in `N`.

## Functions with Examples

### 1. εἰς τὸ + infinitive: purpose or result

This form uses εἰς with the accusative article `τὸ`. It commonly points forward
to the goal, intended outcome, or resulting state of the preceding action.

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Romans 1:11 | εἰς τὸ στηριχθῆναι ὑμᾶς | PREP + T-ASN + V-APN | "to the end ye may be established" |
| Romans 1:20 | εἰς τὸ εἶναι αὐτοὺς ἀναπολογήτους | PREP + T-ASN + V-PAN | "so that they are without excuse" |
| Romans 3:26 | εἰς τὸ εἶναι αὐτὸν δίκαιον | PREP + T-ASN + V-PAN | "that he might be just" |
| 1 Thessalonians 3:2 | εἰς τὸ στηρίξαι ὑμᾶς καὶ παρακαλέσαι | PREP + T-ASN + V-AAN + V-AAN | "to establish you, and to comfort you" |

### 2. πρὸς τὸ + infinitive: goal or directed purpose

πρός with the accusative article emphasizes direction toward an intended act or
result. The construction is close to εἰς τὸ, but πρός more visibly preserves the
idea of orientation "toward" the infinitival action.

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Matthew 5:28 | πρὸς τὸ ἐπιθυμῆσαι αὐτὴν | PREP + T-ASN + V-AAN | "to lust after her" |
| Acts 3:19 | πρὸς τὸ ἐξαλειφθῆναι ὑμῶν τὰς ἁμαρτίας | PREP + T-ASN + V-APN | "that your sins may be blotted out" |

### 3. τοῦ + infinitive: genitive purpose

The genitive article `τοῦ` with an infinitive can express purpose without an
overt preposition. It often follows a main action or verbal idea and gives the
intended aim of that action.

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Matthew 2:13 | ζητεῖν τὸ παιδίον τοῦ ἀπολέσαι αὐτό | T-GSN + V-AAN | "seek the young child to destroy him" |
| Luke 1:79 | τοῦ κατευθῦναι τοὺς πόδας ἡμῶν | T-GSN + V-AAN | "to guide our feet" |
| Acts 26:18 | τοῦ ἐπιστρέψαι ... τοῦ λαβεῖν | T-GSN + V-AAN; T-GSN + V-2AAN | "to turn ... that they may receive" |

## Contrast with Related Forms

| Form | Main Function | Example |
|------|---------------|---------|
| εἰς τὸ + infinitive | purpose, intended result, or result | Rom 3:26 εἰς τὸ εἶναι |
| πρὸς τὸ + infinitive | directed goal or purpose | Acts 3:19 πρὸς τὸ ἐξαλειφθῆναι |
| τοῦ + infinitive | genitive purpose or epexegetical infinitive | Matt 2:13 τοῦ ἀπολέσαι |
| ἵνα + subjunctive | finite purpose/result clause | See `purpose-clause-hina-me-aorist-subjunctive.md` |
| διά + τὸ + infinitive | cause, not purpose/result | Matt 24:12 διὰ τὸ πληθυνθῆναι |
| μετά + τὸ + infinitive | temporal sequence, "after" | Acts 1:3 μετὰ τὸ παθεῖν |

## Notes

- The article does not make the infinitive a finite verb. The infinitive remains
  non-finite and may take its own objects, modifiers, and accusative subject.
- Aorist infinitives usually present the action as a whole; present infinitives
  usually present it as ongoing or processive. The purpose/result force comes
  from the article/preposition construction and context, not from tense alone.
- Not every `T-ASN + V-*` sequence is an articular infinitive. The parser pattern
  also finds substantival participles; confirm that the verbal form is tagged as
  an infinitive (`...N`).

---
*Generated from: greek_parser.py (--verse, --search mood=infinitive, --pattern "PREP T-ASN V-*", --pattern "T-GSN V-*"); KJV text from D:/bible/tools/data/kjv.txt*
*Last updated: 2026-05-15*
