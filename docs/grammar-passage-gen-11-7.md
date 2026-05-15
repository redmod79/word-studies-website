# Grammar Analysis: Genesis 11:7

**"Let us go down, and there confound their language" — the plural cohortative of deliberation**

Core grammatical concern: the abrupt shift between v.5 (singular wayyiqtol *wayyēred YHWH*, "and YHWH came down") and v.7 (1cp cohortatives *nērədāh* and *nāvlāh*, "let us go down, let us confound") — the same singular/plural switching found at Gen 1:26 (*naʿăśeh*, "let us make") and Gen 3:22 ("as one of us"). This entry parses the forms from the Masoretic Text and evaluates the interpretive options exegetes have proposed for the plurals.

---

## Text

### Genesis 11:5 (singular — context)
וַיֵּ֣רֶד יְהוָ֔ה לִרְאֹ֥ת אֶת־הָעִ֖יר וְאֶת־הַמִּגְדָּ֑ל אֲשֶׁ֥ר בָּנ֖וּ בְּנֵ֥י הָאָדָֽם׃

**KJV:** And the LORD came down to see the city and the tower, which the children of men builded.

### Genesis 11:7 (plural — analysis target)
הָ֚בָה נֵֽרְדָ֔ה וְנָבְלָ֥ה שָׁ֖ם שְׂפָתָ֑ם אֲשֶׁר֙ לֹ֣א יִשְׁמְע֔וּ אִ֖ישׁ שְׂפַ֥ת רֵעֵֽהוּ׃

**KJV:** Go to, let us go down, and there confound their language, that they may not understand one another's speech.

---

## Word-by-Word Parsing (Gen 11:7)

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | הָ֚בָה | יהב | Verb.Qal.Impv.2ms | give / come-on! |
| 2 | **נֵֽרְדָ֔ה** | **ירד** | **Verb.Qal.Impf.1cp (cohortative)** | **let us go down** |
| 3 | וְ | ו | Conj | and |
| 4 | **נָבְלָ֥ה** | **בלל** | **Verb.Qal.Impf.1cp (cohortative)** | **let us confound / mix** |
| 5 | שָׁ֖ם | שׁם | Adv | there |
| 6 | שְׂפָתָ֑ם | שׂפה | Noun.fs.Abs.+3mp | their lip / language |
| 7 | אֲשֶׁר֙ | אשׁר | Conj (rel.) | so that / which |
| 8 | לֹ֣א | לא | Neg | not |
| 9 | יִשְׁמְע֔וּ | שׁמע | Verb.Qal.Impf.3mp | they may hear/understand |
| 10 | אִ֖ישׁ | אישׁ | Noun.ms.Abs | a man / each |
| 11 | שְׂפַ֥ת | שׂפה | Noun.fs.Cst | the lip of |
| 12 | רֵעֵֽהוּ | רע | Noun.ms.Abs.+3ms | his fellow |

### Word-by-Word Parsing (Gen 11:5 — for contrast)

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | וַ | ו | Conj | and |
| 2 | **יֵּ֣רֶד** | **ירד** | **Verb.Qal.Wayq.3ms (singular)** | **and he went down** |
| 3 | יְהוָ֔ה | יהוה | PropN.ms.Abs | YHWH |
| 4 | לִרְאֹ֥ת | ראה | Prep + Verb.Qal.InfCon | to see |
| 5 | אֶת־הָעִ֖יר | את / עיר | DirObj + Art + Noun.fs.Abs | the city |
| 6 | וְאֶת־הַמִּגְדָּ֑ל | את / מגדל | Conj + DirObj + Art + Noun.ms.Abs | and the tower |
| 7 | אֲשֶׁ֥ר | אשׁר | Conj (rel.) | which |
| 8 | בָּנ֖וּ | בנה | Verb.Qal.Perf.3p | they built |
| 9 | בְּנֵ֥י | בן | Noun.mp.Cst | sons of |
| 10 | הָאָדָֽם | ה / אדם | Art + Noun.ms.Abs | mankind |

---

## Clause Structure (Gen 11:7)

From `hebrew_parser.py --clause`:

| Clause | Type | Domain | Text | Structure |
|--------|------|--------|------|-----------|
| 1 | ZIm0 | Q (discourse) | הָ֚בָה | [Pred] *hāvāh* — imperative interjection |
| 2 | ZYq0 | Q | נֵֽרְדָ֔ה | [Pred] 1cp cohortative |
| 3 | WYq0 | Q | וְנָבְלָ֥ה שָׁ֖ם שְׂפָתָ֑ם | [Conj] + [Pred] + [Loca] + [Objc] — second cohortative in series |
| 4 | xYq0 | Q | אֲשֶׁר֙ לֹ֣א יִשְׁמְע֔וּ | purpose/result clause with *asher lo'* |
| 5 | Ellp | Q | אִ֖ישׁ שְׂפַ֥ת רֵעֵֽהוּ | elliptic (verb gapped from clause 4): "[each] man the lip of his fellow" |

Three consecutive volitives (imperative + cohortative + we-cohortative) frame the deliberative utterance, followed by a purpose clause (*ʾăšer lōʾ*) stating the intended result. The final clause is verbally elliptic — it supplies the object and subject of יִשְׁמְע֔וּ but re-uses the verb of clause 4.

---

## Key Grammatical Features

### 1. *nērədāh* (נֵֽרְדָ֔ה) — 1cp Qal cohortative of ירד "go down"

- **Form:** `Verb.Qal.Impf.1cp`. The ETCBC database encodes the cohortative as a 1st-person imperfect/yiqtol. The diagnostic marker is the *paragogic* ה֯ suffix on the 1cp prefix conjugation (here vocalized -ādāh, with penultimate accent that the cohortative prefers). The 1cp imperfect without ה ending would be *nērēd*; with paragogic ה it is *nērədāh*, the dedicated cohortative form.
- **Function:** First-person volitive. Gesenius §108 lists the cohortative functions as (a) self-encouragement/resolve ("let me/us …"), (b) deliberation with oneself or another, and (c) request (in subordinate cohortative). Plural 1cp cohortatives most often express **mutual exhortation** or **deliberative resolve** inside a group ("come, let us …"). Waltke-O'Connor §34.5.1a calls the cohortative "the volitive mood of the first person."
- **Significance:** *nērədāh* functions as the semantic counterweight to v.5's singular wayyiqtol *wayyēred*. The root is identical (ירד "descend"); only person/number and mood shift. Gen 11 thus deliberately uses the same verb twice — once as narrative past singular ("he came down") and once as discourse-frame plural deliberation ("let us come down"). The author is highlighting, not suppressing, the switch.
- **Grammar reference:** [qal-imperfect](../hebrew/qal-imperfect.md) (1cp overlap with cohortative, §4 "First-Person"). The library lacks a dedicated cohortative entry — this passage could seed one.

### 2. *nāvlāh* (וְנָבְלָ֥ה) — we-cohortative of בלל "mingle/confound"

- **Form:** `Verb.Qal.Impf.1cp` of the geminate root בלל ("to mix, mingle, confuse"). Morphologically the geminate middle (doubled lamed) contracts in the 1cp prefix form to *nāvəlāh*; again the final -āh is the cohortative paragogic ה.
- **Function:** In a series of volitives (imperative → cohortative → we-cohortative), the *we-*-prefixed cohortative typically expresses **purpose or result** of the preceding volitive, or simply **continuation** of the deliberative chain (Joüon-Muraoka §116b; GKC §108d "cohortative expressing consequence after another volitive"). The structure is exactly the pattern found elsewhere in Genesis 11: compare v.3 *hāvāh nilbənāh* "come, let us make bricks" + *we-niśrəfāh* "and let us burn them"; v.4 *hāvāh nivneh* "come, let us build" + *we-naʿăśeh* "and let us make us a name." The builders use the same rhetorical structure (imperative *hāvāh* + 1cp cohortatives) that God now uses against them — a pointed grammatical echo.
- **Significance:** The verb *bālal* "confound" puns phonetically on *bāvel* "Babel" (v.9 explicitly makes the pun: *ʿal-kēn qārāʾ šəmāh bāvel kī-šām bālal YHWH…*). Grammar carries the irony: the builders said "let us make" (*naʿăśeh*, *nilbənāh*); God replies "let us confound" (*nāvlāh*).
- **Grammar reference:** [syntax-waw-conjunction](../hebrew/syntax-waw-conjunction.md) for waw+cohortative chaining.

### 3. *hāvāh* (הָ֚בָה) — frozen imperative "come!"

- **Form:** `Verb.Qal.Impv.2ms` of יהב "give," with paragogic ה. The ETCBC parses it as a 2ms imperative, but functionally it is a **frozen interjection** ("come! come on!") used to introduce a cohortative of mutual exhortation. GKC §105b and Joüon-Muraoka §105e classify it as an "interjectional imperative."
- **Function:** It is addressed to the plural speakers' own partners, not to a specific 2ms addressee — a discourse-level rhetorical marker comparable to English "come now" or "let's." Three times in Gen 11 it introduces builder-speech (vv.3, 4) and divine-speech (v.7), structurally framing the chapter.
- **Significance:** The grammatical mirroring is deliberate: the builders' *hāvāh nilbənāh* is matched by God's *hāvāh nērədāh*. Same interjection, same morphological pattern, opposite actors and outcomes.

### 4. The number shift v.5 (3ms) ↔ v.7 (1cp) — interpretive options

The parsing data makes the shift unambiguous:

- **v.5**: `Verb.Qal.Wayq.3ms` of ירד, subject יהוה (singular proper noun) → "and YHWH (he) came down."
- **v.7**: `Verb.Qal.Impf.1cp` (cohortative) of ירד, no explicit subject → "let us come down."

The same pattern appears at:

- **Gen 1:26**: 3ms wayyiqtol *wayyōmer ʾĕlōhīm* + 1cp cohortative *naʿăśeh ʾādām bəṣalmēnū kidmūtēnū* ("let us make man in our image, after our likeness").
- **Gen 3:22**: 3ms wayyiqtol *wayyōmer YHWH ʾĕlōhīm* + the prepositional phrase *kəʾaḥad mimmennū* ("as one of us"), with 3ms *yišlaḥ* (singular verb) in the following clause.
- **Isa 6:8**: 1cs + 1cp side by side — *mī ʾēšlaḥ ū-mī yēlek-lānū* ("whom shall I send, and who will go for us?").

**Interpretive options for the 1cp plural** (standard enumeration in the grammars and commentaries):

| # | Option | Argument for | Argument against |
|---|--------|--------------|------------------|
| 1 | **Plural of majesty** / *pluralis majestatis* | Known feature of royal/divine speech in the ANE; coheres with plural *ʾĕlōhīm* used with singular verbs throughout Genesis | Waltke-O'Connor §7.4.3f denies this grammatical category for 1cp pronouns/verbs: "there is no evidence that any kind of unique plural can be used with 1st person"; royal plurals in Hebrew typically attach to nouns, not verbal morphology |
| 2 | **Plural of deliberation / self-address** | Matches the deliberative force of the cohortative; parallel to Eng. "let's see…" used by a single speaker; Joüon-Muraoka §114e allows "cohortative of self-exhortation" | Requires reading the plural as essentially singular; weakens the explicit 1cp morphology |
| 3 | **Address to the divine council** | Heavenly court scenes are explicit in Isa 6, 1 Kgs 22:19–22, Job 1–2, Psa 82; Gen 3:22 "as one of us" implies plurality of beings in the divine sphere; matches 1cp morphology directly | Gen 11 does not narrate a council scene; the council reading must be inferred |
| 4 | **Intra-divine / plurality-within-God reading** (trinitarian / multi-personal) | Grammatically the cleanest match for genuine 1cp (no demotion of plural to singular; no added council characters); coheres with other Gen texts (1:26; 3:22); taken up by NT writers (Jhn 1:1–3 of the creation verses) | Anachronistic projection onto Moses; the ANE comparative data favor council reading; the doctrine of Trinity is later in revelation-history |
| 5 | **Plural of fullness / "comprehensive self"** | Keil-Delitzsch and others argue the plural expresses the fullness of divine being without specifying council or persons | Rhetorical rather than grammatical; can collapse into option 1 or 4 |

The parsing itself is neutral: *nērədāh nāvlāh* is unambiguously 1cp cohortative. Which interpretive option one adopts is a question of discourse-context, canon, and theological framework — not of morphology. The grammar forecloses the option "singular force with a plural form" (option 1 as classically stated), because 1cp cohortative morphology is not analogous to plural nouns of majesty; but it does not by itself decide between options 3, 4, and 5.

**Waltke-O'Connor §7.4.3f–g** on this: "The common notion that the plural pronouns and verbal forms … indicate a plurality of majesty is difficult to sustain. Hebrew has other ways of showing majesty." They prefer a "plural of self-deliberation" (option 2) or a "plural of self-address in the divine council" (option 3).

**GKC §124g–n** treats the phenomenon under "the plural of majesty/intensity" applied to *ʾĕlōhīm* etc., but notes §124g3 that "the plural used by God in Gen 1:26, 11:7, Isa 6:8 has been incorrectly explained in this way."

**Joüon-Muraoka §114e, §136d** list the cohortative plurals in Gen 1:26, 3:22, 11:7 as cases of "deliberation" where "the speaker associates himself with others (real or imagined)."

### 5. *ʾăšer lōʾ yišməʿū* — purpose/result clause

- **Form:** `Conj (relative) + Neg + Verb.Qal.Impf.3mp` of שׁמע. *ʾăšer* + negation + imperfect is a common construction for negative purpose/result ("so that they not …") — Waltke-O'Connor §38.3a notes *ʾăšer* frequently introduces purpose clauses when followed by a modal/volitive-leaning yiqtol.
- **Significance:** The purpose clause makes the *intended consequence* of the cohortative action explicit. The builders' failure (v.8) is the stated divine goal, not an unintended byproduct.
- **Note on *šāmaʿ*:** The verb means "hear" as a physical act, but in context with *śāfāh* ("lip/language") as object-chain (*ʾîš śəfat rēʿēhū* "a man the lip of his fellow"), it clearly means "understand [a language]" — a standard idiom (Gen 42:23; Deut 28:49; Isa 33:19).

---

## Comparison Table: The Three Gen Plural-Speech Passages

| Passage | Trigger verb (sing.) | Divine speech-plural | Form | Function in context |
|---------|----------------------|----------------------|------|---------------------|
| Gen 1:26 | *wayyōmer ʾĕlōhīm* (wayq 3ms) | *naʿăśeh* "let us make" | Qal Impf 1cp (cohortative overlap; no paragogic ה here because of guttural) | Deliberation before creation of ʾādām |
| Gen 3:22 | *wayyōmer YHWH ʾĕlōhīm* (wayq 3ms) | *kəʾaḥad mimmennū* "as one of us" | Prep + Numeral + 1cp pronominal suffix | Post-Fall assessment of humanity |
| Gen 11:7 | *wayyēred YHWH* (wayq 3ms, v.5) + *wayyōmer* (v.6) | *nērədāh … nāvlāh* "let us go down, let us confound" | Qal Impf 1cp cohortative (×2, both with paragogic ה) | Deliberation before scattering at Babel |

All three share the template:
1. Wayyiqtol 3ms narrative frame ("and YHWH said/came down …");
2. Direct speech introducing a 1cp volitive or 1cp pronoun;
3. Action that follows in the narrative reverts to **3ms singular** (Gen 1:27 *wayyivrāʾ* "and he created"; Gen 3:23 *wayšalləḥēhū* "and he sent him out"; Gen 11:8 *wayyāfeṣ* "and he scattered").

Grammar pattern: **outer frame = singular, inner speech = plural, following action = singular.** The plurality surfaces only in the quoted divine deliberation.

---

## Cross-References

**Grammar library:**
- [qal-imperfect](../hebrew/qal-imperfect.md) — covers the 1cs overlap with cohortative; 1cp cohortative is the plural analog.
- [syntax-waw-conjunction](../hebrew/syntax-waw-conjunction.md) — for waw+volitive chaining in v.7.
- [wayyiqtol narrative chain](../hebrew/) — covers v.5 *wayyēred* and v.8 *wayyāfeṣ* as the enclosing singular framework.

**Word studies needed (not yet in library):**
- *yārad* (ירד, H3381) "descend" — the theological verb of divine descent (Gen 11:5,7; 18:21; Exo 3:8; 19:11, 18, 20; Isa 64:1).
- *bālal* (בלל, H1101) "mingle, confound" — geminate root; the play on *bāvel* is central to Gen 11.
- *śāfāh* (שׂפה, H8193) "lip/language" — Gen 11 uses it as a metonym for language, a usage that ties into the eschatological "pure lip" of Zeph 3:9.

**Related passages:**
- Gen 1:26 — parallel 1cp cohortative *naʿăśeh*.
- Gen 3:22 — parallel 1cp pronoun *mimmennū*.
- Isa 6:8 — 1cs + 1cp pair in divine council context.
- Zeph 3:9 — eschatological reversal of Babel (*śāfāh bərūrāh* "pure lip/language").

---

## Reference Citations

- **Waltke, B. K. & O'Connor, M.**, *An Introduction to Biblical Hebrew Syntax* (Eisenbrauns, 1990): §7.4.3f–g on "plural of majesty" (denied for 1cp verbal morphology); §34.5.1 on the cohortative as volitive mood of the first person; §38.3 on *ʾăšer* + imperfect purpose clauses.
- **Gesenius, W.** (ed. Kautzsch-Cowley), *Hebrew Grammar*, 2nd Eng. ed. (Oxford, 1910): §108 on the cohortative (paragogic ה, functions of self-exhortation and deliberation; §108d cohortative of consequence after another volitive); §105b on *hāvāh* as interjectional imperative; §124g–n on the plural of majesty and its (in)applicability to Gen 1:26 / 11:7 / Isa 6:8.
- **Joüon, P. & Muraoka, T.**, *A Grammar of Biblical Hebrew*, 2nd ed. (Pontifical Biblical Institute, 2006): §114e cohortative of self-exhortation and deliberation; §116b waw+cohortative sequencing; §136d plural forms referring to God; §105e interjectional imperative *hāvāh*.
- **Brown-Driver-Briggs**, s.v. בלל (confound, mingle, mix), ירד (go down, descend), יהב (come! — imperative of יהב used interjectionally).
- **Keil, C. F. & Delitzsch, F.**, *Biblical Commentary on the Old Testament: The Pentateuch* vol. 1 (Eerdmans repr.): on Gen 11:7 — treats *nērədāh nāvlāh* as a plural of deliberation within the Godhead, paralleling Gen 1:26.
- **Wenham, G. J.**, *Genesis 1–15*, WBC 1 (Word, 1987): on Gen 11:1–9 — notes the structural mirroring of builder-speech (vv.3–4) and divine-speech (v.7) using identical *hāvāh* + 1cp cohortative formulas.
- **Cassuto, U.**, *A Commentary on the Book of Genesis* II: From Noah to Abraham (Magnes, 1964): on the chiastic structure of Gen 11:1–9 and the *bālal–bāvel* paronomasia.

---

*Generated from: `hebrew_parser.py --verse "Gen 11:7"`, `--verse "Gen 11:5"`, `--clause "Gen 11:7"`, `--verse "Gen 1:26"`, `--verse "Gen 3:22"`; KJV from `D:/bible/tools/data/kjv.txt`.*
*Last updated: 2026-04-18*
