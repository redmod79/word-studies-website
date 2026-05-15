# Grammar Analysis: Psalm 75:8 (MT 75:9)

> **Versification note:** English Psalm 75:8 = Hebrew (MT) Psalm 75:9. The Hebrew parser uses MT numbering. This entry refers to the English reference "Psalm 75:8" throughout, which is the same verse as Hebrew 75:9.

## Text

**Hebrew (MT 75:9):**
כִּ֤י כֹ֪וס בְּֽיַד־יְהוָ֡ה וְיַ֤יִן חָמַ֨ר ׀ מָ֥לֵא מֶסֶךְ֮ וַיַּגֵּ֢ר מִ֫זֶּ֥ה אַךְ־שְׁ֭מָרֶיהָ יִמְצ֣וּ יִשְׁתּ֑וּ כֹּ֝֗ל רִשְׁעֵי־אָֽרֶץ׃

**KJV (Psalm 75:8):**
"For in the hand of the LORD [there is] a cup, and the wine is red; it is full of mixture; and he poureth out of the same: but the dregs thereof, all the wicked of the earth shall wring [them] out, [and] drink [them]."

## Word-by-Word Parsing

| #  | Hebrew        | Lemma  | Parsing                   | Gloss          |
|----|---------------|--------|---------------------------|----------------|
| 1  | כִּ֤י         | כי     | Conj.                     | for / that     |
| 2  | כֹ֪וס         | כוס    | Noun.fs.Abs               | cup            |
| 3  | בְּֽ          | ב      | Prep                      | in             |
| 4  | יַד           | יד     | Noun.s.Cst                | hand (of)      |
| 5  | יְהוָ֡ה       | יהוה   | PropN.ms.Abs              | YHWH           |
| 6  | וְ            | ו      | Conj.                     | and            |
| 7  | יַ֤יִן        | יין    | Noun.ms.Abs               | wine           |
| 8  | חָמַ֨ר        | חמר    | Verb.Qal.Perf.3ms         | foamed/red     |
| 9  | מָ֥לֵא        | מלא    | Adj.ms.Abs                | full           |
| 10 | מֶסֶךְ֮       | מסך    | Noun.ms.Abs               | mixture        |
| 11 | וַ            | ו      | Conj. (wayyiqtol)         | and            |
| 12 | יַּגֵּ֢ר      | נגר    | Verb.Hiphil.Wayq.3ms      | he pours out   |
| 13 | מִ֫           | מן     | Prep                      | from           |
| 14 | זֶּ֥ה         | זה     | DemPron.ms                | this           |
| 15 | אַךְ          | אך     | Adv.                      | surely / only  |
| 16 | שְׁ֭מָרֶיהָ   | שׁמר   | Noun.mp.Abs.+3fs          | its dregs      |
| 17 | יִמְצ֣וּ      | מצה    | Verb.Qal.Impf.3mp         | they drain     |
| 18 | יִשְׁתּ֑וּ    | שׁתה   | Verb.Qal.Impf.3mp         | they drink     |
| 19 | כֹּ֝֗ל        | כל     | Noun.ms.Cst               | all (of)       |
| 20 | רִשְׁעֵי      | רשׁע   | Adj.mp.Cst                | wicked (of)    |
| 21 | אָֽרֶץ        | ארץ    | Noun.s.Abs                | earth          |

## Clause Structure

Six clauses (parser output):

1. **NmCl (Nominal clause, discourse Q):** כִּ֤י כֹ֪וס בְּֽיַד־יְהוָ֡ה — "For [there is] a cup in YHWH's hand."
   - [Conj] כִּי — [Subj] כוס — [PreC] בְּיַד־יְהוָה
   - Verbless nominal clause; the existence/possession of the cup is predicated by the prepositional phrase "in the hand of YHWH."

2. **WXQt (Waw + X + Qatal, circumstantial):** וְיַ֤יִן חָמַ֨ר — "and the wine foams/is red."
   - [Conj] וְ — [Subj] יין — [Pred] חמר (Qal perfect 3ms)
   - Waw-X-qatal with fronted subject — classic circumstantial/descriptive clause attached to the nominal clause above. See [syntax-wx-qatal-circumstantial.md](../hebrew/syntax-wx-qatal-circumstantial.md).

3. **NmCl (Nominal clause):** מָ֥לֵא מֶסֶךְ֮ — "[it is] full of mixture."
   - [PreC] מָלֵא מֶסֶךְ
   - Verbless; the adjective מָלֵא "full" governs an accusative of material מֶסֶךְ "mixture/mixed wine."

4. **Way0 (Wayyiqtol, discourse N = narrative):** וַיַּגֵּ֢ר מִ֫זֶּ֥ה — "and he pours from it."
   - [Conj] וַ — [Pred] יַגֵּר (Hiphil wayyiqtol 3ms) — [Cmpl] מִזֶּה
   - A single wayyiqtol inside otherwise Q-domain discourse: narrative-style advancement portraying YHWH's act of pouring as the next event in the scene.

5. **xYq0 (X + Yiqtol, object-fronted):** אַךְ־שְׁ֭מָרֶיהָ יִמְצ֣וּ — "surely its dregs they shall drain."
   - [Objc] אַךְ שְׁמָרֶיהָ — [Pred] יִמְצוּ
   - Object fronted for emphasis; the dregs themselves — and not merely the wine — are what the wicked will drain.

6. **ZYqX (Yiqtol + subject):** יִשְׁתּ֑וּ כֹּ֝֗ל רִשְׁעֵי־אָֽרֶץ — "they shall drink — all the wicked of the earth."
   - [Pred] יִשְׁתּוּ — [Subj] כֹּל רִשְׁעֵי אָרֶץ
   - The heavy subject phrase is postposed, producing a climactic reveal of who must drink.

## Construct Chains

The parser identifies two construct chains:

1. **יַד־יְהוָה** — "hand of YHWH"
   - יַד (cst) → יְהוָה (abs)
   - Possessive/agency genitive. The cup belongs to YHWH and is wielded by him.

2. **כֹּל רִשְׁעֵי־אָרֶץ** — "all the wicked of the earth"
   - כֹּל (cst) → רִשְׁעֵי (cst) → אָרֶץ (abs)
   - Three-member chain: quantifier + adjective-used-as-substantive + earth. Universalizes the scope — not just one nation but every wicked person on earth.

See [construct-state.md](../hebrew/construct-state.md).

## Key Grammatical Features

### 1. כּוֹס בְּיַד־יְהוָה — Verbless nominal clause with possessive prep-phrase

- **Form:** Noun (subject) + prep + construct noun + proper noun (predicate). No verb "to be" — existence/possession is asserted by juxtaposition.
- **Significance:** The opening clause establishes a tableau, not a narrated event. The cup already exists; it is already in YHWH's hand. The verse opens in a static visionary frame before any action takes place. This is the founding image that later prophetic texts pick up (Jer 25:15; Isa 51:17, 22; Rev 14:10; 16:19) — always the cup is already *there*, held by God, waiting.
- **Grammar reference:** verbless/nominal clauses — no dedicated entry yet in the library; see the general clause treatment.

### 2. וְיַיִן חָמַר — Waw-X-qatal circumstantial clause

- **Form:** Waw-conjunctive + fronted subject יין + Qal perfect 3ms חָמַר. The perfect of חמר ("foam up, ferment, turn red") describes a resultant state rather than a completed past action. Fronting the subject makes the clause circumstantial: it does not advance time but describes the condition of the wine at the scene of the nominal clause.
- **Significance:** The wine is already fermented/red. חמר carries connotations both of redness (color) and of foaming/effervescence (strong, undiluted, potent). The perfect portrays this as an achieved state — this is no new-pressed grape juice but aged, active, dangerous wine. The circumstantial syntax ties this description directly to the cup of clause 1: the cup contains *this* wine.
- **Grammar reference:** [syntax-wx-qatal-circumstantial.md](../hebrew/syntax-wx-qatal-circumstantial.md)
- **Word study:** [H3196-yayin.md](../../word-studies/H3196-yayin.md)

### 3. מָלֵא מֶסֶךְ — Adjective + accusative of material

- **Form:** Verbless clause with predicate adjective מָלֵא ("full") taking מֶסֶךְ ("mixture") as accusative specifying what fills it. מֶסֶךְ denotes wine mixed with spices or other additives — a potent preparation, not wine diluted with water.
- **Significance:** The image intensifies: the cup is full, and full of *mesek* — a compound drink prepared for maximum potency. In Prov 23:30 מֶסֶךְ is the "mixed wine" that inebriates. Combined with חָמַר in the prior clause, the wine is doubly strong: fermented *and* spiced. The founding cup-of-wrath metaphor here is not a casual drink but a carefully prepared draught.

### 4. וַיַּגֵּר — Hiphil wayyiqtol 3ms of נגר

- **Form:** Waw-consecutive + Hiphil imperfect/preterite 3ms of נגר ("pour, run down"). The Hiphil is causative: "he causes (it) to pour out." Wayyiqtol advances discourse by one step.
- **Significance:** This is the one event-verb in the first half of the verse. Three stative/descriptive clauses establish the scene (cup in hand, wine red, full of mixture), then one wayyiqtol breaks in: *and he pours*. The stem is causative — YHWH is the agent, actively tilting the cup. The wayyiqtol inside a Q (discourse/direct-speech) domain is marked: the poet momentarily slips into narrative voice to report the pouring as it happens.
- **Grammar reference:** [stem-hiphil.md](../hebrew/stem-hiphil.md), [hiphil-imperfect.md](../hebrew/hiphil-imperfect.md)

### 5. אַךְ־שְׁמָרֶיהָ יִמְצוּ — Object-fronted yiqtol with emphatic אַךְ

- **Form:** Restrictive/asseverative particle אַךְ + object שְׁמָרֶיהָ ("its dregs," fem-plural + 3fs suffix referring back to כּוֹס) + Qal imperfect 3mp יִמְצוּ ("they will drain"). The object is fronted before the verb for emphasis.
- **Significance:** The object-fronting + אַךְ stacks two marks of emphasis. The point is not merely that the wicked will drink the wine, but that *only the dregs* — or *even the dregs* — will be what they get. The 3fs suffix "her/its" (referring to the feminine noun כּוֹס) binds the dregs back to the cup of clause 1. Grammatically, everything hangs together: one cup, one wine, one pouring, one set of dregs — for all the wicked of the earth.

### 6. יִשְׁתּוּ כֹּל רִשְׁעֵי־אָרֶץ — Yiqtol + postposed heavy subject

- **Form:** Qal imperfect 3mp יִשְׁתּוּ followed by the three-member construct chain כֹּל רִשְׁעֵי־אָרֶץ. The subject is positioned *after* the verb — marked word order; normal X-Yiqtol would front the subject.
- **Significance:** Postposing the subject creates a climactic closure. The verse ends with the identification of who drinks: "all the wicked of the earth." The three-member construct chain universalizes scope — not just one nation's wicked, but the totality of earthly wickedness. This sets the template picked up by later prophets (Jer 25:15–29 names nation after nation) and by Revelation 14:10 where the wicked drink "the wine of the wrath of God."

## Cross-References

### Grammar library

- [syntax-wx-qatal-circumstantial.md](../hebrew/syntax-wx-qatal-circumstantial.md) — circumstantial perfect clauses
- [stem-hiphil.md](../hebrew/stem-hiphil.md) — causative stem (for וַיַּגֵּר)
- [hiphil-imperfect.md](../hebrew/hiphil-imperfect.md) — Hiphil imperfect/wayyiqtol
- [construct-state.md](../hebrew/construct-state.md) — construct chains (יַד־יְהוָה, כֹּל רִשְׁעֵי־אָרֶץ)
- [qal-imperfect.md](../hebrew/qal-imperfect.md) — Qal imperfect (יִמְצוּ, יִשְׁתּוּ)
- [syntax-waw-conjunction.md](../hebrew/syntax-waw-conjunction.md) — waw usage

### Word studies

- [H3563-kowc.md](../../word-studies/H3563-kowc.md) — כּוֹס "cup"
- [H3196-yayin.md](../../word-studies/H3196-yayin.md) — יַיִן "wine"
- [TR-yayin-oinos.md](../../word-studies/TR-yayin-oinos.md) — translation pairing

### Gaps identified (candidates for future library entries)

- **חָמַר (Qal perfect, stative "ferment/red")** — no current entry; would be useful for Deut 32:14, Isa 27:2, Ps 46:4, 75:9.
- **מֶסֶךְ "mixed wine"** — noun not yet studied; parallel to the fuller word-family covering mixture/drink preparation.
- **אַךְ as restrictive/asseverative particle** — no dedicated entry; governs nuance across Pss, Prov, Job.
- **Object-fronting with yiqtol for emphasis** — the xYq0 pattern deserves a standalone grammar reference entry.
- **Verbless/nominal clauses with prep-phrase predicate** — basic enough that one canonical entry would serve many passages.

## Summary

Psalm 75:8 (MT 75:9) is built from six short clauses in a deliberate grammatical rhythm: three scene-setting descriptive clauses (NmCl, WXQt, NmCl), one narrative-advancing wayyiqtol (Way0), and two future-oriented yiqtol clauses with marked word order (xYq0, ZYqX). The grammatical movement mirrors the theological movement: a static cup in YHWH's hand → its description intensifies (red, full, spiced) → YHWH pours → the wicked drain the dregs → *all* of them drink. The founding cup-of-wrath image of the Hebrew Bible is grammatically packaged as a visionary tableau that suddenly breaks into action, aimed universally at "all the wicked of the earth."
