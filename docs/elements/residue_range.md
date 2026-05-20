

# Slot: residue_range 


_Range of residues (e.g., '1-100', '25,27,30-35')_





URI: [aimsleaf:residue_range](https://w3id.org/aims-leaf/residue_range)
Alias: residue_range

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

* Regex pattern: `^[0-9,\-]+$`




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:residue_range |
| native | aimsleaf:residue_range |




## LinkML Source

<details>
```yaml
name: residue_range
description: Range of residues (e.g., '1-100', '25,27,30-35')
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: residue_range
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: string
pattern: ^[0-9,\-]+$

```
</details>