

# Slot: tissue_plant_ontology_term 


_Plant ontology term corresponding to plant structure sampled; see https://planteome.org. May include multiple terms separated by semicolons_





URI: [aimsleaf:tissue_plant_ontology_term](https://w3id.org/aims-leaf/tissue_plant_ontology_term)
Alias: tissue_plant_ontology_term

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [PlantSample](PlantSample.md) | Plant sample info for AIMS-LEAF |  no  |






## Properties

* Range: [String](String.md)




## Comments

* seedling cotyledon (PO:0025471); seedling hypocotyl (PO:0025291)

## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | aimsleaf:tissue_plant_ontology_term |
| native | aimsleaf:tissue_plant_ontology_term |




## LinkML Source

<details>
```yaml
name: tissue_plant_ontology_term
description: Plant ontology term corresponding to plant structure sampled; see https://planteome.org.
  May include multiple terms separated by semicolons
comments:
- seedling cotyledon (PO:0025471); seedling hypocotyl (PO:0025291)
from_schema: https://w3id.org/aims-leaf/
rank: 1000
alias: tissue_plant_ontology_term
owner: PlantSample
domain_of:
- PlantSample
range: string
required: false

```
</details>