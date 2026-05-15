# Dia with Genitive vs Accusative (Greek)

## Definition
**διά** (Strong's G1223) is a Greek preposition whose force is strongly shaped by the case of its complement. With the **genitive**, it normally marks passage, channel, agency, or means: "through, by means of, by." With the **accusative**, it normally marks cause, reason, basis, or interest: "because of, on account of, for the sake of."

1. **Genitive: channel / agency / means / route** - the complement is the route, instrument, intermediate agent, or means through which something happens.
2. **Accusative: cause / reason / sake** - the complement is the reason, basis, occasion, or person/thing for whose sake something happens.
3. **Case is the diagnostic** - English renderings overlap ("by," "through," "for"), so the Greek complement case must be checked.

## Form Recognition
- **Preposition:** διά, often elided as **δι'** before a vowel; parser marks it `[PREP]`.
- **Genitive complement:** the following article, noun, adjective, participle, or pronoun has a morph code with `G`: e.g. `T-GSF`, `N-GSF`, `P-GSM`.
- **Accusative complement:** the following article, noun, adjective, participle, or pronoun has a morph code with `A`: e.g. `T-ASF`, `N-ASF`, `P-2AP`.
- **Parser search:** `python greek_parser.py --lemma "διά" --limit 300`, then parse each verse with `python greek_parser.py --verse "ROM 3:25"` to identify the complement case.
- **Common patterns:** `διά + genitive` = `διὰ/δι'` + `T-G.. / N-G.. / P-G..`; `διά + accusative` = `διὰ/δι'` + `T-A.. / N-A.. / P-A..`.

## Functions with Examples

### 1. Genitive: Agency, Means, or Route

| Reference | Greek | Complement Parsing | KJV Translation |
|-----------|-------|--------------------|-----------------|
| Matt 1:22 | διὰ τοῦ προφήτου | `T-GSM` + `N-GSM` | "by the prophet" |
| John 1:3 | δι' αὐτοῦ | `P-GSM` | "by him" |
| Gal 1:1 | δι' ἀνθρώπου ... διὰ Ἰησοῦ Χριστοῦ | `N-GSM`; `N-GSM` + `N-GSM` | "by man ... by Jesus Christ" |
| Matt 7:13 | διὰ τῆς στενῆς πύλης | `T-GSF` + `A-GSF` + `N-GSF` | "in at the strait gate" |

With persons, **διά + genitive** often marks the intermediate agent or channel. In Matt 1:22 the same clause has **ὑπὸ Κυρίου** ("by the Lord") and **διὰ τοῦ προφήτου** ("through/by the prophet"), showing the distinction between source/agent language and mediated channel. The spatial sense "through/by way of" remains visible when the complement names a route or entrance, as in Matt 7:13.

### 2. Genitive: Means, Instrument, or Channel

| Reference | Greek | Complement Parsing | KJV Translation |
|-----------|-------|--------------------|-----------------|
| Rom 3:22 | διὰ πίστεως | `N-GSF` | "by faith" |
| Rom 3:24 | διὰ τῆς ἀπολυτρώσεως | `T-GSF` + `N-GSF` | "through the redemption" |
| Rom 3:25 | διὰ πίστεως | `N-GSF` | "through faith" |

With abstract nouns, **διά + genitive** marks the means, mediating process, or channel. The construction itself identifies grammatical mediation; it does not by itself decide broader interpretive questions about the referent.

### 3. Accusative: Cause, Reason, Basis, or Sake

| Reference | Greek | Complement Parsing | KJV Translation |
|-----------|-------|--------------------|-----------------|
| Matt 13:21 | διὰ τὸν λόγον | `T-ASM` + `N-ASM` | "because of the word" |
| Rom 3:25 | διὰ τὴν πάρεσιν | `T-ASF` + `N-ASF` | "for the remission" |
| Rom 4:25 | διὰ τὰ παραπτώματα | `T-APN` + `N-APN` | "for our offences" |
| Rom 4:25 | διὰ τὴν δικαίωσιν | `T-ASF` + `N-ASF` | "for our justification" |
| Gal 4:13 | δι' ἀσθένειαν | `N-ASF` | "through infirmity" |

With the accusative, **διά** points to the reason, occasion, basis, or beneficiary-interest behind the action. This can be rendered "because of," "on account of," "for," or "for the sake of," depending on context.

## Diagnostic Passage: Romans 3:25

Romans 3:25 contains both constructions:

| Phrase | Case | Parser Evidence | Grammatical Function |
|--------|------|-----------------|----------------------|
| διὰ πίστεως | Genitive | πίστεως = `N-GSF` | means / channel |
| διὰ τὴν πάρεσιν | Accusative | τὴν = `T-ASF`; πάρεσιν = `N-ASF` | reason / basis |

This is a clean control example: the preposition is the same, but the complement case changes the grammatical force.

## Contrast with Related Forms

| Form | Main Force | Example |
|------|------------|---------|
| **διά + genitive** | through, by means of, by agency of, by way of | Rom 3:24 διὰ τῆς ἀπολυτρώσεως |
| **διά + accusative** | because of, on account of, for the sake of | Matt 13:21 διὰ τὸν λόγον |
| **ὑπό + genitive** | agency/source, especially with passive verbs | Matt 1:22 ὑπὸ Κυρίου |
| **ἐκ + genitive** | source, origin, out from | Rom 3:26 ἐκ πίστεως |
| **εἰς + accusative** | direction, goal, result, purpose | Rom 3:25 εἰς ἔνδειξιν |

---
*Generated from: greek_parser.py (--lemma "διά"; --verse MAT 1:22, MAT 7:13, MAT 13:21, JHN 1:3, ROM 3:22-25, ROM 4:25, GAL 1:1, GAL 4:13) and KJV lookup.*
*Last updated: 2026-05-15*
