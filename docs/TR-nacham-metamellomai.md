# TR: nacham → metamellomai (Relent / Regret / "Repent")

## The Chain

```
Hebrew OT                    LXX (Greek OT)              Greek NT
───────────                  ───────────────             ────────
נָחַם (nâcham)           →  μεταμέλομαι (metamellomai) →  μεταμέλομαι (metamellomai)
H5162, 100 OT verses         rare (~2x; Ps 109:4 [=110:4])  G3338, 5 NT verses
"sigh, be sorry, relent,     primary LXX equivalents:        "regret, care
 comfort, repent"             παρακαλέω, μετανοέω            afterwards"
```

Primary LXX renderings of nacham are **παρακαλέω (G3870, comfort)** — 52x — and **μετανοέω (G3340, change mind / repent)** — 14x. **μεταμέλομαι (G3338)** is a secondary bridge; its importance is disproportionate to frequency because the LXX used it at **Psalm 109:4 (MT 110:4)**, the verse cited verbatim at **Hebrews 7:21**.

## OT Usage (Hebrew)

| Strong's | Word | POS | Occurrences | Primary Meaning |
|----------|------|-----|-------------|-----------------|
| H5162 | נָחַם (nâcham) | verb | 100 verses (108 forms) | sigh, be sorry, relent, comfort, console, repent |
| H5164 | נֹחַם (nocham) | masc. noun | 1 | repentance, sorrow (Hos 13:14) |
| H5165 | נֶחָמָה (nechamah) | fem. noun | 2 | comfort |
| H5150 | נִחוּם (nichuwm) | masc. noun | 3 | comfort, compassion |

**Stem range:** nacham appears in Niphal ("be sorry, relent, repent"), Piel ("comfort"), Pual ("be comforted"), and Hithpael ("be comforted, ease oneself, avenge oneself"). Translation depends heavily on stem.

**Key OT passages:**
- **Gen 6:6** — "And it repented the LORD that he had made man on the earth, and it grieved him at his heart." (Niphal; divine relenting in grief)
- **Num 23:19** — "God is not a man, that he should lie; neither the son of man, that he should repent." (programmatic denial)
- **1 Sam 15:29** — "And also the Strength of Israel will not lie nor repent: for he is not a man, that he should repent." (same Niphal form, same denial)
- **1 Sam 15:11, 35** — "It repenteth me that I have set up Saul" / "the LORD repented that he had made Saul king" (same chapter affirms what 15:29 denies — framing question: two senses of nacham)
- **Ps 110:4** — "The LORD hath sworn, and will not repent, Thou art a priest for ever after the order of Melchizedek." (Niphal negated + oath)
- **Jer 18:8, 10** — "I will repent of the evil... I will repent of the good" (conditional relenting tied to human repentance)
- **Joel 2:13** — "slow to anger, and of great kindness, and repenteth him of the evil" (character formula)
- **Jon 3:9–10; 4:2** — "God repented of the evil... he is a gracious God... and repentest thee of the evil" (same character formula cited back at YHWH)

## LXX Bridge

### H5162 nacham → Greek (LXX renderings, ranked by co-occurrence and PMI)

| Greek | Word (Translit) | Co-occ | PMI Score | Notes |
|-------|-----------------|--------|-----------|-------|
| G3870 | παρακαλέω (parakaleō) | 52 | 28.53 | **Primary** — covers Piel "comfort" and Hithpael "be comforted" (majority Isaiah/Jeremiah) |
| G3340 | μετανοέω (metanoeō) | 14 | 20.21 | **Primary for "repent" sense** — used at 1 Sam 15:29, Joel 2:13, Amos 7:3, 7:6, Jon 3:9, 3:10, 4:2, Jer 18:8, Jer 18:10, etc. |
| G2549 | κακία (kakia) | 8 | 9.00 | Noun co-occurrence — "the evil" of which God relents |
| G3973 | παύω (pauō) | 6 | 8.91 | "cease, stop" — alternative for relenting/desisting |
| G3996 | πενθέω (pentheō) | 5 | 8.46 | "mourn" — for grief/lament contexts |
| G2556 | κακός (kakos) | 10 | 7.49 | Adjective co-occurrence — same "evil" pattern |
| G1653 | ἐλεέω (eleeō) | 5 | 6.73 | "have mercy" — overlaps with consolation |
| G447 | ἀνίημι (aniēmi) | 3 | 6.11 | "let go, release" |
| G3338 | **μεταμέλομαι (metamellomai)** | rare (~2x) | (secondary) | **Not in top co-occurrence**, but used at **Psa 109:4 LXX (= MT 110:4)** and 1 Sam 15:29 in some witnesses — the load-bearing bridge for Hebrews 7:21 |

### G3338 metamellomai ← Hebrew (reverse map)

The `search_strongs.py --hebrew-source G3338` tool returns **no systematic Hebrew source** — confirming that metamellomai is **not a standardized LXX equivalent** for any single Hebrew word. Its OT footprint in Rahlfs is ~2 verses, but one of them is Psalm 109:4 — the verse the author of Hebrews quotes.

**Semantic shift in translation:** The LXX splits nacham into two Greek verbs along a clear semantic fault line:
- **παρακαλέω** when the sense is *console / comfort* (Piel, Pual, Hithpael of interpersonal comfort)
- **μετανοέω** when the sense is *change of mind / relent* (Niphal of divine or human relenting)
- **μεταμέλομαι** when the sense is *regret / care afterwards* — a narrower, more emotional "be sorry for what I did" nuance. The LXX translator of Psalm 109:4 chose this because the oath context requires the nuance "will not have afterward-regret / will not take it back," not merely "will not change mind." NT Hebrews preserves that exact choice.

## NT Usage (Greek)

| Strong's | Word | POS | Occurrences | Primary Meaning |
|----------|------|-----|-------------|-----------------|
| G3338 | μεταμέλομαι (metamellomai) | verb | 5 verses (6 forms) | regret, care afterwards, be sorry |
| G3340 | μετανοέω (metanoeō) | verb | 34 | change one's mind, repent |
| G3341 | μετάνοια (metanoia) | fem. noun | 22 | repentance, change of mind |
| G278 | ἀμεταμέλητος (ametamelētos) | adj. | 2 | not to be repented of, without regret (Rom 11:29; 2 Cor 7:10) |

### NT distribution of G3338

| Verse | Form | Subject | Sense |
|-------|------|---------|-------|
| Matt 21:29 | aor. pass. ptc. | son in parable | regret + course reversal (positive) |
| Matt 21:32 | aor. pass. | hearers of John | failed to regret + believe (negative) |
| Matt 27:3 | aor. pass. ptc. | Judas | regret without salvation |
| 2 Cor 7:8 (×2) | pres. mid. / impf. mid. | Paul | "I do not regret, though I did regret" |
| Heb 7:21 | fut. pass. | YHWH (quoting Ps 110:4 LXX) | "will not regret / take back" the oath |

**Key NT passages:**
- **Heb 7:21** — "The Lord sware and will not repent (οὐ μεταμεληθήσεται), Thou art a priest for ever after the order of Melchisedec." Direct LXX quotation of Ps 109:4.
- **Matt 27:3** — "Judas… when he saw that he was condemned, repented himself (μεταμεληθεὶς)" — emotional regret distinct from saving μετάνοια.
- **2 Cor 7:8–10** — Paul deliberately contrasts μεταμέλομαι (regret, v. 8) with μετάνοια (repentance unto salvation, v. 10) — "godly sorrow worketh repentance (μετάνοιαν) to salvation not to be repented of (ἀμεταμέλητον)." One passage, both words, explicit contrast.

## Direct OT→NT Quotations

| NT Verse | Quotes OT | Shared Word (Chain) | Significance |
|----------|-----------|---------------------|--------------|
| **Heb 7:21** | **Psa 110:4 (LXX 109:4)** | nacham (H5162) → metamellomai (G3338) | The load-bearing verse: God's oath-guaranteed Melchizedek priesthood is proven *irrevocable* because He "will not μεταμεληθήσεται" — i.e., will not have afterward-regret. The writer leans on the Greek verb's narrow "take-back" nuance to argue the priesthood's permanence. |
| Heb 6:17–18 (alluding) | Num 23:19 + Ps 110:4 | nacham → metanoeō/metamellomai | "two immutable things, in which it was impossible for God to lie" — the "God is not a man that he should repent" tradition feeds the oath argument. |
| Rom 11:29 (cognate) | echoes Num 23:19 / 1 Sam 15:29 | nacham → ἀμεταμέλητα (cognate of G3338) | "the gifts and calling of God are without repentance (ἀμεταμέλητα)" — same semantic field: God's commitments are not subject to afterward-regret. |

## Continuity and Shifts

**What stays the same across testaments:**
- **The "God does not repent" tradition** carries cleanly. Num 23:19 and 1 Sam 15:29 (MT: *lo'-nacham*) establish the axiom; Ps 110:4 applies it to an oath; Heb 7:21 cites that oath; Rom 11:29 restates the axiom with the adjective ἀμεταμέλητα. The Hebrew negation of nacham and the Greek negation of metamellomai serve the same theological function: divine fidelity cannot be withdrawn.
- **The emotional register of regret/being-sorry** survives. nacham's root sense ("to sigh, breathe strongly, be moved") aligns with metamellomai's "care afterwards." Matt 27:3 (Judas) and Gen 6:6 (God grieved) occupy the same emotional-grief zone.

**What shifts:**
- **LXX splits what Hebrew fuses.** One Hebrew verb nacham handles four distinct English senses (comfort / relent / regret / avenge). Greek resolves the ambiguity by selecting παρακαλέω, μετανοέω, or μεταμέλομαι depending on context. This splitting is usually theologically convenient but becomes load-bearing at Ps 110:4, where the translator's choice of μεταμέλομαι (not μετανοέω) gives Hebrews a narrower verb to exploit: "God does not *take back* an oath."
- **Hebrew paradox collapses into Greek precision.** The famous tension of 1 Sam 15 (the LORD repents he made Saul king, v.11, 35 — AND the LORD does not repent, v. 29) uses the same Hebrew verb both ways, forcing the reader to reconcile. In LXX Greek (μετανοέω/μεταμέλομαι vs. the negated form) the paradox is dampened by lexical choice, though translators are not always consistent.
- **In the NT, μεταμέλομαι never means salvation-repentance.** That role belongs exclusively to μετανοέω / μετάνοια (see WG-repent, TR-shuv-metanoeo). μεταμέλομαι in the NT is emotional regret (Judas, Matt 27:3) or course-correction short of faith (Matt 21:32) or Paul's literary "I was sorry / am not sorry" (2 Cor 7:8). Paul's explicit pairing in 2 Cor 7:10 formalizes the distinction: μετάνοια unto salvation is itself ἀμεταμέλητος — not subject to metamellomai-regret. The NT thus preserves the Septuagintal split and sharpens it.
- **Jer 18 / Joel 2:13 / Jon 3–4 use μετανοέω in LXX, not μεταμέλομαι.** These are the classical "God relents" conditional-mercy passages; their LXX rendering uses μετανοέω, which is why the NT doctrine of divine responsiveness to repentance travels on the μετανοέω chain, while Heb 7:21's argument travels on the μεταμέλομαι chain.

## See Also

- [G3340-metanoeo.md](G3340-metanoeo.md) — primary "repent" verb in NT; the other half of nacham's LXX split
- [WG-repent.md](WG-repent.md) — word group covering μετανοέω, μεταμέλομαι, ἐπιστρέφω, shuv, nacham
- TR-shuv-metanoeo (if present) — the other major Hebrew→Greek repentance chain
- Gen 6:6, Num 23:19, 1 Sam 15:11+29+35, Ps 110:4, Jer 18:8–10, Joel 2:13, Jon 3:9–10, 4:2, Matt 21:29+32, Matt 27:3, 2 Cor 7:8–10, Rom 11:29, Heb 6:17, Heb 7:21

---
*Generated from: search_strongs.py (--lxx-map H5162, --hebrew-source G3338, --lookup, --lexicon, --verses), gather_trace_data.py H5162 G3338, KJV text lookup.*
*Last updated: 2026-04-18*
