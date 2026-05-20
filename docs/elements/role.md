

# Slot: role 



URI: [aimsleaf:role](https://w3id.org/aims-leaf/role)
Alias: role

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [StudySampleAssociation](StudySampleAssociation.md) | M:N link between Study and Sample with role metadata |  no  |
| [ExperimentSampleAssociation](ExperimentSampleAssociation.md) | M:N link between ExperimentRun and Sample with role metadata |  no  |
| [ExperimentInstrumentAssociation](ExperimentInstrumentAssociation.md) | M:N link between ExperimentRun and Instrument |  no  |
| [SampleDataAssociation](SampleDataAssociation.md) | M:N link between Sample and Data with role metadata |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:role |
| native | aimsleaf:role |




## LinkML Source

<details>
```yaml
name: role
alias: role
domain_of:
- StudySampleAssociation
- SampleDataAssociation
- ExperimentSampleAssociation
- ExperimentInstrumentAssociation
range: string

```
</details>