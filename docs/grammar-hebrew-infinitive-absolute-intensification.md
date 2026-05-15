# Infinitive Absolute + Cognate Finite Verb (Hebrew)

## Definition
The Hebrew **infinitive absolute** placed immediately before (occasionally after) a finite verb of the **same root and stem** forms the *figura etymologica* / *paronomastic infinitive* construction. Also called the "emphatic" or "intensifying" infinitive absolute. The construction is context-neutral in form; force is determined by the finite verb's mood and the discourse frame.

1. **Intensifying / emphatic** — adds rhetorical force to the cognate verb ("surely X," "indeed X," "utterly X"); GKC §113n-r, Joüon-Muraoka §123d-p, IBHS §35.3.1.
2. **Command-strengthening** — with a following imperfect used modally, produces an emphatic, non-negotiable imperative ("you shall certainly do X"); the imperfect alone would be a mere command or prediction.
3. **Concessive / contrastive** — with negation (לֹא + inf.abs. + impf.) produces "I will not *utterly* X" (Amos 9:8), preserving the act while denying totality.
4. **Protasis-emphasis in conditional** — inside אִם-clauses, intensifies the condition ("if thou wilt **indeed** look," 1 Sam 1:11).

## Form Recognition
Two adjacent finite-verbal words share a lemma; the first is tagged **InfAbs**, the second is a **finite form** (Perfect, Imperfect, Imperative, or Participle) of the same root.

- **Parser code (first word):** `sp=verb vt=infa`
- **Parser code (second word):** any finite tense — `vt=perf`, `vt=impf`, `vt=impv`
- **Same lemma requirement:** both words share the three-consonant root (e.g. both חרם, both מות, both ברך)
- **Same stem requirement:** Qal-Qal, Hiphil-Hiphil, Piel-Piel pattern
- The inf.abs. is morphologically invariant (no person/number/gender affixation) — a bare stem form often vocalized qāṭôl (Qal), haqtēl (Hiphil), qattēl (Piel)
- KJV translation clues: "surely," "utterly," "indeed," "in [verb]-ing I will [verb]"

## Functions with Examples

### 1. Intensified Command (Hiphil inf.abs. + Hiphil impf.) — *haḥărēm taḥărîm(ēm)*

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Deut 7:2 | הַחֲרֵ֤ם תַּחֲרִים֙ אֹתָ֔ם | Hiphil.InfAbs + Hiphil.Impf.2ms (חרם) | "thou shalt utterly destroy them" |
| Deut 20:17 | הַחֲרֵ֣ם תַּחֲרִימֵ֗ם | Hiphil.InfAbs + Hiphil.Impf.2ms+3mp (חרם) | "thou shalt utterly destroy them" |

The Hiphil imperfect 2ms carries legislative/directive force ("thou shalt…"); the prefixed cognate inf.abs. raises the command from general prescription to categorical, non-negotiable imperative. Deut 20:17 adds a 3mp suffix on the finite verb, binding the nations listed in apposition directly into the verbal morphology.

### 2. Intensified Warning / Penal Certainty (Qal inf.abs. + yiqtol)

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Gen 2:17 | מֹ֥ות תָּמֽוּת | Qal.InfAbs + Qal.Impf.2ms (מות) | "thou shalt surely die" |
| Gen 3:4 | לֹֽא־מֹ֖ות תְּמֻתֽוּן | Neg + Qal.InfAbs + Qal.Impf.2mp (מות) | "Ye shall not surely die" |
| Exod 21:12 | מֹ֥ות יוּמָֽת | Qal.InfAbs + Hophal.Impf.3ms (מות) | "shall be surely put to death" |

Gen 3:4 illustrates negation: the serpent echoes Gen 2:17's inf.abs. construction with prefixed לֹא, producing a direct contradiction at the level of emphatic certainty. Exod 21:12 shows a rare stem-switch across the construction (Qal inf.abs. + Hophal impf.), treated by grammarians as a licensed exception because the root and semantic force carry the figure (GKC §113w).

### 3. Solemn / Covenantal Promise (Piel or Hiphil inf.abs. + impf.)

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Gen 22:17 | בָרֵ֣ךְ אֲבָרֶכְךָ֗ | Piel.InfAbs + Piel.Impf.1s+2ms (ברך) | "in blessing I will bless thee" |
| Gen 22:17 | הַרְבָּ֨ה אַרְבֶּ֤ה | Hiphil.InfAbs + Hiphil.Impf.1s (רבה) | "in multiplying I will multiply" |

Two back-to-back constructions in a single verse mark the Abrahamic blessing as irrevocable oath-speech.

### 4. Negated Totality (לֹא + inf.abs. + impf.)

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Amos 9:8 | לֹ֣א הַשְׁמֵ֥יד אַשְׁמִ֛יד | Neg + Hiphil.InfAbs + Hiphil.Impf.1s (שׁמד) | "I will not utterly destroy" |

The negation scopes over the intensifier, not the bare verb — YHWH will destroy the sinful kingdom (v.8a הִשְׁמַדְתִּי Hiphil.Perf.1s) but not *utterly* the house of Jacob.

### 5. Emphatic Protasis in Conditional Vow (אִם + inf.abs. + impf.)

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| 1 Sam 1:11 | אִם־רָאֹ֥ה תִרְאֶ֣ה | Cond + Qal.InfAbs + Qal.Impf.2ms (ראה) | "if thou wilt indeed look" |

The inf.abs. intensifies the protasis of a conditional vow (cross-referenced with [syntax-conditional-vow](syntax-conditional-vow.md)).

## Contrast with Related Forms

| Form | Function | Example |
|------|----------|---------|
| Inf.abs. + cognate finite verb | intensifies / makes emphatic | Deut 7:2 |
| Inf.abs. *after* finite verb | adverbial-continuative ("continually doing") — GKC §113r | Jer 23:17 (different function) |
| Inf.abs. standing alone for finite verb | narrative-substitute, imperatival | Deut 5:12 שָׁמֹור (imperatival inf.abs.) |
| Inf.construct + ל | purpose / complement ("in order to") | Gen 2:17 אֲכָלְךָ |
| Cognate accusative (verb + noun from same root) | related emphatic figure, but noun not verb | 1 Sam 1:11 וַתִּדֹּר נֶדֶר "she vowed a vow" |

**Do not confuse** the *figura etymologica* (inf.abs. + finite of same root) with:
- Two consecutive verbs that happen to share a root across different stems with narrative function (Hiphil of נכה + Qal of מות in Exod 21:12 v.12a–b — separate predication, not paronomastic).
- Verbal-hendiadys ("X and Y" = one action).

Cross-references in library: [hiphil-imperfect](hiphil-imperfect.md) (the governing finite verb in most conquest-command cases), [qal-imperfect](qal-imperfect.md), [syntax-conditional-vow](syntax-conditional-vow.md).

## Common Verbs Appearing in This Construction

Based on parser-verified occurrences:

| Verb | Strong's | Gloss in this form | Example |
|------|----------|--------------------|---------|
| חרם | H2763 | "utterly destroy / devote to destruction" (Hiphil) | Deut 7:2; 20:17 |
| מות | H4191 | "surely die" (Qal + Hophal variant) | Gen 2:17; Gen 3:4; Exod 21:12 |
| ברך | H1288 | "in blessing bless" (Piel) | Gen 22:17 |
| רבה | H7235 | "greatly multiply" (Hiphil) | Gen 22:17 |
| שׁמד | H8045 | "utterly destroy" (Hiphil) | Amos 9:8 |
| ראה | H7200 | "indeed look" (Qal) | 1 Sam 1:11 |

## Grammatical Notes

- **Word order:** the inf.abs. almost always **precedes** the finite verb when intensifying (GKC §113n). Post-posed inf.abs. typically signals continuation/duration, not intensification.
- **Translation strategy:** KJV uses "surely," "utterly," "indeed," or cognate-noun paraphrase ("in blessing I will bless"); the LXX frequently renders with cognate noun + verb (εὐλογῶν εὐλογήσω σε, Gen 22:17) — a calque that pulls the Hebrew emphatic figure into Greek.
- **Mood amplification:** the construction intensifies but does not change the finite verb's mood. With directive imperfect it strengthens command; with predictive imperfect it strengthens certainty; with conditional אִם-impf. it strengthens the condition.
- **Parser tagging caveat:** ETCBC/BHSA tags the InfAbs with placeholder "unknownunknown" for person/gender/number — the form is morphologically invariant, so absence of those features is the diagnostic, not a parsing error.

---
*Generated from: hebrew_parser.py (--verse, --lemma)*
*Last updated: 2026-04-18*
