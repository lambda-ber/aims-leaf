

# Slot: slit_gap_horizontal 


_Horizontal slit gap aperture, typically specified in micrometers (µm). Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [aimsleaf:slit_gap_horizontal](https://w3id.org/aims-leaf/slit_gap_horizontal)
Alias: slit_gap_horizontal

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:slit_gap_horizontal |
| native | aimsleaf:slit_gap_horizontal |
| exact | ispyb:DataCollection.slitGapHorizontal |




## LinkML Source

<details>
```yaml
name: slit_gap_horizontal
description: Horizontal slit gap aperture, typically specified in micrometers (µm).
  Data providers may specify alternative units by including the unit in the QuantityValue.
from_schema: https://w3id.org/aims-leaf/
exact_mappings:
- ispyb:DataCollection.slitGapHorizontal
rank: 1000
alias: slit_gap_horizontal
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>