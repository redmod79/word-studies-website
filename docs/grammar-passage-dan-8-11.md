# Grammar Analysis: Daniel 8:11

The **hinge verse** of the little-horn vision: three coordinate perfect-aspect clauses assemble the horn's full assault on the heavenly-realm triad — Prince, *tāmîḏ*, sanctuary-place. The verb-stem choreography is the center of gravity: one **Hiphil perfect** (*higdîl* — reflexive-intensive self-magnification against the Prince) flanked by two **Hophal perfects** (*hûram*, *hušlaḵ* — agentless passive of Hiphil, the voice Hebrew uses when action-without-named-agent is the point). Two parser-verified construct chains (**שַׂר־הַצָּבָא** and **מְכוֹן מִקְדָּשׁוֹ**) with a 3ms pronominal suffix on the second anchor the sanctuary syntactically to the heavenly **śar**, because the horn is grammatically f.s. throughout Daniel 8 and therefore cannot be the antecedent of a 3ms suffix. This is the load-bearing grammatical datum for the heavenly-sanctuary reading of the passage: the construct + suffix architecture forces "his sanctuary" = the Prince's.

For the full three-verse triad (vv.10–12) with voice-chiasm across √שׁלך, see [dan-8-10-12](dan-8-10-12.md). This entry isolates v.11 alone.

## Text

**Hebrew (MT):** וְעַ֥ד שַֽׂר־הַצָּבָ֖א הִגְדִּ֑יל וּמִמֶּ֨נּוּ֙ הוּרַ֣ם הַתָּמִ֔יד וְהֻשְׁלַ֖ךְ מְכֹ֥ון מִקְדָּשֹֽׁו׃

**KJV:** Yea, he magnified [himself] even to the prince of the host, and by him the daily [sacrifice] was taken away, and the place of his sanctuary was cast down.

## Word-by-Word Parsing (hebrew_parser.py --verse "Dan 8:11")

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | וְ | ו | Conj | and |
| 2 | עַ֥ד | עד | Prep | unto / as-high-as |
| 3 | שַֽׂר | שׂר | Noun.ms.Cst | prince-of (construct) |
| 4 | הַ | ה | Art | the |
| 5 | צָּבָ֖א | צבא | Noun.ms.Abs | host |
| 6 | הִגְדִּ֑יל | גדל | Verb.Hiphil.Perf.3ms | he-magnified-[himself] |
| 7 | וּ | ו | Conj | and |
| 8 | מִמֶּ֨נּוּ֙ | מן | Prep.+3ms | from-him / by-him |
| 9 | הוּרַם (K הרים) | רום | Verb.Hophal.Perf.3ms | was-lifted-away / was-taken-away |
| 10 | הַ | ה | Art | the |
| 11 | תָּמִ֔יד | תמיד | Noun.ms.Abs | continual[-offering] |
| 12 | וְ | ו | Conj | and |
| 13 | הֻשְׁלַ֖ךְ | שׁלך | Verb.Hophal.Perf.3ms | was-cast-down |
| 14 | מְכֹ֥ון | מכון | Noun.ms.Cst | place-of (construct) |
| 15 | מִקְדָּשֹֽׁו | מקדשׁ | Noun.ms.Abs.+3ms | his-sanctuary |

## Clause Structure (hebrew_parser.py --clause)

Three coordinate clauses, all Domain **N** (narrative), all **perfect-aspect** (not wayyiqtol) — the parser tags the sequence as **WxQ0 → WxQX → WQtX**:

| Clause | Type | Text | Functional roles |
|--------|------|------|------------------|
| 1 | **WxQ0** | וְעַד־שַׂר־הַצָּבָא הִגְדִּיל | [Conj] + [Cmpl] *ʿaḏ-śar-haṣ-ṣāḇāʾ* (**fronted — focus**) + [Pred] *higdîl* |
| 2 | **WxQX** | וּמִמֶּנּוּ הוּרַם הַתָּמִיד | [Conj] + [Cmpl] *mimmennû* (**fronted**) + [Pred] *hûram* + [Subj] *hat-tāmîḏ* |
| 3 | **WQtX** | וְהֻשְׁלַךְ מְכוֹן מִקְדָּשׁוֹ | [Conj] + [Pred] *hušlaḵ* + [Subj] *məḵôn miqdāšô* |

**Discourse function of w-x-qatal vs. wayyiqtol:** v.10 preceded with three **wayyiqtol** clauses (Qal/Hiphil Wayq 3fs — *tigdal / tappēl / tirməsēm*) carrying foregrounded narrative. V.11 breaks out of that wayyiqtol mainline into **perfect-with-fronted-constituent** clauses — the Biblical Hebrew signature for **focus-fronting / backgrounding / circumstantial** material. The shift marks a **discourse register change**: v.10 narrated the horn's assault on the host; v.11 **highlights** the new target-set (Prince / *tāmîḏ* / sanctuary-place) in focus position and encodes the resulting events in passive voice. Cross-link [syntax-wx-qatal-circumstantial](../hebrew/syntax-wx-qatal-circumstantial.md).

**Fronting pattern:** clauses 1 and 2 both front a PP to the left of the verb (*ʿaḏ-śar-haṣ-ṣāḇāʾ* / *mimmennû*), marking these constituents as the pragmatic focus. Clause 3 does not front — the Pred-Subj order with *hušlaḵ* preceding *məḵôn miqdāšô* is the canonical passive-impersonal shape.

## Construct Chains (hebrew_parser.py --construct)

| Chain | Cst member | Abs member | Translation | Note |
|-------|-----------|-----------|-------------|------|
| 1 | שַׂר (Noun.ms.Cst) | הַצָּבָא (Noun.ms.Abs, def.) | prince-of the-host | heavenly ruler-figure over the host of 8:10 (*ṣəḇāʾ haš-šāmayim* "host of the heavens") |
| 2 | מְכוֹן (Noun.ms.Cst) | מִקְדָּשׁוֹ (Noun.ms.Abs + 3ms suff.) | place-of his-sanctuary | two-member chain; 3ms suffix on absolute member scopes over the whole chain |

## Key Grammatical Features

### 1. הִגְדִּיל — Hiphil perfect 3ms of גדל: reflexive-intensive "self-magnified"

- **Form:** *higdîl* (Verb.Hiphil.Perf.3ms of גדל H1431). Hiphil morphology: hireq-yod preformative **הִ־** + stem with long /î/ theme-vowel in perfect + standard afformative.
- **Function:** the Hiphil of גדל without an overt direct object is Biblical Hebrew's standard **reflexive-intensive / internal-causative** register — "**to magnify [oneself]**, to act greatly, to boast" (GKC §53d; Joüon-Muraoka §54d; W–O §27.2). The Hiphil voice silently supplies the reflexive direct object; KJV captures this with the bracketed "[himself]."
- **Contrast with v.10 *tigdal* (Qal):** v.10's Qal wayyiqtol of גדל = intransitive "grew / became great" (size-increase). V.11's Hiphil perfect of גדל = **action of self-aggrandizement / self-exaltation** — a morally loaded register (cf. Psa 35:26; 38:17; 55:13; Lam 1:9 all Hiphil *higdîl* of enemy boasting; Isa 10:15 / Zeph 2:8, 10 of Assyrian / Moabite-Ammonite self-exaltation). Grammar distinguishes *growth* (Qal) from *self-aggrandizement* (Hiphil).
- **Gender anomaly — 3ms vs. 3fs elsewhere in Dan 8:** the horn (*qeren* H7161) is grammatically **f.s.** throughout Dan 8 — v.5 *qeren* f.s., v.9 *tigdal* 3fs, v.10 triple 3fs wayyiqtol, v.12 quadruple 3fs. The 3ms of *higdîl* is a well-known anomaly (Collins 1993, *Daniel* Hermeneia 333; Montgomery 1927 ICC 334) explained variously as (a) *constructio ad sensum* with the masculine historical referent behind the horn-symbol, (b) agreement with the proximate **3ms** שַׂר just fronted, (c) impersonal "it magnified." Reading (b) matters for clause 3's 3ms-suffix antecedent resolution below.
- **Preposition עַד "up-to / as-high-as":** the same spatial vertical-reach marker used in v.10 (*ʿaḏ-ṣəḇāʾ haš-šāmayim*, "up to the host of the heavens"). The two occurrences climb a ladder: v.10 host → v.11 Prince-of-the-host. The horn's self-magnification culminates not at general altitude but at the heavenly figure named in the construct chain.
- **Cross-links:** [stem-hiphil](../hebrew/stem-hiphil.md), [hiphil-imperfect](../hebrew/hiphil-imperfect.md), [H1431-gadal](../../word-studies/H1431-gadal.md), [TR-gadal-megaluno](../../word-studies/TR-gadal-megaluno.md) (LXX ἐμεγαλύνθη / Theod. ἐμεγαλύνθη), [H8269-sar](../../word-studies/H8269-sar.md), [TR-sar-archon](../../word-studies/TR-sar-archon.md), [H6635-tsaba](../../word-studies/H6635-tsaba.md).

### 2. הוּרַם / הֻשְׁלַךְ — The Hophal passive pair

- **Forms:** *hûram* (Verb.Hophal.Perf.3ms of רום H7311 "be-high / be-exalted" → Hophal "was-lifted-away / was-taken-away") and *hušlaḵ* (Verb.Hophal.Perf.3ms of שׁלך H7993 "throw" → Hophal "was-cast-down"). Hophal morphology: qibbuṣ/shureq preformative **הֻ־** / **הוּ־** + stem + perfect afformative.
- **Hophal stem = passive of Hiphil.** Hebrew's morphology encodes a **lexical active-passive voice pair** for causative verbs: Hiphil "X caused Y to happen" ↔ Hophal "Y was caused-to-happen (by unspecified/suppressed agent)." The Hophal is **rare** (~400 occurrences vs. Hiphil's ~9,000) and clusters at precisely the moments in biblical Hebrew where action-without-named-agent is rhetorically desired. See [stem-hophal](../hebrew/stem-hophal.md) for the canonical entry.
- **Implications for agency:** the choice of Hophal over Hiphil is the hinge of the verse. Compare what v.11 **could** have said and refused to:
  - Hiphil (active, named agent): *wə-hērîm mimmennû ʾeṯ ha-tāmîḏ / wə-hišlîḵ məḵôn miqdāšô* — "and he removed the *tāmîḏ* from him / and he cast down the place of his sanctuary" — horn as grammatical agent.
  - Hophal (actual MT text): *hûram … hat-tāmîḏ / hušlaḵ məḵôn miqdāšô* — "**was-lifted-away** the *tāmîḏ* / **was-cast-down** the place of his sanctuary" — agent grammatically suppressed.
- The grammar **refuses** to name the horn as overt grammatical agent of removal and casting. This is not stylistic accident; it is Hebrew's dedicated voice for obscuring or theologizing agency. Two interpretive options are grammatically available:
  - **(a) Agentless / indefinite-personal passive:** the event happened, but the text will not name who did it.
  - **(b) Divine passive:** the suppressed agent is God — the *tāmîḏ* was removed and the sanctuary-place cast down **within the divine permissive/judicial economy**, with the horn serving as proximate instrument. Cross-link the Greek counterpart [divine-passive](../greek/divine-passive.md); same rhetorical register reappears at Rev 13:5–7 in ἐδόθη + dative passives.
- **מִמֶּנּוּ "from him / by him" (Prep מִן + 3ms suff.):** two well-attested functions with passive verbs —
  - **Ablative of separation:** "away-from him" — the *tāmîḏ* was-removed **away from** the Prince's domain (ESV, NRSV "from him").
  - **Personal-agent marker:** "by-him" — GKC §121f, Joüon-Muraoka §132e list מִן + passive as one of BH's ways to mark agent (though *bə-* and *lə-* are more common). KJV "by him" adopts this reading, making the horn the logical-semantic agent while the verb remains grammatically passive.
- The Hophal + מִמֶּנּוּ combination deliberately leaves both readings grammatically live. What the grammar **rules out** is an unambiguous identification of the horn as *overt grammatical* agent of the verb.
- **Textual-critical note on הוּרַם:** the Masoretic pointing gives **Hophal** *hûram* "was-taken-away"; ETCBC/BHSA (reproduced by the parser) tags the consonantal form as הרים with `Verb.Hophal.Perf.3ms`. A long minority textual tradition (numerous medieval Hebrew MSS; BHS apparatus; Collins 1993, 326–27) repoints as **Hiphil** *hērîm* "he-raised / he-took-away," making the horn the overt subject. The two readings are **morphologically indistinguishable in the unpointed consonantal text** (both הרים); the dispute is a vocalization-tradition dispute. The parser follows MT pointing; the English versions split accordingly (KJV/ESV/NRSV = passive MT-Hophal reading; NIV/some older versions = active repointing).
- **Cross-links:** [stem-hophal](../hebrew/stem-hophal.md), [stem-hiphil](../hebrew/stem-hiphil.md), [divine-passive](../greek/divine-passive.md), [aorist-passive-indicative](../greek/aorist-passive-indicative.md), [H7311-ruwm](../../word-studies/H7311-ruwm.md), [H7993-shalak](../../word-studies/H7993-shalak.md), [H8548-tamid](../../word-studies/H8548-tamid.md).

### 3. מְכוֹן מִקְדָּשׁוֹ — Construct chain with 3ms suffix on the absolute

- **Chain morphology:** *məḵôn* (Noun.ms.**Cst** of מָכוֹן H4349 "fixed-place / established-site / foundation") bound to *miqdāšô* (Noun.ms.**Abs** of מִקְדָּשׁ H4720 "sanctuary" + **3ms pronominal suffix** *-ô* "his"). Classical Biblical Hebrew requires the pronominal suffix on the **absolute** (last) member even when it semantically binds the whole chain — GKC §127a, §128a; Joüon-Muraoka §140. The English equivalent is therefore "**place of his-sanctuary**" ≈ "his sanctuary's place" / "the site-of-his-sanctuary."
- **Antecedent resolution of -ô (3ms):** BH anaphora resolution prefers the nearest eligible 3ms antecedent. In v.11 the candidate 3ms referents are:
  - (a) שַׂר "prince" (Noun.ms, **explicit 3ms**, just fronted into focus position in clause 1)
  - (b) the 3ms of *higdîl* (clause 1 predicate)
  - (c) the 3ms of *mimmennû* (clause 2 fronted PP)
- The horn (*qeren*) is **f.s.** throughout Dan 8 and cannot be the grammatical antecedent of a 3ms suffix; the f.s. verb-chain of vv.5, 9, 10, 12 proves this. The anomalous 3ms of *higdîl* and *mimmennû* in v.11 either **agrees with** the newly-fronted **śar** (constructio ad sensum, reading b above) or agrees with the historical masculine referent behind the horn symbol. On either resolution, the **nearest explicit 3ms noun** eligible as antecedent for *miqdāšô* is **שַׂר־הַצָּבָא** — the Prince of the host.
- **Consequence:** "his sanctuary" is syntactically **the Prince's** sanctuary. The grammar does not permit a reading in which the sanctuary belongs to the horn, because the horn is f.s. and would require *miqdāšāh* (3fs suffix) — which the text does not have. Combined with the preceding construct chain **צְבָא הַשָּׁמָיִם** "host **of the heavens**" (v.10) and the Prince's identification as ruler over that heavenly host, the passage's sanctuary-referent is grammatically anchored **in the heavenly realm**.
- **מָכוֹן + sanctuary/throne idiom:** *māḵôn* collocates elsewhere in BH specifically with **divine dwelling / throne**:
  - Exo 15:17 *məḵôn lə-šiḇtəḵā pāʿaltā YHWH* "the place **for thy dwelling** thou hast made, O YHWH"
  - 1 Kgs 8:13 / 2 Chr 6:2 *bānōh bānîṯî bêṯ zəḇul lāḵ məḵôn lə-šiḇtəḵā ʿôlāmîm* "I have surely built a house of habitation for thee, **a place for thy dwelling for ever**"
  - Psa 89:15 [14] / 97:2 *ṣeḏeq û-mišpāṭ məḵôn kisʾeḵā* "righteousness and judgment are **the foundation of thy throne**"
  - Isa 4:5 *ʿal kol-məḵôn har-ṣiyyôn* "upon every **dwelling-place** of Mount Zion"
- The word belongs to the **divine-dwelling / throne-base** semantic register rather than the general building vocabulary (*bayit* "house," *hêḵāl* "palace/temple").
- **Cross-links:** [H4349-makon](../../word-studies/H4349-makon.md), [H4720-miqdash](../../word-studies/H4720-miqdash.md), [H8269-sar](../../word-studies/H8269-sar.md), [TR-sar-archon](../../word-studies/TR-sar-archon.md), [pluralis-majestatis](../hebrew/pluralis-majestatis.md) (related construct-chain-with-suffix mechanics).

### 4. Lexical contrasts — *mekon* vs. *hêḵāl / bayit*; *miqdāš* vs. *qōḏeš*

Two lexical seams are worth marking because they distinguish Dan 8:11's heavenly-realm vocabulary from more generic sanctuary language.

**מָכוֹן (H4349) vs. הֵיכָל (H1964) / בַּיִת (H1004):**
- *māḵôn* — "fixed-place / established-site / foundation / dwelling-base." Used ~17× in HB, predominantly of **YHWH's heavenly / Zion-enthronement site** (Exo 15:17; 1 Kgs 8:13, 39, 43, 49; 2 Chr 6:2, 30, 33, 39; Ezr 2:68; Psa 33:14; 89:15; 97:2; 104:5; Isa 4:5; 18:4). The word **never** denotes a pagan shrine or an earthly house of an ordinary owner; it is a **dedicated divine-locus** noun.
- *hêḵāl* — "palace / temple" (~80×). Either royal palace (1 Kgs 21:1; 2 Kgs 20:18; Psa 45:9, 16; Dan 1:4) or cultic temple (1 Sam 1:9; 3:3; Isa 6:1 — heavenly; Jer 7:4; Ezk 41; Hag 2:15; Zech 8:9; Mal 3:1). Shared with Akkadian *ekallu*; neutral between earthly and heavenly referent.
- *bayit* — the generic "house" (~2000×). Any dwelling, household, or (definite) temple.
- Daniel 8:11 chose the rarest and most theologically loaded of the three. *məḵôn miqdāšô* is not "his temple-building" (*hêḵāl*) nor "his house" (*bayit*) but "the **established-base** of his sanctuary."

**מִקְדָּשׁ (H4720) vs. קֹדֶשׁ (H6944):**
- *miqdāš* (v.11) — mem-preformative noun of √קדשׁ, "place-of-sanctification / sanctuary." The spatial/institutional noun: the consecrated precinct or sanctuary complex (Exo 25:8; Lev 12:4; 16:33; Num 18:1; Ezk 5:11; 8:6; 43:21; 44:1, 5, 7–9). Focus on the **sanctified locus** as a spatial entity.
- *qōḏeš* (v.13–14) — abstract/concrete noun "holiness / holy-thing / sanctuary." Broader semantic range: abstract holiness, consecrated objects, holy portions of offerings, *and* the sanctuary (Exo 26:33 *qōḏeš ha-qoḏāšîm*; Lev 10:17; Psa 60:8; 63:3; Dan 8:13–14, 9:24, 11:31).
- **The lexical shift across vv.11 → 13–14 is deliberate:** v.11 uses *məḵôn miqdāšô* (the Prince's **established sanctuary-place**) in the cast-down clause. Vv.13–14 shift to *qōḏeš* (*qōḏeš wə-ṣāḇāʾ mirmās*, v.13; *wə-niṣdaq qōḏeš*, v.14). The shift from *miqdāš* ("sanctuary-place" — the specific locus) to *qōḏeš* ("holy-thing / holy-sphere" — the broader holiness-register) enlarges the semantic scope at the vindication. What was violated (*miqdāš*, a specific place) is vindicated in the register of *qōḏeš* (the whole holiness-sphere to which that place belongs). Cross-link [dan-8-13-14-dialogue](dan-8-13-14-dialogue.md), [dan-8-14](dan-8-14.md), [H6944-qodesh](../../word-studies/H6944-qodesh.md), [H4720-miqdash](../../word-studies/H4720-miqdash.md).

### 5. The Prince / *tāmîḏ* / *mekon-miqdasho* triad — sequence of heavenly-realm attacks

The three clauses enumerate three distinct but linked heavenly-realm targets, each in a different role-slot in its clause:

| Clause | Target | Role in clause | Verb-voice | What is attacked |
|--------|--------|----------------|------------|------------------|
| 1 | **שַׂר־הַצָּבָא** (Prince of the host) | [Cmpl] (fronted PP with *ʿaḏ*) | **Hiphil act.** *higdîl* (reflexive) | ontological self-magnification **up-to** the Prince's register |
| 2 | **הַתָּמִיד** (the continual[-offering]) | [Subj] of passive | **Hophal pass.** *hûram* | removal from the Prince's domain (the *tāmîḏ*-service owed to the Prince) |
| 3 | **מְכוֹן מִקְדָּשׁוֹ** (place of his [=Prince's] sanctuary) | [Subj] of passive | **Hophal pass.** *hušlaḵ* | casting-down of the sanctuary-location belonging to the Prince |

**Three observations:**

1. **All three targets belong grammatically to the heavenly realm.** Target 1 is explicitly the **Prince-of-the-host**, the heavenly ruler over the *ṣəḇāʾ haš-šāmayim* of v.10. Target 2's article (*hat-tāmîḏ* with definite article — "the continual," the known continual-service) is anaphoric back to a unique referent in Israel's cult-vocabulary, most plausibly the continual-service owed to that same Prince. Target 3's 3ms suffix *-ô* is grammatically bound to the Prince (the only explicit 3ms antecedent in the discourse-local domain, since the horn is f.s.). The triad cannot be read earth-first: the syntax anchors it heaven-first.

2. **The verbs sequence from active-reflexive → passive → passive.** The horn's direct-agency Hiphil verb (*higdîl*) does not attack the Prince; it performs self-exaltation to the Prince's altitude. The horn is **not** the grammatical subject of any verb whose object is the Prince. The actual removals and castings (clauses 2, 3) are passives — the horn's role is grammatically deniable at the surface level. This is the Hophal's rhetorical point: the vision narrates the outcome (the *tāmîḏ* gone, the sanctuary-place cast down) without making the horn the overt subject of the verb. For the theological reading (divine passive), see [divine-passive](../greek/divine-passive.md).

3. **The sequence reads as a progressive encroachment:** (i) self-exaltation up to the Prince, (ii) removal of the *tāmîḏ* (the ongoing service-link between the Prince and his people), (iii) casting-down of the sanctuary-base (the Prince's established locus). Each step targets a different component of the heavenly-realm Prince-sanctuary-service complex.

## Cross-References

**Grammar library:**
- [stem-hophal](../hebrew/stem-hophal.md) — passive-of-Hiphil morphology and agentless-action rhetoric; load-bearing for *hûram* / *hušlaḵ*
- [stem-hiphil](../hebrew/stem-hiphil.md) — causative / internal-causative / reflexive-intensive H-stem; load-bearing for *higdîl*
- [hiphil-imperfect](../hebrew/hiphil-imperfect.md) — H-stem functional range
- [syntax-wx-qatal-circumstantial](../hebrew/syntax-wx-qatal-circumstantial.md) — v.11's WxQ0 / WxQX / WQtX break-out from v.10 wayyiqtol mainline
- [syntax-waw-conjunction](../hebrew/syntax-waw-conjunction.md) — clause-initial waw coordination
- [divine-passive](../greek/divine-passive.md) — cross-testament parallel for agentless-passive / divine-passive rhetoric
- [aorist-passive-indicative](../greek/aorist-passive-indicative.md) — Greek counterpart for Hophal-class passives

**Adjacent passage analyses:**
- [dan-8-8-9](dan-8-8-9.md) — emergence of the horn; 3mp-suffix antecedent ambiguity of *mēhem*; f.s. gender established for *qeren*
- [dan-8-10-12](dan-8-10-12.md) — the full three-verse triad with voice-chiasm on √שׁלך (supersedes this entry for the wider context)
- [dan-8-13-14-dialogue](dan-8-13-14-dialogue.md) — the 2,300 *ʿereḇ bōqer* and the Niphal of צדק; lexical shift *miqdāš* → *qōḏeš*
- [dan-8-14](dan-8-14.md) — *wə-niṣdaq qōḏeš* in isolation
- [dan-8-17-19](dan-8-17-19.md) — *ʿēṯ qēṣ* and Hithpael *ʾābîn*
- [dan-8-23-25](dan-8-23-25.md) — little-horn-king interpretation
- [dan-8-26](dan-8-26.md) — *səṯōm he-ḥāzôn*

**Word studies (canonical entries):**
- [H1431-gadal](../../word-studies/H1431-gadal.md) — *gāḏal* "be-great / magnify"; Hiphil *higdîl* in v.11
- [H4349-makon](../../word-studies/H4349-makon.md) — *māḵôn* "fixed-place / established-site"
- [H4720-miqdash](../../word-studies/H4720-miqdash.md) — *miqdāš* "sanctuary"
- [H6635-tsaba](../../word-studies/H6635-tsaba.md) — *ṣāḇāʾ* "host / army"
- [H6944-qodesh](../../word-studies/H6944-qodesh.md) — *qōḏeš* "holiness / sanctuary" (v.13–14 contrast)
- [H7311-ruwm](../../word-studies/H7311-ruwm.md) — *rûm* "be-high / be-exalted"; Hophal *hûram*
- [H7993-shalak](../../word-studies/H7993-shalak.md) — *šālaḵ* "throw / cast"; Hophal *hušlaḵ*
- [H8269-sar](../../word-studies/H8269-sar.md) — *śar* "prince / chief"
- [H8548-tamid](../../word-studies/H8548-tamid.md) — *tāmîḏ* "continual[-offering]"

**Translation-pair studies:**
- [TR-gadal-megaluno](../../word-studies/TR-gadal-megaluno.md) — Hebrew גדל ↔ Greek μεγαλύνω
- [TR-sar-archon](../../word-studies/TR-sar-archon.md) — Hebrew שׂר ↔ Greek ἄρχων
