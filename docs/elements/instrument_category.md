

# Slot: instrument_category 


_Category distinguishing beamlines from laboratory equipment_





URI: [aimsleaf:instrument_category](https://w3id.org/aims-leaf/instrument_category)
Alias: instrument_category

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |






## Properties

* Range: [InstrumentCategoryEnum](InstrumentCategoryEnum.md)




## Comments

* Use SYNCHROTRON_BEAMLINE for synchrotron beamlines
* Use ELECTRON_MICROSCOPE for cryo-EM instruments

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:instrument_category |
| native | aimsleaf:instrument_category |




## LinkML Source

<details>
```yaml
name: instrument_category
description: Category distinguishing beamlines from laboratory equipment
comments:
- Use SYNCHROTRON_BEAMLINE for synchrotron beamlines
- Use ELECTRON_MICROSCOPE for cryo-EM instruments
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: instrument_category
owner: Instrument
domain_of:
- Instrument
range: InstrumentCategoryEnum

```
</details>