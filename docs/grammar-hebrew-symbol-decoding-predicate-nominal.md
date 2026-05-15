# Explicit X=Y Symbol Decoding (Predicate-Nominal / Copular Clause)

**Cross-language pattern: Hebrew, Biblical Aramaic, Koine Greek**

## Definition

An *explicit symbol-decoding clause* is a predicate-nominal (copular) construction in which the biblical text itself equates a visionary/apocalyptic image (X) with its referent (Y) by means of a verbless nominal clause, a pronominal copula, or the verb *to be* (היה / הוה / εἰμί). The clause functions as an *on-stage, author-supplied glossary* embedded in the discourse: rather than leaving the image un-interpreted, the narrator or angelic speaker asserts `X [is] Y`, making the correspondence part of the inspired text rather than of later exegesis.

1. **Verbless nominal clause (Hebrew NmCl / Aramaic NmCl)** — juxtaposition of two substantives or substantivized phrases, copula implied: X Y = "X [is] Y".
2. **Pronominal copula (הוּא / אַנְתְּ־הוּא / הוּא ה־)** — 3rd or 2nd person pronoun functions as a copula/focus marker between subject and predicate nominal.
3. **Overt copula (peal *hwh*; Greek εἰμί pres. ind.)** — finite form of "to be," typically 3rd person present/future, linking subject to predicate nominal in apocalyptic interpretation scenes.

## Form Recognition

Across the nine canonical attestations, three surface realizations recur:

- **Juxtaposition, no copula** — two noun phrases placed side-by-side, the first topical/visionary, the second interpretive. Hebrew: הָאַיִל … מַלְכֵי מָדַי וּפָרָס (Dan 8:20); Aramaic: אַרְבְּעָה מַלְכִין יְקוּמוּן (Dan 7:17, with overt *yiqtol* of קום but still in nominal-predication frame).
- **Pronominal copula** — 3ms/2ms pronoun hinging subject and predicate. Hebrew: הוּא הַמֶּלֶךְ הָרִאשׁוֹן (Dan 8:21); Aramaic: אַנְתְּ־הוּא רֵאשָׁה דִּי דַהֲבָא (Dan 2:38).
- **Finite copula** — Greek εἰσίν / ἔστιν (Rev 1:20; 17:9, 15, 18); Aramaic peal *tehĕwēʾ* (Dan 7:23); Greek participial naming-copula ὁ καλούμενος with dual predicate nominative (Rev 12:9).

**Parser codes:**
- Hebrew/Aramaic: `sp=verb lex=HJH` (Hebrew) or `sp=verb lex=HWH` (Aramaic) for overt copula; BHSA clause type `NmCl` for verbless.
- Greek: `lemma=εἰμί tense=pres mood=ind` (G1510); subject NP in nominative + predicate NP in nominative.

## Functions with Examples

### 1. Aramaic pronominal-copula decoding (Daniel 2, 7)

| Reference | Original | Parsing | Decoding |
|-----------|----------|---------|----------|
| Dan 2:38 | אַנְתְּ־הוּא רֵאשָׁה דִּי דַהֲבָא | 2ms pron + 3ms pron (copula) + Noun.ms + *dī* + Noun.ms | "Thou art this head of gold" (Nebuchadnezzar = head of gold) |
| Dan 7:17 | אִלֵּין חֵיוָתָא רַבְרְבָתָא … אַרְבְּעָה מַלְכִין יְקוּמוּן | DemPron.p + Noun.fp + Adj.fp ‖ Num + Noun.mp + peal Impf.3mp קום | "These great beasts … are four kings" (beasts = kings/kingdoms) |
| Dan 7:23 | חֵיוְתָא רְבִיעָיְתָא מַלְכוּ רְבִיעָאָה תֶּהֱוֵא בְאַרְעָא | Noun.fs + Adj.fs ‖ Noun.fs + Adj.fs + peal Impf.3fs הוה | "The fourth beast shall be the fourth kingdom" (overt *hwh* copula) |
| Dan 7:24 | וְקַרְנַיָּא עֲשַׂר מִנַּהּ מַלְכוּתָה עַשְׂרָה מַלְכִין יְקֻמוּן | Noun.fd + Num ‖ Num + Noun.mp + peal Impf.3mp קום | "And the ten horns … are ten kings" |

Dan 2:38 uses the classic Aramaic tripartite nominal clause (pronoun + predicate nominal + *dī*-relative); Dan 7:23 supplies the only overt copula (*tehĕwēʾ*) in the Dan 7 interpretation; vv. 17 and 24 use *yiqtol* of קום ("shall arise") as a predicate-verb that still carries equative force by juxtaposing a visionary subject with a categorical predicate ("four kings," "ten kings").

### 2. Hebrew pronominal/juxtapositional decoding (Daniel 8)

| Reference | Hebrew | Parsing | Decoding |
|-----------|--------|---------|----------|
| Dan 8:20 | הָאַיִל … מַלְכֵי מָדַי וּפָרָס | Art+Noun.ms + rel. cl. ‖ Noun.mp.Cst + PropN + PropN | "The ram … [is/are] the kings of Media and Persia" (verbless NmCl) |
| Dan 8:21 | וְהַצָּפִיר הַשָּׂעִיר מֶלֶךְ יָוָן | Art+Noun.ms + Art+Adj.ms ‖ Noun.ms.Cst + PropN | "The rough goat [is] the king of Grecia" (verbless) |
| Dan 8:21b | וְהַקֶּרֶן הַגְּדוֹלָה … הוּא הַמֶּלֶךְ הָרִאשׁוֹן | Art+Noun.fs + Art+Adj.fs … + 3ms pron (copula) + Art+Noun.ms + Art+Adj.ms | "The great horn … is the first king" (pronominal copula) |

Dan 8 shows the most compressed Hebrew surface form: pure juxtaposition (v. 20; v. 21a) and pronominal copula הוּא (v. 21b). The pronoun הוּא in v. 21b serves the classical tripartite-nominal-clause function (Joüon-Muraoka §154j): it is not semantically redundant but establishes a tight identity equation between the visionary figure and its referent.

### 3. Daniel 9 construct-chain equations

| Reference | Hebrew | Parsing / Force |
|-----------|--------|-----------------|
| Dan 9:25 | שָׁבֻעִים שִׁבְעָה ‖ שָׁבֻעִים שִׁשִּׁים וּשְׁנַיִם | Noun.mp + Num; numerical equations given as bare juxtaposition |
| Dan 9:26 | יִכָּרֵת מָשִׁיחַ וְאֵין לוֹ | Niphal Impf.3ms כרת + neg existential — event-predication, not pure equation |
| Dan 9:27 | וְהִגְבִּיר בְּרִית לָרַבִּים שָׁבוּעַ אֶחָד | Hiphil weqatal גבר + obj + *lə*-PP + accusative of time-unit |

Dan 9:24–27 blends two patterns: (a) bare numerical equations (week-units = years, implicit via the day-year schema; see [day-year-formula](day-year-formula.md)) and (b) event-predications about the anointed one and the covenant-confirmer. The oracle is therefore *partially* self-decoding at the numerical level while leaving the agent-identifications grammatically open (cf. [dan-9-24-27](../passages/dan-9-24-27.md)).

### 4. Greek εἰμί copular decoding (Revelation)

| Reference | Greek | Parsing | Decoding |
|-----------|-------|---------|----------|
| Rev 1:20 | οἱ ἑπτὰ ἀστέρες ἄγγελοι τῶν ἑπτὰ ἐκκλησιῶν εἰσίν … αἱ λυχνίαι αἱ ἑπτὰ ἑπτὰ ἐκκλησίαι εἰσίν | Art+Num+N.NPM ‖ N.NPM + gen. chain + V-PAI-3P εἰμί (×2) | "seven stars are angels of the seven churches … seven candlesticks are seven churches" |
| Rev 17:9 | αἱ ἑπτὰ κεφαλαὶ ἑπτὰ ὄρη εἰσίν … καὶ βασιλεῖς ἑπτά εἰσιν | Art+Num+N.NPF ‖ Num+N.NPN + V-PAI-3P ‖ N.NPM+Num + V-PAI-3P | "seven heads are seven mountains … and are seven kings" (double-decoding) |
| Rev 17:15 | τὰ ὕδατα ἃ εἶδες … λαοὶ καὶ ὄχλοι εἰσὶν καὶ ἔθνη καὶ γλῶσσαι | Art+N.NPN + rel. cl. ‖ four nom. pl. predicates + V-PAI-3P | "the waters … are peoples and multitudes and nations and tongues" |
| Rev 17:18 | ἡ γυνὴ ἣν εἶδες ἔστιν ἡ πόλις ἡ μεγάλη | Art+N.NSF + rel. cl. + V-PAI-3S + Art+N.NSF+Art+Adj.NSF | "the woman which thou sawest is that great city" |
| Rev 12:9 | ὁ δράκων ὁ μέγας, ὁ ὄφις ὁ ἀρχαῖος, ὁ καλούμενος Διάβολος καὶ Ὁ Σατανᾶς | four-fold articular apposition; V-PPP-NSM καλέω as naming-copula | "the great dragon, that old serpent, called the Devil, and Satan" |

Revelation's Greek regularizes the pattern with pres.act.ind. εἰμί (εἰσίν, ἔστιν). Rev 12:9 substitutes an articular present-passive participle of καλέω for the copula (the *ὁ καλούμενος* formula) to equate four distinct nominative-singular labels with the same referent. Rev 17:9 is syntactically exceptional in supplying two different predicate-nominal completions for one subject ("seven heads") in a single clause-chain, making the symbolic head both "seven mountains" and "seven kings."

## Clause-Level Features of the Pattern

- **Anaphoric pointer** — the subject is typically the visionary element already introduced in the preceding narrative ("the ram you saw," "the waters you saw," "the woman you saw"), often with a resumptive relative (אֲשֶׁר רָאִיתָ / ἣν εἶδες / οὓς εἶδες). The decoding clause is *not* a fresh observation but a gloss on prior perception.
- **Angelic-speaker frame** — with the exception of Dan 2:38 (Daniel to Nebuchadnezzar) and Rev 12:9 (narrator voice), every canonical instance is uttered by an angelic interpreter: Dan 7:23 (one of them that stood by), Dan 8:16 (Gabriel), Dan 9:22 (Gabriel), Rev 1:20 (glorified Christ), Rev 17:7, 15 (one of the seven angels).
- **Determiner asymmetry** — predicate nominal is often **indefinite** (Hebrew absolute, Greek anarthrous) even when the subject is definite (e.g., αἱ ἑπτὰ κεφαλαὶ → ἑπτὰ ὄρη; ἡ γυνή → ἡ πόλις is the exception with definite predicate). This follows the standard copular-clause rule that predicate nominals are typically less-determined than their subjects (Colwell's rule territory in Greek; Joüon §154 in Hebrew).
- **Multi-valued referents** — a single visionary element can be decoded to more than one referent within the same pericope: Rev 17:9's heads = mountains *and* kings; Dan 7:17 vs. 7:23 equates beasts with both "kings" (מַלְכִין) and "kingdoms" (מַלְכוּ), showing that the biblical writers do not treat the king/kingdom distinction as compromising the equation.

## Contrast with Related Forms

| Form | Function | Example |
|------|----------|---------|
| Explicit X=Y decoding (this entry) | text supplies its own symbol interpretation | Dan 8:20–21; Rev 17:9, 15, 18 |
| Simile / ὅμοιος + dative | resemblance without identity | Dan 7:4 *kə-ʾaryēh* "like a lion"; Rev 13:2 ὅμοιον παρδάλει |
| Participial naming-copula (ὁ καλούμενος) | labels/titles attached to a referent | Rev 12:9 (four labels → one dragon) |
| Event-predication yiqtol/weqatal | what the decoded entity *does*, not what it *is* | Dan 7:23c–d וְתֵאכֻל … וּתְדוּשִׁנַּהּ; Dan 9:27 וְהִגְבִּיר בְּרִית |
| Day-year numerical conversion | implicit ratio-based decoding of time-units | Num 14:34; Ezek 4:6 → Dan 9:24–27 (see [day-year-formula](day-year-formula.md)) |
| Hebraistic genitive of quality / "son of X" | symbolic naming by genitive apposition (not explicit equation) | see [genitive-of-quality-apposition](../greek/genitive-of-quality-apposition.md), [son-of-X-semitic-idiom](../greek/son-of-X-semitic-idiom.md) |

The explicit-decoding clause is the *strongest* form of inspired self-interpretation in the apocalyptic corpus: unlike simile (which only asserts resemblance), naming-copula (which only attaches a label), or event-predication (which only narrates action), the predicate-nominal decoding clause commits to full identity between image and referent.

## Common Predication Verbs / Copula Forms

| Form | Language | Occurrences in this pattern |
|------|----------|------------------------------|
| ∅ (verbless nominal clause) | Hebrew | Dan 8:20, 8:21a |
| הוּא / אַנְתְּ־הוּא (pronominal copula) | Hebrew / Aramaic | Dan 2:38; 8:21b |
| הוה peal Impf (תֶּהֱוֵא) | Aramaic | Dan 7:23 |
| קום peal Impf (יְקוּמוּן) as predicate-verb in equative force | Aramaic | Dan 7:17, 24 |
| εἰμί V-PAI-3S (ἔστιν) | Greek | Rev 17:18 |
| εἰμί V-PAI-3P (εἰσίν) | Greek | Rev 1:20 (×2); 17:9 (×2); 17:15 |
| καλέω V-PPP-NSM (ὁ καλούμενος) as naming-copula | Greek | Rev 12:9 |

---

*Generated from: hebrew_parser.py --verse (BHSA / ETCBC); greek_parser.py --verse (NA28/MorphGNT); KJV comparison text.*
*Last updated: 2026-04-18*
