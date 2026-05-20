

# Slot: title 


_A human-readable name or title for this entity_





URI: [dcterms:title](http://purl.org/dc/terms/title)
Alias: title

<!-- no inheritance hierarchy -->





## Applicable Classes

| Name | Description | Modifies Slot |
| --- | --- | --- |
| [Image3D](Image3D.md) | A 3D volume or tomogram |  no  |
| [CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |  no  |
| [Sample](Sample.md) | A biological sample used in structural biology experiments |  no  |
| [Image](Image.md) | An image file from structural biology experiments |  no  |
| [Study](Study.md) | A logical grouping of related experiments investigating a research question |  no  |
| [DataFile](DataFile.md) | A data file generated or used in the study |  no  |
| [FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |  no  |
| [MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |  no  |
| [AggregatedProteinView](AggregatedProteinView.md) | Aggregated view of all structural and functional data for a protein |  no  |
| [MeasurementConditions](MeasurementConditions.md) | Conditions under which biophysical measurements were made |  no  |
| [Instrument](Instrument.md) | An instrument used to collect data |  no  |
| [EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |  no  |
| [Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |  no  |
| [ExperimentRun](ExperimentRun.md) | An experimental data collection session |  no  |
| [StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |  no  |
| [XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |  no  |
| [PlantSample](PlantSample.md) | Plant sample info for AIMS-LEAF |  no  |
| [ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |  no  |
| [FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |  no  |
| [FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |  no  |
| [ConformationalEnsemble](ConformationalEnsemble.md) | Ensemble of conformational states for a protein |  no  |
| [Dataset](Dataset.md) | Root container holding flat entity collections and association tables |  no  |
| [PlantSamplePreparation](PlantSamplePreparation.md) | A process that prepares a plant sample for analysis |  no  |
| [XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |  no  |
| [OntologyTerm](OntologyTerm.md) | A term from a controlled vocabulary or ontology |  no  |
| [Movie](Movie.md) | Raw cryo-EM movie with frame-by-frame metadata for motion correction |  no  |
| [WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |  no  |
| [SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |  no  |
| [OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |  no  |
| [NamedThing](NamedThing.md) | A named thing |  no  |
| [PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |  no  |
| [ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |  no  |






## Properties

* Range: [String](String.md)




## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/aims-leaf/




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | dcterms:title |
| native | aimsleaf:title |




## LinkML Source

<details>
```yaml
name: title
description: A human-readable name or title for this entity
from_schema: https://w3id.org/aims-leaf/
rank: 1000
slot_uri: dcterms:title
alias: title
owner: NamedThing
domain_of:
- NamedThing
range: string

```
</details>