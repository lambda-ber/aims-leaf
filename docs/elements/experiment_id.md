

# Slot: experiment_id 



URI: [aimsleaf:experiment_id](https://w3id.org/aims-leaf/experiment_id)
Alias: experiment_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudyExperimentAssociation](StudyExperimentAssociation.md) | M:N link between Study and ExperimentRun |  no  |
| [ExperimentSampleAssociation](ExperimentSampleAssociation.md) | M:N link between ExperimentRun and Sample with role metadata |  no  |
| [WorkflowExperimentAssociation](WorkflowExperimentAssociation.md) | M:N link between WorkflowRun and source ExperimentRuns |  no  |
| [ExperimentInstrumentAssociation](ExperimentInstrumentAssociation.md) | M:N link between ExperimentRun and Instrument |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:experiment_id |
| native | aimsleaf:experiment_id |




## LinkML Source

<details>
```yaml
name: experiment_id
alias: experiment_id
domain_of:
- StudyExperimentAssociation
- ExperimentSampleAssociation
- ExperimentInstrumentAssociation
- WorkflowExperimentAssociation
range: string

```
</details>