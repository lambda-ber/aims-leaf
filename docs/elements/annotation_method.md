

# Slot: annotation_method 


_Computational or experimental method used_





URI: [aimsleaf:annotation_method](https://w3id.org/aims-leaf/annotation_method)
Alias: annotation_method

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




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:annotation_method |
| native | aimsleaf:annotation_method |




## LinkML Source

<details>
```yaml
name: annotation_method
description: Computational or experimental method used
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: annotation_method
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: string

```
</details>