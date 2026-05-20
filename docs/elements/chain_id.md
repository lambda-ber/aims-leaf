

# Slot: chain_id 


_Chain identifier in the PDB structure_





URI: [aimsleaf:chain_id](https://w3id.org/aims-leaf/chain_id)
Alias: chain_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |
| [ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |  no  |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |
| [EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |  no  |
| [PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |  no  |
| [StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |  no  |
| [ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |  no  |






## Properties

* Range: [String](String.md)

* Regex pattern: `^[A-Za-z0-9]+$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:chain_id |
| native | aimsleaf:chain_id |




## LinkML Source

<details>
```yaml
name: chain_id
description: Chain identifier in the PDB structure
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: chain_id
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: string
pattern: ^[A-Za-z0-9]+$

```
</details>