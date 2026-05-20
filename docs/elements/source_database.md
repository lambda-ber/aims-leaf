

# Slot: source_database 


_Source database or resource that provided this annotation_





URI: [aimsleaf:source_database](https://w3id.org/aims-leaf/source_database)
Alias: source_database

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

* Range: [AnnotationSourceEnum](AnnotationSourceEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:source_database |
| native | aimsleaf:source_database |




## LinkML Source

<details>
```yaml
name: source_database
description: Source database or resource that provided this annotation
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: source_database
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: AnnotationSourceEnum

```
</details>