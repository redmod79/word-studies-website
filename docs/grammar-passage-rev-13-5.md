# Grammar Analysis: Revelation 13:5

## Text

**Greek (NA/N1904):** καὶ ἐδόθη αὐτῷ στόμα λαλοῦν μεγάλα καὶ βλασφημίας, καὶ ἐδόθη αὐτῷ ἐξουσία ποιῆσαι μῆνας τεσσεράκοντα δύο.

**KJV:** "And there was given unto him a mouth speaking great things and blasphemies; and power was given unto him to continue forty [and] two months."

## Word-by-Word Parsing

| # | Word | Lemma | Strong | Parsing | Gloss |
|---|------|-------|--------|---------|-------|
| 1 | καὶ | καί | G2532 | CONJ | and |
| 2 | ἐδόθη | δίδωμι | G1325 | V-API-3S (Aor Pass Ind 3Sg) | was given |
| 3 | αὐτῷ | αὐτός | G846 | P-DSN (Dat Sg) | to him |
| 4 | στόμα | στόμα | G4750 | N-NSN (Nom Sg) | a mouth |
| 5 | λαλοῦν | λαλέω | G2980 | V-PAP-NSN (Pres Act Ptcp Nom Sg) | speaking |
| 6 | μεγάλα | μέγας | G3173 | A-APN (Acc Pl Neut) | great [things] |
| 7 | καὶ | καί | G2532 | CONJ | and |
| 8 | βλασφημίας | βλασφημία | G988 | N-APF (Acc Pl Fem) | blasphemies |
| 9 | καὶ | καί | G2532 | CONJ | and |
| 10 | ἐδόθη | δίδωμι | G1325 | V-API-3S (Aor Pass Ind 3Sg) | was given |
| 11 | αὐτῷ | αὐτός | G846 | P-DSN (Dat Sg) | to him |
| 12 | ἐξουσία | ἐξουσία | G1849 | N-NSF (Nom Sg Fem) | authority |
| 13 | ποιῆσαι | ποιέω | G4160 | V-AAN (Aor Act Infinitive) | to act / to continue |
| 14 | μῆνας | μήν II | G3376 | N-APM (Acc Pl Masc) | months |
| 15 | τεσσεράκοντα | τεσσεράκοντα | G5062 | A-NUI (numeral) | forty |
| 16 | δύο | δύο | G1417 | A-NUI (numeral) | two |

(Directly from `python greek_parser.py --verse "REV 13:5"`.)

## Clause Structure

Two coordinate clauses, each built on the same verb ἐδόθη αὐτῷ ("was given to him"):

1. **Clause A:** καὶ ἐδόθη αὐτῷ στόμα λαλοῦν μεγάλα καὶ βλασφημίας
   - Main verb: ἐδόθη (aor pass ind 3sg)
   - Indirect object: αὐτῷ (dat)
   - Subject: στόμα (nom)
   - Attributive participle phrase modifying στόμα: λαλοῦν μεγάλα καὶ βλασφημίας
     - The participle λαλοῦν (nom sg neut) agrees with στόμα in gender, number, and case.
     - Two accusative objects of the participle: μεγάλα (neuter plural substantive, "great things") and βλασφημίας (fem pl, "blasphemies").

2. **Clause B:** καὶ ἐδόθη αὐτῷ ἐξουσία ποιῆσαι μῆνας τεσσεράκοντα [καὶ] δύο
   - Main verb: ἐδόθη
   - Indirect object: αὐτῷ
   - Subject: ἐξουσία (nom)
   - Complementary infinitive: ποιῆσαι ("to act / to continue")
   - Temporal accusative: μῆνας τεσσεράκοντα δύο ("forty-two months") — accusative of duration.

Structurally, the verse is a near-perfect parallelism: grant of **speech** (στόμα … λαλοῦν) paired with grant of **authority** (ἐξουσία … ποιῆσαι), both framed by the passive ἐδόθη αὐτῷ.

## Key Grammatical Features

### 1. ἐδόθη (×2) — Aorist Passive Indicative of δίδωμι

- **Form:** V-API-3S, lemma δίδωμι (G1325). Third singular aorist passive indicative, "was given."
- **Significance — divine passive:** In apocalyptic discourse (and broadly in Jewish Greek), ἐδόθη without an expressed agent typically functions as a *passivum divinum* — an agentless passive whose implicit subject is God. The act of "giving" is therefore not neutral permission but divine *grant* of a limited commission. The beast does not seize its mouth or its authority; both are handed to it under a sovereignty that also bounds them.
- **Repetition:** The verb is repeated verbatim at the head of each clause. The anaphora emphasizes that *every* capacity the beast exercises — speech and authority — is derivative and conferred, not autonomous.
- **Grammar reference:** (planned) `grammar-reference/greek/divine-passive.md`
- **Word study:** `word-studies/G1325-didomi.md`

### 2. λαλοῦν μεγάλα καὶ βλασφημίας — Present Active Participle (Attributive)

- **Form:** V-PAP-NSN, lemma λαλέω (G2980). Nominative singular neuter, agreeing with στόμα.
- **Attributive function:** The participle is anarthrous but functions as an attributive modifier of στόμα ("a mouth [that is] speaking…"). The present aspect portrays the speech as ongoing/characteristic, not punctiliar — this is what the mouth habitually does.
- **Two accusative objects coordinated by καί:**
  - μεγάλα (A-APN) — neuter plural substantivized adjective, "great things." Echoes Dan 7:8, 11, 20 LXX (στόμα λαλοῦν μεγάλα) where the same collocation describes the little horn; this is a direct intertextual citation.
  - βλασφημίας (N-APF) — "blasphemies," feminine accusative plural. Specifies the moral nature of the "great things" as speech against God (cf. Rev 13:6 next verse, which expands the content).
- **Word studies:** `word-studies/G2980-laleo.md`, `word-studies/G3173-megas.md`, `word-studies/G988-blasphemia.md`

### 3. ποιῆσαι — Aorist Active Infinitive of ποιέω

- **Form:** V-AAN, lemma ποιέω (G4160). Aorist active infinitive.
- **Syntactic role:** Complementary/epexegetical infinitive specifying the content or scope of the granted ἐξουσία ("authority … to ___"). Standard pattern: ἐξουσία + infinitive defines the sphere of authority.
- **The interpretive question — does ποιῆσαι govern an implicit object?**
  - **Option A ("to make war"):** Some witnesses — including the Textus Receptus tradition — read πόλεμον (or equivalent) after ποιῆσαι, yielding "to make war forty-two months." This reading harmonizes with v. 7 (ποιῆσαι πόλεμον μετὰ τῶν ἁγίων) and takes μῆνας τεσσεράκοντα δύο as duration of the warfare.
  - **Option B ("to continue / to act" absolutely):** The N1904 / NA / UBS text reads simply ποιῆσαι μῆνας τεσσεράκοντα δύο, with no object. In this construction ποιέω + accusative of time is a recognized idiom meaning "to spend (time)," "to stay," or "to continue." BDAG, s.v. ποιέω §4.2 ("to spend time, continue"), catalogues this precise usage.
  - **Parallels to the absolute / durative reading** (verified via `greek_parser.py`):
    - **Acts 15:33** — ποιήσαντες δὲ χρόνον ("having spent [some] time")
    - **Acts 20:3** — ποιήσας τε μῆνας τρεῖς ("and having stayed three months")
    - **Acts 18:23** — same idiom with χρόνον
    - **James 4:13** — ποιήσομεν ἐκεῖ ἐνιαυτόν ("we will spend there a year")
  - On Option B, the μῆνας accusative is not direct object but **accusative of duration**; the verse asserts not that the beast is granted authority to do some specific act for that period, but that its authorized tenure itself lasts 42 months. KJV "to continue forty [and] two months" reflects exactly this reading.
- **Grammar references:**
  - (planned) `grammar-reference/greek/aorist-infinitive-accusative-of-duration.md`
- **Word study:** `word-studies/G4160-poieo.md`

### 4. μῆνας τεσσεράκοντα [καὶ] δύο — Accusative of Duration

- **Form:** μῆνας is N-APM (lemma μήν II, G3376); τεσσεράκοντα (G5062) and δύο (G1417) are indeclinable numerals.
- **Syntax:** Accusative (μῆνας), not dative or genitive, signals *extent of time* ("for forty-two months") rather than point of time or within-which time. Greek regularly uses the accusative for the period *throughout which* an action obtains.
- **Textual detail on καί:** N1904 prints τεσσεράκοντα δύο (no conjunction). Other witnesses insert καί between the numerals (τεσσεράκοντα καὶ δύο); the sense is unaffected. The KJV "forty and two" reflects the καί reading (KJV bracketing noted above).
- **Duration equivalences within Revelation/Daniel:**
  - 42 months (Rev 11:2; 13:5)
  - 1,260 days (Rev 11:3; 12:6) — 42 × 30 days
  - "a time, and times, and half a time" (Rev 12:14; cf. Dan 7:25; 12:7) — 3½ "times"
  - All three expressions denote the same period across the apocalyptic symbol system.
- **Word study:** `word-studies/G3376-men.md`

### 5. Textual Variant: ποιῆσαι [πόλεμον]

- **Tools used:** `python greek_text_compare.py --verse "REV 13:5"` flagged divergence between N1904 and the TR underlying stream.
- **N1904:** καὶ ἐδόθη αὐτῷ ἐξουσία **ποιῆσαι** μῆνας τεσσεράκοντα δύο. (no object)
- **Variant stream:** Some minuscules (and witnesses reflected in later printed editions) add πόλεμον after ποιῆσαι, presumably harmonizing toward v. 7. The critical editions (NA28/UBS5) follow the shorter reading as more likely original, treating πόλεμον as a scribal clarification.
- **Exegetical upshot:** The two readings are not semantically opposed for any theological argument about the *period* (both yield "forty-two months"), but they differ on *what* the beast is empowered to do during the period:
  - Shorter reading: authority simply to *exist/operate* for 42 months (durative ποιέω).
  - Longer reading: authority to *wage war* for 42 months (transitive ποιέω + πόλεμον).
- Many modern versions (ESV, NASB, NIV) render along the lines of "to exercise authority for forty-two months," handling the infinitive as absolute or paraphrasing the durative idiom. KJV's "to continue" directly translates BDAG §4.2.

## Intertextual Grammar Notes

- **Daniel 7:8, 20, 25 (LXX / Theodotion):** The phrase στόμα λαλοῦν μεγάλα (Dan 7:8) is lexically and syntactically transplanted into Rev 13:5. The little horn's "mouth speaking great things" and its persecution "until a time and times and half a time" (Dan 7:25) supply *both* the language of clause A and the duration framework echoed in clause B.
- **Rev 11:2–3 // 12:6, 14 // 13:5:** The 42-month / 1,260-day / time-times-half-a-time cluster uses distinct grammatical constructions (ἐπί + acc., preposition + numeral, ellipsis + acc. of duration) but the same underlying interval. Rev 13:5 uses the bare accusative-of-duration form.

## Cross-References

- **Grammar library entries (existing):**
  - `grammar-reference/greek/mood-aorist-imperative.md` (related: aorist aspect in mood-forms)
  - `grammar-reference/greek/participle-legon-discourse.md` (related: participles of speech verbs)
- **Grammar library entries (planned — gaps identified by this analysis):**
  - `grammar-reference/greek/divine-passive.md` — for ἐδόθη as *passivum divinum*
  - `grammar-reference/greek/aorist-infinitive-accusative-of-duration.md` — for ποιῆσαι + μῆνας pattern (BDAG ποιέω §4.2)
- **Word studies:**
  - `word-studies/G1325-didomi.md` (δίδωμι)
  - `word-studies/G2980-laleo.md` (λαλέω)
  - `word-studies/G3173-megas.md` (μέγας)
  - `word-studies/G988-blasphemia.md` (βλασφημία)
  - `word-studies/G1849-exousia.md` (ἐξουσία)
  - `word-studies/G4160-poieo.md` (ποιέω)
  - `word-studies/G3376-men.md` (μήν, "month")
  - `word-studies/G4750-stoma.md` (στόμα)

## Tool Provenance

- Parsed via: `python greek_parser.py --verse "REV 13:5"` (Windows, D:/bible/tools/greek/)
- Textual comparison: `python greek_text_compare.py --verse "REV 13:5"` (N1904 vs. TR)
- Parallel idiom verification: `python greek_parser.py --verse "ACT 15:33"`, `"ACT 20:3"`, `"JAS 4:13"` — all attest ποιέω + accusative of time in the durative sense.
