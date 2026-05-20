

# Slot: facility_ror 


_Research Organization Registry (ROR) identifier for the facility_





URI: [aimsleaf:facility_ror](https://w3id.org/aims-leaf/facility_ror)
Alias: facility_ror

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |






## Properties

* Range: [Uriorcurie](Uriorcurie.md)

* Regex pattern: `^https://ror\.org/\w+$`




## Comments

* Persistent identifier for the facility organization
* Example: https://ror.org/02jbv0t02 (Lawrence Berkeley National Laboratory)

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:facility_ror |
| native | aimsleaf:facility_ror |




## LinkML Source

<details>
```yaml
name: facility_ror
description: Research Organization Registry (ROR) identifier for the facility
comments:
- Persistent identifier for the facility organization
- 'Example: https://ror.org/02jbv0t02 (Lawrence Berkeley National Laboratory)'
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: facility_ror
owner: Instrument
domain_of:
- Instrument
range: uriorcurie
pattern: ^https://ror\.org/\w+$

```
</details>