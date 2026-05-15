# Pronominal Suffix on the Absolute Noun of a Construct Chain (Hebrew)

## Definition

A construct chain (*sǝmîkût*) binds two (or more) nouns into a single grammatical phrase in which only the **final (absolute)** noun can carry definite articles, adjectives, or **pronominal suffixes**. The construct-head noun loses stress-autonomy and takes a shortened ("construct state") form; the absolute noun keeps its full form. When a possessive pronominal suffix (e.g., 3ms -ô / -hû) attaches to the absolute noun, the possessor semantically scopes over the **entire compound**, not just the word it is suffixed to.

1. **Whole-phrase possession** — suffix on the absolute binds the whole construct chain to the possessor: *mǝḵôn miqdāšô* "establishment-place of-his-sanctuary" = "the site of his sanctuary" (the whole site-of-sanctuary belongs to "him").
2. **Attributive-genitive specification** — construct + absolute-with-suffix often renders an English adjective + possessive: *šēm qodšô* "name of his-holiness" = "his holy name."
3. **Structural necessity** — since the construct head cannot itself carry a suffix, the absolute is the **only legal attachment point** for a possessor inside a construct chain.

## Form Recognition

- Construct-head noun: shortened vowels, no article, no suffix of its own; parser tag **`Noun.X.Cst`** (where X = gender/number).
- Absolute noun with possessor: full form + suffix morpheme; parser tag **`Noun.X.Abs.+Nxx`** (e.g. `+3ms`, `+2ms`, `+1us`).
- The two nouns stand adjacent with no intervening article, preposition, or conjunction.
- 3ms suffix allomorphs on singular masculine nouns:
  - **-ô** (written וֹ, sometimes defective ֹ) — most common: *miqdāšô*, *qodšô*, *bêṯô*.
  - **-hû** (הוּ) — used mostly after certain vowel-final stems or III-weak roots, and on segolate plurals; same meaning.
- Other suffixes that attach the same way: 1cs -î, 2ms -kā / -eḵā, 2fs -ēḵ, 1cp -ēnû, 2mp -ḵem, 3mp -ām / -êhem.
- **Parser search:** `sp=subs st=c` (construct state) typically adjacent to `sp=subs st=a` with `+3ms` (or other pronominal feature).

## Functions with Examples

### 1. Whole-phrase possession ("the X of Y of his")

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Dan 8:11 | מְכֹ֥ון מִקְדָּשֹֽׁו | Noun.ms.**Cst** מכון + Noun.ms.**Abs.+3ms** מקדשׁ | "the place of his sanctuary" |
| Gen 24:2 | זְקַ֣ן בֵּיתֹ֔ו | Adj.ms.**Cst** זקן + Noun.ms.**Abs.+3ms** בית | "eldest servant of his house" (lit. "elder of his house") |

Dan 8:11 is the paradigm case: the suffix -ô sits on the absolute *miqdāš* but the possession ("his") applies to the whole compound — it is "his [place-of-sanctuary]," not "the place of [his sanctuary-as-separate-entity]." The construct head *mǝḵôn* is ungrammatical as a host for the suffix and so the possessor **must** attach to the absolute.

### 2. Attributive-genitive yielding English adjective + possessive

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Psa 103:1 | שֵׁ֥ם קָדְשֹֽׁו | Noun.ms.**Cst** שׁם + Noun.ms.**Abs.+3ms** קדשׁ | "his holy name" (lit. "name of his holiness") |

The same whole-phrase rule operates, but because the absolute *qōdeš* "holiness" is an abstract quality-noun, the idiomatic English rendering converts the construct-chain-plus-suffix into **possessive + adjective** ("his holy name"). KJV consistently smooths these out; the Hebrew literally says "name of his-holiness."

### 3. Multi-level chains — suffix still on the final absolute

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Psa 26:8 | מְקֹ֗ום מִשְׁכַּ֥ן כְּבֹודֶֽךָ | Noun.ms.Cst מקום + Noun.ms.**Cst** משׁכן + Noun.s.**Abs.+2ms** כבוד | "the place where thine honour dwelleth" (lit. "place of dwelling of thy glory") |
| Exo 15:17 | הַ֣ר נַחֲלָֽתְךָ֔ | Noun.ms.**Cst** הר + Noun.fs.**Abs.+2ms** נחלה | "the mountain of thine inheritance" |

A chain of two constructs + one absolute still obeys the rule: only the **final** noun is absolute, and the suffix (here 2ms -ḵā / -eḵā) attaches there and scopes over the whole phrase. This demonstrates that the rule is structural ("suffix on the chain-final absolute") rather than lexical.

## Contrast: Suffix on Construct-Head vs. Suffix on Absolute

A suffix **on the construct head** is morphosyntactically ill-formed in Standard Biblical Hebrew — a noun in the construct state has relinquished its independent nominal marking. Therefore the distinction is not between two legal options but between **the only legal placement** (on the absolute) and an ungrammatical one.

| Pattern | Status | Example / Note |
|---------|--------|----------------|
| Cst + Abs-with-suffix | **Standard** | Dan 8:11 *mǝḵôn miqdāšô*; Psa 103:1 *šēm qodšô* |
| Abs-with-suffix alone (no chain) | Standard, but different construction | Gen 24:2 עַבְדֹּו֙ "his servant" (single noun, Noun.ms.Abs.+3ms) |
| Suffixed noun + following noun in apposition | Different construction | *ʿaḇdô zǝqan bêṯô* Gen 24:2 "his servant, the elder of his house" — the suffix on *ʿaḇdô* does **not** bind the following chain *zǝqan bêṯô* |
| Suffix on construct-head noun | Ungrammatical | Not attested in standard prose |

The upshot: whenever Hebrew needs to say "his X-of-Y," it places the suffix on **Y** (the absolute), and competent reading must re-scope the possessor back over the whole chain.

## Suffix Morphology (3ms focus)

The 3ms suffix has two principal allomorphs distributed by the stem-shape of the host:

| Allomorph | Host shape | Examples |
|-----------|-----------|----------|
| **-ô** (written וֹ or defective ֹ) | Most singular masculine nouns; consonant-final stems | *miqdāšô* מִקְדָּשׁוֹ Dan 8:11; *qodšô* קָדְשׁוֹ Psa 103:1; *bêṯô* בֵּיתוֹ Gen 24:2; *ʿaḇdô* עַבְדּוֹ Gen 24:2 |
| **-hû** (הוּ) | After long-vowel-final segolates in some forms; certain III-weak stems; poetic | *pîhû* פִּיהוּ "his mouth"; with plural-masc.-pl. construct: *ʿǎḇāḏāw* עֲבָדָיו "his servants" uses the collapsed -āyw written form |
| **-āw / -āyw** (יו) | Masc. plural absolute stems (-îm) with 3ms | *yāḏāw* יָדָיו "his hands"; *pānāw* פָּנָיו "his face" |

In a construct chain, the suffix remains unchanged — the host noun *miqdāš* is singular masculine, so it takes **-ô**; the construct-head noun (*mǝḵôn*) is simply not involved.

## Cross-References

- Construct chain as a syntactic skeleton → see Joüon-Muraoka §129; GKC §128; Waltke-O'Connor IBHS §9.
- Suffix paradigms → GKC §91; Joüon §94; BHRG §25.
- Related grammar entries in this library: [pluralis-majestatis](pluralis-majestatis.md) (some construct-head nouns such as אֲדֹנָיו bear the same morphology but encode single-referent honorifics), [ben-adam-vocative-construct](ben-adam-vocative-construct.md) (construct chain where the absolute does **not** carry a suffix — semantic contrast-point), [corporate-solidarity](corporate-solidarity.md) (*bêṯ* + PropN construct + 3ms suffix at 1Ki 21:29 עַל־בֵּיתוֹ — distinct because the "possessor" is the house itself, not a further name).

## Parser Diagnostic

`hebrew_parser.py --verse "Dan 8:11"` returns:

```
מְכֹ֥ון         Noun.ms.Cst               site
מִקְדָּשֹֽׁו    Noun.ms.Abs.+3ms          sanctuary
```

The adjacent `Cst` → `Abs.+Nxx` pattern is the signature of this construction. When reading such a pair, treat the possessor as binding the **entire compound**, not only the absolute.

---

*Examples verified via `hebrew_parser.py --verse` for Dan 8:11, Psa 103:1, Psa 26:8, Exo 15:17, Gen 24:2.*
*Last updated: 2026-04-20*
