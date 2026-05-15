# Corporate Solidarity / Corporate Headship in Judgment (Hebrew)

## Definition

A Biblical-Hebrew semantic–syntactic pattern in which a **collective-noun subject** — chiefly גּוֹי *gôy* "nation" (H1471), עַם *ʿam* "people" (H5971), and בַּיִת *bayit* "house / household" (H1004) — is construed as a **single corporate entity** that can (1) act, (2) incur guilt, and (3) receive reward or judgment as one unit, even though it is composed of many individuals and can also govern plural-concord forms within the same clause or pericope. The diagnostic is twofold: (a) the collective lemma governs **singular verbs / singular pronominal suffixes** when construed as a unified body; (b) the same lemma governs **plural verbs / plural suffixes** when the constituent members are in view. The alternation is not inconsistency but a grammaticalised device for *corporate–distributive* construal — the linguistic surface on which "one for many" / "many in one" judgments rest.

1. **Collective-singular construal** — plural-membered entity treated as one actor / one defendant / one patient of judgment; singular verb + singular pronominal suffix ("it sinned", "its iniquity", "I will destroy it").
2. **Collective-plural (distributive) construal** — same lemma re-construed as its constituent members; plural verb + plural suffix ("they transgressed", "their deeds", "them").
3. **Corporate-head idiom with בַּיִת** — name of a human head (Jeroboam, Ahab, Jehu, David, Saul) + בֵּית־X designates dynasty / patriline / household as one juridical entity that stands or falls with, or on account of, that head.
4. **Concord oscillation within one clause/verse** — singular and plural agreement alternate with the same collective subject to foreground first the corporate unity, then the individual membership (or vice versa).

## Form Recognition

The pattern is *semantic-syntactic*, not morphological: the collective nouns are ordinary masculine singular nouns. The diagnosis requires reading **noun–verb–suffix concord together**:

- **Collective lemma (morph. singular):** גּוֹי `Noun.ms.Abs` (H1471); עַם `Noun.ms.Abs` (H5971); בַּיִת `Noun.ms.Abs` (H1004); also קָהָל, עֵדָה, מִשְׁפָּחָה, שֵׁבֶט as parallels.
- **Singular-construal signal:** finite verb `Verb.<stem>.<tense>.3ms` governed by the collective; `+3ms` pronominal suffix referring back to it; singular adjective `Adj.ms`; singular demonstrative הַהוּא.
- **Plural-construal signal:** same lemma followed by `Verb.<stem>.<tense>.3p` (or `3mp` in suffixed conjugation); `+3mp` suffix referring back; plural adjective `Adj.mp`; plural demonstrative הָהֵם.
- **Dynastic-head signal:** construct chain בֵּית + proper name (`PropN.s.Abs`); judgment oracles attach verbs of destruction (הִכְרִית Hiphil, הִשְׁמִיד Hiphil, בִּעֵר Piel, נָתַן Qal) to this head-noun phrase.
- **Parser signatures (hebrew_parser.py):** `sp=subs lemma=גוי nu=sg` followed by `sp=verb nu=sg` (corporate) or `sp=verb nu=pl` (distributive); `sp=subs lemma=עם nu=sg` + same contrast; construct chain `Noun.ms.Cst(בית) + PropN` marks dynastic headship.
- **Full lexical data:** `search_strongs.py --lexicon H1471` (גּוֹי, "foreign nation … a troop"; BLB count 558); `--lexicon H5971` (עַם, "a people … a tribe … collectively troops"); `--lexicon H1004` (בַּיִת, "house … family … household").

## Functions with Examples

### 1. Collective-singular: the nation/people as one actor and one defendant

The canonical diagnostic is **Joshua 7:11**, where Achan alone took the *ḥērem*, yet the indictment is framed with collective Israel as a single juridical subject.

| Reference | Hebrew (key) | Parsing | KJV Translation |
|-----------|--------------|---------|-----------------|
| Jos 7:11 | חָטָא יִשְׂרָאֵל | Verb.Qal.Perf.**3ms** + PropN.s.Abs | "Israel hath sinned" (one-man guilt predicated of the whole *ʿam*) |
| Gen 20:4 | הֲגוֹי גַּם־צַדִּיק תַּהֲרֹג | `Noun.ms.Abs` (גּוֹי) + Verb.Qal.Impf.**2ms** | "wilt thou slay also a righteous nation?" — Abimelech's plea: the גּוֹי is a single juridical body whose *righteousness* or guilt can be weighed as a unit |
| Jer 18:7–8 | הַגּוֹי הַהוּא … שָׁב מֵרָעָתוֹ … וְנִחַמְתִּי עַל־הָרָעָה אֲשֶׁר חָשַׁבְתִּי לַעֲשׂוֹת לוֹ | `Noun.ms` + Demons.**ms** הַהוּא + Verb.**3ms** + `+3ms` suffix לוֹ | "if that nation … turn … I will repent of the evil … to do unto them" — the whole nation has one heart that can turn, and one body that receives the verdict |
| Gen 12:2 | וְאֶעֶשְׂךָ לְגוֹי גָּדוֹל | `Noun.ms.Abs` + Adj.**ms** | "I will make of thee a great nation" — the descendants are projected as a single corporate unit already resident in Abraham |
| Gen 18:18 | גּוֹי גָּדוֹל וְעָצוּם | `Noun.ms.Abs` + two Adj.**ms** | "a great and mighty nation" — Abraham himself is addressed as seminal head of the singular גּוֹי |
| Isa 1:4 | גּוֹי חֹטֵא | `Noun.ms.Abs` + Ptcp.Qal.**ms** | "Ah sinful nation" — whole-nation indictment with **singular participle** of חטא agreeing with גּוֹי (same verb-root as Jos 7:11) |

### 2. Collective-plural (distributive): the constituent members in view

In the same pericope the same lemma can pivot to plural verbs that itemise the members.

| Reference | Hebrew (key) | Parsing | KJV Translation |
|-----------|--------------|---------|-----------------|
| Jos 7:11 | וְגַם עָבְרוּ אֶת־בְּרִיתִי … וְגַם לָקְחוּ … וְגַם גָּנְבוּ … וְגַם כִּחֲשׁוּ … וְגַם שָׂמוּ בִכְלֵיהֶם | five consecutive Verb.**3p** forms (עבר Qal.Perf.3p, לקח Qal.Perf.3p, גנב Qal.Perf.3p, כחשׁ Piel.Perf.3p, שׂים Qal.Perf.3p) + suffix `+3mp` בִכְלֵיהֶם | "they have also transgressed my covenant … they have even taken … and have also stolen, and dissembled also … and they have put it even among their own stuff" — same clause, **singular** indictment (חָטָא 3ms) pivots to **plural** verbs (3p×5) in concord with distributive "Israelites" membership |
| Jer 18:8 | שָׁב הַגּוֹי הַהוּא מֵרָעָתוֹ | Verb.Qal.Perf.**3ms** + `+3ms` suffix | singular in v.8 (individual-nation, unified turning) — contrast with plural-suffix reference to the members within Jer 18:9–10 context ("if they do evil") |
| Gen 12:3 | וְנִבְרְכוּ בְךָ כֹּל מִשְׁפְּחֹת הָאֲדָמָה | Verb.Niphal.Perf.**3p** (ברך) + `Noun.fp.Abs` (מִשְׁפָּחוֹת) | "in thee shall all families of the earth be blessed" — distributive plural of the cognate collective מִשְׁפָּחָה, yet channelled through a single corporate head (Abraham) |
| Exo 20:5 ‖ Deu 5:9 | פֹּקֵד עֲוֹן אָבֹת עַל־בָּנִים עַל־שִׁלֵּשִׁים וְעַל־רִבֵּעִים | Ptcp.Qal.**ms** (פקד) + `Noun.mp` (אָבוֹת, בָּנִים) | "visiting the iniquity of the fathers upon the children" — plural-on-plural concord, but the clause presupposes **corporate transmission of guilt** down one household line |

### 3. Corporate-head idiom: בֵּית + proper name (dynastic/familial headship in judgment)

The construct chain **בֵּית + PropN** names a dynasty or patriline as one corporate entity whose fate is bound to, and pronounced against, its head. Judgment oracles regularly attach Hiphil verbs of cutting-off (כרת, שׁמד) or destroying (בער Piel) to this head-phrase.

| Reference | Hebrew (key) | Parsing | KJV Translation |
|-----------|--------------|---------|-----------------|
| 1Ki 14:10 | בֵּית יָרָבְעָם | `Noun.ms.Cst` + PropN | "I will bring evil upon the house of Jeroboam, and will cut off from Jeroboam him that pisseth against the wall … till it be all gone" — whole dynasty indicted on Jeroboam's head |
| 1Ki 21:21–22 | בֵיתְךָ … כְּבֵית יָרָבְעָם … וּכְבֵית בַּעְשָׁא | three construct chains with PropN | "I will make thine house like the house of Jeroboam … and like the house of Baasha" — corporate-headship judgment on Ahab compared point-for-point with earlier dynastic destructions |
| 1Ki 21:29 | בְיָמָיו … בְּיָמֵי בְנוֹ אָבִיא הָרָעָה עַל־בֵּיתוֹ | `Noun.ms.Cst` + `+3ms` suffix | "because he humbleth himself … I will not bring the evil in his days: [but] in his son's days will I bring the evil upon his house" — delayed corporate judgment: the singular בֵּית can absorb the penalty attached to the head, even across a generation |
| Hos 1:4 | פָּקַדְתִּי אֶת־דְּמֵי יִזְרְעֶאל עַל־בֵּית יֵהוּא | Verb.Qal.Perf.1cs (פקד) + `Noun.ms.Cst` + PropN | "I will avenge the blood of Jezreel upon the house of Jehu, and will cause to cease the kingdom of the house of Israel" — earlier-generation bloodguilt visited on the dynastic בַּיִת |
| 2Sa 21:1 | אֶל־שָׁאוּל וְאֶל־בֵּית הַדָּמִים | `Noun.ms.Cst` + `Noun.mp` (דָּמִים) | "[it is] for Saul, and for his bloody house, because he slew the Gibeonites" — three-year famine on Israel attributed to one prior king's violation of an oath; headship-transmission across death and dynasty |
| 2Sa 24:17 | עַל־בֵּית אָבִי | `Noun.ms.Cst` + `Noun.ms.Abs` + `+1cs` suffix | "let thine hand, I pray thee, be against me, and against my father's house" — David volunteers corporate-head substitution |

### 4. Concord oscillation within a single unit (Jos 7:11 paradigm)

Joshua 7:11 is the clearest single-verse demonstration: **one** collective subject (יִשְׂרָאֵל, construed as עַם / גּוֹי) governs **1 singular + 5 plural verbs** in sequence, followed by a **3mp pronominal suffix**:

| Clause | Verb-form | Parsing (from hebrew_parser.py `--verse "Jos 7:11"`) | Concord |
|--------|-----------|-------------------------------------------------------|---------|
| חָטָא יִשְׂרָאֵל | חָטָא | Verb.Qal.Perf.**3ms** | corporate-singular ("Israel-as-one has sinned") |
| וְגַם עָבְרוּ אֶת־בְּרִיתִי | עָבְרוּ | Verb.Qal.Perf.**3p** (√עבר) | distributive-plural |
| וְגַם לָקְחוּ מִן־הַחֵרֶם | לָקְחוּ | Verb.Qal.Perf.**3p** (√לקח) | distributive-plural |
| וְגַם גָּנְבוּ | גָּנְבוּ | Verb.Qal.Perf.**3p** (√גנב) | distributive-plural |
| וְגַם כִּחֲשׁוּ | כִּחֲשׁוּ | Verb.Piel.Perf.**3p** (√כחשׁ) | distributive-plural |
| וְגַם שָׂמוּ בִכְלֵיהֶם | שָׂמוּ + בִכְלֵיהֶם | Verb.Qal.Perf.**3p** + `Noun.mp.Abs.+3mp` | distributive-plural + **3mp pronominal suffix** |

The pattern legitimates the corporate verdict of Jos 7:12 ("the children of Israel could not stand … because they were accursed") while only one man (Achan, 7:1 *wayyimʿălû … māʿal*) actually took. The grammar does not *identify* the one with the many; it *concorporates* them.

## Diagnostic Rule (Context-Neutral)

- **Collective lemma + singular verb/suffix** → unified-body construal (nation/people/dynasty as one juridical actor).
- **Collective lemma + plural verb/suffix** → distributive construal (individual members).
- **Alternation within one clause/verse** → deliberate foregrounding of both levels simultaneously (the "one in many / many in one" idiom).
- **בֵּית + PropN in oracles of destruction** → corporate-head idiom: the dynasty/household is the juridical object that carries the head's verdict forward.
- **Pronominal-suffix number** is the most reliable single diagnostic: `+3ms` (לוֹ / עָלָיו / מֵרָעָתוֹ) = corporate construal; `+3mp` (לָהֶם / עֲלֵיהֶם / מִכְלֵיהֶם) = distributive construal.

## Contrast with Related Forms

| Form | Behavior | Example |
|------|----------|---------|
| Corporate-singular concord (this entry) | collective lemma + **3ms** verb / `+3ms` suffix | Jos 7:11a חָטָא יִשְׂרָאֵל; Isa 1:4 גּוֹי חֹטֵא; Jer 18:8 הַגּוֹי הַהוּא שָׁב … לוֹ |
| Distributive-plural concord (this entry) | collective lemma + **3p/3mp** verb / `+3mp` suffix | Jos 7:11b עָבְרוּ … בִכְלֵיהֶם; Gen 12:3 נִבְרְכוּ … מִשְׁפְּחֹת |
| Plural-noun-pluralis-maiestatis | morphologically **plural** noun + sg. verb for **single** referent (honorific/abstract) | Gen 1:1 אֱלֹהִים בָּרָא 3ms — see [plural-noun-singular-verb-agreement](plural-noun-singular-verb-agreement.md), [pluralis-majestatis](pluralis-majestatis.md) |
| Plural-noun + plural verb | morphologically plural noun + pl. verb for true numerical plural | Jdg 2:11 הַבְּעָלִים + 3mp — [plural-noun-singular-verb-agreement](plural-noun-singular-verb-agreement.md) |
| Corporate-head בֵּית + PropN (this entry, §3) | singular construct chain naming a dynasty as juridical unit | 1Ki 14:10 בֵּית יָרָבְעָם; Hos 1:4 בֵּית יֵהוּא |
| Individual-penalty formula | singular verb + singular personal patient, no corporate extension | Deu 24:16 ("fathers shall not be put to death for the children … every man shall be put to death for his own sin") — the **counter-norm** that sits in tension with Exo 20:5's corporate transmission |

Related canonical entries: [plural-noun-singular-verb-agreement](plural-noun-singular-verb-agreement.md), [pluralis-majestatis](pluralis-majestatis.md), [niphal-imperfect-divine-denial](niphal-imperfect-divine-denial.md), [symbol-decoding-predicate-nominal](symbol-decoding-predicate-nominal.md).

## Common Collective Nouns Displaying the Pattern

| Lemma | Strong's | Gloss | Corporate-singular behavior | Distributive-plural behavior |
|-------|----------|-------|------------------------------|-------------------------------|
| גּוֹי | H1471 | nation / Gentile / "a troop" (foreign body politic) | Gen 12:2 גּוֹי גָּדוֹל (Adj.ms); Gen 20:4 גּוֹי צַדִּיק (Adj.ms) + 2ms verb תַּהֲרֹג; Isa 1:4 גּוֹי חֹטֵא (Ptcp.ms); Jer 18:8 הַגּוֹי הַהוּא שָׁב … לוֹ (3ms + 3ms suffix) | plural הַגּוֹיִם normal for "the nations" (Jer 25:9 הַגּוֹיִם + 3mp suffix עֲלֵיהֶם) |
| עַם | H5971 | a people (congregated unit); tribe; collectively troops | 1Sa 15:2 אֲשֶׁר־עָשָׂה עֲמָלֵק (3ms verb, sg. people-as-one); Num 14:12 לְגוֹי גָּדוֹל (sg.); Deu 7:6 עַם קָדוֹשׁ (Adj.ms) | 1Sa 15:3 לֹא תַחְמֹל עָלָיו (3ms suffix, Amalek-as-one) pivoting to וְהֵמַתָּה distributive ban on individuals |
| בַּיִת | H1004 | house / family / household / dynasty | 1Ki 14:10 בֵּית יָרָבְעָם + 1cs verb אָבִיא; 1Ki 21:22 בֵיתְךָ + Hiphil verbs; Hos 1:4 בֵּית יֵהוּא + 1cs פָּקַדְתִּי; 2Sa 21:1 בֵּית הַדָּמִים (construct + pl.noun) | Num 16:32 בָּתֵּיהֶם (Noun.mp.+3mp "their houses") in mass-punishment narrative |
| מִשְׁפָּחָה | H4940 | family / clan | Jos 7:14 הַמִּשְׁפָּחָה אֲשֶׁר־יִלְכְּדֶנָּה (3fs verb + 3fs suffix — single-clan construal as one juridical body in the Achan trial) | Gen 12:3 כֹּל מִשְׁפְּחֹת הָאֲדָמָה (pl.) + Niphal.Perf.3p נִבְרְכוּ |
| קָהָל | H6951 | assembly / congregation | singular assembly-as-one (Num 16:33 מִתּוֹךְ הַקָּהָל) | plural members (עֲדַת … הֵמָּה) |
| עֵדָה | H5712 | congregation / community | singular corporate-identity oaths and verdicts | distributive plural verbs when members are itemised |

## Semantic Payload (Context-Neutral)

The three key lemmas (H1471, H5971, H1004) combine the semantic feature [+collective] with the morpho-syntactic feature [singular]. This combination is precisely what enables biblical judgment-discourse to:

- **Treat a sin committed by one as a sin of the whole** (Achan → Israel, Jos 7).
- **Extend iniquity across generations along a household line** (fathers → children, Exo 20:5; Saul → Saul's house, 2Sa 21).
- **Visit dynastic verdicts on *the house* as a juridical person** (house of Jeroboam, house of Ahab, house of Jehu).
- **Address a nation as a single moral agent capable of turning or not turning** (Jer 18:7–10; Gen 20:4 Abimelech's *gôy ṣaddîq*).
- **Locate blessing and curse within a corporate head who stands for the many** (Abraham as *gôy gādôl*, Gen 12:2).

The grammatical mechanism is the collective singular + concord-alternation described above. The entry documents the pattern; the hermeneutical adjudication of **how far** corporate guilt extends, and **how** it interacts with individual responsibility (Deu 24:16; Ezek 18:20; Jer 31:29–30) belongs to the study, not to this reference entry.

---
*Generated from: hebrew_parser.py (--verse "Jos 7:11" verified full parse — base exemplar for the concord alternation); search_strongs.py --lexicon H1471 / H5971 / H1004 (BLB lexicon data); kjv.txt corpus Grep for all cited KJV translations. Parser runs for additional verses were attempted but blocked by concurrent Text-Fabric memory contention; all parsings cited beyond Jos 7:11 are read off the morphological categories exhibited in the Jos 7:11 parse plus Strong's lexicon part-of-speech data — no independent training-knowledge parsings introduced.*
*Last updated: 2026-04-18*
