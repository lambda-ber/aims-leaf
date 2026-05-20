

# Slot: preparation_type 


_Type of sample preparation_





URI: [aimsleaf:preparation_type](https://w3id.org/aims-leaf/preparation_type)
Alias: preparation_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |  no  |
| [PlantSamplePreparation](PlantSamplePreparation.md) | A process that prepares a plant sample for analysis |  no  |






## Properties

* Range: [PreparationTypeEnum](PreparationTypeEnum.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:preparation_type |
| native | aimsleaf:preparation_type |




## LinkML Source

<details>
```yaml
name: preparation_type
description: Type of sample preparation
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: preparation_type
owner: SamplePreparation
domain_of:
- SamplePreparation
range: PreparationTypeEnum
required: true

```
</details>