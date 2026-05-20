

# Slot: environmental_medium 


_The environmental material(s) immediately surrounding the sample or specimen at the time of sampling_





URI: [aimsleaf:environmental_medium](https://w3id.org/aims-leaf/environmental_medium)
Alias: environmental_medium

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | Plant sample info for AIMS-LEAF |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `.*\[ENVO:\d+\]$`




## Comments

* bluegrass field soil [ENVO:00005789]

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:environmental_medium |
| native | aimsleaf:environmental_medium |




## LinkML Source

<details>
```yaml
name: environmental_medium
description: The environmental material(s) immediately surrounding the sample or specimen
  at the time of sampling
comments:
- bluegrass field soil [ENVO:00005789]
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: environmental_medium
owner: PlantSample
domain_of:
- PlantSample
range: string
required: false
pattern: .*\[ENVO:\d+\]$

```
</details>