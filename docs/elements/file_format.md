

# Slot: file_format 


_File format_





URI: [aimsleaf:file_format](https://w3id.org/aims-leaf/file_format)
Alias: file_format

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [DataFile](DataFile.md) | A data file generated or used in the study |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |






## Properties

* Range: [FileFormatEnum](FileFormatEnum.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:file_format |
| native | aimsleaf:file_format |




## LinkML Source

<details>
```yaml
name: file_format
description: File format
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: file_format
owner: DataFile
domain_of:
- DataFile
range: FileFormatEnum
required: true

```
</details>