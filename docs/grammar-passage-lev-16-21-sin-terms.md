# Grammar Analysis: Leviticus 16:21 Coordinated Sin Terms

## Text

**Hebrew:** וְסָמַ֨ךְ אַהֲרֹ֜ן אֶת־שְׁתֵּ֣י יָדָ֗יו עַ֨ל רֹ֣אשׁ הַשָּׂעִיר֮ הַחַי֒ וְהִתְוַדָּ֣ה עָלָ֗יו אֶת־כָּל־עֲוֹנֹת֙ בְּנֵ֣י יִשְׂרָאֵ֔ל וְאֶת־כָּל־פִּשְׁעֵיהֶ֖ם לְכָל־חַטֹּאתָ֑ם וְנָתַ֤ן אֹתָם֙ עַל־רֹ֣אשׁ הַשָּׂעִ֔יר וְשִׁלַּ֛ח בְּיַד־אִ֥ישׁ עִתִּ֖י הַמִּדְבָּֽרָה׃

**KJV:** And Aaron shall lay both his hands upon the head of the live goat, and confess over him all the iniquities of the children of Israel, and all their transgressions in all their sins, putting them upon the head of the goat, and shall send [him] away by the hand of a fit man into the wilderness:

## Word-by-Word Parsing: Confession Clause

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | וְ | ו | Conj.+NAN | and |
| 2 | הִתְוַדָּה | ידה | Verb.Hithpael.Perf.3ms | confess/praise |
| 3 | עָלָיו | על | Prep.+3ms | upon him |
| 4 | אֶת | את | Prep | object marker |
| 5 | כָּל | כל | Noun.ms.Cst | all/whole |
| 6 | עֲוֹנֹת | עון | Noun.mp.Cst | iniquities |
| 7 | בְּנֵי | בן | Noun.mp.Cst | sons of |
| 8 | יִשְׂרָאֵל | ישׂראל | PropN.s.Abs.+NAN | Israel |
| 9 | וְ | ו | Conj.+NAN | and |
| 10 | אֶת | את | Prep | object marker |
| 11 | כָּל | כל | Noun.ms.Cst | all/whole |
| 12 | פִּשְׁעֵיהֶם | פשׁע | Noun.mp.Abs.+3mp | their transgressions |
| 13 | לְ | ל | Prep | to/with respect to |
| 14 | כָל | כל | Noun.ms.Cst | all/whole |
| 15 | חַטֹּאתָם | חטאת | Noun.fp.Abs.+3mp | their sins |

## Key Grammatical Features

### 1. הִתְוַדָּה עָלָיו

- **Form:** Hithpael perfect 3ms of ידה with preposition עַל + 3ms suffix.
- **Significance:** The clause describes confession "over/upon him." The prepositional complement marks the ritual target/location of the spoken confession.
- **Grammar reference:** no Hithpael stem entry exists yet.

### 2. אֶת־כָּל־עֲוֹנֹת בְּנֵי יִשְׂרָאֵל

- **Form:** object marker אֶת + construct sequence כָּל עֲוֹנֹת בְּנֵי יִשְׂרָאֵל.
- **Significance:** כָּל is in construct before עֲוֹנֹת, and עֲוֹנֹת is construct before בְּנֵי יִשְׂרָאֵל. The whole phrase functions as the first direct object component of הִתְוַדָּה.
- **Grammar reference:** [construct-state](../hebrew/construct-state.md)
- **Word study:** [H5771-avon](../../word-studies/H5771-avon.md)

### 3. וְאֶת־כָּל־פִּשְׁעֵיהֶם

- **Form:** waw + repeated object marker אֶת + construct כָּל + absolute noun with 3mp suffix.
- **Significance:** Repeating אֶת marks a second coordinated direct-object component. The suffix on פִּשְׁעֵיהֶם binds the term to the same plural group already named as "children of Israel."
- **Grammar reference:** [syntax-compound-object-waw](../hebrew/syntax-compound-object-waw.md); [construct-chain-suffix](../hebrew/construct-chain-suffix.md)
- **Word study:** [H6588-pesha](../../word-studies/H6588-pesha.md)

### 4. לְכָל־חַטֹּאתָם

- **Form:** לְ + construct כָּל + absolute noun חַטֹּאתָם with 3mp suffix.
- **Significance:** The third sin term is introduced by לְ rather than אֶת. Grammatically it is attached to the object complex as a complement, "with respect to / according to / in all their sins." It does not erase the two previous direct-object components.
- **Grammar reference:** [construct-state](../hebrew/construct-state.md)
- **Word study:** [H2403-chattaah](../../word-studies/H2403-chattaah.md)

### 5. Repeated כָּל

- **Form:** כָּל appears three times, each in construct: כָּל־עֲוֹנֹת, כָּל־פִּשְׁעֵיהֶם, כָל־חַטֹּאתָם.
- **Significance:** The repetition distributes totality across each sin term separately. Grammatically, it is not one כָּל governing a three-item list; each term receives its own quantifier.
- **Grammar reference:** [construct-state](../hebrew/construct-state.md)

## Clause Structure

Clause parser output for the confession clause:

| Slot | Hebrew |
|------|--------|
| Conj | וְ |
| Pred | הִתְוַדָּה |
| Cmpl | עָלָיו |
| Objc | אֶת כָּל עֲוֹנֹת בְּנֵי יִשְׂרָאֵל וְ אֶת כָּל פִּשְׁעֵיהֶם לְ כָל חַטֹּאתָם |

The parser treats the full sin-term sequence as one object phrase under הִתְוַדָּה, with internal coordination and complementing.

## Construct Chains

| Chain | Parser Result | Function |
|-------|---------------|----------|
| כָּל עֲוֹנֹת בְּנֵי יִשְׂרָאֵל | construct + construct + construct + absolute | quantified iniquities belonging to Israel's sons |
| כָּל פִּשְׁעֵיהֶם | construct + absolute with 3mp suffix | quantified transgressions belonging to them |
| כָל חַטֹּאתָם | construct + absolute with 3mp suffix | quantified sins belonging to them |

## Cross-References

- **Grammar library:** [construct-state](../hebrew/construct-state.md); [construct-chain-suffix](../hebrew/construct-chain-suffix.md); [syntax-compound-object-waw](../hebrew/syntax-compound-object-waw.md)
- **Word studies:** [H5771-avon](../../word-studies/H5771-avon.md); [H6588-pesha](../../word-studies/H6588-pesha.md); [H2403-chattaah](../../word-studies/H2403-chattaah.md)

---
*Generated from: hebrew_parser.py --verse/--clause/--construct Lev 16:21 and lemma searches for עון, פשׁע, חטאת*
*Last updated: 2026-05-07*
