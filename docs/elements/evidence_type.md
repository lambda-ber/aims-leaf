

# Slot: evidence_type 


_Type of evidence supporting this annotation_





URI: [aimsleaf:evidence_type](https://w3id.org/aims-leaf/evidence_type)
Alias: evidence_type

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

* Range: [EvidenceTypeEnum](EvidenceTypeEnum.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:evidence_type |
| native | aimsleaf:evidence_type |




## LinkML Source

<details>
```yaml
name: evidence_type
description: Type of evidence supporting this annotation
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: evidence_type
owner: ProteinAnnotation
domain_of:
- ProteinAnnotation
range: EvidenceTypeEnum

```
</details>