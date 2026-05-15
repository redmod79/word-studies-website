# First-Person-Plural Cohortative / 1cp Imperfect in Divine Speech (Hebrew)

## Definition

The "cohortative" (*forma coortativa* / *volitive yiqtol*) is the **first-person volitive** form of Biblical Hebrew: morphologically a prefix-conjugation (*yiqtol* / imperfect) with an optional paragogic *he* suffix (-ָה), carrying self-exhortation, resolve, wish, or (when 1cp) mutual proposal — "let me…" / "let us…". When a 1cp cohortative is placed on YHWH's lips with no visible human addressee, the question of **to whom God is speaking** becomes a grammatical-theological crux with four interpretive options traditionally surveyed: (1) plural of majesty / deliberation, (2) address to the divine council, (3) intra-Trinitarian dialogue, (4) plural of self-exhortation / self-summons. GKC §124g–n catalogues the relevant "plurals" (majestatis, deliberationis, extensionis, intensitatis); Waltke–O'Connor §7.4.3 discusses the "honorific plural" and self-deliberation; IBHS §34.5.1–2 treats the cohortative proper.

1. **Paragogic-*he* cohortative** (Gen 11:7 נֵרְדָה *nērĕdāh*, Gen 11:7 וְנָבְלָה *wənāblāh*) — overt volitive morphology
2. **Unmarked 1cp *yiqtol* with cohortative force** (Gen 1:26 נַעֲשֶׂה *naʿăśeh*) — the paragogic *he* is optional, especially on III-*he* roots where it would fuse with the final *he* of the lexeme
3. **Non-volitive 1cp pronominal/suffixal echoes** in the same contexts (Gen 3:22 מִמֶּ֔נּוּ *mimmennû* "from us" 1cp; Isa 6:8 לָ֑נוּ *lānû* "for us" 1cp) — not cohortative but participant in the same referential puzzle

## Form Recognition

- **Preformative נ-** (*nun*) = the 1cp prefix on all *yiqtol* verbs; contrast 1cs **א-** (*aleph*)
- **Optional paragogic *-āh* (-ָה)** appended to the 1cp *yiqtol*: diagnostic of cohortative mood when present, though its absence does not exclude cohortative force
- **III-*he* roots** (עשׂה, היה, רדה) often do not take the paragogic *-āh* because the root's own final *-eh* already supplies the vocalic ending; 1cp *yiqtol* of III-*he* = *naʿăśeh*, *nihyeh*, *nirʾeh*
- **BHSA / ETCBC tagging note:** BHSA does not encode a separate "cohortative" feature. The parser returns `Verb.Qal.Impf.1p` for both ordinary 1cp imperfect and cohortative. Cohortative force must be read off from (a) paragogic *-āh*, (b) volitive context, (c) clause-initial position, (d) chained volitives (imperative + weqatal + *yiqtol*).
- **Parser codes:** `sp=verb vt=impf ps=p1 nu=pl` returns all 1cp prefix-conjugation verbs; no sub-filter for cohortative proper
- **Imperative-anchored clusters** (Gen 11:3, 11:4, 11:7): the presence of a paired imperative *hābâ* "come!" followed by 1cp *yiqtol* is a strong signal that the *yiqtol* is cohortative — "come, let us…"

## Functions with Examples

All examples parsed with `hebrew_parser.py --verse`.

### 1. Divine 1cp Cohortative — *naʿăśeh* / *nērĕdāh*

The two canonical cases of YHWH speaking of himself in the 1cp with volitive force:

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Gen 1:26 | נַֽעֲשֶׂ֥ה אָדָ֛ם בְּצַלְמֵ֖נוּ כִּדְמוּתֵ֑נוּ | עשׂה Qal.Impf.1p + *bĕṣalmēnû* 1cp.suff + *kidmûtēnû* 1cp.suff | "Let us make man in our image, after our likeness" |
| Gen 11:7 | הָ֚בָה נֵֽרְדָ֔ה וְנָבְלָ֥ה שָׁ֖ם שְׂפָתָ֑ם | יהב Qal.Impv.2ms + ירד Qal.Impf.1p (*+āh*) + בלל Qal.Impf.1p (*+āh*) | "Go to, let us go down, and there confound their language" |

**Observations from the parse:**
- Gen 1:26 *naʿăśeh* carries NO paragogic *he*, but (a) the III-*he* root עשׂה would fuse any suffix, and (b) the following 1cp possessive suffixes *bĕṣalmēnû / kidmûtēnû* confirm the plurality is not merely morphological: God also speaks of "our image" and "our likeness".
- Gen 11:7 shows the **textbook cohortative chain**: imperative *hābâ* → 1cp *yiqtol + -āh* → 1cp *weyiqtol + -āh* — the unambiguous cohortative shape — placed verbatim on YHWH's lips, **mirroring the human builders' own *hābâ…nilbĕnāh…niśrĕpāh…nibneh…naʿăśeh* cluster of Gen 11:3–4** (parser: Gen 11:3 נִלְבְּנָ֣ה, נִשְׂרְפָ֖ה; Gen 11:4 נִבְנֶה, נַֽעֲשֶׂה — all `Verb.Qal.Impf.1p`). The divine *nērĕdāh* is thus a grammatically exact counter-cohortative to the Babel-builders' cohortatives.

### 2. Divine 1cp Pronoun / Suffix without Cohortative Verb

These are **not cohortatives** (no 1cp *yiqtol*) but feed the same interpretive debate because the plurality-of-YHWH is carried by a pronominal element:

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Gen 3:22 | הֵן הָאָדָם הָיָה כְּאַחַד מִמֶּנּוּ | היה Qal.Perf.3ms + *mimmennû* מן + 1cp.suff | "Behold, the man is become as one of us" |
| Isa 6:8 | אֶת־מִי אֶשְׁלַח וּמִי יֵלֶךְ־לָנוּ | שׁלח Qal.Impf.1s + הלך Qal.Impf.3ms + *lānû* ל + 1cp.suff | "Whom shall I send, and who will go for us?" |

**Observations:**
- Gen 3:22 uses a **3ms Qal perfect** of היה with the construct phrase כְּאַחַד *kĕʾaḥad* "as one" + the 1cp ablative pronoun *mimmennû* ("from us"). No cohortative; the plurality is pronominal-suffixal only, matched to the 1cp possessive suffixes of 1:26.
- Isa 6:8 is grammatically striking: the **main verb shifts from 1cs to 3ms within a single clause** — אֶשְׁלַח "shall *I* send" (Qal.Impf.1s, אליapreformative) immediately paralleled by יֵלֶךְ "will go" (Qal.Impf.**3**ms) complemented by לָנוּ "for *us*" (1cp suffix on ל). The grammatical number of the subject shifts between the two interrogatives, while the indirect object commits to 1cp. No cohortative, but the 1cs→1cp oscillation is the same pattern in compressed form.

### 3. Non-Divine 1cp Cohortatives (Baseline Usage)

For contrast, the same morphology is everywhere in human speech — it is **not intrinsically theological**:

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Gen 11:3 | נִלְבְּנָה לְבֵנִים וְנִשְׂרְפָה לִשְׂרֵפָה | לבן Qal.Impf.1p (*+āh*) + שׂרף Qal.Impf.1p (*+āh*) | "Let us make brick, and burn them throughly" |
| Gen 11:4 | נִבְנֶה־לָּנוּ עִיר וּמִגְדָּל … וְנַעֲשֶׂה־לָּנוּ שֵׁם | בנה Qal.Impf.1p + עשׂה Qal.Impf.1p | "Let us build us a city and a tower … and let us make us a name" |
| Gen 19:2 | נָלִין | לין Qal.Impf.1p | "we will abide" (hospitality volitive) |
| Gen 22:5 | נֵלְכָה עַד־כֹּה וְנִשְׁתַּחֲוֶה | הלך Qal.Impf.1p (*+āh*) + חוה hsht.Impf.1p | "we will go yonder and worship" |

This baseline shows the form carries mutual proposal / shared resolve among humans; its theological force in Gen 1:26, 11:7, 3:22, Isa 6:8 derives not from morphology but from the fact that **the speaker is YHWH and the addressee is not overtly identified**.

## The Four Interpretive Options

Standard grammars (GKC §124g–n "Plural of Majesty, Deliberation, Intensity"; Waltke–O'Connor §7.4.3 "Honorific Plurals"; IBHS §34.5.1 cohortative; Joüon–Muraoka §114e, §136d–e) systematically canvass four options. Each is compatible with the morphology; none is excluded by it. This reference documents them without adjudication.

### Option 1 — Plural of Majesty / Plural of Deliberation (*pluralis majestatis* / *pluralis deliberationis*)

**Claim:** A royal or divine self-reference plural, analogous to the "royal we" of monarchs; related to the morphologically plural noun אֱלֹהִים used with singular verbs (Gen 1:1 בָּרָא *bārāʾ* 3ms + אֱלֹהִים) and to the "plural of intensification" in Hebrew common nouns (חַיִּים *ḥayyîm* "life," דָּמִים *dāmîm* "bloodshed").

**Grammatical support:** Hebrew does use morphologically plural forms for intensive/honorific reference to single entities (GKC §124g: *pluralis extensionis*, *pluralis majestatis*, *pluralis excellentiae*). The pairing of plural אֱלֹהִים with singular verbs throughout Genesis 1 (*bārāʾ*, *wayyōmer*, *wayyarʾ*, *wayyiqrāʾ* — all Qal.Wayq.**3ms**) is often cited as a parallel.

**Grammatical difficulty:** GKC §124g itself notes caution. No other ANE deity uses 1cp self-reference, and the royal "we" is poorly attested for Hebrew kings — David, Solomon, etc. speak as 1cs. Genuine "deliberative" 1cp (*pluralis deliberationis*) is well attested for humans in council, but the single-speaker royal-we is hard to document in Hebrew prose.

**Variant — Plural of Deliberation / Self-Encouragement:** GKC §124g-N4 allows a "plural of self-deliberation" where a single speaker uses 1cp while deliberating internally (cf. 2 Sam 24:14). On this reading the divine 1cp is deliberative, not plural in reference.

### Option 2 — Address to the Divine Council (*sôd YHWH*)

**Claim:** YHWH speaks in the 1cp because he is addressing the assembled heavenly beings (בְּנֵי הָאֱלֹהִים / קְדֹשִׁים / the *sôd*), including them in the deliberation even though the executive act remains his alone.

**Grammatical support:** The divine council is explicitly present in:
- 1 Kings 22:19–22 (YHWH enthroned, כָּל־צְבָא הַשָּׁמַיִם standing before him; cohortative-like exchange: מִי יְפַתֶּה *mî yĕpatteh* "who will entice?")
- Job 1:6; 2:1 (בְּנֵי הָאֱלֹהִים come to present themselves)
- Psa 82:1 (אֱלֹהִים נִצָּב בַּעֲדַת־אֵל "God stands in the council of El")
- Psa 89:6–8 (סוֹד־קְדֹשִׁים "council of holy ones")
- Isa 6:1–8 — the nearest contextual parallel to the 1cp pronoun in question: Isaiah sees YHWH enthroned, surrounded by seraphim, and then hears YHWH say "whom shall *I* send, and who will go for *us*?" — the 1cp לָנוּ plausibly indexes the already-visible council.

**Grammatical fit:** The Isa 6:8 pattern (1cs אֶשְׁלַח "I will send" + 1cp לָנוּ "for us") is exactly the shape predicted if the council is the referent of 1cp: the sending decision is YHWH's (1cs) but the mission is undertaken on behalf of the whole assembly (1cp).

**Grammatical difficulty:** In Gen 1:26 and 11:7 no council is narratively present in the immediate context; the reader must import it from the wider canon.

### Option 3 — Intra-Trinitarian / Intra-Divine Dialogue

**Claim:** The 1cp signals internal plurality within the one God — persons within the Godhead in conversation with one another. Classical Christian reading since Justin, Irenaeus, Augustine; medieval Jewish counter-reading that the speaker is God + his *šĕkînāh* / wisdom / angels.

**Grammatical support:**
- **Gen 1:26 / 1:27 alternation:** 1:26 *naʿăśeh* (1cp cohortative) + *bĕṣalmēnû / kidmûtēnû* (1cp possessive suffixes ×2) is immediately followed in 1:27 by *wayyibrāʾ* (Qal.Wayq.**3ms**) + *bĕṣalmô* (3ms suffix) + *bĕṣelem ʾĕlōhîm bārāʾ ʾōtô* — the **number shift from 1cp deliberation to 3ms execution** within two verses is the key data point. One speaker, plural reference; one executor, singular verb.
- Gen 3:22 *kĕʾaḥad mimmennû* "as one of us" — the construct *ʾaḥad + min + 1cp* grammatically requires a group that includes the speaker; "one of us" is not reducible to a royal-we without loss.
- Gen 11:7 *nērĕdāh* matches the builders' *nibneh / naʿăśeh* in grammatical shape, setting up a counter-cohortative between one plural subject (Babel) and another (the divine speaker).

**Grammatical difficulty:** The explicit NT Trinitarian categories are not in the Hebrew text; the inference is theological, not morphological. Most modern Hebrew grammarians (GKC, Joüon–Muraoka, Waltke–O'Connor) list this option as a later Christian reading rather than a primary grammatical analysis.

### Option 4 — Plural of Self-Exhortation / Self-Summons (reflexive volitive)

**Claim:** The cohortative 1cp is a rhetorical device of self-summons, functionally equivalent to 1cs self-exhortation, and the "us" is not referential at all — it is the speaker stirring himself to action. Cf. 2 Sam 24:14 *nippĕlāh-nāʾ bĕyad-YHWH* "let us fall into YHWH's hand" (David speaking), which some read as self-deliberation.

**Grammatical support:** The cohortative proper (*yiqtol + -āh*) is a volitive, and the 1cp form is well attested in human speech where the "us" is genuinely plural (Gen 11:3–4 builders). But where a single speaker uses 1cp in internal deliberation, the "us" can collapse to a rhetorical device.

**Grammatical difficulty:** The 1cp pronominal suffixes of Gen 1:26 (*bĕṣalmēnû / kidmûtēnû*), Gen 3:22 (*mimmennû*), and Isa 6:8 (*lānû*) go beyond the volitive verb — they commit the grammar to a genuinely plural referent of "us," which is harder to reduce to a purely rhetorical self-summons.

## Distribution Summary

Drawing the full list of 1cp *yiqtol* forms from `hebrew_parser.py --search "sp=verb vt=impf ps=p1 nu=pl"`:

- **Overwhelming majority = human speakers** (Gen 11:3–4 builders; Gen 19:2 Lot's hospitality; Gen 22:5 Abraham to servants; Gen 19:5, 32 Sodomites and Lot's daughters; etc.).
- **Divine speaker = 3 passages**: Gen 1:26 (creation of mankind), Gen 11:7 (descent to Babel), and (by pronominal extension without 1cp verb) Gen 3:22 (expulsion from Eden) + Isa 6:8 (prophetic commissioning).
- **Clustering:** All three Genesis cases (1:26, 3:22, 11:7) fall within the **primeval history (Gen 1–11)**, which is programmatically the canonically-framed section where divine-human boundaries are being established/contested. Isa 6:8 is the only non-Genesis attestation and occurs at the inaugural prophetic throne-vision where the *sôd* is explicitly present.

## Contrast with Related Forms

| Form | Parsing | Function | Example |
|------|---------|----------|---------|
| **1cs *yiqtol*** (no *-āh*) | Verb.Qal.Impf.1s | ordinary "I will…" | Isa 6:8 אֶשְׁלַח "whom shall I send" |
| **1cs cohortative** (+ *-āh*) | Verb.Qal.Impf.1s | "let me…" / "I resolve to…" | Psa 78:2 אֶפְתְּחָה בְמָשָׁל פִּי "let me open my mouth in a parable" |
| **1cp *yiqtol*** (unmarked) | Verb.Qal.Impf.1p | "we will…" / "let us…" (III-*he* default) | Gen 1:26 נַעֲשֶׂה |
| **1cp cohortative** (+ *-āh*) | Verb.Qal.Impf.1p | "let us…" (overtly volitive) | Gen 11:7 נֵרְדָה / נָבְלָה |
| **3ms jussive** (apocopated) | Verb.Qal.Impf.3ms | "let him/it…" | Gen 1:3 יְהִי |
| **3ms wayyiqtol** (narrative) | Verb.Qal.Wayq.3ms | "and he did…" | Gen 1:27 וַיִּבְרָא (executed what 1:26 proposed) |
| **Plural noun + singular verb** | Noun.mp.Abs + Verb.3ms | honorific/intensive plural | Gen 1:1 בָּרָא אֱלֹהִים |

The number-shift across Gen 1:26 → 1:27 (1cp cohortative proposal → 3ms wayyiqtol execution) is the signature: deliberation in the plural, action in the singular.

See also:
- [ehyeh-1cs-imperfect](ehyeh-1cs-imperfect.md) — 1cs Qal imperfect of היה and its morphological proximity to the Tetragrammaton; parallel 1cs↔3ms rotation at Exo 3:14–15
- [qal-imperfect](qal-imperfect.md) — general Qal imperfect semantics and cohortative-overlap note
- [niphal-imperfect-divine-denial](niphal-imperfect-divine-denial.md) — another formulaic divine-speech construction

## Grammar-Reference Citations

- **GKC §124g–n** — "Plurals indicating comprehension, extension, amplification, and majesty"; §124g notes divine 1cp at Gen 1:26, 3:22, 11:7, Isa 6:8 and cautions the *pluralis majestatis* reading; §124g-N4 offers *pluralis deliberationis*
- **Waltke–O'Connor (IBHS) §7.4.3** — "Honorific plurals" and singular-verb-with-plural-noun as grammatical background; IBHS §34.5.1–2 treats the cohortative as a volitive *yiqtol* with paragogic *-āh*
- **Joüon–Muraoka §114e, §136d–e** — the cohortative proper (mood of resolve / self-exhortation); §136d distinguishes "real plural" from "plural of extension" and "plural of majesty"
- **GKC §145h** — the phenomenon of plural אֱלֹהִים with singular predicate as the governing data-point in the background
- **Cassuto (Genesis I), Westermann (Genesis 1–11), Sarna (JPS Genesis)** — standard exegetical surveys of the four-option debate

## Inventory Note

The form's rarity in divine speech is itself diagnostic: across the full Hebrew Bible, YHWH speaks in 1cs thousands of times (see [ehyeh-1cs-imperfect](ehyeh-1cs-imperfect.md) for one form alone). The 1cp occurs in **Gen 1:26, Gen 3:22, Gen 11:7, Isa 6:8** — and, by some counts, the ambiguous לָנוּ of Isa 6:8 and the enigmatic plural address at Song 1:11 *naʿăśeh-llāk* (though Song 1:11 is speaker-contested). The cluster is small enough to be treated as a discrete phenomenon rather than a productive grammatical pattern.

---

*Generated from: `hebrew_parser.py --verse "Gen 1:26"`, `"Gen 11:7"`, `"Gen 3:22"`, `"Isa 6:8"`; `--search "sp=verb vt=impf ps=p1 nu=pl" --limit 20`; `--lemma "עשׂה"`.*
*Context-neutral: all four interpretive options (majesty/deliberation, divine council, Trinity, self-exhortation) documented with their grammatical support and difficulties without adjudication.*
