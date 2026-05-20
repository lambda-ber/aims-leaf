

# Slot: file_role 


_Role of the file (raw, intermediate, final, diagnostic, metadata)_





URI: [aimsleaf:file_role](https://w3id.org/aims-leaf/file_role)
Alias: file_role

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
| self | aimsleaf:file_role |
| native | aimsleaf:file_role |




## LinkML Source

<details>
```yaml
name: file_role
description: Role of the file (raw, intermediate, final, diagnostic, metadata)
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: file_role
owner: DataFile
domain_of:
- DataFile
range: string

```
</details>