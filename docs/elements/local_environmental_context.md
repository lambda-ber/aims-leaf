

# Slot: local_environmental_context 


_The entity or entities which are in the sample or specimen's local vicinity and which you believe have significant causal influences on your sample or specimen_





URI: [aimsleaf:local_environmental_context](https://w3id.org/aims-leaf/local_environmental_context)
Alias: local_environmental_context

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | Plant sample info for AIMS-LEAF |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `.*\[ENVO:\d+\]$`




## Comments

* hillside [ENVO:01000333]

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:local_environmental_context |
| native | aimsleaf:local_environmental_context |




## LinkML Source

<details>
```yaml
name: local_environmental_context
description: The entity or entities which are in the sample or specimen's local vicinity
  and which you believe have significant causal influences on your sample or specimen
comments:
- hillside [ENVO:01000333]
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: local_environmental_context
owner: PlantSample
domain_of:
- PlantSample
range: string
required: false
pattern: .*\[ENVO:\d+\]$

```
</details>