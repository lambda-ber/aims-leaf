

# Slot: pdb_entry 


_PDB identifier_





URI: [aimsleaf:pdb_entry](https://w3id.org/aims-leaf/pdb_entry)
Alias: pdb_entry

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

* Regex pattern: `^[0-9][A-Za-z0-9]{3}$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:pdb_entry |
| native | aimsleaf:pdb_entry |




## LinkML Source

<details>
```yaml
name: pdb_entry
description: PDB identifier
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: pdb_entry
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: string
pattern: ^[0-9][A-Za-z0-9]{3}$

```
</details>