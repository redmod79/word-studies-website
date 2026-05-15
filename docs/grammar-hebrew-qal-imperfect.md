# Qal Imperfect (Hebrew)

## Definition

The **Qal Imperfect** (also called **yiqtol** or *prefix conjugation*) is the base-stem (Qal) non-perfective verb form. Morphologically it is built by prefixing person markers to the root; semantically it expresses action viewed as **internally unfolding, non-completed, or not-yet-completed** — the viewpoint "from the inside" of a situation (Waltke-O'Connor §29.6c; GKC §107). Because Biblical Hebrew encodes **aspect rather than absolute tense**, a single Qal imperfect form can translate into English as future, present progressive, habitual/gnomic, or modal depending on context.

1. **Future / predictive** — action not yet realized.
2. **Habitual / iterative / gnomic** — repeated or customary action, or timeless truths.
3. **Durative / progressive** — ongoing action viewed from inside ("is being / keeps being").
4. **Modal / volitive** — desire, intention, possibility, permission, obligation; overlaps with cohortative in 1st person and jussive in 3rd.
5. **Past habitual / past continuous** — repeated action in past narrative frames (rare, context-bound).

## Form Recognition

- **Prefix afformatives** (person markers attached to the front of the root):
  - 1cs אֶ־ (ʾe-)  1cp נִ־ (ni-)
  - 2ms תִּ־ (ti-)  2fs תִּ־...־י (ti-...-î)
  - 2mp תִּ־...־וּ (ti-...-û)  2fp תִּ־...־נָה (ti-...-nâ)
  - 3ms יִ־ (yi-)  3fs תִּ־ (ti-)
  - 3mp יִ־...־וּ (yi-...-û)  3fp תִּ־...־נָה (ti-...-nâ)
- Qal stem = base pattern (no stem-prefix, no doubled middle radical, no ־ה־ prefix of Hiphil).
- Theme-vowel normally holem (o) or patach (a) between R2 and R3: יִקְטֹל / יִשְׁלַח.
- Long form (yiqtol / indicative), short form (jussive), cohortative (+ ־ָה on 1st person).
- **Parser code:** `sp=verb vs=qal vt=impf` (hebrew_parser.py search)

## Functions with Examples

### 1. Future / Predictive

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Gen 2:17 | תָּמוּת | Qal.Impf.2ms | "thou shalt surely die" |
| Gen 3:15 | אָשִׁית | Qal.Impf.1s | "I will put [enmity]" |
| Gen 12:2 | אֶֽעֶשְׂךָ | Qal.Impf.1s+2ms | "I will make of thee [a great nation]" |

### 2. Habitual / Gnomic / Durative

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Psa 1:2 | יֶהְגֶּה | Qal.Impf.3ms | "[in his law] doth he meditate day and night" (customary) |
| Gen 2:24 | יַעֲזָב | Qal.Impf.3ms | "shall a man leave" (gnomic custom) |

### 3. Modal / Volitive (Intention, Permission, Prohibition)

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Gen 2:16 | תֹּאכֵל | Qal.Impf.2ms | "thou mayest freely eat" (permission) |
| Exo 20:13 | תִּרְצָח (Qal.Impf.2ms, "kill") | Qal.Impf.2ms | "Thou shalt not kill" (apodictic prohibition) |
| Gen 2:18 | אֶעֱשֶׂה | Qal.Impf.1s | "I will make" (volitive/cohortative overlap) |

### 4. First-Person Singular (1cs) — Cohortative Overlap in Divine Speech

The 1cs Qal imperfect (אֶ־ prefix) frequently blurs with the cohortative (אֶ־...־ָה). In divine self-speech the 1cs yiqtol carries strong volitive force — self-committal, resolve, self-description.

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| **Exo 3:14** | **אֶהְיֶה** (×3) | **Qal.Impf.1s** of היה "be" | **"I AM"** (I will be / I am being / I shall be) |
| Gen 6:7 | אֶמְחֶה | Qal.Impf.1s | "I will destroy" |
| Gen 9:5 | אֶדְרֹשׁ | Qal.Impf.1s | "will I require" |
| Isa 41:10 | אֲחַזַּקְתִּיךָ / אֲאַמֶּצְךָ / אֶתְמָכְךָ | (Piel/Qal Impf.1s series) | "I will strengthen thee … I will help thee … I will uphold thee" |

At Exo 3:14 the form אֶהְיֶה is **unambiguously Qal Impf 1cs of היה**, the same form that appears at Gen 1:3 יְהִי (Qal Impf 3ms, jussive "let there be"). The imperfective aspect licenses the full semantic range "I am / I will be / I continue to be / I am being-what-I-am-being" — English glosses pick one slice of a form that contains all of them simultaneously.

## Contrast with Related Forms

| Form | Viewpoint | Function | Example |
|------|-----------|----------|---------|
| **Qal Perfect** (qatal) | perfective / external | completed, bounded, stative-result | Gen 1:1 בָּרָא "created" (completed act) |
| **Qal Imperfect** (yiqtol) | imperfective / internal | ongoing, future, habitual, modal | Gen 1:3 יְהִי "let there be" |
| **Qal Wayyiqtol** (way-) | perfective in narrative | past narrative sequence | Gen 1:3 וַיֹּאמֶר "and [he] said" |
| **Qal Cohortative** (1st) | volitive | self-resolve, "let me" | Psa 2:3 נְנַתְּקָה "let us break" |
| **Qal Jussive** (3rd/2nd) | volitive | wish/command, "let X" | Gen 1:3 יְהִי "let there be" (short form) |

### Qal Imperfect vs. Hiphil Imperfect

Same imperfective aspect, different **stem voice**:

| Form | Stem Sense | Example | Gloss |
|------|-----------|---------|-------|
| **Qal Impf** | simple active (subject does action) | יָקוּם "he will arise" | agent simply acts |
| **Hiphil Impf** | causative (subject makes another do action) | יָקִים "he will cause-to-arise / raise up" | agent causes |
| **Qal Impf 1cs** (Exo 3:14) | אֶהְיֶה "I will be / I am" | subject *is* | |
| **Hiphil Impf 1cs** (hypothetical) | אַהְיֶה / אֲהֲוֶה "I will cause to be" | subject *makes to be* | |

The Exo 3:14 reading is **Qal** — God is self-predicating existence/presence, not claiming to cause others to exist. A Hiphil imperfect would shift the predication from **self-existence/self-presence** to **causation-of-being** (the causative creator-reading proposed by some scholars depends on re-pointing the form, not on the Masoretic vocalisation, which is Qal).

## Use in Divine Speech

The Qal imperfect dominates divine first-person speech because the aspectual openness matches the character of covenant self-disclosure:

- **Self-commitment**: "I will be with thee" — *ʾehyeh ʿimmāk* (Exo 3:12; Qal Impf 1cs היה).
- **Covenant formula**: "I will be their God and they shall be my people" (Jer 31:33; paired yiqtol predications).
- **Self-revelation**: Exo 3:14 אֶהְיֶה אֲשֶׁר אֶהְיֶה — the relative clause אֲשֶׁר linking two identical Qal Impf 1cs forms produces an idem per idem construction whose semantic openness is a **feature of the imperfective aspect**, not a gap.
- 1cs Qal impf in divine oracles regularly fuses prediction + promise + volition (Isa 41:10; 43:2).

## Common Verbs in Qal Imperfect

| Verb (root) | Strong's | Qal Impf 3ms | Gloss |
|-------------|----------|--------------|-------|
| היה | H1961 | יִהְיֶה / יְהִי | be, become |
| אמר | H559 | יֹאמַר / תֹּאמַר | say |
| עשׂה | H6213 | יַעֲשֶׂה / אֶעֱשֶׂה | do, make |
| נתן | H5414 | יִתֵּן / אֶתֵּן | give |
| ידע | H3045 | יֵדַע / תֵּדַע | know |
| הלך | H1980 | יֵלֵךְ / תֵלֵךְ | walk, go |
| הגה | H1897 | יֶהְגֶּה | meditate, mutter |

## Reference Citations

- **Waltke-O'Connor, *Introduction to Biblical Hebrew Syntax*** §29–31 (pp. 455–478 on Qal; pp. 496–518 on the non-perfective conjugation and its relation to Hiphil; p. 543 on perfective/imperfective viewpoint "from outside vs. from inside"; pp. 539, 565 on yiqtol/jussive morphological distinctions).
- **Gesenius' Hebrew Grammar (Kautzsch-Cowley)** §107 on the imperfect; p. 301: "an action conceived as being still in progress (imperfect, &c.), reaching afterwards in the perfect a calm and settled conclusion."
- **Brown-Driver-Briggs / Barrick-Busenitz, *A Grammar for Biblical Hebrew*** pp. 107–108: "The action of the prefixed verb form (imperfect or yiqtol) … has often been described as incomplete or moving toward completion."
- **Futato, *Beginning Biblical Hebrew*** Lessons 11 (Qal Imperfect) and 31, 33 (Qal/Hiphil comparison).

## Related Library Entries

- [stem-niphal](stem-niphal.md) — passive/reflexive counterpart to Qal.
- [weqatal-apodosis-vow](weqatal-apodosis-vow.md) — contrasting waw+perfect that often follows an imperfect protasis.
- [syntax-conditional-vow](syntax-conditional-vow.md) — imperfect in protasis of conditional vows.

---
*Generated from: hebrew_parser.py (--search, --lemma, --verse), semantic_grammar.py*
*Last updated: 2026-04-18*
