# Infinitive Construct of נתן (*tēt* / *lātēt*) — Predicative-Complement / "Double-Accusative" Construction (Hebrew)

## Definition
The Qal **infinitive construct of נתן** "to give" (H5414), realized most commonly as the bare form **תֵּת** *tēt* (Cst) / **תֵת** (Abs) or prefixed **לָתֵת** *lātēt* (with lamed of purpose), governs a characteristic double-complement pattern: **object₁** (direct — what is given) + **complement** (the role, state, fate, or location *into which* it is given). The verb נתן is lexically tri-valent (giver + thing + recipient/predicate), and its infinitive construct preserves this valency while losing finite agreement. In classical grammars this is treated under "accusative of product/result" (GKC §117ii, Joüon-Muraoka §125w, IBHS §10.2.3c) or as "double accusative of person-and-predicate" when both slots are direct-marked.

1. **Object + Locative/Instrumental complement** — "give X into/under/through Y"; recipient/destination marked by preposition (בְּ־, לְ־, תַּחַת, בְּיַד).
2. **Object + Predicative complement** — "give X *to be* Y" or "give X *as* Y"; second slot is a bare noun or participle expressing the result-state (no copula in Hebrew).
3. **Object + Purpose infinitive** — "give X to do Y" (second *lə-*-infinitive chains onto the first).
4. **Compound (coordinated) object** — the X-slot expands via **וְ־** "and" to yoke two nouns under a single act of giving (e.g. *qōḏeš wə-ṣāḇāʾ* Dan 8:13).

## Form Recognition
- **First word:** `נתן` (Strong's H5414) tagged **Verb.Qal.InfCon** — morphology invariant (no person/number/gender affixation except optional pronominal suffix).
- **Parser code:** `sp=verb vs=qal vt=infc` with `lex=נתן`
- **Spelling variants:** bare **תֵּת** (most common; both Cst and Abs tags in BHSA), **לָתֵת** with prefixed *lə-*, **בְּתִתּוֹ** / **כְּתִתְּךָ** with prepositional prefix + pronominal suffix, rare **נְתָן** (Gen 38:9).
- **Diagnostic syntax:** the infinitive is immediately followed (within 1–4 words) by (a) a nominal direct object — often marked with אֶת־ or a pronominal suffix, and (b) a second constituent that is *not* a second direct object of some other verb but supplies the destination, agent, or result-state of the giving.
- **Distinguish from finite נָתַן:** the InfCon lacks person-affixes (no *nātattî* "I gave" shape); it is typically embedded under a main verb (עַד + infinitive, לְ + infinitive of purpose), a modal (יָכֹל, חָדַל, הוֹסִיף), or stands in construct to a governing noun/preposition.

## Functions with Examples

### 1. Compound Object + Predicative Complement — Dan 8:13b as type-specimen

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Dan 8:13 | תֵּ֛ת וְקֹ֥דֶשׁ וְצָבָ֖א מִרְמָֽס | Qal.InfCon.Cst + Noun.ms.Abs + Conj + Noun.ms.Abs + Noun.ms.Abs | "to give [both] the sanctuary and the host [to be] trodden under foot" |

The infinitive תֵּת governs a **coordinated-nominal object** (קֹדֶשׁ וְצָבָא — the two nouns yoked by waw under a single verbal act) plus a **predicative complement** מִרְמָס "a trampling / trampled thing" (Noun.ms.Abs, lexical H4823 √רמס "trample"). Hebrew has no copula in the result-slot; the semantic frame is "give [both] sanctuary and host *as* a trampled thing" — X₁, X₂ → Y. The KJV "to be trodden under foot" supplies a modal "to be" that the Hebrew does not write. The waw on וְקֹדֶשׁ is *not* a disjunctive introducing a new clause; it coordinates inside the verb's object-slot (construct-governance continues across the conjunction).

### 2. Object + Locative-Instrumental Complement (prepositional destination)

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Deu 1:27 | לָתֵ֥ת אֹתָ֛נוּ בְּיַ֥ד הָאֱמֹרִ֖י | lə + Qal.InfCon.Abs + DO-marker+1p + Prep + Noun.s.Cst + Adj.ms.Abs | "to deliver us into the hand of the Amorites" |
| 1Ki 5:17 [Eng 5:3] | עַ֤ד תֵּת־יְהוָה֙ אֹתָ֔ם תַּ֖חַת כַּפֹּ֥ות רַגְלָֽי | Prep + Qal.InfCon.Cst + YHWH + DO-marker+3mp + Noun.ms.Cst + Noun.fp.Cst + Noun.fd.Abs+1s | "until the LORD put them under the soles of my feet" |

1Ki 5:17 is the **syntactic parallel** to Dan 8:13: the same InfCon *tēt* governs an object (אֹתָם "them" = enemies) + a locative-predicative complement (*taḥat kappōt raglāy* "under my feet-soles"). Both verses deploy the same frame — InfCon of נתן + object + subjugation-predicate — with locative preposition תַּחַת in 1Ki 5:17 vs. bare noun מִרְמָס in Dan 8:13. Deu 1:27 shows the prepositional variant בְּיַד ("into the hand of") marking hostile transfer.

### 3. Object + Purpose-Infinitive Complement (double-infinitive chain)

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Eze 15:6 | נְתַתִּ֥יו לָאֵ֖שׁ לְאָכְלָ֑ה | Qal.Perf.1s+3ms + Prep + Noun + Prep + Noun.fs.Abs | "which I have given to the fire for fuel" |

Though the Ezek 15:6 main verb is finite (perf. *nətattîw*), it displays the **lexical semantic frame** of נתן that the InfCon inherits: object (3ms suffix on the verb) + recipient (לָאֵשׁ "to the fire") + predicative purpose (לְאָכְלָה "for/as food/fuel"). When this frame is nominalized under InfCon, the same triple valency persists.

### 4. Object + Single Complement (simplex giving)

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Gen 4:12 | לֹֽא־תֹסֵ֥ף תֵּת־כֹּחָ֖הּ לָ֑ךְ | Neg + Hiphil.Impf.3fs + Qal.InfCon.Cst + Noun.ms.Abs+3fs + Prep+2ms | "shall not henceforth yield unto thee her strength" |
| Exo 5:7 | לֹ֣א תֹאסִפ֞וּן לָתֵ֨ת תֶּ֧בֶן | Neg + Hiphil.Impf.2mp + lə + Qal.InfCon.Abs + Noun.ms.Abs | "Ye shall no more give … straw" |
| Lev 20:4 | בְּתִתֹּ֥ו מִזַּרְעֹ֖ו לַמֹּ֑לֶךְ | Prep + Qal.InfCon.Abs+3ms + Prep + Noun.ms.Abs+3ms + Prep+Noun | "when he giveth of his seed unto Molech" |

The baseline pattern — object + indirect recipient marked by lamed (לְ־) — is the lexically unmarked use. Gen 4:12 fronts the object (כֹּחָהּ "her strength") before the recipient (לָךְ "unto thee"); Lev 20:4 shows InfCon + 3ms subject-suffix (בְּתִתּוֹ "in his giving") with partitive מִזַּרְעוֹ and dative לַמֹּלֶךְ.

## Contrast with Related Forms

| Form | Function | Example |
|------|----------|---------|
| InfCon of נתן + object + predicate (this entry) | "give X [as / under / into] Y" | Dan 8:13; 1Ki 5:17 |
| Finite נָתַן + double accusative | same frame, finite verb | Eze 15:6 |
| Inf.Abs. + cognate finite נתן (paronomastic) | *intensifies* act of giving ("surely give") | Num 22:17; *see [infinitive-absolute-intensification](infinitive-absolute-intensification.md)* |
| InfCon of any verb + לְ prefix | purpose / complement ("in order to") | general; *see [seal-command-syntax-daniel](seal-command-syntax-daniel.md)* (לַחְתֹּם chain) |
| Bare predicate-nominal (verbless X = Y) | symbol decoding, copula-less equation | *see [symbol-decoding-predicate-nominal](symbol-decoding-predicate-nominal.md)* |
| Cognate accusative (verb + noun same root) | emphatic figure via noun, not InfAbs | 1Sa 1:11 וַתִּדֹּר נֶדֶר |

The **predicative-complement** slot of נתן (function 1) overlaps semantically with the predicate-nominal pattern but is **verb-governed**, not verbless: the "is/to be" sense is supplied by the giving-verb's result-role, not by an independent copular clause. The **locative-instrumental** slot (function 2) overlaps with the בְּיַד "into-hand-of" transfer idiom that recurs across the Deuteronomistic conquest/defeat vocabulary.

## Recurrent Predicate-Complement Nouns Attested with נתן

Based on parser-verified occurrences of נתן (Qal finite + InfCon) governing a second-slot predicate-noun:

| Predicate Noun | Strong's | Gloss | Example |
|----------------|----------|-------|---------|
| מִרְמָס | H4823 | "trampling / trodden thing" | Dan 8:13 (with תֵּת InfCon) |
| בְּיַד | H3027 + prep | "into the hand of" (subjugation) | Deu 1:27 לָתֵת…בְּיַד |
| תַּחַת + body-part | H8478 | "under (feet/soles of)" | 1Ki 5:17 תֵּת…תַּחַת כַּפּוֹת רַגְלָי |
| לְאָכְלָה | H402 | "for food/fuel" | Eze 15:6 נְתַתִּיו לָאֵשׁ לְאָכְלָה |
| לְבַז | H957 | "for a spoil/prey" | frame-parallel Num 14:3 יִהְיוּ לָבַז |
| לִשְׁמָמָה | H8047 | "for a desolation" | lexical family cognate of שֹׁמֵם (Dan 8:13a) |

The Dan 8:13 predicate-noun מִרְמָס ("a trampled thing") belongs to the same semantic class as "spoil, desolation, food-for-fire" — a **result-state noun** designating what the object is transformed *into* by the act of giving.

## Grammatical Notes

- **InfCon governs verbally, not substantivally:** even though morphologically a verbal noun, the InfCon retains the argument-structure of the finite verb. It takes a direct object (optionally אֶת-marked), not a genitival modifier (contrast with deverbal noun נְתִינָה which would take genitive). Dan 8:13 תֵּת governs קֹדֶשׁ וְצָבָא as verbal object, not as genitive "the giving of X."
- **Subject of the infinitive:** can be (a) supplied from context (Dan 8:13 — horn of v.11–12, or the pôlmônî / speaker-supplied agent), (b) expressed as pronominal suffix (Lev 20:4 *bə-tittô* "in his giving"), or (c) overt noun following the InfCon (1Ki 5:17 *tēt YHWH ʾōtām* "the LORD's giving them"). Dan 8:13 leaves the subject **unspecified** — the construction is agent-occluded, parallel to the Hophal passives הוּרַם / הֻשְׁלַךְ of Dan 8:11 (see [stem-hophal](stem-hophal.md)).
- **Waw-coordination inside the object slot:** when the InfCon governs compound objects joined by waw (Dan 8:13 וְקֹדֶשׁ וְצָבָא), the coordination is **internal** to the verbal complement. The two nouns share a single act of giving; treatment of them as separate predications would require repetition of the governing InfCon or a new finite verb. This is the same coordination pattern as compound objects of finite verbs (see [syntax-waw-conjunction](syntax-waw-conjunction.md) for disjunctive-vs-conjunctive diagnostics).
- **Anarthrous predicate:** the predicative complement מִרְמָס in Dan 8:13 is **absolute (not definite)** — consistent with Hebrew predicate-nominal grammar where the predicate slot is typically indefinite to distinguish it from the definite subject (cf. [symbol-decoding-predicate-nominal](symbol-decoding-predicate-nominal.md)).
- **Translation tradition:** KJV supplies "to be" in English ("to be trodden under foot") even though Hebrew has no copula in the predicate-complement slot. LXX Dan 8:13 θ' renders καὶ τὸ ἅγιον καὶ ἡ δύναμις συμπατηθήσεται with a future passive (συμπατέω "trample together"), converting the infinitive-predicate construction into a finite passive clause.
- **ETCBC/BHSA tagging:** InfCon is tagged `unknownunknown` for person/gender/number (the form is morphologically invariant); state is either `Cst` or `Abs` depending on whether a following noun is analyzed as construct-governed or absolute-apposed. Dan 8:13 tags תֵּת as `Abs` — the following nouns are treated as verbal objects, not genitival modifiers.

---

*Generated from: hebrew_parser.py (--verse, --lemma, --search); parser-verified Dan 8:13, 1Ki 5:17 [Heb 5:17/Eng 5:3], Deu 1:27, Eze 15:6, Lev 20:4, Exo 5:7, Gen 4:12*

*Cross-references: [infinitive-absolute-intensification](infinitive-absolute-intensification.md), [construct-state](construct-state.md), [symbol-decoding-predicate-nominal](symbol-decoding-predicate-nominal.md), [stem-hophal](stem-hophal.md), [syntax-waw-conjunction](syntax-waw-conjunction.md)*

*Last updated: 2026-04-20*
