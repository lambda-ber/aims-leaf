

# Slot: defocus 


_Defocus value, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue._





URI: [aimsleaf:defocus](https://w3id.org/aims-leaf/defocus)
Alias: defocus

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [Movie](Movie.md) | Raw cryo-EM movie with frame-by-frame metadata for motion correction |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:defocus |
| native | aimsleaf:defocus |




## LinkML Source

<details>
```yaml
name: defocus
description: Defocus value, typically specified in micrometers. Data providers may
  specify alternative units by including the unit in the QuantityValue.
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: defocus
owner: Image2D
domain_of:
- Image2D
range: QuantityValue
inlined: true

```
</details>