# Grammar Analysis: Ezekiel 28 Construct-Chain Cluster

**Scope.** Passage grammar for the construct chains clustered in Ezekiel 28: "garden of God," "holy mountain of God," "stones of fire," "seat of God," and "heart of God." This entry documents the nominal syntax, not the theological referents.

## Construct Chains

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Eze 28:2 | מֹושַׁב אֱלֹהִים | `מֹושַׁב` Noun.ms.Cst + `אֱלֹהִים` Noun.mp.Abs | "seat of God" |
| Eze 28:2 | לֵב יַמִּים | `לֵב` Noun.ms.Cst + `יַמִּים` Noun.mp.Abs | "midst/heart of the seas" |
| Eze 28:2 | לֵב אֱלֹהִים | `לֵב` Noun.ms.Cst + `אֱלֹהִים` Noun.mp.Abs | "heart of God" |
| Eze 28:13 | גַּן־אֱלֹהִים | `גַּן` Noun.s.Cst + `אֱלֹהִים` Noun.mp.Abs | "garden of God" |
| Eze 28:14 | הַר קֹדֶשׁ אֱלֹהִים | `הַר` Noun.ms.Cst + `קֹדֶשׁ` Noun.ms.Abs + `אֱלֹהִים` Noun.mp.Abs | "holy mountain of God" |
| Eze 28:14 | אַבְנֵי־אֵשׁ | `אַבְנֵי` Noun.fp.Cst + `אֵשׁ` Noun.s.Abs | "stones of fire" |
| Eze 28:16 | הַר אֱלֹהִים | `הַר` Noun.ms.Cst + `אֱלֹהִים` Noun.mp.Abs | "mountain of God" |
| Eze 28:16 | אַבְנֵי־אֵשׁ | `אַבְנֵי` Noun.fp.Cst + `אֵשׁ` Noun.s.Abs | "stones of fire" |

## Key Grammatical Features

### 1. Repeated `X of God` Chains

The chains `מֹושַׁב אֱלֹהִים`, `לֵב אֱלֹהִים`, `גַּן־אֱלֹהִים`, `הַר ... אֱלֹהִים`, and `הַר אֱלֹהִים` all use construct syntax. The first noun is the bound head; `אֱלֹהִים` is the absolute noun that supplies the genitive relation.

Grammar reference: [construct-state](../hebrew/construct-state.md).

### 2. Multi-Word Chain: `har qodesh elohim`

Ezek 28:14 has a three-member chain: `הַר` + `קֹדֶשׁ` + `אֱלֹהִים`. The parser reports `הַר` as construct and `קֹדֶשׁ`/`אֱלֹהִים` as absolute forms within the phrase. Semantically, English must smooth this as "holy mountain of God," but the Hebrew structure compresses holiness and divine possession/association into one nominal cluster.

### 3. Repeated Locative Removal

The chains from v.14 recur in v.16 under removal prepositions:

| Location in v.14 | Removal in v.16 |
|------------------|-----------------|
| `בְּהַר קֹדֶשׁ אֱלֹהִים` - on/in holy mountain of God | `מֵהַר אֱלֹהִים` - from mountain of God |
| `בְּתֹוךְ אַבְנֵי־אֵשׁ` - in midst of stones of fire | `מִתֹּוךְ אַבְנֵי־אֵשׁ` - from midst of stones of fire |

The repeated heads and complements create a grammatical reversal: location/status in v.14 becomes removal in v.16.

### 4. `Heart` Chains Contrast Human Claim and Divine Comparison

Ezek 28:2 uses `לֵב יַמִּים` ("heart of seas") for claimed enthronement location and `לֵב אֱלֹהִים` ("heart of God") for claimed internal status/comparison. Both are ordinary construct chains; the grammar records the claim language without adjudicating the claim.

## Cross-References

- [construct-state](../hebrew/construct-state.md)
- [construct-chain-suffix](../hebrew/construct-chain-suffix.md)
- [isa-14-ezek-28-self-deification](isa-14-ezek-28-self-deification.md)
- [ezk-28-1-19-prince-king-structure](ezk-28-1-19-prince-king-structure.md)
- [ezk-28-13-15-niphal-creation-found-sequence](ezk-28-13-15-niphal-creation-found-sequence.md)

---
*Generated from: hebrew_parser.py --verse/--construct Eze 28:2,13,14,16; KJV corpus lookup.*
*Last updated: 2026-05-07*
