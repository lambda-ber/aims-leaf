

# Slot: start_angle 


_Starting rotation angle, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [aimsleaf:start_angle](https://w3id.org/aims-leaf/start_angle)
Alias: start_angle

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
| self | aimsleaf:start_angle |
| native | aimsleaf:start_angle |
| exact | nsls2:Start_angle, imgCIF:_diffrn_scan_axis.angle_start, ispyb:DataCollection.axisStart |




## LinkML Source

<details>
```yaml
name: start_angle
description: Starting rotation angle, typically specified in degrees. Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: https://w3id.org/aims-leaf/
exact_mappings:
- nsls2:Start_angle
- imgCIF:_diffrn_scan_axis.angle_start
- ispyb:DataCollection.axisStart
rank: 1000
alias: start_angle
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>