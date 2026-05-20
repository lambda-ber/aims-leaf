

# Class: WorkflowRun 


_A computational processing workflow execution_





URI: [aimsleaf:WorkflowRun](https://w3id.org/aims-leaf/WorkflowRun)





```mermaid
 classDiagram
    class WorkflowRun
    click WorkflowRun href "../WorkflowRun/"
      NamedThing <|-- WorkflowRun
        click NamedThing href "../NamedThing/"
      
      WorkflowRun : additional_software
        
      WorkflowRun : description
        
      WorkflowRun : id
        
      WorkflowRun : parameters_file_path
        
      WorkflowRun : processing_level
        
          
    
        
        
        WorkflowRun --> "0..1" QuantityValue : processing_level
        click QuantityValue href "../QuantityValue/"
    

        
      WorkflowRun : processing_parameters
        
      WorkflowRun : software_name
        
      WorkflowRun : software_version
        
      WorkflowRun : title
        
      WorkflowRun : workflow_code
        
      WorkflowRun : workflow_type
        
          
    
        
        
        WorkflowRun --> "1" WorkflowTypeEnum : workflow_type
        click WorkflowTypeEnum href "../WorkflowTypeEnum/"
    

        
      
```





## Inheritance
* [NamedThing](NamedThing.md)
    * **WorkflowRun**



## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [workflow_code](workflow_code.md) | 1 <br/> [String](String.md) | Human-friendly identifier for the computational workflow run (e | direct |
| [workflow_type](workflow_type.md) | 1 <br/> [WorkflowTypeEnum](WorkflowTypeEnum.md) | Type of processing workflow | direct |
| [processing_level](processing_level.md) | 0..1 <br/> [QuantityValue](QuantityValue.md) | Processing level (0=raw, 1=corrected, 2=derived, 3=model) | direct |
| [software_name](software_name.md) | 1 <br/> [String](String.md) | Software used for processing | direct |
| [software_version](software_version.md) | 0..1 <br/> [String](String.md) | Software version | direct |
| [additional_software](additional_software.md) | 0..1 <br/> [String](String.md) | Additional software used in pipeline | direct |
| [processing_parameters](processing_parameters.md) | 0..1 <br/> [String](String.md) | Parameters used in processing | direct |
| [parameters_file_path](parameters_file_path.md) | 0..1 <br/> [String](String.md) | Path to parameters file or text of key parameters | direct |
| [id](id.md) | 1 <br/> [Uriorcurie](Uriorcurie.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... | [NamedThing](NamedThing.md) |
| [title](title.md) | 0..1 <br/> [String](String.md) | A human-readable name or title for this entity | [NamedThing](NamedThing.md) |
| [description](description.md) | 0..1 <br/> [String](String.md) | A detailed textual description of this entity | [NamedThing](NamedThing.md) |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [Dataset](Dataset.md) | [workflow_runs](workflow_runs.md) | range | [WorkflowRun](WorkflowRun.md) |
| [StudyWorkflowAssociation](StudyWorkflowAssociation.md) | [workflow_id](workflow_id.md) | range | [WorkflowRun](WorkflowRun.md) |
| [WorkflowExperimentAssociation](WorkflowExperimentAssociation.md) | [workflow_id](workflow_id.md) | range | [WorkflowRun](WorkflowRun.md) |
| [WorkflowInputAssociation](WorkflowInputAssociation.md) | [workflow_id](workflow_id.md) | range | [WorkflowRun](WorkflowRun.md) |
| [WorkflowOutputAssociation](WorkflowOutputAssociation.md) | [workflow_id](workflow_id.md) | range | [WorkflowRun](WorkflowRun.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:WorkflowRun |
| native | aimsleaf:WorkflowRun |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: WorkflowRun
description: A computational processing workflow execution
from_schema: https://w3id.org/aims-leaf/
is_a: NamedThing
attributes:
  workflow_code:
    name: workflow_code
    description: Human-friendly identifier for the computational workflow run (e.g.,
      'MOTION-CORR-RUN-001', 'RELION-REFINE-240815'). Used for tracking processing
      pipelines and computational provenance.
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - WorkflowRun
    required: true
  workflow_type:
    name: workflow_type
    description: Type of processing workflow
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - WorkflowRun
    range: WorkflowTypeEnum
    required: true
  processing_level:
    name: processing_level
    description: Processing level (0=raw, 1=corrected, 2=derived, 3=model)
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - WorkflowRun
    range: QuantityValue
    inlined: true
  software_name:
    name: software_name
    description: Software used for processing
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - WorkflowRun
    required: true
  software_version:
    name: software_version
    description: Software version
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - WorkflowRun
  additional_software:
    name: additional_software
    description: Additional software used in pipeline
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - WorkflowRun
  processing_parameters:
    name: processing_parameters
    description: Parameters used in processing
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - WorkflowRun
  parameters_file_path:
    name: parameters_file_path
    description: Path to parameters file or text of key parameters
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    domain_of:
    - WorkflowRun

```
</details>

### Induced

<details>
```yaml
name: WorkflowRun
description: A computational processing workflow execution
from_schema: https://w3id.org/aims-leaf/
is_a: NamedThing
attributes:
  workflow_code:
    name: workflow_code
    description: Human-friendly identifier for the computational workflow run (e.g.,
      'MOTION-CORR-RUN-001', 'RELION-REFINE-240815'). Used for tracking processing
      pipelines and computational provenance.
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: workflow_code
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
    required: true
  workflow_type:
    name: workflow_type
    description: Type of processing workflow
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: workflow_type
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: WorkflowTypeEnum
    required: true
  processing_level:
    name: processing_level
    description: Processing level (0=raw, 1=corrected, 2=derived, 3=model)
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: processing_level
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: QuantityValue
    inlined: true
  software_name:
    name: software_name
    description: Software used for processing
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: software_name
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
    required: true
  software_version:
    name: software_version
    description: Software version
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: software_version
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  additional_software:
    name: additional_software
    description: Additional software used in pipeline
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: additional_software
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  processing_parameters:
    name: processing_parameters
    description: Parameters used in processing
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: processing_parameters
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
    range: string
  parameters_file_path:
    name: parameters_file_path
    description: Path to parameters file or text of key parameters
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: parameters_file_path
    owner: WorkflowRun
    domain_of:
    - WorkflowRun
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
    owner: WorkflowRun
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
    owner: WorkflowRun
    domain_of:
    - NamedThing
    range: string
  description:
    name: description
    description: A detailed textual description of this entity
    from_schema: https://w3id.org/aims-leaf/
    rank: 1000
    alias: description
    owner: WorkflowRun
    domain_of:
    - NamedThing
    - AttributeGroup
    range: string

```
</details>