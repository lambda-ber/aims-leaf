

# Slot: exposure_time 



URI: [aimsleaf:exposure_time](https://w3id.org/aims-leaf/exposure_time)
Alias: exposure_time

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [ExperimentalConditions](ExperimentalConditions.md) | Environmental and experimental conditions |  no  |
| [Movie](Movie.md) | Raw cryo-EM movie with frame-by-frame metadata for motion correction |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:exposure_time |
| native | aimsleaf:exposure_time |




## LinkML Source

<details>
```yaml
name: exposure_time
alias: exposure_time
domain_of:
- ExperimentRun
- Image
- ExperimentalConditions
range: string

```
</details>