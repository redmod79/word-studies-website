# Pluralis Majestatis / Plural of Majesty (Hebrew)

## Definition

A morphologically plural noun (masculine *-îm* or, more rarely, feminine *-ôt*) used of a **single referent** to intensify, honor, or sum up the totality of that referent's qualities. Also called **plural of excellence**, **plural of intensification**, **honorific plural**, or **intensive plural**. Gesenius (GKC §124g) classifies it as a subspecies of the **abstract plural**: "the *pluralis excellentiae* or *maiestatis*… is properly a variety of the abstract plural, since it sums up the several characteristics belonging to the idea, besides possessing the secondary sense of an intensification of the original idea" (p.362). It is **not** a plural of number — the referent is one.

1. **Plural of majesty / excellence** — a single exalted referent (God, a lord, a master, a great beast) is expressed in the plural to signal greatness, completeness, or dignity.
2. **Plural of intensification** — the plural amplifies inherent qualities rather than counting members.
3. **Honorific plural** — a plural of address or reference applied to humans or God to convey respect (Waltke-O'Connor §7.4.3).

## Form Recognition

- Morphologically a standard masculine plural (*-îm*) or feminine plural (*-ôt*) noun.
- **The parser tags it as plural** (`Noun.mp.Abs` / `Noun.fp.Abs`) — morphology alone cannot distinguish it from a plural of number.
- Four contextual signals mark the majestic reading:
  1. **Singular verb agreement** with the plural noun as subject (GKC §145h, §132h).
  2. **Singular adjective/attribute agreement** (GKC §132h; e.g. `אֱלֹהִים צַדִּיק` "righteous God," Ps 7:12 [Eng 7:11]).
  3. **Singular pronominal suffix** or singular resumption in context.
  4. **Referent is unambiguously one individual** (context, narrative, naming).
- **Parser query:** no direct feature code — search plural nouns and inspect verb/attribute agreement and referent context.

## Functions with Examples

### 1. Deity: אֱלֹהִים of the God of Israel

Waltke-O'Connor §7.4.3b: "Most honorific plurals in the Bible involve the God of Israel, and the most common of these is *ʾĕlōhîm*, used about twenty-five hundred times. When used of the God of Israel, this term usually takes singular agreement."

| Reference | Hebrew | Parsing | Agreement signal |
|-----------|--------|---------|------------------|
| Gen 1:1 | בָּרָ֣א אֱלֹהִ֑ים | `Verb.Qal.Perf.3ms` + `Noun.mp.Abs` | singular verb with plural subject |
| Ps 7:12 (MT; Eng 7:11) | אֱ֭לֹהִים שֹׁופֵ֣ט צַדִּ֑יק | `Noun.mp.Abs` + `Ptcp.ms` + `Adj.ms.Abs` | singular participle + singular adjective |

### 2. Human lords/masters: אָדוֹן (H113) / אֲדֹנָי (H136)

GKC §124i (p.419): "plurals which have a singular meaning… especially the *pluralis excellentiae* or *maiestatis*… אֲדֹנִים master, Ex 21:4." Waltke-O'Connor p.155–156 lists `קְדוֹשִׁים` "Holy One" and `אֲדֹנִים` "Lord" as further honorific plurals for God, noting the honorific use of `אָדוֹן` in the singular or plural for "a divine or human lord."

| Reference | Hebrew | Parsing | Referent |
|-----------|--------|---------|----------|
| Exo 21:4 | אֲדֹנָיו֙ יִתֶּן־לֹ֣ו אִשָּׁ֔ה | `Noun.mp.Abs.+3ms` subject + `Verb.Qal.Impf.3ms` | one master (singular verb `yittēn`) |
| Exo 21:4 | לַֽאדֹנֶ֔יהָ | `Noun.mp.Abs.+3fs` | her one master |

### 3. Owner / master: בַּ֫עַל (H1167) as intensive plural

GKC §124i also lists `בְּעָלִים` "master, owner" at Ex 21:29.

| Reference | Hebrew | Parsing | Referent |
|-----------|--------|---------|----------|
| Exo 21:29 | בִּבְעָלָיו֙ … בְּעָלָ֖יו יוּמָֽת | `Noun.mp.Abs.+3ms` + `Verb.Hophal.Impf.3ms` | one ox-owner (singular "he shall be put to death") |

Contrast with the genuine numerical plural `הַבְּעָלִים` "the Baalim" at Jdg 2:11 (`Verb.Qal.Wayq.3mp` + plural referent — Israel served *multiple* local Baals).

### 4. Great beast: בְּהֵמוֹת (H930) — feminine-plural form, single creature

Waltke-O'Connor §7.4.2 (p.153–154): "Two of the great monsters in the Bible are designated with intensive plurals" — Leviathan-like entities whose sheer size/menace is lexicalized as a plural. `בְּהֵמוֹת` looks like a feminine plural of `בְּהֵמָה` "beast" but functions here as a singular name for one colossal creature.

| Reference | Hebrew | Parsing | Agreement signal |
|-----------|--------|---------|------------------|
| Job 40:15 | בְ֭הֵמֹות אֲשֶׁר־עָשִׂ֣יתִי עִמָּ֑ךְ … יֹאכֵֽל | `Noun.mp.Abs` + `Verb.Qal.Impf.3ms` `yōʾkēl` "he eats" | singular masculine verb though noun is fem-pl form |

## Distinction from Plural of Number

The same form (*-îm*) can mark either function; **only context and agreement disambiguate**.

| Feature | Plural of Number | Plural of Majesty |
|---------|------------------|-------------------|
| Referent count | many | one |
| Verb agreement | plural (`3mp`/`3fp`) | usually singular (`3ms`/`3fs`) |
| Attribute agreement | plural adjective | singular adjective |
| Example (Elohim) | Ex 12:12 "gods of Egypt" (plural referent) | Gen 1:1 "God created" (`bārāʾ` 3ms) |
| Example (Baal) | Jdg 2:11 `הַבְּעָלִים` served (`wayyaʿabdû` 3mp) | Exo 21:29 ox's `בְּעָלָיו` (`yûmāt` 3ms) |
| Example (Adonim) | "masters" as multiple people | Exo 21:4 one master (`yittēn` 3ms) |

GKC §132h: "plurals which have a singular meaning are frequently construed with the singular, especially the *pluralis excellentiae* or *maiestatis*."

## How Singular Verb Agreement Signals the Majestic Plural

The strongest morphosyntactic diagnostic is **grammatical concord asymmetry**: a morphologically plural noun paired with a **singular finite verb and/or singular attribute**. This concord mismatch is the textbook footprint of the *pluralis majestatis*:

- Gen 1:1 `אֱלֹהִים בָּרָא` — `Noun.mp` + `Verb.Qal.Perf.3ms` → singular-verb agreement signals one referent (God), despite plural noun.
- Exo 21:4 `אֲדֹנָיו יִתֶּן` — `Noun.mp.+3ms` + `Verb.Qal.Impf.3ms` → one master.
- Exo 21:29 `בְּעָלָיו … יוּמָת` — `Noun.mp.+3ms` + `Verb.Hophal.Impf.3ms` → one owner.
- Job 40:15 `בְהֵמֹות … יֹאכֵל` — fem-pl form + `3ms` verb → one beast.

GKC §145h explicitly frames this: "The *pluralis excellentiae* or *pluralis maiestatis* is joined, as a rule, to the singular of the attribute."

## Counter-Examples: Elohim Construed with Plural Verbs

The "singular-verb rule" is a tendency, not an absolute. Several passages construe `אֱלֹהִים` with genuinely plural verbs/attributes even when the referent is the God of Israel. GKC §145i footnotes cases such as `אֱלֹהִים חַיִּים` "living God" (plural adjective) alongside the standard singular pattern.

| Reference | Hebrew | Parsing | Plural Feature |
|-----------|--------|---------|----------------|
| Gen 20:13 | הִתְע֣וּ אֹתִ֗י אֱלֹהִים֮ | `Verb.Hiphil.Perf.3p` + `Noun.mp.Abs` | **3p** "they caused me to wander" — Abraham speaking to a pagan king |
| Gen 35:7 | נִגְל֤וּ אֵלָיו֙ הָֽאֱלֹהִ֔ים | `Verb.Niphal.Perf.3p` + `Noun.mp.Abs` (with article) | **3p** "God revealed themselves" at Bethel |
| 2 Sam 7:23 | אֲשֶׁ֣ר הָלְכֽוּ־אֱ֠לֹהִים לִפְדֹּֽות־לֹ֨ו | `Verb.Qal.Perf.3p` + `Noun.mp.Abs` | **3p** "God went to redeem" |
| Ps 58:12 (MT; Eng 58:11) | יֵשׁ־אֱ֝לֹהִ֗ים שֹׁפְטִ֥ים בָּאָֽרֶץ | `Noun.mp.Abs` + `Ptcp.mp.Abs` | **masculine-plural participle** "judging" |

These cases are noted but not resolved by the grammars: the grammatical plural occasionally surfaces in verb/attribute agreement even where the referent is the singular God of Israel. Interpretive significance of these counter-examples (honorific, plurality-within-Godhead, idiomatic, speaker-perspective, etc.) is a separate theological question left to context-specific studies — the grammatical reference entry only documents the phenomenon.

## Contrast with Related Forms

| Form | Function | Example |
|------|----------|---------|
| Plural of majesty | one referent, plural form, (usually) singular agreement | Gen 1:1 `אֱלֹהִים בָּרָא` |
| Plural of number | many referents, plural form, plural agreement | Ex 12:12 `אֱלֹהֵי מִצְרַיִם`; Jdg 2:11 `הַבְּעָלִים` served (3mp) |
| Plural of extension (*pluralia tantum*) | inherently large/complex singleton (water, heaven, face) | `שָׁמַיִם` "heaven(s)," `מַיִם` "water(s)," `פָּנִים` "face" |
| Plural of abstraction | abstract qualities in plural form | `רַחֲמִים` "compassion," `חַיִּים` "life" |
| 1cp cohortative in divine speech | plural verb-ending with YHWH as speaker (Gen 1:26; 11:7; Isa 6:8) | separate phenomenon; see [cohortative-1cp-divine-speech](cohortative-1cp-divine-speech.md) |

GKC §124a–e treats extension, abstraction, and majesty as three faces of the non-numerical plural. Waltke-O'Connor §7.4 ("Number") groups them together as plurals of **kind**, **extension**, and **intensification**.

## Common Hebrew Nouns Showing the Majestic Plural

| Noun | Strong's | Form | Typical referent | Parser-verified example |
|------|----------|------|------------------|-------------------------|
| אֱלֹהִים | H430 | m.pl. | God of Israel (1×); any god (pl.) | Gen 1:1 (sg. verb) |
| אֲדֹנִים / אֲדֹנָי | H113 / H136 | m.pl. | single human or divine lord | Exo 21:4 (sg. verb) |
| בְּעָלִים | H1167 | m.pl. | single owner/master | Exo 21:29 (sg. verb) |
| בְּהֵמוֹת | H930 | f.pl. form | single great beast | Job 40:15 (sg. verb) |
| קְדוֹשִׁים | H6918 | m.pl. | "Holy One" (divine title) | Prov 9:10; 30:3 |
| תְּרָפִים | H8655 | m.pl. | single household idol (sometimes) | 1 Sam 19:13 (sg. agreement in some cases) |

## Textbook Citations

- **Gesenius (GKC) §124 g–i** (pp. 360–362, 388, 419) — primary treatment of *pluralis excellentiae / maiestatis* as a subspecies of the abstract plural; catalog of nouns (`אֱלֹהִים`, `אֲדֹנִים`, `בְּעָלִים`, `פָּנִים`, `רַחֲמִים`); **§132h** — concord of plural noun with singular attribute; **§145h** — rule that such plurals take singular predicate.
- **Waltke-O'Connor, *An Introduction to Biblical Hebrew Syntax* (IBHS) §7.4.2–3** (pp. 151–156) — "intensive plurals" including Leviathan and Behemoth (§7.4.2); "honorific plurals" (§7.4.3) treating `אֱלֹהִים`, `אֲדֹנִים`, `קְדוֹשִׁים`, and the singular-agreement norm.
- **Brown-Driver-Briggs (BDB)** lexicon s.v. `אֱלֹהִים`, `אָדוֹן`, `בַּעַל` — notes plural-of-majesty usage.
- **BHSG (Biblical Hebrew Study Grammar, Pratico-Van Pelt)** — plural noun morphology (Lessons 5–6, pp. 45ff.); standard paradigms do not treat *pluralis majestatis* as a separate category, subsumed under masculine/feminine plural nouns.
- **Joüon-Muraoka §136d–e** (cross-referenced in BDB notes) — *pluralis majestatis* / *excellentiae*.

(All textbook references above verified via `D:/Bible/tools/search/semantic_grammar.py` queries against indexed GKC, Waltke-O'Connor, BDB, Futato, and BHSG PDFs.)

---
*Generated from: hebrew_parser.py (--verse, --lemma), semantic_grammar.py (GKC §124 / §132h / §145h, Waltke-O'Connor §7.4.2–3, BDB, BHSG)*
*Last updated: 2026-04-18*
