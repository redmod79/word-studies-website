# Grammar Analysis: 1 John 2:18–23 (with 4:1–3; 2 Jn 1:7)

Scope: all five NT occurrences of ἀντίχριστος (Strong's G500), which are the complete Johannine dossier for the term. This analysis is context-neutral; it documents the lexical, morphological, and syntactic data without adopting any particular identification of the antichrist figure in later traditions.

---

## 1. The Complete Johannine Dossier

`greek_parser.py --lemma "ἀντίχριστος"` returns exactly five hits — all in the Johannine epistles:

| # | Reference | Form | Parsing | Syntactic Role |
|---|-----------|------|---------|----------------|
| 1 | 1 John 2:18a | ἀντίχριστος | [N-NSM] Nom Sg M — **anarthrous** | Subject of ἔρχεται ("cometh") |
| 2 | 1 John 2:18b | ἀντίχριστοι | [N-NPM] Nom Pl M — **anarthrous** | Subject of γεγόνασιν ("are become / now exist") |
| 3 | 1 John 2:22 | ὁ ἀντίχριστος | [N-NSM] Nom Sg M — **articular** | Predicate noun of οὗτός ἐστιν |
| 4 | 1 John 4:3 | τοῦ ἀντιχρίστου | [N-GSM] Gen Sg M — **articular** | Genitive modifier of elided πνεῦμα |
| 5 | 2 John 1:7 | ὁ ἀντίχριστος | [N-NSM] Nom Sg M — **articular** | Second predicate noun joined by καί |

Note: ἀντίχριστος occurs **only** in 1 John and 2 John. It appears nowhere else in the NT — not in 2 Thessalonians, not in Revelation, not in the Synoptics. Any systematic correlation with 2 Thess 2 "man of lawlessness" or Revelation's beast-figures is **an exegetical inference from thematic parallels**, not a lexical identity.

**Word study reference:** [G500-antichristos](../../word-studies/G500-antichristos.md)
**Related textual issue:** [textual-variant-2thess-2-3](../greek/textual-variant-2thess-2-3.md)

---

## 2. 1 John 2:18 — Prophecy Heard + Present Fulfillment

**Greek (NA/Crit):** Παιδία, ἐσχάτη ὥρα ἐστίν, καὶ καθὼς ἠκούσατε ὅτι ἀντίχριστος ἔρχεται, καὶ νῦν ἀντίχριστοι πολλοὶ γεγόνασιν· ὅθεν γινώσκομεν ὅτι ἐσχάτη ὥρα ἐστίν.

**KJV:** Little children, it is the last time: and as ye have heard that antichrist shall come, even now are there many antichrists; whereby we know that it is the last time.

### Parsing Table (verse 18)

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | Παιδία | παιδίον | G3813 | N-VPN (Voc Pl N) |
| 2 | ἐσχάτη | ἔσχατος | G2078 | A-NSF-S |
| 3 | ὥρα | ὥρα | G5610 | N-NSF |
| 4 | ἐστίν | εἰμί | G1510 | V-PAI-3S |
| 5 | καὶ | καί | G2532 | CONJ |
| 6 | καθὼς | καθώς | G2531 | ADV |
| 7 | ἠκούσατε | ἀκούω | G191 | **V-AAI-2P** (Aor Act Ind 2Pl) |
| 8 | ὅτι | ὅτι | G3754 | CONJ (content) |
| 9 | **ἀντίχριστος** | ἀντίχριστος | G500 | **N-NSM, anarthrous** |
| 10 | ἔρχεται | ἔρχομαι | G2064 | **V-PNI-3S** (Pres M/P Ind 3Sg) |
| 11 | καὶ | καί | G2532 | CONJ |
| 12 | νῦν | νῦν | G3568 | ADV |
| 13 | **ἀντίχριστοι** | ἀντίχριστος | G500 | **N-NPM, anarthrous** |
| 14 | πολλοὶ | πολύς | G4183 | A-NPM |
| 15 | **γεγόνασιν** | γίνομαι | G1096 | **V-2RAI-3P** (Perf Act Ind 3Pl) |
| 16 | ὅθεν | ὅθεν | G3606 | ADV (inferential) |
| 17 | γινώσκομεν | γινώσκω | G1097 | V-PAI-1P |
| 18 | ὅτι | ὅτι | G3754 | CONJ |
| 19 | ἐσχάτη | ἔσχατος | G2078 | A-NSF-S |
| 20 | ὥρα | ὥρα | G5610 | N-NSF |
| 21 | ἐστίν | εἰμί | G1510 | V-PAI-3S |

### Key Grammatical Features — 2:18

**(a) ἠκούσατε (V-AAI-2P) + ὅτι-content clause: "ye have heard that…"**
Aorist indicative 2nd plural — the audience has, at some specifiable point in the past, received teaching about a coming figure. The ὅτι introduces the content of that teaching. John is **quoting received tradition**, not originating it. The form of that tradition is not expanded here, but the fact that he can invoke it as common knowledge ("as ye have heard") shows it was pre-existing catechesis in the Johannine community.

**(b) ἀντίχριστος ἔρχεται — anarthrous singular + present indicative "cometh"**
Two features interlock:
- **Anarthrous** (no definite article): functions as a categorical/quality designator rather than pointing to a specific known individual ("an antichrist-figure is coming" / "antichrist, as a category, is coming"). Greek anarthrous predicates in prophecy commonly have this generalizing force.
- **Present indicative ἔρχεται**: the "futuristic present" idiom used of expected/scheduled eschatological arrivals (cf. Matt 17:11 Ἠλίας ἔρχεται; Rev 1:7 ἔρχεται μετὰ τῶν νεφελῶν). Grammatically present, referentially future-oriented. The KJV "shall come" captures the force correctly.

**(c) νῦν ἀντίχριστοι πολλοὶ γεγόνασιν — "now many antichrists have come to be"**
- νῦν: temporal adverb anchoring to the present moment of writing.
- ἀντίχριστοι (plural, anarthrous): **John pluralises his own term**. This is the decisive lexical move. The single coming figure of tradition is paired with multiple present manifestations.
- γεγόνασιν (**Perfect active indicative**, from γίνομαι): state-resultant perfect. They have come into being and the resulting state persists — "have appeared and now exist." The perfect tense makes the present reality of these figures the grammatical emphasis, not merely the fact of their past emergence.

**(d) The καθὼς … καί … νῦν structure: prophecy → fulfillment pattern**
καθώς introduces the tradition ("as ye have heard that [X]"); the second καί + νῦν introduces the present state ("and now [Y has happened]"). This is a comparison/correspondence structure: what was heard as future is being actualized — though not exhausted — in the present plurality. John does **not** say the singular prophecy is cancelled by the plural fulfillment; the aorist "ye have heard" stays on the books while γεγόνασιν describes the current situation.

**(e) ὅθεν γινώσκομεν ὅτι ἐσχάτη ὥρα ἐστίν — inferential**
ὅθεν ("whence, from which"): inference particle. The plurality of antichrists **is** the evidence for ἐσχάτη ὥρα ("last hour"). Grammatically, the deniers are not the precursors of the last hour — they are its identifying marker.

---

## 3. 1 John 2:19 — The Departure

**Greek:** ἐξ ἡμῶν ἐξῆλθαν, ἀλλ᾽ οὐκ ἦσαν ἐξ ἡμῶν· εἰ γὰρ ἐξ ἡμῶν ἦσαν, μεμενήκεισαν ἂν μεθ᾽ ἡμῶν· ἀλλ᾽ ἵνα φανερωθῶσιν ὅτι οὐκ εἰσὶν πάντες ἐξ ἡμῶν.

**KJV:** They went out from us, but they were not of us; for if they had been of us, they would [no doubt] have continued with us: but [they went out], that they might be made manifest that they were not all of us.

### Key Features — 2:19

| Word | Parsing | Note |
|------|---------|------|
| ἐξῆλθαν | V-2AAI-3P | **Aorist active ind.** — punctiliar past departure |
| ἦσαν | V-IAI-3P | **Imperfect** — continuous past state ("were not [ever] of us") |
| ἦσαν (εἰ γὰρ) | V-IAI-3P | Imperfect in protasis of 2nd-class condition |
| μεμενήκεισαν | **V-LAI-3P** (**Pluperfect act. ind.**) | apodosis of contrary-to-fact cond. — "they would have remained" |
| ἂν | PRT | modal particle marking the apodosis as hypothetical |
| φανερωθῶσιν | V-APS-3P | **Aorist passive subjunctive** in ἵνα clause — "that they might be manifested" |
| εἰσὶν | V-PAI-3P | Present — "they are not of us" as present reality |

**(a) Second-class contrary-to-fact condition** (εἰ + imperfect ἦσαν … μεμενήκεισαν ἂν): "If they had been [but they were not] of us, they would have remained [but they did not]." The pluperfect μεμενήκεισαν is rare in the NT and emphatically locates the non-remaining as a completed fact with continuing result.

**(b) ἵνα φανερωθῶσιν** — purpose/result of the departure. Aorist passive subjunctive: "that they be manifested" (**divine passive** implication — cf. [divine-passive](../greek/divine-passive.md) — the manifestation is providentially directed). Grammatically, the schism serves a revelatory function.

**(c) Antecedent of "they"**: the subject of ἐξῆλθαν is the ἀντίχριστοι πολλοί of v.18. V.19 thus identifies the "many antichrists" as former insiders — their "going out" (ἐξῆλθαν) is the historical correlate of their "coming into being" (γεγόνασιν).

---

## 4. 1 John 2:20–21 — The Anointing and the Truth

**Greek (v.20):** καὶ ὑμεῖς χρῖσμα ἔχετε ἀπὸ τοῦ Ἁγίου, καὶ οἴδατε πάντες.
**Greek (v.21):** οὐκ ἔγραψα ὑμῖν ὅτι οὐκ οἴδατε τὴν ἀλήθειαν, ἀλλ᾽ ὅτι οἴδατε αὐτήν, καὶ ὅτι πᾶν ψεῦδος ἐκ τῆς ἀληθείας οὐκ ἔστιν.

**KJV (v.20):** But ye have an unction from the Holy One, and ye know all things.
**KJV (v.21):** I have not written unto you because ye know not the truth, but because ye know it, and that no lie is of the truth.

### Key Features — 2:20–21

- **χρῖσμα** (N-ASN, G5545): "anointing, unguent." Lexical play on Χριστός (the Anointed) / ἀντίχριστος. Those who have the χρῖσμα are positionally opposite the ἀντί-χριστος faction. John exploits the cognate relationship: Christ is anointed, his people have the anointing, against-the-anointed-one is the opposing pole.
- **ἔχετε** (Pres Act Ind 2Pl): durative possession of the anointing — present and ongoing.
- **οἴδατε** (V-RAI-2P, Perfect act. ind. of οἶδα): Perfect in form, present in meaning — "ye know." Used three times across vv.20–21, reinforcing the community's settled epistemic standing.
- **ἔγραψα** (V-AAI-1S, Aor): epistolary aorist — "I write" from the sender's viewpoint, "I have written" from the recipient's. Marks meta-commentary on the letter itself.

---

## 5. 1 John 2:22 — The Definition

**Greek:** Τίς ἐστιν ὁ ψεύστης εἰ μὴ ὁ ἀρνούμενος ὅτι Ἰησοῦς οὐκ ἔστιν ὁ Χριστός; οὗτός ἐστιν ὁ ἀντίχριστος, ὁ ἀρνούμενος τὸν Πατέρα καὶ τὸν Υἱόν.

**KJV:** Who is a liar but he that denieth that Jesus is the Christ? He is antichrist, that denieth the Father and the Son.

### Parsing Table (verse 22)

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | Τίς | τίς | G5101 | I-NSM (interrog.) |
| 2 | ἐστιν | εἰμί | G1510 | V-PAI-3S |
| 3 | ὁ | ὁ | G3588 | T-NSM |
| 4 | ψεύστης | ψεύστης | G5583 | N-NSM |
| 5 | εἰ μὴ | εἰ + μή | G1487/G3361 | COND + PRT-N ("except, if not") |
| 6 | ὁ | ὁ | G3588 | T-NSM |
| 7 | **ἀρνούμενος** | ἀρνέομαι | G720 | **V-PNP-NSM** (Pres M/P Ptcp) |
| 8 | ὅτι | ὅτι | G3754 | CONJ (content) |
| 9 | Ἰησοῦς | Ἰησοῦς | G2424 | N-NSM |
| 10 | οὐκ | οὐ | G3756 | PRT-N |
| 11 | ἔστιν | εἰμί | G1510 | V-PAI-3S |
| 12 | ὁ | ὁ | G3588 | T-NSM |
| 13 | Χριστός | Χριστός | G5547 | N-NSM |
| 14 | οὗτός | οὗτος | G3778 | D-NSM |
| 15 | ἐστιν | εἰμί | G1510 | V-PAI-3S |
| 16 | **ὁ ἀντίχριστος** | ἀντίχριστος | G500 | **N-NSM, articular** |
| 17 | ὁ | ὁ | G3588 | T-NSM |
| 18 | ἀρνούμενος | ἀρνέομαι | G720 | V-PNP-NSM |
| 19 | τὸν Πατέρα | πατήρ | G3962 | N-ASM |
| 20 | καὶ | καί | G2532 | CONJ |
| 21 | τὸν Υἱόν | υἱός | G5207 | N-ASM |

### Key Grammatical Features — 2:22

**(a) ὁ ἀρνούμενος — articular present participle (substantive use)**
The articular participle functions as a substantival noun: "the one who is denying." Present aspect = ongoing, characteristic activity. This is the defining description; it names a type of person by their continuous action. The same construction repeats twice in v.22, forming an envelope:

> *ὁ ἀρνούμενος ὅτι Ἰησοῦς οὐκ ἔστιν ὁ Χριστός … ὁ ἀρνούμενος τὸν Πατέρα καὶ τὸν Υἱόν*

**(b) ὅτι … οὐκ ἔστιν — the "redundant/pleonastic οὐ" after a verb of denial**
The surface construction looks like a double negative ("denies that Jesus is NOT the Christ"). In Greek, verbs of denying / preventing / doubting frequently take a redundant οὐ in the complement clause. BDF §429 and Wallace (pp. 756–767) treat this as emphatic reinforcement: "denies that Jesus [is the] Christ" is the meaning, not "denies that Jesus is not the Christ." The KJV translators handled this correctly by rendering "denieth that Jesus is the Christ" (dropping the pleonastic negative).

Note: some witnesses omit the οὐκ; the bracketed apparatus retains it as the lectio difficilior. Either way, the sense is identical.

**(c) οὗτός ἐστιν ὁ ἀντίχριστος — equative copular clause with DEFINITE PREDICATE**
- οὗτος (D-NSM): anaphoric demonstrative, pointing back to the denier.
- ὁ ἀντίχριστος: **articular** predicate — "this one is THE antichrist." Colwell's rule does not apply (both subject and predicate are articular), so the identification is mutually convertible: the denier = the antichrist, and the antichrist = the denier.

This is the **definitional verse** for the term in Johannine usage. Grammatically, John provides a two-sided equation:

```
"Jesus-is-not-the-Christ"-denier  ≡  ὁ ἀντίχριστος  ≡  Father-and-Son-denier
```

Whatever else is later predicated of "antichrist" from other texts (2 Thess, Rev, etc.), **in John's own lexical stipulation**, the term is defined by Christological and Binitarian denial — it is a fundamentally theological/confessional category, not primarily a political or eschatological-figure category.

**(d) τὸν Πατέρα καὶ τὸν Υἱόν — expansion of the denial**
Denying Jesus-as-Christ = denying both the Father and the Son. Grammatically linked by simple καί. The logic: the Son is only "Son" in relation to the Father; to deny the Son (Jesus is not the Christ) is to deny the relational structure that includes the Father. V.23 then makes this explicit: πᾶς ὁ ἀρνούμενος τὸν Υἱὸν οὐδὲ τὸν Πατέρα ἔχει.

---

## 6. 1 John 2:23 — The Corollary

**Greek:** πᾶς ὁ ἀρνούμενος τὸν Υἱὸν οὐδὲ τὸν Πατέρα ἔχει· ὁ ὁμολογῶν τὸν Υἱὸν καὶ τὸν Πατέρα ἔχει.

**KJV:** Whosoever denieth the Son, the same hath not the Father: [(but) he that acknowledgeth the Son hath the Father also].

### Key Features — 2:23

- **πᾶς ὁ ἀρνούμενος / ὁ ὁμολογῶν**: articular present participles again, this time paired as opposites — denying (ἀρνέομαι) vs. confessing (ὁμολογέω). Both are substantival.
- **Balanced antithetical parallelism**: the two halves are grammatical mirror images. One clause with ἀρνούμενος + οὐδέ + ἔχει (negating possession), one with ὁμολογῶν + καί + ἔχει (affirming possession).
- The second half was disputed in some Byzantine witnesses (bracketed in the KJV); NA/Crit editions include it without brackets.

---

## 7. 1 John 4:1–3 — The Pneumatological Extension

### Parsing Summary — 4:1

| Word | Parsing | Note |
|------|---------|------|
| Ἀγαπητοί | A-VPM | vocative of address |
| μὴ … πιστεύετε | V-PAM-2P | **Present imperative with μή** — "stop believing / do not continue believing" (often progressive-prohibitive force) |
| δοκιμάζετε | V-PAM-2P | Present imperative positive — "keep testing" |
| πνεύματα | N-APN | "spirits" (neuter plural) |
| πολλοὶ ψευδοπροφῆται | A-NPM + N-NPM | "many false prophets" |
| ἐξεληλύθασιν | **V-2RAI-3P** (Perfect) | "have gone out [and still are out]" — same perfect-state logic as γεγόνασιν in 2:18 |

### Parsing Summary — 4:2

| Word | Parsing | Note |
|------|---------|------|
| γινώσκετε | V-PAI-2P (or PAM-2P) | "ye know" / "know ye" — form ambiguous |
| πᾶν πνεῦμα | A-NSN + N-NSN | "every spirit" |
| ὃ ὁμολογεῖ | R-NSN + V-PAI-3S | relative clause, pres. act. ind. — "which confesses" |
| Ἰησοῦν Χριστὸν ἐν σαρκὶ ἐληλυθότα | double acc. + **V-2RAP-ASM** | Perfect active participle in accusative — modifies Ἰησοῦν Χριστὸν; see below |

### Parsing Summary — 4:3

| Word | Parsing | Note |
|------|---------|------|
| πᾶν πνεῦμα ὃ μὴ ὁμολογεῖ | A-NSN T R-NSN PRT-N V-PAI-3S | "every spirit which confesses not" |
| τὸν Ἰησοῦν | T-ASM N-ASM | (NA reads τὸν Ἰησοῦν; TR expands "that Jesus Christ is come in the flesh" — major variant) |
| τοῦτό ἐστιν τὸ τοῦ **ἀντιχρίστου** | D-NSN + V-PAI-3S + T-NSN + T-GSM + N-GSM | "this is the [spirit] of the antichrist" |
| ὃ ἀκηκόατε ὅτι ἔρχεται | R + V-2RAI-2P-ATT + CONJ + V-PNI-3S | "which ye have heard that it is coming" |
| νῦν ἐν τῷ κόσμῳ ἐστὶν ἤδη | ADV + PREP + T-DSM + N-DSM + V-PAI-3S + ADV | "now is in the world already" |

### Key Grammatical Features — 4:1–3

**(a) ἐληλυθότα (V-2RAP-ASM) — perfect active participle, accusative, modifying Ἰησοῦν Χριστὸν**
This is a double-accusative object-complement construction after ὁμολογεῖ: "confesses Jesus Christ [as having] come in the flesh." The **perfect active participle** ἐληλυθότα signals a **past coming whose effects abide** — the incarnation is a completed event with ongoing consequence. See [participle-perfect-passive-state](../greek/participle-perfect-passive-state.md) for the parallel semantic logic of the Greek perfect (active vs. passive, both share the state-result aspect).

The confessional formula is not "Jesus Christ came in the flesh" (simple past) but "Jesus Christ has come, and remains come, in the flesh." The perfect aspect **guards against docetic denial**, which is John's grammatical target here.

**(b) τὸ τοῦ ἀντιχρίστου — articular neuter with genitive: "the [spirit] of the antichrist"**
The article τό is neuter singular, picking up πνεῦμα from vv.1–2 by ellipsis: "this is the [πνεῦμα] of the antichrist." The antichrist is a **genitive qualifier**, not the subject. Grammatically this yields "the antichrist-spirit" or "the spirit that belongs to / comes from the antichrist" — the **spirit characteristic of the antichrist** rather than the antichrist figure himself.

Possible genitive classifications (context-neutral):
- **Genitive of source**: the spirit that comes from / originates from the antichrist.
- **Genitive of quality/attribute**: the antichrist-type spirit.
- **Possessive genitive**: the spirit that belongs to the antichrist.
The Greek does not decide between these; all three are grammatically licit. What the genitive **does** grammatically foreclose is flat identification: "spirit of antichrist" ≠ "the antichrist himself."

**(c) ὃ ἀκηκόατε ὅτι ἔρχεται — recapitulation of 2:18**
- ἀκηκόατε (**V-2RAI-2P-ATT**, perfect active indicative, Attic reduplication): "ye have heard" with perfect-state force. Upgrades the 2:18 aorist ἠκούσατε to a perfect — "ye have heard [and still carry that tradition]."
- ὅτι ἔρχεται: same verb and tense as 2:18. The traditional formula is quoted verbatim.
- νῦν ἐν τῷ κόσμῳ ἐστὶν ἤδη: "now is in the world already." Triple temporal emphasis (νῦν + ἤδη + present ἐστίν) pressing the current-operation point.

The 2:18 pattern ("heard that X comes / now X is here") is **repeated almost word-for-word** in 4:3, now applied to the **spirit** of antichrist rather than the persons.

**(d) παντὶ πνεύματι … τὰ πνεύματα — the plural ontology of spirits**
πνεῦμα in 4:1–3 is **countable and plural** ("every spirit … the spirits … every spirit"). This is continuous with the plurality of 2:18 (ἀντίχριστοι πολλοί): John's schema operates with multiple individuated deceiving agents, not a single monolithic figure in the present tense. The testing verb δοκιμάζετε (pres. imp.) treats spirit-discernment as an ongoing community practice.

---

## 8. 2 John 1:7 — Pairing and Closure

**Greek:** ὅτι πολλοὶ πλάνοι ἐξῆλθον εἰς τὸν κόσμον, οἱ μὴ ὁμολογοῦντες Ἰησοῦν Χριστὸν ἐρχόμενον ἐν σαρκί· οὗτός ἐστιν ὁ πλάνος καὶ ὁ ἀντίχριστος.

**KJV:** For many deceivers are entered into the world, who confess not that Jesus Christ is come in the flesh. This is a deceiver and an antichrist.

### Key Grammatical Features — 2 Jn 1:7

| Word | Parsing | Note |
|------|---------|------|
| πολλοὶ πλάνοι | A-NPM + A-NPM | "many deceivers" — plural again |
| ἐξῆλθον | V-2AAI-3P | **Aorist** (vs. perfect ἐξεληλύθασιν in 1 Jn 4:1) — here the departure is reported as completed event, not state |
| οἱ μὴ ὁμολογοῦντες | T-NPM + PRT-N + V-PAP-NPM | articular present participle plural: "those who do not confess" |
| Ἰησοῦν Χριστὸν ἐρχόμενον ἐν σαρκί | N-ASM + N-ASM + **V-PNP-ASM** | **present** participle ἐρχόμενον (not perfect as in 1 Jn 4:2) |
| οὗτός ἐστιν ὁ πλάνος καὶ ὁ ἀντίχριστος | D-NSM + V-PAI-3S + T-NSM + N-NSM + CONJ + T-NSM + N-NSM | "this one is the deceiver and the antichrist" |

**(a) ἐρχόμενον (present) vs. ἐληλυθότα (perfect) at 1 Jn 4:2**
Same book-cluster, same context, same basic formula — but here the participle is **present**, not perfect. Two scholarly readings:
- Same referent, different tense: present participle generalized to the confession as such ("Jesus Christ [who is] coming in flesh"), encompassing both the incarnation and any future mode of flesh-coming.
- A second-coming extension: if the present is futuristic ("is [to be] coming"), then the confessional test extends to Christ's future parousia in flesh, not only the first incarnation.
Either reading is grammatically defensible; the tense shift is lexical data, not proof of either reading.

**(b) οὗτός ἐστιν ὁ πλάνος καὶ ὁ ἀντίχριστος — paired articular predicates**
Two articular predicate nouns joined by καί. The grammar invites Granville Sharp territory — but note: GS rule applies most strictly when both nouns share a single article (τὸν πλάνον καὶ ἀντίχριστον) and are personal singulars of a certain class. Here both nouns **have their own article** (ὁ πλάνος καὶ ὁ ἀντίχριστος), which signals **co-reference without collapsing** — "this same person is [both] the deceiver and the antichrist." Two labels for one referent.

**(c) ὁ πλάνος (singular, articular) after πλάνοι (plural)**
Grammatical move parallel to 1 Jn 2:22: start with a plural group (πολλοὶ πλάνοι), then single out a representative category-noun with the article (ὁ πλάνος). Each individual deceiver **is** "the deceiver"; each is also **"the antichrist."** The singular article does not imply there is only one — it denotes the category instantiated.

---

## 9. Consolidated Grammatical Findings

### 9.1 Anarthrous singular vs. articular singular vs. plural

| Pattern | Passage | Greek | Function |
|---------|---------|-------|----------|
| **Anarthrous singular** (prophetic) | 1 Jn 2:18a | ἀντίχριστος ἔρχεται | futuristic-present / categorical coming-figure of pre-existing tradition |
| **Anarthrous plural** (present reality) | 1 Jn 2:18b | ἀντίχριστοι πολλοί | multiple present manifestations |
| **Articular singular (predicate)** | 1 Jn 2:22 | ὁ ἀντίχριστος | definitional equation: the denier ≡ the antichrist |
| **Articular genitive (attributive)** | 1 Jn 4:3 | τὸ τοῦ ἀντιχρίστου | pneumatological — "the [spirit] of the antichrist" |
| **Articular singular (paired predicate)** | 2 Jn 1:7 | ὁ πλάνος καὶ ὁ ἀντίχριστος | co-referenced category labels for each deceiver |

### 9.2 The perfect-tense "already-fulfilled" pattern

Three perfects converge on the "antichrist is already operating" point:

- 1 Jn 2:18: ἀντίχριστοι πολλοὶ **γεγόνασιν** (V-2RAI-3P) — "have come into being [and exist now]"
- 1 Jn 4:1: πολλοὶ ψευδοπροφῆται **ἐξεληλύθασιν** (V-2RAI-3P) — "have gone out [and are out now]"
- 1 Jn 4:3: ὃ **ἀκηκόατε** ὅτι ἔρχεται (V-2RAI-2P-ATT) — "which ye have heard that it is coming" — with "now in the world already" (νῦν … ἐστὶν ἤδη)

All three use the perfect to collapse the gap between a traditionally "future" expectation and the community's present experience.

### 9.3 Defining verbs: ἀρνέομαι and ὁμολογέω

The antichrist is defined by verbs, not by apocalyptic imagery:

| Verb | Occurrences in scope | Parsing |
|------|----------------------|---------|
| **ἀρνέομαι** (G720, "deny") | 1 Jn 2:22 (2×), 2:23 (1×) | V-PNP-NSM — articular pres. ptcp. substantive |
| **ὁμολογέω** (G3670, "confess") | 1 Jn 2:23 (ὁμολογῶν), 4:2 (ὁμολογεῖ), 4:3 (μὴ ὁμολογεῖ), 2 Jn 1:7 (μὴ ὁμολογοῦντες) | Various — mostly articular participles |

The ἀντίχριστος is grammatically constructed as the **negation pole** of ὁμολογέω-Christology: where faithful spirits confess ("Jesus Christ [having] come in the flesh"), antichrist-spirits refuse that confession.

### 9.4 Context-neutral observation on bridge to 2 Thess 2

The user's stated correlation note: 2 Thess 2:7 τὸ μυστήριον ἤδη ἐνεργεῖται τῆς ἀνομίας ("the mystery of lawlessness already works") structurally parallels the Johannine "already" pattern (νῦν … γεγόνασιν, νῦν … ἐστὶν ἤδη). Grammatically both authors use present/perfect indicatives to report a currently-operating evil that traditional eschatology had framed as future. This is a **structural-grammatical parallel**, not a lexical identification — Paul uses ὁ ἄνομος / ὁ ἄνθρωπος τῆς ἀνομίας, John uses ἀντίχριστος; the words are different, and any theological correlation must argue from more than lexis. See [textual-variant-2thess-2-3](../greek/textual-variant-2thess-2-3.md) for the ἁμαρτίας/ἀνομίας issue at the Pauline end.

---

## 10. Cross-References

**Grammar library:**
- [participle-perfect-passive-state](../greek/participle-perfect-passive-state.md) — aspect-logic for ἐληλυθότα (perfect active) parallels the perfect passive discussion
- [divine-passive](../greek/divine-passive.md) — for φανερωθῶσιν (2:19) providential-manifestation sense
- [textual-variant-2thess-2-3](../greek/textual-variant-2thess-2-3.md) — the Pauline counterpart figure and its TR/NA variant

**Word studies:**
- [G500-antichristos](../../word-studies/G500-antichristos.md) — lexical and etymological coverage
- [G5547-christos](../../word-studies/G5547-christos.md) — the positive term ἀντίχριστος negates
- [TR-mashiyach-christos](../../word-studies/TR-mashiyach-christos.md) — Messiah/Christ translation history
- [G480-antikeimai](../../word-studies/G480-antikeimai.md) — the ἀντι- prefix and "opposer" semantic field (including 2 Thess 2:4 ὁ ἀντικείμενος)

**Passage analyses:**
- [rev-13-1-10](rev-13-1-10.md) — Revelation's beast-figure grammar (separate lexical field; no ἀντίχριστος)
- [rev-13-3](rev-13-3.md), [rev-13-5](rev-13-5.md) — related Revelation parsings
