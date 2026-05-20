

# Slot: start_time 


_Data collection start timestamp_





URI: [aimsleaf:start_time](https://w3id.org/aims-leaf/start_time)
Alias: start_time

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:start_time |
| native | aimsleaf:start_time |
| exact | ispyb:DataCollection.startTime |




## LinkML Source

<details>
```yaml
name: start_time
description: Data collection start timestamp
from_schema: https://w3id.org/aims-leaf/
exact_mappings:
- ispyb:DataCollection.startTime
rank: 1000
alias: start_time
owner: ExperimentRun
domain_of:
- ExperimentRun
range: string

```
</details>