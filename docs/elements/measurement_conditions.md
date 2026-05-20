

# Slot: measurement_conditions 


_Conditions under which measurement was made. If multiple sets of conditions were used, this will represent that the same values were obtained under different conditions. If values differ under different conditions, separate BiophysicalProperty instances should be created._





URI: [aimsleaf:measurement_conditions](https://w3id.org/aims-leaf/measurement_conditions)
Alias: measurement_conditions

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [BiophysicalProperty](BiophysicalProperty.md) | Measured or calculated biophysical properties |  no  |






## Properties

* Range: [MeasurementConditions](MeasurementConditions.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:measurement_conditions |
| native | aimsleaf:measurement_conditions |




## LinkML Source

<details>
```yaml
name: measurement_conditions
description: Conditions under which measurement was made. If multiple sets of conditions
  were used, this will represent that the same values were obtained under different
  conditions. If values differ under different conditions, separate BiophysicalProperty
  instances should be created.
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: measurement_conditions
owner: BiophysicalProperty
domain_of:
- BiophysicalProperty
range: MeasurementConditions
multivalued: true
inlined: true
inlined_as_list: true

```
</details>