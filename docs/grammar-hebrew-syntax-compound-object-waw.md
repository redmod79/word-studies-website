# Compound Object/Subject with Conjunction Waw (Hebrew)

## Definition

Biblical Hebrew routinely links two (or more) nominals into a single syntactic constituent by placing **וְ** between them. The resulting **compound phrase** — traditionally called a *coordinate phrase* — functions as **one slot** in the clause: one subject, one object, one complement. The predicate, modifier, preposition, or quantifier that governs the phrase distributes over **every** member. If two nouns joined by waw occupy the object slot of a verb, both are acted on; if they occupy the subject slot of a predicate nominal, the predicate is asserted of both; if a preposition precedes the first member, it reaches through the waw to the second unless repeated.

Three functions stand out in the data:

1. **Shared predicate (verbal or nominal)** — the verb/predicate acts on or is asserted of every conjunct equally.
2. **Shared modifier or quantifier** — an adjective, numeral, or participial attribute modifying the compound phrase modifies each member.
3. **Shared preposition / governing particle** — a single prep (with or without repetition) applies to all conjuncts.

This is distinct from the *clause-level* functions of waw documented in [syntax-waw-conjunction](syntax-waw-conjunction.md) (conjunctive-sequential, disjunctive, alternative, epexegetical). Those describe waw between **clauses or clause constituents**; this entry describes waw between **nominals inside a single phrase slot**.

## Form Recognition

- Morphology: **וְ** / **וּ** / **וָ** prefixed to the second (and any further) nominal of the group.
- Parser signature: `Conj.+NAN` (lemma `ו`) sitting between two nouns/adjectives/participles of the same grammatical category, with the ETCBC clause analyzer grouping them under a **single phrase function label** — e.g. `[Subj] X וְ Y`, `[Objc] X וְ Y`, `[Cmpl] X וְ Y`.
- Diagnostic: run `hebrew_parser.py --clause <ref>`. If the clause analyzer places both nouns under one `[Subj]` / `[Objc]` / `[Cmpl]` / `[PreC]` bracket, they form a compound constituent and share the clause's other slot-fillers.
- Number agreement of a governing verb is not decisive: Hebrew allows **singular agreement with the nearer conjunct** (Dan 8:13) or **plural agreement with the whole group** (Gen 2:25). Both patterns leave the compound-object semantics intact.
- The object marker **אֵת** and most prepositions are typically repeated before each conjunct (Gen 1:1 `אֵת… וְאֵת…`; Deu 6:5 `בְּ… וּבְ… וּבְ…`), but repetition is optional (Exo 20:11 drops אֵת before `הַיָּם`).

## Functions with Examples

### 1. Compound object — predicate acts on both members

| Reference | Hebrew (compound + predicate) | Parser analysis | KJV |
|-----------|-------------------------------|-----------------|-----|
| Gen 1:1 | אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ … בָּרָא | `[Pred] בָּרָא` + `[Objc] אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ` | "God created **the heaven and the earth**" |
| Exo 20:11 | אֶת־הַשָּׁמַיִם וְאֶת־הָאָרֶץ אֶת־הַיָּם וְאֶת־כָּל־אֲשֶׁר־בָּם … עָשָׂה | single Qal Perf `עָשָׂה` governing four conjuncts | "made **heaven and earth, the sea, and all that in them is**" |
| Dan 9:24 | לַחְתֹּם חָזוֹן וְנָבִיא | `[Pred] לַחְתֹּם` + `[Objc] חָזוֹן וְנָבִיא` (InfC clause) | "to seal up **the vision and prophecy**" |

In each case the Qal/Hiph perfect (or inf-con) discharges its action onto the **entire compound phrase** — not onto the first noun alone with the second added as afterthought. The clause-structure parser confirms this by bracketing both members under one `[Objc]` label.

### 2. Compound subject — predicate asserted of both members

| Reference | Hebrew (compound + predicate) | Parser analysis | KJV |
|-----------|-------------------------------|-----------------|-----|
| Gen 2:25 | וַיִּהְיוּ שְׁנֵיהֶם עֲרוּמִּים הָאָדָם וְאִשְׁתּוֹ | `[Subj] שְׁנֵיהֶם הָאָדָם וְאִשְׁתּוֹ` + `[PreC] עֲרוּמִּים` | "they were **both naked, the man and his wife**" |
| Dan 8:13 | וְקֹדֶשׁ וְצָבָא מִרְמָס | `[Subj] קֹדֶשׁ וְצָבָא` + `[PreC] מִרְמָס` (verbless NmCl) | "**the sanctuary and the host** to be trodden under foot" |
| Dan 9:24 | שָׁבֻעִים שִׁבְעִים נֶחְתַּךְ עַל עַמְּךָ וְעַל עִיר קָדְשֶׁךָ | `[Pred] נֶחְתַּךְ` + `[Cmpl] עַל עַמְּךָ וְעַל עִיר קָדְשֶׁךָ` | "determined upon **thy people and upon thy holy city**" |

**Dan 8:13 is the paradigm verbless-clause example.** The clause analyzer reports exactly two slots: `[Subj]` = `קֹדֶשׁ וְצָבָא` (compound subject of two coordinated masculine singular absolute nouns), and `[PreC]` = `מִרְמָס` (the predicate complement, "trampling / trodden ground"). The single predicate `מִרְמָס` is asserted of the whole compound subject; there is no grammatical mechanism by which it could attach to only the nearer noun. *Both* the sanctuary *and* the host are predicated as "trampling" — grammatically inseparable targets of the one trampling-state asserted by the nominal clause. (The identical pattern governs Gen 2:25 `עֲרוּמִּים` jointly predicated of Adam-and-his-wife, and Dan 9:24 `נֶחְתַּךְ` with its dual-prepositional complement `עַל עַמְּךָ וְעַל עִיר קָדְשֶׁךָ`.)

### 3. Shared modifier / quantifier over compound phrase

| Reference | Hebrew | Analysis | KJV |
|-----------|--------|----------|-----|
| Gen 2:25 | שְׁנֵיהֶם … הָאָדָם וְאִשְׁתּוֹ | numeral שְׁנֵיהֶם ("the two of them") scoping over both conjuncts | "**both** … the man and his wife" |
| Gen 1:14 | וְהָיוּ לְאֹתֹת וּלְמוֹעֲדִים וּלְיָמִים וְשָׁנִים | one copula + lamed-of-purpose distributing to four coordinate nouns | "let them be for **signs, and for seasons, and for days, and years**" |

### 4. Shared governing preposition

| Reference | Hebrew | Analysis | KJV |
|-----------|--------|----------|-----|
| Deu 6:5 | בְּכָל־לְבָבְךָ וּבְכָל־נַפְשְׁךָ וּבְכָל־מְאֹדֶךָ | preposition בְּ + quantifier כָל repeated before each conjunct; all three are complements of the single verb וְאָהַבְתָּ | "with **all thine heart, and with all thy soul, and with all thy might**" |
| Gen 14:19 | קֹנֵה שָׁמַיִם וָאָרֶץ | participle קֹנֵה governs bare compound `שָׁמַיִם וָאָרֶץ` (no repetition, no object-marker) | "possessor of **heaven and earth**" |

## Distributive Scope — the Load-Bearing Principle

When two nominals are joined by waw into a single phrase slot, **the predicate / modifier / preposition attaches to the phrase, not to the first member alone**. Grammatically, Hebrew has no construction that would allow a predicate to hit only the first conjunct of a coordinate subject while leaving the second conjunct outside the predication — the phrase is a unit by definition.

To say of `קֹדֶשׁ וְצָבָא` that only `קֹדֶשׁ` is "trampling" would require either (a) deleting the waw and making `צָבָא` a separate clause — which the Masoretic accentuation and ETCBC clause parse reject, or (b) repointing as a disjunctive waw splitting the constituent — unsupported by the clause analyzer and by any reference grammar treatment of Dan 8:13. Both members of the compound subject are within the predicate's scope; this is mechanical, not interpretive.

## Contrast with Related Forms

| Construction | Relation of terms | Example |
|--------------|-------------------|---------|
| **Compound phrase (waw-coordinate)** — this entry | Two independent nominals in parallel; each takes the predicate fully | Dan 8:13 `קֹדֶשׁ וְצָבָא מִרְמָס` |
| **Construct chain** — see [construct-state](construct-state.md) | Two nominals in head-modifier bond; only the head is predicated, the second qualifies the first | Dan 8:14 `קֹדֶשׁ` (implicit head) vs. Psa 20:3 `מִקְדָּשׁ` + construct |
| **Apposition** (no waw) | Second noun re-identifies the first; same referent | Gen 2:25 `שְׁנֵיהֶם הָאָדָם וְאִשְׁתּוֹ` — שְׁנֵיהֶם appositive to the compound |
| **Disjunctive waw between clauses** — see [syntax-waw-conjunction](syntax-waw-conjunction.md) | Waw between full clauses marking scene/participant break | Gen 3:1 `וְהַנָּחָשׁ הָיָה` |
| **Alternative/enumerative waw** ("or") — see [syntax-waw-conjunction](syntax-waw-conjunction.md) §3 | Waw in casuistic legal lists where conjuncts are mutually sufficient alternatives | Exo 21:15 `אָבִיו וְאִמּוֹ` |

Note the sharp contrast with the alternative-waw reading: casuistic-legal enumerative waw produces **mutual alternatives** (striking father *or* mother suffices for the penalty). Compound-phrase waw in narrative / vision / nominal-clause contexts produces **mutual inclusion** (sanctuary *and* host are both trampled). The two functions are distinguished by genre and clause type — not by morphology — and only the enumerative function is "either/or." The default reading of two nouns + waw in a verbless predicate-nominal clause (Dan 8:13) is inclusive-coordinate.

## Parser Verification Workflow

1. `hebrew_parser.py --verse <ref>` — confirms both nominals carry the same part-of-speech / state so they can coordinate.
2. `hebrew_parser.py --clause <ref>` — confirms the ETCBC parser groups them under a **single** phrase-function bracket (`[Subj]`, `[Objc]`, `[Cmpl]`, `[PreC]`).
3. If a single bracket contains `X וְ Y`, the predicate / modifier of that clause distributes to both.

---

*Generated from: `hebrew_parser.py --verse`, `--clause`; ETCBC BHSA phrase-function tagging.*
*Reference grammars: Waltke–O'Connor §§4.5, 39.2.1; GKC §§146, 154a; Joüon–Muraoka §150.*
*Last updated: 2026-04-20*
