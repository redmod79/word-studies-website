# Conditional Vow Syntax (Hebrew)

## Definition
A recurring syntactic pattern in which a human vow to God is framed as a conditional sentence: **protasis** introduced by אִם ("if") specifying what YHWH is asked to do, and **apodosis** (introduced by waw + perfect / weqatal) specifying what the vower will do in return. The protasis verb is typically imperfect (often intensified by a preceding infinitive absolute), and each further clause in both protasis and apodosis is chained by weqatal. This is a sub-type of Hebrew real/future-conditional syntax, specialized for votive speech.

1. **Conditional frame** — אִם marks a future, real (not contrary-to-fact) condition presented to the deity
2. **Emphatic protasis** — infinitive absolute + finite verb (tautological infinitive) often intensifies the "if indeed..." clause
3. **Sequential apodosis** — weqatal (waw + perfect) carries the vower's future pledge forward, often multiple clauses

## Form Recognition
- Speech-frame trigger: verb נדר ("vow") + cognate accusative נֶדֶר, followed by אמר ("say"), then direct speech
- Protasis head: **אִם** as a conjunction (tagged `Conj` on אם, not adverbial)
- Protasis verb: Qal Imperfect (often 2ms addressing YHWH); optionally preceded by homolexical Infinitive Absolute
- Apodosis verbs: waw + Perfect (weqatal) — same form that continues an imperfect's future force
- **Parser codes:**
  - Infinitive absolute + imperfect pair: `sp=verb vt=infa` followed by `sp=verb vt=impf` of same lemma
  - Weqatal apodosis: `sp=verb vt=perf` preceded by ו Conj

## Functions with Examples

### 1. Simple conditional vow (אִם + imperfect protasis, weqatal apodosis)

Jacob at Bethel — the protasis uses plain imperfect (no inf. abs.), then shifts to weqatal within the protasis itself before the apodosis is marked.

| Reference | Hebrew | Parsing | KJV gloss |
|-----------|--------|---------|-----------|
| Gen 28:20 | אִם־יִהְיֶה אֱלֹהִים עִמָּדִי | אם Conj + היה Qal.Impf.3ms | "If God will be with me" |
| Gen 28:20 | וּשְׁמָרַנִי | ו Conj + שׁמר Qal.Perf.3ms + 1cs | "and will keep me" (weqatal, still protasis) |
| Gen 28:20 | וְנָתַן־לִי לֶחֶם | ו Conj + נתן Qal.Perf.3ms | "and will give me bread" (weqatal) |
| Gen 28:21 | וְשַׁבְתִּי בְשָׁלוֹם | ו Conj + שׁוב Qal.Perf.1cs | "so that I come again in peace" (weqatal) |
| Gen 28:21 | וְהָיָה יְהוָה לִי לֵאלֹהִים | ו Conj + היה Qal.Perf.3ms | "then shall YHWH be my God" — **apodosis** |

### 2. Emphatic conditional vow (אִם + inf. abs. + imperfect, weqatal apodosis)

The protasis is intensified by the tautological infinitive absolute ("if thou wilt indeed…"), a standard oath-register device. The apodosis is a weqatal of the vower's pledge.

| Reference | Hebrew | Parsing | KJV gloss |
|-----------|--------|---------|-----------|
| Num 21:2 | אִם־נָתֹן תִּתֵּן אֶת־הָעָם הַזֶּה בְּיָדִי | אם Conj + נתן Qal.InfAbs + נתן Qal.Impf.2ms | "If thou wilt indeed deliver this people into my hand" |
| Num 21:2 | וְהַחֲרַמְתִּי אֶת־עָרֵיהֶם | ו Conj + חרם Hiphil.Perf.1cs | "then I will utterly destroy their cities" — **apodosis** |
| Judg 11:30 | אִם־נָתוֹן תִּתֵּן אֶת־בְּנֵי עַמּוֹן בְּיָדִי | אם Conj + נתן Qal.InfAbs + נתן Qal.Impf.2ms | "If thou shalt without fail deliver the children of Ammon" |
| Judg 11:31 | וְהָיָה הַיּוֹצֵא... וְהָיָה לַיהוָה | ו Conj + היה Qal.Perf.3ms (×2) | "Then it shall be... shall surely be the LORD'S" — **apodosis head** |
| Judg 11:31 | וְהַעֲלִיתִהוּ עֹלָה | ו Conj + עלה Hiphil.Perf.1cs + 3ms | "and I will offer it up as a burnt-offering" — apodosis cont. |
| 1Sa 1:11 | אִם־רָאֹה תִרְאֶה בָּעֳנִי אֲמָתֶךָ | אם Conj + ראה Qal.InfAbs + ראה Qal.Impf.2ms | "if thou wilt indeed look on the affliction of thy handmaid" |
| 1Sa 1:11 | וּזְכַרְתַּנִי | ו Conj + זכר Qal.Perf.2ms + 1cs | "and remember me" (weqatal, protasis continues) |
| 1Sa 1:11 | וְנָתַתָּה לַאֲמָתְךָ זֶרַע אֲנָשִׁים | ו Conj + נתן Qal.Perf.2ms | "and wilt give to thy handmaid a man child" (weqatal, protasis) |
| 1Sa 1:11 | וּנְתַתִּיו לַיהוָה | ו Conj + נתן Qal.Perf.1cs + 3ms | "then I will give him to YHWH" — **apodosis** |

### 3. Shift of subject marks protasis→apodosis boundary

Because both protasis and apodosis continue with weqatal, the transition is signaled not by verb form but by **person shift** (from 2ms/3ms verbs about God to 1cs verbs about the speaker). In Jacob's vow the shift is from 3ms (God's acts) to 1cs (speaker's pledge in v.22). In Hannah's vow it is from 2ms (God's acts) to 1cs (וּנְתַתִּיו, "and I will give him").

| Passage | Protasis verbs | Apodosis verbs |
|---------|----------------|----------------|
| Gen 28:20–22 | יִהְיֶה, וּשְׁמָרַנִי, וְנָתַן, וְשַׁבְתִּי (3ms / 1cs of return) | וְהָיָה יְהוָה לִי, אֲעַשְּׂרֶנּוּ (1cs pledge) |
| Num 21:2 | נָתֹן תִּתֵּן (2ms) | וְהַחֲרַמְתִּי (1cs) |
| Judg 11:30–31 | נָתוֹן תִּתֵּן (2ms) | וְהָיָה... וְהַעֲלִיתִהוּ (3ms subject + 1cs pledge) |
| 1Sa 1:11 | תִרְאֶה, וּזְכַרְתַּנִי, וְנָתַתָּה (2ms) | וּנְתַתִּיו (1cs) |

## Contrast with Related Forms

| Form | Function | Example |
|------|----------|---------|
| אִם + imperfect (this entry) | Real/future condition, esp. vows & oaths | Gen 28:20; 1Sa 1:11 |
| אִם + perfect | Real condition in present/past; sometimes contrary-to-fact with לוּא | — |
| לוּ / לוּלֵא + perfect | Counterfactual ("if only…"/"were it not") | — |
| כִּי as conditional | "When/if" — more temporal, less vow-specific | — |
| Infinitive absolute + finite verb | Emphasis; with אִם in oaths = "if indeed" | Num 21:2; Judg 11:30; 1Sa 1:11 |
| Weqatal (waw-consecutive perfect) | Continues imperfect/future force; chains clauses | every apodosis here |

The vow-conditional is a **specialized register** of the general אִם + imperfect real-condition pattern. Its formal hallmarks are (a) the narrative frame verb נדר + cognate נֶדֶר, (b) optional tautological infinitive absolute intensifying the protasis, and (c) weqatal chains that run across the protasis/apodosis seam, with the boundary marked by subject shift.

## Common Verbs in This Pattern

Verbs observed in the protases and apodoses of the four vows above:

| Verb | Strong's | Role | Occurrence here |
|------|----------|------|-----------------|
| היה | H1961 | Protasis ("if X be"); apodosis opener ("then shall be") | Gen 28:20, 21; Jdg 11:31 |
| שׁמר | H8104 | Protasis (asked of God) | Gen 28:20 |
| נתן | H5414 | Protasis (God gives) + apodosis (vower gives) | Gen 28:20; Num 21:2; Jdg 11:30; 1Sa 1:11 |
| ראה | H7200 | Protasis inf. abs. + impf. | 1Sa 1:11 |
| זכר | H2142 | Protasis weqatal ("remember me") | 1Sa 1:11 |
| חרם | H2763 (Hiphil) | Apodosis pledge ("devote to destruction") | Num 21:2 |
| עלה | H5927 (Hiphil) | Apodosis pledge ("offer up") | Jdg 11:31 |
| עשׂר | H6237 (Piel) | Apodosis pledge ("tithe"; inf. abs. + impf.) | Gen 28:22 |

Note Gen 28:22 also contains an emphatic inf. abs. + imperfect *in the apodosis* (עַשֵּׂר אֲעַשְּׂרֶנּוּ, "I will surely tithe it"), mirroring the emphatic protasis device seen in the other three vows.

---
*Generated from: hebrew_parser.py --verse (Gen 28:20–22; Num 21:2; Jdg 11:30–31; 1Sa 1:11); kjv.txt*
*Last updated: 2026-04-16*
