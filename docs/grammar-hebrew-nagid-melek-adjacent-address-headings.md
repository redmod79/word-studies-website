# `nagid` vs. `melek` in Adjacent Prophetic Address Headings (Hebrew)

## Definition

Biblical Hebrew can distinguish adjacent prophetic address headings by changing the title noun while preserving the same target proper name. In Ezekiel 28, `נְגִיד צֹר` ("prince/chief of Tyre") and `מֶלֶךְ צֹור` ("king of Tyre") occur in adjacent oracle headings. Grammatically, these are separate construct chains with different head nouns, not variant spellings of one title.

1. **`nagid` heading** - a commander, leader, ruler, prince/chief; often office/function oriented.
2. **`melek` heading** - king; royal title and sovereignty marker.
3. **Adjacent heading contrast** - repeated prophetic commission plus changed title marks a new address unit.

## Form Recognition

- `נְגִיד` is parsed `Noun.ms.Cst` before the proper name `צֹר`.
- `מֶלֶךְ` is parsed `Noun.ms.Cst` before the proper name `צֹור`.
- Both form construct chains: `[title.Cst] + [proper-name.Abs]`.
- The contrast is structural when a new speech formula or commission introduces the second title.

## Functions with Examples

### 1. `nagid` as Address Heading

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Eze 28:2 | לִנְגִיד צֹר | Prep + `נְגִיד` Noun.ms.Cst + PropN | "unto the prince of Tyrus" |
| Dan 9:25 | נָגִיד | Noun.ms.Abs/Cst by context | "Messiah the Prince" |
| Dan 9:26 | נָגִיד | Noun.ms.Cst in phrase | "the prince that shall come" |

`search_strongs.py --lexicon H5057` gives `נָגִיד` as a masculine noun, BLB count 44, with glosses including captain, chief, governor, leader, prince, ruler.

### 2. `melek` as Address Heading

| Reference | Hebrew | Parsing | KJV Translation |
|-----------|--------|---------|-----------------|
| Eze 28:12 | עַל־מֶלֶךְ צֹור | Prep + `מֶלֶךְ` Noun.ms.Cst + PropN | "upon the king of Tyrus" |
| Eze 32:2 | פַּרְעֹה מֶלֶךְ־מִצְרַיִם | noun + `מֶלֶךְ` Noun.ms.Cst + PropN | "Pharaoh king of Egypt" |
| Isa 14:4 | עַל־מֶלֶךְ בָּבֶל | Prep + `מֶלֶךְ` Noun.ms.Cst + PropN | "against the king of Babylon" |

`search_strongs.py --lexicon H4428` gives `מֶלֶךְ` as a masculine noun meaning king/royal.

## Ezekiel 28 Diagnostic

| Feature | Ezek 28:2 | Ezek 28:12 |
|---------|-----------|------------|
| Speech opener | `אֱמֹר` Qal imperative 2ms | `שָׂא` Qal imperative 2ms + `קִינָה` |
| Addressee title | `נְגִיד` | `מֶלֶךְ` |
| Proper name | `צֹר` | `צֹור` |
| Genre | Direct judgment oracle | Lament/qinah oracle |
| Formula | `כֹּה אָמַר אֲדֹנָי יְהוִה` | `כֹּה אָמַר אֲדֹנָי יְהוִה` |

The shared proper name and messenger formula keep both units within the Tyre complex. The changed title and qinah command mark a distinct address movement.

## Contrast with Related Forms

| Form | Grammatical Behavior | Interpretive Boundary |
|------|----------------------|-----------------------|
| `נְגִיד צֹר` | construct chain with office title as head | Marks an addressee as prince/chief; does not grammatically prove a different person |
| `מֶלֶךְ צֹור` | construct chain with royal title as head | Marks an addressee as king; does not grammatically prove a different person |
| Apposition | Two nominals re-identify one referent inside one phrase | Ezek 28:2 and 28:12 are in separate headings, not a single appositional phrase |
| Corporate personification | Singular ruler/city title can speak for a polity | See [prophetic-double-address-corporate-personification](prophetic-double-address-corporate-personification.md) |

## Cross-References

- [construct-state](construct-state.md)
- [qinah-lamentation-foreign-oracles](qinah-lamentation-foreign-oracles.md)
- [ezk-28-1-19-prince-king-structure](../passages/ezk-28-1-19-prince-king-structure.md)
- [isa-14-ezek-28-self-deification](../passages/isa-14-ezek-28-self-deification.md)

---
*Generated from: hebrew_parser.py --verse/--construct Eze 28:2,12; Eze 32:2; search_strongs.py --lexicon H5057/H4428; KJV corpus lookup.*
*Last updated: 2026-05-07*
