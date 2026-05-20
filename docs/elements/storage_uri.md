

# Slot: storage_uri 


_Storage URI (S3, Globus, etc.)_





URI: [aimsleaf:storage_uri](https://w3id.org/aims-leaf/storage_uri)
Alias: storage_uri

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
| self | aimsleaf:storage_uri |
| native | aimsleaf:storage_uri |




## LinkML Source

<details>
```yaml
name: storage_uri
description: Storage URI (S3, Globus, etc.)
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: storage_uri
owner: DataFile
domain_of:
- DataFile
range: string

```
</details>