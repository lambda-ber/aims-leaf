

# Slot: undulator_gap 


_Undulator gap setting, typically specified in millimeters (mm). Data providers may specify alternative units by including the unit in the QuantityValue. Primary undulator gap for beamlines with insertion devices._





URI: [aimsleaf:undulator_gap](https://w3id.org/aims-leaf/undulator_gap)
Alias: undulator_gap

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Comments

* Primary undulator gap for beamlines with insertion devices

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:undulator_gap |
| native | aimsleaf:undulator_gap |
| exact | ispyb:DataCollection.undulatorGap1 |




## LinkML Source

<details>
```yaml
name: undulator_gap
description: Undulator gap setting, typically specified in millimeters (mm). Data
  providers may specify alternative units by including the unit in the QuantityValue.
  Primary undulator gap for beamlines with insertion devices.
comments:
- Primary undulator gap for beamlines with insertion devices
from_schema: https://w3id.org/aims-leaf/
exact_mappings:
- ispyb:DataCollection.undulatorGap1
rank: 1000
alias: undulator_gap
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>