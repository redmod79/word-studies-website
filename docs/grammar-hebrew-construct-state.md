# Hebrew Construct State (סְמִיכוּת *smîḵûṯ*)

**Category:** Nominal syntax — genitive/possessive relation

**Scope:** Canonical reference for the Hebrew construct chain — the syntactic relationship in which two (or more) nouns are juxtaposed to express a genitive/possessive/attributive relation. The first noun (*nomen regens*, "governing noun" / construct-form head) is morphologically reduced and phonologically bound to the second noun (*nomen rectum*, "governed noun" / absolute form). Traditional Hebrew grammar calls this construction *smîḵûṯ* ("leaning" / "support").

---

## 1. Definition

The construct chain is Hebrew's primary mechanism for expressing a wide range of nominal relations that English usually renders with "of" or with a possessive apostrophe.

```
[ Noun.Cst ]  [ Noun.Abs ]
  nomen         nomen
  regens        rectum
```

Two nouns are placed in immediate juxtaposition with no intervening preposition, conjunction, or article. The first noun is formally marked as *construct* (Cst) — syntactically dependent on the second, which stands in the *absolute* form (Abs). The pair forms a single accentual-phonological unit (often joined in the text by *maqqep̄*, e.g. בֶּן־אָדָם).

The whole chain behaves grammatically as a single noun phrase whose grammatical head is the construct noun but whose definiteness and possessive attachment are determined by the final absolute noun.

---

## 2. Morphology — how the construct form is recognized

The construct form is typically a phonologically **reduced** version of the absolute form. Reduction results from loss of word-accent (the construct form is proclitic to the following absolute):

| Feature | Absolute | Construct | Mechanism |
|---------|----------|-----------|-----------|
| Long vowel in open final syllable shortens | דָּבָר *dāḇār* | דְּבַר *dəḇar* | ā → ə / a |
| Segolate stays similar (ms) | מֶלֶךְ *meleḵ* | מֶלֶךְ *meleḵ* | no change |
| fs *-āh* → *-at* | תּוֹרָה *tôrāh* | תּוֹרַת *tôraṯ* | -āh → -aṯ |
| mp *-îm* → *-ê* | דְּבָרִים *dəḇārîm* | דִּבְרֵי *diḇrê* | -îm → -ê |
| fp *-ôṯ* unchanged | מַלְכוֹת *malḵôṯ* | מַלְכוֹת *malḵôṯ* | — |
| Dual *-ayim* → *-ê* | יָדַיִם *yāḏayim* | יְדֵי *yəḏê* | -ayim → -ê |

Diagnostic tags from ETCBC/BHSA (via `hebrew_parser.py`):

- `Noun.ms.Cst` — masculine singular construct
- `Noun.fs.Cst` — feminine singular construct
- `Noun.mp.Cst` — masculine plural construct
- `Noun.ms.Abs` — masculine singular absolute
- `Noun.ms.Abs.+3ms` — absolute noun with 3ms pronominal suffix

**Parser-verified examples** (from `hebrew_parser.py --verse`):

- Dan 8:11 — מְכֹון `Noun.ms.Cst` (from absolute מָכוֹן *māḵôn* "place, site") + מִקְדָּשֹׁו `Noun.ms.Abs.+3ms`
- Exo 3:1 — הַר `Noun.ms.Cst` (from absolute הַר; here shortened to monosyllable) + הָאֱלֹהִים `Art + Noun.mp.Abs` → "mountain of God / *the* mountain of God"
- Psa 23:3 — מַעְגְּלֵי `Noun.mp.Cst` (from absolute מַעְגָּלִים) + צֶדֶק `Noun.ms.Abs` → "paths of righteousness"
- Dan 8:14 — שְׁלֹשׁ `Noun.s.Cst` + מֵאֹות `Noun.fp.Abs` → "three (of) hundreds" = "three hundred"

---

## 3. Rules of the chain

### 3.1 No article on the construct head

The construct noun **never takes the definite article הַ־**. Definiteness of the whole chain is determined by the absolute noun:

| Form of absolute | Definiteness of the chain |
|------------------|---------------------------|
| Absolute is definite (has article, is proper noun, or has pronominal suffix) | Whole chain is definite |
| Absolute is indefinite | Whole chain is indefinite |

- Exo 3:1 הַר הָאֱלֹהִים — "*the* mountain of God" (absolute has article → whole chain definite)
- בֶּן מֶלֶךְ — "a son of a king" (neither definite)
- בֶּן הַמֶּלֶךְ — "the son of the king" / "the king's son" (absolute definite → whole chain definite)

This is why one cannot say *הַבֶּן הַמֶּלֶךְ. To say "*the* king's son" one writes בֶּן־הַמֶּלֶךְ, letting definiteness transfer across the chain.

### 3.2 No intervening material

Nothing may intervene between the construct head and the absolute noun — no article on the head, no adjective, no preposition, no conjunction. Adjectives modifying the construct head appear **after** the absolute noun and must be disambiguated by gender/number concord:

- דְּבַר הַמֶּלֶךְ הַטּוֹב — ambiguous: "the good word of the king" OR "the word of the good king" (both are ms.Abs)

For this reason Hebrew sometimes prefers the prepositional alternative לְ־ (see §5) when disambiguation is needed.

### 3.3 Chaining

A construct noun may itself govern another construct noun, producing chains of three or more:

- כְּלִי בֵית יְהוָה — "vessel(s) of the house of YHWH" (1Ki 7:48)
- Every noun except the last is in the construct form; only the final noun is absolute.

---

## 4. Semantic typing — the absolute specifies what the construct is

The construct chain is grammatically uniform but semantically diverse. The absolute noun *types* (restricts, qualifies, classifies) the construct head. Standard semantic categories (Waltke-O'Connor §9, GKC §128, Joüon §129):

| Type | Example | Gloss |
|------|---------|-------|
| **Possessive** (owner) | בֵּית דָּוִד | "David's house" |
| **Subjective** (agent of action-noun) | מוֹרָא יְהוָה | "the fear *which YHWH inspires*" (Pro 1:7) |
| **Objective** (patient of action-noun) | יִרְאַת יְהוָה | "the fear *directed toward* YHWH" |
| **Material** | כְּלִי כֶסֶף | "a vessel *made of* silver" |
| **Partitive** | מִקְצֵה הָעָם | "(some) *from among* the people" |
| **Attributive / quality** | מַעְגְּלֵי־צֶדֶק (Psa 23:3) | "paths *characterized by* righteousness" |
| **Superlative** | קֹדֶשׁ קָדָשִׁים | "most holy" (lit. "holy of holies") |
| **Origin / source** | אִישׁ מִצְרִי (rare; usually PP) | "a man of Egypt" |
| **Purpose / destination** | צֹאן הַטִּבְחָה | "sheep *for* slaughter" (Psa 44:23) |
| **Epexegetical / apposition** | נְהַר פְּרָת | "the river (that is) the Euphrates" |
| **Location** | מְכוֹן מִקְדָּשׁ | "site of (the) sanctuary" (Dan 8:11) |

The construction itself is semantically underspecified. It is the lexical meaning of the two nouns plus context that forces one reading. The same construct chain *yir'at YHWH* is read subjectively or objectively depending on discourse.

### 4.1 Dan 8:11 — *məḵôn miqdāšô* as a locational + possessive stack

```
וְהֻשְׁלַךְ   מְכוֹן     מִקְדָּשׁ        -וֹ
wə-hušlaḵ     məḵôn    miqdāš       -ô
Conj-Hophal.Pf.3ms  Noun.ms.Cst  Noun.ms.Abs  +3ms
"and the site-of his-sanctuary was cast down"
```

The chain carries two layers at once:
- **Locational** (site/established place *for*) — the construct head מְכוֹן "place, fixed site" (from √כון "be established") types its absolute as the *thing located there*;
- **Possessive** (whose sanctuary) — carried on the absolute noun by the 3ms pronominal suffix (see §6).

Note the construct *məḵôn* is the reduced/unaccented form of absolute מָכוֹן (cf. Exo 15:17 לְשִׁבְתְּךָ מָכוֹן פָּעַלְתָּ יְהוָה, where *māḵôn* stands absolute). The Dan 8:11 form is parser-tagged `Noun.ms.Cst`, and its definiteness is transferred from the definite absolute (definite by virtue of its 3ms suffix).

---

## 5. Contrast with prepositional alternatives

Biblical Hebrew sometimes uses prepositions instead of — or alongside — a construct chain. The alternatives are not semantically identical; each has its own contour.

### 5.1 *lə-* of belonging (periphrastic genitive)

- מִזְמוֹר לְדָוִד (Psa 23:1) "a psalm *belonging to / for / by* David"
- vs. construct מִזְמוֹר דָּוִד — unattested in Psalms titles

The *lə-* form expresses authorship, dedication, or belonging with looser attachment and is preferred when (a) the possessor is indefinite, (b) the head noun needs its own modifier, or (c) the construction would otherwise be ambiguous. The whole phrase can be definite (*ha-mizmôr*) without affecting the possessor-phrase — something impossible inside a construct chain.

### 5.2 *šel* / אֲשֶׁר לְ־ (Mishnaic and later; rare in BH)

Post-biblical Hebrew develops the analytic particle שֶׁל (< אֲשֶׁר לְ־) as a full genitive marker: הַבַּיִת שֶׁל הַמֶּלֶךְ "the king's house." Biblical Hebrew occasionally uses אֲשֶׁר לְ־ periphrastically (Gen 29:9 הַצֹּאן אֲשֶׁר לְאָבִיהָ, "the flock *which belongs to* her father") when the construct chain is syntactically blocked.

### 5.3 *min* of source

For origin/provenance, Hebrew typically uses מִן + absolute rather than construct: אִישׁ מִמִּצְרַיִם "a man *from* Egypt" is preferred over construct אִישׁ מִצְרַיִם when a spatial-origin rather than ethnic-classifier reading is wanted.

### 5.4 When construct is preferred

Construct is the default for:
- tight possessive/part-whole relations,
- fixed collocations (בֶּן־אָדָם, בַּת־יְרוּשָׁלִַם, אִישׁ חַיִל),
- attributive-quality genitives (מַעְגְּלֵי־צֶדֶק Psa 23:3, אֵשֶׁת חַיִל Pro 31:10),
- superlatives (שִׁיר הַשִּׁירִים, קֹדֶשׁ קָדָשִׁים),
- temple/sanctuary terminology (מְכוֹן מִקְדָּשׁוֹ Dan 8:11, הֵיכַל יְהוָה, בֵּית אֱלֹהִים, הַר הַקֹּדֶשׁ).

Prepositional alternatives are preferred when the head needs a modifier, when disambiguation of long chains is needed, or when looser attachment (authorship, dedication, benefit) is in view.

---

## 6. Pronominal suffixes attach to the final absolute noun

This is a distinctive rule: in a construct chain, a pronominal suffix attaches **to the last (absolute) noun** — even though semantically it often "belongs" to the first (construct head).

```
[ Noun.Cst ]  [ Noun.Abs + suffix ]
                           ↑
                    suffix goes here
```

The suffix marks the possessor of the *whole* chain. It cannot attach to the construct head because the construct form is already reduced and bound.

Parser-verified:

- Dan 8:11 — מְכוֹן מִקְדָּשׁ-וֹ *məḵôn miqdāš-ô* — "*his* sanctuary-site" (3ms suffix on the final absolute מִקְדָּשׁ, yet semantically the whole "site-of-his-sanctuary" is what is his; idiomatic English needs either "the site of his sanctuary" or "his holy place")
- Psa 23:1 — רֹעִי (Qal ptcp as head) — contrast a construct example: דִּבְרֵי־פִי (Psa 36:4) "the words of my mouth" — 1cs suffix on פֶּה (absolute) governs the whole chain
- Ezek-formula בֶּן־אָדָם with no suffix; but cf. דַּם־בְּרִיתוֹ "*the blood of his covenant*" (Zech 9:11): suffix on absolute בְּרִית transfers possession to whole chain — "*his* covenant-blood"

### 6.1 Consequence for definiteness

A pronominal suffix makes its host noun inherently definite (like a proper name or an article). Since construct definiteness is inherited from the absolute, a construct chain ending in Abs + suffix is always definite. Dan 8:11 *məḵôn miqdāšô* is therefore definite ("*the* site of *his* sanctuary" — never "a site of his sanctuary"), despite there being no article anywhere in the phrase.

### 6.2 Why not attach the suffix to the construct head?

Attaching the suffix to the construct head would require de-reducing the construct form back to the absolute form (since suffixes attach only to absolutes). That would break the construct chain and produce a different syntax: *məḵônô miqdāš* would mean "his place (is) a sanctuary" (two separate nominal units, perhaps a verbless clause) — not the genitive chain "the site of his sanctuary."

This is why the grammar *requires* the suffix to ride the final absolute: the construct relation and the possessive suffix cannot both be carried by the same noun.

---

## 7. Diagnostic checklist

To identify a construct chain:

1. Two (or more) adjacent nouns with no intervening preposition/article/conjunction
2. First noun tagged `Noun.*.Cst` by parser; morphologically reduced
3. Last noun tagged `Noun.*.Abs` (possibly with `+Ns` pronominal suffix)
4. Construct head carries no article
5. Definiteness of whole chain = definiteness of final absolute
6. Semantic relation inferred from lexemes + context (possessive, objective, subjective, attributive, etc.)

---

## 8. Cross-references

- [construct-chain-suffix](construct-chain-suffix.md) — focused sub-entry on the pronominal-suffix rule (§6 here expanded); 3ms allomorphs -ô / -hû / -āw, multi-level chain behavior, parser-verified canon
- [ben-adam-vocative-construct](ben-adam-vocative-construct.md) — construct chain בֵּן + אָדָם as address form; demonstrates Noun.ms.Cst + Noun.ms.Abs with vocative pragmatics
- [distributive-lamed-ratio](distributive-lamed-ratio.md) — prepositional alternative using *lə-* for ratio/distributive relations rather than construct
- [pluralis-majestatis](pluralis-majestatis.md) — definiteness of אֱלֹהִים with pronominal suffix and inside construct chains
- [apocalyptic-time-unit-grammar](apocalyptic-time-unit-grammar.md) — Dan 8:14 שְׁלֹשׁ מֵאוֹת construct-numeric chain
- [symbol-decoding-predicate-nominal](symbol-decoding-predicate-nominal.md) — verbless predicate-nominal contrasted with construct (X of Y vs. X is Y)

---

## 9. Standard grammars

- GKC §§89, 127–130 (construct state morphology and syntax)
- Waltke-O'Connor, *Biblical Hebrew Syntax* §§9.1–9.8 (full semantic taxonomy of the genitive relation)
- Joüon-Muraoka §§92, 129–131
- BHRG §25
- Futato, *Beginning Biblical Hebrew*, Lessons 10, 14
- Williams, *Hebrew Syntax* §§25–44
