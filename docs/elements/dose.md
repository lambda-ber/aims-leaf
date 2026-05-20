

# Slot: dose 


_Electron dose in e-/Å²_





URI: [aimsleaf:dose](https://w3id.org/aims-leaf/dose)
Alias: dose

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [Movie](Movie.md) | Raw cryo-EM movie with frame-by-frame metadata for motion correction |  no  |






## Properties

* Range: [QuantityValue](QuantityValue.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:dose |
| native | aimsleaf:dose |




## LinkML Source

<details>
```yaml
name: dose
description: Electron dose in e-/Å²
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: dose
owner: Image
domain_of:
- Image
range: QuantityValue
inlined: true

```
</details>