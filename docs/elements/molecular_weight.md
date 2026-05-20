

# Slot: molecular_weight 


_Molecular weight, typically specified in kilodaltons (kDa). Data providers may specify alternative units (e.g., Daltons, g/mol) by including the unit in the QuantityValue._





URI: [aimsleaf:molecular_weight](https://w3id.org/aims-leaf/molecular_weight)
Alias: molecular_weight

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
| self | aimsleaf:molecular_weight |
| native | aimsleaf:molecular_weight |




## LinkML Source

<details>
```yaml
name: molecular_weight
description: Molecular weight, typically specified in kilodaltons (kDa). Data providers
  may specify alternative units (e.g., Daltons, g/mol) by including the unit in the
  QuantityValue.
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: molecular_weight
owner: Sample
domain_of:
- Sample
range: QuantityValue
inlined: true

```
</details>