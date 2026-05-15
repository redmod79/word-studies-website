# ἐνέργεια + Subjective Genitive (Greek)

## Definition

The **subjective genitive** is a genitive case construction in which the noun in the genitive *performs the action* implied by its head noun (the noun it modifies). The genitive names the **subject/agent** of the verbal idea embedded in the head noun, not its object. Wallace classifies it under "Genitive of Producer / Subjective Genitive" (Wallace, *Greek Grammar Beyond the Basics*, 113–116).

The noun **ἐνέργεια** (G1753, "working, operation, effectual working") is a verbal noun built on ἐνεργέω ("to work, to be at work in"). Because its lexical content is inherently verbal, a following genitive almost always names **the agent doing the working**, making ἐνέργεια + genitive a near-canonical host for the subjective-genitive construction in the Pauline corpus.

1. **Subjective genitive** — the genitive names the doer of the action implicit in the head noun ("the working of God" = God works).
2. **ἐνέργεια + personal genitive** — Pauline idiom; the genitive almost always specifies whose working it is.
3. **Prepositional collocation κατά + ἐνέργεια(ν) + gen.** — "according to the working of [agent]"; identifies the causal/instrumental source behind an action or state.

## Form Recognition

- Head noun is a **verbal noun** (action nominal): ἐνέργεια, πίστις, ἀγάπη, κρίσις, ἐλπίς, ἀποκάλυψις, παράκλησις, κλῆσις.
- Modified by a noun in the **genitive case** denoting a person or agent capable of performing the action.
- Diagnostic test: paraphrase with a finite verb — "the X-ing of Y" → "Y X-s." If the paraphrase yields a coherent sentence where the genitive is the grammatical subject, it is subjective.
- Contrast diagnostic: if the paraphrase instead makes the genitive the **direct object** ("Y is X-ed"), the genitive is *objective*, not subjective.
- **Parser signature for ἐνέργεια constructions:** `N-ASF` (after κατά) or `N-GSF` (after διά) + article + `N-GSM/GSF` personal noun.
- **Morph code pattern (κατά + ἐνέργειαν + gen.):** `PREP T-ASF N-ASF T-GSM N-GSM` (e.g., κατὰ τὴν ἐνέργειαν τοῦ Θεοῦ).

## Functions with Examples

### 1. ἐνέργεια + Subjective Genitive — God as Agent (Pauline norm)

The Pauline corpus uses ἐνέργεια eight times; in every instance where a personal genitive or pronoun is attached, the genitive specifies **who is doing the working**. In six of these seven referential occurrences the agent is **God/Christ**.

| Reference | Greek (construction) | Morph | KJV |
|-----------|----------------------|-------|-----|
| Eph 1:19 | κατὰ τὴν ἐνέργειαν τοῦ κράτους τῆς ἰσχύος **αὐτοῦ** | PREP T-ASF N-ASF … P-GSM | "according to the working of his mighty power" |
| Eph 3:7 | κατὰ τὴν ἐνέργειαν τῆς δυνάμεως **αὐτοῦ** | PREP T-ASF N-ASF T-GSF N-GSF P-GSM | "according to the effectual working of his power" |
| Eph 4:16 | κατ' ἐνέργειαν ἐν μέτρῳ ἑνὸς ἑκάστου μέρους | PREP N-ASF | "according to the effectual working in the measure of every part" |
| Phil 3:21 | κατὰ τὴν ἐνέργειαν τοῦ δύνασθαι **αὐτὸν** | PREP T-ASF N-ASF T-GSN V-PNN P-ASM | "according to the working whereby he is able" |
| Col 1:29 | κατὰ τὴν ἐνέργειαν **αὐτοῦ** τὴν ἐνεργουμένην ἐν ἐμοί | PREP T-ASF N-ASF P-GSM | "according to his working, which worketh in me mightily" |
| Col 2:12 | διὰ τῆς πίστεως τῆς ἐνεργείας **τοῦ Θεοῦ** | PREP T-GSF N-GSF T-GSM N-GSM | "through the faith of the operation of God" |

Paraphrase test on Col 2:12: "the working of God" → **God works** (raises Christ from the dead — explicit in the following relative clause τοῦ ἐγείραντος αὐτὸν ἐκ νεκρῶν). The genitive τοῦ Θεοῦ is the subject of the verbal idea in ἐνεργείας. Same analysis applies to all six.

### 2. ἐνέργεια + Subjective Genitive — Satan as Agent (inversion)

2 Thess 2:9 applies the identical syntactic pattern to an opposing agent:

| Reference | Greek | Morph | KJV |
|-----------|-------|-------|-----|
| 2 Thess 2:9 | κατ' ἐνέργειαν **τοῦ Σατανᾶ** | PREP N-ASF T-GSM N-GSM | "after the working of Satan" |

The construction κατ' ἐνέργειαν + genitive of a personal agent is *morphologically identical* to the Pauline God-pattern (Eph 1:19; 3:7; Col 1:29; Phil 3:21). The genitive τοῦ Σατανᾶ is **subjective**: Satan performs the working. The παρουσία of the man of lawlessness is not self-generated — it is Satan at work through him.

Paraphrase test: "according to the working of Satan" → **Satan works** (in/through the man of lawlessness). The signs and wonders enumerated in the same verse (ἐν πάσῃ δυνάμει καὶ σημείοις καὶ τέρασιν ψεύδους) are grammatically subordinated to this subjective-genitive head: they are instruments of Satan's ἐνέργεια, not the lawless one's independent capacity.

### 3. ἐνέργεια + Subjective Genitive — Delusion as Agent (2 Thess 2:11)

| Reference | Greek | Morph | KJV |
|-----------|-------|-------|-----|
| 2 Thess 2:11 | πέμπει αὐτοῖς ὁ Θεὸς ἐνέργειαν πλάνης | V-PAI-3S P-DPM T-NSM N-NSM N-ASF N-GSF | "God shall send them strong delusion" |

Here the genitive πλάνης ("of error/delusion") is the content/source of the working God sends — also functionally subjective (the delusion *does* the working). Same construction type, different agent class.

## Structural Parallel: Rev 13:2 / 13:4

The Pauline subjective-genitive pattern for Satan in 2 Thess 2:9 has a direct narrative/structural analogue in the Apocalypse:

| Reference | Greek construction | English (KJV) |
|-----------|--------------------|----|
| Rev 13:2 | **ἔδωκεν αὐτῷ ὁ δράκων** τὴν δύναμιν αὐτοῦ | "the dragon gave him his power" |
| Rev 13:4 | τῷ δράκοντι **τῷ δεδωκότι** τὴν ἐξουσίαν τῷ θηρίῳ | "the dragon which gave power unto the beast" |
| 2 Thess 2:9 | κατ' ἐνέργειαν **τοῦ Σατανᾶ** | "after the working of Satan" |

Rev 13:2/4 expresses the same agency-transfer relation in **active verbal syntax** (δράκων as nominative subject of δίδωμι, beast as dative recipient). 2 Thess 2:9 expresses it in **nominal syntax** using a subjective genitive (Σατανᾶ as gen. agent under ἐνέργεια). The syntactic vehicles differ; the propositional content is parallel: *the adversary-figure operates as instrumental channel of a prior agent's power*.

## Contrast with Related Genitive Subtypes

| Subtype | Paraphrase test | ἐνέργεια example |
|---------|-----------------|------------------|
| **Subjective** | "X V-s" — gen. is subject | ἐνέργεια τοῦ Θεοῦ = "God works" (Col 2:12) |
| **Objective** | "X is V-ed" — gen. is object | Not attested with ἐνέργεια; ἐνέργεια has no patient-role reading. |
| **Possessive** | "belonging to X" — gen. possesses | Weaker reading; "God's working" blurs into subjective when head noun is verbal. |
| **Source/Origin** | "V coming from X" | Overlaps with subjective for verbal heads; distinction often non-forcing. |
| **Plenary (both)** | Subj + obj simultaneously | Debated for πίστις Χριστοῦ; not applicable to ἐνέργεια because it takes no patient. |

**Key principle (Wallace 113–116):** When the head noun is a verbal noun (like ἐνέργεια, from ἐνεργέω), the default reading is subjective unless the context forces an objective/patient reading. ἐνέργεια lexically denotes *the act of working*; an action's grammatical slots are (agent, instrument), not (agent, patient), so a genitive modifying it naturally fills the agent slot.

## Subtypes of Subjective Genitive (Wallace 113–116)

| Subtype | Description | Example with ἐνέργεια |
|---------|-------------|------------------------|
| Pure subjective | Gen. = grammatical subject of implied verb | ἐνέργεια τοῦ Θεοῦ (Col 2:12) |
| Subjective of source/producer | Gen. = the one *from whom* the action originates | ἐνέργεια αὐτοῦ (Col 1:29) — God's own active power |
| Subjective with instrumental extension | Head noun governs ἐν + dat. or acc. naming the medium | κατὰ τὴν ἐνέργειαν αὐτοῦ τὴν ἐνεργουμένην ἐν ἐμοί (Col 1:29) — God works *in* Paul |

## Summary of the Pauline Pattern

- **8 total NT occurrences** of ἐνέργεια, **all Pauline**, **all with κατά or διά + personal/agentive genitive** (or equivalent pronoun).
- **7 reference God/Christ as agent** (Eph 1:19, 3:7, 4:16; Phil 3:21; Col 1:29, 2:12; 2 Thess 2:11 — delusion *sent by* God).
- **1 references Satan as agent** (2 Thess 2:9) — structurally identical construction, inverted referent.
- Morphology, preposition, case, and article-structure match across the divine and satanic uses: the grammar treats Satan's ἐνέργεια and God's ἐνέργεια as the *same kind of relation* — an agent working through a visible manifestation.

---
*Generated from: greek_parser.py (--lemma ἐνέργεια, --verse on all 7 occurrences). Wallace, *Greek Grammar Beyond the Basics* (1996), 113–116 (subjective genitive).*
*Last updated: 2026-04-17*
