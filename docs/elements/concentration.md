

# Slot: concentration 


_Sample concentration, typically specified in mg/mL or µM. Data providers may specify alternative units (e.g., molar, g/L) by including the unit in the QuantityValue._





URI: [aimsleaf:concentration](https://w3id.org/aims-leaf/concentration)
Alias: concentration

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |
| [PlantSample](PlantSample.md) | Plant sample info for AIMS-LEAF |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:concentration |
| native | aimsleaf:concentration |




## LinkML Source

<details>
```yaml
name: concentration
description: Sample concentration, typically specified in mg/mL or µM. Data providers
  may specify alternative units (e.g., molar, g/L) by including the unit in the QuantityValue.
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: concentration
owner: Sample
domain_of:
- Sample
range: QuantityValue
inlined: true

```
</details>