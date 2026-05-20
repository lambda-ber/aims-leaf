

# Slot: instrument_code 


_Human-friendly facility or laboratory identifier for the instrument (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and equipment tracking._





URI: [aimsleaf:instrument_code](https://w3id.org/aims-leaf/instrument_code)
Alias: instrument_code

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:instrument_code |
| native | aimsleaf:instrument_code |




## LinkML Source

<details>
```yaml
name: instrument_code
description: Human-friendly facility or laboratory identifier for the instrument (e.g.,
  'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and
  equipment tracking.
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: instrument_code
owner: Instrument
domain_of:
- Instrument
range: string
required: true

```
</details>