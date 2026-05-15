# Plural Noun + Singular Verb Agreement (Hebrew)

## Definition

A widespread Biblical Hebrew concord pattern in which a **morphologically plural noun** (ending in *-îm* / *-ôt* or dual *-ayim*) governs a **grammatically singular** verb, adjective, pronoun, or participle. When this occurs with a plural form that refers to a single referent, the plural is interpreted as a *plural of majesty / honorific / intensity / abstraction* (the "honorific plural"); when the same plural form instead governs **plural** agreement, the noun is interpreted as a genuine numerical plural (multiple referents). The rule is therefore diagnostic: **agreement morphology — not the noun's plural ending — determines whether the referent is singular or multiple.**

1. **Honorific / majestic plural (*pluralis maiestatis*)** — plural form, singular agreement; single referent construed with intensified/exalted status (אֱלֹהִים of YHWH, בְּעָלִים of a single husband, אֲדוֹנִים of a single lord).
2. **Abstract / extensional plural (*pluralis extensivus*)** — plural form, typically singular agreement; single extended referent (מַיִם "water[s]," פָּנִים "face," שָׁמַיִם "heavens," רַחֲמִים "compassion").
3. **True numerical plural** — plural form, plural agreement; multiple referents (אֱלֹהִים of actual multiple gods/judges; אֲדֹנִים of multiple masters).

## Form Recognition

The pattern is visible only in the *combined* morphology of the noun-phrase **and** the word agreeing with it. Steps:

- Check the noun: `Noun.mp.Abs` (masculine-plural absolute) or `Noun.fp.Abs` or `Noun.md/fd` (dual).
- Check the governing verb's person/number: `Verb.<stem>.<tense>.3ms` vs. `Verb.<stem>.<tense>.3p` / `3mp` / `3fp`.
- Check any adjective/pronoun referring to the noun: `Adj.ms.Abs` / `PersPron.3ms` vs. `Adj.mp.Abs` / `PersPron.3mp`.
- Singular agreement → honorific/abstract plural; plural agreement → numerical plural.
- **Parser signatures (hebrew_parser.py):** `sp=subs nu=pl` co-occurring with `sp=verb nu=sg`; contrast with `sp=subs nu=pl` co-occurring with `sp=verb nu=pl`.

## Functions with Examples

### 1. Elohim (H430) + singular agreement (honorific plural, single divine referent)

אֱלֹהִים is morphologically `Noun.mp.Abs` in every one of its ~2,601 occurrences. Agreement overwhelmingly — though not universally — resolves to singular when the referent is Israel's God.

| Reference | Noun | Governing Form | Parsing | Observation |
|-----------|------|----------------|---------|-------------|
| Gen 1:1 | אֱלֹהִים | בָּרָא | Verb.Qal.Perf.**3ms** | "God created" — singular verb with plural noun; canonical example |
| Gen 1:2 | אֱלֹהִים | מְרַחֶפֶת | Verb.Piel.Ptcp.**fs** | Spirit of God "hovering" (fem. sg. participle agreeing with רוּחַ, but clause subject Elohim still construed singular) |
| Gen 1:9 | אֱלֹהִים | יֹּאמֶר | Verb.Qal.Wayq.**3ms** | "And God said" — wayyiqtol 3ms; pattern repeated dozens of times in Gen 1 |
| Gen 1:26 | אֱלֹהִים | יֹּאמֶר / נַעֲשֶׂה | Wayq.**3ms** / Impf.**1p** | Narrator uses 3ms of God; *quoted* divine speech uses 1cp "let us make" — agreement asymmetry within one verse |
| Deu 6:4 | אֱלֹהֵינוּ | אֶחָד | Numeral **ms** | "YHWH our gods (pl.) — one (sg.)" — Shema itself juxtaposes plural noun + singular numeral |
| Psa 58:12 (Eng 11) | אֱלֹהִים | שֹׁפְטִים | Verb.Qal.Ptcp.**mp** | Plural participle "judging / (are) judges" — here agreement is plural, enabling the "God judging in the earth" reading vs. "there are gods judging in the earth"; morphology alone is ambiguous |

### 2. Elohim (H430) + plural agreement (genuine numerical plural or contested honorific)

A small but exegetically load-bearing set of verses pair אֱלֹהִים with a **plural** verb, adjective, or pronoun. In each case context determines whether the plural agreement signals (a) true polytheistic reference, (b) a grammatical lapse/variant where honorific plural took plural agreement anyway, or (c) theological intent.

| Reference | Noun | Governing Form | Parsing | Observation |
|-----------|------|----------------|---------|-------------|
| Gen 20:13 | אֱלֹהִים | הִתְעוּ | Verb.Hiphil.Perf.**3p** | "God caused me to wander" — **plural verb with singular referent** (spoken by Abraham to a pagan king; honorific plural with plural agreement) |
| Gen 31:53 | אֱלֹהֵי אַבְרָהָם וֵאלֹהֵי נָחוֹר | יִשְׁפְּטוּ | Verb.Qal.Impf.**3mp** | Two coordinated *elohê*-phrases followed by plural verb; numerical plural (gods of Abraham + gods of Nahor) |
| Gen 35:7 | הָאֱלֹהִים | נִגְלוּ | Verb.Niphal.Perf.**3p** | "the gods revealed themselves" — plural verb with the article + plural noun; often read as honorific plural-with-plural-concord |
| Exo 22:8 | אֱלֹהִים | יַרְשִׁיעֻן | Verb.Hiphil.Impf.**3mp** | "whom the *elohim* shall condemn" — plural verb; commonly taken as "judges" (numerical plural) |
| Jos 24:19 | אֱלֹהִים | קְדֹשִׁים / הוּא | Adj.**mp** / PersPron.**3ms** | Plural noun + **plural adjective** "holy ones" + **singular** pronoun "he" — both agreements in one clause |
| 2Sa 7:23 | אֱלֹהִים | הָלְכוּ | Verb.Qal.Perf.**3p** | "God went" — plural verb; **directly paralleled by 1Ch 17:21** הָלַךְ Verb.Qal.Perf.**3ms** (same sentence, singular verb in the Chronicles recension — the clearest MT "minimal pair") |
| Isa 54:5 | בֹּעֲלַיִךְ / עֹשַׂיִךְ | plural participles | Ptcp.Qal.**mp** | "your Husband(s) / your Maker(s)" — plural participle forms with singular feminine referent; honorific |
| Ecc 12:1 | בּוֹרְאֶיךָ | — | Ptcp.Qal.**mp** | "remember your Creator(s)" — plural participle with 2ms pronominal suffix; honorific |

### 3. Other morphologically plural nouns showing the same concord alternation

| Noun | Typical agreement | Representative verse | Parsing |
|------|-------------------|----------------------|---------|
| מַיִם "waters" (dual/plural form, always `Noun.mp.Abs`) | **plural** verb normally: Gen 1:9 יִקָּווּ Verb.Niphal.Impf.**3mp**; Gen 7:19 גָּבְרוּ Verb.Qal.Perf.**3p** | Gen 1:9; 7:19 | agreement tracks the *extensive* reading ("the waters gathered / prevailed") |
| פָּנִים "face" (always `Noun.mp`) | **plural** verb: Exo 33:14 פָּנַי יֵלֵכוּ Verb.Qal.Impf.**3mp** ("my face[s] shall go"); but predicate often singular ("his face was …") | Exo 33:14; Gen 1:2 עַל־פְּנֵי (construct chain, no finite verb) | abstract-extensive; agreement varies by clause type |
| שָׁמַיִם "heavens" (dual form) | singular or plural verb | Gen 1:1 object of singular בָּרָא; Psa 19:2 הַשָּׁמַיִם מְסַפְּרִים Ptcp.**mp** | extensive plural |
| אֲדֹנִים "master(s)" | singular verb for honorific of single master; plural verb for multiple masters | Gen 24:9 (honorific of Abraham) vs. Exo 21:4 (multiple owners) | diagnostic test: same form, different referent-count from concord |
| בְּעָלִים "husband / owner(s)" | singular or plural — same diagnostic applies | Isa 54:5 בֹּעֲלַיִךְ ms-suffix referent | — |

## Diagnostic Rule (Context-Neutral)

Because Biblical Hebrew encodes `number` on both nouns and their agreeing words, concord morphology — not lexical form — is the load-bearing signal:

- **Plural noun + singular verb/adjective/pronoun → honorific or abstract plural, single referent.**
- **Plural noun + plural verb/adjective/pronoun → either (a) numerical plural, or (b) honorific plural with attracted plural agreement, resolvable only by context.**

The appeal to the plural *ending* of אֱלֹהִים alone cannot settle referent-plurality; the same noun takes 3ms concord in Gen 1:1 and 3p concord in Gen 20:13 with no change in lexeme. The 2Sa 7:23 ‖ 1Ch 17:21 minimal pair (same utterance, plural vs. singular verb of the same lemma הלך) is the clearest MT demonstration that agreement can vary even for identical referents across recensions.

## Contrast with Related Forms

| Form | Behavior | Example |
|------|----------|---------|
| Plural noun + singular agreement | honorific/extensive plural, single referent | Gen 1:1 אֱלֹהִים … בָּרָא 3ms |
| Plural noun + plural agreement | numerical plural **or** honorific with plural concord | Gen 20:13 אֱלֹהִים … הִתְעוּ 3p |
| 1cp cohortative inside divine speech | speaker-internal plural; independent of concord with a subject-noun | Gen 1:26 נַעֲשֶׂה — linked to [hiphil-imperfect](hiphil-imperfect.md) for stem contrast |
| Singular אֵל (H410) | morphologically sg.; never triggers the honorific-plural diagnostic | Gen 35:7 אֵל בֵּית־אֵל; Jos 24:19 אֵל קַנּוֹא |
| Pronominal copula הוּא / הֵם | singular vs. plural selection re-encodes the concord choice | Jos 24:19 הוּא (sg.) after אֱלֹהִים קְדֹשִׁים (pl.) |

Related canonical entries: [qal-imperfect](qal-imperfect.md), [hiphil-imperfect](hiphil-imperfect.md), [ehyeh-1cs-imperfect](ehyeh-1cs-imperfect.md), [symbol-decoding-predicate-nominal](symbol-decoding-predicate-nominal.md).

## Common Plural-Form Nouns Displaying the Pattern

| Noun | Strong's | Typical referent(s) | Concord diagnostic |
|------|----------|---------------------|--------------------|
| אֱלֹהִים | H430 | God / gods / judges | ~2,601× `Noun.mp.Abs`; overwhelmingly 3ms concord for YHWH; 3p concord at Gen 20:13, Gen 31:53, Gen 35:7, Exo 22:8, 2Sa 7:23, and select others |
| מַיִם | H4325 | water(s) | `Noun.mp.Abs`; regularly 3mp concord (Gen 1:9; 7:19) |
| פָּנִים | H6440 | face / presence | `Noun.mp`; plural concord (Exo 33:14) or absorbed into construct chains (Gen 1:2) |
| שָׁמַיִם | H8064 | heavens / sky | `Noun.mp.Abs`; concord varies |
| חַיִּים | H2416 | life / lives | `Noun.mp.Abs`; abstract — often singular concord |
| רַחֲמִים | H7356 | compassion | `Noun.mp.Abs`; abstract — singular concord typical |
| בְּעָלִים | H1167 | husband / owner | concord diagnoses single vs. multiple (Isa 54:5 honorific) |
| אֲדֹנִים | H113 | lord / master(s) | concord diagnoses single vs. multiple |

---
*Generated from: hebrew_parser.py (--verse, --lemma, --search). All parsings verified from ETCBC BHSA data.*
*Last updated: 2026-04-18*
