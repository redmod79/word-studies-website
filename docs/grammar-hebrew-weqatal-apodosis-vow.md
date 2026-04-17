# Weqatal (Perfect Consecutive) in Apodosis of Vow/Oath (Hebrew)

## Definition
The **weqatal** (also called "waw-consecutive + perfect" or "perfect consecutive") is a suffix-conjugation verb prefixed with וְ- that advances the main line of *non-past* discourse — future, modal, habitual, or consequent action. In vow/oath and conditional speech it most often stands in the **apodosis** ("then..."), committing the speaker to a future act contingent on the protasis ("if..."). The classic example is וְהַעֲלִיתִהוּ עֹלָה in Judg 11:31 — Jephthah's Hiphil Perf 1cs + waw + 3ms suffix: "*then* I will offer it up as a burnt offering."

1. **Apodosis of conditional vow** — the "then I will ___" clause pledging the speaker's obligation if a condition is met
2. **Continuation of a prior modal/future verb** — chaining further promises/commitments onto an initial imperfect, imperative, or participle
3. **Protasis extension** — occasionally continues the conditional clause itself (the "if..." side) before the apodosis begins

## Form Recognition
A weqatal looks identical in consonantal form to a plain perfect; the construction is recognized by **context and accentuation**, not morphology alone:

- **וְ- prefixed to a perfect-conjugation verb** (qatal form)
- In 1cs and 2ms forms, the stress often shifts to the final syllable (e.g., וְנָתַתָּ֥ה *wǝnātattā́* vs. plain perfect נָתַ֫תָּ *nātáttā*) — though this is inconsistent and not diagnostic for Hiphil perfects like וְהַעֲלִיתִ֖הוּ
- Follows a **future-oriented trigger**: imperfect, imperative, infinitive, participle of imminent action, or אִם clause
- **Parser codes:** `vs=<any stem> vt=perf` with a prefixed וְ conjunction. The hebrew_parser.py tool does *not* tag weqatal distinctly from plain perfect — identification is syntactic.

## Functions with Examples

### 1. Apodosis of a Vow (Subject = Speaker Pledging)

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Judg 11:31 | וְהַעֲלִיתִ֖הוּ עֹלָֽה | Verb.Hiphil.Perf.1s.+3ms | "and I will offer it up [for] a burnt offering" |
| Num 21:2 | וְהַֽחֲרַמְתִּ֖י אֶת־עָרֵיהֶֽם | Verb.Hiphil.Perf.1s | "then I will utterly destroy their cities" |
| 1 Sam 1:11 | וּנְתַתִּ֤יו לַֽיהוָה֙ | Verb.Qal.Perf.1s.+3ms | "then I will give him unto the LORD" |

All three are the **apodosis of an אִם-clause vow**. The speaker binds him/herself to a future cultic act (offer/devote/dedicate). The Hiphil forms in Judg 11:31 and Num 21:2 are structurally parallel: *Hiphil weqatal 1cs* committing the vower to causative action (cause-to-ascend / cause-to-be-devoted).

### 2. Apodosis of an Oath/Conditional (Subject = Second Party)

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Gen 24:8 | וְנִקִּ֕יתָ מִשְּׁבֻעָתִ֖י | Verb.Niphal.Perf.2ms | "then thou shalt be clear from this my oath" |
| 1 Sam 1:11 | וּזְכַרְתַּ֨נִי֙ ... וְנָתַתָּ֥ה | Verb.Qal.Perf.2ms | "and remember me ... and wilt give" |

Here the weqatal sits in the **apodosis of a conditional oath** but the subject is the *addressee* (Abraham's servant; YHWH). The form carries the consequent release or requested action.

### 3. Chained Weqatals Extending a Future Line

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Gen 28:20 | וּשְׁמָרַ֨נִי ... וְנָֽתַן־לִ֥י | Qal.Perf.3ms.+1us / Qal.Perf.3ms | "and will keep me ... and will give me" |
| Gen 28:21 | וְשַׁבְתִּ֥י ... וְהָיָ֧ה יְהוָ֛ה לִ֖י לֵאלֹהִֽים | Qal.Perf.1s / Qal.Perf.3ms | "So that I come again ... then shall the LORD be my God" |
| Exo 21:6 | וְהִגִּישֹׁ֤ו ... וְרָצַ֨ע ... וַעֲבָדֹ֖ו | Hiphil.Perf.3ms / Qal.Perf.3ms / Qal.Perf.3ms.+3ms | "shall bring him ... shall bore ... and he shall serve" |

Jacob's vow (Gen 28:20–22) illustrates weqatals within the **protasis** (conditions God must fulfill), with the apodosis introduced by a non-weqatal clause in v. 21b (יִהְיֶ֖ה ... וְהָיָ֧ה). Exo 21:6 is legal-conditional casuistic law — the standard "if X happens... *then* [weqatal] shall do Y" pattern.

## Contrast with Related Forms

| Form | Function | Example |
|------|----------|---------|
| **Weqatal (apodosis)** | future/modal commitment after condition | Judg 11:31 וְהַעֲלִיתִהוּ |
| **Plain Perfect (qatal)** | completed past action | Exo 21:5 אָהַ֨בְתִּי "I have loved" |
| **Wayyiqtol (וַ+impf)** | narrative past sequence | Judg 11:30 וַיִּדַּר "and he vowed" |
| **Imperfect (yiqtol)** | future/modal, often in protasis | 1 Sam 1:11 תִרְאֶ֣ה "[if] thou wilt look" |
| **Cohortative** | 1st person self-exhortation | — |

Weqatal and wayyiqtol are mirror-image "consecutive" forms: *wayyiqtol* advances **past narrative**; *weqatal* advances **future/modal/habitual** discourse. A Hiphil Perf 1cs + waw after a conditional clause is almost always weqatal, not a simple perfect — the semantics are commissive, not retrospective.

## Common Patterns in Vow Apodosis

| Vow Form | Protasis Trigger | Apodosis Weqatal | Reference |
|----------|------------------|------------------|-----------|
| אִם + InfAbs + Impf | "if indeed you give..." | וְהַחֲרַמְתִּי | Num 21:2 |
| וְהָיָה + participle + Impf | "whoever comes out..." | וְהַעֲלִיתִהוּ | Judg 11:31 |
| אִם + InfAbs + Impf + chained weqatals | "if indeed you look... and give..." | וּנְתַתִּיו | 1 Sam 1:11 |
| אִם + Impf | "if she will not..." | וְנִקִּיתָ | Gen 24:8 |

The **Hiphil weqatal 1cs with pronominal suffix** (וְהַעֲלִיתִ֖הוּ, "and-I-will-cause-it-to-ascend") is the diagnostic shape in Judg 11:31: causative stem + commissive weqatal + 3ms object suffix collapses "I will cause *it* to go up" into a single inflected word.

---
*Generated from: hebrew_parser.py (--verse, --search); KJV text via D:/bible/tools/data/kjv.txt*
*Last updated: 2026-04-16*
