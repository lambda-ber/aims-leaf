

# Slot: sample_type 


_Type of biological sample_





URI: [aimsleaf:sample_type](https://w3id.org/aims-leaf/sample_type)
Alias: sample_type

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |
| [PlantSample](PlantSample.md) | Plant sample info for AIMS-LEAF |  no  |






## Properties

* Range: [SampleTypeEnum](SampleTypeEnum.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:sample_type |
| native | aimsleaf:sample_type |




## LinkML Source

<details>
```yaml
name: sample_type
description: Type of biological sample
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: sample_type
owner: Sample
domain_of:
- Sample
range: SampleTypeEnum
required: true

```
</details>