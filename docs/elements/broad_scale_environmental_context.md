

# Slot: broad_scale_environmental_context 


_The major environmental system the sample or specimen came from. The system(s) identified should have a coarse spatial grain_





URI: [aimsleaf:broad_scale_environmental_context](https://w3id.org/aims-leaf/broad_scale_environmental_context)
Alias: broad_scale_environmental_context

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | Plant sample info for AIMS-LEAF |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `.*\[ENVO:\d+\]$`




## Comments

* rangeland biome [ENVO:01000247]

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:broad_scale_environmental_context |
| native | aimsleaf:broad_scale_environmental_context |




## LinkML Source

<details>
```yaml
name: broad_scale_environmental_context
description: The major environmental system the sample or specimen came from. The
  system(s) identified should have a coarse spatial grain
comments:
- rangeland biome [ENVO:01000247]
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: broad_scale_environmental_context
owner: PlantSample
domain_of:
- PlantSample
range: string
required: false
pattern: .*\[ENVO:\d+\]$

```
</details>