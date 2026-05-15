# Hiphil Imperfect / Hiphil Causative Stem (Hebrew)

## Definition
The **Hiphil** (הִפְעִיל) is the H-stem (causative stem) of the Hebrew verb, formed by prefixing he (ה) to the root with a characteristic i-class theme vowel (ī/ê) in strong verbs. It converts a Qal verb's meaning into a causative action — "cause X to do / become Y." The **Imperfect** is its yiqtol conjugation, expressing non-perfective aspect (incomplete, habitual, modal, or future) and, with waw-consecutive, narrative past (Wayyiqtol).

Primary functions of the stem:

1. **Causative-factitive** — subject causes the object to perform/enter the Qal action ("make ride," "raise up")
2. **Declarative / estimative** — subject declares or treats the object as X ("pronounce righteous," "declare guilty")
3. **Denominative / productive** — derives verbs from nouns ("give rain," "bear fruit")
4. **Internal/intransitive causative** — subject causes itself to enter a state ("multiply [intrans.]," "be early")

## Form Recognition

### Morphological markers
- **Prefix:** he (ה) with a-vowel in Perf./Ptcp. (*hiqṭîl*, *maqṭîl*); ה elides in Impf. leaving only the preformative vowel ạ/ē
- **Theme vowel:** long *î* (hiriq-yod) between 2nd and 3rd root letter in the "default" form (hence *hiphīl*)
- **Preformative pattern in Imperfect:** prefix vowel *a* (patach) under the personal preformative (יַ־, תַּ־, אַ־, נַ־) — diagnostic contrast with Qal's *i*-class or *a*-class
- **Jussive/Wayyiqtol shortening:** the long *î* shortens to *ê* or segol (e.g., יַקְטֵל, וַיַּקְטֵל)

### Paradigm skeleton (strong verb קטל-type; actual verb is קום)
| Form | Pattern | Example |
|------|---------|---------|
| Perfect 3ms | hiqṭîl | הֵקִים ("he raised up") |
| Imperfect 3ms | *yaqṭîl* | יָקִים ("he will raise up") |
| Wayyiqtol 3ms | *wayyaqṭēl* | וַיַּקֵם |
| Participle ms | *maqṭîl* | מֵקִים |
| Infinitive Cst | *haqṭîl* | הָקִים |
| Imperative ms | *haqṭēl* | הָקֵם |

### Parser code
`sp=verb vs=hif vt=impf` (Hiphil Imperfect)
`sp=verb vs=hif` (Hiphil any tense)

## Functions with Examples

### 1. Causative-factitive (primary/prototypical)
Subject causes object to do or become what the Qal root expresses.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Gen 17:20 | יֹולִ֔יד | Hiphil.Impf.3ms of ילד | "twelve princes shall he beget" (cause to bear/be born) |
| Gen 41:43 | וַיַּרְכֵּב | Hiphil.Wayq.3ms of רכב | "he made him to ride" (caused him to ride) |
| Deut 18:15 | יָקִים | Hiphil.Impf.3ms of קום | "the LORD thy God will raise up" (cause to arise) |
| Gen 6:19 | תָּבִיא | Hiphil.Impf.2ms of בוא | "thou shalt bring" (cause to come) |
| Gen 19:32 | נַשְׁקֶה | Hiphil.Impf.1p of שׁקה | "we will make [him] drink" (cause to drink) |

Contrast each with its Qal: ילד Qal = "bear a child"; Hiphil = "cause to be born / beget." רכב Qal = "ride"; Hiphil = "cause to ride / make ride." קום Qal = "arise / stand"; Hiphil = "raise up / erect."

### 2. Declarative / estimative
Subject does not produce the action but pronounces / treats the object as having it.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Gen 18:28 | אַשְׁחִית | Hiphil.Impf.1s of שׁחת | "I will [not] destroy it" (classic causative; contextual declarative overlap) |
| 1 Kings 8:32 | הַרְשִׁיעַ / הַצְדִּיק | Hiphil InfCst of רשׁע / צדק | "condemning / justifying" (declare guilty / righteous) |

### 3. Internal causative / intransitive outcome
Subject causes itself to enter the Qal state — the Hiphil looks semantically intransitive in English.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Gen 3:16 | אַרְבֶּה | Hiphil.Impf.1s of רבה | "I will [greatly] multiply" (cause to be many) |
| Gen 22:17 | אַרְבֶּה | Hiphil.Impf.1s of רבה | "I will multiply thy seed" |
| Gen 4:7 | תֵּיטִיב | Hiphil.Impf.2ms of יטב | "if thou doest well" (cause [oneself/action] to be good) |
| Gen 1:11 | תַּֽדְשֵׁא | Hiphil.Impf.3fs of דשׁא | "let the earth bring forth [grass]" (cause grass to sprout) |

### 4. Denominative / productive
Derives verbs from nouns, often expressing "produce / yield X."

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Gen 3:18 | תַּצְמִיחַ | Hiphil.Impf.3fs of צמח | "[thorns] shall it bring forth" |
| Gen 1:24 | תֹּוצֵא | Hiphil.Impf.3fs of יצא | "let the earth bring forth" (cause to go out) |

## Contrast with Qal (Base Stem)

| Root | Qal (G-stem) | Hiphil (H-stem / causative) |
|------|--------------|------------------------------|
| קום | *yāqûm* "he will arise / stand" | *yāqîm* "he will raise up / erect" |
| בוא | *yābôʾ* "he will come" | *yābîʾ* "he will bring / cause to come" |
| ילד | *yēlēd* "she will bear [a child]" | *yôlîd* "he will beget / sire" |
| ראה | *yirʾeh* "he will see" | *yarʾeh* "he will show / cause to see" |
| שׁוב | *yāšûb* "he will return" | *yāšîb* "he will bring back / restore" |
| היה | *yihyeh* "he will be" | **(unattested — see below)** |

The Qal expresses the action with its natural subject; the Hiphil introduces an external causer that brings about that action in a different object. This is the key semantic move: **Qal = "X happens"; Hiphil = "someone causes X to happen."**

## Contrast with Other Causative-Related Stems

| Stem | Function | Example |
|------|----------|---------|
| **Hiphil** | Active causative ("cause to do") | הֵקִים "he raised up" |
| **Hophal** | Passive of Hiphil ("be caused to do") | הוּקַם "he was raised up" |
| **Piel** | Factitive / intensive / resultative (brings about a state) | כִּלָּה "he finished / brought to completion" |
| **Pual** | Passive of Piel | כֻּלָּה "it was finished" |
| **Niphal** | Simple passive / middle / reflexive | נִכְרַת "he was cut off" (see [stem-niphal](stem-niphal.md)) |

Piel and Hiphil overlap semantically but differ in focus: Piel typically **brings about a state** (factitive — "make X into Y"), while Hiphil **causes an agent to perform an action** (causative proper — "make X do Y"). With certain roots only one of the two is attested.

## The YHWH Causative-Etymology Debate

A well-known alternative etymology of the Tetragrammaton YHWH (יהוה) proposes that it is a **Hiphil Imperfect 3ms of the verb היה / הוה "to be,"** yielding *yahweh* < *yahwî* / *yahwê* with the meaning **"He causes to be"** / **"He brings into being"** / **"He who creates/sustains existence."** The major proponent was **W. F. Albright** (*From the Stone Age to Christianity*, 1940; *Yahweh and the Gods of Canaan*, 1968), followed by D. N. Freedman, F. M. Cross (*Canaanite Myth and Hebrew Epic*, 1973, pp. 60–75), and others. On this reading, YHWH is a clipped cultic epithet from something like *yahwê ṣəbāʾôt* "He who creates the (heavenly) hosts."

### Arguments advanced for the Hiphil reading
1. **Vowel pattern:** the traditionally reconstructed pointing *yahwê* (cf. Theodoret's Ἰαβέ, Clement's Ἰαουέ) aligns phonologically with a Hiphil *yaqtil/yaqtel* preformative (yod + *a* + first root consonant), not a Qal *yiqtol* (yod + *i* + first root consonant, expected *yihyeh*).
2. **III-weak pattern:** for III-yod/ה roots, the Hiphil Impf. 3ms ends in segol/tsere (e.g., יַרְבֶּה, יַעֲלֶה, יַרְאֶה), matching *yahweh* better than the Qal *yihyeh*.
3. **Divine-epithet parallels:** other West-Semitic divine names are causative participles/verbs of creation (e.g., *ʾēl qōneh* "El-creator"; Ugaritic *bny bnwt* "creator of creatures").
4. **Theological fit with Genesis 1:** a creator-God named "He causes to be" mirrors the עשׂה/ברא/אמר creation verbs and anchors the divine name in the role of Maker.

### Counter-arguments — grammatical
1. **No Hiphil of היה is attested anywhere in the Hebrew Bible.** Parsing the full lemma inventory (hebrew_parser.py `--lemma "היה"`) returns occurrences **only in Qal and Niphal**. There is **zero** Hiphil, Piel, Pual, Hophal, or Hithpael form of היה in ~3,500+ occurrences. Causative "bring into being" is regularly expressed by other roots (ברא, עשׂה, יצר, כון Hiphil, קום Hiphil, ילד Hiphil) — never by היה.
2. **No Hiphil of cognate הוה either.** The alternative root הוה (archaic/Aramaic "to be/become") appears in the Hebrew Bible essentially only as part of the Tetragrammaton itself and in a handful of Qal forms (e.g., Eccl 2:22, Neh 6:6) — never as a Hiphil.
3. **Exodus 3:14 reads Qal, not Hiphil.** God's self-interpretation אֶהְיֶה אֲשֶׁר אֶהְיֶה is pointed and parsed as **Qal Impf. 1cs** of היה ("I AM / I WILL BE"), not Hiphil ("I cause to be"). The inspired in-text gloss of the name is a Qal existential, not a causative.
4. **Masoretic pointing.** The traditional Qere perpetuum substitutes אֲדֹנָי, so the original vowels are uncertain; reconstructions of *yahwê* remain hypothetical. The consonants יהוה are equally compatible with a Qal Impf. 3ms of an archaic *hwy* root ("he is / he will be") and require no Hiphil.
5. **Distribution of causative preformative patterns.** The Hiphil Impf. 3ms typically shows patach or segol under the preformative yod (יַ־/יֶ־) with a long *î* theme (יָקִים, יָבִיא, יוֹלִיד). While III-weak roots do end in segol (יַרְבֶּה), the full Hiphil pattern yahwê is only one of several possible readings of the consonantal skeleton — not forced by morphology.
6. **Semitic comparative data is mixed.** Amorite and Ugaritic theophoric names do contain causative-style verbs, but the correspondence is contested; the same names are also read as Qal/G-stem by many Semitists (e.g., J. A. Fitzmyer; H. Ringgren, *TDOT* V:500–521).

### Qal reading
The mainstream alternative takes YHWH as a **Qal Impf. 3ms** (possibly of an archaic *hwy* form prior to the standard Hebrew *hyy*), meaning simply **"He is"** / **"He will be"** / **"He who is / will be." This matches:
- Exodus 3:14's in-text Qal gloss אֶהְיֶה (1cs of the same verb, same stem)
- The total absence of any Hiphil of היה in the canonical corpus
- The Septuagint rendering ἐγώ εἰμι ὁ ὤν ("I am the Being One," Exod 3:14 LXX) — existential, not causative
- Ancient Jewish exegesis (Targums, rabbis, Josephus)

### Summary table of the debate

| Reading | Stem | Gloss | Chief evidence for | Chief evidence against |
|---------|------|-------|-------------------|-----------------------|
| **Qal** | G | "He is / will be" | Exod 3:14 Qal gloss; all attested היה forms are Qal/Niphal; LXX ὁ ὤν | Reconstructed pointing *yahwê* less natural for Qal |
| **Hiphil** | H | "He causes to be / brings into being" | Reconstructed *yahwê* vowel-pattern; Amorite/Ugaritic theophoric parallels; theological fit with creator-role | **No Hiphil of היה or הוה attested in the Hebrew Bible**; Exod 3:14 reads Qal; Qere-perpetuum obscures original vowels |

Both readings are grammatically **possible** from the bare consonants יהוה; the dispute turns on (a) reconstructed vocalization, (b) comparative Semitic typology, and (c) how much weight to give Exodus 3:14's Qal self-interpretation versus external cognate evidence.

## Grammar Citations

- **Gesenius-Kautzsch-Cowley (GKC) §53** — Hiphil conjugation (formation, meaning, paradigm)
- **Joüon-Muraoka §54** — Hiphil as causative H-stem; §113 on imperfect aspect
- **Waltke-O'Connor (IBHS) §27** — "The Causative Stems: Hiphil and Hophal" (pp. 433–452); §27.2 on causative-factitive / declarative-estimative / denominative subdivisions
- **van der Merwe-Naudé-Kroeze, *Biblical Hebrew Reference Grammar* §16.5** — Hiphil functions with examples
- **HALOT / BDB** s.v. היה — list only Qal and Niphal; no Hiphil entry
- **TDOT III:369–381 (Jenni/Westermann on היה)** — notes absence of Hiphil of היה
- **TDOT V:500–521 (Ringgren on YHWH)** — surveys Qal vs. Hiphil etymology debate
- **F. M. Cross, *Canaanite Myth and Hebrew Epic* (1973), pp. 60–75** — Hiphil causative proposal
- **W. F. Albright, *From the Stone Age to Christianity* (1957), pp. 258–261** — classic Hiphil-causative argument

---
*Generated from: hebrew_parser.py --search "sp=verb vs=hif vt=impf" (30+ results), --lemma "היה" (full corpus), --verse Deut 18:15 / Gen 41:43, KJV text*
*Last updated: 2026-04-18*
