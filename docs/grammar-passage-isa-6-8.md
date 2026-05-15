# Grammar Analysis: Isaiah 6:8

## Text

**Hebrew (BHS/ETCBC):**
וָאֶשְׁמַ֞ע אֶת־קֹ֤ול אֲדֹנָי֙ אֹמֵ֔ר אֶת־מִ֥י אֶשְׁלַ֖ח וּמִ֣י יֵֽלֶךְ־לָ֑נוּ וָאֹמַ֖ר הִנְנִ֥י שְׁלָחֵֽנִי׃

**KJV (Isa 6:8):** "Also I heard the voice of the Lord, saying, Whom shall I send, and who will go for us? Then said I, Here [am] I; send me."

## Narrative Context (vv.1–7, required for v.8)

From KJV `D:/bible/tools/data/kjv.txt`:

| v. | KJV |
|----|-----|
| 6:1 | "In the year that king Uzziah died I saw also the Lord sitting upon a throne, high and lifted up, and his train filled the temple." |
| 6:2 | "Above it stood the seraphims: each one had six wings; with twain he covered his face, and with twain he covered his feet, and with twain he did fly." |
| 6:3 | "And one cried unto another, and said, Holy, holy, holy, is the LORD of hosts: the whole earth is full of his glory." |
| 6:4 | "And the posts of the door moved at the voice of him that cried, and the house was filled with smoke." |
| 6:5 | "Then said I, Woe is me! for I am undone; because I am a man of unclean lips, and I dwell in the midst of a people of unclean lips: for mine eyes have seen the King, the LORD of hosts." |
| 6:6 | "Then flew one of the seraphims unto me, having a live coal in his hand, which he had taken with the tongs from off the altar:" |
| 6:7 | "And he laid it upon my mouth, and said, Lo, this hath touched thy lips; and thine iniquity is taken away, and thy sin purged." |

v.8 therefore occurs inside a throne-room / heavenly-court scene: YHWH enthroned (v.1), plural seraphim attendants antiphonally crying (vv.2–3), smoke/quake theophany (v.4), prophetic cleansing (vv.5–7). The plural *lanu* in v.8 must be read against this already-plural heavenly-retinue scene, not an otherwise-unmarked soliloquy. This is a **divine-council/throne-vision genre** in the Isa 6 / 1 Kgs 22:19–22 / Job 1:6–12 / 2:1–6 / Ps 82:1 / Dan 7:9–10 mold.

## Word-by-Word Parsing (from `hebrew_parser.py --verse "Isa 6:8"`)

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | וָ | ו | Conj | and |
| 2 | אֶשְׁמַ֞ע | שׁמע | Verb.Qal.**Wayq.1s** | hear |
| 3 | אֶת | את | Prep | \<obj marker\> |
| 4 | קֹ֤ול | קול | Noun.ms.**Cst** | sound/voice |
| 5 | אֲדֹנָי֙ | אדני | PropN.ms.Abs | Lord |
| 6 | אֹמֵ֔ר | אמר | Verb.Qal.**Ptcp** ms Abs | saying |
| 7 | אֶת | את | Prep | \<obj marker\> |
| 8 | מִ֥י | מי | IntPron | who |
| 9 | **אֶשְׁלַ֖ח** | שׁלח | **Verb.Qal.Impf.1s** | shall-I-send |
| 10 | וּ | ו | Conj | and |
| 11 | מִ֣י | מי | IntPron | who |
| 12 | יֵֽלֶךְ | הלך | Verb.Qal.Impf.**3ms** | will-go |
| 13 | **לָ֑נוּ** | ל | **Prep.+1cp** | for-us |
| 14 | וָ | ו | Conj | and |
| 15 | אֹמַ֖ר | אמר | Verb.Qal.Wayq.1s | said |
| 16 | הִנְנִ֥י | הנה | Interj.+1cs | behold-me |
| 17 | שְׁלָחֵֽנִי | שׁלח | Verb.Qal.**Impv.2ms.+1cs** | send-me |

## Clause Structure (from `hebrew_parser.py --clause "Isa 6:8"`)

| # | Type | Domain | Text | Function |
|---|------|--------|------|----------|
| 1 | Way0 | N (narrative) | וָאֶשְׁמַע אֶת קוֹל אֲדֹנָי | Wayyiqtol main: "and I heard the voice of the Lord" (Pred + Objc) |
| 2 | Ptcp | N | אֹמֵר | attributive/circumstantial participle headed by *qol ʾadonay*: "…saying" (PreC) |
| 3 | **xYq0** | **Q (quotation)** | אֶת מִי אֶשְׁלַח | fronted-object yiqtol: Objc *ʾet-mi* + Pred *ʾeshlach* — **"whom shall I send"** |
| 4 | **WXYq** | **Q** | וּמִי יֵלֶךְ לָנוּ | Conj + Subj *mi* + Pred *yelek* + Adju *lanu* — **"and who will go for us"** |
| 5 | Way0 | N | וָאֹמַר | Wayyiqtol narrative resumption: "and I said" |
| 6 | NmCl | Q | הִנְנִי | IntS: deictic/self-presentation "here-I-am" |
| 7 | ZIm0 | Q | שְׁלָחֵנִי | imperative with pronominal-object: "send me" (PreO) |

Two features of the clause map are load-bearing:

- Clauses **3 and 4 are the divine quotation** (domain Q). The speaker is YHWH himself; no human speaker mediates.
- **One speaker-subject, two number values**: clause 3's predicate *ʾeshlach* is **1cs** (single grammatical subject); clause 4's adjunct *lanu* is **1cp** (plural pronominal reference). Both are voiced by the same *qol ʾadonay* without any shift in speech-frame.

## Construct Chain

`hebrew_parser.py --construct "Isa 6:8"`:

- קוֹל (Cst) ↔ אֲדֹנָי (Abs): "the voice of the Lord" — one chain, no other nominal binding. The fronted-accusative *ʾet-qol ʾadonay ʾomer* marks the divine voice as a single, determinate speech-source; the plural *lanu* is therefore **not** a linguistic artefact of a compound Nomen-regens subject.

## Key Grammatical Features

### 1. אֶשְׁלַ֖ח *ʾeshlach* — Qal Imperfect 1cs

- **Form:** Qal yiqtol, aleph-preformative (1cs common-gender), root שׁלח H7971 "send."
- **Function here:** deliberative / modal *yiqtol* in a rhetorical question fronted by interrogative *mi* + object-marker *ʾet* — "whom shall I send?" The aleph-preformative unambiguously restricts the subject to **a single speaker** ("I," 1cs). 1cs yiqtol has no gender distinction and no plural counterpart morphologically (the 1cp is נִשְׁלַח *nishlach* with nun-preformative); if the speaker intended a plural self-reference the verb would be *nishlach*, not *ʾeshlach* (GKC §47; Joüon–Muraoka §44; Waltke-O'Connor §29.4).
- **Deliberative nuance:** Waltke-O'Connor §31.4h ("The modal deliberative imperfect asks what is to be done, especially in rhetorical self-questioning"); GKC §107t; Joüon–Muraoka §113d ("The imperfect is used for actions envisaged as possible, desirable, obligatory").
- **Grammar reference:** [qal-imperfect](../hebrew/qal-imperfect.md) — prefix afformatives 1cs אֶ־ vs. 1cp נִ־; modal-volitive 1st-person range.

### 2. לָ֑נוּ *lanu* — Preposition לְ + 1cp pronominal suffix

- **Form:** the preposition לְ with the **1st-person common plural** pronominal suffix נוּ־ ("for us / to us"). Parser tag `Prep.+1up` (ETCBC code for 1cp).
- **Function here:** **adjunct** (Adju) in clause 4, modifying *yelek* "will go." The clause-level parser explicitly labels *lanu* as an adjunct, not a datival recipient of an implicit transitive verb. The referent of the suffix is the speaker (YHWH) **together with some plurality**.
- **The 1cp is morphologically unambiguous.** The suffix נוּ־ is the pure 1cp form (contrast 1cs נִי־ *-ni* as in the preceding הִנְנִי *hinneni* and following שְׁלָחֵנִי *shelacheni*). There is no Biblical Hebrew form where נוּ־ on a preposition can mean "me" (GKC §91e; Joüon–Muraoka §94g). The number contrast *ʾeshlach* (1cs) vs. *lanu* (1cp) is therefore linguistically **irreducible**, not a textual or translational artefact.

### 3. יֵ֫לֶךְ *yelek* — Qal Imperfect 3ms

- **Form:** Qal yiqtol 3ms of הלך (parsed by ETCBC under root הלך with suppletive "go" semantics; same form as standard Qal impf of ילך in older grammars). The subject is the interrogative מִי "who" (SUBJ slot in clause 4).
- **Function here:** indefinite-personal modal yiqtol — "who [is it that] will go." The 3ms singular subject *mi* + singular *yelek* contrasts intentionally with the plural *lanu*: the messenger is sought **one** at a time, on behalf of a plural sender. The mismatch is not "everyone goes for us" (which would be 3mp *yelku*) but "some single agent goes **for a plural us**."

### 4. וָאֶשְׁמַ֞ע / וָאֹמַ֖ר — Wayyiqtol 1cs (narrative frame)

- **Form:** Qal wayyiqtol 1cs of שׁמע (v.8a) and אמר (v.8d) — standard prophetic-autobiography narrative chain (cf. Isa 6:1 *wāʾerʾeh*, part of the throne-vision frame formula).
- **Function:** sequentially-ordered mainline narrative verbs in domain N, framing the embedded divine-quotation (domain Q, clauses 3–4, 6–7). The wayyiqtol chain preserves the standard **vision-report** template documented in [vision-introduction-formulas](../hebrew/vision-introduction-formulas.md).

### 5. הִנְנִ֥י שְׁלָחֵֽנִי *hinneni shelacheni* — Isaiah's response

- **Form:** interjection הִנֵּה + 1cs suffix נִי־ ("behold-me," 1cs) + Qal imperative 2ms of שׁלח + 1cs-object suffix נִי־ ("send-me," 2ms verb / 1cs object).
- **Significance:** every pronominal marker in Isaiah's reply is **singular 1cs**, matching *ʾeshlach* exactly and contrasting with *lanu*. Isaiah identifies as one messenger sent by one sender; he does **not** reply in the plural. His grammar tracks *ʾeshlach* (1cs sender–1cs sent), leaving the plural *lanu* semantically unresolved by the human speaker.
- **Speech-act sequence:** deliberative question (divine, 1cs + 1cp adjunct) → volunteer-self-presentation *hinneni* (cf. Gen 22:1, 11; 31:11; 46:2; Exo 3:4; 1 Sam 3:4–10 — stock prophetic call-response idiom) → imperative-of-commission *shelacheni*.

## The Grammatical Crux: *ʾeshlach* (1cs) + *lanu* (1cp) in One Divine Utterance

The verse is widely cited as one of the three canonical OT passages where YHWH speaks of himself simultaneously in the singular and in the plural. The other two are given in the user's brief (Gen 1:26; Gen 11:7) and are parsed below. In all three the grammatical shape is identical at the level of **the morphology is irreducible**: the plural form cannot be eliminated by re-pointing, re-reading, or re-segmenting the consonantal text.

### Gen 1:26 parallel (`hebrew_parser.py --verse "Gen 1:26"`)

וַיֹּ֣אמֶר אֱלֹהִ֔ים **נַֽעֲשֶׂ֥ה** אָדָ֛ם **בְּצַלְמֵ֖נוּ כִּדְמוּתֵ֑נוּ**

| Word | Parsing | Note |
|------|---------|------|
| יֹּ֣אמֶר | Verb.Qal.Wayq.**3ms** | singular speech-frame with *ʾElohim* |
| אֱלֹהִ֔ים | Noun.**mp**.Abs | morph. plural, **grammatically singular** (takes 3ms verb) |
| נַֽעֲשֶׂ֥ה | Verb.Qal.**Impf.1p** | 1cp cohortative "let us make" (nun-preformative, contrast 1cs א־) |
| צַלְמֵ֖נוּ | Noun.ms.Abs.**+1cp** | "our image" — 1cp pronominal suffix |
| דְמוּתֵ֑נוּ | Noun.fs.Abs.**+1cp** | "our likeness" — 1cp pronominal suffix |

Then v.27 immediately reverts to singular: וַיִּבְרָא אֱלֹהִים אֶת־הָאָדָם **בְּצַלְמוֹ** בְּצֶלֶם אֱלֹהִים בָּרָא אֹתוֹ ("in **his** [3ms] image… created **him**") — a 3ms-suffix execution of the 1cp deliberation. The plurality is confined to the divine council-deliberation mode; the creative act is singular.

### Gen 11:7 parallel (`hebrew_parser.py --verse "Gen 11:7"`)

הָ֚בָה **נֵֽרְדָ֔ה** וְ**נָבְלָ֥ה** שָׁ֖ם שְׂפָתָ֑ם

| Word | Parsing | Note |
|------|---------|------|
| הָ֚בָה | Verb.Qal.Impv.2ms | hortatory "come!" (frozen imv. of יהב) |
| נֵֽרְדָ֔ה | Verb.Qal.**Impf.1p** | 1cp cohortative "let us go down" |
| נָבְלָ֥ה | Verb.Qal.**Impf.1p** | 1cp cohortative "let us confound" |

Then Gen 11:5 already had **singular** YHWH descending (*wayyered YHWH*); Gen 11:8–9 resumes with singular *wayyaphes* / *balal YHWH*. Same pattern: the plural is confined to the deliberative/announced intention; execution is singular.

### Comparison of the three loci

| Locus | Singular form | Plural form | Intervening singular? |
|-------|--------------|-------------|------------------------|
| Gen 1:26 | *ʾElohim* + 3ms *wayyoʾmer* | 1cp *naʿăseh* + 1cp suffix *ṣalmenu/demutenu* | v.27 3ms *wayyivra* / *beṣalmo* |
| Gen 11:7 | v.5 3ms *wayyered YHWH* | 1cp *nerdah* + 1cp *nabelah* | v.8 3ms *wayyaphes YHWH* |
| **Isa 6:8** | **1cs *ʾeshlach*** (the volitional core) | **1cp *lanu*** (the adjunct) | **same verse, same utterance** |

Isa 6:8 is uniquely tight: Gen 1:26 and Gen 11:7 keep singular-divine and plural-divine in **adjacent verses**; Isa 6:8 places them inside **one interrogative speech-act** without an intervening speech-frame. That compression is what makes the verse grammatically striking.

## Interpretive Options (grammatical constraints on each)

The following four readings have been advanced in the grammar and commentary literature. Each is evaluated against the morphological facts above without theological adjudication.

### (1) Divine Council / Heavenly Retinue

- **Claim:** *lanu* includes YHWH + the seraphim attendants who have been onstage since v.2. YHWH deliberates over whom to send on behalf of the whole heavenly court; *ʾeshlach* (1cs) is the personal act of commissioning, *lanu* (1cp) is the corporate beneficiary.
- **Grammar fit:** strongest contextual fit — the throne-room + seraphim scene is already plural-agent-staffed; Isa 6 is the clearest OT divine-council scene alongside 1 Kgs 22:19–22 (Micaiah's vision, where YHWH explicitly consults *kol-ṣebaʾ hashamayim* "all the host of heaven" and asks *mi yefatteh* "who will entice Ahab"). The *mi yelek lanu* "who will go for us" of Isa 6:8 is structurally identical to *mi yefatteh* of 1 Kgs 22:20 and is issued by the same enthroned YHWH in both scenes.
- **Grammar limit:** the 1cp *lanu* is the **only** plural in the verse; the verb is still 1cs. On this reading YHWH alone decides (1cs *ʾeshlach*) but acts for the corporate "us" (1cp *lanu*). The mismatch is itself evidence for, not against, this reading — it is exactly the grammar of a chair-of-council.
- **Literature:** Waltke-O'Connor §7.4.3b flag 1cp divine reference as "address to heavenly court"; Joüon–Muraoka §114e lists Isa 6:8 under "plural of self-deliberation in divine speech … referring to God and his attendants"; H. W. Wolff, *Anthropology of the OT* (ET 1974), treats *lanu* as plural-of-assembly.

### (2) Plural of Majesty / Plural of Deliberation (a grammatical intransitive)

- **Claim:** Biblical Hebrew has an attested category of "plural of majesty" (esp. in nouns: *ʾElohim* 3ms, *ʾadonai* 3ms, *beʿalav* Exod 22:7) and, by extension, "plural of self-address" / "plural of deliberation" in a single speaker's volitive (cf. 2 Sam 24:14 *nippelah-naʾ beyad-YHWH*). On this reading *lanu* is merely a stylistic fossil of royal/majestic self-reference.
- **Grammar fit:** the category exists for nouns (GKC §124g–k, "pluralis excellentiae / majestatis") and is generally acknowledged for nouns addressing or describing God. For **verbs and pronominal suffixes**, however, the evidence is contested. GKC §124g–n admits the nominal category but **expresses caution** that the verbal/suffixal "plural of majesty" is not well attested outside the small handful of passages under discussion here (Gen 1:26; 3:22; 11:7; Isa 6:8). Joüon–Muraoka §114e is likewise cautious, noting that the four-passage corpus is also the inventory for reading (1) and the category is partly posited to explain them.
- **Grammar limit:** the "plural of majesty" reading is **circular** — it is derived largely from the same four verses it is invoked to explain. As a standalone grammatical category for verbs/suffixes it has thin independent attestation (Waltke-O'Connor §7.4.3b: "The plural of majesty in verbs is dubious"; cf. also Cassuto, *Genesis I*, 54–57; Westermann, *Genesis 1–11*, 144–145).

### (3) Intra-trinitarian Address (Christian dogmatic reading)

- **Claim:** The plural *lanu* and its parallels in Gen 1:26; 3:22; 11:7 are addressed among the persons of the Godhead (traditionally: Father to Son and Spirit, or the three speaking collegially). On this reading *ʾeshlach* (1cs) is the single divine essence; *lanu* (1cp) is the plural of persons.
- **Grammar fit:** the reading requires no extra grammatical machinery beyond (1) — it is a **theological specification** of what the 1cp includes. At the level of morphology it cannot be distinguished from the divine-council reading; both posit a plural addressee/coagent beside the 1cs decision-maker.
- **Grammar limit:** Hebrew grammar alone does **not** disclose the identity of the "us." Waltke-O'Connor §7.4.3b explicitly: "the text does not specify the identity of the plurality … the traditional Christian interpretation is a theological extension beyond what grammar alone supports." Joüon–Muraoka §114e concurs — the verse is grammatically neutral between heavenly-court and intra-divine-plurality readings. Gordon Wenham, *Genesis 1–15* (WBC), 27–28, lists the trinitarian reading as grammatically possible but canonically under-determined in Gen 1:26; his verdict generalises to Isa 6:8.
- **NT linkage:** John 12:41 applies Isa 6 directly to the pre-incarnate Christ ("these things said Isaiah, when he saw his glory"), and Acts 28:25–27 attributes the Isa 6:9–10 commission to the Holy Spirit. The NT reads the throne-vision speaker as christologically and pneumatologically plural; this is a post-exegetical datum that shapes how later Christian readers parse the *lanu* — but it does **not alter** the 1cs/1cp morphology of the Hebrew itself.

### (4) Plural of Self-Exhortation / Cohortative "we-of-deliberation"

- **Claim:** The 1cp cohortatives in Gen 1:26 (*naʿăseh*) and Gen 11:7 (*nerdah / nabelah*) can be read as speaker-alone cohortatives where Hebrew allows a first-person plural form when a single speaker reasons with himself (cf. colloquial English "let's see"). Isa 6:8 is then claimed as a residual pronoun-level case.
- **Grammar fit:** the category is recognised for cohortatives (GKC §108b notes "the cohortative expresses the speaker's own will, and the 1st pl. sometimes with a single speaker"), but the examples GKC cites (2 Sam 24:14; Gen 26:22) are not divine speech and not in throne-vision contexts.
- **Grammar limit:** even if the cohortative category extends here, **Isa 6:8 has no cohortative form**: *ʾeshlach* is standard 1cs yiqtol, not 1cp cohortative *nishlechah*. The plural is carried only by the pronominal suffix *lanu*. Stretching the self-exhortation category from verbs to suffixes is lexically unsupported (Joüon–Muraoka §114).

### Grammatical summary

- Morphology rules out monotone-singular readings: *lanu* **is** 1cp; *ʾeshlach* **is** 1cs; neither form is ambiguous.
- Morphology does **not** rule out, and cannot discriminate among, readings (1), (2), (3), (4). The choice is made on **context, canonical correlation, and theological commitment**, not on Hebrew forms.
- The context of Isa 6 (seraphim, throne-room, heavenly voices in antiphon) is **maximally favourable** to reading (1) and, under Christian canonical reading, to (3) as a specification of (1); it is **least favourable** to the pure plural-of-majesty reading (2), whose case rests elsewhere.

## Cross-References

### Grammar library

- [qal-imperfect](../hebrew/qal-imperfect.md) — 1cs vs. 1cp prefix afformatives; modal/deliberative yiqtol range.
- [vision-introduction-formulas](../hebrew/vision-introduction-formulas.md) — Isa 6:1 *wāʾerʾeh* is in this formula inventory; the vv.1–8 unit belongs to the throne-vision genre.
- [symbol-decoding-predicate-nominal](../hebrew/symbol-decoding-predicate-nominal.md) — verbless predicate-nominal clauses and divine-council speech patterns (for 1 Kgs 22:19–22 parallel mechanics).
- [ehyeh-1cs-imperfect](../hebrew/ehyeh-1cs-imperfect.md) — companion treatment of a 1cs Qal imperfect in divine self-disclosure; parallel methodology for parsing divine-speech person-shift.

### Passage analyses

- [exodus-3-13-15](exodus-3-13-15.md) — parallel divine self-disclosure with 1cs/3ms person-shift inside theophany (contrast: Exo 3 shifts persons *across* verses; Isa 6:8 shifts number *within* a verse).
- [isa-14-ezek-28-self-deification](isa-14-ezek-28-self-deification.md) — inverse case: human speaker using divine first-person; useful for contrasting legitimate plural-of-council vs. illegitimate 1cs self-divinising.

### Word studies

- (None yet for שׁלח H7971 *shalach* or הלך H1980 *halak*; candidate additions flagged.)

## Textbook Citations

- GKC (Gesenius-Kautzsch-Cowley) §47 (1cs/1cp preformatives); §107t (deliberative imperfect); §108b (cohortative with singular speaker); §124g–n (pluralis majestatis/excellentiae — nominal scope); §145 (agreement asymmetry).
- Joüon–Muraoka, *A Grammar of Biblical Hebrew* (rev. ed. 2006) §44 (1cs form paradigm); §94g (1cp pronominal suffix נוּ־); §113d (modal imperfect); §114e (plural-of-deliberation in divine speech; specifically Gen 1:26; 11:7; Isa 6:8).
- Waltke & O'Connor, *An Introduction to Biblical Hebrew Syntax* (1990) §7.4.3b (honorific/majestic and address-to-court plurals; caution on verbal plural of majesty); §29.4 (prefix-conjugation afformatives); §29.6c (aspect of yiqtol); §31.4h (modal/deliberative yiqtol).
- Cassuto, *A Commentary on the Book of Genesis I: From Adam to Noah* (ET 1961), 54–57 (Gen 1:26 plural reading, heavenly-court option).
- Westermann, *Genesis 1–11: A Continental Commentary* (ET 1984), 144–145 (plural of deliberation, council reading).
- Wenham, *Genesis 1–15* (WBC 1, 1987), 27–28 (catalogue of Gen 1:26 readings).
- J. D. Levenson, *Creation and the Persistence of Evil* (1988), ch. 1 (divine council in Isa 6 / 1 Kgs 22).

## Notes for Downstream Studies

- Isa 6:8's 1cs/1cp compression inside **one** utterance makes it the *grammatically tightest* of the three classic OT plural-of-divinity verses.
- Any argument that weakens the divine-council reading by erasing the plural in Gen 1:26 / 11:7 must still account for *lanu* in Isa 6:8, where no adjacent singular verse exists to "rescue" the plural.
- John 12:41 / Acts 28:25–27 give the NT's own reading of the *qol ʾadonay* of v.1 as christological/pneumatological, but this is canonical exegesis, not Hebrew morphology.
- The "here am I; send me" (*hinneni shelacheni*) speech-act has structural parallels across call narratives (Gen 22; Exo 3; 1 Sam 3; Jer 1); in all of them the prophet/patriarch answers in 1cs — the plurality of the sender is never matched by a plurality in the sent.
