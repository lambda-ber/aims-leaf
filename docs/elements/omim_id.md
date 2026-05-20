

# Slot: omim_id 


_OMIM database identifier_





URI: [aimsleaf:omim_id](https://w3id.org/aims-leaf/omim_id)
Alias: omim_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^[0-9]{6}$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:omim_id |
| native | aimsleaf:omim_id |




## LinkML Source

<details>
```yaml
name: omim_id
description: OMIM database identifier
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: omim_id
owner: MutationEffect
domain_of:
- MutationEffect
range: string
pattern: ^[0-9]{6}$

```
</details>