# Constructio ad Sensum (Hebrew)

## Definition

*Constructio ad sensum* ("construction according to sense") is the phenomenon in Biblical Hebrew where grammatical agreement (gender, number, or both) follows the **meaning or sense** of the subject rather than its strict morphological form. GKC §145 identifies this as one of two main causes of agreement anomalies in Hebrew (the other being word-order effects when the predicate precedes the subject). The phenomenon covers several distinct sub-patterns:

1. **Collective noun + plural predicate** — a morphologically singular collective subject (עַם, יִשְׂרָאֵל, צֹאן, בָּקָר) governs a plural verb because the speaker has the individual members in view.
2. **Singular-to-plural shift within a sentence** — the construction begins with a singular predicate (before the collective subject is mentioned or when the group is first conceived as a unit), then shifts to plural once the constituents come into focus.
3. **Predicate-before-subject gender override** — when the predicate precedes its subject, Hebrew tolerates masculine default agreement even with a feminine subject, because the subject's gender has not yet been "announced."
4. **Mixed-gender compound subjects** — when two or more subjects of different genders share a predicate, the predicate takes masculine agreement (as the "prior" or default gender); a following predicate takes plural.
5. **Elohim agreement anomalies** — the *pluralis majestatis* אֱלֹהִים overwhelmingly governs singular verbs when referring to Israel's God, but occasionally takes plural verbs/attributes (*constructio ad sensum* treating the plural morphology as semantically live).

## Form Recognition

There is no single parser code for this phenomenon — it is diagnosed by **mismatched agreement** between subject and predicate:

- A `Noun.ms.Abs` or `Noun.s.Abs` (collective) paired with a `Verb.<stem>.<tense>.3mp` or `3fp` verb → collective *ad sensum*
- A `Verb.<stem>.<tense>.3ms` preceding a `Noun.fs.Abs` or `Noun.fp.Abs` subject → predicate-before-subject gender override
- A singular verb followed by plural verbs within the same clause/sentence with the same subject → number shift
- `Noun.mp.Abs` אֱלֹהִים paired with `Verb.<stem>.<tense>.3p` when the referent is Israel's God → Elohim *ad sensum*

**Diagnostic method:** parse the verse with `hebrew_parser.py --verse`, then compare the number/gender features of the subject noun against those of its governing verb(s).

## Functions with Examples

### 1. Collective Noun + Plural Predicate

A morphologically singular collective noun governs a plural verb because the speaker construes the group as its individual members. GKC §145c: "Not infrequently the construction begins in the singular … but is carried on, after the collective subject has been mentioned, in the plural."

| Reference | Subject | Verb(s) | Parsing | Observation |
|-----------|---------|---------|---------|-------------|
| 1 Ki 20:20 | אֲרָם (PropN.s) | וַיָּנֻסוּ | Verb.Qal.Wayq.**3mp** | "and the Syrians (sg. gentilic) fled (pl.)" — collective nation with plural verb |
| Job 1:14 | הַבָּקָר (Noun.s.Abs) | הָיוּ חֹרְשׁוֹת | Verb.Qal.Perf.**3p** + Ptcp.**fp** | "the cattle (sg. collective) were ploughing (pl. fem.)" — *ad sensum* plural + feminine from the cows in view |
| 1 Sa 4:5 | כָל־יִשְׂרָאֵל (PropN.s) | וַיָּרִעוּ | Verb.Hiphil.Wayq.**3mp** | "all Israel (sg.) shouted (pl.)" — people as individuals shouting |
| Gen 30:39 | הַצֹּאן (Noun.s.Abs) | וַיֶּחֱמוּ | Verb.Qal.Wayq.**3mp** | "the flock (sg. collective) conceived (pl. masc.)" — then same verse: וַתֵּלַדְןָ (Wayq.**3fp**) "bore (pl. fem.)" — gender also shifts mid-verse |

### 2. Singular-to-Plural Shift Within a Sentence

GKC §145c: "Not infrequently the construction begins in the singular (especially when the predicate precedes; see o below), but is carried on … in the plural." The predicate nearest the collective subject or before it takes singular; subsequent predicates shift to plural as the constituent members come into semantic focus.

| Reference | Hebrew Pattern | Parsing | KJV |
|-----------|----------------|---------|-----|
| Exo 1:20 | וַיִּרֶב הָעָם וַיַּעַצְמוּ | Wayq.**3ms** הָעָם (Noun.ms) + Wayq.**3mp** | "and the people multiplied (sg.), and waxed very mighty (pl.)" |
| 1 Sa 4:17 | נָס יִשְׂרָאֵל | Verb.Qal.Perf.**3ms** | "Israel is fled (sg.)" — then later in same speech: שְׁנֵי בָנֶיךָ מֵתוּ (Perf.**3p**) compound subject with plural |
| Gen 30:39 | וַיֶּחֱמוּ … וַתֵּלַדְןָ הַצֹּאן | Wayq.**3mp** → Wayq.**3fp** | First verb: plural masculine (flock conceived); second verb: plural feminine (flock bore young) — shift from masculine-default to feminine-*ad sensum* within one verse |

### 3. Predicate-Before-Subject Gender Override

When the verbal predicate **precedes** its subject, Hebrew permits masculine-default agreement regardless of the subject's grammatical gender. GKC §145o,p: the preceding predicate may appear as masculine singular even before a feminine subject, because "the gender of the subject is as yet unknown." GKC §145p notes "a similar dislike of the feminine form" in verbal predicates.

| Reference | Predicate | Subject | Parsing | Observation |
|-----------|-----------|---------|---------|-------------|
| Gen 30:39 | וַיֶּחֱמוּ | הַצֹּאן (Noun.s — treated as fem. collective) | Verb.Qal.Wayq.**3mp** | Masculine-plural predicate before feminine collective subject; GKC §145p cites this verse |
| Jdg 21:21 | יֵצְאוּ | בְנֹות־שִׁילוֹ (Noun.fp.Cst) | Verb.Qal.Impf.**3mp** | "if the daughters of Shiloh come out (masc. pl.)" — masculine predicate before feminine-plural subject (GKC §145p) |

GKC §145o further notes that when compound subjects follow the predicate, the predicate may agree with only the **nearest** subject (singular), even though the compound group is semantically plural (see §5 below).

### 4. Mixed-Gender Compound Subjects

When two or more subjects of different grammatical genders share a predicate, the predicate takes masculine agreement as the "prior gender" (GKC §146d, §132d). A predicate that follows such compound subjects is put in the plural (GKC §146a).

| Reference | Subjects | Predicate | Parsing | Observation |
|-----------|----------|-----------|---------|-------------|
| Gen 18:11 | אַבְרָהָם (PropN.ms) וְשָׂרָה (PropN.fs) | זְקֵנִים בָּאִים | Adj.**mp** + Ptcp.**mp** | "Abraham and Sarah were old (masc. pl.), advanced (masc. pl.) in days" — masculine wins over mixed genders |
| Gen 8:22 | זֶרַע וְקָצִיר וְקֹר וָחֹם (4 masc. pairs) | לֹא יִשְׁבֹּתוּ | Verb.Qal.Impf.**3mp** | "seedtime and harvest, cold and heat … shall not cease (pl.)" — plural predicate following multiple singular subjects |
| Gen 31:14 | רָחֵל וְלֵאָה (two fem.) | וַתַּעַן | Verb.Qal.Wayq.**3fs** | "Then answered (fem. sg.) Rachel and Leah" — predicate before compound subject agrees with nearest member only (GKC §146b) |

### 5. Elohim Agreement Patterns (*Pluralis Majestatis*)

אֱלֹהִים (`Noun.mp.Abs`) overwhelmingly takes singular agreement when referring to the God of Israel — the standard *pluralis majestatis* pattern (GKC §145h; see [pluralis-majestatis](pluralis-majestatis.md)). However, a small set of verses construe אֱלֹהִים with **plural** verbs or attributes even when the referent is unambiguously Israel's God. These represent *constructio ad sensum* in which the morphologically plural form "leaks through" to the agreement pattern.

| Reference | Hebrew | Parsing | KJV | Observation |
|-----------|--------|---------|-----|-------------|
| Gen 1:1 | בָּרָא אֱלֹהִים | Verb.Qal.Perf.**3ms** + Noun.mp.Abs | "God created" | **Standard:** singular verb with plural noun |
| Gen 20:13 | הִתְעוּ אֹתִי אֱלֹהִים | Verb.Hiphil.Perf.**3p** + Noun.mp.Abs | "God caused me to wander" | **Anomalous:** plural verb; Abraham speaking to pagan Abimelech |
| Gen 35:7 | נִגְלוּ אֵלָיו הָאֱלֹהִים | Verb.Niphal.Perf.**3p** + Art. + Noun.mp.Abs | "God appeared unto him" | **Anomalous:** plural verb with article + Elohim |
| 2 Sa 7:23 | הָלְכוּ אֱלֹהִים | Verb.Qal.Perf.**3p** + Noun.mp.Abs | "God went to redeem" | **Anomalous:** plural verb; cf. parallel 1 Ch 17:21 הָלַךְ (Perf.**3ms**) — same sentence, singular verb in Chronicles recension |
| Jos 24:19 | אֱלֹהִים קְדֹשִׁים הוּא | Noun.mp + Adj.**mp** + PersPron.**3ms** | "he is an holy God" | **Mixed concord:** plural adjective + singular pronoun in same clause |

The 2 Sa 7:23 ‖ 1 Ch 17:21 minimal pair is the clearest MT demonstration that agreement with אֱלֹהִים can vary for identical referents across recensions. GKC §145i notes these cases without resolving whether the plural agreement is a grammatical lapse, a dialectal variant, or theologically significant.

## Diagnostic Summary

| Pattern | Subject Form | Predicate Agreement | Trigger |
|---------|-------------|---------------------|---------|
| Collective *ad sensum* | singular collective noun | plural verb | individual members in view |
| Sg→Pl shift | same collective subject | singular → plural across clause | focus shifts from group to members |
| Predicate-before-subject | feminine/plural subject | masculine singular/default verb | subject gender/number not yet announced |
| Mixed-gender compound | masc. + fem. subjects | masculine plural (following); singular nearest (preceding) | masculine as "prior gender" |
| Elohim *ad sensum* | אֱלֹהִים (Noun.mp) | plural verb/adjective | morphological plural form "leaks through" |

## Contrast with Related Forms

| Phenomenon | Behavior | Example |
|------------|----------|---------|
| *Constructio ad sensum* | agreement follows meaning, not form | Exo 1:20 עָם (ms) + וַיַּעַצְמוּ (3mp) |
| Standard agreement | predicate matches subject in gender and number | Gen 1:1 אֱלֹהִים (mp) + בָּרָא (3ms, *pluralis majestatis*) |
| *Pluralis majestatis* (strict) | plural noun + singular agreement → one referent | Gen 1:1; see [pluralis-majestatis](pluralis-majestatis.md) |
| Corporate solidarity | collective noun alternates sg/pl agreement based on corporate vs. individual framing | Jos 7:11; see [corporate-solidarity](corporate-solidarity.md) |
| Plural noun + singular verb agreement | diagnostic rule for honorific/extensive plurals | see [plural-noun-singular-verb-agreement](plural-noun-singular-verb-agreement.md) |

## Common Nouns and Names Subject to *Constructio ad Sensum*

| Noun | Strong's | Type | Agreement pattern |
|------|----------|------|-------------------|
| עַם | H5971 | collective ("people") | singular as unit; plural *ad sensum* for constituent members (Exo 1:20) |
| יִשְׂרָאֵל | — | proper noun (collective nation) | singular as nation; plural for "the Israelites" (1 Sa 4:5; 1 Ki 20:20) |
| אֲרָם | — | proper noun (collective nation) | singular as nation; plural for "the Syrians" (1 Ki 20:20) |
| צֹאן | H6629 | collective ("flock/sheep") | singular or plural; gender-shift within one verse (Gen 30:39) |
| בָּקָר | H1241 | collective ("cattle") | singular form; plural + feminine *ad sensum* (Job 1:14) |
| אֱלֹהִים | H430 | *pluralis majestatis* | usually singular; occasionally plural *ad sensum* (Gen 20:13; 35:7) |

## Textbook Citations

- **Gesenius (GKC) §145** — primary treatment of agreement anomalies: §145a (general rule), §145b–l (*constructio ad sensum* subcategories: collectives with plural predicates, singular-to-plural shift), §145o–p (predicate before subject: masculine default, gender override), §145h–i (Elohim and *pluralis maiestatis* agreement), §145s (compound subjects with mixed genders).
- **GKC §146** — agreement rules for compound subjects: §146a (following predicate is plural), §146b (preceding predicate agrees with nearest member), §146d (masculine as "prior gender" for mixed-gender groups).
- **GKC §132d,h** — singular attribute with *pluralis maiestatis*; masculine as prior gender for attributes of mixed-gender nouns.
- **Waltke-O'Connor, *IBHS*** — §7.2.1 (collectives and agreement), §7.4.3 (honorific plurals and agreement norms).
- **Joüon-Muraoka** — §150 (agreement of verb with subject in number and gender); §136d–e (*pluralis majestatis* / *excellentiae*).

(All textbook references verified via `D:/Bible/tools/search/semantic_grammar.py` queries against indexed GKC, Waltke-O'Connor, BDB, Futato, and BHSG PDFs.)

---
*Generated from: hebrew_parser.py (--verse), semantic_grammar.py (GKC §145 / §146 / §132, Waltke-O'Connor §7.2–7.4, Joüon-Muraoka §150)*
*Last updated: 2026-04-29*
