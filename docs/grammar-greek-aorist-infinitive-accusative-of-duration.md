# Aorist Infinitive with Accusative of Duration (Greek)

## Definition

A construction in which an aorist infinitive (usually of an activity or stative verb)
takes an accusative substantive denoting a span of time. The accusative answers the
question "how long?" (Wallace, *Basics of NT Syntax* pp. 75, 92–93; BDF §161), and
the aorist infinitive packages the whole span as a single bounded event viewed
externally. The most frequent lexical instance in the NT is **ποιέω + acc. of time**
used idiomatically for "spend/stay/continue [for a duration]" (BDAG ποιέω §4.2).

1. **Accusative of extent of time** — the noun in the accusative specifies the
   duration over which the verbal action holds (Wallace 201–203; Machen §382;
   BDF §161).
2. **ποιέω + acc. of time idiom** — "to spend, stay, continue (for) [time]";
   the verb loses its normal "do/make" sense and functions as a
   stay/duration verb (BDAG §4.2).
3. **Aorist-aspect bounded span** — the aorist (perfective) aspect + explicit
   temporal accusative presents the entire span as a closed whole seen
   from outside, not an unfolding process. Pairs naturally with finite aorists
   of granting, deciding, traveling, etc.

## Form Recognition

- **Infinitive morphology:** 1st aor. act. inf. `-σαι` (ποιῆ**σαι**, πιστεῦ**σαι**);
  2nd aor. act. inf. `-εῖν` (λιπ**εῖν**); aor. mid. `-σασθαι`; aor. pass. `-θῆναι`.
- **Accusative time-word:** μῆνας, ἡμέρας, ἔτη, ἐνιαυτόν, χρόνον, νυχθήμερον,
  ὥραν — usually adjacent to the verb, often without preposition.
- **Parser search:** `tense=aorist mood=infinitive` for the infinitive;
  `case=accusative` on time-nouns (μήν, ἡμέρα, ἔτος, χρόνος, ἐνιαυτός).
- **Morph code pattern:** `V-AAN` (aor. act. inf.) + `N-ASM/APM` on a time-word.
- **No preposition required.** Greek expresses duration by the bare accusative;
  contrast ἐν + dative ("at/during a point"), genitive ("kind of time"), or
  ἐπί/διά + gen. (also duration, but marked).

## Functions with Examples

### 1. ποιέω + acc. of time = "spend/stay/continue" (BDAG §4.2)

The dominant NT use of this idiom. The aorist/perfect forms of ποιέω with
an accusative duration denote **completed residence or continuance** over the
named span; the aorist participle with χρόνον is a near-formulaic travel marker
in Luke-Acts.

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Acts 15:33 | ποιήσαντες … χρόνον | V-AAP-NPM + N-ASM | "after they had tarried [there] a space" |
| Acts 18:23 | ποιήσας χρόνον τινά | V-AAP-NSM + N-ASM | "after he had spent some time" |
| Acts 20:3 | ποιήσας … μῆνας τρεῖς | V-AAP-NSM + N-APM | "[there] abode three months" |
| 2 Cor 11:25 | νυχθήμερον … πεποίηκα | N-ASN + V-RAI-1S | "a night and a day I have been [in the deep]" |
| Jas 4:13 | ποιήσομεν ἐκεῖ ἐνιαυτόν | V-FAI-1P + N-ASM | "continue there a year" |

Notes:
- The aorist **participle** (ποιήσας / ποιήσαντες) in Luke-Acts travel summaries
  functions as a backgrounded bounded-span event: "having spent X time,
  [main verb]."
- 2 Cor 11:25 uses the **perfect** (πεποίηκα) with an accusative of duration
  (νυχθήμερον, "a day-and-night"): stative-resultative force on the same idiom.
- Jas 4:13 shows the **future indicative** of the same idiom (ποιήσομεν …
  ἐνιαυτόν), confirming that the construction is not tense-bound: the
  accusative-of-duration pattern rides on the verb regardless of tense.

### 2. Aorist infinitive of ποιέω + acc. of duration as a bounded-span complement

When the same idiom is embedded under a finite verb (esp. ἐδόθη, "was given"),
the aorist infinitive + accusative of duration encodes a **finite, pre-delimited
grant** of the action. The aorist aspect views the whole span externally — the
span is set; no iterative, conative, or open-ended reading is suggested by the
morphology itself.

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Rev 13:5 | ἐδόθη … ἐξουσία ποιῆσαι μῆνας τεσσεράκοντα [καὶ] δύο | V-API-3S … V-AAN + N-APM | "power was given unto him to continue forty [and] two months" |

Parsing of Rev 13:5: ἐδόθη (V-API-3S, aor. pass. ind.) αὐτῷ (dat.) ἐξουσία
(nom. subject) ποιῆσαι (V-AAN, aor. act. inf., complement of ἐξουσία) μῆνας
τεσσεράκοντα δύο (N-APM + numerals, acc. of extent of time).

Semantic structure:
- **Finite verb** (ἐδόθη, aorist passive): a single completed act of granting.
- **Infinitive** (ποιῆσαι, aorist active): the content of the grant, perfective.
- **Accusative of duration** (μῆνας … δύο): the bounded span over which the
  granted action holds.

The KJV renders ποιῆσαι as "to continue," taking the ποιέω + acc.-of-time idiom
(§1 above). Under that reading the sense is "authority … to continue [acting /
to hold sway] for forty-two months."

**Alternative parsing.** If πόλεμον ("war") is supplied from the neighboring
v. 7 (καὶ ἐδόθη αὐτῷ ποιῆσαι πόλεμον, "to make war" — same verb + acc. object,
no time-word), ποιῆσαι in v. 5 can be read as "to make (war) for forty-two
months," making μῆνας τεσσεράκοντα δύο an accusative of duration modifying the
action of war-making rather than the idiom. This requires ellipsis of the
object, but is grammatically possible. Either way the accusative μῆνας … δύο
is an **accusative of extent of time** under Wallace's category, and the aorist
infinitive presents the action as a bounded perfective whole.

### 3. Non-ποιέω examples of the broader pattern (acc. of duration)

The accusative-of-duration construction is not limited to ποιέω; the same
case-function operates with any verb taking an explicit time-span, including
aorist infinitives of other verbs (Wallace 201; BDF §161).

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Matt 20:6 | τί ὧδε ἑστήκατε … ὅλην τὴν ἡμέραν | A-ASF + N-ASF | "Why stand ye here all the day…?" |
| Mark 1:13 | ἦν ἐν τῇ ἐρήμῳ τεσσεράκοντα ἡμέρας | A-APF + N-APF | "he was in the wilderness forty days" |
| John 11:6 | ἔμεινεν … δύο ἡμέρας | A-APF + N-APF | "he abode two days" |

These show the bare accusative time-span without preposition — the standard
Greek marker for extent of time.

## Contrast with Related Case-Uses of Time

| Form | Temporal Question | Nuance | Example |
|------|-------------------|--------|---------|
| **Accusative of time** | "How long?" | extent / duration | Rev 13:5 μῆνας … δύο |
| Dative of time | "When?" (point) | position in time | Matt 17:23 τῇ τρίτῃ ἡμέρᾳ |
| Genitive of time | "During what kind of time?" | kind / within | John 3:2 ἦλθεν … νυκτός |
| ἐν + dative | "at / in" | location in time | Matt 2:1 ἐν ἡμέραις Ἡρῴδου |
| ἐπί / διά + gen. | "for / throughout" | marked duration | Acts 19:10 ἐπὶ ἔτη δύο |

See Wallace *Basics of NT Syntax* pp. 75, 92–93; BDF §§161, 201; Machen §382.

## Contrast with Related Infinitive Uses

| Form | Function | Example |
|------|----------|---------|
| Aorist infinitive + acc. of duration | bounded perfective span | Rev 13:5 ποιῆσαι μῆνας … δύο |
| Aorist infinitive of purpose | goal of main verb | Matt 5:17 ἦλθον … καταλῦσαι |
| Present infinitive + acc. of duration | ongoing/iterative span | (rarer; stresses process within span) |
| Articular infinitive (τοῦ + inf.) | purpose / epexegetical | Acts 20:3 γνώμης τοῦ ὑποστρέφειν |
| Infinitive as complement of ἐξουσία / δύναμις | content of granted capacity | Rev 13:5, 7; John 1:12 ἐξουσίαν … γενέσθαι |

## Aspect Note

The aorist infinitive + accusative of duration is not a contradiction. Greek
aspect (perfective) describes how the speaker presents the action, not its
real-world internal time. An accusative of duration states *how long* the
action extends; the aorist presents that whole extended state or activity as
a **single closed whole viewed from outside**. Compare Mark 1:13 (imperfect
ἦν + τεσσεράκοντα ἡμέρας — internal view) vs. Rev 13:5 (aor. inf. ποιῆσαι +
μῆνας … δύο — external, bounded view). Both are grammatical; the aspect
choice is rhetorical.

---
*Generated from: greek_parser.py (--verse), semantic_grammar.py ("accusative of
time extent of time", "infinitive of purpose aorist"), Wallace BNTS pp. 75,
92–93, 201–203; BDF §§161, 201; Machen §382; BDAG ποιέω §4.2.*
*Last updated: 2026-04-17*
