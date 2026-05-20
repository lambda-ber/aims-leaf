

# Slot: wavelength 


_X-ray wavelength, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [aimsleaf:wavelength](https://w3id.org/aims-leaf/wavelength)
Alias: wavelength

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
| self | aimsleaf:wavelength |
| native | aimsleaf:wavelength |
| exact | nsls2:Wavelength, imgCIF:_diffrn_radiation_wavelength.wavelength, mmCIF:_diffrn_radiation_wavelength.wavelength, ispyb:DataCollection.wavelength |




## LinkML Source

<details>
```yaml
name: wavelength
description: X-ray wavelength, typically specified in Angstroms (Å). Data providers
  may specify alternative units by including the unit in the QuantityValue.
from_schema: https://w3id.org/aims-leaf/
exact_mappings:
- nsls2:Wavelength
- imgCIF:_diffrn_radiation_wavelength.wavelength
- mmCIF:_diffrn_radiation_wavelength.wavelength
- ispyb:DataCollection.wavelength
rank: 1000
alias: wavelength
owner: ExperimentRun
domain_of:
- ExperimentRun
range: QuantityValue
inlined: true

```
</details>