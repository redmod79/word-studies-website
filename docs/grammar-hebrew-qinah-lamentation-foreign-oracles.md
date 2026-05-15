# Qinah / Lamentation Genre in Foreign-King and City Oracles (Hebrew)

## Definition

`קִינָה` (*qinah*, H7015) is a feminine noun meaning elegy, dirge, or lamentation. In prophetic oracles it can function as a commissioned speech-act: the prophet is told to "lift up" (`נשׂא`, Qal) a lament over a city, king, or nation. The formula marks the oracle as a funeral-like judgment song, even when the addressee is still active in the narrative horizon.

1. **Commissioned lament** - prophet receives an imperative to lift up a qinah over an object.
2. **Foreign city/king lament** - qinah is directed `ʿal` ("upon/over/against") Tyre, the king of Tyre, Pharaoh/Egypt, or similar nations.
3. **Performed lament** - qinah can itself be the object chanted by others, using the Piel verb `קונן` / `קוּן` ("chant a dirge").

## Form Recognition

- Noun: `קִינָה`, parsed `Noun.fs.Abs`, glossed "elegy."
- Commission formula: `שָׂא קִינָה` = Qal imperative 2ms of נשׂא + direct object qinah.
- Directional target: `עַל` + person/city/nation.
- Performed lament formula: Piel forms of `קין/קון`, e.g. `קֹונְנוּהָ`, `תְּקֹונֵנָּה`.
- Parser signatures: `lemma=קינה`, or `lemma=נשׂא` near `קִינָה`, or Piel `lemma=קין`.

## Functions with Examples

### 1. City Lament Over Tyre

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Eze 27:2 | שָׂא עַל־צֹר קִינָה | `נשׂא` Qal.Impv.2ms + `קינה` Noun.fs.Abs | "take up a lamentation for Tyrus" |
| Eze 27:32 | קִינָה | Noun.fs.Abs | "in their wailing they shall take up a lamentation for thee" |

### 2. King Lament in a Foreign Oracle

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Eze 28:12 | שָׂא קִינָה עַל־מֶלֶךְ צֹור | Qal.Impv.2ms + Noun.fs.Abs + `ʿal` + construct chain | "take up a lamentation upon the king of Tyrus" |
| Eze 32:2 | שָׂא קִינָה עַל־פַּרְעֹה מֶלֶךְ־מִצְרַיִם | Qal.Impv.2ms + Noun.fs.Abs + `ʿal` + royal title | "take up a lamentation for Pharaoh king of Egypt" |

### 3. Lament as a Chanted Performance

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Eze 32:16 | קִינָה הִיא | Noun.fs.Abs + Pron.3fs | "This is the lamentation" |
| Eze 32:16 | קֹונְנוּהָ | Verb.Piel.Perf.3p.+3fs | "wherewith they shall lament her" |
| Eze 32:16 | תְּקֹונֵנָּה אֹותָהּ | Verb.Piel.Impf.3fp + Obj.+3fs | "shall lament her" |

## Contrast with Related Speech-Act Forms

| Formula | Function | Example |
|---------|----------|---------|
| `נָשָׂא קִינָה` | Lift up a lament/dirge | Eze 27:2; 28:12; 32:2 |
| `נָשָׂא מָשָׁל` | Lift up a proverb/parable/taunt | See [mashal-speech-act](mashal-speech-act.md) |
| `קֹונֵן / קוּן` Piel | Chant or perform a dirge | Eze 32:16 |
| `כֹּה אָמַר יְהוָה` | Messenger formula for divine speech | Eze 28:12, 22 |

## Diagnostic Rule

When `קִינָה` appears with `שָׂא` plus `עַל`, the grammar marks a directed lament over a target. The form is compatible with both individual and corporate targets: a city (`צֹר`), a king (`מֶלֶךְ צֹור`), or Pharaoh/Egypt. The lament genre does not by itself identify whether the referent is only individual, only corporate, or typological; it marks the speech act as a funeral-like judgment performance.

## Lexical Notes

- `קִינָה` (H7015): BLB count 18; definition "dirge/lamentation."
- `קוּן` (H6969): verb, BLB count 8; "chant or wail at a funeral"; parser-verified in Eze 32:16 with Piel forms.

## Cross-References

- [mashal-speech-act](mashal-speech-act.md)
- [ezk-28-1-19-prince-king-structure](../passages/ezk-28-1-19-prince-king-structure.md)
- [nagid-melek-adjacent-address-headings](nagid-melek-adjacent-address-headings.md)

---
*Generated from: hebrew_parser.py --verse Eze 27:2; 28:12; 32:2; 32:16; search_strongs.py --lexicon H7015/H6969; KJV corpus lookup.*
*Last updated: 2026-05-07*
