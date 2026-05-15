# Grammar Analysis: Daniel 12:7, 12:11-12

## Scope

Three apocalyptic time-marker clauses that close the book of Daniel:

1. **Dan 12:7** — "a time, times, and a half" (לְמוֹעֵד מוֹעֲדִים וָחֵצִי) — the oath-formula duration of the persecuting power's dominion.
2. **Dan 12:11** — "1,290 days" (יָמִים אֶלֶף מָאתַיִם וְתִשְׁעִים) — the span measured from the removal of the תָּמִיד and setting up of the שִׁקּוּץ שֹׁמֵם.
3. **Dan 12:12** — "1,335 days" (יָמִים אֶלֶף שְׁלֹשׁ מֵאוֹת שְׁלֹשִׁים וַחֲמִשָּׁה) — the blessing-span for the one who waits and attains.

This analysis is **context-neutral**: it describes the grammar, syntax, and lexical data from the parsing tools and documents all major interpretive positions without endorsement.

---

## Daniel 12:7

### Text
**Hebrew:** וָאֶשְׁמַ֞ע אֶת־הָאִ֣ישׁ ׀ לְב֣וּשׁ הַבַּדִּ֗ים אֲשֶׁ֣ר מִמַּעַל֮ לְמֵימֵ֣י הַיְאֹר֒ וַיָּ֨רֶם יְמִינ֤וֹ וּשְׂמֹאלוֹ֙ אֶל־הַשָּׁמַ֔יִם וַיִּשָּׁבַ֖ע בְּחֵ֣י הָעוֹלָ֑ם כִּי֩ לְמוֹעֵ֨ד מוֹעֲדִ֜ים וָחֵ֗צִי וּכְכַלּ֛וֹת נַפֵּ֥ץ יַד־עַם־קֹ֖דֶשׁ תִּכְלֶ֥ינָה כָל־אֵֽלֶּה׃

**KJV:** "And I heard the man clothed in linen, which [was] upon the waters of the river, when he held up his right hand and his left hand unto heaven, and sware by him that liveth for ever that [it shall be] for a time, times, and an half; and when he shall have accomplished to scatter the power of the holy people, all these [things] shall be finished."

### Word-by-Word Parsing (from hebrew_parser.py)

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | וָ | ו | Conj | and |
| 2 | אֶשְׁמַע | שׁמע | Verb.Qal.Wayq.1s | I heard |
| 3 | אֶת | את | Prep | \<object marker\> |
| 4 | הָאִישׁ | אישׁ | Noun.ms.Abs + Art | the man |
| 5 | לְבוּשׁ | לבושׁ | Adj.ms.Cst | clothed |
| 6 | הַבַּדִּים | בד | Noun.mp.Abs + Art | the linen-cloths |
| 7 | אֲשֶׁר | אשׁר | Rel.conj | who/which |
| 8 | מִמַּעַל | מעל | Prep + Noun.s.Abs | from above |
| 9 | לְמֵימֵי | מים | Prep + Noun.mp.Cst | to/over the waters of |
| 10 | הַיְאֹר | יאר | Noun.ms.Abs + Art | the river |
| 11 | וַיָּרֶם | רום | Verb.**Hiphil**.Wayq.3ms | and he raised/lifted up |
| 12 | יְמִינוֹ | ימין | Noun.fs.Abs + 3ms suf | his right hand |
| 13 | וּשְׂמֹאלוֹ | שׂמאל | Noun.ms.Abs + 3ms suf | and his left |
| 14 | אֶל־הַשָּׁמַיִם | שׁמים | Prep + Noun.mp.Abs | to the heavens |
| 15 | וַיִּשָּׁבַע | שׁבע | Verb.**Niphal**.Wayq.3ms | and he swore |
| 16 | בְּחֵי הָעוֹלָם | חי + עולם | Prep + Adj.ms.Cst + Noun.ms.Abs | by the-living-of the-eternity |
| 17 | כִּי | כי | Conj | that |
| 18 | לְמוֹעֵד | מועד | Prep + Noun.ms.Abs | for an appointed-time |
| 19 | מוֹעֲדִים | מועד | Noun.**mp**.Abs | appointed-times |
| 20 | וָחֵצִי | חצי | Conj + Noun.ms.Abs | and a half |
| 21 | וּכְכַלּוֹת | כלה | Conj + Prep + Verb.Piel.InfCon | and at the completing of |
| 22 | נַפֵּץ | נפץ | Verb.Piel.InfCon | to shatter |
| 23 | יַד־עַם־קֹדֶשׁ | יד / עם / קדשׁ | Noun.s.Cst + Noun.ms.Cst + Noun.ms.Abs | the-hand-of the-people-of holiness (3-link construct chain) |
| 24 | תִּכְלֶינָה | כלה | Verb.Qal.Impf.**3fp** | they(fem.pl.) shall be finished |
| 25 | כָּל־אֵלֶּה | כל + אלה | Noun.ms.Cst + DemPron.p | all these |

### Clause Structure (from hebrew_parser.py --clause)

| # | Clause Type | Domain | Text (translit.) | Function |
|---|------------|--------|-------------------|----------|
| 1 | Way0 (wayyiqtol) | Narrative | wāʾešmaʿ ʾet-hāʾîš lǝbûš habaddîm | "And I (Daniel) heard the man clothed in linen" |
| 2 | NmCl (verbless/relative) | Narrative | ʾăšer mimmaʿal lǝmêmê hayǝʾōr | "who [was] above the waters of the river" |
| 3 | Way0 | Narrative | wayyāreim yǝmînô ûśǝmōʾlô ʾel-haššāmayim | "and he lifted his right and his left to heaven" |
| 4 | Way0 | Narrative | wayyiššābaʿ bǝḥê hāʿôlām | "and he swore by the-living of eternity" |
| 5 | NmCl (content of oath) | Narrative | kî lǝmôʿēd môʿădîm wāḥēṣî | "that [it shall be] for an appointed-time, appointed-times, and a half" |
| 6 | WxYX (waw + X + yiqtol) | Discourse | ûtikleynâ kol-ʾēlleh | "and all these shall come to a conclusion" |
| 7 | InfC | Discourse | kǝkallôt | "as/when (the) completing" |
| 8 | InfC | Discourse | nappēṣ yad-ʿam-qōdeš | "of shattering the hand of the holy people" |

The oath itself (clause 5) is a **verbless nominal clause** introduced by כִּי, with the prepositional phrase לְמוֹעֵד מוֹעֲדִים וָחֵצִי functioning as the **Time** constituent (predicate of duration). Supplied copular force: "[it will be] for a time…".

### Key Grammatical Features — Dan 12:7

#### 1. לְמוֹעֵד מוֹעֲדִים וָחֵצִי — the "time, times, half" formula

**Parsing & morphology:**

- **מוֹעֵד** (G4150 / lemma מועד) — Noun.**ms.Abs**, singular "appointed time/season/feast" (from יעד "appoint"). Same lemma as Gen 1:14 (luminaries for מוֹעֲדִים "seasons"); Lev 23:2, 4, 37 (cultic "appointed feasts"); Dan 8:19 "the appointed time of the end" (מוֹעֵד קֵץ); Dan 11:27, 29, 35; Hab 2:3.
- **מוֹעֲדִים** — Noun.**mp**.Abs, **masculine plural** of the same lemma מועד. Because the head noun מועד is masculine (-îm plural), the plural form **cannot be grammatically forced to mean exactly "two"**; the regular masculine plural of מועד is -îm, and Hebrew never formed a distinct dual for מועד in the MT. (Contrast nouns that do have a morphologically marked dual, e.g., יוֹמַיִם "two days," שְׁנָתַיִם "two years," יָדַיִם "two hands".)
- **וָחֵצִי** — Conj + Noun.ms.Abs, "and a half." חֵצִי (lemma חצי, from חצה "divide") regularly means "half" in a fractional sense: Exod 24:6; 25:10, 17; Num 12:12; 1 Kgs 3:25.

**The number-of-"times" question (morphological catalog):**

The plural מוֹעֲדִים is morphologically *indefinite as to count* — any number ≥ 2. The tradition has settled on the value "**2** times" because:

- (a) The Aramaic parallel in **Dan 7:25** reads עִדָּן וְעִדָּנִין וּפְלַג עִדָּן. The middle form עִדָּנִין in Biblical Aramaic ends in -în (emphatic pl. ending), and some grammarians (e.g., Rosenthal, *Grammar of Biblical Aramaic* §48) identify -în on עִדָּנִין in this verse as a **dual** inherited from Northwest-Semitic duals — i.e., "two periods." This reading is widely adopted but not uncontested; other grammarians treat -în as the ordinary Aramaic m.pl. ending (same termination as yomîn "days," malkîn "kings"), in which case the plural is simply ≥ 2.
- (b) The Revelation 12:14 Greek rendering καιρὸν καὶ καιροὺς καὶ ἥμισυ καιροῦ uses **καιρούς** (acc. m. **pl.**), which in itself is likewise indefinite as to number (≥ 2) but in Koine has no productive dual.
- (c) The arithmetic correspondence (1 + 2 + 0.5 = 3.5 "times" ≈ 1260 days of Rev 11:3; 12:6 ≈ 42 months of Rev 11:2; 13:5 at 30 days/month) has functioned as the *interpretive* anchor that fixes מוֹעֲדִים at "two"; the fixing is **exegetical/numerical**, not purely morphological.

**Translation implications:** Most English versions render "time, times, and half a time" preserving the indeterminacy (KJV, ESV, NASB, NIV, NRSV). The LXX-Theodotion reads καιρὸν καὶ καιροὺς καὶ ἥμισυ καιροῦ — same construction, inheriting the same ambiguity. The Old Greek renders εἰς καιρὸν καὶ καιροὺς καὶ ἥμισυ καιροῦ with the matching form.

**Semantic range of מוֹעֵד:**

| Nuance | Example | Note |
|--------|---------|------|
| Appointed cultic season/feast | Lev 23:2, 4, 37 | sacred calendar |
| Divinely fixed eschatological time | Dan 8:19; 11:27, 29, 35; Hab 2:3 | vision-context technical use |
| Meeting/place | Exod 27:21 אֹהֶל מוֹעֵד | "tent of meeting" |
| Astronomical season | Gen 1:14 | sun/moon fix מוֹעֲדִים |

In Dan 8:19 מוֹעֵד קֵץ ("the appointed time of the end") and 11:27, 29, 35 the lemma is clearly technical-apocalyptic — the *divinely-set* time-point. In 12:7 the unit-sense ("a period whose length is itself a מוֹעֵד") is imported.

#### 2. The Oath Formula — wayyiššābaʿ bǝḥê hāʿôlām + כִּי

**Parsing:** וַיִּשָּׁבַע (Verb.**Niphal**.Wayq.3ms, from שׁבע "swear"). Niphal of שׁבע is the regular form for "swear an oath" (Gen 21:23–24, 31; 24:7, 9; 25:33; Exod 13:19; Deut 6:13; Isa 45:23; Jer 12:16; ~185× in MT). See [Niphal Stem](../hebrew/stem-niphal.md) for the passive/middle/reflexive semantics; with שׁבע the Niphal is fossilized as the standard "take an oath" middle.

**The oath formula structure:**

- **בְּ + חֵי + הָעוֹלָם** — "by the-living-of the-eternity" = "by Him who lives forever." חַי is an adjective here in construct (Adj.ms.Cst), forming a construct chain with הָעוֹלָם. Idiomatic oath-by-the-life-of (Gen 42:15 חֵי פַרְעֹה; Num 14:21, 28 חַי־אָנִי YHWH-oath form; 1 Sam 17:55; 25:26; 2 Sam 15:21).
- **כִּי** (clause 5) — post-oath conjunction introducing the *content* of the oath. When following an oath formula, כִּי functions as the declarative "that" (not causal "because"): Gen 22:16–17 בִּי נִשְׁבַּעְתִּי … כִּי בָרֵךְ אֲבָרֶכְךָ; 1 Sam 14:39; 20:3; 26:16; 1 Kgs 2:23; Isa 45:23.

**Solemnity markers stacked in 12:7:**

1. Two hands raised to heaven (normally oaths raise *one* hand — Gen 14:22; Deut 32:40; Ezek 20:5–6, 15; Rev 10:5). The *two*-hand lift in Dan 12:7 is unique in the MT and intensifies the solemnity.
2. Oath sworn by the eternal Living One (חֵי הָעוֹלָם) — maximum swearing-formula.
3. Content introduced by כִּי — direct quote of the sworn duration.

The effect: the time-period stated is **divinely sealed by double-intensified oath**, not merely reported.

#### 3. וּכְכַלּוֹת נַפֵּץ יַד־עַם־קֹדֶשׁ — Temporal Infinitival Construction

**Parsing:** וּ (conj) + כְ (Prep "when/as") + כַלּוֹת (Verb.**Piel**.InfCon from כלה "complete, finish") + נַפֵּץ (Verb.**Piel**.InfCon from נפץ "shatter"; appears as the construct/governed object of כַלּוֹת).

**Construction:** כ + infinitive-construct is a **temporal clause** — "when/as X is happening" (GKC §114e, JM §166l). Functionally equivalent to a subordinate temporal clause "when the shattering of the holy-people's hand is completed."

**Stacked construct chain (yad-ʿam-qōdeš):** Three links — "hand of people of holiness" = "the hand/power of the holy people." This is a rare three-noun construct chain; parallel to Dan 8:25 שַׂר שָׂרִים "prince of princes" (two-link) and extended patterns like Gen 9:25 עֶבֶד עֲבָדִים (two-link superlative).

**Piel stem choice:**

- כַלָּה (Piel of כלה) = transitive/factitive "bring to completion, finish off" (contrast Qal כָּלָה "come to an end" — as in v.24 תִּכְלֶינָה).
- נַפֵּץ (Piel of נפץ) = intensive/factitive "shatter, dash in pieces." Parallel נפץ Piel in Ps 2:9 (though HMT reads Qal there), Jer 13:14; 51:20–23; 48:12.

The Piel pair builds a **completed-action temporal frame** for v.24 תִּכְלֶינָה כָל־אֵלֶּה (Qal impf. 3fp "all these shall come to an end"). The 3fp agreement is with the feminine-plural understanding of the preceding אֵלֶּה ("these things/events" as a set — fem.pl. agreement with the collective).

**The כ + InfCon governs the end-bracket of the 3.5 time-units:** The oath links two events —
(1) the *duration*: מוֹעֵד מוֹעֲדִים וָחֵצִי;
(2) the *terminus*: כְּכַלּוֹת נַפֵּץ יַד־עַם־קֹדֶשׁ.
Both clauses are apposed to explain *when* "all these" will be finished.

#### 4. תִּכְלֶינָה — Qal Impf. 3fp Feminine-Plural Subject Agreement

**Parsing:** Verb.Qal.Impf.**3fp** from כלה ("come to an end, be completed"). The **3fp** is the rare feminine-plural yiqtol termination (-nâ), the standard paradigmatic 3fp/2fp form (GKC §47k).

**Subject agreement:** כָּל־אֵלֶּה — "all these [things]." אֵלֶּה is common-gender demonstrative plural; the 3fp verb agreement here treats the collective set-of-events (implicit: הַפְּלָאוֹת of v.6, "the wonders") as fem.pl. Note that v.6 asks קֵץ הַפְּלָאוֹת ("end of the wonders"; פְּלָאוֹת is fem.pl.), and the 3fp verb in v.7 agrees with that antecedent.

**Lexical doublet:** Root כלה occurs in both Piel InfCon (כַלּוֹת, "to complete") and Qal Impf. (תִּכְלֶינָה, "shall come to an end") in the same verse — deliberate paronomasia framing the duration.

---

## Daniel 12:11

### Text
**Hebrew:** וּמֵעֵת֙ הוּסַ֣ר הַתָּמִ֔יד וְלָתֵ֖ת שִׁקּ֣וּץ שֹׁמֵ֑ם יָמִ֕ים אֶ֖לֶף מָאתַ֥יִם וְתִשְׁעִֽים׃

**KJV:** "And from the time [that] the daily [sacrifice] shall be taken away, and the abomination that maketh desolate set up, [there shall be] a thousand two hundred and ninety days."

### Word-by-Word Parsing

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | וּ | ו | Conj | and |
| 2 | מֵ | מן | Prep | from |
| 3 | עֵת | עת | Noun.s.**Cst** | time-of |
| 4 | הוּסַר | סור | Verb.**Hophal**.Perf.3ms | (it/he) was removed / caused-to-turn-aside |
| 5 | הַתָּמִיד | תמיד | Noun.ms.Abs + Art | the Continual (daily) |
| 6 | וְ | ו | Conj | and |
| 7 | לָ | ל | Prep | to/for |
| 8 | תֵת | נתן | Verb.**Qal.InfCon** | (the) giving/setting |
| 9 | שִׁקּוּץ | שׁקוץ | Noun.ms.Abs | abomination / detested-thing |
| 10 | שֹׁמֵם | שׁמם | Verb.**Qal.Ptcp**.ms.Abs | desolating / causing-desolation |
| 11 | יָמִים | יום | Noun.**mp**.Abs | days |
| 12 | אֶלֶף | אלף | Noun.s.Abs | thousand |
| 13 | מָאתַיִם | מאה | Noun.**fd**.Abs | two-hundred (dual of מֵאָה) |
| 14 | וְ | ו | Conj | and |
| 15 | תִשְׁעִים | תשׁע | Noun.mp.Abs | ninety |

### Clause Structure

| # | Clause Type | Text | Function |
|---|------------|------|----------|
| 1 | Prep + Cst-chain (Time phrase) | וּמֵעֵת הוּסַר הַתָּמִיד | "and from the time (of) (it-was-)removed the-Continual" |
| 2 | Coord. InfC phrase | וְלָתֵת שִׁקּוּץ שֹׁמֵם | "and (from) the giving (of) an-abomination that-desolates" |
| 3 | NmCl (verbless predicate of duration) | יָמִים אֶלֶף מָאתַיִם וְתִשְׁעִים | "[there shall be] days, 1,000, 200, and 90" |

### Key Grammatical Features — Dan 12:11

#### 1. מֵעֵת הוּסַר — "from the time [of] was-removed" (Relative Asyndeton / Construct-before-Finite-Verb)

The construction עֵת + finite verb (Hophal 3ms הוּסַר) without explicit relative אֲשֶׁר is a **construct-before-finite-verb** (or equivalently, headless relative introduced by an implicit "that/when"):

- עֵת ("time") is parsed Noun.s.**Cst** (construct), despite being followed by a finite verb. GKC §130d and JM §129q catalog the Hebrew construction whereby a noun (esp. a time-noun like עֵת, יוֹם, שָׁנָה) is in construct with a following **verbal clause** treated as a quasi-nominal rection.
- Parallels: Gen 2:4 בְּיוֹם עֲשׂוֹת — "in the day of (God's) making"; Exod 6:28 בְּיוֹם דִּבֶּר יהוה — "in the day (when) YHWH spoke"; 1 Sam 25:15 כָּל־יְמֵי הִתְהַלַּכְנוּ — "all the days (that) we walked about"; Ps 4:8 מֵעֵת דְּגָנָם — "from (the) time (of) their grain."
- Semantic effect: "from [the] time [when] the Continual was removed."

#### 2. הוּסַר — Hophal Perfect 3ms of סור

**Parsing:** Verb.**Hophal** (causative-passive of the Hiphil of סור). The Hiphil הֵסִיר = "cause to depart / remove / take away"; the Hophal הוּסַר = passive thereof, "be caused-to-depart / be removed / be taken away."

**Stem significance:**
- The **Hophal** (rare stem, ~400× total in MT) is the passive of the Hiphil — it identifies an **external agent** without naming one. This is the Hebrew structural equivalent of the Greek "**divine passive**" or the Latin passive of agency-suppression. The agent of the removal is syntactically unspecified.
- Cross-reference: [Niphal Stem](../hebrew/stem-niphal.md) for related passive semantics. The Hophal of סור elsewhere: 2 Sam 20:12 (Hophal); Dan 11:31 הוּסַר (identical form — deliberate linkage between 11:31 and 12:11); Isa 17:1 (Hophal of מוּסָר).
- **Daniel 11:31 ‖ Daniel 12:11 lexical bracket:** Both verses use the identical Hophal form הוּסַר + subject הַתָּמִיד, marking Dan 12:11 as a **resumption / quantification** of the Dan 11:31 event rather than an independent prediction.

#### 3. הַתָּמִיד — Substantivized Adjective "the Continual"

**Parsing:** Noun.ms.Abs + Art (lemma תמיד, gloss "continuity"). Originally an **adverb** ("continually, regularly"), תָּמִיד is substantivized with the article in Daniel's apocalyptic vocabulary (Dan 8:11, 12, 13; 11:31; 12:11) to denote the continually-offered cultic provision.

**The crux:** The word **lacks an explicit complement** (no עוֹלָה, no זֶבַח). KJV and most English versions bracket "[sacrifice]" — the bracket is not in the Hebrew. The noun is elliptical and the *referent* of the ellipsis is interpretively contested (see word study [temid](../../word-studies/temid.md) if present).

**Candidate supplied referents in the tradition:**

| Supplied noun | Meaning | Supporting passages |
|---------------|---------|---------------------|
| עֹלָה / תָּמִיד עֹלַת | "continual burnt-offering" (daily tamid lamb) | Exod 29:38–42; Num 28:3–8 |
| זֶבַח | "continual sacrifice" | generic |
| מִנְחָה | "continual grain-offering" | Num 4:16 |
| עֲבֹדָה | "continual service / temple ministry" | whole cultus-as-system |
| Christ's heavenly-sanctuary ministry (historicist) | truth of continual mediation | symbolic |

All five readings are grammatically possible. The grammar supplies only "the Continual"; the referent is supplied by interpretive framework.

#### 4. וְלָתֵת שִׁקּוּץ שֹׁמֵם — Infinitival "Setting up the Abomination that Desolates"

**Parsing:**
- וְלָתֵת — Conj + Prep ל + Verb.**Qal.InfCon** of נתן ("give"). Here נתן carries the sense "**set up / install / place**" (Deut 14:26; 1 Kgs 2:24).
- שִׁקּוּץ — Noun.ms.Abs, "detestable thing / abomination" (from שׁקץ "abhor"). Appears ~28× in MT; often paired with idols or ritually detested objects (Deut 29:17 [Eng 16]; 1 Kgs 11:5, 7; Jer 4:1; Ezek 5:11; Hos 9:10).
- שֹׁמֵם — Verb.Qal.**Ptcp**.ms.Abs of שׁמם ("be desolate/appalled"). As an **active participle** modifying שִׁקּוּץ, it is the substantivized/attributive-participle construction "abomination [that is] desolating / that causes desolation." The Qal of שׁמם is sometimes stative/intransitive ("be appalled, be desolate"), sometimes transitive-active ("cause desolation"); the participle absorbs both senses.

**Linked forms of the phrase in Daniel:**
- Dan 9:27 — שִׁקּוּצִים מְשֹׁמֵם (plural noun + **Poel** participle, "abominations of a desolator / on wing of abominations one-who-desolates")
- Dan 11:31 — הַשִּׁקּוּץ מְשׁוֹמֵם (sg. + Poel participle + definite article)
- Dan 12:11 — שִׁקּוּץ שֹׁמֵם (sg. + **Qal** participle — the lightest form)
- 1 Macc 1:54 — βδέλυγμα ἐρημώσεως (Antiochene precedent)
- LXX-Theodotion of Daniel renders all three with τὸ βδέλυγμα τῆς ἐρημώσεως
- Mat 24:15 ‖ Mk 13:14 cite this phrase explicitly (τὸ βδέλυγμα τῆς ἐρημώσεως); see [mat-24-15-mk-13-14-abomination](mat-24-15-mk-13-14-abomination.md).

**The ל + InfCon parallel to the preceding finite verb:** The Hebrew parallels two events —
(a) מֵעֵת הוּסַר הַתָּמִיד ("from-the-time was-removed the-Continual") and
(b) וְלָתֵת שִׁקּוּץ שֹׁמֵם ("and to-set-up the-abomination that-desolates").
The ל + InfCon in (b) coordinates with the מֵ in (a) — "from [the time of] X, **and** [from the time] of Y." Both events jointly anchor the start-point of the 1,290-day count.

#### 5. יָמִים אֶלֶף מָאתַיִם וְתִשְׁעִים — The Numeral Phrase

**Parsing & syntax:**
- יָמִים (Noun.mp.Abs "days") — heads the numeral phrase; placed **first** in the counted-noun construction (an exegetically significant word-order choice).
- אֶלֶף — "thousand" (Noun.s.Abs).
- מָאתַיִם — Noun.**fd**.Abs; "two-hundred" is the **dual** of מֵאָה ("hundred"). This is a morphologically marked **true dual**: מֵאָה → מָאתַיִם is one of Hebrew's surviving dual formations (cf. שְׁנָתַיִם "two years," יוֹמַיִם "two days"). The form is unambiguously "exactly two hundred" — *not* a plural-with-indefinite-count.
- וְתִשְׁעִים — "and ninety" (tens-pl. formation).

**Total:** 1,000 + 200 + 90 = **1,290 days**.

**Counted-noun word order in Hebrew numerals:**

In BH, numerals ≥ 100 almost always **precede** the counted noun (Gen 5:5 תְּשַׁע מֵאוֹת שָׁנָה, "nine hundred years"; Num 1:46 שֵׁשׁ־מֵאוֹת אֶלֶף וּשְׁלֹשֶׁת אֲלָפִים וַחֲמֵשׁ מֵאוֹת וַחֲמִשִּׁים). The counted-noun-**first** word order of Dan 12:11 (יָמִים אֶלֶף מָאתַיִם וְתִשְׁעִים) is **unusual**. The same pattern recurs in 12:12 (יָמִים אֶלֶף שְׁלֹשׁ מֵאוֹת …). Possible functions:
- **Topicalization/focus** — "as for days: 1,290" — foregrounding *duration* as the predicated measure.
- **Cardinal-appositive apposition** — nominal clause "[they are] days, [namely] 1,290."
- **Rhetorical count-down form** — apocalyptic numerological emphasis (cf. the parallel 12:12 pattern, and the exact-day counts in Dan 8:14 ʿereḇ bōqer 2,300).

Note that Dan 8:14 (עַד עֶרֶב בֹּקֶר אַלְפַּיִם וּשְׁלֹשׁ מֵאוֹת, "until evening-morning 2,300") uses the dual אַלְפַּיִם for "two thousand" — another marked numerical dual in Daniel's apocalyptic arithmetic. See [dan-8-14](dan-8-14.md).

---

## Daniel 12:12

### Text
**Hebrew:** אַשְׁרֵ֥י הַֽמְחַכֶּ֖ה וְיַגִּ֑יעַ לְיָמִ֕ים אֶ֕לֶף שְׁלֹ֥שׁ מֵא֖וֹת שְׁלֹשִׁ֥ים וַחֲמִשָּֽׁה׃

**KJV:** "Blessed [is] he that waiteth, and cometh to the thousand three hundred and five and thirty days."

### Word-by-Word Parsing

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | אַשְׁרֵי | אשׁר | Noun.**mp.Cst** | happinesses-of / blessings-of |
| 2 | הַ | ה | Art | the |
| 3 | מְחַכֶּה | חכה | Verb.**Piel.Ptcp**.ms.Abs | one-waiting / who waits |
| 4 | וְ | ו | Conj | and |
| 5 | יַגִּיעַ | נגע | Verb.**Hiphil.Impf**.3ms | he shall arrive / reach / attain |
| 6 | לְ | ל | Prep | to |
| 7 | יָמִים | יום | Noun.mp.Abs | days |
| 8 | אֶלֶף | אלף | Noun.s.Abs | thousand |
| 9 | שְׁלֹשׁ | שׁלשׁ | Noun.s.**Cst** | three(-hundreds) |
| 10 | מֵאוֹת | מאה | Noun.**fp**.Abs | hundreds |
| 11 | שְׁלֹשִׁים | שׁלשׁ | Noun.mp.Abs | thirty (tens-form) |
| 12 | וַחֲמִשָּׁה | חמשׁ | Conj + Noun.fs.Abs | and five |

### Clause Structure

| # | Clause Type | Text | Function |
|---|------------|------|----------|
| 1 | NmCl (beatitude formula) | אַשְׁרֵי הַמְחַכֶּה | "blessed (is) the one waiting" |
| 2 | WeYiqtol (coordinated prospective) | וְיַגִּיעַ לְיָמִים … | "and he reaches/attains to 1,335 days" |

### Key Grammatical Features — Dan 12:12

#### 1. אַשְׁרֵי + Substantivized Participle — The Beatitude Formula

**Parsing:** אַשְׁרֵי is a **masculine-plural construct noun** (plurale tantum in cst form) from the root אשׁר ("to bless, pronounce happy"). Morphologically frozen as a **beatitude formula**: "[the] happinesses-of [the one who] …" = "how blessed is the one who …!" GKC §124f catalogs it as an exclamatory construct-plural (similar to כֹּהֲנֵי יהוה "priests of YHWH" structurally, but exclamatory-fossilized).

**Pattern parallels:**

| Reference | Text |
|-----------|------|
| Ps 1:1 | אַשְׁרֵי־הָאִישׁ אֲשֶׁר… "Blessed (is) the-man who…" |
| Ps 32:1–2 | אַשְׁרֵי נְשׂוּי־פֶּשַׁע; אַשְׁרֵי אָדָם… |
| Ps 84:5, 6, 13 | threefold אַשְׁרֵי |
| Ps 112:1; 119:1–2; 128:1 | wisdom-torah beatitude |
| Prov 8:32, 34 | wisdom personified |
| Isa 30:18 | אַשְׁרֵי כָּל־חוֹכֵי לוֹ ("blessed are all who wait for Him") — **closest lexical parallel to Dan 12:12** (חוֹכֵי is Qal ptcp. of חכה) |
| Dan 12:12 | אַשְׁרֵי הַמְחַכֶּה (Piel ptcp.) |

The formula takes either an אֲשֶׁר + finite-verb relative clause (Ps 1:1) **or** a substantivized participle (Dan 12:12) as its complement.

**Participle:** הַמְחַכֶּה — Verb.**Piel**.Ptcp.ms.Abs of חכה ("wait, tarry, long for"). חכה is a Piel-only / near-Piel-only verb in BH (~14× total; most forms Piel). Piel adds intensive/durative coloring: "one who *eagerly/persistently* waits."

#### 2. וְיַגִּיעַ — WeYiqtol (Hiphil) "and he shall reach"

**Parsing:** Verb.**Hiphil.Impf**.3ms of נגע ("touch, reach, arrive at"). Prefixed by weaw conjunctive + prefixed yiqtol. In this context the form is a **weyiqtol** (waw + yiqtol), not a weqatal. Functionally the weyiqtol coordinates with the substantivized-participle subject: "(the one) waiting, and-he-reaches."

**Hiphil of נגע semantics:**
- Qal נגע = "touch, strike."
- Hiphil הִגִּיעַ = causative or ingressive "cause to touch / reach / attain to / arrive at." With לְ + goal: "attain to (a time/place/number)" — Est 2:12, 15; 4:14; 8:17; 9:1; 1 Sam 14:9; 2 Sam 20:13.
- In Dan 12:12 the goal is לְיָמִים אֶלֶף שְׁלֹשׁ מֵאוֹת שְׁלֹשִׁים וַחֲמִשָּׁה — attaining the **1,335-day** terminus.

**Subject continuity:** The subject of וְיַגִּיעַ is the participle-phrase הַמְחַכֶּה. Hebrew participle-plus-weyiqtol chains regularly maintain subject identity (cf. Jer 17:7 אַשְׁרֵי הַגֶּבֶר אֲשֶׁר יִבְטַח בַּיהוה — subject continues under waw). The force is "*blessed is the one* who waits *and (who) attains*."

**Alternative parsing (minority):** Some grammarians (e.g., Montgomery, *ICC* Daniel) read וְיַגִּיעַ as a jussive-like optative ("may he reach"). The consonantal form is identical; the masoretic vocalization supports the simple imperfect. Either reading preserves the same lexical content.

#### 3. לְיָמִים אֶלֶף שְׁלֹשׁ מֵאוֹת שְׁלֹשִׁים וַחֲמִשָּׁה — The 1,335 Numeral

**Parsing & arithmetic:**
- לְיָמִים — Prep ל + Noun.mp.Abs "to/as-far-as days." Goal of יַגִּיעַ.
- אֶלֶף — 1,000.
- שְׁלֹשׁ מֵאוֹת — "three (of) hundreds" = **300**. שְׁלֹשׁ is in construct; מֵאוֹת is f.pl. of מֵאָה. Standard BH numerical construct chain (contrast the **dual** מָאתַיִם in v.11).
- שְׁלֹשִׁים — tens-formation of שׁלשׁ = **30**.
- וַחֲמִשָּׁה — "and five" (f.sg. form because counted unit "day" is masculine, triggering chiastic-gender agreement: masculine noun → feminine-form cardinal 3–10, a BH rule — GKC §97a, JM §100d).

**Total:** 1,000 + 300 + 30 + 5 = **1,335 days**.

**Difference from v.11:** 1,335 − 1,290 = **45 days**. The grammar itself does not explain the 45-day gap; the text simply pairs two terminus-counts from the same start-point.

**Word-order parallel to v.11:** Same counted-noun-first pattern (יָמִים אֶלֶף…). The pairing is deliberate and structural.

---

## Cross-Verse Syntactic & Lexical Links

### 1. Triple Time-Formula Bracket (Dan 12:7, 12:11, 12:12)

| Verse | Formula | Morphology |
|-------|---------|-----------|
| 12:7 | לְמוֹעֵד מוֹעֲדִים וָחֵצִי | noun + m.pl. + "half" — **indefinite plural** |
| 12:11 | אֶלֶף מָאתַיִם וְתִשְׁעִים | 1000 + **dual** 200 + 90 — **exact cardinal** |
| 12:12 | אֶלֶף שְׁלֹשׁ מֵאוֹת שְׁלֹשִׁים וַחֲמִשָּׁה | 1000 + 300 + 30 + 5 — **exact cardinal** |

The shift **from indeterminate "time, times, and half"** (v.7) to **two exact day-counts** (vv.11–12) is a deliberate rhetorical move from oath-language (formulaic) to calendrical specification (numerical).

### 2. "Daily Removed" (הוּסַר הַתָּמִיד) Links Dan 11:31 ‖ 12:11

Exact formulaic identity:
- Dan 11:31 — וְהֵסִירוּ הַתָּמִיד (Hiphil 3mp perfect + object) "and they shall remove the Continual"
- Dan 12:11 — מֵעֵת הוּסַר הַתָּמִיד (Hophal 3ms perfect passive) "from-the-time the Continual was-removed"

Stem shift (**Hiphil active in 11:31 → Hophal passive in 12:11**) reframes the same event from agent-focused (11:31: "they shall remove") to consequence-focused (12:11: "was-removed"). The Hophal agent-suppression allows theological framing of the act as a consequential fact-on-the-ground regardless of the human agent.

### 3. Greek Retrieval in NT

- **Rev 12:14** καιρὸν καὶ καιροὺς καὶ ἥμισυ καιροῦ ≈ **Dan 12:7** MT מוֹעֵד מוֹעֲדִים וָחֵצִי ≈ **Dan 7:25** Aramaic עִדָּן וְעִדָּנִין וּפְלַג עִדָּן. See [Rev 11-12 time markers](rev-11-12-time-markers.md).
- **Mat 24:15 ‖ Mk 13:14** τὸ βδέλυγμα τῆς ἐρημώσεως ≈ **Dan 12:11** שִׁקּוּץ שֹׁמֵם (also Dan 9:27; 11:31). See [mat-24-15-mk-13-14-abomination](mat-24-15-mk-13-14-abomination.md).
- **Dan 7:25** ‖ 12:7 linkage: both have the self-same time-time-half formula (Aramaic / Hebrew). See [dan-7-25-26](dan-7-25-26.md).

### 4. Day-for-Year Principle (Grammar-Neutral Catalogue)

The question whether the "days" of 12:11–12 are literal 24-hour days or prophetic-day = year units is **exegetical / hermeneutical**, not grammatical. The grammar of יָמִים ("days") is ordinary plural of יוֹם and neither mandates nor excludes a symbolic transformation. Positions documented:

| Position | Treatment of יָמִים | Result |
|----------|---------------------|--------|
| Preterist / Antiochene | Literal days | ~3½ years of persecution under Antiochus IV Epiphanes (168–165 BCE); 1,290 ≈ Dec 168 BCE to Dec 164 BCE; 1,335 adds 45 days |
| Futurist / dispensational | Literal days | Tribulation-period count during final 3½-year Great Tribulation |
| Historicist / year-day | Prophetic day = solar year | 1,260-year, 1,290-year, and 1,335-year spans; Num 14:34 + Ezek 4:6 as principle |
| Symbolic-idealist | Symbolic indefinite | Durational symbol of suffering, not a calendar count |

The grammar supplies יָמִים ("days"), plural, ordinary lemma. The interpretive transform is not grammatical but hermeneutical.

---

## Cross-References

### Grammar Library
- [Niphal Stem](../hebrew/stem-niphal.md) — background on וַיִּשָּׁבַע (Niphal wayyiqtol of שׁבע in the oath formula).
- [Waw Conjunction](../hebrew/syntax-waw-conjunction.md) — polyfunctional waw in וָחֵצִי, וְלָתֵת, וְיַגִּיעַ.
- [WX-QATAL Circumstantial Clause](../hebrew/syntax-wx-qatal-circumstantial.md) — comparable waw + non-verb + qatal construction (not present here but useful contrast with the waw+yiqtol pattern of 12:12).

### Passage Analyses
- [Daniel 7:25-26](dan-7-25-26.md) — Aramaic parallel עִדָּן וְעִדָּנִין וּפְלַג עִדָּן; little-horn persecution clock.
- [Daniel 8:14](dan-8-14.md) — 2,300 ʿereḇ bōqer; dual אַלְפַּיִם parallel.
- [Daniel 8:23-25](dan-8-23-25.md) — little-horn interpretation oracle.
- [Daniel 11:36-37](dan-11-36-37.md) — self-exalting king; הֵסִירוּ הַתָּמִיד foreshadow.
- [Revelation 11-12 Time Markers](rev-11-12-time-markers.md) — 42 months / 1,260 days / time-times-half in Greek; direct descendant of Dan 12:7.
- [Matthew 24:15 ‖ Mark 13:14](mat-24-15-mk-13-14-abomination.md) — NT citation of שִׁקּוּץ שֹׁמֵם.
- [Revelation 13:1-10](rev-13-1-10.md) — 42-month beast reign; ἐδόθη divine-passive framework.

### Interpretive Schools (Context-Neutral Catalogue)
All grammatical points above are compatible with:
- **Antiochene / preterist**: 1,290/1,335 literal days spanning the 168–164 BCE desolation/restoration of the Jerusalem temple.
- **Futurist / dispensational**: 1,290/1,335 literal days in a future 3½-year Great Tribulation.
- **Historicist / year-day**: 1,290/1,335 years measuring the papal/Islamic/ecclesiastical desolation period, variously dated (e.g., 508/538 CE to 1798/1843/1844 CE in Adventist historicism).
- **Symbolic / idealist**: non-calendrical duration symbols.

The grammar neither forces nor forbids any of these readings; each is compatible with the Hebrew as parsed.

---

## Summary Grammatical Inventory

| Feature | Verse | Form | Key point |
|---------|-------|------|-----------|
| Wayyiqtol narrative chain | 12:7 | וָאֶשְׁמַע, וַיָּרֶם, וַיִּשָּׁבַע | 1cs + 3ms + 3ms Niphal swear |
| Oath-formula + כִּי content | 12:7 | נִשְׁבַּע בְּחֵי הָעוֹלָם כִּי | declarative כִּי after oath |
| 3-link construct chain | 12:7 | יַד־עַם־קֹדֶשׁ | nested genitives |
| כ + Piel InfCon (temporal) | 12:7 | כְכַלּוֹת נַפֵּץ | temporal subord. |
| Qal Impf. 3fp | 12:7 | תִּכְלֶינָה | rare fem.pl. ending -nâ |
| Cst-noun + finite verb | 12:11 | מֵעֵת הוּסַר | headless relative |
| Hophal perfect | 12:11 | הוּסַר | agent-suppressing passive |
| ל + InfCon (coord. event) | 12:11 | וְלָתֵת | "and (from) the setting-up" |
| Qal ptcp. attributive | 12:11 | שֹׁמֵם | "(that) desolates" modifying שִׁקּוּץ |
| Marked dual numeral | 12:11 | מָאתַיִם | exact 200 (not indefinite) |
| Beatitude formula | 12:12 | אַשְׁרֵי הַמְחַכֶּה | cst-pl noun + subst. ptcp. |
| Piel participle of חכה | 12:12 | הַמְחַכֶּה | intensive "one waiting" |
| Weyiqtol subject-continuity | 12:12 | וְיַגִּיעַ | participial subject continues |
| Hiphil of נגע + לְ goal | 12:12 | יַגִּיעַ לְיָמִים | "attain to days" |
| Counted-noun first order | 12:11, 12:12 | יָמִים אֶלֶף… | marked topicalization |
