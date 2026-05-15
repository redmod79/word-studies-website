# Grammar Analysis: Hebrews 9:23-28 (Heavenly Purification, Once-for-All Offering, Judgment, and Second Appearing)

**Mode:** Passage unit analysis (context-neutral)  
**Scope:** Heb 9:23-28 as the concluding paragraph of the Hebrews 9 sanctuary argument: heavenly things purified with better sacrifices (v.23), Christ's entry into heaven itself and present appearing before God (v.24), the non-repetition of his self-offering (vv.25-26), the human appointment to death and judgment (v.27), and Christ's once-offered / second-appearing contrast (v.28).
**Study context supplied:** `sanctuary-service-unified-account`. Grammar only; theological synthesis belongs in the study that cites this reference.

---

## 1. Text (Greek parser output with KJV)

| v. | Greek | KJV |
|----|-------|-----|
| 23 | Ἀνάγκη οὖν τὰ μὲν ὑποδείγματα τῶν ἐν τοῖς οὐρανοῖς τούτοις καθαρίζεσθαι, αὐτὰ δὲ τὰ ἐπουράνια κρείττοσιν θυσίαις παρὰ ταύτας. | [It was] therefore necessary that the patterns of things in the heavens should be purified with these; but the heavenly things themselves with better sacrifices than these. |
| 24 | οὐ γὰρ εἰς χειροποίητα εἰσῆλθεν ἅγια Χριστός, ἀντίτυπα τῶν ἀληθινῶν, ἀλλ’ εἰς αὐτὸν τὸν οὐρανόν, νῦν ἐμφανισθῆναι τῷ προσώπῳ τοῦ Θεοῦ ὑπὲρ ἡμῶν· | For Christ is not entered into the holy places made with hands, [which are] the figures of the true; but into heaven itself, now to appear in the presence of God for us: |
| 25 | οὐδ’ ἵνα πολλάκις προσφέρῃ ἑαυτόν, ὥσπερ ὁ ἀρχιερεὺς εἰσέρχεται εἰς τὰ ἅγια κατ’ ἐνιαυτὸν ἐν αἵματι ἀλλοτρίῳ, | Nor yet that he should offer himself often, as the high priest entereth into the holy place every year with blood of others; |
| 26 | ἐπεὶ ἔδει αὐτὸν πολλάκις παθεῖν ἀπὸ καταβολῆς κόσμου· νυνὶ δὲ ἅπαξ ἐπὶ συντελείᾳ τῶν αἰώνων εἰς ἀθέτησιν τῆς ἁμαρτίας διὰ τῆς θυσίας αὐτοῦ πεφανέρωται. | For then must he often have suffered since the foundation of the world: but now once in the end of the world hath he appeared to put away sin by the sacrifice of himself. |
| 27 | καὶ καθ’ ὅσον ἀπόκειται τοῖς ἀνθρώποις ἅπαξ ἀποθανεῖν, μετὰ δὲ τοῦτο κρίσις, | And as it is appointed unto men once to die, but after this the judgment: |
| 28 | οὕτως καὶ ὁ Χριστός, ἅπαξ προσενεχθεὶς εἰς τὸ πολλῶν ἀνενεγκεῖν ἁμαρτίας, ἐκ δευτέρου χωρὶς ἁμαρτίας ὀφθήσεται τοῖς αὐτὸν ἀπεκδεχομένοις εἰς σωτηρίαν. | So Christ was once offered to bear the sins of many; and unto them that look for him shall he appear the second time without sin unto salvation. |

---

## 2. Word-by-Word Parsing (from `greek_parser.py`)

### Hebrews 9:23

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | Ἀνάγκη | ἀνάγκη | G318 | N-NSF — Nom Sg F |
| 2 | οὖν | οὖν | G3767 | CONJ |
| 3 | τὰ | ὁ | G3588 | T-APN — Acc Pl N |
| 4 | μὲν | μέν | G3303 | PRT |
| 5 | ὑποδείγματα | ὑπόδειγμα | G5262 | N-APN — Acc Pl N |
| 6 | τῶν | ὁ | G3588 | T-GPN — Gen Pl N |
| 7 | ἐν | ἐν | G1722 | PREP |
| 8 | τοῖς | ὁ | G3588 | T-DPM — Dat Pl M |
| 9 | οὐρανοῖς | οὐρανός | G3772 | N-DPM — Dat Pl M |
| 10 | τούτοις | οὗτος | G3778 | D-DPN — Dat Pl N |
| 11 | καθαρίζεσθαι | καθαρίζω | G2511 | **V-PPN — Pres Pass Inf** |
| 12 | αὐτὰ | αὐτός | G846 | P-APN — Acc Pl N |
| 13 | δὲ | δέ | G1161 | CONJ |
| 14 | τὰ | ὁ | G3588 | T-APN — Acc Pl N |
| 15 | ἐπουράνια | ἐπουράνιος | G2032 | A-APN — Acc Pl N |
| 16 | κρείττοσιν | κρείττων | G2909 | A-DPF-C — Dat Pl F Comparative |
| 17 | θυσίαις | θυσία | G2378 | N-DPF — Dat Pl F |
| 18 | παρὰ | παρά | G3844 | PREP |
| 19 | ταύτας | οὗτος | G3778 | D-APF — Acc Pl F |

**Verbal frame:** ἀνάγκη governs the infinitive καθαρίζεσθαι. The accusative noun phrases τὰ μὲν ὑποδείγματα and αὐτὰ δὲ τὰ ἐπουράνια function as the accusative subjects of the infinitive: "the patterns ... to be purified" / "the heavenly things themselves [to be purified]." The μέν ... δέ pairing marks a contrast between earthly copies and the heavenly realities. τούτοις is a dative of means/instrument ("with these"), while κρείττοσιν θυσίαις is another instrumental dative, modified by a comparative adjective and sharpened by παρά + accusative ("than these").

### Hebrews 9:24

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | οὐ | οὐ | G3756 | PRT-N |
| 2 | γὰρ | γάρ | G1063 | CONJ |
| 3 | εἰς | εἰς | G1519 | PREP |
| 4 | χειροποίητα | χειροποίητος | G5499 | A-APN — Acc Pl N |
| 5 | εἰσῆλθεν | εἰσέρχομαι | G1525 | **V-2AAI-3S — Aor Act Ind 3sg** |
| 6 | ἅγια | ἅγιος | G40 | A-APN — Acc Pl N |
| 7 | Χριστός | Χριστός | G5547 | N-NSM — Nom Sg M |
| 8 | ἀντίτυπα | ἀντίτυπος | G499 | A-APN — Acc Pl N |
| 9 | τῶν | ὁ | G3588 | T-GPN — Gen Pl N |
| 10 | ἀληθινῶν | ἀληθινός | G228 | A-GPN — Gen Pl N |
| 11 | ἀλλ’ | ἀλλά | G235 | CONJ |
| 12 | εἰς | εἰς | G1519 | PREP |
| 13 | αὐτὸν | αὐτός | G846 | P-ASM — Acc Sg M |
| 14 | τὸν | ὁ | G3588 | T-ASM — Acc Sg M |
| 15 | οὐρανόν | οὐρανός | G3772 | N-ASM — Acc Sg M |
| 16 | νῦν | νῦν | G3568 | ADV |
| 17 | ἐμφανισθῆναι | ἐμφανίζω | G1718 | **V-APN — Aor Pass Inf** |
| 18 | τῷ | ὁ | G3588 | T-DSN — Dat Sg N |
| 19 | προσώπῳ | πρόσωπον | G4383 | N-DSN — Dat Sg N |
| 20 | τοῦ | ὁ | G3588 | T-GSM — Gen Sg M |
| 21 | Θεοῦ | θεός | G2316 | N-GSM — Gen Sg M |
| 22 | ὑπὲρ | ὑπέρ | G5228 | PREP |
| 23 | ἡμῶν | ἐγώ | G1473 | P-1GP — Gen Pl |

**Verbal frame:** εἰσῆλθεν is the finite verb: Christ "entered" as a completed aorist event. The οὐ ... ἀλλ' contrast negates entry into χειροποίητα ἅγια and affirms entry εἰς αὐτὸν τὸν οὐρανόν. ἀντίτυπα τῶν ἀληθινῶν is appositional to the handmade holy places: "antitypical/corresponding copies of the true." The aorist passive infinitive ἐμφανισθῆναι gives the present purpose/result of the entry: "now to appear / be manifested" before God's face, with ὑπὲρ ἡμῶν marking representative action "on behalf of us."

### Hebrews 9:25

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | οὐδ’ | οὐδέ | G3761 | CONJ-N |
| 2 | ἵνα | ἵνα | G2443 | CONJ |
| 3 | πολλάκις | πολλάκις | G4178 | ADV |
| 4 | προσφέρῃ | προσφέρω | G4374 | **V-PAS-3S — Pres Act Subj 3sg** |
| 5 | ἑαυτόν | ἑαυτοῦ | G1438 | F-3ASM — Acc Sg M |
| 6 | ὥσπερ | ὥσπερ | G5618 | ADV |
| 7 | ὁ | ὁ | G3588 | T-NSM — Nom Sg M |
| 8 | ἀρχιερεὺς | ἀρχιερεύς | G749 | N-NSM — Nom Sg M |
| 9 | εἰσέρχεται | εἰσέρχομαι | G1525 | **V-PNI-3S — Pres Mid/Pass Ind 3sg** |
| 10 | εἰς | εἰς | G1519 | PREP |
| 11 | τὰ | ὁ | G3588 | T-APN — Acc Pl N |
| 12 | ἅγια | ἅγιος | G40 | A-APN — Acc Pl N |
| 13 | κατ’ | κατά | G2596 | PREP |
| 14 | ἐνιαυτὸν | ἐνιαυτός | G1763 | N-ASM — Acc Sg M |
| 15 | ἐν | ἐν | G1722 | PREP |
| 16 | αἵματι | αἷμα | G129 | N-DSN — Dat Sg N |
| 17 | ἀλλοτρίῳ | ἀλλότριος | G245 | A-DSN — Dat Sg N |

**Verbal frame:** οὐδ' ἵνα negates a purpose construction: Christ did not enter "in order that" he might repeatedly offer himself. προσφέρῃ is present active subjunctive, so the negated idea is repeated or ongoing offering, reinforced by πολλάκις. The comparison ὥσπερ introduces the earthly high priest's customary pattern. εἰσέρχεται is present indicative with customary force, further defined by κατ' ἐνιαυτόν ("year by year") and ἐν αἵματι ἀλλοτρίῳ ("with another's blood").

### Hebrews 9:26

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | ἐπεὶ | ἐπεί | G1893 | CONJ |
| 2 | ἔδει | δεῖ | G1163 | **V-IAI-3S — Impf Act Ind 3sg** |
| 3 | αὐτὸν | αὐτός | G846 | P-ASM — Acc Sg M |
| 4 | πολλάκις | πολλάκις | G4178 | ADV |
| 5 | παθεῖν | πάσχω | G3958 | **V-2AAN — Aor Act Inf** |
| 6 | ἀπὸ | ἀπό | G575 | PREP |
| 7 | καταβολῆς | καταβολή | G2602 | N-GSF — Gen Sg F |
| 8 | κόσμου | κόσμος | G2889 | N-GSM — Gen Sg M |
| 9 | νυνὶ | νυνί | G3570 | ADV |
| 10 | δὲ | δέ | G1161 | CONJ |
| 11 | ἅπαξ | ἅπαξ | G530 | ADV |
| 12 | ἐπὶ | ἐπί | G1909 | PREP |
| 13 | συντελείᾳ | συντέλεια | G4930 | N-DSF — Dat Sg F |
| 14 | τῶν | ὁ | G3588 | T-GPM — Gen Pl M |
| 15 | αἰώνων | αἰών | G165 | N-GPM — Gen Pl M |
| 16 | εἰς | εἰς | G1519 | PREP |
| 17 | ἀθέτησιν | ἀθέτησις | G115 | N-ASF — Acc Sg F |
| 18 | τῆς | ὁ | G3588 | T-GSF — Gen Sg F |
| 19 | ἁμαρτίας | ἁμαρτία | G266 | N-GSF — Gen Sg F |
| 20 | διὰ | διά | G1223 | PREP |
| 21 | τῆς | ὁ | G3588 | T-GSF — Gen Sg F |
| 22 | θυσίας | θυσία | G2378 | N-GSF — Gen Sg F |
| 23 | αὐτοῦ | αὐτός | G846 | P-GSM — Gen Sg M |
| 24 | πεφανέρωται | φανερόω | G5319 | **V-RPI-3S — Perf Pass Ind 3sg** |

**Verbal frame:** ἐπεὶ ἔδει ... παθεῖν states the consequence that would follow if repeated offering were required: repeated suffering from the foundation of the world. ἔδει is imperfect active indicative in an unrealized / counterfactual explanatory frame. νυνὶ δὲ marks the actual contrast: "but now." ἅπαξ supplies the once-only adverbial frame. πεφανέρωται is perfect passive indicative: Christ "has appeared / has been manifested" with the result still standing in view. εἰς ἀθέτησιν τῆς ἁμαρτίας gives the aim/result of the appearing, while διὰ τῆς θυσίας αὐτοῦ supplies the means.

### Hebrews 9:27

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | καὶ | καί | G2532 | CONJ |
| 2 | καθ’ | κατά | G2596 | PREP |
| 3 | ὅσον | ὅσος | G3745 | K-ASN — Acc Sg N |
| 4 | ἀπόκειται | ἀπόκειμαι | G606 | **V-PNI-3S — Pres Mid/Pass Ind 3sg** |
| 5 | τοῖς | ὁ | G3588 | T-DPM — Dat Pl M |
| 6 | ἀνθρώποις | ἄνθρωπος | G444 | N-DPM — Dat Pl M |
| 7 | ἅπαξ | ἅπαξ | G530 | ADV |
| 8 | ἀποθανεῖν | ἀποθνῄσκω | G599 | **V-2AAN — Aor Act Inf** |
| 9 | μετὰ | μετά | G3326 | PREP |
| 10 | δὲ | δέ | G1161 | CONJ |
| 11 | τοῦτο | οὗτος | G3778 | D-ASN — Acc Sg N |
| 12 | κρίσις | κρίσις | G2920 | N-NSF — Nom Sg F |

**Verbal frame:** καθ' ὅσον introduces the comparison that v.28 completes with οὕτως καί. ἀπόκειται is a present middle/passive indicative meaning "is laid up / appointed." The dative τοῖς ἀνθρώποις marks those for whom the appointment stands. ἅπαξ modifies the aorist infinitive ἀποθανεῖν: "to die once." μετὰ δὲ τοῦτο κρίσις is a verbless clause: "and after this, judgment."

### Hebrews 9:28

| # | Word | Lemma | Strong's | Parsing |
|---|------|-------|----------|---------|
| 1 | οὕτως | οὕτω | G3779 | ADV |
| 2 | καὶ | καί | G2532 | CONJ |
| 3 | ὁ | ὁ | G3588 | T-NSM — Nom Sg M |
| 4 | Χριστός | Χριστός | G5547 | N-NSM — Nom Sg M |
| 5 | ἅπαξ | ἅπαξ | G530 | ADV |
| 6 | προσενεχθεὶς | προσφέρω | G4374 | **V-APP-NSM — Aor Pass Ptcp Nom Sg M** |
| 7 | εἰς | εἰς | G1519 | PREP |
| 8 | τὸ | ὁ | G3588 | T-ASN — Acc Sg N |
| 9 | πολλῶν | πολύς | G4183 | A-GPM — Gen Pl M |
| 10 | ἀνενεγκεῖν | ἀναφέρω | G399 | **V-2AAN — Aor Act Inf** |
| 11 | ἁμαρτίας | ἁμαρτία | G266 | N-APF — Acc Pl F |
| 12 | ἐκ | ἐκ | G1537 | PREP |
| 13 | δευτέρου | δεύτερος | G1208 | A-GSN — Gen Sg N |
| 14 | χωρὶς | χωρίς | G5565 | ADV |
| 15 | ἁμαρτίας | ἁμαρτία | G266 | N-GSF — Gen Sg F |
| 16 | ὀφθήσεται | ὁράω | G3708 | **V-FPI-3S — Fut Pass Ind 3sg** |
| 17 | τοῖς | ὁ | G3588 | T-DPM — Dat Pl M |
| 18 | αὐτὸν | αὐτός | G846 | P-ASM — Acc Sg M |
| 19 | ἀπεκδεχομένοις | ἀπεκδέχομαι | G553 | **V-PNP-DPM — Pres Mid/Pass Ptcp Dat Pl M** |
| 20 | εἰς | εἰς | G1519 | PREP |
| 21 | σωτηρίαν | σωτηρία | G4991 | N-ASF — Acc Sg F |

**Verbal frame:** οὕτως καί completes the analogy begun in v.27. Christ, like humanity, has a once-for-all death/offering horizon marked by ἅπαξ, but the second half of the analogy diverges: humanity has "after this, judgment"; Christ "will appear a second time ... unto salvation." προσενεχθείς is an aorist passive participle: "having been offered." εἰς τὸ ... ἀνενεγκεῖν is an articular infinitive construction of purpose/result: "in order to bear / carry up the sins of many." ὀφθήσεται is future passive indicative, "he will be seen / will appear." τοῖς ... ἀπεκδεχομένοις is a substantival present participle, "to the ones waiting for him." εἰς σωτηρίαν gives the goal of the second appearing.

---

## 3. Key Grammatical Features

### 1. Ἀνάγκη + accusative subjects + present passive infinitive (v.23)

- **Form:** ἀνάγκη + accusative noun phrases + καθαρίζεσθαι (`V-PPN`, present passive infinitive).
- **Function:** The construction expresses necessity: the patterns and the heavenly things are placed under the same infinitival predicate, "to be purified." The μέν ... δέ contrast distinguishes the two objects of purification, not two unrelated arguments.
- **Significance for this passage:** The grammar does not make "heavenly things" a stray appositional aside. αὐτὰ δὲ τὰ ἐπουράνια is an accusative subject coordinated with τὰ μὲν ὑποδείγματα under the governing ἀνάγκη. This is the load-bearing syntax behind the KJV's "but the heavenly things themselves."
- **References:** word studies [G2511 καθαρίζω](../../word-studies/G2511-katharizo.md), [G2032 ἐπουράνιος](../../word-studies/G2032-epouranios.md), [G2378 θυσία](../../word-studies/G2378-thysia.md), [WG-cleansing](../../word-studies/WG-cleansing.md), [WG-sacrifice](../../word-studies/WG-sacrifice.md).

### 2. οὐ ... ἀλλ' entry contrast and ἐμφανισθῆναι (v.24)

- **Form:** οὐ γὰρ εἰς χειροποίητα ... ἀλλ' εἰς αὐτὸν τὸν οὐρανόν; main verb εἰσῆλθεν (`V-2AAI-3S`); infinitive ἐμφανισθῆναι (`V-APN`).
- **Function:** The aorist εἰσῆλθεν treats Christ's entry as a completed event. The οὐ ... ἀλλ' construction makes the location contrast explicit: not handmade holy places, but heaven itself. ἐμφανισθῆναι expresses the present purpose/result of that entry: to appear before God's face on behalf of us.
- **Significance for this passage:** The syntax ties heavenly entry to present appearing before God. The grammar does not merely say Christ "went somewhere"; it presents a completed entry with an ongoing representative orientation, marked by νῦν and ὑπὲρ ἡμῶν.
- **References:** word studies [G499 ἀντίτυπος](../../word-studies/G499-antitypon.md), [G1718 ἐμφανίζω](../../word-studies/G1718-emphanizo.md), [WG-appearing](../../word-studies/WG-appearing.md), [WG-temple](../../word-studies/WG-temple.md).

### 3. Negated repeated offering versus once-only manifestation (vv.25-26)

- **Form:** οὐδ' ἵνα πολλάκις προσφέρῃ (`V-PAS-3S`, present active subjunctive); ὥσπερ ... εἰσέρχεται (`V-PNI-3S`, customary present); ἔδει ... πολλάκις παθεῖν; νυνὶ δὲ ἅπαξ ... πεφανέρωται (`V-RPI-3S`, perfect passive indicative).
- **Function:** The negated ἵνα clause rejects repeated self-offering. The high priest's repeated yearly pattern is expressed with the present εἰσέρχεται plus κατ' ἐνιαυτόν. The counterfactual consequence is stated with ἔδει ... παθεῖν: if repeated offering were needed, repeated suffering would follow. The actual contrast is νυνὶ δὲ ἅπαξ: "but now once." The perfect πεφανέρωται presents the appearing as accomplished with abiding result.
- **Significance for this passage:** The once-for-all logic is not built on the noun "sacrifice" alone. It is carried by repeated adverbs and verbal aspect: πολλάκις is denied twice, while ἅπαξ is asserted. The perfect indicative then gives the present standing significance of the once-only appearing.
- **Grammar references:** [greek/tense-perfect-indicative](../greek/tense-perfect-indicative.md), [greek/tense-perfect](../greek/tense-perfect.md), [greek/tense-present-active-indicative](../greek/tense-present-active-indicative.md).
- **Word studies:** [G4374 προσφέρω](../../word-studies/G4374-prosphero.md), [G5319 φανερόω](../../word-studies/G5319-phaneroo.md), [G530 ἅπαξ](../../word-studies/G530-hapax.md), [G115 ἀθέτησις](../../word-studies/G115-athetesis.md), [G266 ἁμαρτία](../../word-studies/G266-hamartia.md), [WG-offerup](../../word-studies/WG-offerup.md), [WG-atonement](../../word-studies/WG-atonement.md), [WG-sin](../../word-studies/WG-sin.md).

### 4. καθ' ὅσον ... οὕτως καί analogy: death, judgment, and second appearing (vv.27-28)

- **Form:** καθ' ὅσον ἀπόκειται ... ἅπαξ ἀποθανεῖν ... κρίσις; οὕτως καὶ ὁ Χριστός ... ὀφθήσεται.
- **Function:** καθ' ὅσον introduces the human side of the comparison: an appointment to die once, followed by judgment. οὕτως καί introduces the Christ side: he was once offered and will appear a second time. The comparison is structurally tight, but not identical in outcome: the human clause ends with κρίσις; the Christ clause ends εἰς σωτηρίαν.
- **Significance for this passage:** κρίσις is not grammatically attached to Christ's second appearing as its goal; it belongs to the human side of the comparison in v.27. In v.28, the goal phrase is εἰς σωτηρίαν, and the dative participial phrase τοῖς ... ἀπεκδεχομένοις identifies the beneficiaries as "those waiting for him."
- **References:** word studies [G2920 κρίσις](../../word-studies/G2920-krisis.md), [WG-judgment](../../word-studies/WG-judgment.md). No canonical word study for G4991 σωτηρία is present in the library at time of writing.

### 5. προσενεχθείς + εἰς τὸ ἀνενεγκεῖν + ὀφθήσεται (v.28)

- **Form:** προσενεχθείς (`V-APP-NSM`, aorist passive participle), εἰς τὸ ... ἀνενεγκεῖν (`V-2AAN`, articular aorist infinitive), ὀφθήσεται (`V-FPI-3S`, future passive indicative), ἀπεκδεχομένοις (`V-PNP-DPM`, present participle).
- **Function:** The aorist passive participle summarizes the completed offering: "having been offered once." The articular infinitive gives the purpose/result: "to bear the sins of many." The future passive indicative points forward to a second appearing. The present participle describes the continuing posture of those who wait for him.
- **Significance for this passage:** The syntax separates the sin-bearing event from the second appearing. The first appearing/offering is associated with ἁμαρτίας as the object borne; the second appearing is χωρὶς ἁμαρτίας and εἰς σωτηρίαν. Grammatically, χωρὶς ἁμαρτίας modifies the second appearing by negation of association: "apart from sin," not "without sinning."
- **Grammar reference:** [greek/divine-passive](../greek/divine-passive.md) is relevant as a category for agentless passives, though Heb 9:28 should be handled carefully because the immediate context also speaks of Christ offering himself.
- **Word studies:** [G4374 προσφέρω](../../word-studies/G4374-prosphero.md), [G399 ἀναφέρω](../../word-studies/G399-anaphero.md), [G266 ἁμαρτία](../../word-studies/G266-hamartia.md), [WG-appearing](../../word-studies/WG-appearing.md).

---

## 4. Clause and Argument Structure

1. **v.23 necessity statement:** ἀνάγκη governs one infinitival purification frame with two contrasted accusative subjects.
2. **v.24 entry explanation:** γάρ explains v.23 by contrasting earthly handmade holy places with heaven itself; Christ's entry has the purpose/result of appearing before God for us.
3. **vv.25-26 non-repetition argument:** οὐδ' ἵνα rejects repeated self-offering; ἐπεὶ introduces the unacceptable consequence of repeated suffering; νυνὶ δὲ ἅπαξ asserts the actual once-only appearing.
4. **vv.27-28 analogy and contrast:** καθ' ὅσον gives the human pattern: once to die, then judgment. οὕτως καί gives the Christological pattern: once offered to bear sins, then second appearing apart from sin unto salvation.

The Greek parser's `--similar` search found no NT verses at similarity >= 0.6 for either Heb 9:23 or Heb 9:28, so the passage's full morphosyntactic sequence appears distinctive in the parser corpus.

---

## 5. Cross-References

**Grammar library:**

- [Perfect Tense - Indicative Mood](../greek/tense-perfect-indicative.md) — πεφανέρωται in v.26.
- [Perfect Tense](../greek/tense-perfect.md) — broader perfect-tense reference.
- [Present Active Indicative](../greek/tense-present-active-indicative.md) — customary present force relevant to the high priest's yearly εἰσέρχεται in v.25.
- [Divine Passive](../greek/divine-passive.md) — category relevant for evaluating agentless passive forms, especially ἐμφανισθῆναι, προσενεχθείς, and ὀφθήσεται; application must be context-controlled.
- [Comparative Adjective with Definite Article](../greek/comparative-adjective-with-article.md) — comparative morphology background for κρείττοσιν, though Heb 9:23 uses anarthrous comparative adjective + noun rather than article + comparative.

**Word studies:**

- [G2511 καθαρίζω](../../word-studies/G2511-katharizo.md) — "purify / cleanse" in v.23.
- [G2032 ἐπουράνιος](../../word-studies/G2032-epouranios.md) — "heavenly" in v.23.
- [G2378 θυσία](../../word-studies/G2378-thysia.md) — "sacrifice" in vv.23, 26.
- [G499 ἀντίτυπος](../../word-studies/G499-antitypon.md) — "figures / antitypes" in v.24.
- [G1718 ἐμφανίζω](../../word-studies/G1718-emphanizo.md) — "appear / manifest" in v.24.
- [G4374 προσφέρω](../../word-studies/G4374-prosphero.md) — "offer" in vv.25, 28.
- [G5319 φανερόω](../../word-studies/G5319-phaneroo.md) — "appear / manifest" in v.26.
- [G530 ἅπαξ](../../word-studies/G530-hapax.md) — "once" in vv.26-28.
- [G115 ἀθέτησις](../../word-studies/G115-athetesis.md) — "putting away / annulment" in v.26.
- [G266 ἁμαρτία](../../word-studies/G266-hamartia.md) — "sin(s)" in vv.26, 28.
- [G2920 κρίσις](../../word-studies/G2920-krisis.md) — "judgment" in v.27.
- [G399 ἀναφέρω](../../word-studies/G399-anaphero.md) — "bear / offer up" in v.28.
- [G40 ἅγιος](../../word-studies/G40-hagios.md), [G129 αἷμα](../../word-studies/G129-haima.md), [G749 ἀρχιερεύς](../../word-studies/G749-archiereus.md) — sanctuary-service vocabulary supporting vv.24-25.

**Word-group studies:**

- [WG-cleansing](../../word-studies/WG-cleansing.md)
- [WG-appearing](../../word-studies/WG-appearing.md)
- [WG-atonement](../../word-studies/WG-atonement.md)
- [WG-blood](../../word-studies/WG-blood.md)
- [WG-judgment](../../word-studies/WG-judgment.md)
- [WG-offerup](../../word-studies/WG-offerup.md)
- [WG-priests](../../word-studies/WG-priests.md)
- [WG-sacrifice](../../word-studies/WG-sacrifice.md)
- [WG-sin](../../word-studies/WG-sin.md)
- [WG-temple](../../word-studies/WG-temple.md)

---

## 6. Parser Commands Used

```powershell
cd D:/bible/tools/greek
python greek_parser.py --verse "HEB 9:23"
python greek_parser.py --verse "HEB 9:24"
python greek_parser.py --verse "HEB 9:25"
python greek_parser.py --verse "HEB 9:26"
python greek_parser.py --verse "HEB 9:27"
python greek_parser.py --verse "HEB 9:28"
python greek_parser.py --similar "HEB 9:23" --min-sim 0.6 --limit 5
python greek_parser.py --similar "HEB 9:28" --min-sim 0.6 --limit 5
```

KJV source: `D:/bible/tools/data/kjv.txt`, lines matching `Hebrews 9:23-28`.
