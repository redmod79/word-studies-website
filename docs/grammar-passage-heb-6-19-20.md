# Grammar Analysis: Hebrews 6:19-20 (Anchor Within the Veil and the Forerunner High Priest)

**Mode:** Passage unit analysis (context-neutral)
**Scope:** Heb 6:19-20 as the conclusion of the oath/hope argument in Heb 6:13-18, with focus on the anchor metaphor, the phrase "within the veil," the forerunner language, and Christ's high-priestly identity after the order of Melchisedec.
**Aim:** Parser-verified word-by-word grammar; documentation of the load-bearing grammatical features: (a) the feminine relative pronoun ἣν referring back to ἐλπίς in v.18, (b) ἄγκυραν with agreeing accusative modifiers ἀσφαλῆ / βεβαίαν / εἰσερχομένην, (c) εἰς τὸ ἐσώτερον τοῦ καταπετάσματος as spatial sanctuary language, (d) εἰσῆλθεν as the finite aorist entry of Jesus the forerunner, and (e) γενόμενος ἀρχιερεύς as appositional priestly-status language. Grammar only; theological conclusions are deferred to downstream studies.

---

## 1. Text

| v. | Greek (parser output) | KJV |
|----|------------------------|-----|
| 19 | ἣν ὡς ἄγκυραν ἔχομεν τῆς ψυχῆς ἀσφαλῆ τε καὶ βεβαίαν καὶ εἰσερχομένην εἰς τὸ ἐσώτερον τοῦ καταπετάσματος, | Which [hope] we have as an anchor of the soul, both sure and stedfast, and which entereth into that within the veil; |
| 20 | ὅπου πρόδρομος ὑπὲρ ἡμῶν εἰσῆλθεν Ἰησοῦς, κατὰ τὴν τάξιν Μελχισέδεκ ἀρχιερεὺς γενόμενος εἰς τὸν αἰῶνα. | Whither the forerunner is for us entered, [even] Jesus, made an high priest for ever after the order of Melchisedec. |

---

## 2. Word-by-Word Parsing Tables (from `greek_parser.py`)

### Heb 6:19

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | ἣν | ὅς | G3739 | R-ASF (Acc Sg Fem relative pronoun) |
| 2 | ὡς | ὡς | G5613 | ADV (comparative marker, "as") |
| 3 | ἄγκυραν | ἄγκυρα | G45 | N-ASF (Acc Sg Fem, "anchor") |
| 4 | ἔχομεν | ἔχω | G2192 | V-PAI-1P (Pres Act Ind 1st Pl, "we have") |
| 5 | τῆς | ὁ | G3588 | T-GSF (Gen Sg Fem article) |
| 6 | ψυχῆς | ψυχή | G5590 | N-GSF (Gen Sg Fem, "of soul") |
| 7 | ἀσφαλῆ | ἀσφαλής | G804 | A-ASF (Acc Sg Fem, "sure/safe") |
| 8 | τε | τέ | G5037 | PRT (enclitic connective, "both") |
| 9 | καὶ | καί | G2532 | CONJ ("and") |
| 10 | βεβαίαν | βέβαιος | G949 | A-ASF (Acc Sg Fem, "steadfast/firm") |
| 11 | καὶ | καί | G2532 | CONJ ("and") |
| 12 | εἰσερχομένην | εἰσέρχομαι | G1525 | V-PNP-ASF (Pres M/P Ptcp Acc Sg Fem, "entering") |
| 13 | εἰς | εἰς | G1519 | PREP (+ accusative, motion into/toward) |
| 14 | τὸ | ὁ | G3588 | T-ASN (Acc Sg Neut article) |
| 15 | ἐσώτερον | ἐσώτερος | G2082 | A-ASN-C (Acc Sg Neut comparative adjective, substantival "the inner/within") |
| 16 | τοῦ | ὁ | G3588 | T-GSN (Gen Sg Neut article) |
| 17 | καταπετάσματος | καταπέτασμα | G2665 | N-GSN (Gen Sg Neut, "of the veil") |

### Heb 6:20

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | ὅπου | ὅπου | G3699 | ADV (locative relative adverb, "where/whither") |
| 2 | πρόδρομος | πρόδρομος | G4274 | A-NSM (Nom Sg Masc adjective used substantivally, "forerunner") |
| 3 | ὑπὲρ | ὑπέρ | G5228 | PREP (+ genitive, "on behalf of") |
| 4 | ἡμῶν | ἐγώ | G1473 | P-1GP (Gen Pl 1st person pronoun, "of us") |
| 5 | εἰσῆλθεν | εἰσέρχομαι | G1525 | V-2AAI-3S (2nd Aor Act Ind 3rd Sg, "entered") |
| 6 | Ἰησοῦς | Ἰησοῦς | G2424 | N-NSM (Nom Sg Masc, subject) |
| 7 | κατὰ | κατά | G2596 | PREP (+ accusative, norm/standard, "according to") |
| 8 | τὴν | ὁ | G3588 | T-ASF (Acc Sg Fem article) |
| 9 | τάξιν | τάξις | G5010 | N-ASF (Acc Sg Fem, "order/arrangement") |
| 10 | Μελχισέδεκ | Μελχισέδεκ | G3198 | N-PRI (indeclinable proper noun; parser marks Gen Sg M) |
| 11 | ἀρχιερεὺς | ἀρχιερεύς | G749 | N-NSM (Nom Sg Masc, "high priest") |
| 12 | γενόμενος | γίνομαι | G1096 | V-2ADP-NSM (2nd Aor Mid Deponent Ptcp Nom Sg Masc, "having become/being made") |
| 13 | εἰς | εἰς | G1519 | PREP (+ accusative, duration/resulting state) |
| 14 | τὸν | ὁ | G3588 | T-ASM (Acc Sg Masc article) |
| 15 | αἰῶνα | αἰών | G165 | N-ASM (Acc Sg Masc, "age/forever") |

---

## 3. Key Grammatical Features

### 3.1 ἣν ... ἔχομεν — Feminine Relative Pronoun Resuming "Hope"

**Form:** ἣν is accusative singular feminine (R-ASF). Its nearest grammatical antecedent is ἐλπίδος in Heb 6:18: τῆς προκειμένης ἐλπίδος ("the hope set before [us]"). The KJV supplies the antecedent in brackets: "Which [hope]."

**Syntax:** The relative pronoun functions as the direct object of ἔχομεν ("we have"). Its feminine gender matches ἐλπίς / ἐλπίδος, not ἄγκυραν by derivation. The sentence then uses ὡς ἄγκυραν as a comparative predicate-complement: "which hope we have as an anchor."

**Significance:** Grammatically, the anchor is not an independent subject introduced in v.19; it is the image applied to the already-mentioned hope from v.18. This keeps vv.19-20 attached to the previous sentence's "hope set before us" rather than beginning a detached sanctuary metaphor. The relative pronoun binds the whole anchor/veil/forerunner construction to the exhortational aim of Heb 6:18.

**Word studies:** [G1680-elpis](../../word-studies/G1680-elpis.md), [WG-hope](../../word-studies/WG-hope.md).

### 3.2 ἄγκυραν ... ἀσφαλῆ τε καὶ βεβαίαν καὶ εἰσερχομένην — Accusative Anchor with Coordinated Modifiers

**Form:** ἄγκυραν is accusative singular feminine (N-ASF). The two adjectives ἀσφαλῆ and βεβαίαν are also accusative singular feminine, agreeing with ἄγκυραν. The participle εἰσερχομένην is present middle/passive participle accusative singular feminine (V-PNP-ASF), likewise agreeing with ἄγκυραν / ἣν.

**Modifier chain:** The structure is:

| Element | Parsing | Function |
|---------|---------|----------|
| ἄγκυραν | N-ASF | comparative complement after ὡς |
| ἀσφαλῆ | A-ASF | first adjectival modifier, "sure/safe" |
| βεβαίαν | A-ASF | second adjectival modifier, "steadfast/firm" |
| εἰσερχομένην | V-PNP-ASF | participial modifier, "entering" |

The τε καὶ pair links ἀσφαλῆ and βεβαίαν as a coordinated adjective pair ("both sure and steadfast"). The following καὶ adds the participial description: the anchor-hope is not merely firm; it is characterized as entering into the inner space.

**Present participle:** εἰσερχομένην is present in aspect, not a finite verb. It presents the anchor-hope under the description of entering/going in. Because εἰσέρχομαι is deponent in the present middle/passive form, the M/P morphology should not be pressed as a passive; the lexeme normally carries active sense in middle form.

**Significance:** The grammar makes "entering within the veil" an attribute of the anchor-hope. The finite verb of the clause is ἔχομεν ("we have"), while εἰσερχομένην supplies the spatial direction of the image. The line of thought is: we have hope as an anchor; that anchor is sure and steadfast; that anchor is described as entering into the inner sanctuary space.

**Word studies:** [G45-ankyra](../../word-studies/G45-ankyra.md). Relevant grammar background: [greek/paired-middle-participles](../greek/paired-middle-participles.md) notes present M/P form ambiguity and deponent middle-only verbs such as ἔρχομαι; this verse has a single deponent present M/P participle, not the paired-participle construction treated there.

### 3.3 εἰς τὸ ἐσώτερον τοῦ καταπετάσματος — Motion Into the Interior of the Veil

**Form:** εἰς governs the accusative τὸ ἐσώτερον. ἐσώτερον is accusative singular neuter comparative adjective (A-ASN-C), substantivized by the article τὸ: "the inner [place/part]," KJV "that within." τοῦ καταπετάσματος is genitive singular neuter: "of the veil."

**Spatial syntax:** The construction is not simply "to the veil" but "into the inner [place] of the veil":

| Phrase | Parsing | Function |
|--------|---------|----------|
| εἰς | prep. + acc. | motion into/toward |
| τὸ ἐσώτερον | T-ASN + A-ASN-C | substantival comparative, "the more inward place / the interior" |
| τοῦ καταπετάσματος | T-GSN + N-GSN | genitive boundary/object, "of the veil" |

The genitive can be described as a boundary or reference genitive: the "inner" space is defined with respect to the veil. The comparative adjective ἐσώτερος marks an inward location relative to a boundary, not merely an abstract inwardness.

**Sanctuary vocabulary:** καταπέτασμα is the standard Greek term for the sanctuary veil/curtain in the NT. The existing word study notes that in Hebrews the genitive forms of καταπέτασμα occur in sanctuary-access phrases, including Heb 6:19 ("within the veil") and Heb 10:20 ("through the veil"). The translation-reference study links καταπέτασμα to Hebrew פֹּרֶכֶת (poreketh), the inner veil before the Most Holy Place.

**Significance:** The grammar gives a spatial sanctuary image: the anchor-hope is described as entering εἰς ("into") the inner region marked by the veil. The phrase is not grammatically vague devotional language; it is built from directional εἰς, a substantivized comparative adjective of interiority, and the genitive "of the veil."

**Word studies:** [G2082-esoteros](../../word-studies/G2082-esoteros.md), [G2665-katapetasma](../../word-studies/G2665-katapetasma.md), [TR-poreketh-katapetasma](../../word-studies/TR-poreketh-katapetasma.md), [WG-tabernacle](../../word-studies/WG-tabernacle.md), [WG-temple](../../word-studies/WG-temple.md).

### 3.4 ὅπου ... πρόδρομος ὑπὲρ ἡμῶν εἰσῆλθεν Ἰησοῦς — Locative Continuation and Aorist Entry

**Form:** ὅπου is a locative relative adverb, "where/whither," resuming the destination of v.19. εἰσῆλθεν is second aorist active indicative 3rd singular (V-2AAI-3S) from εἰσέρχομαι. Ἰησοῦς is nominative singular masculine, the subject. πρόδρομος is nominative singular masculine, an adjective used substantivally/predicatively, "forerunner."

**Clause structure:** The verbal core is:

> ὅπου ... εἰσῆλθεν Ἰησοῦς
> "where Jesus entered"

πρόδρομος stands in predicate/appositional relation to Ἰησοῦς: Jesus entered as forerunner. ὑπὲρ ἡμῶν is a prepositional phrase with ὑπέρ + genitive, "on behalf of us," placed before the finite verb and attached to the representative nature of the entry.

**Aorist entry vs. present participial entering:** Heb 6:19 uses εἰσερχομένην, a present participle modifying the anchor-hope. Heb 6:20 uses εἰσῆλθεν, a finite aorist indicative whose subject is Jesus. The grammar distinguishes the metaphorical description of hope/anchor from the completed entry of Jesus as forerunner. They share the same verb family, but not the same subject or verbal form.

**Significance:** The aorist finite verb presents Jesus' entry as a bounded completed event in the argument. The locative adverb ὅπου ties that event to the "within the veil" destination of v.19. The nominative πρόδρομος identifies the manner/status of the entrant: not merely one who entered, but one who entered ahead on behalf of others.

**Grammar reference:** [greek/aorist-active-indicative-narrative-chain](../greek/aorist-active-indicative-narrative-chain.md) covers finite aorist active indicatives as bounded event-line forms; Heb 6:20 is a single finite aorist entry statement, not a multi-verb chain.

**Word studies:** [G4274-prodromos](../../word-studies/G4274-prodromos.md), [G2424-Iesous](../../word-studies/G2424-Iesous.md), [WG-intercession](../../word-studies/WG-intercession.md).

### 3.5 κατὰ τὴν τάξιν Μελχισέδεκ ἀρχιερεὺς γενόμενος εἰς τὸν αἰῶνα — High-Priest Status and Duration

**Form:** κατὰ τὴν τάξιν is κατά + accusative, "according to the order/arrangement." τάξιν is accusative singular feminine (N-ASF). Μελχισέδεκ is an indeclinable proper name. ἀρχιερεύς is nominative singular masculine, "high priest." γενόμενος is second aorist middle deponent participle nominative singular masculine (V-2ADP-NSM) from γίνομαι. εἰς τὸν αἰῶνα is εἰς + accusative, idiomatically "unto the age / forever."

**Appositional participial structure:** The nominative cluster agrees with Ἰησοῦς:

| Element | Parsing | Function |
|---------|---------|----------|
| Ἰησοῦς | N-NSM | subject of εἰσῆλθεν |
| πρόδρομος | A-NSM | predicate/appositional title, "forerunner" |
| ἀρχιερεύς | N-NSM | predicate/appositional title, "high priest" |
| γενόμενος | V-2ADP-NSM | participial explanation, "having become / being made" |

The participle γενόμενος is best read as circumstantial/appositional: Jesus entered as forerunner, having become high priest according to the order of Melchisedec. The participle does not make "high priest" a separate finite assertion; it attaches priestly status to the subject of εἰσῆλθεν.

**Duration phrase:** εἰς τὸν αἰῶνα modifies the priestly-status clause: "high priest forever." The same phrase is central to the Psalm 110:4 citation that Hebrews develops in the surrounding argument ("Thou art a priest for ever after the order of Melchisedec," KJV).

**Significance:** The grammar joins three descriptors of Jesus in one nominative frame: forerunner, Jesus, high priest. The sanctuary entry of v.20 is therefore not generic access language; it is explicitly bound to high-priestly office and to the Melchisedec order formula.

**Word studies:** [G749-archiereus](../../word-studies/G749-archiereus.md), [G2409-hiereus](../../word-studies/G2409-hiereus.md), [TR-kohen-hiereus](../../word-studies/TR-kohen-hiereus.md), [G1096-ginomai](../../word-studies/G1096-ginomai.md), [G4274-prodromos](../../word-studies/G4274-prodromos.md), [WG-priests](../../word-studies/WG-priests.md), [WG-forever](../../word-studies/WG-forever.md).

---

## 4. Clause Structure

Heb 6:19-20 forms a relative continuation from v.18:

1. **Antecedent in v.18:** τῆς προκειμένης ἐλπίδος — "the hope set before [us]."
2. **Relative clause in v.19:** ἣν ... ἔχομεν — "which [hope] we have."
3. **Comparative complement:** ὡς ἄγκυραν τῆς ψυχῆς — "as an anchor of the soul."
4. **Coordinated modifiers of the anchor/hope:** ἀσφαλῆ τε καὶ βεβαίαν καὶ εἰσερχομένην — "both sure and steadfast and entering."
5. **Directional sanctuary phrase:** εἰς τὸ ἐσώτερον τοῦ καταπετάσματος — "into the inner [place] of the veil."
6. **Locative relative continuation in v.20:** ὅπου ... εἰσῆλθεν Ἰησοῦς — "where Jesus entered."
7. **Representative-forerunner frame:** πρόδρομος ὑπὲρ ἡμῶν — "as forerunner on behalf of us."
8. **Priestly apposition:** κατὰ τὴν τάξιν Μελχισέδεκ ἀρχιερεὺς γενόμενος εἰς τὸν αἰῶνα — "having become high priest forever according to the order of Melchisedec."

The passage has two finite verbs: ἔχομεν in v.19 and εἰσῆλθεν in v.20. The participles εἰσερχομένην and γενόμενος are subordinate modifiers. This prevents flattening the passage into one undifferentiated "entry" claim: hope/anchor is described by a present participle as entering; Jesus is the subject of a completed aorist entry as forerunner and high priest.

---

## 5. Similar Pattern Search

The Greek parser's `--similar` search returned no NT verses at similarity >= 0.6 for either Heb 6:19 or Heb 6:20.

| Target | Parser target pattern | Result |
|--------|-----------------------|--------|
| Heb 6:19 | R-ASF ADV N-ASF V-PAI-1P T-GSF N-GSF A-ASF PRT CONJ A-ASF CONJ V-PNP-ASF PREP T-ASN A-ASN-C T-GSN N-GSN | No verses found with similarity >= 0.6 |
| Heb 6:20 | ADV A-NSM PREP P-1GP V-2AAI-3S N-NSM PREP T-ASF N-ASF N-PRI N-NSM V-2ADP-NSM PREP T-ASM N-ASM | No verses found with similarity >= 0.6 |

This confirms that the exact syntactic profile is uncommon in the NT, especially the combined anchor metaphor, inner-veil spatial phrase, forerunner title, and Melchisedekian high-priest apposition.

---

## 6. Cross-References

### Grammar Library

- [greek/aorist-active-indicative-narrative-chain](../greek/aorist-active-indicative-narrative-chain.md) — for εἰσῆλθεν as a bounded aorist active indicative event form.
- [greek/paired-middle-participles](../greek/paired-middle-participles.md) — limited background for present M/P morphology and deponent middle-only verbs; Heb 6:19 has a single deponent present M/P participle, not this paired construction.
- [greek/genitive-of-quality-apposition](../greek/genitive-of-quality-apposition.md) — broad background for genitive analysis; Heb 6:19 specifically uses τοῦ καταπετάσματος as the genitive reference/boundary for τὸ ἐσώτερον.

### Word Studies

- [G1680-elpis](../../word-studies/G1680-elpis.md) — ἐλπίς, the antecedent of ἣν.
- [WG-hope](../../word-studies/WG-hope.md) — English word-group study for hope.
- [G45-ankyra](../../word-studies/G45-ankyra.md) — ἄγκυρα, anchor metaphor in Heb 6:19.
- [G2082-esoteros](../../word-studies/G2082-esoteros.md) — ἐσώτερος, "inner/within."
- [G2665-katapetasma](../../word-studies/G2665-katapetasma.md) — καταπέτασμα, sanctuary veil.
- [TR-poreketh-katapetasma](../../word-studies/TR-poreketh-katapetasma.md) — Hebrew פֹּרֶכֶת to Greek καταπέτασμα translation-reference bridge.
- [G4274-prodromos](../../word-studies/G4274-prodromos.md) — πρόδρομος, NT hapax "forerunner."
- [G749-archiereus](../../word-studies/G749-archiereus.md) — ἀρχιερεύς, high priest.
- [G2409-hiereus](../../word-studies/G2409-hiereus.md) — ἱερεύς, priest.
- [TR-kohen-hiereus](../../word-studies/TR-kohen-hiereus.md) — Hebrew כֹּהֵן to Greek ἱερεύς priestly bridge.
- [G1096-ginomai](../../word-studies/G1096-ginomai.md) — γίνομαι, γενόμενος in v.20.
- [WG-priests](../../word-studies/WG-priests.md) — English word-group study for priest language.
- [WG-intercession](../../word-studies/WG-intercession.md) — representative/on-behalf priestly ministry themes.
- [WG-tabernacle](../../word-studies/WG-tabernacle.md) — sanctuary/tabernacle vocabulary.
- [WG-temple](../../word-studies/WG-temple.md) — temple/sanctuary vocabulary.
- [WG-forever](../../word-studies/WG-forever.md) — εἰς τὸν αἰῶνα / forever language.

### Related Passage Analyses

- [heb-6-13-18](heb-6-13-18.md) — immediate preceding context: Abrahamic oath, two immutable things, and "hope set before us."
- [heb-8-1-2](heb-8-1-2.md) — Christ as high priest and minister of the heavenly sanctuary.
- [heb-9-11-22](heb-9-11-22.md) — Christ entering the greater/more perfect tabernacle and the holy places.

### Gaps Flagged

Grammar concept entries not yet present that would benefit from future canonical treatment:

- **greek/substantival-comparative-adjective** — for τὸ ἐσώτερον as article + comparative adjective used substantivally.
- **greek/relative-pronoun-antecedent-resumption** — for ἣν resuming an antecedent from the previous verse/sentence.
- **greek/predicate-appositional-nominative** — for πρόδρομος / ἀρχιερεύς in apposition to Ἰησοῦς.
- **greek/deponent-present-middle-passive-participle** — for εἰσερχομένην and similar M/P-form deponent participles with active sense.
