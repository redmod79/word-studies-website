# Grammar Analysis: Deuteronomy 7:1–6 — The Seven-Nations Ḥerem Command

**"When YHWH brings you in… and casts out seven nations… you shall utterly devote them to destruction"**

Moses' first full exposition of the conquest mandate: a protasis-apodosis structure in which YHWH's own *causative* bringing-in and dispossession ground Israel's *imperfective* obligations to strike, devote-to-destruction, cut off covenant, withhold favor, avoid intermarriage, and demolish cult paraphernalia — all rooted in Israel's status as chosen ("holy people, treasured possession"). The passage is a tightly knit chain of **Hiphil imperfects** and **weqatal perfects consecutive**, built on the theological-grammatical principle that God's causation precedes and enables Israel's obedience. This entry parses all six verses, documents the BHSA clause structure, analyzes the *paronomastic infinitive absolute* in 7:2, the three לֹא-prohibitions, and the Qal perfect of divine election in 7:6.

---

## Text

**Hebrew (BHS / ETCBC):**

> **7:1** כִּ֤י יְבִֽיאֲךָ֙ יְהוָ֣ה אֱלֹהֶ֔יךָ אֶל־הָאָ֕רֶץ אֲשֶׁר־אַתָּ֥ה בָא־שָׁ֖מָּה לְרִשְׁתָּ֑הּ וְנָשַׁ֣ל גֹּֽויִם־רַבִּ֣ים ׀ מִפָּנֶ֡יךָ הַֽחִתִּי֩ וְהַגִּרְגָּשִׁ֨י וְהָאֱמֹרִ֜י וְהַכְּנַעֲנִ֣י וְהַפְּרִזִּ֗י וְהַֽחִוִּי֙ וְהַיְבוּסִ֔י שִׁבְעָ֣ה גֹויִ֔ם רַבִּ֥ים וַעֲצוּמִ֖ים מִמֶּֽךָּ׃
>
> **7:2** וּנְתָנָ֞ם יְהוָ֧ה אֱלֹהֶ֛יךָ לְפָנֶ֖יךָ וְהִכִּיתָ֑ם הַחֲרֵ֤ם תַּחֲרִים֙ אֹתָ֔ם לֹא־תִכְרֹ֥ת לָהֶ֛ם בְּרִ֖ית וְלֹ֥א תְחָנֵּֽם׃
>
> **7:3** וְלֹ֥א תִתְחַתֵּ֖ן בָּ֑ם בִּתְּךָ֙ לֹא־תִתֵּ֣ן לִבְנֹ֔ו וּבִתֹּ֖ו לֹא־תִקַּ֥ח לִבְנֶֽךָ׃
>
> **7:4** כִּֽי־יָסִ֤יר אֶת־בִּנְךָ֙ מֵֽאַחֲרַ֔י וְעָבְד֖וּ אֱלֹהִ֣ים אֲחֵרִ֑ים וְחָרָ֤ה אַף־יְהוָה֙ בָּכֶ֔ם וְהִשְׁמִידְךָ֖ מַהֵֽר׃
>
> **7:5** כִּֽי־אִם־כֹּ֤ה תַעֲשׂוּ֙ לָהֶ֔ם מִזְבְּחֹתֵיהֶ֣ם תִּתֹּ֔צוּ וּמַצֵּבֹתָ֖ם תְּשַׁבֵּ֑רוּ וַאֲשֵֽׁירֵהֶם֙ תְּגַדֵּע֔וּן וּפְסִילֵיהֶ֖ם תִּשְׂרְפ֥וּן בָּאֵֽשׁ׃
>
> **7:6** כִּ֣י עַ֤ם קָדֹושׁ֙ אַתָּ֔ה לַיהוָ֖ה אֱלֹהֶ֑יךָ בְּךָ֞ בָּחַ֣ר ׀ יְהוָ֣ה אֱלֹהֶ֗יךָ לִהְיֹ֥ות לֹו֙ לְעַ֣ם סְגֻלָּ֔ה מִכֹּל֙ הָֽעַמִּ֔ים אֲשֶׁ֖ר עַל־פְּנֵ֥י הָאֲדָמָֽה׃ ס

**KJV:**

> **7:1** When the LORD thy God shall bring thee into the land whither thou goest to possess it, and hath cast out many nations before thee, the Hittites, and the Girgashites, and the Amorites, and the Canaanites, and the Perizzites, and the Hivites, and the Jebusites, seven nations greater and mightier than thou;
>
> **7:2** And when the LORD thy God shall deliver them before thee; thou shalt smite them, [and] utterly destroy them; thou shalt make no covenant with them, nor shew mercy unto them:
>
> **7:3** Neither shalt thou make marriages with them; thy daughter thou shalt not give unto his son, nor his daughter shalt thou take unto thy son.
>
> **7:4** For they will turn away thy son from following me, that they may serve other gods: so will the anger of the LORD be kindled against you, and destroy thee suddenly.
>
> **7:5** But thus shall ye deal with them; ye shall destroy their altars, and break down their images, and cut down their groves, and burn their graven images with fire.
>
> **7:6** For thou [art] an holy people unto the LORD thy God: the LORD thy God hath chosen thee to be a special people unto himself, above all people that [are] upon the face of the earth.

---

## Word-by-Word Parsing

Direct output of `hebrew_parser.py --verse "Deu 7:1"` … `"Deu 7:6"` (BHSA ETCBC morphology).

### Deuteronomy 7:1

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | כִּ֤י | כי | Conj | that / when |
| 2 | יְבִֽיאֲךָ֙ | בוא | **Verb.Hiphil.Impf.3ms.+2ms** | he brings you in |
| 3 | יְהוָ֣ה | יהוה | PropN.ms.Abs | YHWH |
| 4 | אֱלֹהֶ֔יךָ | אלהים | Noun.mp.Abs.+2ms | your God(s) |
| 5 | אֶל | אל | Prep | to |
| 6 | הָ אָ֕רֶץ | ה + ארץ | Art. + Noun.s.Abs | the land |
| 7 | אֲשֶׁר | אשׁר | Conj (relative) | which |
| 8 | אַתָּ֥ה | אתה | PersPron.2ms | you |
| 9 | בָא | בוא | Verb.Qal.Ptcp.ms.Abs | coming |
| 10 | שָׁ֖מָּה | שׁם | Adv. | there(ward) |
| 11 | לְ רִשְׁתָּ֑הּ | ל + ירשׁ | Prep + **Verb.Qal.InfCon.+3fs** | to possess it |
| 12 | וְ נָשַׁ֣ל | ו + **נשׁל** | Conj + **Verb.Qal.Perf.3ms** (weqatal) | and (he) shall pluck-off / drive-out |
| 13 | גֹּֽויִם רַבִּ֣ים | גוי + רב | Noun.mp.Abs + Adj.mp.Abs | many nations |
| 14 | מִ פָּנֶ֡יךָ | מן + פנה | Prep + Noun.mp.Abs.+2ms | from before you |
| 15–27 | הַֽחִתִּי֩ … וְהַיְבוּסִ֔י | (7 gentilic adjs) | Art + Adj.ms.Abs | Hittite…Jebusite |
| 28 | שִׁבְעָ֣ה גֹויִ֔ם | שׁבע + גוי | Noun.fs.Abs + Noun.mp.Abs | seven nations |
| 29 | רַבִּ֥ים וַעֲצוּמִ֖ים מִמֶּֽךָּ | רב + עצום + מן | Adj.mp + Adj.mp + Prep+2ms | more numerous and mightier than you |

### Deuteronomy 7:2

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | וּ נְתָנָ֞ם | ו + **נתן** | Conj + **Verb.Qal.Perf.3ms.+3mp** (weqatal) | and he will give them |
| 2 | יְהוָ֧ה אֱלֹהֶ֛יךָ | — | — | YHWH your God |
| 3 | לְ פָנֶ֖יךָ | ל + פנה | Prep + Noun.mp.Abs.+2ms | before you |
| 4 | וְ הִכִּיתָ֑ם | ו + **נכה** | Conj + **Verb.Hiphil.Perf.2ms.+3mp** (weqatal) | and you shall strike them |
| 5 | הַחֲרֵ֤ם | **חרם** | **Verb.Hiphil.InfAbs** | utterly destroy (emphatic) |
| 6 | תַּחֲרִים֙ | **חרם** | **Verb.Hiphil.Impf.2ms** | you shall devote-to-destruction |
| 7 | אֹתָ֔ם | את | Prep.+3mp (obj. marker) | them |
| 8 | לֹא | לא | Negation | not |
| 9 | תִכְרֹ֥ת | **כרת** | **Verb.Qal.Impf.2ms** | you shall cut (= make) |
| 10 | לָהֶ֛ם | ל | Prep.+3mp | to them |
| 11 | בְּרִ֖ית | ברית | Noun.fs.Abs | covenant |
| 12 | וְ לֹ֥א תְחָנֵּֽם | ו + לא + **חנן** | Conj + Neg + **Verb.Qal.Impf.2ms.+3mp** | and you shall not show them favor |

### Deuteronomy 7:3

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | וְ לֹ֥א | ו + לא | Conj + Neg | and not |
| 2 | תִתְחַתֵּ֖ן | חתן | **Verb.Hithpael.Impf.2ms** | you shall intermarry |
| 3 | בָּ֑ם | ב | Prep.+3mp | with them |
| 4 | בִּתְּךָ֙ | בת | Noun.fs.Abs.+2ms | your daughter |
| 5 | לֹא־ תִתֵּ֣ן | לא + **נתן** | Neg + **Verb.Qal.Impf.2ms** | you shall not give |
| 6 | לִ בְנֹ֔ו | ל + בן | Prep + Noun.ms.Abs.+3ms | to his son |
| 7 | וּ בִתֹּ֖ו | ו + בת | Conj + Noun.fs.Abs.+3ms | and his daughter |
| 8 | לֹא־ תִקַּ֥ח | לא + לקח | Neg + Verb.Qal.Impf.2ms | you shall not take |
| 9 | לִ בְנֶֽךָ | ל + בן | Prep + Noun.ms.Abs.+2ms | for your son |

### Deuteronomy 7:4

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | כִּֽי־ יָסִ֤יר | כי + סור | Conj + **Verb.Hiphil.Impf.3ms** | for he will turn aside (causatively) |
| 2 | אֶת־ בִּנְךָ֙ | את + בן | obj.marker + Noun.ms.Abs.+2ms | your son |
| 3 | מֵֽ אַחֲרַ֔י | מן + אחר | Prep + Noun.mp.Abs.+1cs | from after me |
| 4 | וְ עָבְד֖וּ | ו + עבד | Conj + **Verb.Qal.Perf.3p** (weqatal) | and they will serve |
| 5 | אֱלֹהִ֣ים אֲחֵרִ֑ים | אלהים + אחר | Noun.mp.Abs + Adj.mp.Abs | other gods |
| 6 | וְ חָרָ֤ה | ו + חרה | Conj + **Verb.Qal.Perf.3ms** (weqatal) | and will burn (hot) |
| 7 | אַף־ יְהוָה֙ | אף + יהוה | Noun.ms.Cst + PropN | the nostril/anger of YHWH |
| 8 | בָּכֶ֔ם | ב | Prep.+2mp | against you (pl.) |
| 9 | וְ הִשְׁמִידְךָ֖ | ו + שׁמד | Conj + **Verb.Hiphil.Perf.3ms.+2ms** (weqatal) | and he will destroy you |
| 10 | מַהֵֽר | מהר | Verb.Piel.InfAbs (adverbial) | quickly |

### Deuteronomy 7:5

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | כִּֽי־ אִם־ כֹּ֤ה | כי + אם + כה | Conj + Conj + Adv | but rather thus |
| 2 | תַעֲשׂוּ֙ | עשׂה | Verb.Qal.Impf.2mp | you (pl.) shall do |
| 3 | לָהֶ֔ם | ל | Prep.+3mp | to them |
| 4 | מִזְבְּחֹתֵיהֶ֣ם | מזבח | Noun.mp.Abs.+3mp | their altars |
| 5 | תִּתֹּ֔צוּ | נתץ | Verb.Qal.Impf.2mp | you shall tear down |
| 6 | וּ מַצֵּבֹתָ֖ם | ו + מצבה | Conj + Noun.fp.Abs.+3mp | and their pillars |
| 7 | תְּשַׁבֵּ֑רוּ | שׁבר | **Verb.Piel.Impf.2mp** | you shall shatter |
| 8 | וַ אֲשֵֽׁירֵהֶם֙ | ו + אשׁרה | Conj + Noun.fp.Abs.+3mp | and their Asherah-poles |
| 9 | תְּגַדֵּע֔וּן | גדע | **Verb.Piel.Impf.2mp** (paragogic nun) | you shall hew down |
| 10 | וּ פְסִילֵיהֶ֖ם | ו + פסיל | Conj + Noun.mp.Abs.+3mp | and their idols |
| 11 | תִּשְׂרְפ֥וּן | שׂרף | Verb.Qal.Impf.2mp (paragogic nun) | you shall burn |
| 12 | בָּ אֵֽשׁ | ב + ה + אשׁ | Prep + Art + Noun.s.Abs | in the fire |

### Deuteronomy 7:6

| # | Hebrew | Lemma | Parsing | Gloss |
|---|--------|-------|---------|-------|
| 1 | כִּ֣י | כי | Conj | for |
| 2 | עַ֤ם קָדֹושׁ֙ | עם + קדושׁ | Noun.ms.Abs + Adj.ms.Abs | a holy people |
| 3 | אַתָּ֔ה | אתה | PersPron.2ms | [are] you |
| 4 | לַ יהוָ֖ה | ל + יהוה | Prep + PropN | to YHWH |
| 5 | אֱלֹהֶ֑יךָ | אלהים | Noun.mp.Abs.+2ms | your God |
| 6 | בְּךָ֞ | ב | Prep.+2ms | in you / in your case |
| 7 | בָּחַ֣ר | **בחר** | **Verb.Qal.Perf.3ms** | he chose |
| 8 | יְהוָ֣ה אֱלֹהֶ֗יךָ | — | — | YHWH your God |
| 9 | לִ הְיֹ֥ות | ל + היה | Prep + Verb.Qal.InfCon | to be |
| 10 | לֹו֙ | ל | Prep.+3ms | to him / for himself |
| 11 | לְ עַ֣ם סְגֻלָּ֔ה | ל + עם + סגלה | Prep + Noun.ms.**Cst** + Noun.fs.Abs | for a people-of-treasured-possession |
| 12 | מִ כֹּל֙ | מן + כל | Prep + Noun.ms.Cst | out of all |
| 13 | הָֽ עַמִּ֔ים | ה + עם | Art + Noun.mp.Abs | the peoples |
| 14 | אֲשֶׁ֖ר | אשׁר | rel. | who [are] |
| 15 | עַל־ פְּנֵ֥י | על + פנה | Prep + Noun.mp.**Cst** | upon the face of |
| 16 | הָ אֲדָמָֽה | ה + אדמה | Art + Noun.fs.Abs | the ground |

---

## Clause Structure (BHSA)

Direct output of `hebrew_parser.py --clause "Deu 7:N"`. Clause-type codes: **xYqX** = כי + imperfect (protasis); **WQt0/WQtX** = weqatal (perfect consecutive, apodotic/narrative continuation); **xYq0** = כי + imperfect; **WxY0** = waw-conjunction + X + imperfect (circumstantial/coordinated prohibition); **Ptcp** = participial; **InfC** = infinitive-construct adjunct; **AjCl** = adjectival clause; **NmCl** = nominal clause.

| Vs | Clause type | Text | Function |
|----|-------------|------|----------|
| 7:1 | **xYqX** (Q) | כִּ֤י יְבִֽיאֲךָ֙ יְהוָ֣ה אֱלֹהֶ֔יךָ אֶל־הָאָ֕רֶץ | **Protasis**: "When YHWH brings you in…" |
| 7:1 | Ptcp (Attr) | אֲשֶׁר־אַתָּ֥ה בָא־שָׁ֖מָּה | relative clause modifying הָאָרֶץ |
| 7:1 | InfC (Adju) | לְרִשְׁתָּ֑הּ | purpose adjunct ("to possess it") |
| 7:1 | **WQt0** (Q) | וְנָשַׁ֣ל גֹּֽויִם… | **Weqatal continuation** of protasis ("and casts out") |
| 7:1 | AjCl (Attr) | רַבִּ֥ים וַעֲצוּמִ֖ים מִמֶּֽךָּ | attributive adjectival clause ("greater and mightier than you") |
| 7:2 | **WQtX** (Q) | וּנְתָנָ֞ם יְהוָ֧ה אֱלֹהֶ֛יךָ לְפָנֶ֖יךָ | **Continued protasis** ("and gives them before you") |
| 7:2 | **WQt0** (Q) | וְהִכִּיתָ֑ם | **Apodosis** begins: "then you shall strike them" |
| 7:2 | **xYq0** (Q) | הַחֲרֵ֤ם תַּחֲרִים֙ אֹתָ֔ם | asyndetic imperfect: "you shall utterly devote them" |
| 7:2 | xYq0 (Q) | לֹא־תִכְרֹ֥ת לָהֶ֛ם בְּרִ֖ית | prohibition #1 ("you shall not cut a covenant") |
| 7:2 | **WxY0** (Q) | וְלֹ֥א תְחָנֵּֽם | prohibition #2 ("and you shall not show favor") |
| 7:3 | WxY0 (Q) | וְלֹ֥א תִתְחַתֵּ֖ן בָּ֑ם | prohibition #3 ("and you shall not intermarry") |
| 7:3 | xYq0 (Q) | בִּתְּךָ֙ לֹא־תִתֵּ֣ן לִבְנֹ֔ו | casus-pendens + neg.imperfect |
| 7:3 | WxY0 (Q) | וּבִתֹּ֖ו לֹא־תִקַּ֥ח לִבְנֶֽךָ | paralleled prohibition |
| 7:4 | **xYq0** (Q) | כִּֽי־יָסִ֤יר אֶת־בִּנְךָ֙ מֵֽאַחֲרַ֔י | motive clause: "for he/it would turn your son away" |
| 7:4 | WQt0 (Q) | וְעָבְד֖וּ אֱלֹהִ֣ים אֲחֵרִ֑ים | weqatal result ("and they would serve other gods") |
| 7:4 | **WQtX** (Q) | וְחָרָ֤ה אַף־יְהוָה֙ בָּכֶ֔ם | weqatal result ("and YHWH's anger would burn") |
| 7:4 | WQt0 (Q) | וְהִשְׁמִידְךָ֖ מַהֵֽר | weqatal result ("and he would destroy you quickly") |
| 7:5 | **xYq0** (Q) | כִּֽי־אִם־כֹּ֤ה תַעֲשׂוּ֙ לָהֶ֔ם | "but rather thus shall you do to them" (adversative) |
| 7:5 | xYq0 (Q) | מִזְבְּחֹתֵיהֶ֣ם תִּתֹּ֔צוּ | casus-pendens + imperfect (1st destruction verb) |
| 7:5 | WxY0 (Q) | וּמַצֵּבֹתָ֖ם תְּשַׁבֵּ֑רוּ | (2nd destruction verb) |
| 7:5 | WxY0 (Q) | וַאֲשֵֽׁירֵהֶם֙ תְּגַדֵּע֔וּן | (3rd destruction verb) |
| 7:5 | WxY0 (Q) | וּפְסִילֵיהֶ֖ם תִּשְׂרְפ֥וּן בָּאֵֽשׁ | (4th destruction verb) |
| 7:6 | **NmCl** (Q) | כִּ֣י עַ֤ם קָדֹושׁ֙ אַתָּ֔ה לַיהוָ֖ה אֱלֹהֶ֑יךָ | **motive** verbless clause: "for [you are] a holy people" |
| 7:6 | **xQtX** (Q) | בְּךָ֞ בָּחַ֣ר יְהוָ֣ה אֱלֹהֶ֗יךָ מִכֹּל֙ הָֽעַמִּ֔ים | **fronted PP + qatal**: "in you YHWH chose…" |
| 7:6 | InfC (Adju) | לִהְיֹ֥ות לֹו֙ לְעַ֣ם סְגֻלָּ֔ה | purpose infinitive ("to be his treasured people") |
| 7:6 | NmCl (Attr) | אֲשֶׁ֖ר עַל־פְּנֵ֥י הָאֲדָמָֽה | relative nominal clause |

The whole paragraph is a single **conditional/temporal macrostructure**: 7:1–2a = protasis (כי + Hiphil imperfect + weqatal consecutive chain describing YHWH's causative action); 7:2b–5 = apodosis / Israel's obligations (weqatal, imperfects, and לא-prohibitions); 7:6 = **כי motive clause** grounding the whole in Israel's election. The grammar is perfectly transparent theologically: *God acts first (Hiphil), therefore Israel acts (imperfect/weqatal), because God chose her (Qal perfect).*

---

## Key Grammatical Features

### 1. יְבִֽיאֲךָ (7:1) — Hiphil Imperfect of בוא, "he will bring you in" (causative)

- **Form:** Verb, **Hiphil** stem, imperfect, 3ms with 2ms object suffix. Lemma בוא ("come/enter"). The Hiphil of בוא = **causative "bring in"** — the standard Deuteronomic verb for YHWH's leading Israel into the land (cf. Deut 4:38; 6:10; 8:7; 9:4; 11:29; Num 14:24, 31; 20:12). The 2ms suffix makes Israel the direct object of YHWH's causation.
- **Significance:** The whole paragraph is grammatically anchored in a Hiphil verb: everything Israel will later do (weqatal consecutives, imperfects of prohibition, imperfects of destruction) rests on what YHWH first *causes to happen*. Hebrew grammar encodes the theology: **divine initiative is causative (Hiphil), human response is imperfective (Qal/Piel/Hiphil imperfect).**
- **Grammar reference:** [`grammar-reference/hebrew/hiphil-imperfect.md`](../hebrew/hiphil-imperfect.md), [`grammar-reference/hebrew/stem-hiphil.md`](../hebrew/stem-hiphil.md)

### 2. וְנָשַׁ֣ל (7:1) — weqatal of נשל (H5394), "and he shall cast out"

- **Form:** BHSA parses as **Verb.Qal.Perf.3ms** with conjunctive waw (functioning as *weqatal* / **waw-consecutive perfect**). The lemma נשל (H5394) occurs only 7× in the HB (Exo 3:5 "put off [thy shoes]"; Deut 7:1, 22 "cast out [nations]"; 19:5 "slip [of an axehead]"; 28:40 "drop off [olives]"; Josh 5:15; 2 Kgs 16:6). Semantic core: "to slip/pluck off" — whether a sandal, an olive from a tree, an axehead from its handle, or a nation from its land. The metaphor is striking: YHWH will "slip the nations off" the land the way a ripe olive falls from the branch.
- **Parsing note:** BDB and HALOT classify 7:1's נָשַׁל as Qal perfect (the Piel attested elsewhere has a more intensive nuance). The *weqatal* here continues the protasis of the כי-clause: "When YHWH brings you in (Hiphil impf) **and casts off** (weqatal) many nations…" The sequence Hiphil-impf → weqatal is the standard protasis-continuation pattern (Joüon-Muraoka §119c; Waltke-O'Connor §32.2.1c).
- **Significance:** This is the *second* verb describing YHWH's causative action (after the Hiphil of בוא), and together they form the grammatical foundation for Israel's obligations. The conquest is framed not as Israel dispossessing the nations but as **YHWH dispossessing them before Israel** (מִפָּנֶיךָ "from before you" makes the syntactic subordination explicit — Israel is the *beneficiary*, not the agent, of dispossession).
- **Word study:** No canonical entry yet for H5394 (gap noted). See [`word-studies/H3423-yarash.md`](../../word-studies/H3423-yarash.md) for the complementary verb "dispossess/inherit" (ירשׁ) used in the same verse in the infinitive לְרִשְׁתָּהּ ("to possess it").

### 3. וּנְתָנָ֞ם + וְהִכִּיתָ֑ם (7:2) — weqatal chain: divine giving + human striking

- **Form:**
  - וּ + נְתָנָ֞ם = Conj + **Verb.Qal.Perf.3ms.+3mp** = weqatal "and he shall give them" (lemma נתן H5414).
  - וְ + הִכִּיתָ֑ם = Conj + **Verb.Hiphil.Perf.2ms.+3mp** = weqatal "and you shall strike them" (lemma נכה H5221).
- **Significance:** The shift of subject across a weqatal boundary is crucial. The first weqatal (נְתָנָם) continues the protasis (YHWH's action: "when he gives them before you"); the second weqatal (וְהִכִּיתָ֑ם) inaugurates the apodosis (Israel's obligation: "then you shall strike them"). Hebrew does not mark the protasis/apodosis hinge with a particle — the transition is marked by **subject shift** within the weqatal chain (YHWH 3ms → Israel 2ms). Joüon-Muraoka §167 identifies this as the "casus realis" conditional: when the protasis is taken as certain ("when," not "if"), the apodosis begins at the first subject-shifted weqatal or imperfect.
- **Hiphil of נכה:** The verb נכה (nakah, "strike") is always **Hiphil** when used transitively of military smiting in the Deuteronomistic History (Deut 1:4; 2:33; 3:3; Josh 7:5; 8:21; 10:10, 20; Judg 1:8; 3:29; 1 Sam 4:2; 15:7; etc.). The Qal of this root is essentially nonexistent in BH. So "you shall strike them" is by morphological necessity a Hiphil — there is no simple/Qal option. See [`word-studies/H5221-nakah.md`](../../word-studies/H5221-nakah.md), [`word-studies/TR-nakah-patasso.md`](../../word-studies/TR-nakah-patasso.md).
- **Grammar reference:** [`grammar-reference/hebrew/syntax-waw-conjunction.md`](../hebrew/syntax-waw-conjunction.md) (functions of conjunctive waw); compare [`grammar-reference/hebrew/weqatal-apodosis-vow.md`](../hebrew/weqatal-apodosis-vow.md) for weqatal in apodosis of vows (parallel mechanics).
- **Word studies:** [`H5414-nathan`](../../word-studies/H5414-nathan.md), [`H5221-nakah`](../../word-studies/H5221-nakah.md), [`G1325-didomi`](../../word-studies/G1325-didomi.md).

### 4. הַחֲרֵ֤ם תַּחֲרִים֙ (7:2) — Hiphil infinitive absolute + Hiphil imperfect (paronomasia) of חרם

- **Form:** **Verb.Hiphil.InfAbs** (הַחֲרֵם) + **Verb.Hiphil.Impf.2ms** (תַּחֲרִים) from the same root חרם (H2763). The *infinitive-absolute-before-finite-verb* construction is Hebrew's standard **intensifying/asseverative paronomasia**: it renders the force as "you **shall surely/utterly** devote them to destruction." GKC §113n; Joüon-Muraoka §123g; Waltke-O'Connor §35.3.1.
- **Semantics of חרם (Hiphil):** The Hiphil of חרם = "to place under *ḥerem*, to devote irrevocably to YHWH by destruction." The root (BDB, HALOT) refers to something *banned* from common use — either by consecration to the sanctuary (Lev 27:21, 28–29) or by destruction as YHWH's portion (Deut 2:34; 3:6; 13:16; 20:17; Josh 6:17–21; 10:40; 11:11–12; 1 Sam 15:3). In Deut 7:2 the Hiphil paronomasia intensifies the verb: *not merely strike, but utterly devote by destruction*. The cognate noun חֵרֶם (H2764, "devoted thing / ban") is the result; the verb describes the act of transferring something from profane to sacred-for-destruction.
- **Paronomasia function:** The infinitive absolute construction has three recognized nuances (Joüon §123e–l): (a) intensification ("surely"), (b) continuation/durativity, (c) polar absoluteness. Context in Deut 7:2 favors (a): contrastive emphasis over the prohibitions that follow (no covenant, no favor, no intermarriage). The emphatic construction makes the *ḥerem* the central command — the other prohibitions are corollaries of this central mandate.
- **Parallel vow-paronomasia:** Cf. Judg 11:31 (Jephthah's vow), Gen 2:17 (מוֹת תָּמוּת "thou shalt surely die"), 1 Sam 15:3 (וְהַחֲרַמְתֶּם אֶת־כָּל־אֲשֶׁר־לוֹ), where the same construction asserts irrevocable action.
- **Grammar reference:** [`grammar-reference/hebrew/hiphil-imperfect.md`](../hebrew/hiphil-imperfect.md); compare inf-abs paronomasia documented in [`grammar-reference/passages/jdg-11-30-31.md`](jdg-11-30-31.md) (נָתוֹן תִּתֵּן, "if thou shalt without fail deliver").
- **Word studies:** [`H2763-charam`](../../word-studies/H2763-charam.md), [`H2764-cherem`](../../word-studies/H2764-cherem.md). See also [`word-studies/H8045-shamad.md`](../../word-studies/H8045-shamad.md), [`TR-shamad-apollymi`](../../word-studies/TR-shamad-apollymi.md) for the related destruction vocabulary in v.4.

### 5. The Three לֹא-Prohibitions of 7:2–3 — negated Qal/Hithpael imperfects

Biblical Hebrew expresses **categorical / permanent prohibitions** with **לֹא + imperfect** (non-jussive), distinguished from **temporary / specific prohibitions**, which use **אַל + jussive**. GKC §107o, §109c; Joüon-Muraoka §114i, §160f; Waltke-O'Connor §34.2.1b, §34.3.

The pericope stacks three such categorical prohibitions:

| # | Verse | Phrase | Parsing | Gloss | Object |
|---|-------|--------|---------|-------|--------|
| 1 | 7:2 | לֹא־תִכְרֹ֥ת … בְּרִ֖ית | Neg + **Verb.Qal.Impf.2ms** (כרת H3772) | you shall not cut (= make) a covenant | בְּרִית |
| 2 | 7:2 | וְלֹ֥א תְחָנֵּֽם | Neg + **Verb.Qal.Impf.2ms.+3mp** (חנן H2603) | and you shall not show them favor | +3mp suffix |
| 3 | 7:3 | וְלֹ֥א תִתְחַתֵּ֖ן בָּ֑ם | Neg + **Verb.Hithpael.Impf.2ms** (חתן) | and you shall not intermarry with them | בָּם |

**Categorical force.** Because the construction is *לא + imperfect* (not אַל + jussive), the prohibitions are absolute and permanent — they are not situational injunctions to avoid a particular covenant or match, but **standing prohibitions of all covenants, all favor, all intermarriages** with the seven nations. This is the Decalogue-style prohibition (Ex 20:3–17 likewise uses לא + imperfect throughout).

**כרת ברית — "cut a covenant."** The verb כרת (H3772) in the **Qal** with בְּרִית as its object is the idiomatic Hebrew expression for **making a covenant** (originating from the cutting of sacrificial animals in covenant ceremonies, Gen 15:10, 17–18; Jer 34:18). LXX typically renders this with διατίθεμαι / διαθήκην. See [`word-studies/H3772-karath.md`](../../word-studies/H3772-karath.md) and [`word-studies/TR-karath-diatithemi.md`](../../word-studies/TR-karath-diatithemi.md), [`word-studies/H1285-beriyth.md`](../../word-studies/H1285-beriyth.md), [`word-studies/G1242-diatheke.md`](../../word-studies/G1242-diatheke.md). The prohibition לֹא־תִכְרֹת … בְּרִית forbids the Canaanites all diplomatic covenantal relation — precisely the thing Joshua violates with the Gibeonites (Josh 9:15 ויכרת להם יהושׁע ברית, the same verb).

**חנן — "show favor / have mercy."** The Qal of חנן (H2603, "be gracious, show favor") with +3mp suffix means "show *them* favor." The prohibition וְלֹ֥א תְחָנֵּֽם is often discussed alongside the parallel at Deut 23:6 [H23:7] (לֹא־תִדְרֹשׁ שְׁלֹמָם וְטֹבָתָם) and Deut 20:16–17 (חרם mandate). The root חנן also yields the cognate noun חֵן ("grace/favor," ~70×) and the name יוֹחָנָן / יְהוֹחָנָן ("YHWH has been gracious") and Hebrew חַנָּה / Ἄννα. See [`word-studies/H2603-chanan.md`](../../word-studies/H2603-chanan.md), [`word-studies/TR-chanan-eleeo.md`](../../word-studies/TR-chanan-eleeo.md). The grammatical tension is acute: the people whose very God is *rav-ḥesed* (Ex 34:6) is forbidden from extending *ḥen* to these seven nations — a prohibition the prophets will later remember when Israel extends covenant favor to foreign gods (Hos 2:19 [H2:21]; Jer 31:2).

**חתן (Hithpael) — "make oneself a son-in-law."** The verb חתן normally appears in the Qal participle חֹתֵן ("father-in-law") and in the Hithpael "to become son-in-law, intermarry." The Hithpael prohibition in 7:3a is then *glossed* (7:3b–c) with two Qal imperfects as prohibitions on the concrete acts: *your daughter you shall not give* (תִתֵּן, Qal impf of נתן), *and his daughter you shall not take* (תִקַּח, Qal impf of לקח). The Qal form *תִתֵּן* is the same lemma נתן as the weqatal וּנְתָנָם in 7:2, but now it is the *prohibited* act of giving — showing how Hebrew pivots a single lexical root (נתן) from divine positive action ("he will give them") to forbidden human action ("you shall not give [your daughter]") by grammatical context alone.

**Grammar reference:** no existing entry for "lo + imperfect categorical prohibition" specifically; GKC §107o cited. Related: [`grammar-reference/hebrew/qal-imperfect.md`](../hebrew/qal-imperfect.md).

**Word studies:** [`H5414-nathan`](../../word-studies/H5414-nathan.md), [`H3772-karath`](../../word-studies/H3772-karath.md), [`H2603-chanan`](../../word-studies/H2603-chanan.md), [`WG-covenant`](../../word-studies/WG-covenant.md).

### 6. בְּךָ֞ בָּחַ֣ר יְהוָ֣ה (7:6) — fronted PP + Qal perfect of בחר (H977), "in you YHWH chose"

- **Form:** Prepositional phrase בְּךָ֞ ("in you") **fronted** before the verb בָּחַ֣ר (lemma בחר H977, "choose"; Qal perfect 3ms) + subject יְהוָ֣ה. BHSA tags this clause xQtX ("X-qatal-X" — an element other than the verb is fronted before a qatal verb).
- **Significance of the fronting:** Default Hebrew word order is Verb-Subject-Object (VSO). Fronting a non-subject constituent before the verb marks it as **topicalized / contrastive**: "**In you** (and not in others) YHWH chose." The contrast is made explicit in the prepositional phrase מִכֹּל֙ הָֽעַמִּ֔ים ("out of all the peoples"). The same rhetorical construction appears in Deut 7:7–8 (where the contrast is developed: not because Israel was numerous, but because YHWH loved you).
- **Significance of the Qal perfect:** בָּחַר is a **Qal perfect** (not imperfect or participle): the choosing is presented as **a completed, past, foundational act** — not a present process, not a future contingency. In Deuteronomy this pattern is consistent: whenever YHWH's election of Israel is narrated, the verb is Qal perfect (Deut 4:37 ובחר; 7:6 בָּחַר; 7:7 חָשַׁק; 10:15 בָּחַר). The verb בחר occurs 172× in the HB with various subjects; when YHWH is the subject, the referent is almost always (a) Israel/the patriarchs, (b) the Davidic king, or (c) the chosen place of worship (Jerusalem / Temple) — the three loci of Deuteronomic election theology.
- **Relationship to the herem paragraph:** Verse 6 supplies the **motive** (כִּי, "for") for everything in 7:1–5. The logic runs: *Cast them out and utterly destroy them and don't intermarry or covenant with them — **because** YHWH chose you to be his treasured possession (עַם סְגֻלָּה), and that election will be corrupted by syncretistic fusion.* The theology is encoded in the grammar: the weqatal chain of 7:1–5 (ongoing future actions conditioned by YHWH's initiative) is grounded in a Qal perfect of election that has *already* happened.
- **Word study:** No canonical entry yet for H977 (gap noted). Related: [`word-studies/H5459-segullah.md`](../../word-studies/) if present; [`word-studies/H6944-qodesh.md`](../../word-studies/H6944-qodesh.md) for the holiness vocabulary that parallels election; [`word-studies/WG-holiness.md`](../../word-studies/WG-holiness.md).

### 7. לְעַם סְגֻלָּה (7:6) — construct chain: "for a people of treasured-possession"

- **Form:** לְ + עַם (Noun.ms.**Cst**) + סְגֻלָּה (Noun.fs.Abs). BHSA marks עַם as construct state (Cst), so the phrase is a **construct chain**, not two appositional nouns. The construct-chain meaning is "a people [which is his] treasured-possession" — *segullah* specifies the type/function of *ʿam*.
- **סְגֻלָּה (segullah, H5459):** Occurs only 8× in the HB (Exod 19:5; Deut 7:6; 14:2; 26:18; 1 Chr 29:3; Ps 135:4; Eccl 2:8; Mal 3:17). Semantic core: a **private treasure / personal property** reserved for the owner's special use — a royal treasury term in the Akkadian cognate *sikiltu(m)* (Alalakh and Ugaritic texts use it for royal property sequestered from taxation). In Deut 7:6, 14:2, and 26:18, *segullah* is the theological technical term for Israel's unique status: she is YHWH's own *private treasure*, distinguished from "all the peoples on the face of the ground."
- **Significance:** The construct chain is more precise than apposition would be. "A treasured people" (apposition) could describe any favorite nation; "a people-of-segullah" (construct) marks the noun סְגֻלָּה as the **defining category** — Israel is not merely *among* favored nations, she *is* YHWH's *segullah*, his private royal treasury of humanity. The LXX renders this λαὸς περιούσιος ("a people of his own possession"), a rare Greek adjective (LSJ "specially one's own") that Paul echoes in Titus 2:14 (λαὸν περιούσιον) and that 1 Pet 2:9 reworks as λαὸς εἰς περιποίησιν.
- **Grammar reference:** construct state reference not yet documented as standalone; see [`grammar-reference/passages/deut-6-4.md`](deut-6-4.md) for a parallel proper-name + common-noun appositional phrase (יְהוָה אֱלֹהֵינוּ, *not* construct); the contrast here (עַם סְגֻלָּה *is* construct) is instructive.

---

## Macro-Pattern: The Protasis-Apodosis-Motive Shape of Deut 7:1–6

Putting the clause structure together, the whole pericope is one extended rhetorical sentence:

```
PROTASIS (7:1–2a)                        APODOSIS (7:2b–5)
כי + Hiphil impf (יביאך)                 weqatal 2ms (והכיתם)
  + weqatal 3ms (ונשל)                     + inf.abs. + impf 2ms (החרם תחרים)
  + weqatal 3ms (ונתנם)                     + לא + impf 2ms (לא תכרת ... ולא תחננם)
                                            + לא + Hithpael impf 2ms (לא תתחתן)
                                            + לא + Qal impf 2ms × 2 (לא תתן ... לא תקח)
                                            + כי impf (motive: יסיר)
                                              + weqatal result (עבדו, חרה, והשמידך)
                                            + adversative (כי אם כה תעשו)
                                              + 4× Piel/Qal impf 2mp (תתצו, תשברו, תגדעון, תשרפון)

                MOTIVE CLAUSE (7:6)
                כי + verbless NmCl (עם קדוש אתה)
                  + fronted-PP + Qal Perf (בך בחר יהוה)
                  + purpose InfC (להיות לו לעם סגלה)
```

Three observations:

1. **Divine actions are causative (Hiphil) or gifting (Qal of נתן);** human actions are striking (Hiphil of נכה), devoting (Hiphil of חרם), and destroying (Qal/Piel of נתץ, שבר, גדע, שרף). Israel does not *initiate* the dispossession; she *completes* it under instruction.

2. **Prohibitions (לא + imperfect) are categorical, not situational.** Covenant-cutting, favor-showing, and intermarriage with the seven nations are permanently forbidden — the same grammatical construction as the Decalogue.

3. **The motive clause (7:6) grounds ethical imperative in prior election.** The logic of the passage is not "destroy them and you will become holy" but "**because** you are already holy and chosen (Qal perfect), therefore destroy them (weqatal / imperfect)." The Qal perfect of בחר (7:6) is ontologically prior to the weqatal of והכיתם (7:2).

This three-part shape — causative Hiphil protasis, consecutive-perfect apodosis of human obligation, perfect-tense motive of divine election — is the **grammatical spine of Deuteronomic ethics**, reappearing in Deut 9:1–6 (the humility sermon on election), Deut 10:12–22 (the great summary), and Deut 14:1–2 (food laws grounded in election). Reading the grammar backwards: understand the ethics of Deuteronomy 7 means understanding *why* the Qal perfect בָּחַר in v.6 is not an afterthought but the ground of the whole paragraph.

---

## Ḥerem Vocabulary in Canonical Context

The חרם mandate of 7:2 sits inside a larger lexical field of conquest/destruction verbs that Deut 7:1–6 samples:

| Lemma | Strong's | Stem | Semantic core | Deut 7 occurrence |
|-------|----------|------|---------------|-------------------|
| בוא | H935 | Hiphil | bring in (causatively) | 7:1 יְבִיאֲךָ |
| ירשׁ | H3423 | Qal | possess / dispossess | 7:1 לְרִשְׁתָּהּ |
| נשׁל | H5394 | Qal | pluck off / cast out | 7:1 וְנָשַׁל |
| נתן | H5414 | Qal | give / deliver | 7:2 וּנְתָנָם; 7:3 תִתֵּן (negated) |
| נכה | H5221 | Hiphil | strike / smite | 7:2 וְהִכִּיתָם |
| חרם | H2763 | Hiphil | devote to destruction | 7:2 הַחֲרֵם תַּחֲרִים |
| כרת | H3772 | Qal | cut (covenant) | 7:2 לֹא־תִכְרֹת (negated) |
| חנן | H2603 | Qal | show favor | 7:2 וְלֹא תְחָנֵּם (negated) |
| חתן | H2859 | Hithpael | intermarry | 7:3 לֹא תִתְחַתֵּן (negated) |
| לקח | H3947 | Qal | take | 7:3 לֹא תִקַּח (negated) |
| סור | H5493 | Hiphil | turn aside | 7:4 יָסִיר |
| עבד | H5647 | Qal | serve (gods) | 7:4 וְעָבְדוּ |
| חרה | H2734 | Qal | burn (of anger) | 7:4 וְחָרָה |
| שׁמד | H8045 | Hiphil | exterminate | 7:4 וְהִשְׁמִידְךָ |
| עשׂה | H6213 | Qal | do / make | 7:5 תַעֲשׂוּ |
| נתץ | H5422 | Qal | tear down (altars) | 7:5 תִּתֹּצוּ |
| שׁבר | H7665 | Piel | shatter (pillars) | 7:5 תְּשַׁבֵּרוּ |
| גדע | H1438 | Piel | hew down (asherah) | 7:5 תְּגַדֵּעוּן |
| שׂרף | H8313 | Qal | burn (idols) | 7:5 תִּשְׂרְפוּן |
| בחר | H977 | Qal | choose | 7:6 בָּחַר |
| היה | H1961 | Qal | be (become) | 7:6 לִהְיוֹת |

Note the distributional pattern: **Hiphil verbs cluster at the protasis and at the warning of v.4** (*causative* actions of YHWH — bringing in, turning aside, destroying — or causative actions Israel performs under divine permission — striking, devoting, exterminating). **Qal and Piel verbs dominate the apodosis for Israel's physical activity** — cut covenant (neg), give daughter (neg), serve, tear down, shatter, hew down, burn. The theological grammar of the passage is: *the causative (Hiphil) is God's and God's delegated violence; the physical execution (Qal/Piel) is Israel's, but only in response.*

---

## The Same Pattern Elsewhere in Deuteronomy & Joshua

The grammatical pattern of Deut 7:1–6 — *Hiphil imperfect + weqatal chain + לא prohibitions + motive of election* — is not unique but **paradigmatic**. Key parallels:

| Passage | Hiphil imperf of YHWH's causation | weqatal chain | לא-prohibitions | Motive of election |
|---------|-------------------------------------|---------------|------------------|---------------------|
| Deut 7:1–6 | יְבִיאֲךָ | וְנָשַׁל, וּנְתָנָם, וְהִכִּיתָם | לא תכרת, לא תחננם, לא תתחתן | בָּחַר (7:6) |
| Deut 12:29 | יַכְרִית (Hiphil of כרת!) | — | — | (implied) |
| Deut 20:16–18 | נֹתֵן (ptcp) | — | הַחֲרֵם תַּחֲרִים (same inf.abs.+impf!) | 20:18 motive |
| Josh 23:4–13 | הִפִּיל, הוֹרִישׁ | — | לֹא לָבוֹא, לֹא תִזְכִּירוּ, לֹא תִשָּׁבְעוּ | 23:3 (YHWH fought) |
| Judg 2:1–3 | אַעֲלֶה | — | לֹא־תִכְרְתוּ בְרִית | covenant at Bochim |

Most striking: **Deut 20:16–18 repeats Deut 7:2's infinitive-absolute + imperfect paronomasia verbatim** (הַחֲרֵ֣ם תַּחֲרִימֵ֔ם), showing that Moses' ḥerem formula is a fixed deuteronomic-legal idiom, not a one-off expression. Josh 11:20 retrospectively confirms the execution (הַחֲרִימָם… the cognate Hiphil perf noun-less + object suffix).

---

## The LXX Rendering

The LXX of Deut 7:1–6 (Rahlfs) renders the Hebrew grammar with careful formal equivalence:

- **Hiphil imperfect יְבִיאֲךָ** → εἰσαγάγῃ σε ("he brings you in"), 3rd-singular aorist subjunctive (the natural Greek equivalent of a Hebrew imperfect after ὅταν / after ἐὰν).
- **weqatal chain וְנָשַׁל … וּנְתָנָם** → καὶ ἐξαρεῖ … καὶ παραδώσει ("and he will remove … and he will deliver"), future indicatives (LXX's default for weqatal in apodosis of a conditional).
- **Infinitive-absolute paronomasia הַחֲרֵם תַּחֲרִים** → ἀφανισμῷ ἀφανιεῖς ("with utter destruction you shall destroy"), LXX's standard cognate-dative-noun construction for inf-abs + impf paronomasia. See [`grammar-reference/greek/lxx-disjunctive-waw-vows.md`](../greek/lxx-disjunctive-waw-vows.md) for related LXX rendering patterns of Hebrew inf-abs constructions.
- **לא + imperfect prohibitions** → οὐ + future indicative (οὐ διαθήσῃ … οὐδὲ μὴ ἐλεήσητε … οὐ γαμβρεύσετε), the LXX standard for categorical prohibitions (Decalogue-style).
- **Qal perfect of election בָּחַר** → ἐξελέξατο ("he chose"), middle aorist — reflecting YHWH's self-interested act of choosing. Paul picks up this vocabulary extensively (ἐκλεκτός, ἐκλογή, Rom 9:11; 11:5, 28; Eph 1:4; etc.).
- **עַם סְגֻלָּה** → λαὸν περιούσιον (rare adjective, "specially one's own"), retained at Deut 14:2, 26:18; Titus 2:14.

---

## Cross-References

### Grammar Library
- [`grammar-reference/hebrew/stem-hiphil.md`](../hebrew/stem-hiphil.md) — Hiphil stem general semantics (causative, declarative, factitive)
- [`grammar-reference/hebrew/hiphil-imperfect.md`](../hebrew/hiphil-imperfect.md) — Hiphil imperfect paradigm and functions (relevant to יְבִיאֲךָ, יָסִיר, וְהִשְׁמִידְךָ, תַּחֲרִים)
- [`grammar-reference/hebrew/qal-imperfect.md`](../hebrew/qal-imperfect.md) — Qal imperfect paradigm (relevant to תִכְרֹת, תְחָנֵּם, תִתֵּן, תִקַּח, תַעֲשׂוּ, תִּתֹּצוּ, תִּשְׂרְפוּן)
- [`grammar-reference/hebrew/syntax-waw-conjunction.md`](../hebrew/syntax-waw-conjunction.md) — conjunctive vs. disjunctive waw (relevant to weqatal chain)
- [`grammar-reference/hebrew/weqatal-apodosis-vow.md`](../hebrew/weqatal-apodosis-vow.md) — weqatal in apodosis (parallel mechanics)
- [`grammar-reference/hebrew/syntax-conditional-vow.md`](../hebrew/syntax-conditional-vow.md) — protasis-apodosis mechanics (same grammar, vow register)
- [`grammar-reference/hebrew/syntax-wx-qatal-circumstantial.md`](../hebrew/syntax-wx-qatal-circumstantial.md) — disjunctive waw + X + qatal (helps contrast with weqatal here)

### Word Studies
- [`word-studies/H5414-nathan.md`](../../word-studies/H5414-nathan.md) — נתן "give" (7:2 divine; 7:3 negated human)
- [`word-studies/H5221-nakah.md`](../../word-studies/H5221-nakah.md) — נכה "strike" (Hiphil, 7:2)
- [`word-studies/TR-nakah-patasso.md`](../../word-studies/TR-nakah-patasso.md) — נכה ↔ πατάσσω (LXX translation)
- [`word-studies/H2763-charam.md`](../../word-studies/H2763-charam.md) — חרם "devote to destruction" (Hiphil, 7:2)
- [`word-studies/H2764-cherem.md`](../../word-studies/H2764-cherem.md) — חֵרֶם "devoted thing / ban" (cognate noun)
- [`word-studies/H3772-karath.md`](../../word-studies/H3772-karath.md) — כרת "cut (covenant)" (7:2 prohibition)
- [`word-studies/TR-karath-diatithemi.md`](../../word-studies/TR-karath-diatithemi.md) — כרת ↔ διατίθεμαι (covenant-cutting LXX)
- [`word-studies/H1285-beriyth.md`](../../word-studies/H1285-beriyth.md) — ברית "covenant"
- [`word-studies/H2603-chanan.md`](../../word-studies/H2603-chanan.md) — חנן "show favor" (7:2 prohibition)
- [`word-studies/TR-chanan-eleeo.md`](../../word-studies/TR-chanan-eleeo.md) — חנן ↔ ἐλεέω
- [`word-studies/H8045-shamad.md`](../../word-studies/H8045-shamad.md) — שׁמד "exterminate" (Hiphil, 7:4)
- [`word-studies/TR-shamad-apollymi.md`](../../word-studies/TR-shamad-apollymi.md) — שׁמד ↔ ἀπόλλυμι
- [`word-studies/H3423-yarash.md`](../../word-studies/H3423-yarash.md) — ירשׁ "possess/dispossess" (7:1 לְרִשְׁתָּהּ)
- [`word-studies/H430-elohiym.md`](../../word-studies/H430-elohiym.md) — אלהים "god(s)" (pervasive in the pericope)
- [`word-studies/H6944-qodesh.md`](../../word-studies/H6944-qodesh.md) — קדושׁ "holy" (7:6 עַם קָדוֹשׁ)
- [`word-studies/WG-covenant.md`](../../word-studies/WG-covenant.md) — English entry: covenant vocabulary
- [`word-studies/WG-holiness.md`](../../word-studies/WG-holiness.md) — English entry: holiness vocabulary

### Word-Study Gaps Identified
- **H977 בחר** ("choose") — no canonical entry. Significant gap given the word's Deuteronomic density (172× total, heavy in chs 4, 7, 10, 12, 14, 16, 17, 30); election theology.
- **H5394 נשׁל** ("pluck off / cast out") — no canonical entry. Only 7 occurrences but highly significant for the conquest narrative (Deut 7:1, 22).
- **H5459 סְגֻלָּה** ("treasured possession") — no canonical entry. Key covenantal term (8× only, but theologically central: Exod 19:5; Deut 7:6; 14:2; 26:18; 1 Chr 29:3; Ps 135:4; Eccl 2:8; Mal 3:17). NT parallel λαὸς περιούσιος (Titus 2:14).
- **H2859 חתן** (Hithpael "intermarry") — no canonical entry.
- **Grammar-reference gap:** no standalone entry for *לא + imperfect as categorical prohibition* (distinct from אל + jussive). Would be useful as a counterpart to existing [`mood-aorist-imperative.md`](../greek/mood-aorist-imperative.md) entry for Greek.
- **Grammar-reference gap:** no standalone entry for *infinitive absolute paronomasia* (inf.abs. + finite verb), though an instance is documented inline at [`passages/jdg-11-30-31.md`](jdg-11-30-31.md). Promoting this to a dedicated grammar-reference entry would let future studies of Gen 2:17 (מות תמות), Deut 7:2 / 20:17 (החרם תחרים), 1 Sam 15:3, and Jer 22:10 reference it canonically.

### Related Passages
- [`grammar-reference/passages/deut-6-4.md`](deut-6-4.md) — the Shema (immediate literary context; unique Deity premise)
- [`grammar-reference/passages/1sa-15-1-33.md`](1sa-15-1-33.md) — Saul and the Amalekite ḥerem (later application of Deut 7 logic)
- [`grammar-reference/passages/jdg-11-30-31.md`](jdg-11-30-31.md) — parallel inf-abs paronomasia (נתון תתן)

### Grammar References (external)
- GKC §107o (categorical prohibitions with לא + imperfect), §113n (inf-abs + finite verb paronomasia), §112 (weqatal consecutive), §124g–i (plural of majesty for אלהים), §141 (nominal clauses)
- Joüon-Muraoka §119c (weqatal continuing protasis), §123e–l (inf-abs functions), §160f (לא vs. אל prohibitions), §167 (conditional-protasis patterns)
- Waltke-O'Connor §32.2 (weqatal), §34.2.1b / §34.3 (prohibitions), §35.3.1 (inf-abs paronomasia)
- BDB s.v. בוא (Hiphil), נשׁל, נתן, נכה (Hiphil), חרם, כרת, חנן, בחר, סְגֻלָּה
- HALOT s.v. נשׁל (rare root, 7× HB); חרם (with extensive Hiphil discussion for devotional ban)

### Parallel Traditions
- **Deut 20:16–18** — the same inf-abs + impf paronomasia (הַחֲרֵ֣ם תַּחֲרִימֵ֔ם) applied to the same seven-nations list; the locus classicus for ḥerem-warfare law
- **Josh 10–11; 11:20** — the narrative execution of Deut 7's mandate; 11:20 explicitly cites YHWH's initiative (לְחַרְמָם)
- **Judg 2:1–3** — the post-conquest indictment: Israel *did* cut covenant (contra Deut 7:2), and YHWH judicially declares he will no longer drive the nations out (contrast with 7:1 יְבִיאֲךָ)
- **1 Sam 15** — Saul's failed ḥerem on Amalek; Deut 7:2's הַחֲרֵם תַּחֲרִים grammar reappears in Samuel's command
- **Mal 3:17** — eschatological reuse of סְגֻלָּה ("they shall be mine, says YHWH of hosts, in the day when I make my סְגֻלָּה")
- **1 Pet 2:9** — NT transposition of the same cluster (γένος ἐκλεκτόν, ἔθνος ἅγιον, λαὸς εἰς περιποίησιν), drawing on Exod 19:5–6 and Deut 7:6 together
- **Titus 2:14** — explicit Greek quotation of Deut 7:6's λαὸν περιούσιον applied to the Church
