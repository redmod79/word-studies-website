# Weqatal (Perfect Consecutive) in Legal/Imperatival Function (Hebrew)

## Definition
The **weqatal** — waw + suffix-conjugation verb (וְ + qatal) — when threaded through legal/paraenetic prose functions as a **second-person command**, not a past narrative or a bare future prediction. In the Deuteronomic code it forms long chains of covenant obligations addressed to Israel ("and thou shalt give / eat / rejoice"), taking its imperatival force from an anchoring imperative, imperfect-of-command, or infinitive-absolute + imperfect trigger upstream, then propagating that force through every subsequent וְ+perfect until the chain is broken by a new speech-act (לֹא+impf prohibition, casuistic כִּי-clause, motive clause, etc.).

1. **Legal injunction continuing an imperatival trigger** — weqatal carries the 2ms/2mp command after an opening impv, yiqtol-of-command, or inf.abs.+impf
2. **Chained covenant obligations (feast / tithe / cult laws)** — stacks of weqatals in Deut 12, 14, 16 binding the addressee to a sequence of cultic acts at the chosen-place
3. **Independent-opening command** — a weqatal may even open a verse/paragraph (Deut 16:11 וְשָׂמַחְתָּ) carrying imperatival force from the broader pericope without an adjacent trigger

## Form Recognition
The weqatal is **morphologically identical to a plain perfect**; the legal-imperatival reading is recognized by **genre + chain position**, not by morphology alone:

- **וְ- prefixed to a perfect-conjugation verb** (2ms or 2mp dominant in Deuteronomic code)
- Stress shift: in 1cs/2ms forms classical weqatal stress moves to the ultima (וְנָתַתָּ֣ה Deut 14:26) — but stress is inconsistent, especially in final-heh and hollow roots
- **Genre diagnostic:** occurs in second-person paraenetic/legal direct address, not narrative; the discourse is instruction about future conduct, not report of past events
- **Upstream anchor:** a Qal/Piel/Hiphil imperfect, imperative, or inf.abs.+impf in the immediate pericope licenses the imperatival reading
- **Parser codes:** `vs=<any stem> vt=perf ps=2` with prefixed וְ conjunction. The ETCBC/BHSA parser does **not** tag weqatal distinctly from plain perfect — identification is syntactic and generic.

## Functions with Examples

### 1. Weqatal Chain After an Imperfect-of-Command (Deuteronomic feast-law)

**Deut 12:5–7 Three-stage chain** — יִבְחַ֨ר (Qal.Impf.3ms "shall choose" — the protasis of the central-sanctuary law) → תִדְרְשׁ֖וּ (Qal.Impf.2mp "ye shall seek" — the first command) → then a cascade of weqatals:

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Deut 12:5 | וּבָ֥אתָ שָֽׁמָּה | Verb.Qal.Perf.**2ms** + waw | "and thither thou shalt come" |
| Deut 12:6 | וַהֲבֵאתֶ֣ם שָׁ֗מָּה עֹלֹֽתֵיכֶם֙ | Verb.Hiphil.Perf.**2mp** + waw | "and thither ye shall bring your burnt offerings" |
| Deut 12:7 | וַאֲכַלְתֶּם־שָׁ֗ם | Verb.Qal.Perf.**2mp** + waw | "and there ye shall eat" |
| Deut 12:7 | וּשְׂמַחְתֶּ֗ם | Verb.Qal.Perf.**2mp** + waw | "and ye shall rejoice" |

Notice the number shift 2ms→2mp→2mp within three verses — characteristic of Deuteronomy's *Numeruswechsel*. Every וְ+Perf carries forward the imperatival force triggered by תִדְרְשׁ֖וּ. KJV consistently renders "and thou/ye shall X," never "and thou/ye came/brought/ate/rejoiced."

### 2. Weqatal Chain After Infinitive-Absolute + Imperfect (tithe-law)

**Deut 14:22–26** opens with the paronomastic intensifier עַשֵּׂ֣ר תְּעַשֵּׂ֔ר (Piel.InfAbs + Piel.Impf.2ms "thou shalt truly tithe" — cross-linked to [infinitive-absolute-intensification](infinitive-absolute-intensification.md)). The tithe-command then propagates through weqatals:

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Deut 14:26 | וְנָתַתָּ֣ה הַכֶּ֡סֶף | Verb.Qal.Perf.**2ms** + waw | "and thou shalt bestow that money" |
| Deut 14:26 | וְאָכַ֣לְתָּ שָּׁ֗ם | Verb.Qal.Perf.**2ms** + waw | "and thou shalt eat there" |
| Deut 14:26 | וְשָׂמַחְתָּ֖ אַתָּ֥ה וּבֵיתֶֽךָ | Verb.Qal.Perf.**2ms** + waw | "and thou shalt rejoice, thou, and thine household" |

Three weqatals triple-binding the Israelite to the act-sequence *give → eat → rejoice*. The triad *נתן / אכל / שׂמח* recurs across the Deuteronomic feast calendar (12:7, 12:18, 14:26, 16:11, 16:14) and is always carried by weqatal morphology once the opening command is issued.

### 3. Independent-Opening Weqatal (Feast-Paragraph Head)

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Deut 16:11 | וְשָׂמַחְתָּ֞ לִפְנֵ֣י יְהוָ֣ה | Verb.Qal.Perf.**2ms** + waw | "And thou shalt rejoice before the LORD" |
| Deut 16:14 | וְשָׂמַחְתָּ֖ בְּחַגֶּ֑ךָ | Verb.Qal.Perf.**2ms** + waw | "And thou shalt rejoice in thy feast" |
| Deut 12:18 | וְשָׂמַחְתָּ֗ לִפְנֵי֙ יְהוָ֣ה | Verb.Qal.Perf.**2ms** + waw | "and thou shalt rejoice before the LORD thy God" |

In 16:11 and 16:14 the weqatal *opens* the verse and — effectively — the injunction. The imperatival force comes from the pericope's genre (Shavuot and Sukkot laws respectively), not a local anchor. Deut 12:18 shows the transitional mid-paragraph pattern: a Qal.Impf.2ms anchor (תֹּאכְלֶ֗נּוּ "thou shalt eat it") licenses the weqatal that immediately follows (וְשָׂמַחְתָּ).

## Contrast with Related Forms

| Form | Temporal Domain | Function | Example |
|------|-----------------|----------|---------|
| **Weqatal (legal/imperatival)** | future / obligatory | covenant command, binds addressee to act | Deut 14:26 וְנָתַתָּ֣ה |
| **Weqatal (apodosis of vow)** | future / commissive | speaker pledges own future act after אִם | Judg 11:31 וְהַעֲלִיתִ֖הוּ ([weqatal-apodosis-vow](weqatal-apodosis-vow.md)) |
| **Weqatal (pure prediction)** | future / indicative | declarative forecast, not obligation | Gen 12:3 וְנִבְרְכוּ "and shall be blessed" (prophetic promise, not command) |
| **Wayyiqtol (וַ+impf)** | past / narrative | narrative past sequence | Deut 1:19 וַנִּסַּ֣ע "and we departed" |
| **Imperfect (yiqtol)** | future / modal | often protasis or initial command-anchor | Deut 14:22 תְּעַשֵּׂ֔ר "thou shalt tithe" |
| **Imperative (impv)** | present-future / direct command | positive 2nd-person only | Deut 6:4 שְׁמַע "hear" |
| **לֹא + yiqtol (prohibition)** | eternal / categorical | negative command (never weqatal + לֹא) | Exo 20:13 לֹא תִרְצָח ([imperative-mood](imperative-mood.md)) |

**Three diagnostic contrasts** worth stating explicitly:

1. **Weqatal vs. wayyiqtol.** Consecutive forms are mirror-images of each other: *wayyiqtol* = waw + imperfect-morphology, advances **past narrative** ("and he did"); *weqatal* = waw + perfect-morphology, advances **future/modal/habitual** discourse ("and thou shalt do"). Identical surface-pattern (waw + finite verb) but opposite tense-domain. Deuteronomy's legal code is almost entirely weqatal + yiqtol; the narrative frame (Deut 1–3) is almost entirely wayyiqtol.

2. **Weqatal (legal) vs. weqatal (pure prediction).** Both are future-oriented and morphologically identical. Distinction is by **addressee + genre**: 2nd-person legal paraenesis = imperatival ("and thou shalt eat," addressee obligated); 3rd-person or declarative prophecy = predictive ("and it shall come to pass," no obligation imposed). Deut 28 blessings/curses mix both — "and thou shalt" weqatals addressing Israel's conduct vs. "and X shall happen to thee" weqatals predicting divine action.

3. **Weqatal (legal) vs. weqatal (apodosis of vow).** Both are commissive/obligatory, but the speech-act differs. The apodosis-of-vow weqatal binds the **speaker** ("I will offer him up," Judg 11:31) after a self-imposed אִם-condition. The legal weqatal binds the **addressee** ("thou shalt give," Deut 14:26) under God-imposed covenant command. See [weqatal-apodosis-vow](weqatal-apodosis-vow.md) for the votive type.

## Common Verbs in Deuteronomic Legal Weqatal Chains

Derived from Deut 12:5–7; 12:18; 14:22–26; 16:11, 14 (parser-verified):

| Verb | Strong's | Gloss in this form | Notable occurrences |
|------|----------|--------------------|---------------------|
| בוא | H935 | "thou shalt come" / "ye shall bring" (Hiphil) | Deut 12:5 וּבָ֥אתָ (Qal.Perf.2ms); 12:6 וַהֲבֵאתֶ֣ם (Hiphil.Perf.2mp) |
| אכל | H398 | "ye/thou shalt eat" | Deut 12:7 וַאֲכַלְתֶּם־ (2mp); 14:26 וְאָכַ֣לְתָּ (2ms) |
| שׂמח | H8055 | "thou/ye shall rejoice" | Deut 12:7 (2mp); 12:18, 14:26, 16:11, 16:14 (all 2ms) |
| נתן | H5414 | "thou shalt give" | Deut 14:26 וְנָתַתָּ֣ה (2ms) |

The distinctive Deuteronomic triad **give → eat → rejoice** (נתן / אכל / שׂמח) appears as three weqatals in Deut 14:26 and structures the pilgrimage-feast laws of Deut 16. The 2ms singular addressee dominates the legal code, with occasional shifts to 2mp plural — *Numeruswechsel* that Deuteronomic studies (von Rad, Tigay, McConville) treat as rhetorical rather than source-critical.

## Recognition Heuristic

When reading Deuteronomy's legal corpus, apply this test to any וְ + perfect 2ms/2mp form:

1. Is the surrounding pericope paraenetic/legal (not narrative)? → weqatal
2. Is there an upstream imperative, inf.abs.+impf, or command-yiqtol within the paragraph or pericope-head? → weqatal-imperatival
3. Does the subject = the addressee (not the speaker)? → legal weqatal, not apodosis-of-vow weqatal
4. KJV renders as "and thou/ye shall X"? → confirms the weqatal-imperatival classification (KJV is near-perfectly consistent on this)

If all four checks pass, the form is a legal/imperatival weqatal, carrying the same deontic force as the opening imperfect-of-command or imperative.

---
*Generated from: hebrew_parser.py (--verse on Deut 12:5–7, 12:18, 14:22, 14:26, 16:11, 16:14); KJV text via D:/bible/tools/data/kjv.txt*
*Last updated: 2026-04-19*
