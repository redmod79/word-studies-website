# Aorist Imperative (Greek)

## Definition

The aorist imperative commands an action viewed as a whole, complete event rather than an ongoing process. It calls for a specific, decisive act without reference to duration or repetition, in contrast to the present imperative which commands continuous or repeated action.

1. **Specific/decisive command** -- calls for a definite, punctiliar act
2. **Urgent/ingressive command** -- demands immediate action, often in a crisis
3. **Third-person petition** -- "let X be/happen" (prayer, wish, or indirect command)

## Form Recognition

- Aorist stem (typically with sigma augment in first aorist: -σατε, -σον; or second aorist stem change)
- Imperative mood endings (-ον, -ατε, -άτω for active; -θητε, -θήτω for passive; -σαι, -σασθε for middle)
- **Parser search:** `mood=imperative tense=aorist`
- **Morph code patterns:** `V-AAM-2P` (active), `V-APM-2P` (passive), `V-AMM-2P` (middle), `V-2AAM-2S` (second aorist active)

## Functions with Examples

### 1. Specific/Decisive Command

Commands a single, complete action to be carried out as a definite act.

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Rev 14:7 | Φοβήθητε | V-AOM-2P | "Fear God" |
| Rev 14:7 | δότε | V-2AAM-2P | "give glory to him" |
| Rev 14:7 | προσκυνήσατε | V-AAM-2P | "worship him" |
| Eph 6:11 | ἐνδύσασθε | V-AMM-2P | "Put on the whole armour" |
| 1 Cor 5:7 | ἐκκαθάρατε | V-AAM-2P | "Purge out therefore the old leaven" |
| 1 Cor 6:20 | δοξάσατε | V-AAM-2P | "glorify God in your body" |
| Rom 6:13 | παραστήσατε | V-AAM-2P | "yield yourselves unto God" |

### 2. Urgent/Ingressive Command

Demands immediate action, often at a turning point or in response to a crisis.

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Acts 2:38 | Μετανοήσατε | V-AAM-2P | "Repent" |
| Acts 2:40 | Σώθητε | V-APM-2P | "Save yourselves" |
| Jas 4:7 | ὑποτάγητε | V-2APM-2P | "Submit yourselves therefore to God" |
| Jas 4:7 | ἀντίστητε | V-2AAM-2P | "Resist the devil" |
| Jas 4:8 | ἐγγίσατε | V-AAM-2P | "Draw nigh to God" |
| Rev 2:5 | μετανόησον | V-AAM-2S | "repent, and do the first works" |
| Matt 3:8 | ποιήσατε | V-AAM-2P | "Bring forth therefore fruits" |

### 3. Third-Person Petition/Wish

Uses third-person endings (-τω, -τωσαν) to express "let it be so" in prayer, wishes, or indirect commands.

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Matt 6:9 | Ἁγιασθήτω | V-APM-3S | "Hallowed be thy name" |
| Matt 6:10 | ἐλθάτω | V-2AAM-3S | "Thy kingdom come" |
| Matt 6:10 | γενηθήτω | V-AOM-3S | "Thy will be done" |
| Matt 5:16 | λαμψάτω | V-AAM-3S | "Let your light so shine" |
| Acts 2:38 | βαπτισθήτω | V-APM-3S | "be baptized every one of you" |

## Contrast with Present Imperative

| Feature | Aorist Imperative | Present Imperative |
|---------|-------------------|--------------------|
| **Aspect** | Action as a whole/complete event | Ongoing, repeated, or continuous action |
| **Force** | "Do this (now/once/decisively)" | "Keep doing this" or "make this your practice" |
| **Parser code** | `V-AAM`, `V-APM`, `V-AMM` | `V-PAM`, `V-PNM` |

**Illustrative contrast:**

| Aorist | Present | Significance |
|--------|---------|-------------|
| Μετανοήσατε (Acts 2:38) -- "Repent" (decisive turning) | Μετανοεῖτε (Matt 4:17) -- "Repent" (ongoing call) | Aorist: one decisive break; present: continuous lifestyle |
| πρόσευξαι (Matt 6:6) -- "pray" (specific act) | προσεύχεσθε (Matt 6:9) -- "pray ye" (habitual practice) | Aorist: this particular prayer; present: regular practice |
| ποιήσατε (Matt 3:8) -- "bring forth fruit" (decisive act) | ποιεῖτε (Matt 7:12) -- "do unto others" (ongoing principle) | Aorist: produce it now; present: keep doing it always |

## Notes on Usage

- The aorist imperative does not inherently mean "do it immediately" -- urgency comes from context, not the tense alone. The aorist views the action as a single whole, which in imperative mood naturally suits decisive commands.
- When multiple aorist imperatives appear in sequence (as in Rev 14:7 or Jas 4:7-8), the effect is a rapid series of distinct demands, each calling for a specific response.
- The aorist passive imperative (Φοβήθητε, ὑποτάγητε, Σώθητε) is common for deponent or semi-deponent verbs and does not always carry passive meaning.

---
*Generated from: greek_parser.py (--search, --verse)*
*Last updated: 2026-04-13*
