

# Slot: detector_distance 


_Distance from sample to detector, typically specified in millimeters (mm). Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [aimsleaf:detector_distance](https://w3id.org/aims-leaf/detector_distance)
Alias: detector_distance

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
| self | aimsleaf:detector_distance |
| native | aimsleaf:detector_distance |
| exact | nsls2:Detector_distance, imgCIF:_diffrn_measurement.sample_detector_distance, mmCIF:_diffrn_detector.distance, ispyb:DataCollection.detectorDistance |




## LinkML Source

<details>
```yaml
name: detector_distance
description: Distance from sample to detector, typically specified in millimeters
  (mm). Data providers may specify alternative units by including the unit in the
  QuantityValue.
from_schema: https://w3id.org/aims-leaf/
exact_mappings:
- nsls2:Detector_distance
- imgCIF:_diffrn_measurement.sample_detector_distance
- mmCIF:_diffrn_detector.distance
- ispyb:DataCollection.detectorDistance
rank: 1000
alias: detector_distance
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>