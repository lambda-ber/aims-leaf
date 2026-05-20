

# Class: XRFImage 


_X-ray fluorescence (XRF) image showing elemental distribution_





URI: [aimsleaf:XRFImage](https://w3id.org/aims-leaf/XRFImage)





```mermaid
 classDiagram
    class XRFImage
    click XRFImage href "../XRFImage/"
      DataFile <|-- XRFImage
        click DataFile href "../DataFile/"
      
      XRFImage : beam_energy
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : beam_energy
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : beam_size
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : beam_size
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : calibration_standard
        
      XRFImage : checksum
        
      XRFImage : creation_date
        
      XRFImage : data_type
        
          
    
        
        
        XRFImage --> "0..1" DataTypeEnum : data_type
        click DataTypeEnum href "../DataTypeEnum/"
    

        
      XRFImage : description
        
      XRFImage : detector_model
        
      XRFImage : detector_technology
        
          
    
        
        
        XRFImage --> "0..1" DetectorTechnologyEnum : detector_technology
        click DetectorTechnologyEnum href "../DetectorTechnologyEnum/"
    

        
      XRFImage : dimensions_x
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : dimensions_x
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : dimensions_y
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : dimensions_y
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : dwell_time
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : dwell_time
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : elements_measured
        
      XRFImage : file_format
        
          
    
        
        
        XRFImage --> "1" FileFormatEnum : file_format
        click FileFormatEnum href "../FileFormatEnum/"
    

        
      XRFImage : file_name
        
      XRFImage : file_path
        
      XRFImage : file_role
        
      XRFImage : file_size_bytes
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : file_size_bytes
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : flux
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : flux
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : id
        
      XRFImage : pixel_size
        
          
    
        
        
        XRFImage --> "0..1" QuantityValue : pixel_size
        click QuantityValue href "../QuantityValue/"
    

        
      XRFImage : related_entity
        
      XRFImage : source_type
        
          
    
        
        
        XRFImage --> "0..1" XRaySourceTypeEnum : source_type
        click XRaySourceTypeEnum href "../XRaySourceTypeEnum/"
    

        
      XRFImage : storage_uri
        
      XRFImage : title
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * [DataFile](DataFile.md)
        * **XRFImage**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [pixel_size](pixel_size.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Pixel size, typically specified in Angstroms | direct |
| [dimensions_x](dimensions_x.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Image width, typically specified in pixels | direct |
| [dimensions_y](dimensions_y.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Image height, typically specified in pixels | direct |
| [beam_energy](beam_energy.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | X-ray beam energy, typically specified in kiloelectronvolts (keV) | direct |
| [beam_size](beam_size.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | X-ray beam size, typically specified in micrometers | direct |
| [dwell_time](dwell_time.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Dwell time per pixel, typically specified in milliseconds | direct |
| [elements_measured](elements_measured.md) | * <br/> [String](String.md) | Elements detected and measured | direct |
| [source_type](source_type.md) | 0..1 <br/> [XRaySourceTypeEnum](XRaySourceTypeEnum.md) | X-ray source type (synchrotron or lab-source) | direct |
| [detector_technology](detector_technology.md) | 0..1 <br/> [DetectorTechnologyEnum](DetectorTechnologyEnum.md) | Type of X-ray detector technology used | direct |
| [detector_model](detector_model.md) | 0..1 <br/> [String](String.md) | Specific detector model used for XRF measurement | direct |
| [flux](flux.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Photon flux, typically specified in photons per second | direct |
| [calibration_standard](calibration_standard.md) | 0..1 <br/> [String](String.md) | Reference standard used for calibration | direct |
| [file_name](file_name.md) | 1 <br/> [String](String.md) | Name of the file | [DataFile](DataFile.md) |
| [file_path](file_path.md) | 0..1 <br/> [String](String.md) | Path to the file | [DataFile](DataFile.md) |
| [file_format](file_format.md) | 1 <br/> [FileFormatEnum](FileFormatEnum.md) | File format | [DataFile](DataFile.md) |
| [file_size_bytes](file_size_bytes.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | File size in bytes | [DataFile](DataFile.md) |
| [checksum](checksum.md) | 0..1 <br/> [String](String.md) | SHA-256 checksum for data integrity | [DataFile](DataFile.md) |
| [creation_date](creation_date.md) | 0..1 <br/> [Date](Date.md) | File creation date | [DataFile](DataFile.md) |
| [data_type](data_type.md) | 0..1 <br/> [DataTypeEnum](DataTypeEnum.md) | Type of data in the file | [DataFile](DataFile.md) |
| [storage_uri](storage_uri.md) | 0..1 <br/> [String](String.md) | Storage URI (S3, Globus, etc | [DataFile](DataFile.md) |
| [related_entity](related_entity.md) | 0..1 <br/> [String](String.md) | ID of the entity that owns this file | [DataFile](DataFile.md) |
| [file_role](file_role.md) | 0..1 <br/> [String](String.md) | Role of the file (raw, intermediate, final, diagnostic, metadata) | [DataFile](DataFile.md) |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... | [NamedThing](NamedThing.md) |
| [title](title.md) | 0..1 <br/> [String](String.md) | A human-readable name or title for this entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A detailed textual description of this entity | [NamedThing](NamedThing.md) |










## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:XRFImage |
| native | aimsleaf:XRFImage |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: XRFImage
description: X-ray fluorescence (XRF) image showing elemental distribution
from_schema: https://w3id.org/aims-leaf/
is_a: DataFile
attributes:
  pixel_size:
    name: pixel_size
    description: Pixel size, typically specified in Angstroms. Data providers may
      specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    domain_of:
    - Image
    - FTIRImage
    - XRFImage
    - RefinementParameters
    range: QuantityValue
    inlined: true
  dimensions_x:
    name: dimensions_x
    description: Image width, typically specified in pixels. Data providers may specify
      alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    domain_of:
    - Image
    - FTIRImage
    - XRFImage
    range: QuantityValue
    inlined: true
  dimensions_y:
    name: dimensions_y
    description: Image height, typically specified in pixels. Data providers may specify
      alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    domain_of:
    - Image
    - FTIRImage
    - XRFImage
    range: QuantityValue
    inlined: true
  beam_energy:
    name: beam_energy
    description: X-ray beam energy, typically specified in kiloelectronvolts (keV).
      Data providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - XRFImage
    - ExperimentalConditions
    range: QuantityValue
    inlined: true
  beam_size:
    name: beam_size
    description: X-ray beam size, typically specified in micrometers. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - XRFImage
    range: QuantityValue
    inlined: true
  dwell_time:
    name: dwell_time
    description: Dwell time per pixel, typically specified in milliseconds. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    domain_of:
    - ExperimentRun
    - XRFImage
    range: QuantityValue
    inlined: true
  elements_measured:
    name: elements_measured
    description: Elements detected and measured
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - XRFImage
    range: string
    multivalued: true
  source_type:
    name: source_type
    description: X-ray source type (synchrotron or lab-source)
    from_schema: https://w3id.org/aims-leaf/
    domain_of:
    - XRayInstrument
    - XRFImage
    range: XRaySourceTypeEnum
  detector_technology:
    name: detector_technology
    description: Type of X-ray detector technology used
    comments:
    - For XRF, typically energy-dispersive or wavelength-dispersive detectors
    from_schema: https://w3id.org/aims-leaf/
    domain_of:
    - CryoEMInstrument
    - XRayInstrument
    - XRFImage
    range: DetectorTechnologyEnum
  detector_model:
    name: detector_model
    description: Specific detector model used for XRF measurement
    from_schema: https://w3id.org/aims-leaf/
    domain_of:
    - CryoEMInstrument
    - XRayInstrument
    - XRFImage
    range: string
  flux:
    name: flux
    description: Photon flux, typically specified in photons per second. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    domain_of:
    - ExperimentRun
    - XRFImage
    range: QuantityValue
    inlined: true
  calibration_standard:
    name: calibration_standard
    description: Reference standard used for calibration
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - XRFImage
    range: string

```
</details>

### Induced

<details>
```yaml
name: XRFImage
description: X-ray fluorescence (XRF) image showing elemental distribution
from_schema: https://w3id.org/aims-leaf/
is_a: DataFile
attributes:
  pixel_size:
    name: pixel_size
    description: Pixel size, typically specified in Angstroms. Data providers may
      specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    alias: pixel_size
    owner: XRFImage
    domain_of:
    - Image
    - FTIRImage
    - XRFImage
    - RefinementParameters
    range: QuantityValue
    inlined: true
  dimensions_x:
    name: dimensions_x
    description: Image width, typically specified in pixels. Data providers may specify
      alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    alias: dimensions_x
    owner: XRFImage
    domain_of:
    - Image
    - FTIRImage
    - XRFImage
    range: QuantityValue
    inlined: true
  dimensions_y:
    name: dimensions_y
    description: Image height, typically specified in pixels. Data providers may specify
      alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    alias: dimensions_y
    owner: XRFImage
    domain_of:
    - Image
    - FTIRImage
    - XRFImage
    range: QuantityValue
    inlined: true
  beam_energy:
    name: beam_energy
    description: X-ray beam energy, typically specified in kiloelectronvolts (keV).
      Data providers may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: beam_energy
    owner: XRFImage
    domain_of:
    - XRFImage
    - ExperimentalConditions
    range: QuantityValue
    inlined: true
  beam_size:
    name: beam_size
    description: X-ray beam size, typically specified in micrometers. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: beam_size
    owner: XRFImage
    domain_of:
    - XRFImage
    range: QuantityValue
    inlined: true
  dwell_time:
    name: dwell_time
    description: Dwell time per pixel, typically specified in milliseconds. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    alias: dwell_time
    owner: XRFImage
    domain_of:
    - ExperimentRun
    - XRFImage
    range: QuantityValue
    inlined: true
  elements_measured:
    name: elements_measured
    description: Elements detected and measured
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: elements_measured
    owner: XRFImage
    domain_of:
    - XRFImage
    range: string
    multivalued: true
  source_type:
    name: source_type
    description: X-ray source type (synchrotron or lab-source)
    from_schema: https://w3id.org/aims-leaf/
    alias: source_type
    owner: XRFImage
    domain_of:
    - XRayInstrument
    - XRFImage
    range: XRaySourceTypeEnum
  detector_technology:
    name: detector_technology
    description: Type of X-ray detector technology used
    comments:
    - For XRF, typically energy-dispersive or wavelength-dispersive detectors
    from_schema: https://w3id.org/aims-leaf/
    alias: detector_technology
    owner: XRFImage
    domain_of:
    - CryoEMInstrument
    - XRayInstrument
    - XRFImage
    range: DetectorTechnologyEnum
  detector_model:
    name: detector_model
    description: Specific detector model used for XRF measurement
    from_schema: https://w3id.org/aims-leaf/
    alias: detector_model
    owner: XRFImage
    domain_of:
    - CryoEMInstrument
    - XRayInstrument
    - XRFImage
    range: string
  flux:
    name: flux
    description: Photon flux, typically specified in photons per second. Data providers
      may specify alternative units by including the unit in the QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    alias: flux
    owner: XRFImage
    domain_of:
    - ExperimentRun
    - XRFImage
    range: QuantityValue
    inlined: true
  calibration_standard:
    name: calibration_standard
    description: Reference standard used for calibration
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: calibration_standard
    owner: XRFImage
    domain_of:
    - XRFImage
    range: string
  file_name:
    name: file_name
    description: Name of the file
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: file_name
    owner: XRFImage
    domain_of:
    - DataFile
    - Image
    range: string
    required: true
  file_path:
    name: file_path
    description: Path to the file
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: file_path
    owner: XRFImage
    domain_of:
    - DataFile
    range: string
  file_format:
    name: file_format
    description: File format
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: file_format
    owner: XRFImage
    domain_of:
    - DataFile
    range: FileFormatEnum
    required: true
  file_size_bytes:
    name: file_size_bytes
    description: File size in bytes
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: file_size_bytes
    owner: XRFImage
    domain_of:
    - DataFile
    range: QuantityValue
    inlined: true
  checksum:
    name: checksum
    description: SHA-256 checksum for data integrity
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: checksum
    owner: XRFImage
    domain_of:
    - DataFile
    range: string
  creation_date:
    name: creation_date
    description: File creation date
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: creation_date
    owner: XRFImage
    domain_of:
    - DataFile
    range: date
  data_type:
    name: data_type
    description: Type of data in the file
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: data_type
    owner: XRFImage
    domain_of:
    - DataFile
    range: DataTypeEnum
  storage_uri:
    name: storage_uri
    description: Storage URI (S3, Globus, etc.)
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: storage_uri
    owner: XRFImage
    domain_of:
    - DataFile
    range: string
  related_entity:
    name: related_entity
    description: ID of the entity that owns this file
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: related_entity
    owner: XRFImage
    domain_of:
    - DataFile
    range: string
  file_role:
    name: file_role
    description: Role of the file (raw, intermediate, final, diagnostic, metadata)
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: file_role
    owner: XRFImage
    domain_of:
    - DataFile
    range: string
  id:
    name: id
    description: Globally unique identifier as an IRI or CURIE for machine processing
      and external references. Used for linking data across systems and semantic web
      integration.
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    identifier: true
    alias: id
    owner: XRFImage
    domain_of:
    - NamedThing
    - Attribute
    range: uriorcurie
    required: true
  title:
    name: title
    description: A human-readable name or title for this entity
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    slot_uri: dcterms:title
    alias: title
    owner: XRFImage
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A detailed textual description of this entity
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: description
    owner: XRFImage
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>