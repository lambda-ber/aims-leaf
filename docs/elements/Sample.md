

# Class: Sample 


_A biological sample used in structural biology experiments_





URI: [aimsleaf:Sample](https://w3id.org/aims-leaf/Sample)





```mermaid
 classDiagram
    class Sample
    click Sample href "../Sample/"
      NamedThing <|-- Sample
        click NamedThing href "../NamedThing/"
      

      Sample <|-- PlantSample
        click PlantSample href "../PlantSample/"
      

      Sample : anatomy
        
          
    
        
        
        Sample --> "0..1" OntologyTerm : anatomy
        click OntologyTerm href "../OntologyTerm/"
    

        
      Sample : buffer_composition
        
          
    
        
        
        Sample --> "0..1" BufferComposition : buffer_composition
        click BufferComposition href "../BufferComposition/"
    

        
      Sample : cell_type
        
          
    
        
        
        Sample --> "0..1" OntologyTerm : cell_type
        click OntologyTerm href "../OntologyTerm/"
    

        
      Sample : concentration
        
          
    
        
        
        Sample --> "0..1" QuantityValue : concentration
        click QuantityValue href "../QuantityValue/"
    

        
      Sample : description
        
      Sample : id
        
      Sample : molecular_weight
        
          
    
        
        
        Sample --> "0..1" QuantityValue : molecular_weight
        click QuantityValue href "../QuantityValue/"
    

        
      Sample : organism
        
          
    
        
        
        Sample --> "0..1" OntologyTerm : organism
        click OntologyTerm href "../OntologyTerm/"
    

        
      Sample : parent_sample_id
        
          
    
        
        
        Sample --> "0..1" Sample : parent_sample_id
        click Sample href "../Sample/"
    

        
      Sample : preparation_method
        
      Sample : purity_percentage
        
          
    
        
        
        Sample --> "0..1" QuantityValue : purity_percentage
        click QuantityValue href "../QuantityValue/"
    

        
      Sample : quality_metrics
        
      Sample : sample_code
        
      Sample : sample_type
        
          
    
        
        
        Sample --> "1" SampleTypeEnum : sample_type
        click SampleTypeEnum href "../SampleTypeEnum/"
    

        
      Sample : storage_conditions
        
          
    
        
        
        Sample --> "0..1" StorageConditions : storage_conditions
        click StorageConditions href "../StorageConditions/"
    

        
      Sample : title
        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **Sample**
        * [PlantSample](PlantSample.md)



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [sample_code](sample_code.md) | 1 <br/> [String](String.md) | Human-friendly laboratory identifier or facility code for the sample (e | direct |
| [sample_type](sample_type.md) | 1 <br/> [SampleTypeEnum](SampleTypeEnum.md) | Type of biological sample | direct |
| [molecular_weight](molecular_weight.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Molecular weight, typically specified in kilodaltons (kDa) | direct |
| [concentration](concentration.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Sample concentration, typically specified in mg/mL or µM | direct |
| [buffer_composition](buffer_composition.md) | 0..1 <br/> [BufferComposition](BufferComposition.md) | Buffer composition including pH, salts, additives | direct |
| [preparation_method](preparation_method.md) | 0..1 <br/> [String](String.md) | Method used to prepare the sample | direct |
| [storage_conditions](storage_conditions.md) | 0..1 <br/> [StorageConditions](StorageConditions.md) | Storage conditions for the sample | direct |
| [organism](organism.md) | 0..1 <br/> [OntologyTerm](OntologyTerm.md) | Source organism for the sample (e | direct |
| [anatomy](anatomy.md) | 0..1 <br/> [OntologyTerm](OntologyTerm.md) | Anatomical part or tissue (e | direct |
| [cell_type](cell_type.md) | 0..1 <br/> [OntologyTerm](OntologyTerm.md) | Cell type if applicable (e | direct |
| [parent_sample_id](parent_sample_id.md) | 0..1 <br/> [Sample](Sample.md) | Reference to parent sample for derivation tracking | direct |
| [purity_percentage](purity_percentage.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Sample purity, typically specified as a percentage (range: 0-100) | direct |
| [quality_metrics](quality_metrics.md) | 0..1 <br/> [String](String.md) | Quality control metrics for the sample | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... | [NamedThing](NamedThing.md) |
| [title](title.md) | 0..1 <br/> [String](String.md) | A human-readable name or title for this entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A detailed textual description of this entity | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Dataset](Dataset.md) | [samples](samples.md) | range | [Sample](Sample.md) |
| [Sample](Sample.md) | [parent_sample_id](parent_sample_id.md) | range | [Sample](Sample.md) |
| [StudySampleAssociation](StudySampleAssociation.md) | [sample_id](sample_id.md) | range | [Sample](Sample.md) |
| [SampleDataAssociation](SampleDataAssociation.md) | [sample_id](sample_id.md) | range | [Sample](Sample.md) |
| [ExperimentSampleAssociation](ExperimentSampleAssociation.md) | [sample_id](sample_id.md) | range | [Sample](Sample.md) |
| [PlantSample](PlantSample.md) | [parent_sample_id](parent_sample_id.md) | range | [Sample](Sample.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:Sample |
| native | aimsleaf:Sample |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Sample
description: A biological sample used in structural biology experiments
from_schema: https://w3id.org/aims-leaf/
is_a: NamedThing
attributes:
  sample_code:
    name: sample_code
    description: Human-friendly laboratory identifier or facility code for the sample
      (e.g., 'ALS-12.3.1-SAMPLE-001', 'LAB-PROT-2024-01'). Used for local reference
      and tracking within laboratory workflows.
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - Sample
    required: true
  sample_type:
    name: sample_type
    description: Type of biological sample
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - Sample
    range: SampleTypeEnum
    required: true
  molecular_weight:
    name: molecular_weight
    description: Molecular weight, typically specified in kilodaltons (kDa). Data
      providers may specify alternative units (e.g., Daltons, g/mol) by including
      the unit in the QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - Sample
    range: QuantityValue
    inlined: true
  concentration:
    name: concentration
    description: Sample concentration, typically specified in mg/mL or µM. Data providers
      may specify alternative units (e.g., molar, g/L) by including the unit in the
      QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - Sample
    range: QuantityValue
    inlined: true
  buffer_composition:
    name: buffer_composition
    description: Buffer composition including pH, salts, additives
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - Sample
    - MeasurementConditions
    range: BufferComposition
  preparation_method:
    name: preparation_method
    description: Method used to prepare the sample
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - Sample
  storage_conditions:
    name: storage_conditions
    description: Storage conditions for the sample
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - Sample
    range: StorageConditions
  organism:
    name: organism
    description: Source organism for the sample (e.g., NCBITaxon:3702 for Arabidopsis
      thaliana)
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - Sample
    - AggregatedProteinView
    range: OntologyTerm
  anatomy:
    name: anatomy
    description: Anatomical part or tissue (e.g., UBERON:0008945 for leaf)
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - Sample
    range: OntologyTerm
  cell_type:
    name: cell_type
    description: Cell type if applicable (e.g., CL:0000057 for fibroblast)
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - Sample
    range: OntologyTerm
  parent_sample_id:
    name: parent_sample_id
    description: Reference to parent sample for derivation tracking
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - Sample
    range: Sample
  purity_percentage:
    name: purity_percentage
    description: 'Sample purity, typically specified as a percentage (range: 0-100).
      Data providers may specify as decimal fraction by including the unit in the
      QuantityValue.'
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - Sample
    range: QuantityValue
    inlined: true
  quality_metrics:
    name: quality_metrics
    description: Quality control metrics for the sample
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - Sample

```
</details>

### Induced

<details>
```yaml
name: Sample
description: A biological sample used in structural biology experiments
from_schema: https://w3id.org/aims-leaf/
is_a: NamedThing
attributes:
  sample_code:
    name: sample_code
    description: Human-friendly laboratory identifier or facility code for the sample
      (e.g., 'ALS-12.3.1-SAMPLE-001', 'LAB-PROT-2024-01'). Used for local reference
      and tracking within laboratory workflows.
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: sample_code
    owner: Sample
    domain_of:
    - Sample
    range: string
    required: true
  sample_type:
    name: sample_type
    description: Type of biological sample
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: sample_type
    owner: Sample
    domain_of:
    - Sample
    range: SampleTypeEnum
    required: true
  molecular_weight:
    name: molecular_weight
    description: Molecular weight, typically specified in kilodaltons (kDa). Data
      providers may specify alternative units (e.g., Daltons, g/mol) by including
      the unit in the QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: molecular_weight
    owner: Sample
    domain_of:
    - Sample
    range: QuantityValue
    inlined: true
  concentration:
    name: concentration
    description: Sample concentration, typically specified in mg/mL or µM. Data providers
      may specify alternative units (e.g., molar, g/L) by including the unit in the
      QuantityValue.
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: concentration
    owner: Sample
    domain_of:
    - Sample
    range: QuantityValue
    inlined: true
  buffer_composition:
    name: buffer_composition
    description: Buffer composition including pH, salts, additives
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: buffer_composition
    owner: Sample
    domain_of:
    - Sample
    - MeasurementConditions
    range: BufferComposition
  preparation_method:
    name: preparation_method
    description: Method used to prepare the sample
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: preparation_method
    owner: Sample
    domain_of:
    - Sample
    range: string
  storage_conditions:
    name: storage_conditions
    description: Storage conditions for the sample
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: storage_conditions
    owner: Sample
    domain_of:
    - Sample
    range: StorageConditions
  organism:
    name: organism
    description: Source organism for the sample (e.g., NCBITaxon:3702 for Arabidopsis
      thaliana)
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: organism
    owner: Sample
    domain_of:
    - Sample
    - AggregatedProteinView
    range: OntologyTerm
  anatomy:
    name: anatomy
    description: Anatomical part or tissue (e.g., UBERON:0008945 for leaf)
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: anatomy
    owner: Sample
    domain_of:
    - Sample
    range: OntologyTerm
  cell_type:
    name: cell_type
    description: Cell type if applicable (e.g., CL:0000057 for fibroblast)
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: cell_type
    owner: Sample
    domain_of:
    - Sample
    range: OntologyTerm
  parent_sample_id:
    name: parent_sample_id
    description: Reference to parent sample for derivation tracking
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: parent_sample_id
    owner: Sample
    domain_of:
    - Sample
    range: Sample
  purity_percentage:
    name: purity_percentage
    description: 'Sample purity, typically specified as a percentage (range: 0-100).
      Data providers may specify as decimal fraction by including the unit in the
      QuantityValue.'
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: purity_percentage
    owner: Sample
    domain_of:
    - Sample
    range: QuantityValue
    inlined: true
  quality_metrics:
    name: quality_metrics
    description: Quality control metrics for the sample
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: quality_metrics
    owner: Sample
    domain_of:
    - Sample
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
    owner: Sample
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
    owner: Sample
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A detailed textual description of this entity
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: description
    owner: Sample
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>