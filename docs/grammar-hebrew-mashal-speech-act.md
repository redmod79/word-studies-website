# Mashal Speech-Act Formula (נָשָׂא מָשָׁל / מָשַׁל מָשָׁל)

## Definition

The *mashal* speech-act is a formulaic literary frame by which a speaker is reported to "lift up / propound a *mashal*" — a weighty, authoritative, often poetic utterance typically bearing revelatory, proverbial, dirge, or riddle-like content. Two verbal formulae recur:

1. **נָשָׂא מָשָׁל** (*nāśāʾ māšāl*) — "lift up a *mashal*" (Qal of נשׂא H5375 with מָשָׁל H4912 as direct object). Cognate with *nāśāʾ qôl* "lift up the voice" and *nāśāʾ qînāh* "lift up a lament." Dominant in Num 23–24 (Balaam oracles), Isa 14:4, Mic 2:4, Hab 2:6, Job 27:1; 29:1.
2. **מָשַׁל מָשָׁל** (*māšal māšāl*) — "speak/utter a *mashal*" (Qal imperative of the cognate verb משׁל H4911 with its internal-object noun). Dominant in Ezekiel (Ezk 17:2; 24:3; cf. the derogatory quotation formula in Ezk 12:23; 18:2–3).

A third variant uses בְּ + מָשָׁל as an instrumental phrase with פתח "open": **אֶפְתְּחָה בְמָשָׁל פִּי** "I will open my mouth in/with a *mashal*" (Psa 78:2).

The formula marks the transition from narrative prose into elevated, bounded oracular/sapiential discourse. It is a genre-switch signal, not merely a speech-introducer.

## Form Recognition

Three morphosyntactic signatures, each recoverable from parsed text:

### (a) Wayyiqtol narrative frame (Balaam / Job type)

```
וַיִּשָּׂא מְשָׁלוֹ וַיֹּאמַר
way-yiśśāʾ  məšālô   way-yōʾmar
Qal.Wayq.3ms  Noun.ms.Abs.+3ms  Qal.Wayq.3ms
"And-he-lifted his-mashal and-said…"
```

- **Parser codes:** `Verb.Qal.Wayq.3ms` of נשׂא + `Noun.ms.Abs.+3ms` of משׁל + `Verb.Qal.Wayq.3ms` of אמר
- The 3ms suffix on מְשָׁלוֹ ("his *mashal*") — possessive pronominal — is formulaic; the oracle "belongs to" the speaker.
- Coordinated wayyiqtol pair (נשׂא…אמר) creates a fixed doublet: the second verb (וַיֹּאמַר) opens the direct-speech content.

### (b) Imperative prophetic commission (Ezekiel type)

```
וּמְשֹׁל … מָשָׁל
û-məšōl  …  māšāl
Verb.Qal.Impv.2ms  Noun.ms.Abs
"and-propound … a-mashal"
```

- **Parser codes:** `Verb.Qal.Impv.2ms` of משׁל H4911 + its cognate internal object `Noun.ms.Abs` of משׁל H4912.
- **Figura etymologica / paronomasia**: verb and noun share the root משׁל; cf. Ezk 17:2 חוּד חִידָה (cognate riddle-command) in immediate parallelism.
- Addressed to the prophet as 2ms vocative; speech-act is commissioned, not self-initiated.

### (c) 1cs Cohortative self-announcement (Psalter type)

```
אֶפְתְּחָה בְמָשָׁל פִּי
ʾep̄təḥāh  bə-māšāl  pî
Verb.Qal.Impf(Coh).1s  Prep+Noun.ms.Abs  Noun.ms.Abs.+1us
"I-will-open in-a-mashal my-mouth"
```

- **Parser codes:** `Verb.Qal.Impf.1s` (often cohortative with paragogic -āh) of פתח + בְ-prefixed `Noun.ms.Abs` of משׁל + body-part noun פֶּה with 1cs suffix.
- First-person speaker self-framing; the *mashal* is **instrumental** (בְּ) rather than a direct object.

### Diagnostic: recurring collocations

- **מָשָׁל ‖ חִידָה** (proverb/riddle) — parallelism at Ezk 17:2, Psa 78:2, Hab 2:6, Psa 49:5.
- **מָשָׁל ‖ נְאֻם** (proverb/oracle-speech) — Num 24:3, 15.
- **מָשָׁל ‖ נְהִי / קִינָה** (proverb/lament-dirge) — Mic 2:4.
- **מָשָׁל + עַל + addressee** — Isa 14:4 הַמָּשָׁל הַזֶּה עַל־מֶלֶךְ בָּבֶל; Hab 2:6 עָלָיו מָשָׁל יִשָּׂאוּ. Marks taunt-song / dirge over a target.

## Functions with Examples

### 1. Balaam-oracle incipit (נָשָׂא מָשָׁל + wayyiqtol)

Seven-fold opener across the four Balaam oracles, each marking a discrete pericope of poetic revelation.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Num 23:7 | וַיִּשָּׂא מְשָׁלוֹ וַיֹּאמַר | Qal.Wayq.3ms + Noun.ms.Abs.+3ms + Qal.Wayq.3ms | "he took up his parable, and said" |
| Num 23:18 | וַיִּשָּׂא מְשָׁלוֹ וַיֹּאמַר | identical | "he took up his parable, and said" |
| Num 24:3 | וַיִּשָּׂא מְשָׁלוֹ וַיֹּאמַר | identical | "he took up his parable, and said" |
| Num 24:15 | וַיִּשָּׂא מְשָׁלוֹ וַיֹּאמַר | identical | "he took up his parable, and said" |
| Num 24:20 | וַיַּרְא…וַיִּשָּׂא מְשָׁלוֹ וַיֹּאמַר | Qal.Wayq.3ms ראה + formula | "he…took up his parable, and said" |
| Num 24:21 | (same formula) |  | (parable on Kenites) |
| Num 24:23 | (same formula) |  | (final parable) |

The **formulaic identity** across all seven occurrences makes the wayyiqtol pair a structural marker dividing the Balaam block into seven poetic cola.

### 2. Prophetic-commission imperative (מְשֹׁל מָשָׁל)

Ezekiel uses the cognate-accusative imperative exclusively for the prophet's mandated performance of riddle-parables over Israel/Judah.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Ezk 17:2 | חוּד חִידָה וּמְשֹׁל מָשָׁל | Qal.Impv.2ms חוד + Noun.fs.Abs + Qal.Impv.2ms משׁל + Noun.ms.Abs | "put forth a riddle, and speak a parable" |
| Ezk 24:3 | וּמְשֹׁל אֶל־בֵּית־הַמֶּרִי מָשָׁל | Qal.Impv.2ms + אֶל + Noun.ms.Cst + Noun.ms.Abs | "utter a parable unto the rebellious house" |

At Ezk 17:2 the imperative is paired with **חוּד חִידָה** — the matching cognate-accusative of חוד "propound" + חִידָה "riddle" — creating a double *figura etymologica* opener. At Ezk 24:3 the dative phrase אֶל־בֵּית־הַמֶּרִי ("unto the rebellious house") is fronted between verb and object, polemically qualifying the addressee.

### 3. Psalmist self-announcement (אֶפְתְּחָה בְמָשָׁל)

A first-person sapiential opener.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Psa 78:2 | אֶפְתְּחָה בְמָשָׁל פִּי אַבִּיעָה חִידוֹת מִנִּי־קֶדֶם | Qal.Impf.1s פתח + Prep+Noun + Noun+1us ‖ Hiphil.Impf.1s נבע + Noun.fp.Abs + Prep + Noun.ms.Abs | "I will open my mouth in a parable: I will utter dark sayings of old" |
| Psa 49:5 | אַטֶּה לְמָשָׁל אָזְנִי אֶפְתַּח בְּכִנּוֹר חִידָתִי | Hiphil.Impf.1s נטה + לְ+Noun + Noun+1us ‖ Qal.Impf.1s פתח + בְּ+Noun + Noun+1us | "I will incline mine ear to a parable: I will open my dark saying upon the harp" |

Psa 78:2 pairs בְמָשָׁל (instrumental) with חִידוֹת (f.pl. of חִידָה, "riddles / dark sayings"), completing the standard *mashal ‖ ḥîdāh* parallelism.

### 4. Taunt-song / dirge over an oppressor (מָשָׁל + עַל)

When the preposition עַל ("upon, against") is attached, the *mashal* becomes a **taunt-mashal** directed against a named target.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Isa 14:4 | וְנָשָׂאתָ הַמָּשָׁל הַזֶּה עַל־מֶלֶךְ בָּבֶל | Qal.Perf.2ms (weqatal) + Art+Noun+Dem + Prep + Noun.ms.Cst | "thou shalt take up this proverb against the king of Babylon" |
| Mic 2:4 | יִשָּׂא עֲלֵיכֶם מָשָׁל | Qal.Impf.3ms + Prep+2mp + Noun | "shall one take up a parable against you" |
| Hab 2:6 | עָלָיו מָשָׁל יִשָּׂאוּ | Prep+3ms + Noun + Qal.Impf.3mp | "shall not all these take up a parable against him" |

The directional preposition עַל/עֲלֵי converts the neutral "lift up a *mashal*" into an adversarial speech-act. At Mic 2:4 the *mashal* is then explicated by **נְהִי** (lament) and שָׁדוֹד נְשַׁדֻּנוּ (inf.abs. paronomasia of שׁדד "utterly despoiled"), showing the dirge sub-genre.

### 5. Job narrative resumption (יסף Hiphil + נשׂא InfCon)

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Job 27:1 | וַיֹּסֶף אִיּוֹב שְׂאֵת מְשָׁלוֹ וַיֹּאמַר | Hiphil.Wayq.3ms יסף + Qal.InfCon נשׂא + Noun.ms.Abs.+3ms + Qal.Wayq.3ms | "Moreover Job continued his parable, and said" |
| Job 29:1 | (same formula) | identical | "Moreover Job continued his parable, and said" |

The Hiphil wayyiqtol of יסף ("add, continue") + infinitive construct שְׂאֵת (from נשׂא) creates a **resumption** variant: "and he continued to lift up his *mashal*." The 3ms suffix on מְשָׁלוֹ again marks the oracle as the speaker's own.

## Contrast with Related Speech-Act Formulae

| Formula | Lexical core | Function | Example |
|---------|--------------|----------|---------|
| **נָשָׂא מָשָׁל** | נשׂא + מָשָׁל | lift up a (poetic) oracle/proverb | Num 23:7; Isa 14:4 |
| **מָשַׁל מָשָׁל** | משׁל + מָשָׁל (cognate-acc.) | commissioned prophetic riddle-parable | Ezk 17:2; 24:3 |
| **אֶפְתְּחָה בְמָשָׁל** | פתח + בְּ+מָשָׁל | 1cs self-announcement of sapiential speech | Psa 78:2; 49:5 |
| **נָשָׂא קִינָה** | נשׂא + קִינָה | lift up a lament-dirge | 2Sa 1:17; Amo 5:1; Ezk 19:1; 27:2 |
| **נָשָׂא קוֹל** | נשׂא + קוֹל | lift up the voice (generic) | Gen 21:16; Jdg 9:7 |
| **נָאַם / נְאֻם** | נאם noun-construct | oracle-attribution tag | Num 24:3–4 (paired with *mashal*) |
| **כֹּה אָמַר יהוה** | אמר Qal.Perf.3ms + divine subject | prophetic messenger-formula | Ezk 24:3 (paired with *mashal* command) |

The *mashal* formula is cognate with — but distinct from — the *qînāh* (dirge) formula: both use נשׂא as speech-verb, but *qînāh* is narrowly funerary while *mashal* ranges over proverb, riddle, oracle, taunt, and sapiential poem.

## Lexical Notes on מָשָׁל (H4912)

- **BLB count:** 39 occurrences as noun.
- **Semantic range** (per BLB/BDB): "proverb, parable, similitude, byword, taunt-song, discourse." The noun is **polysemous** — the genre of each *mashal* is determined by surrounding syntax (presence of עַל, parallel with חִידָה / נְאֻם / נְהִי, etc.), not by the lexeme alone.
- **Etymology:** the root משׁל H4911 carries the sense of "be like, represent, compare"; the noun *mashal* is thus fundamentally a **likeness-speech**. A secondary homonym משׁל H4910 "rule, govern" is distinct in biblical usage though orthographically identical in many forms.
- **Distribution of the speech-act formula:** Num 23–24 (7×), Isa 14:4, Mic 2:4, Hab 2:6, Ezk 17:2, 24:3, Psa 49:5, Psa 78:2, Job 27:1, 29:1 — concentrated in oracle, prophetic-commission, taunt-song, and wisdom-psalm contexts.

## Verbal Collocations in the Formula

| Verb | Strong's | Form | Partner | Occurrences (of the formula) |
|------|----------|------|---------|------------------------------|
| נשׂא "lift" | H5375 | Qal.Wayq.3ms / Perf.2ms / Impf.3ms-3mp / InfCon | מָשָׁל | Num 23:7, 18; 24:3, 15, 20, 21, 23; Isa 14:4; Mic 2:4; Hab 2:6; Job 27:1; 29:1 |
| משׁל "speak a proverb" | H4911 | Qal.Impv.2ms | מָשָׁל (internal obj.) | Ezk 17:2; 24:3 |
| פתח "open" | H6605 | Qal.Impf.1s (coh.) | בְּמָשָׁל | Psa 78:2; 49:5 |
| יסף "add/continue" | H3254 | Hiphil.Wayq.3ms + InfCon of נשׂא | מָשָׁלוֹ | Job 27:1; 29:1 |
| חוד "propound (riddle)" | H2330 | Qal.Impv.2ms | חִידָה (parallel to mashal) | Ezk 17:2 |
| אמר "say" | H559 | Qal.Wayq.3ms / weqatal 2ms | (introduces speech content) | Num 23–24 passim; Isa 14:4; Ezk 24:3; Job 27:1 |

## Syntactic Template Summary

```
[SPEECH-ACT FRAME]       →   [ORACLE BODY]
wayyiqtol-pair (narrative)      poetry / riddle / taunt / dirge
  or imperative (commission)
  or cohortative (self-intro)
  + optional עַל-target
  + optional ‖ חִידָה / נְאֻם / נְהִי
```

The frame is **separable** from the body: once the formulaic line is uttered, the genre, meter, and pragmatic target of the following material are constrained by (a) the preposition (עַל vs. בְּ vs. ø), (b) the parallel term (*ḥîdāh*, *nəʾum*, *nəhî*), and (c) the speaker's identity and commission.

## See Also

- [syntax-waw-conjunction](syntax-waw-conjunction.md) — the wayyiqtol-pair וַיִּשָּׂא…וַיֹּאמַר relies on narrative waw-consecutive
- [stem-niphal](stem-niphal.md) — contrast with Niphal passive speech-events (e.g., נֶאֱמַר "it is spoken")

---

*Generated from: hebrew_parser.py (--verse on Num 23:7, 23:18, 24:3, 24:15, 24:20; Eze 17:2, 24:3; Psa 78:2; Isa 14:4; Mic 2:4; Hab 2:6; Job 27:1); search_strongs.py --lexicon H4912, H5375*
*Last updated: 2026-04-18*
