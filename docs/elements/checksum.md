

# Slot: checksum 


_SHA-256 checksum for data integrity_





URI: [aimsleaf:checksum](https://w3id.org/aims-leaf/checksum)
Alias: checksum

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataFile](DataFile.md) | A data file generated or used in the study |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:checksum |
| native | aimsleaf:checksum |




## LinkML Source

<details>
```yaml
name: checksum
description: SHA-256 checksum for data integrity
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: checksum
owner: DataFile
domain_of:
- DataFile
range: string

```
</details>