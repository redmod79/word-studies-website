# LXX Rendering of Hebrew Waw in Vow Apodoses (Greek)

## Definition

This entry catalogues how the Septuagint translators rendered the Hebrew coordinating particle **וְ** ("waw") when it heads a clause in the *apodosis* of a vow (condition-plus-weqatal pattern). The question has direct exegetical weight at **Judges 11:31**, where the contested waw on וְהַעֲלִיתִיהוּ ("and/or I will offer it up") is the hinge of the conjunctive-vs-disjunctive reading debate.

Default LXX equivalents of MT waw are conjunctive or mildly adversative Greek particles, not disjunctive ones:

1. **καί** — the overwhelming default rendering of וְ in all clause types; a straight conjunctive-sequential equivalent.
2. **δέ** — "and / but / now"; mildly adversative or scene-shifting, used especially where the waw heads a disjunctive-circumstantial clause (waw + non-verb).
3. **οὖν** — "therefore, so"; rare, used where the Hebrew waw carries an inferential nuance.
4. **ἤ** ("or") — rare and marked; used where the translator judged the Hebrew waw to express an exclusive alternative rather than coordination.
5. **εἰ μή** ("unless") — not a waw-rendering in standard usage; it renders כִּי אִם or אִם־לֹא constructions, not bare waw.

**Key finding for Jdg 11:31:** Neither the A-text nor the B-text of LXX Judges renders the contested waw with ἤ or εἰ μή. The two recensions diverge — the A-text uses conjunctive **καί**, while the B-text drops the conjunction altogether (**asyndeton**) — but neither takes the disjunctive route. The ancient Greek translators, whether Old Greek or kaige-revised, read the waw as coordinating, not alternating.

## Form Recognition

- **καί** as waw-equivalent: `CONJ` tag in morphological parsers; clause-initial; overwhelming frequency in LXX narrative prose.
- **δέ** as waw-equivalent: `PRT` / `CONJ` postpositive; typically at clause-second position; often pairs with μέν earlier in the context.
- **ἤ** as disjunctive: `CONJ` disjunctive; marked; Wallace (*Basics of NT Syntax* p.300) classifies it as the primary Greek disjunctive ("or"), giving an alternative possibility.
- **asyndeton** (no conjunction) in LXX narrative is itself a marked rendering — it typically signals either (a) a literal reflex of zero-conjunction in an exemplar, (b) a paratactic flourish where the translator wanted to juxtapose clauses without grammatical subordination, or (c) in Judges-B, a kaige-Theodotionic leveling. Asyndeton is *not* equivalent to ἤ; it leaves the clause relation open rather than marking it as disjunctive.

## Functions with Examples

### 1. Default: καί for Hebrew וְ (overwhelming majority)

LXX translators routinely render waw-consecutive and simple waw with καί even in weqatal apodoses of conditional/votive statements. This is a hallmark of the kaige and Old Greek translation technique for the historical books.

| Reference | Hebrew | LXX (A-text) | Relation |
|-----------|--------|--------------|----------|
| Gen 28:21 (Jacob's vow apodosis) | וְהָיָה יְהוָה לִי לֵאלֹהִים | καὶ ἔσται μοι κύριος εἰς θεόν | καί = וְ |
| Num 21:2 (Israel's vow apodosis) | וְהַחֲרַמְתִּי אֶת־עָרֵיהֶם | καὶ ἀναθεματιῶ αὐτὴν καὶ τὰς πόλεις αὐτῆς | καί = וְ (Hiphil weqatal) |
| 1 Sam 1:11 (Hannah's vow apodosis) | וּנְתַתִּיו לַיהוָה | καὶ δώσω αὐτὸν ἐνώπιόν σου δοτὸν | καί = וְ (Qal weqatal) |

In every parallel vow-apodosis where MT reads weqatal + waw, the LXX reads καί. This is the baseline against which Judges 11:31 must be read.

### 2. The crux: Judges 11:31

The Hebrew apodosis chain is:
> וְהָיָה לַיהוָה **וְ**הַעֲלִיתִיהוּ עֹלָה

The two extant recensions of LXX Judges render this chain differently — neither with a disjunctive particle.

#### A-text (Codex Alexandrinus; Rahlfs' main text; reflects later / fuller tradition)

> καὶ ἔσται τῷ κυρίῳ **καὶ** ἀνοίσω αὐτὸν ὁλοκαύτωμα
>
> "and it shall be to the LORD, **and** I will offer him up [as] a whole-burnt-offering"

- The contested waw is rendered **καί** — the default conjunctive coordinator.
- This mirrors the preceding וְהָיָה לַיהוָה → καὶ ἔσται τῷ κυρίῳ, treating the two clauses as parallel links in a single apodosis chain.
- **Exegetical force:** the A-text translator read the Hebrew as *and*, not *or*.

#### B-text (Codex Vaticanus; Swete's LXX; widely held to reflect kaige-revised Judges)

> καὶ ἔσται τῷ κυρίῳ· **ἀνοίσω** αὐτὸν ὁλοκαύτωμα
>
> "and it shall be to the LORD; I will offer him up [as] a whole-burnt-offering"

- The contested waw is rendered by **asyndeton** — no conjunction at all, a bare paratactic juxtaposition (often marked editorially with a high stop or colon).
- This is an unusual rendering; the expected default would be καί. The translator dropped the conjunction rather than pick one.
- **Exegetical force:** the B-text translator left the clause-relation open — neither explicitly coordinate nor explicitly disjunctive. Brenton's English rendering of the B-text ("he shall be the Lord's: I will offer him up") captures this neutrality with a colon.

#### What neither text does

Neither recension uses **ἤ** ("or"), and neither uses **εἰ μή** ("unless"). If the disjunctive reading ("dedicate OR sacrifice") had been the dominant ancient Jewish understanding, ἤ was the obvious Greek particle and was readily available — it appears elsewhere in LXX for Hebrew אוֹ (e.g., Exo 21:16 LXX: ὃς ἐὰν κλέψῃ τις υἱὸν Ἰσραηλ … ἢ εὑρεθῇ ἐν αὐτῷ; Lev 5:1–4 etc.). Its **absence** from Jdg 11:31 in both recensions is substantive.

### 3. Related: LXX uses of ἤ for Hebrew אוֹ (the dedicated "or" particle)

These examples show that the LXX translators *did* use ἤ where Hebrew had an unambiguous disjunctive particle — making its absence at Jdg 11:31 even more noticeable.

| Reference | Hebrew | LXX | Function |
|-----------|--------|-----|----------|
| Exo 21:16 | אִישׁ … וְנִמְצָא | ἢ εὑρεθῇ | ἤ rendering waw where context forces "or" (casuistic law) |
| Exo 21:20 | בְּשֵׁבֶט … אוֹ אֶת־אֲמָתוֹ | ἢ τὴν παιδίσκην αὐτοῦ | ἤ for אוֹ (true disjunction) |
| Lev 5:1 | אוֹ רָאָה אוֹ יָדָע | ἢ ἑώρακεν ἢ σύνοιδεν | ἤ …ἤ for אוֹ … אוֹ (paired alternatives) |

The LXX translators had ἤ in their toolbox and used it freely for disjunction. They did not reach for it at Jdg 11:31.

## The Josephus Parallel (Ant. 5.7.10)

Josephus paraphrases Jephthah's vow in *Antiquities* 5.7.10 (Whiston's English, reflecting the lost Greek of Josephus' own re-telling):

> "he had vowed to perform sacred offices; and **if he came home in safety, to offer in sacrifice what living creature soever should first meet him**."

- Josephus does **not** reproduce the vow's clause structure. He paraphrases the referent of הַיּוֹצֵא as "what living creature soever" (ὅ τι ἂν ζῷον … or equivalent in Josephus' Greek), and collapses the two-weqatal apodosis into a single infinitive of purpose ("to offer in sacrifice").
- His "what living creature soever" is **generic / universal**, not strictly disjunctive — it reads the vow as covering any animal that happens to come out first. This is not the same as reading the waw as "or" (dedication vs. sacrifice); rather, it takes the sacrificial outcome as the single apodosis and widens the subject-class.
- Josephus goes on to say that Jephthah did sacrifice his daughter, and that the act "was neither conformable to the law, nor acceptable to God." He reads the vow as univocally sacrificial — consistent with the καί / asyndeton of LXX, not with a disjunctive waw.
- **Value as evidence:** Josephus (1st-cent Judaism, writing for a Greco-Roman audience) did not know the disjunctive reading of Jdg 11:31 — or, if he did, he rejected it. His generalizing "what living creature soever" shows that the *class of referent* was a point of translational interest, but the *grammatical relation* between the two apodosis clauses was not.

## Contrast with Related Forms

| Greek particle | Function | Typical Hebrew source | Used at Jdg 11:31? |
|----------------|----------|------------------------|---------------------|
| καί | and (conjunctive) | וְ (default) | Yes — A-text |
| δέ | and / but (mild adversative) | וְ in scene-shift / circumstantial | No |
| οὖν | therefore, so (inferential) | לָכֵן, rare waw | No |
| ἤ | or (true disjunction) | אוֹ | **No — in neither recension** |
| εἰ μή | unless, except | כִּי אִם / אִם־לֹא | **No** |
| (asyndeton) | bare juxtaposition | — | Yes — B-text |

## Subtypes / Recension Notes

| Recension | Jdg 11:31 conjunction | Textual character |
|-----------|------------------------|---------------------|
| A-text (Codex Alexandrinus; Rahlfs main) | **καί** | Closer to Old Greek in Judges; fuller, more expansive text |
| B-text (Codex Vaticanus; Swete; Brenton base) | **asyndeton** (no conjunction) | Kaige-Theodotionic revision in Judges; more literal; often preserves unusual syntax |
| Lucianic (AII / glnw group) | (not surveyed here; Rahlfs apparatus required) | Sometimes preserves older OG against both A and B |

The **significance** is that neither of the two main ancient Greek renderings of Judges — the A-text (representing something closer to Old Greek) and the B-text (representing the kaige revision) — took the disjunctive route. Both treat the two-weqatal apodosis as a single connected promise, whether explicitly (καί) or by paratactic juxtaposition (asyndeton). The absence of ἤ in both is powerful negative evidence against the claim that ancient Jewish translators considered "dedicate OR sacrifice" an admissible reading of Jdg 11:31.

## Exegetical Bearing on Jdg 11:31

Putting the LXX evidence alongside the Hebrew grammar ([hebrew/syntax-waw-conjunction.md](../hebrew/syntax-waw-conjunction.md), [hebrew/weqatal-apodosis-vow.md](../hebrew/weqatal-apodosis-vow.md)):

1. **Hebrew grammar** allows the disjunctive ("or") reading of וְ as a *marked* option, especially in casuistic-enumerative contexts; it does not force it, and the default in a weqatal apodosis chain is conjunctive.
2. **LXX A-text** reads it conjunctively (καί) — a direct vote for "and".
3. **LXX B-text** reads it asyndetically — a vote for "neither explicitly and nor explicitly or"; leaves the question open but does not endorse disjunction.
4. **Josephus** paraphrases the vow as univocally sacrificial, widening the subject-class but not splitting the predicate.
5. **Neither Greek recension** uses ἤ or εἰ μή, although both particles were available and used elsewhere in LXX for genuine disjunction.

The combined Greek-witness evidence therefore **supports the conjunctive ("and offer it up") reading** of the Hebrew and **does not support** the disjunctive ("dedicate or offer it up") reading. The disjunctive interpretation is a later, derived exegetical move — driven by theological considerations (prohibition of human sacrifice; parallels with Hannah's dedication in 1 Sam 1) — not by the ancient translation tradition.

## Reference Grammars / Tools Consulted

- Wallace, *Basics of NT Syntax*, p.300 — disjunctive (alternative) conjunctions; ἤ as primary disjunctive.
- BDF (Blass–Debrunner–Funk), §§299–300, 442 — ἤ in questions and alternatives; καί in Semitic-style parataxis.
- Swete, *The Old Testament in Greek according to the Septuagint* — B-text of Judges with variant apparatus.
- Rahlfs-Hanhart, *Septuaginta* — prints Judges as a double text (A and B) on the same page.
- Josephus, *Antiquities* V.vii.10 (Whiston §§263–266) — paraphrase of Jephthah's vow.
- `semantic_grammar.py "Hebrew waw translation" --greek` and `"disjunctive conjunction"` — textbook citations.

## Cross-References

- [hebrew/syntax-waw-conjunction.md](../hebrew/syntax-waw-conjunction.md) — Hebrew waw polyfunctionality
- [hebrew/weqatal-apodosis-vow.md](../hebrew/weqatal-apodosis-vow.md) — weqatal chain in vow apodoses
- [hebrew/syntax-conditional-vow.md](../hebrew/syntax-conditional-vow.md) — vow syntactic template
- [passages/jdg-11-30-31.md](../passages/jdg-11-30-31.md) — full grammar analysis of Jephthah's vow

---
*Generated from: Swete (biblehub.com/sepd), Blue Letter Bible LXX (A-text / Rahlfs), Perseus/Penelope Josephus Ant. 5.7.10 (Whiston), `semantic_grammar.py`.*
*Last updated: 2026-04-17*
