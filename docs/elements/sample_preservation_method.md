

# Slot: sample_preservation_method 


_The method employed for preserving or fixing the tissue. Use Fresh if the sample was harvested immdiately before processing. Select from the following options: [Formaldehyde, N2 Freeze, FFPE, Fresh]_





URI: [aimsleaf:sample_preservation_method](https://w3id.org/aims-leaf/sample_preservation_method)
Alias: sample_preservation_method

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSamplePreparation](PlantSamplePreparation.md) | A process that prepares a plant sample for analysis |  no  |






## Properties

* Range: [SamplePreservationEnum](SamplePreservationEnum.md)




## Comments

* N2 freeze

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:sample_preservation_method |
| native | aimsleaf:sample_preservation_method |




## LinkML Source

<details>
```yaml
name: sample_preservation_method
description: 'The method employed for preserving or fixing the tissue. Use Fresh if
  the sample was harvested immdiately before processing. Select from the following
  options: [Formaldehyde, N2 Freeze, FFPE, Fresh]'
comments:
- N2 freeze
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: sample_preservation_method
owner: PlantSamplePreparation
domain_of:
- PlantSamplePreparation
range: SamplePreservationEnum
required: false

```
</details>