# Construct Chain as Destination Complement (Hebrew)

## Definition

A Hebrew construct chain may stand as the object of a directional preposition, forming a single destination complement. The preposition governs the whole chain, not only the first noun; the construct head and absolute noun together name the destination.

1. **Preposition + construct chain** - אֶל, לְ, עַד, or בְ may govern a complete construct phrase.
2. **Destination complement** - the phrase answers "to where?" or "into what location?"
3. **Chain-level semantics** - the final absolute noun specifies the kind, owner, quality, or class of the head noun.

## Form Recognition

- Directional or locative preposition before a construct head.
- First noun parsed `Noun.*.Cst`; following noun parsed `Noun.*.Abs`.
- Clause parser often tags the whole prepositional phrase as `[Cmpl]`.
- **Parser search:** `sp=subs st=c` to locate construct heads; then check verse/clause context.
- **Construct parser:** `hebrew_parser.py --construct <ref>`.

## Functions with Examples

### 1. אֶל + Construct Chain as Goal

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Lev 16:22 | אֶל־אֶרֶץ גְּזֵרָה | Prep + Noun.s.Cst + Noun.fs.Abs | "unto a land not inhabited" |
| Gen 2:11 | אֶרֶץ הַחֲוִילָה | Noun.s.Cst + Art + proper/location noun | "the land of Havilah" |
| Gen 2:13 | אֶרֶץ כּוּשׁ | Noun.s.Cst + proper/location noun | "the land of Ethiopia" |

In Lev 16:22, אֶל governs the full construct phrase אֶרֶץ גְּזֵרָה. The destination is not merely "land" in abstraction but the land qualified by גְּזֵרָה.

### 2. Locative Complement with Construct Chain

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Lev 16:21 | בְּיַד־אִישׁ עִתִּי | Prep + Noun.s.Cst + Noun.ms.Abs + Adj.ms.Abs | "by the hand of a fit man" |
| Lev 16:21 | עַל רֹאשׁ הַשָּׂעִיר | Prep + Noun.ms.Cst + Art + Noun.ms.Abs | "upon the head of the goat" |
| Lev 16:22 | בַּמִּדְבָּר | Prep + Art + Noun.ms.Abs | "in the wilderness" |

These examples show the contrast between a preposition governing a construct chain and a preposition governing a simple absolute noun.

## Contrast with Related Forms

| Form | Function | Example |
|------|----------|---------|
| Preposition + construct chain | destination/location phrase headed by full chain | Lev 16:22 אֶל־אֶרֶץ גְּזֵרָה |
| Bare construct chain | nominal relation without preposition | Lev 16:21 רֹאשׁ הַשָּׂעִיר |
| Preposition + absolute noun | simple location/destination, no internal genitive relation | Lev 16:22 בַּמִּדְבָּר |
| Directional heh | locative/directional suffix, often "toward" | Lev 16:21 הַמִּדְבָּרָה |

## Lev 16:22 Parser-Verified Form

| Word | Lemma | Parsing | Gloss |
|------|-------|---------|-------|
| אֶל | אל | Prep | to |
| אֶרֶץ | ארץ | Noun.s.Cst | earth/land |
| גְּזֵרָה | גזרה | Noun.fs.Abs | dry land / cut-off place |

Clause parser tags the phrase as `[Cmpl] אֶל אֶרֶץ גְּזֵרָה`, a destination complement of וְנָשָׂא. The grammar establishes the phrase as a goal/destination complement; it does not decide theological symbolism.

---
*Generated from: hebrew_parser.py (--verse, --construct, --clause, --lemma)*
*Last updated: 2026-05-07*
