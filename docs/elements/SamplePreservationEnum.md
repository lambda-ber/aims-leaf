# Enum: SamplePreservationEnum 




_The method employed for preserving or fixing the tissue. Use Fresh if the sample was harvested immdiately before processing. Select from the following options: [Formaldehyde, N2 Freeze, FFPE, Fresh]_



URI: [aimsleaf:SamplePreservationEnum](https://w3id.org/aims-leaf/SamplePreservationEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| N2_freeze | None | Plunge freezing in liquid nitrogen |
| Formaldehyde | None | Formeldehyde fixation |
| FFPE | None | FFPE |
| Fresh | None | Fresh harvest |
| Other | None | Other, leave details in comment |




## Slots

| Name | Description |
| ---  | --- |
| [sample_preservation_method](sample_preservation_method.md) | The method employed for preserving or fixing the tissue |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/






## LinkML Source

<details>
```yaml
name: SamplePreservationEnum
description: 'The method employed for preserving or fixing the tissue. Use Fresh if
  the sample was harvested immdiately before processing. Select from the following
  options: [Formaldehyde, N2 Freeze, FFPE, Fresh]'
from_schema: https://w3id.org/aims-leaf/
rank: 1000
permissible_values:
  N2_freeze:
    text: N2_freeze
    description: Plunge freezing in liquid nitrogen
  Formaldehyde:
    text: Formaldehyde
    description: Formeldehyde fixation
  FFPE:
    text: FFPE
    description: FFPE
  Fresh:
    text: Fresh
    description: Fresh harvest
  Other:
    text: Other
    description: Other, leave details in comment

```
</details>