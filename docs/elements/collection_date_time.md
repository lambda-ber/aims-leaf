

# Slot: collection_date_time 


_The time of sampling, either as an instance (single point in time) or interval. All valid ISO8601 formats are acceptable_





URI: [aimsleaf:collection_date_time](https://w3id.org/aims-leaf/collection_date_time)
Alias: collection_date_time

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | Plant sample info for AIMS-LEAF |  no  |






## Properties

* Range: [String](String.md)

* Required: True




## Comments

* 2025-08-10T14:00:00-07:00

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:collection_date_time |
| native | aimsleaf:collection_date_time |




## LinkML Source

<details>
```yaml
name: collection_date_time
description: The time of sampling, either as an instance (single point in time) or
  interval. All valid ISO8601 formats are acceptable
comments:
- '2025-08-10T14:00:00-07:00'
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: collection_date_time
owner: PlantSample
domain_of:
- PlantSample
range: string
required: true

```
</details>