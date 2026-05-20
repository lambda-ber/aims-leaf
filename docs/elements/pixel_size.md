

# Slot: pixel_size 



URI: [aimsleaf:pixel_size](https://w3id.org/aims-leaf/pixel_size)
Alias: pixel_size

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [RefinementParameters](RefinementParameters.md) | Parameters specific to 3D refinement workflows |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [Movie](Movie.md) | Raw cryo-EM movie with frame-by-frame metadata for motion correction |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:pixel_size |
| native | aimsleaf:pixel_size |




## LinkML Source

<details>
```yaml
name: pixel_size
alias: pixel_size
domain_of:
- Image
- FTIRImage
- XRFImage
- RefinementParameters
range: string

```
</details>