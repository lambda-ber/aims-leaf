

# Slot: sample_id 



URI: [aimsleaf:sample_id](https://w3id.org/aims-leaf/sample_id)
Alias: sample_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |  no  |
| [SampleDataAssociation](SampleDataAssociation.md) | M:N link between Sample and Data with role metadata |  no  |
| [PlantSamplePreparation](PlantSamplePreparation.md) | A process that prepares a plant sample for analysis |  no  |
| [StudySampleAssociation](StudySampleAssociation.md) | M:N link between Study and Sample with role metadata |  no  |
| [ExperimentSampleAssociation](ExperimentSampleAssociation.md) | M:N link between ExperimentRun and Sample with role metadata |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:sample_id |
| native | aimsleaf:sample_id |




## LinkML Source

<details>
```yaml
name: sample_id
alias: sample_id
domain_of:
- SamplePreparation
- StudySampleAssociation
- SampleDataAssociation
- ExperimentSampleAssociation
range: string

```
</details>