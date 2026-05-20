

# Slot: data_id 


_Reference to the data_





URI: [aimsleaf:data_id](https://w3id.org/aims-leaf/data_id)
Alias: data_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SampleDataAssociation](SampleDataAssociation.md) | M:N link between Sample and Data with role metadata |  no  |






## Properties

* Range: [DataFile](DataFile.md)

* Required: True




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:data_id |
| native | aimsleaf:data_id |




## LinkML Source

<details>
```yaml
name: data_id
description: Reference to the data
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: data_id
owner: SampleDataAssociation
domain_of:
- SampleDataAssociation
range: DataFile
required: true

```
</details>