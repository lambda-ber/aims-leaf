

# Slot: sample_datafile_associations 


_Links between samples and datafiles (M:N)_





URI: [aimsleaf:sample_datafile_associations](https://w3id.org/aims-leaf/sample_datafile_associations)
Alias: sample_datafile_associations

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Dataset](Dataset.md) | Root container holding flat entity collections and association tables |  no  |






## Properties

* Range: [SampleDataAssociation](SampleDataAssociation.md)

* Multivalued: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:sample_datafile_associations |
| native | aimsleaf:sample_datafile_associations |




## LinkML Source

<details>
```yaml
name: sample_datafile_associations
description: Links between samples and datafiles (M:N)
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: sample_datafile_associations
owner: Dataset
domain_of:
- Dataset
range: SampleDataAssociation
multivalued: true
inlined: true
inlined_as_list: true

```
</details>