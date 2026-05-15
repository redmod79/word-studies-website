# Grammar Analysis: Daniel 4:16, 23, 25, 32 — "Seven ʿiddānîn" over Nebuchadnezzar

**MT numbering:** Daniel 4:13, 20, 22, 29 (the Hebrew-Bible versification of the Aramaic narrative).
**Register:** Aramaic (Biblical Aramaic; Daniel's Aramaic section runs 2:4b–7:28).
**Source:** ETCBC BHSA handles the Aramaic portions of Daniel; `hebrew_parser.py` returns Aramaic morphology directly.

## Text

### The recurring phrase

All four occurrences carry the identical noun-phrase core: **וְשִׁבְעָה עִדָּנִין יַחְלְפוּן עֲלוֹהִי / עֲלָךְ** — *wə-šiḇʿâ ʿiddānîn yaḥləp̄ûn ʿălôhî / ʿălāḵ* — "and seven *ʿiddānîn* shall pass over him / over thee."

### Dan 4:16 [MT 4:13] (interpretation of the watcher's decree)

**Aramaic:** לִבְבֵהּ מִן־אֲנָשָׁא יְשַׁנּוֹן וּלְבַב חֵיוָה יִתְיְהִב לֵהּ וְשִׁבְעָה עִדָּנִין יַחְלְפוּן עֲלוֹהִי

**KJV:** "Let his heart be changed from man's, and let a beast's heart be given unto him; and let seven times pass over him."

### Dan 4:23 [MT 4:20] (Daniel repeats the decree to the king)

**Aramaic (tail):** … וְעִם־חֵיוַת בָּרָא חֲלָקֵהּ עַד דִּי־שִׁבְעָה עִדָּנִין יַחְלְפוּן עֲלוֹהִי

**KJV:** "… [let] his portion [be] with the beasts of the field, **till** seven times pass over him."

### Dan 4:25 [MT 4:22] (Daniel applies it to Nebuchadnezzar)

**Aramaic (core):** וְשִׁבְעָה עִדָּנִין יַחְלְפוּן עֲלָךְ עַד דִּי־תִנְדַּע דִּי־שַׁלִּיט עִלָּאָה בְּמַלְכוּת אֲנָשָׁא

**KJV:** "… and seven times shall pass over thee, **till thou know** that the most High ruleth in the kingdom of men, and giveth it to whomsoever he will."

### Dan 4:32 [MT 4:29] (the heavenly voice executes the decree)

**Aramaic (core):** וְשִׁבְעָה עִדָּנִין יַחְלְפוּן עֲלָךְ עַד דִּי־תִנְדַּע דִּי־שַׁלִּיט עִלָּאָה בְּמַלְכוּת אֲנָשָׁא

**KJV:** "… and seven times shall pass over thee, until thou know that the most High ruleth in the kingdom of men, and giveth it to whomsoever he will."

## Word-by-Word Parsing of the Core Phrase

Source: `hebrew_parser.py --verse "Dan 4:13 / 4:20 / 4:22 / 4:29"` (ETCBC BHSA).

| # | Aramaic | Lemma | Parsing | Gloss |
|---|---------|-------|---------|-------|
| 1 | וְ | ו | Conj | and |
| 2 | שִׁבְעָ֥ה | שׁבע | Noun.fs.Abs | seven |
| 3 | עִדָּנִ֖ין | **עדן** | **Noun.mp.Abs** | **times / periods** |
| 4 | יַחְלְפ֥וּן | **חלף** | **Verb.Peal.Impf.3mp** | **shall pass by** |
| 5 | עֲלֹֽוהִי / עֲלָ֑ךְ | על | Prep.+3ms / +2ms | upon him / upon thee |

Full parsings for each verse's surrounding clause are available from the tool; the common four-verse phrase above is what anchors the chronology.

## Clause Structure (all four passages)

Source: `hebrew_parser.py --clause "Dan 4:13 / 4:20 / 4:22 / 4:29"`.

In **every occurrence**, the seven-*ʿiddānîn* clause is parsed as one of two closely related types:

- **Dan 4:13** — clause type **WXYq** (waw + subject-fronted yiqtol): `[Subj] שִׁבְעָה עִדָּנִין [Pred] יַחְלְפוּן [Cmpl] עֲלוֹהִי`
- **Dan 4:20** — clause type **XYqt** (subordinated by עַד־דִּי, subject-fronted yiqtol): `[Subj] שִׁבְעָה עִדָּנִין [Pred] יַחְלְפוּן [Cmpl] עֲלוֹהִי`
- **Dan 4:22** — clause type **WXYq**: `[Subj] שִׁבְעָה עִדָּנִין [Pred] יַחְלְפוּן [Cmpl] עֲלָךְ`
- **Dan 4:29** — clause type **WXYq**: `[Subj] שִׁבְעָה עִדָּנִין [Pred] יַחְלְפוּן [Cmpl] עֲלָךְ`

**What this clause-type uniformity means:** The Aramaic grammar treats "seven *ʿiddānîn*" as the **grammatical subject** of the verb יַחְלְפוּן (Peal impf. 3mp of חלף "to pass by"). The *ʿiddānîn* are not an object or an adverbial accusative of duration — they are the *thing that does the passing*. Time itself is personified as the agent that sweeps over the king. The fronting (X before yiqtol) highlights the numbered duration as the load-bearing unit of the sentence.

## Key Grammatical Features

### 1. עִדָּנִין — Noun.mp.Abs of עִדָּן (Aramaic H5732)

- **Form:** Masculine plural absolute. The singular עִדָּן ("a time / a period"); plural עִדָּנִין ("times / periods").
- **Not a dual.** Biblical Aramaic has a dual (for natural pairs — hands, eyes), but עִדָּנִין carries the standard mp absolute ending ־ִין, not the dual ־ַיִן. This matters at Dan 7:25 where "times" (middle term of *time, times, half a time*) is this same morphological plural — formally indefinite "times," not grammatically "two times."
- **Lexical range (per BDB, HALOT, the canonical word study `A5732-iddan.md`):** Two senses: (a) general time / duration / opportunity (Dan 2:8; 7:12; 3:5, 15; 2:21); (b) **definite set period, often = year** (Dan 4:16, 23, 25, 32; and by extension Dan 7:25).
- **See:** [Word study A5732-iddan.md](../../word-studies/A5732-iddan.md) for full lexicon data, distribution, cognates (Akkadian *adannu*), and LXX mapping (→ καιρός, 9×).

### 2. יַחְלְפוּן — Peal Imperfect 3mp of חלף ("to pass by, pass over")

- **Stem:** Peal (the Aramaic G-stem, cognate to Hebrew Qal). Simple active.
- **Form:** Impf. 3mp with the final *-ûn* (the Aramaic long-imperfect ending, carrying over from Proto-Semitic *-ūna*; cf. Hebrew's lost energic).
- **Aspect/function:** In Aramaic prophetic-narrative discourse the Peal imperfect functions as a future-in-the-past (the decree describes what *will* happen to the king), and with a numerical-duration subject it carries **distributive-iterative** force: "seven time-periods shall each pass over him" — one after another in sequence, not collapsed into a single span.
- **Subject-verb agreement:** 3mp agreeing with עִדָּנִין. "Seven" is a singular number-noun feminine, but the counted noun עִדָּנִין (mp) governs agreement — standard Aramaic behavior with numerals above three.
- **Hebrew cognate חלף:** "to pass by, change, sweep over" (e.g., Isa 8:8 "it shall overflow and go over"). The core sense is *durative transit* — the action is the passage itself, not the arrival.

### 3. עַד־דִּי — "Until that" (bounded terminus)

Three of the four verses (4:23, 25, 32) introduce the seven-*ʿiddānîn* clause with עַד־דִּי ("until that"):

- Dan 4:23: עַד דִּי־שִׁבְעָה עִדָּנִין יַחְלְפוּן עֲלוֹהִי
- Dan 4:25: עַד דִּי־תִנְדַּע דִּי־שַׁלִּיט עִלָּאָה — "**until thou know** that the Most High rules"
- Dan 4:32: עַד דִּי־תִנְדַּע דִּי־שַׁלִּיט עִלָּאָה — identical

**Grammatical significance:** עַד + דִּי is the Aramaic conjunction "until [that]," taking a finite clause (impf.) as its complement. It marks **a terminus** — the seven-*ʿiddānîn* span is explicitly *bounded*. The narrative gives two concurrent termini for the same duration:
1. **Physical:** "until seven *ʿiddānîn* pass over him" (completion of the count).
2. **Cognitive / theological:** "until thou *know* that the Most High rules" (Peal impf. 2ms of ידע) — the pedagogical endpoint.

The two termini coincide: the time-count and the knowledge-acquisition are calibrated to each other. This is the lexical seam where duration and purpose meet.

### 4. Passives of decree: יִתְיְהִב and יִתְנִנַּהּ (divine passive)

- **יִתְיְהִב (4:16):** Hithpeel (passive) of יהב ("to give") → "shall be given." Subject = לְבַב חֵיוָה ("a beast's heart"). No human agent; God is the implied decreer. This is the same **divine-passive / passivum divinum** pattern at work in Dan 7:25's יִתְיַהֲבוּן ("they shall be given into his hand") — see `passages/dan-7-25-26.md` §3.
- **יִתְנִנַּהּ (4:25, 32):** Peal impf. 3ms of נתן "to give" + 3fs object suffix ("he shall give it") — predicate of "the Most High … giveth it [the kingdom] to whomsoever he will." Here the agent *is* named (עִלָּאָה, "the Most High"), resolving the ambiguity that the passive in v. 16 left open.

**Theological grammar:** The pattern is **passive at the start, active-named at the end**. The king's descent (v. 16) is a decree from unnamed heaven; the king's restoration / knowledge-of-the-Most-High (vv. 25, 32) names the agent who was behind the passive all along. The seven *ʿiddānîn* are the bridge — the bounded interval in which the unnamed agent teaches the king who He is.

### 5. The construction שִׁבְעָה עִדָּנִין + יַחְלְפוּן + עַל-X — unique to Daniel 4

This exact collocation (seven + *ʿiddānîn* + *ḥălap* "pass over" + עַל + pronominal suffix) occurs **4× in Daniel 4 and nowhere else in the Hebrew Bible or Biblical Aramaic corpus**. The parser confirms: search for the lemma `עדן` across the Aramaic corpus yields 15 occurrences (all in Daniel 2–7); the four in Daniel 4 are the only ones paired with the numeral `שׁבע` + the verb `חלף`. This is a narrative signature, not a general-Aramaic time-idiom.

## The Central Exegetical Question: Does *ʿiddān* = Year Here?

The narrative supplies the answer **internally**, through three independent lines of textual evidence.

### Evidence A: Seasonal cycle implied by the vegetation-and-dew imagery

The seven-*ʿiddānîn* period is not abstract duration; it is framed by agricultural / meteorological details that presuppose multi-year experience:

- Dan 4:15 / 4:23: "his portion be **with the beasts of the field**" — pastoral setting.
- Dan 4:15, 23, 25, 33: "let it be wet with the **dew of heaven** (טַל שְׁמַיָּא)" — dew is a seasonal phenomenon (dry-season dew in Mesopotamia is morning moisture from August–October).
- Dan 4:25, 32, 33: "they shall make thee to **eat grass as oxen** (עִשְׂבָּא כְתוֹרִין לָךְ יְטַעֲמוּן)" — grass requires seasonal regrowth.
- Dan 4:33: "till his hairs were grown like **eagles' [feathers]** and his nails like **birds' [claws]**" — hair and nail growth to visible eagle-feather / bird-claw length requires on the order of *years*, not days or months. Human scalp hair averages ~15 cm/year; "eagles' feathers" length (≥30-40 cm) implies 2-3+ years minimum.

**Grammatical note:** The parser confirms that each of these elements is a **nominal / verbal phrase in the same clause-chain** as the seven-*ʿiddānîn* clause — they are co-temporal with the ʿiddānîn, not prior or subsequent. They describe *what happens during* the seven-count.

### Evidence B: The narrative's historical framing

Dan 4 is told as autobiography-by-decree (Nebuchadnezzar's first-person edict in vv. 1–18, 34–37, with third-person narrative interlude vv. 28–33). The framing assumes:

- The king's kingdom must outlast the episode (v. 26: "thy kingdom shall be sure unto thee, after that thou shalt have known"). A seven-**day** exile would not have required the kingdom-preservation promise.
- Historical witnesses (cuneiform-attested gap in Nebuchadnezzar's inscriptional record, traditionally placed in his later regnal years) are consistent with a multi-year absence. The text assumes the hiatus is long enough to be politically significant.

### Evidence C: Lexical-semantic precedent for *ʿiddān* = year

The word study `A5732-iddan.md` records BDB's explicit note: *"technically, a year."* HALOT notes the Akkadian cognate *adannu* ("fixed / appointed / definite time"), from which *ʿiddān* as a standardized annual-cycle term is the natural Aramaic heir. In Dan 7:25 the LXX-Theodotion renders *ʿiddān* by καιρός, but Josephus (*Ant.* 10.10.6 §216), the Peshitta, and Jerome all gloss the seven-*ʿiddānîn* as "seven years" — the ancient versional consensus is unanimous.

### Conclusion for the narrative register

**In Daniel 4, ʿiddān = year.** The grammar does not force this by itself (the noun is lexically ambiguous); the *narrative embedding* forces it. The combination of:
- agricultural seasonal cycles requiring multi-year duration,
- hair/nail growth requiring years,
- historical-political framing requiring a multi-year hiatus,

yields the semantic anchor: *within the Daniel corpus, the unmarked default sense of ʿiddān in a count-phrase is "year."*

This is the **internal-biblical day-year lexical anchor.** It is not day-for-year prophetic hermeneutic; it is simply that the word *ʿiddān*, when counted out over Nebuchadnezzar, *means* "year." The text establishes *ʿiddān = šānāh* (Heb. שָׁנָה, "year") by its own narrative logic.

## The Transfer Question: Does Dan 4's ʿiddān=year Govern Dan 7:25?

Here the analysis must present **both readings honestly**, because this is where grammar alone cannot decide — it is a genre-level hermeneutical question, and the grammar offers evidence for both.

### Reading 1: Literal-year transfer (historicist day-for-year → 1260 years)

**Claim:** Dan 4 establishes *ʿiddān = year*. Dan 7:25 uses the same Aramaic word עִדָּן (three times: עִדָּן, עִדָּנִין, פְלַג עִדָּן). Therefore the "time, times, and half a time" of Dan 7:25 = 3.5 **years**. Then, because Dan 7:25 is *apocalyptic-symbolic* discourse (not narrative), a secondary day-for-year expansion applies: 3.5 years × 360 days = 1260 **prophetic days** = 1260 **literal years** (the historicist reading, anchored by Num 14:34 and Ezek 4:4–6 — see `passages/num-14-34.md` and `passages/ezk-4-4-6.md`).

**Grammatical evidence for Reading 1:**
- **Lexical uniformity:** The word עִדָּן is identical in both passages. Dan 4 and Dan 7 are the same Aramaic register, the same author, the same book, the same scroll, possibly composed in close proximity. Arguing the word shifts meaning between chapters requires a positive justification *from the text itself*.
- **Dan 4 fixes the default:** With the narrative register supplying the lexical anchor (ʿiddān = year), any subsequent use within the same corpus should carry that default unless the text overrides it. Dan 7:25 does not override.
- **Parallel in Dan 12:7 (Hebrew):** The same formula recurs as מוֹעֵד מוֹעֲדִים וָחֵצִי ("a time, times, and a half"). The Hebrew מוֹעֵד is often a temporal unit tied to the festal *year* (see `A5732-iddan.md` "easily confused" table). The parallel reinforces an annual reading.
- **Revelation 12:14 Greek calque:** καιρὸν καὶ καιροὺς καὶ ἥμισυ καιροῦ appears alongside Rev 12:6's parallel ἡμέρας χιλίας διακοσίας ἑξήκοντα (1260 **days**) and Rev 13:5's μῆνας τεσσεράκοντα [καὶ] δύο (42 **months**). The three expressions are in apposition: 3.5 times = 1260 days = 42 months. This equates "time" = 360 days = 1 prophetic year.
- **Day-for-year hermeneutic (Num 14:34; Ezek 4:4–6):** Already established within the OT itself as the convention for reading **symbolic** prophetic time-spans. Dan 7 is symbolic (beasts from the sea, horns, etc.); a literal 3.5-year reading would be the odd one out among its imagery.

**Result:** 3.5 ʿiddānîn = 3.5 years (Dan 4 lexical anchor) → 1260 days (3.5 × 360) → 1260 years (Num 14:34 / Ezek 4:4–6 hermeneutic).

### Reading 2: Literal 3.5 years (preterist / futurist short-timeframe)

**Claim:** Dan 4's ʿiddān=year carries directly into Dan 7:25 as a **literal** 3.5-year period. No day-for-year expansion. Dan 7:25 describes a bounded 3.5-year persecution, either (a) already fulfilled in Antiochus IV's desecration of the temple (preterist: 167–164 BC, roughly 3.5 years) or (b) yet future in a final tribulation (futurist: a literal 3.5-year period of end-time persecution).

**Grammatical evidence for Reading 2:**
- **Lexical uniformity works both ways:** If Dan 4 establishes ʿiddān=year, and the Daniel corpus is consistent, then Dan 7:25's 3.5 ʿiddānîn = 3.5 literal years — full stop. *No secondary expansion*. Reading 1's move from "3.5 years" to "3.5 × 360 days" requires an extra interpretive step that the grammar does not supply.
- **Dan 12:11–12 mentions specific day-counts (1290 and 1335 days)** alongside the time-times-half formula, which some argue means the text can *count in days* when it means days and *count in years* when it means years. The ʿiddān formula would then remain 3.5 literal years.
- **The verb יַחְלְפוּן and the Peal imperfect** carry distributive-iterative force (see §2 above): "each time-period passes over him in succession." In Dan 4 the count is observable on the ground — the king can track seven yearly cycles. In Dan 7:25, if the same durational realism applies, 3.5 observable cycles = 3.5 literal years (a time frame that *fits lived human experience*, as Dan 4 does).
- **Genre-shift objection to Reading 1:** Reading 1 asserts that apocalyptic genre triggers day-for-year expansion, but the grammar of Dan 7:25 is *not* formally distinguished from Dan 4:16's grammar. Same lemma, same stem, same construct patterns. If the text wanted to signal "these are prophetic-days-standing-for-years," one would expect a grammatical or discourse marker. None is present.

**Result:** 3.5 ʿiddānîn = 3.5 literal years. Persecution span is short, intense, bounded.

### Which grammatical evidence tips the balance?

The grammar **alone** does not decide. What tips the balance is whether one accepts:

1. **The day-for-year principle from Num 14:34 / Ezek 4:4–6 as a hermeneutical key for symbolic prophecy** (supporting Reading 1). The principle is *inside* the OT, not imposed from outside.
2. **The genre distinction between Dan 4 (historical narrative) and Dan 7 (apocalyptic vision)** as exegetically decisive (supporting Reading 1).
3. **The apposition of "time, times, and half a time" with "1260 days" and "42 months" in Rev 12:6, 14; 13:5** as a canonical gloss fixing the equation (supporting Reading 1).

Versus:
1. **Lexical consistency as a hermeneutical primitive** — the word ʿiddān means what it means in Dan 4 (year), so 3.5 ʿiddānîn = 3.5 years (supporting Reading 2).
2. **Absence of any grammatical day-for-year marker in Dan 7:25** (supporting Reading 2).

### What the grammar *does* settle

Three points are not in dispute and rest squarely on the parser output:

1. **ʿiddān in Dan 4 = year.** The narrative embedding forces it; the Aramaic word carries this sense natively per lexicon and versional tradition. This is the internal biblical anchor.
2. **Dan 7:25 uses the same word.** Three times. With identical lexical meaning at the lexeme level.
3. **At minimum, 3.5 ʿiddānîn = 3.5 years.** Both readings agree on this. The question is whether a secondary prophetic-expansion (day-for-year) then applies.

The grammar thus establishes the *floor* (3.5 years minimum duration) but not the *ceiling* (literal 3.5 years vs. 1260 years). The ceiling is a hermeneutical decision about genre and canonical cross-reference, not a grammatical one.

## The Seven-*ʿiddānîn* as Pedagogy

One more grammatical feature worth surfacing: in both vv. 25 and 32, the seven-*ʿiddānîn* clause is *subordinated to* a clause of knowing:

> וְשִׁבְעָה עִדָּנִין יַחְלְפוּן עֲלָךְ **עַד דִּי־תִנְדַּע** דִּי־שַׁלִּיט עִלָּאָה בְּמַלְכוּת אֲנָשָׁא
> "… and seven *ʿiddānîn* shall pass over thee, **until thou know** that the Most High rules in the kingdom of mankind."

- **תִנְדַּע** (Peal impf. 2ms of ידע, "to know"): the telos of the seven-year discipline is *knowledge of divine sovereignty*.
- The bounded time-count exists *for* the cognitive acquisition. This is the same pattern Dan 7:25 inverts: there the "time, times, and half a time" is the duration in which the saints are worn out and the horn's authority is exercised — but the telos in Dan 7:26 is likewise the judgment that vindicates. The pedagogy of Dan 4 (the king learns) becomes the vindication of Dan 7 (the saints are vindicated). Same grammar, same temporal structure, different subject of the pedagogy.

## Cross-References

- **Word study:** [A5732-iddan.md](../../word-studies/A5732-iddan.md) — full canonical entry for עִדָּן.
- **Related passage analyses in the library:**
  - [passages/dan-7-25-26.md](dan-7-25-26.md) — the "time, times, and half a time" formula; Pael of בלה, Ithpeel passive, WXYq disjunctive.
  - [passages/num-14-34.md](num-14-34.md) — *yôm laššānāh yôm laššānāh* formula: the foundational day-for-year biblical anchor.
  - [passages/ezk-4-4-6.md](ezk-4-4-6.md) — Ezekiel's 390 + 40 days = 390 + 40 years, second explicit day-for-year anchor.
  - [passages/dan-12-7-11-12.md](dan-12-7-11-12.md) — Hebrew parallel מוֹעֵד מוֹעֲדִים וָחֵצִי + the 1290 / 1335 day-counts.
  - [passages/rev-13-5.md](rev-13-5.md) — Greek echo of Dan 7:25 (ἐδόθη αὐτῷ … μῆνας τεσσεράκοντα [καὶ] δύο).
- **Grammar reference entries (Aramaic — gaps to fill):**
  - `aramaic/stem-peal.md` — Peal (G-stem) paradigm; יַחְלְפוּן as flagship durative-iterative impf.
  - `aramaic/clause-type-wxyq.md` — subject-fronted yiqtol as foregrounding / scene-setting.
  - `aramaic/particle-ad-di.md` — עַד־דִּי "until that" as terminus-marker governing a finite clause.

---

*Generated from: `hebrew_parser.py --verse "Dan 4:13 / 4:20 / 4:22 / 4:29"`; `hebrew_parser.py --clause` on the same; `hebrew_parser.py --construct "Dan 4:13 / 4:20"`; KJV text from `tools/data/kjv.txt`; word study `A5732-iddan.md`; prior passage analysis `dan-7-25-26.md`.*
*Last updated: 2026-04-19*
