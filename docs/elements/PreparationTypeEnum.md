# Enum: PreparationTypeEnum 




_Types of sample preparation_



URI: [aimsleaf:PreparationTypeEnum](https://w3id.org/aims-leaf/PreparationTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| cryo_em | None | Cryo-EM preparation |
| xray_crystallography | None | X-ray crystallography preparation |
| saxs | None | SAXS/WAXS preparation |
| sans | None | SANS preparation |
| protein_expression | None | Protein expression in host cells |
| protein_purification | None | Protein purification |
| negative_stain | None | Negative stain EM preparation |
| thin_section | None | Petrographic thin-section preparation |
| thick_section | None | Petrographic thick-section preparation |
| microtome_section | None | Microtome preparation |
| cryo_section | None | Cryo-section microtome preparation |
| ultratome_section | None | Ultra-Microtome preparation |
| whole_mount | None | Whole mount of sample |
| other_mount | None | Other mount of sample |




## Slots

| Name | Description |
| ---  | --- |
| [preparation_type](preparation_type.md) | Type of sample preparation |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/






## LinkML Source

<details>
```yaml
name: PreparationTypeEnum
description: Types of sample preparation
from_schema: https://w3id.org/aims-leaf/
rank: 1000
permissible_values:
  cryo_em:
    text: cryo_em
    description: Cryo-EM preparation
  xray_crystallography:
    text: xray_crystallography
    description: X-ray crystallography preparation
  saxs:
    text: saxs
    description: SAXS/WAXS preparation
  sans:
    text: sans
    description: SANS preparation
  protein_expression:
    text: protein_expression
    description: Protein expression in host cells
  protein_purification:
    text: protein_purification
    description: Protein purification
  negative_stain:
    text: negative_stain
    description: Negative stain EM preparation
  thin_section:
    text: thin_section
    description: Petrographic thin-section preparation
  thick_section:
    text: thick_section
    description: Petrographic thick-section preparation
  microtome_section:
    text: microtome_section
    description: Microtome preparation
  cryo_section:
    text: cryo_section
    description: Cryo-section microtome preparation
  ultratome_section:
    text: ultratome_section
    description: Ultra-Microtome preparation
  whole_mount:
    text: whole_mount
    description: Whole mount of sample
  other_mount:
    text: other_mount
    description: Other mount of sample

```
</details>