# WX-QATAL: Circumstantial / Disjunctive Clause (Hebrew)

## Definition
**WX-QATAL** is the label (Joüon–Muraoka, Niccacci, Randall Buth) for a clause consisting of **waw + a non-verb element (X) + a qatal (suffix-conjugation) verb**, where "X" is the fronted subject, object, prepositional phrase, or adverb — *not* the verb. When this construction follows a wayyiqtol ("and-then" narrative chain), it **breaks** that chain and does **not** advance the story line. Instead it supplies **background, circumstantial, parenthetical, contrastive, or stative-resultant** information concerning the same scene (Waltke–O'Connor §39.2.3; GKC §§141e, 142d, 156).

Three related functions cluster under the label:

1. **Circumstantial / attendant-state** — describes a condition simultaneous with, antecedent to, or ongoing during the main action ("while X was…", "X being…").
2. **Disjunctive / contrastive** — shifts participant or scene, often rendered "but/now/as for X" (W–O'C §39.2.3a: "continuity of scene and participants, but a change of action").
3. **Stative-resultant / perfect of state** — the qatal of a stative or state-entailing verb, expressing a **state** that obtains (past, present, or "perfect") rather than a punctual event (W–O'C §30.5.3; §30.3).

## Form Recognition
**Word order is the key diagnostic**, not morphology of the verb in isolation. The qatal is identical to the qatal used in foreground coordinate-past clauses; what makes the clause circumstantial is that **something other than the verb** stands first after the waw.

| Element slot | Required form |
|---|---|
| 1. Conjunction | וְ (plain waw, not וַ of wayyiqtol) |
| 2. X (fronted constituent) | Noun, pronoun (הוּא / הִיא / הֵם), proper name, object, PP, or negative |
| 3. Verb | qatal (suffix conjugation) — any stem |

- Parser signal in `hebrew_parser.py`: `Conj` immediately followed by a non-verb tag (`PersPron`, `Noun`, `PropN`, `Neg`, `Prep`), then a `Verb … Perf`.
- Distinguish from **wayyiqtol** (וַ + prefixed yiqtol with דגשׁ, verb-first).
- Distinguish from **weqatal** (waw + qatal *verb-first*, no X between them; typically modal/future or habitual).
- Distinguish from **verbless clauses** (waw + X + predicate with no finite verb, e.g. Gen 13:2 — same *pragmatic* disjunctive force but not technically WX-QATAL because the predicate is nominal/adjectival).

## Functions with Examples

### 1. Circumstantial / Background (scene-setting before the main verb)

| Reference | Hebrew (clause) | Parsing | KJV |
|-----------|-----------------|---------|-----|
| Gen 3:1 | וְהַנָּחָשׁ הָיָה עָרוּם | Conj + Art+Noun.ms.Abs (subj) + Qal.Perf.3ms | "Now the serpent was more subtil…" |

Opens the new scene by describing an existing state of the serpent *before* any action. KJV's "**Now** the serpent…" captures the disjunctive waw exactly. The qatal of הָיָה here is the **perfect of state** (W–O'C §30.3): not "and then the serpent became crafty," but "the serpent was [already] crafty."

### 2. Parenthetical / Background Inserted into a Wayyiqtol Chain

| Reference | Hebrew (clause) | Parsing | KJV |
|-----------|-----------------|---------|-----|
| Jdg 11:39b | וְהִיא לֹא־יָדְעָה אִישׁ | Conj + PersPron.3fs (subj) + Neg + Qal.Perf.3fs + Noun.ms.Abs | "and she knew no man" |

Embedded between two wayyiqtols (וַיַּעַשׂ לָהּ אֶת־נִדְרוֹ … וַתְּהִי־חֹק בְּיִשְׂרָאֵל). The fronted pronoun הִיא + negative + qatal breaks the narrative chain. This is **not** reporting the next event ("and *then* she did not know a man"); it is a **parenthetical stative notice** about her status — the narrator's comment that she **was / had been** a virgin — inserted into the account before the transition to the annual custom. See §"Key Question: Jdg 11:39b" below.

### 3. Disjunctive / Contrastive (participant shift with qatal of state-verb)

| Reference | Hebrew (clause) | Parsing | KJV |
|-----------|-----------------|---------|-----|
| Jdg 14:4a | וְאָבִיו וְאִמּוֹ לֹא יָדְעוּ | Conj + Noun.ms+3ms + Conj + Noun.fs+3ms (subj) + Neg + Qal.Perf.3p | "But his father and his mother knew not…" |

KJV's "**But**" reflects the disjunctive force. The qatal יָדְעוּ ("knew") is stative/epistemic: "they had-no-knowledge / were unaware," a state simultaneous with Samson's dealings — **not** the next event in sequence. Note the second half of the same verse (וּבָעֵת הַהִיא פְּלִשְׁתִּים מֹשְׁלִים בְּיִשְׂרָאֵל) is a parallel *verbless* circumstantial clause ("and at that time the Philistines were ruling over Israel"), sharing the same pragmatic function as a WX-QATAL.

### 4. Stative-Resultant (qatal of state in background mode)

| Reference | Hebrew (clause) | Parsing | KJV |
|-----------|-----------------|---------|-----|
| Gen 13:2 | וְאַבְרָם כָּבֵד מְאֹד | Conj + PropN (subj) + Adj.ms.Abs + Adv *(verbless)* | "And Abram [was] very rich…" |

**Parser note:** Gen 13:2 is technically a **verbless clause** — `kaved` is tagged as an adjective here, not a qatal verb — but the pragmatic slot is identical to WX-QATAL: waw + fronted subject + predicate of state = background/circumstantial information about Abram's condition, not the next narrative event. The line between "stative qatal" and "predicate adjective" is thin in Biblical Hebrew; both occupy the same discourse slot (W–O'C §30.5.3 on stative perfects; GKC §141e).

### 5. Circumstantial Verbless with Dative-Possessive (further type)

| Reference | Hebrew (clause) | Parsing | KJV |
|-----------|-----------------|---------|-----|
| 1 Sam 1:2a | וְלוֹ שְׁתֵּי נָשִׁים | Conj + Prep+3ms + Noun.fd.Cst + Noun.fp.Abs *(verbless)* | "And he had two wives" |

A verbless "possessive lamed" clause, parallel in discourse function to WX-QATAL. (The follow-up וַיְהִי לִפְנִנָּה יְלָדִים, "and Peninnah had children," is *wayyiqtol* of הָיָה with fronted dative — a common narrator's way of recording circumstance using the wayyiqtol of the copula; it contrasts in word order with true WX-QATAL but shares background function.)

## Contrast with Related Constructions

| Construction | Word order | Discourse role | Example |
|---|---|---|---|
| **wayyiqtol** | וַ + prefix verb **first** | Foreground, sequential narrative ("and then…") | Jdg 11:39a וַתָּשָׁב (and she returned) |
| **weqatal** (waw-relative) | וְ + qatal **first** | Foreground modal/future, habitual, apodosis of vow/oath | Jdg 11:31 וְהַעֲלִיתִהוּ (and I will offer) |
| **waw + qatal coordinate past** | וְ + qatal **first** | Coordinate past without X; rarer, disputed; often in poetry/lists | — (see W–O'C §32.3) |
| **WX-QATAL** (this entry) | וְ + X + qatal | **Background / circumstantial / stative / contrastive**; halts the chain | Gen 3:1; Jdg 11:39b; Jdg 14:4 |
| **Verbless WX-clause** | וְ + X + nominal/adj predicate | Same pragmatic slot as WX-QATAL, no finite verb | Gen 13:2; 1 Sam 1:2 |

**Why it matters:** mistaking WX-QATAL for a coordinated sequential qatal ("and-then…") imports a temporal succession the construction does not carry. Conversely, mistaking a wayyiqtol of הָיָה (e.g. וַיְהִי in Jdg 11:39a) for a scene-setter erases the foreground step.

## Key Question: Judges 11:39b

> וַיַּעַשׂ לָהּ אֶת־נִדְרוֹ אֲשֶׁר נָדָר **וְהִיא לֹא־יָדְעָה אִישׁ** וַתְּהִי־חֹק בְּיִשְׂרָאֵל
> "…he did with her according to his vow which he had vowed; **and she knew no man**; and it became a custom in Israel."

**Is the italicized clause sequential or circumstantial?**

*Sequential reading* ("and thereafter she did not know a man") would require wayyiqtol — וְלֹא יָדְעָה with a verb-first order, or more naturally וְלֹא נוֹדְעָה + a repeated verb — but the text has WX order (**וְהִיא** … יָדְעָה), which is **the textbook marker of a disjunctive/circumstantial clause** (W–O'C §39.2.3; GKC §156).

*Circumstantial / stative-resultant reading* ("…and she, she had-not-known a man") fits the standard function of the construction: a **parenthetical notice of her state**. On this reading the qatal יָדְעָה is a **perfect of state** (W–O'C §30.3; §30.5.3: stative/effected-state verbs in the suffix conjugation denote a present state arising from an anterior situation) — the narrator's summary that **at the time of the vow's fulfillment her condition was that of a virgin**, consistent with the preceding two-month mourning לִבְתוּלֶיהָ (Jdg 11:37–38).

Grammatical verdict: the clause is **not a statement that her virginity continued after the vow's execution through a subsequent lifetime of celibacy** (which would be the sequential reading); it is a **background state-description framing the fulfillment of the vow**. Whatever the vow's fulfillment entailed (immolation vs. lifelong consecration — a separate lexical/theological question), the WX-QATAL is supplying *attendant circumstance*, not *subsequent action*.

References: Waltke–O'Connor §30.3, §30.5.3 (perfective and perfect of state); §39.2.3 (disjunctive waw); GKC §141e, §156 (circumstantial clauses with waw + subject + perfect).

## Reference Grammars Consulted
- Waltke & O'Connor, *An Introduction to Biblical Hebrew Syntax*, §30.3 (perfective and perfect state), §30.5.3 (stative verbs in the suffix conjugation), §39.2.3 (Disjunctive Waw), §§32.3, 33 (waw-relative contrast).
- Gesenius–Kautzsch–Cowley (GKC), §141e (circumstantial noun-clause with waw + subj + perf.), §142d (waw + subj + pf. as circumstantial), §156 (circumstantial clauses), §164 (temporal/circumstantial subordination).
- Joüon–Muraoka, *A Grammar of Biblical Hebrew*, §159 (circumstantial clauses); §166 (disjunctive waw).
- Niccacci, *The Syntax of the Verb in Classical Hebrew Prose*, §§17–19 (background WX-QATAL in narrative).

## Related Library Entries
- [syntax-waw-conjunction](syntax-waw-conjunction.md) — general conjunctive/disjunctive force of וְ
- [weqatal-apodosis-vow](weqatal-apodosis-vow.md) — foreground weqatal in vow apodosis (contrast)
- [syntax-conditional-vow](syntax-conditional-vow.md) — protasis/apodosis in vow register

---
*Generated from: hebrew_parser.py (--verse Gen 3:1, Gen 13:2, Jdg 11:39, 1Sa 1:2, Jdg 14:4); semantic_grammar.py (W–O'C §39.2.3 "Disjunctive Waw" p.736–738; GKC §156 "Circumstantial Clauses" p.455–456; W–O'C §30.3 "Perfective Aspect and the Perfect State" p.550).*
*Last updated: 2026-04-17*
