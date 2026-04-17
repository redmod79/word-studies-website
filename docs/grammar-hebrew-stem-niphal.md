# Niphal Stem (Hebrew)

## Definition
The Niphal (נִפְעַל) is the N-stem in Hebrew, formed by prefixing נ (nun) to the root. It primarily expresses:

1. **Simple passive** — the subject receives the action
2. **Reflexive** — the subject acts on itself
3. **Tolerative/middle** — the subject allows or submits to an action

## Form Recognition
- **Perfect:** נִ prefix — נִקְטַל (niqtal), e.g., נִצְדַּק (Dan 8:14), נִשְׁחָתָה (Gen 6:12)
- **Imperfect:** Dagesh in first root letter — יִקָּטֵל (yiqqatel), e.g., יִכָּרֵת (Gen 9:11)
- **Participle:** נִ prefix — נִקְטָל, e.g., נִרְאֶה (Gen 12:7)
- **Imperative:** הִ prefix — הִקָּטֵל, e.g., הִפָּרֶד (Gen 13:9)
- **Infinitive Construct:** הִ prefix — הִקָּטֵל, e.g., הִבָּרְאָם (Gen 2:4)
- **Parser code:** `sp=verb vs=nif`

## Tense Distribution (from 500 occurrences sampled)

| Tense | Count | % |
|-------|-------|---|
| Imperfect | 174 | 35% |
| Perfect | 143 | 29% |
| Participle | 66 | 13% |
| Wayyiqtol | 64 | 13% |
| Infinitive Construct | 27 | 5% |
| Imperative | 21 | 4% |
| Infinitive Absolute | 5 | 1% |

## Functions with Examples

### 1. Simple Passive (most common)
The subject receives the action performed by an external agent.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Gen 1:9 | יִקָּווּ | Niphal.Impf.3mp of קוה | "Let the waters be gathered together" |
| Gen 9:11 | יִכָּרֵת | Niphal.Impf.3ms of כרת | "neither shall all flesh be cut off" |
| Gen 7:23 | יִּמָּחוּ | Niphal.Wayq.3mp of מחה | "they were destroyed" (wiped out) |
| Dan 8:14 | נִצְדַּק | Niphal.Perf.3ms of צדק | "shall be cleansed" (lit. vindicated) |

### 2. Reflexive
The subject performs the action on itself.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Gen 3:10 | אֵחָבֵא | Niphal.Wayq.1s of חבא | "I hid myself" |
| 2 Sam 22:24 | אֶשְׁתַּמֵּר | Niphal of שׁמר | "have kept myself from mine iniquity" |
| Gen 13:9 | הִפָּרֶד | Niphal.Impv.2ms of פרד | "separate thyself" |

### 3. Tolerative / Middle
The subject allows or submits to the action — neither fully active nor fully passive.

| Reference | Hebrew | Parsing | KJV |
|-----------|--------|---------|-----|
| Isa 65:1 | נִדְרַשְׁתִּי | Niphal.Perf.1s of דרשׁ | "I am sought of them that asked not" |
| Gen 12:7 | יֵּרָא | Niphal.Wayq.3ms of ראה | "the LORD appeared unto Abram" (allowed himself to be seen) |
| Gen 6:6 | יִּנָּחֶם | Niphal.Wayq.3ms of נחם | "it repented the LORD" (was grieved within himself) |

## Common Niphal Verbs

| Verb | Gloss in Niphal | Occurrences (sampled) |
|------|-----------------|----------------------|
| ראה (ra'ah) | be seen, appear | 38 |
| שׁאר (sha'ar) | remain, be left | 32 |
| אכל (akal) | be eaten | 24 |
| עשׂה (asah) | be made, be done | 23 |
| שׁבע (shaba) | swear (reflexive) | 21 |
| מצא (matsa) | be found | 21 |
| מול (mul) | be circumcised | 17 |
| נצב (natsab) | stand, take one's stand | 14 |
| קבץ (qabats) | be gathered | 12 |
| כרת (karath) | be cut off | 12 |

## Contrast with Other Passive/Reflexive Stems

| Stem | Type | Function | Example |
|------|------|----------|---------|
| **Niphal** | Simple passive/reflexive | Subject receives action or acts on self | נִכְרַת "was cut off" |
| **Pual** | Intensive passive | Subject receives intensified action | כֻּפַּר "was atoned for" |
| **Hophal** | Causative passive | Subject is caused to undergo action | הָשְׁלַךְ "was thrown down" |
| **Hithpael** | Reflexive/iterative | Subject acts on self repeatedly | הִתְהַלֵּךְ "walked about" |

The Niphal is the most common passive stem. Pual and Hophal are rarer and more specialized.

---
*Generated from: hebrew_parser.py --search "sp=verb vs=nif" (500 results sampled), KJV text*
*Last updated: 2026-03-31*
