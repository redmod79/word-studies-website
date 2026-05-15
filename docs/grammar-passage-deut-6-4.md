# Grammar Analysis: Deuteronomy 6:4 — The Shema

**"Hear, O Israel: YHWH our God, YHWH [is] one"**

The theological and liturgical heart of Jewish monotheism, opening the *Shema* (named for its first word שְׁמַע, "hear"). The verse consists of only six Hebrew words, yet its verbless predication and ambiguous apposition have generated three defensible translations, each with different doctrinal weight. This entry parses every word, documents the BHSA clause analysis, maps the syntactic options, and evaluates whether אֶחָד (*echad*) permits "compound unity" by comparison with its other substantival uses (Gen 2:24; Num 13:23; Ezek 37:17) and with the exclusive-uniqueness term יָחִיד (*yachid*, H3173). LXX reading: εἷς ἐστίν.

---

## Text

**Hebrew (BHS / ETCBC):**
שְׁמַ֖ע יִשְׂרָאֵ֑ל יְהוָ֥ה אֱלֹהֵ֖ינוּ יְהוָ֥ה׀ אֶחָֽד׃

**Transliteration:** *Shĕmaʻ Yisraʼel, YHWH Ĕloheinu, YHWH ʼEchad*

**KJV:** "Hear, O Israel: The LORD our God [is] one LORD:"

**LXX (Rahlfs, Deut 6:4):** Ἄκουε, Ισραηλ· κύριος ὁ θεὸς ἡμῶν κύριος εἷς ἐστιν.
("Hear, Israel: the Lord our God, Lord, one is" — εἷς = "one," masculine singular cardinal; the added ἐστίν makes the implicit Hebrew copula explicit.)

---

## Word-by-Word Parsing

Direct output of `hebrew_parser.py --verse "Deu 6:4"`:

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | שְׁמַ֖ע | שׁמע | Verb.Qal.Impv.2ms | hear |
| 2 | יִשְׂרָאֵ֑ל | ישׂראל | PropN.s.Abs | Israel |
| 3 | יְהוָ֥ה | יהוה | PropN.ms.Abs | YHWH |
| 4 | אֱלֹהֵ֖ינוּ | אלהים | Noun.mp.Abs.+1cp | our God(s) |
| 5 | יְהוָ֥ה | יהוה | PropN.ms.Abs | YHWH |
| 6 | אֶחָֽד | אחד | Noun.s.Abs | one |

Masoretic accentuation is notable: the *paseq* (׀) between the second יְהוָ֥ה and אֶחָֽד (word 5 → 6) signals a minor pause, and the large ע of שְׁמַע and large ד of אֶחָד in the Masoretic manuscripts spell out the acrostic עֵד ("witness").

---

## Clause Structure (BHSA)

Direct output of `hebrew_parser.py --clause "Deu 6:4"`:

| Clause | Type | Domain | Text | Function |
|--------|------|--------|------|----------|
| 1 | ZIm0 | Q | שְׁמַ֖ע | [Pred] — zero-subject imperative clause |
| 2 | Voct | Q | יִשְׂרָאֵ֑ל | [Voct] — vocative |
| 3 | CPen | Q | יְהוָ֥ה אֱלֹהֵ֖ינוּ | [Frnt] — **casus pendens / left-dislocation** |
| 4 | NmCl | Q | יְהוָ֥ה אֶחָֽד | [Subj] יְהוָה + [PreC] אֶחָד — **verbless nominal clause** |

The BHSA syntactic tagging is decisive: it reads clause 3 (יְהוָה אֱלֹהֵינוּ) as *casus pendens* (hanging topic, "As for YHWH our God…") and clause 4 (יְהוָה אֶחָד) as the resumptive nominal-clause predication ("YHWH is one"). This is one of the three main translation options (see §2 below), and it is the one the BHSA encoders judged grammatically most natural.

No construct chains are present: `hebrew_parser.py --construct "Deu 6:4"` returns no results. יְהוָה אֱלֹהֵינוּ is **appositional**, not construct — YHWH is not grammatically "genitive" to Elohim.

---

## Key Grammatical Features

### 1. שְׁמַ֖ע — Qal imperative 2ms

- **Form:** Verb, Qal stem, imperative mood, 2nd masculine singular, addressed to the collective "Israel" (functioning as a singular addressee).
- **Significance:** The imperative governs the whole rhetorical unit 6:4–9 and is the title of the prayer. The 2ms with a collective noun is standard Deuteronomic covenant address (cf. Deut 4:1; 5:1; 9:1; 20:3; 27:9). It is not merely "listen" but "hear with covenant attentiveness" — a verb of reception + obedience (cf. שָׁמַע + ב / ל constructions meaning "obey").
- **Grammar reference:** `grammar-reference/hebrew/qal-imperfect.md` (related Qal paradigm). Imperative shares the Qal stem's basic active/fientive semantics.

### 2. אֱלֹהֵ֖ינוּ — "our God(s)" (formally plural, syntactically singular)

- **Form:** Noun, masculine **plural** absolute, with 1st common plural suffix (+1cp). Lemma אֱלֹהִים (H430) — the so-called *plural of majesty* or *honorific plural*.
- **Significance:** The form אֱלֹהֵינוּ preserves the -îm plural of אֱלֹהִים under suffix (the final mem drops before suffixes in construct/bound form). Although morphologically plural, אֱלֹהִים as a designation of the true God governs **singular** verbs and adjectives throughout the Hebrew Bible — e.g., Gen 1:1 בָּרָא (3ms, not 3mp) אֱלֹהִים. GKC §124g–i, §145h classify this as *pluralis excellentiae / majestatis*: a plural of intensification or comprehensiveness, not of numerical plurality. Joüon-Muraoka §136d makes the same point.
- **The logical tension of the Shema:** The verse predicates אֶחָד ("one") of a subject identified by a plural noun (אֱלֹהִים) with a singular proper name (יְהוָה). The formal clash — plural noun governed by a singular numeral — is resolved within Hebrew grammar by the majestic-plural convention, and that resolution is exactly what makes the Shema grammatically compact rather than self-contradictory.
- **Word study:** `word-studies/H433-eloah.md` (singular cognate); Elohim (H430) study to be written if a canonical entry is needed.

### 3. Apposition: יְהוָה אֱלֹהֵינוּ — proper name + common noun

- **Form:** Two nominatives in apposition. יְהוָה is a proper noun (PropN.ms.Abs); אֱלֹהֵינוּ is a common noun with suffix. Hebrew apposition does not use a linking particle.
- **Significance:** The relation is *explicative apposition* — "YHWH, [who is] our God." Waltke-O'Connor §12.1 treats proper-name + common-noun apposition as a standard idiom ("David the king," "YHWH our God"). The phrase is covenantal: it identifies which god is "our God" by the personal name YHWH. This construction appears ~280× in the Hebrew Bible and is especially dense in Deuteronomy.
- **Implication for translation:** Because the apposition already identifies YHWH with Elohim, the question raised by the Shema is not *which* god, but *what* is predicated of that god in the second half.

### 4. יְהוָה אֶחָד — verbless nominal clause

- **Form:** Subject (יְהוָה) + predicate complement (אֶחָד). No explicit copula. Hebrew nominal clauses supply "is/are" in translation from context; tense comes from discourse (here, gnomic/present).
- **Significance:** The core assertion. אֶחָד here is substantival/adjectival, functioning as predicate. See §3 below for the three possible parsings of the whole verse depending on how this clause relates to the preceding phrase.
- **Grammar reference:** `grammar-reference/hebrew/symbol-decoding-predicate-nominal.md` (verbless clause mechanics).

### 5. אֶחָד — cardinal numeral "one"

- **Form:** Noun/adjective, singular, absolute state (Noun.s.Abs per BHSA). Strong's H259.
- **Semantic range:** Strong's glosses it as "properly, **united**, i.e., one." Functions as (a) cardinal numeral, (b) ordinal "first," (c) indefinite article "a certain," (d) substantival "one [of a group]," (e) quasi-adverbial "together." The question of whether it intrinsically carries "compound unity" is §4 below.
- **Word study:** `word-studies/H259-echad.md` — 739 verses, 980 tokens; full distribution documented.

---

## 1. The Three Syntactic Options

The verse contains four words (יְהוָה אֱלֹהֵינוּ יְהוָה אֶחָד) with no finite verb and no copula. Any pair of adjacent words can be read as subject-predicate; any pair can be read as apposition. This yields the following well-attested options (surveyed in Tigay, *JPS Torah Commentary: Deuteronomy*, Excursus 10; McConville, *Deuteronomy* [AOTC]; Block, *Deuteronomy* [NIVAC]; Weinfeld, *Deuteronomy 1–11* [AB]):

### Option A — "YHWH our God, YHWH is one" (KJV / JPS 1917 / NASB marg.)

Parse: [יְהוָה אֱלֹהֵינוּ] = apposition (subject). [יְהוָה אֶחָד] = nominal clause (predicate "YHWH is one").

But this reading requires a second subject "YHWH" after the vocative, leaving the opening phrase dangling. Most modern grammarians treat the opening יְהוָה אֱלֹהֵינוּ as *casus pendens* / left-dislocation — exactly as the BHSA tagging does (clause 3 = CPen, "Frnt[onted]"). In casus-pendens syntax the topic is stated, then resumed by a subject in the main clause. Here the main-clause subject is the second יְהוָה.

Rendering (smoothed): "As for YHWH our God — YHWH is one."

### Option B — "YHWH is our God, YHWH alone" (NJPS 1985 / NRSV marg. / Tigay)

Parse: [יְהוָה] = subject. [אֱלֹהֵינוּ] = predicate. [יְהוָה אֶחָד] = restatement, with אֶחָד construed as "alone / only."

This reading treats the verse as a confession of **exclusive loyalty** rather than numerical unity: Israel is to worship YHWH, not the storm-gods or the local *baʿalim*. It harmonizes with Deut 6:5 ("you shall love YHWH your God with all your heart…"), which is a commandment of exclusive allegiance. It also matches the broader Deuteronomic theology of *one place* of worship (Deut 12). Tigay argues this fits the adverbial use of אֶחָד in Josh 22:20; 1 Chr 29:1 ("alone"), and the absence of polemic against a *multiple* YHWH.

Rendering: "YHWH is our God, YHWH alone."

### Option C — "YHWH our God is one YHWH" (older KJV gloss / Ibn Ezra)

Parse: [יְהוָה אֱלֹהֵינוּ] = subject in apposition. [יְהוָה אֶחָד] = predicate noun phrase.

This reading is grammatically possible but contextually strained: "one YHWH" presupposes a contrast with a *plural* YHWH, a notion otherwise absent in Deuteronomy. It may reflect polemic against regional YHWH-cults (the "YHWH of Teman," "YHWH of Samaria" inscriptions at Kuntillet ʿAjrud), reading the Shema as asserting that these manifestations are *one* YHWH. Block (NIVAC) and a minority of scholars take this line.

Rendering: "YHWH our God is one YHWH."

### Option D — "YHWH is our God; YHWH is one" (coordinated nominal clauses)

Parse: two juxtaposed verbless clauses. [יְהוָה] = subj, [אֱלֹהֵינוּ] = pred; [יְהוָה] = subj, [אֶחָד] = pred.

Grammatically clean (two NmCl in asyndetic parataxis), but the BHSA parser does *not* analyze the first pair as an independent nominal clause — it tags יְהוָה אֱלֹהֵינוּ as CPen (*casus pendens*), which presupposes the second clause completes it. So Option D is defensible but not what the BHSA encoders saw.

### Which option does the grammar alone decide?

**None decisively.** All four are syntactically possible. The grammar narrows the field:
- The BHSA tagging (CPen + NmCl) strongly favors Option A (casus pendens construction), i.e., "As for YHWH our God — YHWH is one."
- The presence of the *paseq* (׀) between the second יְהוָה and אֶחָד in the Masoretic text suggests the Masoretes read יְהוָה as subject and אֶחָד as predicate (supporting A / B / D against C, where אֶחָד יְהוָה would be a single predicate phrase).
- The LXX's explicit εἷς ἐστιν ("is one") — with the copula restored — mirrors Option A, reading אֶחָד as predicate complement.

The difference between A and B is **lexical**, not syntactic: does אֶחָד here mean "one [in number/unity]" or "alone/only"? That question pushes us into §4.

---

## 2. Eloheinu: Plural Form, Singular Proper Name

The theological cruxes of the Shema hinge on what to make of a morphologically plural noun (אֱלֹהִים) taking a singular personal name (יְהוָה) and being predicated with a singular cardinal (אֶחָד).

### Grammatical fact

Standard grammars agree that אֱלֹהִים as the Israelite designation for YHWH is a **plural of majesty** (Latin: *pluralis maiestatis* / *pluralis excellentiae*):

- **GKC §124g–i:** "The plural אֱלֹהִים, as a designation of the one true God, is a plural of majesty… accompanied by a singular predicate." Cites Gen 1:1; Deut 6:4.
- **Joüon-Muraoka §136d:** "The plural אֱלֹהִים, when applied to the God of Israel, takes the verb in the singular; it is a plural of excellence expressing fullness."
- **Waltke-O'Connor §7.4.3:** "Plurals of majesty / abstraction are characterized by a singular referent; predicates agree with the singular sense."
- **BDB s.v. אֱלֹהִים:** "plur. intensive of majesty… when referring to the one true God, takes singular verb." 2,602 occurrences referring to the God of Israel, consistently with singular agreement.

### Evidence from the verse itself

In Deut 6:4 itself the plural אֱלֹהֵינוּ is immediately modified by the singular אֶחָד, the singular proper name יְהוָה (twice), and (v.5) by the singular 2ms verb וְאָהַבְתָּ with 2ms suffix. Hebrew grammar routinely resolves the morphological plural of אֱלֹהִים toward singular agreement when the referent is YHWH, and toward plural agreement when the referent is actual plural deities (Gen 31:32 אֱלֹהֶיךָ with plural verb; Judg 10:14 with plural verbs; etc.). The Shema follows the standard singular-agreement pattern.

### Is this evidence for plurality in the Godhead?

Grammatically, the plural form of אֱלֹהִים, by itself, is **not** evidence of plurality in the Godhead. The majestic-plural convention is attested outside Israelite theology (Phoenician inscriptions use אֱלֹהִים of a single deity; cf. the Ahiram sarcophagus). Any argument for plurality must come from the broader canon (Gen 1:26 "let **us** make"; Isa 6:8; the divine-council texts) — not from the word אֱלֹהִים in isolation. The Shema's own grammatical resolution is relentlessly singular.

What the plural form *does* contribute is semantic **fullness / intensity**: YHWH is "God" in the fullest sense — the all-encompassing deity, not one-among-many. That fullness is compatible with a simple monad, with a complex monad, or with a plural-in-unity conception; the grammar itself does not adjudicate among them.

---

## 3. Echad (H259) vs. Yachid (H3173) — Does *echad* Allow Compound Unity?

A recurring popular argument claims that אֶחָד (*echad*) in Deut 6:4 denotes "compound unity" — oneness made up of parts — whereas יָחִיד (*yachid*) would have denoted "absolute numerical singularity" had Moses intended to preclude plurality in the Godhead. The claim is often deployed on both sides: as evidence *for* a plural-in-unity Godhead, and (by Jewish apologetics) as a misreading of lexicography.

The grammar and corpus data:

### A. Lexical data

| Term | Strong's | Occurrences | Core sense | Distribution |
|------|----------|------------:|-----------|-------------|
| אֶחָד | H259 | ~980 tokens / 739 verses | cardinal numeral "one"; ordinal "first"; indefinite "a"; substantival "one [of]"; adverbial "together" | every book of the OT; one of the most frequent numerals |
| יָחִיד | H3173 | 12 occurrences / 12 verses | "only one" — only/sole offspring; solitary; bereaved | Gen 22:2, 12, 16; Judg 11:34; Jer 6:26; Amos 8:10; Zech 12:10; Pss 22:21; 25:16; 35:17; 68:7; Prov 4:3 |

**Data source:** `hebrew_parser.py --lemma "אחד"` and `hebrew_parser.py --lemma "יחיד"`.

Observations:
1. יָחִיד is **not** a numeral. It is an adjective meaning "only (child), sole, solitary, bereaved." Its paradigm contexts are the *only son* of Abraham (Gen 22), the *only daughter* of Jephthah (Judg 11:34), and the *lonely* one in the Psalms (Ps 25:16). It would be lexically inappropriate to say "YHWH is yachid" in the sense of "numerically one" — it would more naturally mean "YHWH is solitary / bereaved / an only-child."
2. אֶחָד is the ordinary word for "one," used of days (Gen 1:5), persons (one man), items (one cluster), loaves (one loaf), and nations (one people, Gen 11:6; 34:16).
3. A hypothetical "Shema with yachid" (שְׁמַע יִשְׂרָאֵל יְהוָה אֱלֹהֵינוּ יְהוָה יָחִיד) would be grammatically marked and exegetically odd — a claim that YHWH is "solitary" or "an only child" — which is why Moses would not have used it regardless of Trinitarian debate.

### B. Does *echad* intrinsically mean "compound unity"?

**No — not intrinsically.** אֶחָד simply means "one." Whether the "one" is composed of parts depends on the *noun it counts*, not on אֶחָד itself. Compare:

| Verse | Phrase | Parse | Counts what? | Compound? |
|-------|--------|-------|-------------|-----------|
| Gen 1:5 | יֹום אֶחָד | "day one / one day" | one calendar day | No (a day is one unit) |
| Gen 2:24 | לְבָשָׂ֥ר אֶחָֽד | "one flesh" | husband + wife → one flesh | **Yes** (two persons unified) |
| Gen 11:6 | עַם אֶחָד | "one people" | all post-flood humans | **Yes** (many individuals, one collective) |
| Gen 41:25 | חֲלֹום פַּרְעֹה אֶחָד הוּא | "Pharaoh's dream is one" | two dreams (vv. 1–7) | **Yes** (two dreams, one meaning) |
| Num 13:23 | אֶשְׁכֹּול עֲנָבִים אֶחָד | "one cluster of grapes" | many grapes on a stem | **Yes** (many berries, one cluster) |
| 2 Sam 7:23 | גֹּוי אֶחָד | "one nation" | all Israel | **Yes** (many people, one nation) |
| Ezek 37:17 | לְעֵץ אֶחָד | "one stick" | two sticks (Judah + Joseph) joined | **Yes** (two → one) |
| Ezek 37:22 | לְגֹוי אֶחָד | "one nation" | two kingdoms reunited | **Yes** |
| Ex 26:6 | מִשְׁכָּן אֶחָד | "one tabernacle" | ten curtains linked | **Yes** |
| Exod 24:3 | קֹול אֶחָד | "one voice" | whole congregation speaking | **Yes** (many voices, one response) |

In every case it is the **referent of the noun** that makes the "oneness" compound or simple — not the word אֶחָד. אֶחָד is lexically neutral on this: it denotes cardinality "one," and whatever internal complexity "one X" contains comes from what X is.

### C. Does this mean *echad* supports a plural-in-unity reading of Deut 6:4?

**Grammatically permissive, not grammatically decisive.** Since אֶחָד does not *exclude* internal plurality (as the examples above show), nothing in the grammar of Deut 6:4 rules out a complex-monad reading. But nothing in the grammar *requires* it either. The verse with יָחִיד would have been lexically odd, but that is because יָחִיד is the wrong numeral for a theological statement of unity, not because Moses was carefully preserving plural-in-unity space.

**The word alone cannot carry a trinitarian argument,** since אֶחָד equally counts simple entities (one day, one man) and compound ones (one flesh, one cluster). Conversely, Jewish-apologetic insistence that אֶחָד *always* means "absolute numerical one" is also wrong: Gen 2:24 and Ezek 37:17 show the word plainly used of compound entities.

The honest summary is:
- Grammar and lexicon: אֶחָד = "one," referent-neutral.
- Would *yachid* have worked?: No — it means "only-one/solitary," a different concept.
- Does the Shema's אֶחָד prove or disprove plurality in YHWH?: Neither. The verse asserts unity; what is inside that unity must be determined from other texts.

---

## 4. The LXX Evidence

The LXX renders the verse:

> Ἄκουε, Ισραηλ· κύριος ὁ θεὸς ἡμῶν κύριος εἷς ἐστιν.

Key features:

1. **εἷς** — masculine singular nominative cardinal "one." LSJ and BDAG agree εἷς is referent-neutral in the same way אֶחָד is: it counts one entity, compound or simple, depending on the noun it modifies. Paul uses εἷς of the unity of Christ and his body ("we, though many, are ἓν σῶμα, one body," 1 Cor 10:17; 12:12) — the same compound-unity semantics as Gen 2:24's מִן־בָּשָׂ֥ר אֶחָֽד, which LXX renders σάρκα μίαν.
2. **ἐστιν** — explicit copula "is" added. Greek, unlike Hebrew, tolerates but does not require a copula in nominal predication; here the LXX chose to supply it, decisively marking אֶחָד as predicate ("is one") rather than attributive ("one YHWH"). This rules out Option C (§2) as the LXX reading.
3. **Word order preserved:** κύριος ὁ θεὸς ἡμῶν κύριος εἷς ἐστιν mirrors the Hebrew exactly. The LXX does **not** choose between Options A and B — it retains the ambiguity while fixing the predicate identity.
4. **NT citation:** Jesus cites Deut 6:4 in Mark 12:29 (κύριος ὁ θεὸς ἡμῶν κύριος εἷς ἐστιν) using the exact LXX wording, and the scribe responds in v.32 with καλῶς… ἐπ᾽ ἀληθείας εἶπες ὅτι εἷς ἐστιν καὶ οὐκ ἔστιν ἄλλος πλὴν αὐτοῦ — glossing εἷς as "one, and there is no other besides him," which is Option B's exclusive-loyalty sense. Paul in 1 Cor 8:4 (οὐδεὶς θεὸς εἰ μὴ εἷς) and Eph 4:6 (εἷς θεὸς καὶ πατήρ) reads the Shema the same way.

The LXX and the NT both treat אֶחָד / εἷς as **predicate** ("is one"), and both gloss its force as **exclusive uniqueness** ("there is no other"). That aligns with Option B lexically, with Option A syntactically, and is compatible with (but does not affirm) the complex-monad reading.

---

## Synthesis

The six-word Shema is grammatically simple but semantically dense. What the grammar establishes:

1. **Form:** Imperative + vocative + casus pendens + nominal clause. (BHSA tagging.)
2. **Subject of predication:** The second יְהוָה is subject; אֶחָד is predicate complement. (Paseq + LXX ἐστίν.)
3. **Plural Elohim:** Plural of majesty, governed by singular verbs/adjectives throughout the verse. Grammatically compatible with any view of the Godhead; not evidence for plurality in itself.
4. **Echad vs. yachid:** אֶחָד is the correct numeral; יָחִיד would mean "solitary/only-child" and is lexically wrong for a monotheistic confession. אֶחָד is referent-neutral as to whether the "one" contains internal complexity (contrast Gen 2:24; Num 13:23; Ezek 37:17 compound, vs. Gen 1:5 simple).

What the grammar does **not** settle:
- Whether Option A, B, or D is the intended reading (all three are grammatically defensible; context and Deuteronomic theology favor A or B).
- Whether YHWH's "oneness" is numerical simplicity, exclusive uniqueness, or complex unity — this is a question of canonical theology, not of Deut 6:4 syntax.

The verse is, in the words of Tigay, "a declaration of allegiance" before it is a metaphysical theorem. Grammar alone tells us it is a declaration; what is declared must be heard alongside the rest of the canon.

---

## Cross-References

### Grammar Library
- `grammar-reference/hebrew/qal-imperfect.md` — Qal paradigm (imperative shares stem semantics)
- `grammar-reference/hebrew/symbol-decoding-predicate-nominal.md` — verbless nominal clause structure

### Word Studies
- `word-studies/H259-echad.md` — אֶחָד, full distribution (739 verses, 980 tokens)
- `word-studies/H3173-yachiyd.md` — יָחִיד, "only one / solitary" (12 occurrences)
- `word-studies/H3068-yhwh.md` — the Tetragrammaton
- `word-studies/H433-eloah.md` — singular cognate of אֱלֹהִים

### Related Passages
- `grammar-reference/passages/exodus-3-13-15.md` — divine name at the burning bush
- `grammar-reference/passages/exodus-6-2-3.md` — the name YHWH revealed to Moses

### Grammar References (external)
- GKC §124g–i (plural of majesty), §141 (nominal clauses), §145h (agreement with majestic plural)
- Joüon-Muraoka §136d (plural of majesty), §154 (verbless clauses)
- Waltke-O'Connor §7.4.3 (honorific plural), §8.4 (apposition), §12.1 (proper-name apposition)
- BDB s.v. אֱלֹהִים, אֶחָד, יָחִיד

### Parallel Traditions
- Mark 12:29–32 — Jesus cites Deut 6:4 in LXX wording; scribe glosses εἷς as "no other besides him"
- 1 Cor 8:4–6; Eph 4:4–6 — Pauline readings of the Shema
- Gen 2:24; Num 13:23; Ezek 37:17 — compound-unity uses of אֶחָד (all confirmed in parser output)
