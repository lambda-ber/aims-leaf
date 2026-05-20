

# Slot: beamline_id 


_Beamline identifier at synchrotron/neutron facility_





URI: [mmCIF:_diffrn_source.pdbx_synchrotron_beamline](http://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_diffrn_source.pdbx_synchrotron_beamline)
Alias: beamline_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |






## Properties

* Range: [String](String.md)




## Comments

* Use facility-specific naming convention
* Examples: '12.3.1' (ALS), '17-ID-1' (NSLS-II), 'I04' (Diamond)

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mmCIF:_diffrn_source.pdbx_synchrotron_beamline |
| native | aimsleaf:beamline_id |




## LinkML Source

<details>
```yaml
name: beamline_id
description: Beamline identifier at synchrotron/neutron facility
comments:
- Use facility-specific naming convention
- 'Examples: ''12.3.1'' (ALS), ''17-ID-1'' (NSLS-II), ''I04'' (Diamond)'
from_schema: https://w3id.org/aims-leaf/
rank: 1000
slot_uri: mmCIF:_diffrn_source.pdbx_synchrotron_beamline
alias: beamline_id
owner: Instrument
domain_of:
- Instrument
range: string

```
</details>