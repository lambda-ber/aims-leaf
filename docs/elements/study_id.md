

# Slot: study_id 



URI: [aimsleaf:study_id](https://w3id.org/aims-leaf/study_id)
Alias: study_id

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudySampleAssociation](StudySampleAssociation.md) | M:N link between Study and Sample with role metadata |  no  |
| [StudyExperimentAssociation](StudyExperimentAssociation.md) | M:N link between Study and ExperimentRun |  no  |
| [StudyWorkflowAssociation](StudyWorkflowAssociation.md) | M:N link between Study and WorkflowRun |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:study_id |
| native | aimsleaf:study_id |




## LinkML Source

<details>
```yaml
name: study_id
alias: study_id
domain_of:
- StudySampleAssociation
- StudyExperimentAssociation
- StudyWorkflowAssociation
range: string

```
</details>