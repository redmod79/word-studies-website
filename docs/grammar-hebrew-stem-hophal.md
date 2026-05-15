# Hophal Stem (Hebrew)

## Definition

The **Hophal** (הָפְעַל / הֻפְעַל; also spelled *Hŏp̄ʿal*, *Hophʿal*, *Hopʿal*) is the **passive counterpart of the Hiphil** — the causative-passive stem. Where Hiphil says "X caused Y to do/become Z," Hophal says "Y was caused to do/become Z" — with the causer typically **unnamed**. The Hophal is morphologically marked by a *u*-class preformative vowel (*hû-* / *ho-* / *hā-*) and a *short-a* theme vowel.

The stem is comparatively rare (~440 occurrences in BH, vs. ~9,000 Hiphil) but carries outsized theological freight because of its **systematic agent-suppression**. Classic "divine passive" readings cluster here.

Core functions:

1. **Causative passive** — subject undergoes the Hiphil action from an unnamed causer ("was brought," "was struck down," "was taken away")
2. **Agent-occluded passive** — grammar deliberately suppresses who caused the action; often theologically loaded (divine agency implied but not named, or agency deliberately ambiguous)
3. **Stative-result of a causation** — subject is in the resulting state of a prior Hiphil action ("was set up," "was established"; esp. participle)

## Form Recognition

### Morphological markers
- **Perfect:** *huqṭal* / *hoqṭal* (הָקְטַל) — short-*u* or short-*o* preformative vowel, short-*a* theme: הוּרַד "was brought down" (Gen 39:1), הֻכָּה "was smitten" (Exo 22:1), הוּשַׁב "was returned" (Gen 42:28), הוּרַם "was taken away" (Dan 8:11), הֻשְׁלַךְ "was cast down" (Dan 8:11), הוּבָא "was brought" (Lev 13:2), הֻסַּר "was removed" (Dan 12:11)
- **Imperfect:** *yuqṭal* / *yoqṭal* (יֻקְטַל) — short-*u* preformative, short-*a* theme: יוּמָת "shall be put to death" (Exo 21:12, etc., ~17×), יֻקַּם "shall be avenged" (Gen 4:15), יֻקַּח "shall be taken" (Gen 18:4), יֻחַן "shall be favored" (Isa 26:10), תּוּקַד "shall be kept burning" (Lev 6:2)
- **Wayyiqtol:** *wayyuqṭal*: וַיֻּגַּד "and it was told" (Gen 22:20; 27:42; 31:22; 38:13, 24 — the formulaic narrative passive), וַיֻּכּוּ "and they were beaten" (Exo 5:14)
- **Participle:** *muqṭal* / *moqṭal* (מֻקְטָל): מֻצָּב "set up" (Gen 28:12 Jacob's ladder), מוּצֵאת "brought forth" (Gen 38:25), מֻכִּים "beaten" (Exo 5:16)
- **Infinitive Construct:** הֻלֶּדֶת "being born" (Gen 40:20)
- **Imperative:** rare — הָשְׁכְּבָה "be laid down!" (Ezek 32:19)

### Diagnostic features
- **Short-*u* (qibbuṣ) or short-*o* (qamets-ḥaṭuph) preformative vowel** is the single most reliable marker — Hiphil has long-*î* theme; Hophal replaces this with short-*a* and darkens the preformative from *hi-/ya-* to *hu-/yu-*
- Often spelled **full** with *waw*: הוּ־ (hu-) for 3ms perfect (הוּרַד, הוּבָא, הוּרַם)
- **No agent** typically expressed — when an agent does appear it is introduced with בְּיַד or מִן (by the hand of / from), and even then is often left unnamed
- For I-*w*/*y* roots (ירד, ילד, יצא), the initial *y* assimilates and the form looks like *hû-* + CCaC (הוּרַד, הוּלַד, הוּצָא)
- For geminate roots (סבב, קלל), theme vowel often lengthens (הוּסַב "was turned")

### Parser code
`sp=verb vs=hof` — any Hophal form
`sp=verb vs=hof vt=perf` — Hophal Perfect (*huqṭal*)
`sp=verb vs=hof vt=impf` — Hophal Imperfect (*yuqṭal*)
`sp=verb vs=hof vt=wayq` — Hophal Wayyiqtol
`sp=verb vs=hof vt=ptca` — Hophal Participle (*muqṭal*)

**Total inventory:** 434 occurrences across the Hebrew Bible (ETCBC/BHSA tagging, parser-verified).

## Functions with Examples

### 1. Causative passive (primary function)
Subject undergoes the Hiphil-causative action; the causer is grammatically passive-suppressed.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Gen 39:1 | הוּרַד | Hophal.Perf.3ms of ירד | "Joseph **was brought down** to Egypt" (causer = Ishmaelites, suppressed in the verb itself) |
| Gen 42:28 | הוּשַׁב | Hophal.Perf.3ms of שׁוב | "My money **is restored**" (Joseph's doing, but to the brothers it is agent-unknown) |
| Gen 12:15 | תֻּקַּח | Hophal.Wayq.3fs of לקח | "the woman **was taken** into Pharaoh's house" |
| Lev 13:2 | הוּבָא | Hophal.Perf.3ms of בוא | "then he **shall be brought** unto Aaron" (priestly-procedural passive) |
| Exo 22:1 | הֻכָּה | Hophal.Perf.3ms of נכה | "if the thief **be smitten**" |
| Jer 38:22 | מֻצָּאוֹת | Hophal.Ptcp.fp of יצא | "**shall be brought forth** to the king of Babylon's princes" |

### 2. Agent-occluded / legally-passive formula
Hophal is the workhorse of Pentateuchal legal passives — "he shall be put to death," "shall be avenged," "shall be burnt" — where the law names the crime and the penalty but **not the executioner**. The grammar presses the act into the impersonal.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Exo 21:12 | יוּמָת | Hophal.Impf.3ms of מות | "he that smiteth a man... **shall be surely put to death**" (mot yûmāt formula) |
| Exo 21:15, 16, 17; 22:18 | יוּמָת | Hophal.Impf.3ms of מות | repeated capital-penalty formula (~17× Hophal of מות) |
| Gen 4:15 | יֻקָּם | Hophal.Impf.3ms of נקם | "vengeance **shall be taken on him** sevenfold" |
| Gen 4:24 | יֻקַּם | Hophal.Impf.3ms of נקם | "Cain **shall be avenged** sevenfold" |
| Lev 6:2 | תּוּקַד | Hophal.Impf.3fs of יקד | "the fire **shall be kept burning**" (perpetual-altar formula; cultic impersonal-passive) |

The Hophal here encodes the **legal third-person impersonal** — Hebrew has no indefinite "one" pronoun (no *man* like German, no *on* like French), so the agent-occluded passive Hophal fills that slot.

### 3. Narrative reporting-formula וַיֻּגַּד ("and it was told")
The wayyiqtol of נגד "tell, declare" appears ~40× as a Hophal, becoming a stock narrative device: *news reaches the character, reporter unnamed*. This keeps the focal subject (Abraham, Jacob, Judah, Pharaoh) the grammatical patient of information-delivery rather than the doer.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Gen 22:20 | וַיֻּגַּד | Hophal.Wayq.3ms of נגד | "that **it was told** Abraham" |
| Gen 27:42 | וַיֻּגַּד | Hophal.Wayq.3ms of נגד | "these words of Esau her elder son **were told** to Rebekah" |
| Gen 31:22 | וַיֻּגַּד | Hophal.Wayq.3ms of נגד | "**it was told** Laban on the third day" |
| Gen 38:13, 24 | וַיֻּגַּד | Hophal.Wayq.3ms of נגד | "**it was told** Tamar / Judah" |
| Exo 14:5 | וַיֻּגַּד | Hophal.Wayq.3ms of נגד | "**it was told** the king of Egypt that the people fled" |

### 4. Stative-result participle (*muqṭal*)
The participle describes the object in its **resulting state** from a prior Hiphil causation.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Gen 28:12 | מֻצָּב | Hophal.Ptcp.ms of יצב | "a ladder **set up** on the earth" (Jacob's ladder — the ladder is in a set-up state) |
| Exo 5:16 | מֻכִּים | Hophal.Ptcp.mp of נכה | "thy servants **are beaten**" |
| Gen 43:18 | מוּבָאִים | Hophal.Ptcp.mp of בוא | "we **are brought in**" |
| Lev 6:14 | מֻרְבֶּכֶת | Hophal.Ptcp.fs of רבך | "when it is **soaked** [in oil]" |

### 5. Agent-suppressed theological passive (Daniel's preferred stem for violent reversal)
Daniel uses Hophal with striking density at the climactic moments of his visions — moments where the text refuses to name who acts. The grammar is the theology: **something is happening to the sanctuary / the horn / the beast, and the text will not say who is doing it.**

| Reference | Hebrew | Parsing | KJV | Agent-occlusion |
|-----------|--------|---------|-----|-----------------|
| Dan 7:4 | הֳקִימַת | Hophal.Perf.3fs of קום (Aramaic) | "[the lion] **was made to stand** upon the feet as a man" | passive divine forming of the beast-vision |
| Dan 7:11 | הוּבַד | Hophal.Perf.3ms of אבד (Aramaic) | "his body **destroyed**" | beast is destroyed; doer unnamed |
| Dan 8:11 | הוּרַם | Hophal.Perf.3ms of רום | "the daily [sacrifice] **was taken away**" | *hûram hat-tāmîḏ* — horn is the surface context, but the Hophal grammatically obscures the actor |
| Dan 8:11 | הֻשְׁלַךְ | Hophal.Perf.3ms of שׁלך | "the place of his sanctuary **was cast down**" | *hušlaḵ məḵôn miqdāšô* — paired agent-suppressed passive |
| Dan 12:11 | הוּסַר | Hophal.Perf.3ms of סור | "from the time that the daily [sacrifice] **shall be taken away**" | lexical bracket-partner to 11:31's Hiphil active — deliberate stem-alternation between parallel passages |

**Dan 8:11 textual-critical note.** The MT reads הוּרַם (Hophal "was taken away"). Some MSS and ancient versions present Hiphil-active variants ("he [the horn] took away"). The difference is one of voice-grammar and theological framing:
- **Hophal reading:** the removal is agent-suppressed — the horn is not the grammatical subject of the verb; the text refuses to say who causes the continual to be taken away. This admits a divine-permissive reading ("the continual was taken away" — ultimately under God's overruling allowance).
- **Hiphil reading:** the horn is the active causer ("he took away the continual") — a straightforward human-wicked-agent reading.

The Masoretic Hophal is the harder reading and is followed by most critical editions. The interpretive payoff is significant: the Hophal refuses to make the horn the uncaused agent of the desolation, leaving open the question of whose hand ultimately moves the history.

### 6. Rhetorical-favor passive
A small but pointed class where Hophal expresses that favor or a privileged state **is bestowed** (or refused) by an unnamed giver — typically God.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Isa 26:10 | יֻחַן | Hophal.Impf.3ms of חנן | "let favor **be shewed** to the wicked, yet will he not learn righteousness" — divine-grace passive; God is the unnamed favor-giver |
| Job 38:6 | הָטְבָּעוּ | Hophal.Perf.3p of טבע | "[the earth's] foundations **were fastened/sunk**" — cosmic-creation passive; YHWH is the unnamed fixer |
| Ezek 32:32 | הֻשְׁכַּב | Hophal.Perf.3ms of שׁכב | "he **shall be made to lie** in the midst of the uncircumcised" — underworld-consignment passive |
| Ezek 32:19 | הָשְׁכְּבָה | Hophal.Impv.2ms of שׁכב | "**be thou laid** with the uncircumcised!" — rare Hophal imperative; addressee is commanded *to be caused to lie down* |

## Contrast with Related Passive Stems

Hebrew has **four passive-capable stems**, each the passive of a different active stem:

| Active stem | Its passive | Semantic note | Example root: קדשׁ "be holy" |
|-------------|-------------|---------------|-------------------------------|
| Qal (basic) | Niphal (simple passive / reflexive / middle) | generic passive | — (Qal stative for this root) |
| Piel (factitive: make-X) | Pual (intensive passive: was-made-X) | strong result-passive | *qiddēš* "consecrated" → *quddaš* "was consecrated" |
| Hiphil (causative: cause-to-X) | **Hophal (causative passive: was-caused-to-X)** | **agent-suppressed** | *hiqdîš* "dedicated" → *huqdaš* "was dedicated" |
| Hithpael (reflexive) | — (self-reflexive) | *hitqaddēš* "sanctify oneself" | |

### Hophal vs. Niphal
Both translate as English "was X-ed," but they are **not interchangeable**:
- **Niphal** is the passive of a **Qal active** — a single event, one level of causation. Nothing is implied about a causer beyond the subject's own lack of agency.
- **Hophal** is the passive of a **Hiphil causative** — there is a causer in the semantic frame, but the grammar suppresses naming it. The event has **two levels** (causer → instrument → patient), and the Hophal fronts the patient while occluding the causer.

| Hophal | Niphal of same root | Semantic difference |
|--------|---------------------|---------------------|
| הוּרַד "was brought down" (external causer did this to him) | (Qal passive ptcp יוּרָד / Niphal not attested) | Hophal of ירד implies an agent who *caused* the descent (Gen 39:1 Joseph to Egypt) |
| הוּבָא "was brought in" (someone brought him) | בָא Qal "came" (of himself) | Hophal requires a causer; Qal is self-motion |
| יוּמָת "shall be put to death" (legal executioner unnamed) | נִכְרַת "shall be cut off" (divine-judicial passive, often self-effected) | Hophal mot-yumat presupposes a human executing the sentence; Niphal *nikhrat* often describes a state of excommunication without external execution |

Link: [stem-niphal.md](stem-niphal.md)

### Hophal vs. Pual
Both are passives of transitive stems (Hiphil, Piel), and for some roots both exist with distinct semantic force:
- **Pual** = was intensively/resultatively made X (focuses on **state brought about**)
- **Hophal** = was caused to perform/undergo X (focuses on **external causation**)

Example: גנב (steal). The parser tags Gen 40:15 *gunnab gunnabtî* ("I was surely stolen away") as **Pual** — the intensification here is on the thoroughness of the act, not the agency behind it. A Hophal of גנב is unattested. This shows the stems are not freely interchangeable.

## Contrast with Hiphil (active-passive voice pair)

| Form | Voice | Example | Gloss |
|------|-------|---------|-------|
| **Hiphil** | active causative | הֵקִים *hēqîm* | "he raised up" |
| **Hophal** | passive of Hiphil | הוּקַם *hûqam* | "he was raised up" |
| **Hiphil** | active causative | הֵבִיא *hēbîʾ* | "he brought" |
| **Hophal** | passive of Hiphil | הוּבָא *hûbāʾ* | "he/it was brought" |
| **Hiphil** | active causative | הִכָּה *hikkāh* | "he smote" |
| **Hophal** | passive of Hiphil | הֻכָּה *hukkāh* | "he was smitten" |
| **Hiphil** | active causative | הִגִּיד *higgîd* | "he told, declared" |
| **Hophal** | passive of Hiphil | הֻגַּד *huggad* | "it was told" |
| **Hiphil** | active causative | הוֹרִיד *hôrîd* | "he brought down" |
| **Hophal** | passive of Hiphil | הוּרַד *hûrad* | "he was brought down" |

**Lexical-bracket phenomenon.** Several Danielic and prophetic passages pair the Hiphil and Hophal of the same root across parallel verses to mark active/passive framing of the same event:
- Dan 11:31 Hiphil active (human subject "they shall take away") ‖ Dan 12:11 Hophal passive (same event, agent-suppressed)
- Dan 8:11 MT Hophal ‖ variant Hiphil (textual contest over voice, same event)
- Ezek 32:32 Hophal *hushkab* "shall be made to lie" ‖ Ezek 32:19 Hophal imperative *hoshkebah* framed by a Qal imperative *rědāh* "go down!" (active-to-passive grammar of being driven into Sheol)

Link: [stem-hiphil.md](stem-hiphil.md)

## Common Hophal Verbs

| Verb root | Strong's | Hiphil meaning | Hophal meaning | Representative references |
|-----------|----------|----------------|----------------|---------------------------|
| מות (mut) | H4191 | (Hiphil *hēmît*) "put to death" | **יוּמָת "shall be put to death"** | Exo 21:12, 15, 16, 17; Lev 20:2 (~17× legal formula) |
| נגד (nagad) | H5046 | (Hiphil only) "tell, declare" | **הֻגַּד "it was told"** | Gen 22:20; 27:42; 31:22; 38:13, 24 (~40× narrative formula) |
| נקם (naqam) | H5358 | "avenge" | יֻקַּם "shall be avenged" | Gen 4:15, 24; Exo 21:21 |
| לקח (laqach) | H3947 | "take" | יֻקַּח "shall be taken" | Gen 12:15; 18:4 |
| בוא (bo) | H935 | "bring in" | הוּבָא "was brought" | Lev 13:2, 9; Gen 43:18 |
| ירד (yarad) | H3381 | "bring down" | הוּרַד "was brought down" | Gen 39:1 |
| שׁוב (shub) | H7725 | "restore, bring back" | הוּשַׁב "was returned" | Gen 42:28; Exo 10:8 |
| רום (rum) | H7311 | "raise, lift up" | **הוּרַם "was taken away / raised"** | Dan 8:11 |
| שׁלך (shalak) | H7993 | "cast down" | **הֻשְׁלַךְ "was cast down"** | Dan 8:11 |
| סור (sur) | H5493 | "remove, take away" | **הוּסַר "was taken away"** | Dan 12:11 |
| נכה (nakah) | H5221 | "smite" | הֻכָּה / מֻכִּים "was smitten / beaten" | Exo 5:14, 16; 22:1 |
| חנן (chanan) | H2603 | "show favor" | יֻחַן "be favored" | Isa 26:10 |
| שׁכב (shakab) | H7901 | "lay down" | הֻשְׁכַּב "was made to lie down" | Ezek 32:32 |
| טבע (tava) | H2883 | "sink, fasten" | הָטְבְּעוּ "were sunk/fastened" | Job 38:6; Jer 38:22 |
| יקד (yaqad) | H3344 | "kindle" | תּוּקַד "shall be kept burning" | Lev 6:2, 5, 6 |
| יצב (yatsav) | H3320 | "set, station" | מֻצָּב "set up" | Gen 28:12 |

## Why Hophal matters theologically

The Hophal is the **agent-occluded passive** of Hebrew. When the grammar turns Hophal three phenomena commonly follow in the discourse:

1. **Divine-permissive framing.** The text reports an event without making any creature its sufficient cause. The Hophal leaves room for YHWH's overruling providence without directly naming Him — the *textus apertus* of divine agency. This is how Daniel narrates desecrations of the sanctuary (8:11 *hûram*, *hušlaḵ*; 12:11 *hûsar*): the grammar refuses to credit the horn with uncaused destruction, preserving the theological point that no action against God's holy things happens except under His permission.
2. **Legal-impersonal framing.** In Pentateuchal law the executioner of the death-penalty is almost never named as grammatical subject; the offender *yûmāt* "shall be put to death." Responsibility is distributed across the covenant community without being pinned on a named agent.
3. **Text-critical leverage.** Because Hophal and Hiphil differ by only a single vowel (short-*u* + short-*a* vs. long-*î*), and the Masoretic pointing post-dates the consonantal text by many centuries, Hophal/Hiphil alternation is a **live textual variable**. Dan 8:11's *hûram* (Hophal MT) vs. *hērîm* (Hiphil variant) is a textbook case: the consonants are identical (הרים), and the voice of the verb — and thus the theological frame — depends on the pointing. Manuscripts, LXX evidence, and exegetical tradition frequently diverge at these points.

For Dan 8:11 specifically, the MT Hophal is defended by the majority of critical editions (BHS, BHQ) and is the harder reading. The Hiphil variant makes the horn the uncaused agent; the Hophal preserves the text's deliberate agency-ambiguity. This is not a minor pointing dispute — it is a voice-level theological choice.

## Grammar Citations

- **GKC §53** — Hophal conjugation, paradigms, agent-suppression functions
- **GKC §53u** — agent expressed with בְּיַד or מִן after Hophal
- **Joüon-Muraoka §56–57** — Hophal morphology (*huqṭal* / *hoqṭal* variants), agent-neutral passive
- **Waltke-O'Connor (IBHS) §28** — The Causative-Passive Stem (Hophal); §28.1 on voice-pairing with Hiphil; §28.2 on semantic functions (passive of Hiphil, rarely stative-resultative)
- **van der Merwe-Naudé-Kroeze §16.6** — Hophal usage and its rarity
- **BHRG §16.6** — Hophal's agent-suppression and legal-impersonal function
- **BDB / HALOT** — entries for verbs listed above, noting Hophal-specific glosses

---
*Generated from: hebrew_parser.py --search "sp=verb vs=hof" (434 total occurrences across HB); --verse for Dan 8:11, Gen 40:15, Job 38:6, Isa 26:10, Ezek 32:23/32, Gen 22:20, Gen 28:12, Gen 39:1, Lev 6:2, Lev 13:2, Exo 21:12; KJV text for cross-verification; ETCBC/BHSA morphological tagging*
*Last updated: 2026-04-19*
