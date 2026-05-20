# Enum: DataTypeEnum 




_Types of data_



URI: [aimsleaf:DataTypeEnum](https://w3id.org/aims-leaf/DataTypeEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| micrograph | None | Electron micrograph |
| diffraction | None | Diffraction pattern |
| scattering | None | Scattering data |
| particles | None | Particle stack |
| volume | None | 3D volume |
| model | None | Atomic model |
| metadata | None | Metadata file |
| raw_data | None | Raw experimental data |
| processed_data | None | Processed data |
| movie | None | Raw cryo-EM movie |
| motion_corrected | None | Motion-corrected micrograph |
| ctf_estimation | None | CTF estimation results |
| particle_coordinates | None | Particle picking coordinates |
| class_averages | None | 2D or 3D class averages |
| fsc_curve | None | Fourier Shell Correlation data |
| map_half | None | Half-map for gold-standard refinement |
| validation_report | None | Validation report |
| xrf_image | None | XRF elemental image |
| ir_image | None | IR/Raman vibrational band image |
| chemical_image | None | Image of specific chemical species, from XRF-XAS Imaging ir FTIR/Raman Imagin... |




## Slots

| Name | Description |
| ---  | --- |
| [data_type](data_type.md) | Type of data in the file |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/






## LinkML Source

<details>
```yaml
name: DataTypeEnum
description: Types of data
from_schema: https://w3id.org/aims-leaf/
rank: 1000
permissible_values:
  micrograph:
    text: micrograph
    description: Electron micrograph
  diffraction:
    text: diffraction
    description: Diffraction pattern
  scattering:
    text: scattering
    description: Scattering data
  particles:
    text: particles
    description: Particle stack
  volume:
    text: volume
    description: 3D volume
  model:
    text: model
    description: Atomic model
  metadata:
    text: metadata
    description: Metadata file
  raw_data:
    text: raw_data
    description: Raw experimental data
  processed_data:
    text: processed_data
    description: Processed data
  movie:
    text: movie
    description: Raw cryo-EM movie
  motion_corrected:
    text: motion_corrected
    description: Motion-corrected micrograph
  ctf_estimation:
    text: ctf_estimation
    description: CTF estimation results
  particle_coordinates:
    text: particle_coordinates
    description: Particle picking coordinates
  class_averages:
    text: class_averages
    description: 2D or 3D class averages
  fsc_curve:
    text: fsc_curve
    description: Fourier Shell Correlation data
  map_half:
    text: map_half
    description: Half-map for gold-standard refinement
  validation_report:
    text: validation_report
    description: Validation report
  xrf_image:
    text: xrf_image
    description: XRF elemental image
  ir_image:
    text: ir_image
    description: IR/Raman vibrational band image
  chemical_image:
    text: chemical_image
    description: Image of specific chemical species, from XRF-XAS Imaging ir FTIR/Raman
      Imaging

```
</details>