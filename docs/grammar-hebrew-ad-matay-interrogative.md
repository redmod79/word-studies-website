# ʿaḏ-māṯay (עַד־מָתַי) "How Long?" — Interrogative Lament Construction (Hebrew)

## Definition

Fixed compound interrogative **preposition עַד "until" + temporal interrogative מָתַי "when"** (ETCBC parses מָתַי as `Introg`, glossed "when"; עַד as `Prep`, glossed "unto"), functioning idiomatically as "until when? / how long?" It asks for the **endurance-limit / *terminus ad quem*** of an ongoing trial, oppression, delay, or divine silence. The sister form **עַד־אָנָה** (preposition עַד + locative-temporal interrogative אָנָה "whither / until where") carries the same semantic force in psalm-lament register (Psa 13:2 [MT]; cf. Hab 1:2).

1. **Lament / complaint** — sufferer (human or prophet) asks God how long the affliction must continue
2. **Impatience / rebuke** — speaker (human or divine) asks an addressee how long the offending behavior will persist
3. **Oracular / angelic query** — heavenly being asks YHWH how long a decreed judgment will remain in force — the question that *triggers* a time-answer

## Form Recognition

- Two-word maqqef-bound compound: **עַד־מָתַי** (sometimes unbound עַד מָתַי); variant **עַד־אָנָה**
- First word parses `Prep` (lemma עד); second word parses `Introg` (lemma מתי, H4970, or אן, H575)
- Always clause-initial or near-initial in direct speech
- **Parser search:** `hebrew_parser.py --lemma "מתי"` returns 28 instances of the interrogative (the lemma also surfaces as proper-name homographs *Amittai*, *Hamathite* — filter by parsing tag `Introg`)
- **KJV diagnostic:** invariably rendered "How long…?" — the English idiom is a near-perfect calque

## Functions with Examples

### 1. Lament-Psalm Complaint (sufferer → YHWH)

The voice is the afflicted worshiper; the addressee is YHWH; the expected answer is **relief / intervention**. The fourfold repetition in Psa 13 uses the variant **עַד־אָנָה**.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Psa 6:4 [MT] / 6:3 [Eng] | וְאַתָּה יְהוָה עַד־מָתָי | Prep + Introg | "but thou, O LORD, how long?" |
| Psa 13:2 [MT] / 13:1 [Eng] | עַד־אָנָה יְהוָה תִּשְׁכָּחֵנִי … עַד־אָנָה תַּסְתִּיר | Prep + Introg (×2) + Qal.Impf.2ms | "How long wilt thou forget me, O LORD? … how long wilt thou hide thy face" |
| Psa 74:10 | עַד־מָתַי אֱלֹהִים יְחָרֶף צָר | Prep + Introg + Piel.Impf.3ms | "O God, how long shall the adversary reproach?" |
| Psa 80:5 [MT] / 80:4 | עַד־מָתַי עָשַׁנְתָּ | Prep + Introg + Qal.Perf.2ms | "how long wilt thou be angry against the prayer of thy people?" |
| Psa 90:13 | שׁוּבָה יְהוָה עַד־מָתָי | Qal.Impv.2ms + Prep + Introg | "Return, O LORD, how long?" |
| Psa 94:3 | עַד־מָתַי רְשָׁעִים יְהוָה | Prep + Introg + Noun.mp.Abs | "LORD, how long shall the wicked, how long shall the wicked triumph?" |

### 2. Impatience / Rebuke (speaker → offending addressee)

The speaker (YHWH, prophet, ruler) addresses a party whose behavior is delinquent. Expected answer is **cessation / repentance**.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Exo 10:3 | עַד־מָתַי מֵאַנְתָּ לֵעָנֹת | Prep + Introg + Piel.Perf.2ms | "How long wilt thou refuse to humble thyself?" |
| 1 Sa 16:1 | עַד־מָתַי אַתָּה מִתְאַבֵּל | Prep + Introg + PersPron.2ms + Hithpael.Ptcp.ms | "How long wilt thou mourn for Saul?" |
| 1 Ki 18:21 | עַד־מָתַי אַתֶּם פֹּסְחִים | Prep + Introg + PersPron.2mp + Qal.Ptcp.mp | "How long halt ye between two opinions?" |
| Jer 4:14 | עַד־מָתַי תָּלִין בְּקִרְבֵּךְ | Prep + Introg + Qal.Impf.3fs | "How long shall thy vain thoughts lodge within thee?" |
| Jer 23:26 | עַד־מָתַי הֲיֵשׁ | Prep + Introg + Introg.+Part | "How long shall [this] be in the heart of the prophets that prophesy lies?" |
| Psa 82:2 | עַד־מָתַי תִּשְׁפְּטוּ־עָוֶל | Prep + Introg + Qal.Impf.2mp | "How long will ye judge unjustly…?" |

### 3. Prophetic / Oracular Query (prophet or angel → YHWH) — Oracle-Triggering

A prophet or heavenly being asks YHWH how long a decreed condition will hold. Distinctively, the question **triggers a bounded answer** — the ʿaḏ-māṯay question opens a lock to which YHWH's subsequent ʿaḏ-X answer is the key. **Dan 8:13–14 is the paradigm** of this function.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Isa 6:11 | עַד־מָתַי אֲדֹנָי | Prep + Introg + Noun.ms.Abs | "Lord, how long? And he answered, Until [עַד אֲשֶׁר] the cities be wasted…" |
| Hab 2:6 | עַד־מָתַי | Prep + Introg | "…woe to him that increaseth [that which is] not his! how long?" |
| Zech 1:12 | עַד־מָתַי אַתָּה לֹא־תְרַחֵם | Prep + Introg + PersPron.2ms + Neg + Piel.Impf.2ms | "O LORD of hosts, how long wilt thou not have mercy on Jerusalem…?" |
| **Dan 8:13** | עַד־מָתַי הֶחָזוֹן הַתָּמִיד וְהַפֶּשַׁע שֹׁמֵם | Prep + Introg + Art+Noun + Art+Noun + Conj+Art+Noun + Qal.Ptcp.ms | "How long [shall be] the vision [concerning] the daily, and the transgression of desolation…?" |
| Jer 47:5 [MT] / 47:6 [Eng frame] | עַד־מָתַי תִּתְגֹּודָדִי | Prep + Introg + Hithpael.Impf.2fs | "how long wilt thou cut thyself?" (sword-of-YHWH taunt) |

### 4. The Lock-and-Key Syntax: ʿaḏ-māṯay Question → ʿaḏ-X Answer

The distinctive apocalyptic deployment of ʿaḏ-māṯay is not the question *per se* but the **paired syntactic frame** in which the same preposition עַד recurs in the answer, binding question to answer across speaker turns. The question asks "until *when*?"; the answer supplies "until *X* [time-unit / event]." Parser-verified pairings:

| Question | Answer | Shared Preposition |
|----------|--------|--------------------|
| **Dan 8:13** עַד־מָתַי הֶחָזוֹן | **Dan 8:14** עַד עֶרֶב בֹּקֶר אַלְפַּיִם וּשְׁלֹשׁ מֵאוֹת | עַד … עַד |
| Isa 6:11a עַד־מָתַי אֲדֹנָי | Isa 6:11b עַד אֲשֶׁר אִם־שָׁאוּ עָרִים | עַד … עַד (אֲשֶׁר) |
| Zech 1:12 עַד־מָתַי אַתָּה לֹא־תְרַחֵם … זֶה שִׁבְעִים שָׁנָה | Zech 1:16 לָכֵן כֹּה־אָמַר יְהוָה שַׁבְתִּי | (answer in promise-oracle form) |

In Dan 8:13–14 the lock-and-key is at maximum tightness: no intervening narrative, direct speaker-turn, identical preposition עַד re-used as the head of the answer. The 2,300 evenings-mornings of Dan 8:14 is grammatically the **object of the question's interrogative adverb** — syntactically, v.14 *completes* v.13.

## Contrast with Related Forms

| Form | Function | Example |
|------|----------|---------|
| **עַד־מָתַי** | "until when?" (temporal endurance) | Dan 8:13; Psa 6:4 |
| **עַד־אָנָה** | "until whither / how long?" (variant, same function) | Psa 13:2; Hab 1:2 (MT) |
| **כַּמָּה** | "how much / how many?" (quantity, not duration) | 2 Sa 19:35; Job 13:23 |
| **מָתַי** alone | "when?" (simple temporal question, no endurance force) | Gen 30:30; Psa 42:3 "when shall I come and appear" |
| **לָמָּה / מַדּוּעַ** | "why?" (causal interrogative, not temporal) | Exo 5:22; Jer 12:1 |
| **עַד + noun** (declarative) | "until X" (endpoint of an action, no interrogation) | Dan 8:14 עַד עֶרֶב בֹּקֶר; Dan 7:25 עַד־עִדָּן וְעִדָּנִין וּפְלַג עִדָּן |

The **question-form עַד־מָתַי and the answer-form עַד + time-unit share the preposition עַד deliberately** — this is the grammatical hinge of apocalyptic time-prophecy. Cross-linked to [apocalyptic-time-unit-grammar](apocalyptic-time-unit-grammar.md) (the Dan 8:14 *ʿereḇ bōqer* counter itself) and [seal-command-syntax-daniel](seal-command-syntax-daniel.md) (the deferred-disclosure frame into which the answer is sealed).

## Distribution

- **28 occurrences** of מָתַי as `Introg` (hebrew_parser.py --lemma "מתי"; filter out proper-name homographs *Amittai* at 2Ki 14:25, Jon 1:1 and gentilic *Hamathite* at Gen 10:18)
- Concentrated in Psalms (7×: 6:4, 41:6, 74:10, 80:5, 82:2, 90:13, 94:3, 119:84), Jeremiah (5×: 4:14, 4:21, 12:4, 13:27, 23:26, 31:22, 47:5), and Daniel (1×: 8:13 — a single canonical occurrence, matching the one-time-only apocalyptic lock-and-key)
- Speakers: human sufferer (psalmists), YHWH (Exo 10:3; Num 14:27), prophet (Isa 6:11; Hab 2:6), angel (Zech 1:12; Dan 8:13), non-Israelite (Abner 2 Sa 2:26)

## Common Collocations in This Form

| Collocation | Pattern | Example |
|-------------|---------|---------|
| עַד־מָתַי + Divine-name vocative | interrogative + vocative | Psa 6:4 עַד־מָתָי + יְהוָה |
| עַד־מָתַי + PersPron.2 + Ptcp | interrogative + personal pronoun + participle | 1 Ki 18:21 עַד־מָתַי אַתֶּם פֹּסְחִים |
| עַד־מָתַי + Noun + Ptcp | interrogative + nominalized vision-object + descriptive participle | **Dan 8:13** עַד־מָתַי הֶחָזוֹן … שֹׁמֵם |
| Question עַד־מָתַי ‖ Answer עַד X | paired-preposition lock-and-key | Dan 8:13 ‖ 8:14; Isa 6:11a ‖ 6:11b |

---
*Generated from: hebrew_parser.py (--lemma "מתי", --verse "Dan 8:13", --verse "Dan 8:14", --verse "Psa 13:2"); KJV text D:/bible/tools/data/kjv.txt*
*Parser-verified references: Dan 8:13; 8:14; Psa 6:4; 13:2; 74:10; 80:5; 82:2; 94:3; Exo 10:3; 1 Ki 18:21; Isa 6:11; Hab 2:6; Zech 1:12; Jer 4:14; 23:26; 47:5*
*Last updated: 2026-04-19*
