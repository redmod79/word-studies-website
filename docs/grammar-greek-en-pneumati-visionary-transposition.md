# ἐν πνεύματι — Visionary-State Marker / Visionary Transposition (Greek)

## Definition

In Revelation, the anarthrous prepositional phrase **ἐν πνεύματι** ("in [the] Spirit" / "in spirit") functions as a **discrete technical marker** signaling the seer's entry into, or transposition within, the visionary state. It occurs four times (Rev 1:10; 4:2; 17:3; 21:10) and demarcates the four macro-sections of the book. Unlike general Pauline/Lukan adverbial uses of ἐν πνεύματι (e.g., "walk in the Spirit," "rejoice in the Spirit"), the Revelation pattern pairs the phrase with a first-person verb of visionary becoming or transport and introduces a new locus of vision.

1. **Inception** — enters the visionary state and establishes the first vantage point (Rev 1:10).
2. **Transposition** — relocates the seer to a new vantage within the same visionary state (Rev 4:2; 17:3; 21:10).
3. **Structural demarcation** — segments Revelation into four panels at exactly these four points.

## Form Recognition

The phrase is built from a fixed three-element syntactic kernel:

- **ἐν** (G1722) — [PREP]
- **πνεύματι** — πνεῦμα (G4151), [N-DSN] Dative Singular Neuter, **anarthrous** (no article)
- Paired with a **first-person singular aorist verb** of becoming (γίνομαι G1096) or of being carried (ἀποφέρω G667, passive-active action on the seer)

Morphological diagnostics:
- **Parser search (verb):** `lemma=γίνομαι tense=aorist voice=middle person=1 number=singular` for 1:10 and 4:2; `lemma=ἀποφέρω tense=aorist person=3` acting on accusative με for 17:3 and 21:10.
- **Morph codes to match:** `V-2ADI-1S` (ἐγενόμην) and `V-AAI-3S` + accusative 1s pronoun (ἀπήνεγκέν με).
- **Diagnostic phrase:** anarthrous dative πνεύματι immediately governed by ἐν, with no genitive modifier (contrast Pauline τῷ πνεύματι or πνεύματι θεοῦ).
- **Case for πνεῦμα** is locative/sphere dative — translational options "in the Spirit" vs. "in spirit" (subjective-ecstatic state) cannot be settled by morphology alone; the dative + ἐν construction is neutral between agentive, locative, and state-of-being senses.

## The Four Occurrences (Tool-Verified)

### 1. Revelation 1:10 — Inception

Greek text (parser output):
> ἐγενόμην ἐν Πνεύματι ἐν τῇ κυριακῇ ἡμέρᾳ, καὶ ἤκουσα ὀπίσω μου φωνὴν μεγάλην ὡς σάλπιγγος

| Word | Lemma | Strong | Parse |
|------|-------|--------|-------|
| ἐγενόμην | γίνομαι | G1096 | V-2ADI-1S (Aor Mid Ind 1S) |
| ἐν | ἐν | G1722 | PREP |
| Πνεύματι | πνεῦμα | G4151 | N-DSN |
| ἐν | ἐν | G1722 | PREP |
| τῇ ... ἡμέρᾳ | ὁ / ἡμέρα | G3588 / G2250 | T-DSF / N-DSF |

**Structure:** γίνομαι (aorist middle, 1s) + ἐν πνεύματι + ἐν + temporal dative (ἡμέρᾳ). The double-ἐν construction distinguishes the **state** (ἐν πνεύματι, sphere/mode) from the **calendar time** (ἐν τῇ κυριακῇ ἡμέρᾳ, temporal-locative). The aorist of γίνομαι with ἐν + dative idiomatically expresses *coming-to-be-in* a state (compare ἐγένετο ἐν ἀγωνίᾳ Luke 22:44 — "he came to be in agony").

### 2. Revelation 4:2 — Transposition to heavenly throne-room

> εὐθέως ἐγενόμην ἐν Πνεύματι· καὶ ἰδοὺ θρόνος ἔκειτο ἐν τῷ οὐρανῷ

| Word | Lemma | Strong | Parse |
|------|-------|--------|-------|
| εὐθέως | εὐθέως | G2112 | ADV |
| ἐγενόμην | γίνομαι | G1096 | V-2ADI-1S |
| ἐν | ἐν | G1722 | PREP |
| Πνεύματι | πνεῦμα | G4151 | N-DSN |

**Structure:** Identical kernel to 1:10 (ἐγενόμην ἐν Πνεύματι) fronted by adverb εὐθέως ("immediately"). Because the seer is already within the Patmos-inception vision, 4:2 is grammatically **not a fresh inception** but an intensified re-entry / re-location within the same visionary arc — marked by εὐθέως and immediately followed by ἰδού + new locus (θρόνος ... ἐν τῷ οὐρανῷ).

### 3. Revelation 17:3 — Transposition to wilderness

> καὶ ἀπήνεγκέν με εἰς ἔρημον ἐν Πνεύματι. καὶ εἶδον γυναῖκα καθημένην ἐπὶ θηρίον κόκκινον

| Word | Lemma | Strong | Parse |
|------|-------|--------|-------|
| ἀπήνεγκέν | ἀποφέρω | G667 | V-AAI-3S |
| με | ἐγώ | G1473 | P-1AS |
| εἰς | εἰς | G1519 | PREP |
| ἔρημον | ἔρημος | G2048 | A-ASF |
| ἐν | ἐν | G1722 | PREP |
| Πνεύματι | πνεῦμα | G4151 | N-DSN |

**Structure shift:** 1st-person γίνομαι ("I came to be") gives way to 3rd-person ἀποφέρω acting on accusative με ("he carried me away"). The ἐν πνεύματι adjunct now modifies **the mode of transport** (aorist active of ἀποφέρω + εἰς + acc. of destination + ἐν πνεύματι of manner/sphere). ἀποφέρω (G667, 7 NT occurrences) contributes the sense of bodily / ecstatic removal; ἐν πνεύματι qualifies the removal as occurring **in the Spirit / in spirit**, not corporeally.

### 4. Revelation 21:10 — Transposition to high mountain

> καὶ ἀπήνεγκέν με ἐν Πνεύματι ἐπὶ ὄρος μέγα καὶ ὑψηλόν, καὶ ἔδειξέν μοι τὴν πόλιν τὴν ἁγίαν Ἱερουσαλὴμ

| Word | Lemma | Strong | Parse |
|------|-------|--------|-------|
| ἀπήνεγκέν | ἀποφέρω | G667 | V-AAI-3S |
| με | ἐγώ | G1473 | P-1AS |
| ἐν | ἐν | G1722 | PREP |
| Πνεύματι | πνεῦμα | G4151 | N-DSN |
| ἐπὶ | ἐπί | G1909 | PREP |
| ὄρος ... ὑψηλόν | ὄρος / μέγας / ὑψηλός | G3735 / G3173 / G5308 | N-ASN / A-ASN / A-ASN |

**Structure:** Grammatically identical to 17:3 (ἀπήνεγκέν με ἐν πνεύματι + preposition-of-destination + accusative), but ἐν πνεύματι is **fronted** before the destination prepositional phrase (contrast 17:3's post-destination placement). Word-order variation between 17:3 and 21:10 is stylistic; syntactic function is equivalent.

## Four-Panel Structural Function

The four occurrences are non-accidentally distributed: each marks the head of a major section of Revelation.

| # | Reference | Verb kernel | Spatial frame | Section introduced |
|---|-----------|-------------|---------------|--------------------|
| 1 | Rev 1:10 | ἐγενόμην ἐν πνεύματι | Patmos (ἐν τῇ κυριακῇ ἡμέρᾳ) | Letters to the seven churches (1–3) |
| 2 | Rev 4:2 | ἐγενόμην ἐν πνεύματι | heaven (θρόνος ... ἐν τῷ οὐρανῷ) | Throne-room / seals / trumpets / bowls (4–16) |
| 3 | Rev 17:3 | ἀπήνεγκέν με ... ἐν πνεύματι | wilderness (εἰς ἔρημον) | Judgment of Babylon (17–20) |
| 4 | Rev 21:10 | ἀπήνεγκέν με ἐν πνεύματι | high mountain (ἐπὶ ὄρος μέγα καὶ ὑψηλόν) | New Jerusalem (21–22) |

Internal grammatical chiasm:
- **A** 1:10 γίνομαι + earthly locus (Patmos)
- **B** 4:2 γίνομαι + heavenly locus (throne)
- **B′** 17:3 ἀποφέρω + desert locus (wilderness)
- **A′** 21:10 ἀποφέرω + elevated locus (mountain)

The γίνομαι → ἀποφέρω shift at the midpoint (after Rev 16) marks the transition from passive state-entry to active angelic conveyance for the two final judgment/salvation contrasts (harlot-city vs. bride-city), with parallel destination-nouns (ἔρημον 17:3 ‖ ὄρος 21:10) and parallel following showing-verbs (εἶδον 17:3 / ἔδειξέν μοι 21:10).

## Background: LXX Ezekiel Parallels

The visionary-transport idiom with πνεῦμα + dative / accusative-of-person is a direct inheritance from LXX Ezekiel. Tool-verified LXX citations:

| LXX Reference | Greek (LXX) | Shared elements |
|---------------|-------------|-----------------|
| Ezek 3:14 | καὶ τὸ πνεῦμα ἐξῆρέν με καὶ ἀνέλαβέν με ... ἐπορεύθην ἐν ὁρμῇ τοῦ πνεύματός μου | πνεῦμα + accusative με + verb of lifting / carrying |
| Ezek 8:3 | καὶ ἀνέλαβέν με πνεῦμα ... καὶ ἤγαγέν με εἰς Ιερουσαλημ ἐν ὁράσει θεοῦ | πνεῦμα + με + ἤγαγέν + εἰς + destination |
| Ezek 11:24 | καὶ ἀνέλαβέν με πνεῦμα καὶ ἤγαγέν με εἰς γῆν Χαλδαίων ... ἐν ὁράσει ἐν πνεύματι θεοῦ | explicit **ἐν πνεύματι** + visionary transport |
| Ezek 37:1 | καὶ ἐξήγαγέν με **ἐν πνεύματι κύριος** καὶ ἔθηκέν με ἐν μέσῳ τοῦ [πεδίου] | **ἐν πνεύματι** + subject κύριος + carrying-out verb |

Rev 17:3 / 21:10 (ἀπήνεγκέν με ... ἐν πνεύματι + εἰς/ἐπὶ + destination) reproduces the LXX-Ezekiel schema almost morpheme-for-morpheme, swapping the verb of carrying from ἄγω / ἀναλαμβάνω / ἐξάγω to ἀποφέρω. Ezek 37:1 is the closest lexical match: same anarthrous ἐν πνεύματι + 3ms aorist active of a carrying-verb + accusative με.

## Contrast with General NT ἐν πνεύματι Uses

The Revelation pattern is **not** equivalent to broader NT uses of ἐν πνεύματι. Three non-visionary categories must be distinguished:

| Usage type | Sample references | Function |
|------------|-------------------|----------|
| Instrumental (agent-Spirit) | Matt 12:28 ἐν πνεύματι θεοῦ ἐκβάλλω; Matt 22:43 ἐν πνεύματι καλεῖ | means/agency — "by the Spirit" |
| Sphere-of-life / walk | Rom 8:9; Gal 5:16 περιπατεῖτε πνεύματι; Eph 6:18 προσευχόμενοι ἐν πνεύματι | habitual mode of Christian existence |
| Ecstatic / charismatic state | 1 Cor 14:2 πνεύματι λαλεῖ μυστήρια; Luke 2:27 ἐν τῷ πνεύματι εἰς τὸ ἱερόν | Spirit-driven state, overlapping but not identical to Revelation's τεχνικός use |

The Revelation formula is distinguished by (a) first-person narrative framing, (b) pairing with a verb of becoming or transport, (c) introduction of a new visionary locus, and (d) structural-segmentation function at the book's macro-divisions.

## Translation Ambiguity (Documented, Not Adjudicated)

The anarthrous πνεύματι + dative of ἐν leaves four translational options that the grammar alone does not decide:

1. **"in the Spirit"** (agent/sphere — the Holy Spirit as source of the ecstatic state); KJV, most modern versions.
2. **"in spirit"** (human-pneumatic contrast with σῶμα / σάρξ — ecstatic disembodiment; cf. 2 Cor 12:2–3 εἴτε ἐν σώματι ... εἴτε ἐκτὸς τοῦ σώματος).
3. **"in prophetic inspiration"** (technical prophetic-state gloss; appeals to Ezek-LXX background).
4. **Ambiguous by design** (both senses intended — the Spirit of God effecting the seer's spirit-state).

None of these is settled by morphology; all four are grammatically compatible with `ἐν [PREP] + πνεύματι [N-DSN]` anarthrous.

## Linked Library Entries

- [apocalyptic-narrative-prolepsis](apocalyptic-narrative-prolepsis.md) — visionary-sequence ≠ historical-sequence; same genre-mechanics operate within each ἐν-πνεύματι panel.
- [participle-perfect-passive-state](participle-perfect-passive-state.md) — state-aspect summary tableaux that typically follow an ἐν-πνεύματι transposition.

---
*Generated from: greek_parser.py --verse REV 1:10 / 4:2 / 17:3 / 21:10; search_strongs.py --lookup G1096 / G667 / G4151; search_strongs.py --lxx-verse Eze 3:14 / 8:3 / 11:24 / 37:1*
*Last updated: 2026-04-18*
