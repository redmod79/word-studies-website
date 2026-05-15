# Divine Passive / Passivum Divinum / Theological Passive (Greek)

## Definition
The **divine passive** (Latin *passivum divinum*; also "theological passive") is a passive verb whose unexpressed agent is God. Rooted in a Semitic reverential convention — the Jewish aversion to uttering the divine name — it functions as a circumlocution: the passive voice conceals God as the actor while leaving his agency obvious in context. The construction is formally identical to any agent-less passive; the "divine" label is a semantic/pragmatic reading supplied by context, not a distinct morphological category.

1. **Reverent circumlocution** — the passive avoids naming God as subject while clearly implying him (Jewish/Semitic background).
2. **Eschatological/future promise** — future-passive verbs of blessing where God is the implied benefactor (Beatitudes).
3. **Soteriological passives** — Pauline verbs of justification, salvation, and resurrection where God is the unnamed agent.
4. **Apocalyptic permission** — aorist passive ἐδόθη marking actions done or allowed by God's sovereign decree (esp. Revelation).

## Form Recognition
- **Any passive-voice verb with no expressed agent** (no ὑπό/ἀπό/παρά + genitive, no dative of means) **where the context makes God the obvious subject of the action**.
- Most often appears in the aorist passive indicative (V-API-3S / 3P) or future passive indicative (V-FPI-3S / 3P).
- **Parser search:** `voice=passive` combined with context screening (agent-less, God-saturated discourse).
- **Morph code patterns:**
  - `V-API-3S` — aorist passive indicative 3rd singular (e.g., ἐδόθη)
  - `V-FPI-3P` — future passive indicative 3rd plural (e.g., παρακληθήσονται)
  - `V-APP-NPM` — aorist passive participle nom. plur. masc. (e.g., δικαιωθέντες)
- Diagnostic question: "Who is doing this?" If the answer supplied by the discourse is "God" and no agent is stated, treat as a candidate divine passive.

## Functions with Examples

### 1. Beatitude / Promise Passives (Synoptic Tradition)

Future passive with God as implied benefactor. The "Jewish aversion to the divine name" is most visible in Jesus' own speech in Matthew.

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Matt 5:4 | παρακληθήσονται | V-FPI-3P | "they shall be comforted" |
| Matt 5:6 | χορτασθήσονται | V-FPI-3P | "they shall be filled" |
| Matt 5:7 | ἐλεηθήσονται | V-FPI-3P | "they shall obtain mercy" |

Sense: "God will comfort / fill / show mercy to them." The triad of Beatitude passives is Wallace's paradigm example (Basics of NT Syntax, 191).

### 2. Pauline Soteriological Passives

Passive verbs for justification, salvation, and resurrection where God (or "God in Christ") is the unnamed agent. The passive foregrounds the recipient while reserving divine agency for the theological backdrop.

| Reference | Greek | Morph Code | KJV Translation |
|-----------|-------|------------|-----------------|
| Rom 3:28 | δικαιοῦσθαι | V-PPN | "is justified" (pres. pass. inf.) |
| Rom 4:25 | παρεδόθη … ἠγέρθη | V-API-3S … V-API-3S | "was delivered … was raised" |
| Rom 5:9 | δικαιωθέντες … σωθησόμεθα | V-APP-NPM … V-FPI-1P | "being justified … we shall be saved" |

Sense: God justifies, God raised, God will save. The agent is deliberately withheld from the surface but is supplied by Pauline theology.

### 3. Apocalyptic ἐδόθη (Revelation)

Aorist passive of δίδωμι ("it was given / given to him") marks divine permission. In Revelation the construction is a signature feature: hostile powers act only insofar as God has sovereignly granted them scope.

| Reference | Greek | Morph Code | What Is "Given" |
|-----------|-------|------------|-----------------|
| Rev 6:2 | ἐδόθη αὐτῷ στέφανος | V-API-3S | a crown (to the white-horse rider) |
| Rev 6:4 | ἐδόθη αὐτῷ μάχαιρα μεγάλη | V-API-3S | a great sword (to the red-horse rider) |
| Rev 6:8 | ἐδόθη αὐτοῖς ἐξουσία | V-API-3S | authority over a fourth of the earth |
| Rev 9:1 | ἐδόθη αὐτῷ ἡ κλείς | V-API-3S | the key of the pit of the abyss |
| Rev 9:3 | ἐδόθη αὐταῖς ἐξουσία | V-API-3S | power (to the locust-scorpions) |
| Rev 9:5 | ἐδόθη αὐτοῖς ἵνα … | V-API-3S | (that they should not kill but torment) |
| Rev 11:1 | ἐδόθη μοι κάλαμος | V-API-3S | a reed (measuring-rod) to John |
| Rev 13:5 | ἐδόθη αὐτῷ στόμα / ἐξουσία ποιῆσαι μῆνας μβ´ | V-API-3S | a mouth speaking great things; authority to act 42 months |
| Rev 13:7 | ἐδόθη αὐτῷ ποιῆσαι πόλεμον / ἐξουσία | V-API-3S | to make war with the saints; authority over every tribe |
| Rev 13:14 | ἐδόθη αὐτῷ ποιῆσαι | V-API-3S | (signs) to perform before the beast |
| Rev 13:15 | ἐδόθη αὐτῷ δοῦναι πνεῦμα | V-API-3S | to give breath to the image |
| Rev 16:8 | ἐδόθη αὐτῷ καυματίσαι | V-API-3S | to scorch men with fire |
| Rev 19:8 | ἐδόθη αὐτῇ ἵνα περιβάληται | V-API-3S | (the Bride) to be clothed in fine linen |
| Rev 20:4 | κρίμα ἐδόθη αὐτοῖς | V-API-3S | judgment (given to the enthroned) |

The construction is structurally the same across positive and negative recipients: God grants the white rider's crown, the Bride's wedding garment, the beast's 42-month mandate, and the persecuted saints' seat of judgment with identical syntax (ἐδόθη + dative of recipient). Morphologically, every instance listed is aorist passive indicative third singular of δίδωμι (G1325).

## Contrast with Related Forms

| Form | Function | Agent Disclosure | Example |
|------|----------|------------------|---------|
| Divine passive | Passive with God as implied agent | Agent suppressed; recovered from context | Matt 5:4 παρακληθήσονται |
| Passive with ὑπό + gen. | Ordinary passive with explicit agent | Agent named | Matt 3:6 ἐβαπτίζοντο ὑπ' αὐτοῦ |
| Passive with ἀπό / παρά + gen. | Ultimate agent (less common) | Agent named | — |
| Passive with dative of means | Impersonal means / instrument | Agent still unnamed but non-personal | — |
| Middle voice | Subject-affecting action | Subject = agent | Rev 19:7 ἡτοίμασεν ἑαυτήν |
| Active with ὁ Θεός | Direct divine subject | God named explicitly | Rom 8:30 οὓς ἐδικαίωσεν |

Wallace cautions that "divine passive" is a pragmatic label, not a formal one: it is a subtype of the agent-less passive and should not be inflated into a separate grammatical category (Basics, 192; ExSyn 437–438).

## Scholarly References

- **D. B. Wallace**, *Basics of New Testament Syntax* (Zondervan, 2000), 191–192 = *Greek Grammar Beyond the Basics* (ExSyn), 437–438. Defines "divine passive / theological passive" under agent-less passives; uses Matt 5:4, 5:6, 5:7; Rom 3:28; 1 Cor 7:23; Gal 5:13; Eph 2:5 as specimens.
- **BDF** (Blass–Debrunner–Funk), *A Greek Grammar of the New Testament*, §130(1): the passive as a reverential substitute for naming God as subject.
- **J. Jeremias**, *New Testament Theology* I (ET 1971), 9–14: coined/popularized the term *passivum divinum* as a feature of Jesus' ipsissima vox reflecting Semitic reverence for the divine name.

## Subtypes / Pragmatic Categories

| Subtype | Description | Example |
|---------|-------------|---------|
| Reverential | Avoids the divine name for piety | Matt 5:4 παρακληθήσονται |
| Soteriological | Justification / salvation / resurrection verbs | Rom 4:25 ἠγέρθη |
| Permissive-apocalyptic | God grants / allows an act by another agent | Rev 13:5 ἐδόθη … ἐξουσία |
| Consecrating-apocalyptic | God grants a gift or office to a faithful recipient | Rev 19:8 ἐδόθη αὐτῇ |

---
*Generated from: greek_parser.py (--verse), semantic_grammar.py (--greek)*
*Last updated: 2026-04-17*
