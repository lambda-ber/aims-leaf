

# Slot: synchrotron_mode 


_Synchrotron storage ring fill mode_





URI: [aimsleaf:synchrotron_mode](https://w3id.org/aims-leaf/synchrotron_mode)
Alias: synchrotron_mode

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |






## Properties

* Range: [String](String.md)




## Comments

* e.g., 'Top-up', 'Decay', 'Hybrid'

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:synchrotron_mode |
| native | aimsleaf:synchrotron_mode |
| exact | ispyb:DataCollection.synchrotronMode |




## LinkML Source

<details>
```yaml
name: synchrotron_mode
description: Synchrotron storage ring fill mode
comments:
- e.g., 'Top-up', 'Decay', 'Hybrid'
from_schema: https://w3id.org/aims-leaf/
exact_mappings:
- ispyb:DataCollection.synchrotronMode
rank: 1000
alias: synchrotron_mode
owner: ExperimentRun
domain_of:
- ExperimentRun
range: string

```
</details>