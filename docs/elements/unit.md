

# Slot: unit 


_The unit of measurement. Should be taken from the UCUM unit collection or the Unit Ontology. Examples include Angstroms, micrometers, kilodaltons, degrees._





URI: [aimsleaf:unit](https://w3id.org/aims-leaf/unit)
Alias: unit

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [QuantityValue](QuantityValue.md) | A simple quantity value, representing a measurement with a numeric value and ... |  yes  |
| [BiophysicalProperty](BiophysicalProperty.md) | Measured or calculated biophysical properties |  no  |






## Properties

* Range: [String](String.md)



## Aliases


* scale


## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:unit |
| native | aimsleaf:unit |
| undefined | nmdc:unit, qud:unit, schema:unitCode, UO:0000000 |




## LinkML Source

<details>
```yaml
name: unit
description: The unit of measurement. Should be taken from the UCUM unit collection
  or the Unit Ontology. Examples include Angstroms, micrometers, kilodaltons, degrees.
from_schema: https://w3id.org/aims-leaf/
aliases:
- scale
mappings:
- nmdc:unit
- qud:unit
- schema:unitCode
- UO:0000000
rank: 1000
alias: unit
domain_of:
- QuantityValue
- BiophysicalProperty
range: string

```
</details>