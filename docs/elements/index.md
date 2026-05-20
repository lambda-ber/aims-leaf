# aims-leaf

aims-leaf is a comprehensive schema for representing multimodal structural biology imaging data, 
from atomic-resolution structures to tissue-level organization. It supports diverse experimental 
techniques including cryo-EM, X-ray crystallography, SAXS/SANS, fluorescence microscopy, and 
spectroscopic imaging.

## Schema Organization

The schema follows a **relational design** with flat entity collections and explicit association
tables for many-to-many relationships. This maps cleanly to SQL databases while supporting
flexible data reuse across studies.

The top-level entity is a [Dataset](Dataset.md), which serves as a container for related research.
A dataset might represent all data from a specific grant, collaboration, or publication.

### Entity Tables

All entities are stored in flat collections at the Dataset level:

**Biological Materials**
- [Samples](Sample.md): The biological specimens being studied (proteins, nucleic acids, complexes,
  cells, tissues). Each sample includes detailed molecular composition, buffer conditions, and
  storage information. For example, a purified protein with its sequence, concentration, and buffer pH.

- [Sample Preparations](SamplePreparation.md): How samples were prepared for specific techniques.
  This includes cryo-EM grid preparation (vitrification parameters), crystallization conditions for
  X-ray studies, or staining protocols for fluorescence microscopy.

**Data Collection**
- [Instruments](Instrument.md): The equipment used, from Titan Krios microscopes to synchrotron
  beamlines. Each instrument type ([CryoEMInstrument](CryoEMInstrument.md),
  [XRayInstrument](XRayInstrument.md), [SAXSInstrument](SAXSInstrument.md)) has specific parameters
  like accelerating voltage, detector type, or beam energy.

- [Experiment Runs](ExperimentRun.md): Individual data collection sessions. An experiment run
  captures when, how, and under what conditions data was collected, including quality metrics
  like resolution and completeness.

**Data Processing**
- [Workflow Runs](WorkflowRun.md): Computational processing steps applied to raw data. This includes
  motion correction for cryo-EM movies, 3D reconstruction, model building, or phase determination
  for crystallography. Each workflow tracks the software used, parameters, and computational resources.

**Data Products**
- [Data Files](DataFile.md): Any files generated or used, from raw data to final models. Each file
  is tracked with checksums for data integrity and typed (micrograph, particles, volume, model).

- [Images](Image.md): Specialized classes for different imaging modalities:
  - [Image2D](Image2D.md): Micrographs, diffraction patterns
  - [Image3D](Image3D.md): 3D reconstructions, tomograms
  - [FTIRImage](FTIRImage.md): Molecular composition maps from infrared spectroscopy
  - [FluorescenceImage](FluorescenceImage.md): Fluorophore-labeled cellular components
  - [OpticalImage](OpticalImage.md): Brightfield/phase contrast microscopy
  - [XRFImage](XRFImage.md): Elemental distribution maps

**Logical Groupings**
- [Studies](Study.md): Lightweight groupings representing focused investigations of specific
  biological questions. For example, a study might investigate "Heat stress response in Arabidopsis"
  or "Structure of the human ribosome under different conditions."

### Association Tables

Many-to-many relationships are represented via explicit association tables, which can carry
relationship metadata (e.g., the role of a sample in an experiment):

- **StudySampleAssociation**: Links samples to studies (with role: target, control, reference)
- **StudyExperimentAssociation**: Links experiments to studies
- **StudyWorkflowAssociation**: Links workflows to studies
- **ExperimentSampleAssociation**: Links samples to experiments (with role and preparation used)
- **ExperimentInstrumentAssociation**: Links instruments to experiments (with role: primary, detector)
- **WorkflowExperimentAssociation**: Links source experiments to workflows
- **WorkflowInputAssociation**: Links input files to workflows
- **WorkflowOutputAssociation**: Links output files to workflows

This relational design enables:
- **Sample reuse**: The same sample can be used in multiple studies and experiments
- **Multi-instrument experiments**: An experiment can use multiple instruments with different roles
- **Integrative workflows**: A workflow can combine data from multiple experiments

## Example Usage

A typical cryo-EM study of a protein complex would include:
1. Sample records for the purified complex with molecular weight and buffer composition
2. Grid preparation details with vitrification parameters
3. Microscope specifications and data collection parameters
4. Processing workflows from motion correction through 3D refinement
5. Final reconstructed volumes and fitted atomic models

A multimodal plant imaging study might combine:
1. Whole plant optical imaging for morphology
2. XRF imaging to map nutrient distribution
3. FTIR spectroscopy to identify stress-related molecular changes
4. Fluorescence microscopy to track specific protein responses
5. Cryo-EM of isolated organelles for ultrastructural details

## Key Features

- **Relational design**: Flat entity tables with explicit association tables for M:N relationships
- **SQL-friendly**: Maps directly to normalized database tables
- **Technique-agnostic core**: The same schema handles data from any structural biology method
- **Rich metadata**: Comprehensive tracking from sample to structure
- **Workflow provenance**: Complete computational reproducibility
- **Multimodal support**: Seamlessly integrate data across scales and techniques
- **Standards-compliant**: Follows FAIR principles and integrates with existing ontologies


URI: https://w3id.org/aims-leaf/

Name: aims-leaf



## Classes

| Class | Description |
| --- | --- |
| [Any](Any.md) |  |
| [Attribute](Attribute.md) | A domain, measurement, attribute, property, or any descriptor for additional ... |
| [AttributeGroup](AttributeGroup.md) | A grouping of related data attributes that form a logical unit |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BiophysicalProperty](BiophysicalProperty.md) | Measured or calculated biophysical properties |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[BufferComposition](BufferComposition.md) | Buffer composition for sample storage |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ComputeResources](ComputeResources.md) | Computational resources used |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ConformationalState](ConformationalState.md) | Individual conformational state |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CTFEstimationParameters](CTFEstimationParameters.md) | Parameters specific to CTF estimation workflows |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DatabaseCrossReference](DatabaseCrossReference.md) | Cross-references to external databases |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataCollectionStrategy](DataCollectionStrategy.md) | Strategy for data collection |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExperimentalConditions](ExperimentalConditions.md) | Environmental and experimental conditions |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ImageFeature](ImageFeature.md) | Semantic annotations describing features identified in images using controlle... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[LigandInteraction](LigandInteraction.md) | Small molecule/ligand interactions with proteins |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MotionCorrectionParameters](MotionCorrectionParameters.md) | Parameters specific to motion correction workflows |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ParticlePickingParameters](ParticlePickingParameters.md) | Parameters specific to particle picking workflows |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QualityMetrics](QualityMetrics.md) | Quality metrics for experiments |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[RefinementParameters](RefinementParameters.md) | Parameters specific to 3D refinement workflows |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StorageConditions](StorageConditions.md) | Storage conditions for samples |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TechniqueSpecificPreparation](TechniqueSpecificPreparation.md) | Base class for technique-specific preparation details |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CryoEMPreparation](CryoEMPreparation.md) | Cryo-EM specific sample preparation |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XRayPreparation](XRayPreparation.md) | X-ray crystallography specific preparation |
| [AttributeValue](AttributeValue.md) | The value for any attribute of an entity |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DateTimeValue](DateTimeValue.md) | A date or date and time value |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[QuantityValue](QuantityValue.md) | A simple quantity value, representing a measurement with a numeric value and ... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[TextValue](TextValue.md) | A value described using a text string, optionally with a controlled vocabular... |
| [ExperimentInstrumentAssociation](ExperimentInstrumentAssociation.md) | M:N link between ExperimentRun and Instrument |
| [ExperimentSampleAssociation](ExperimentSampleAssociation.md) | M:N link between ExperimentRun and Sample with role metadata |
| [NamedThing](NamedThing.md) | A named thing |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[AggregatedProteinView](AggregatedProteinView.md) | Aggregated view of all structural and functional data for a protein |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ConformationalEnsemble](ConformationalEnsemble.md) | Ensemble of conformational states for a protein |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[DataFile](DataFile.md) | A data file generated or used in the study |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FTIRImage](FTIRImage.md) | Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular comp... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XRFImage](XRFImage.md) | X-ray fluorescence (XRF) image showing elemental distribution |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Dataset](Dataset.md) | Root container holding flat entity collections and association tables |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ExperimentRun](ExperimentRun.md) | An experimental data collection session |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Image](Image.md) | An image file from structural biology experiments |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Image2D](Image2D.md) | A 2D image (micrograph, diffraction pattern) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FluorescenceImage](FluorescenceImage.md) | Fluorescence microscopy image capturing specific molecular targets through fl... |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Movie](Movie.md) | Raw cryo-EM movie with frame-by-frame metadata for motion correction |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OpticalImage](OpticalImage.md) | Visible light optical microscopy or photography image |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Image3D](Image3D.md) | A 3D volume or tomogram |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Instrument](Instrument.md) | An instrument used to collect data |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[CryoEMInstrument](CryoEMInstrument.md) | Cryo-EM microscope specifications |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[XRayInstrument](XRayInstrument.md) | X-ray diffractometer or synchrotron beamline specifications |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MeasurementConditions](MeasurementConditions.md) | Conditions under which biophysical measurements were made |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[OntologyTerm](OntologyTerm.md) | A term from a controlled vocabulary or ontology |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProteinAnnotation](ProteinAnnotation.md) | Base class for all protein-related functional and structural annotations |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[EvolutionaryConservation](EvolutionaryConservation.md) | Evolutionary conservation information |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[FunctionalSite](FunctionalSite.md) | Functional sites including catalytic, binding, and regulatory sites |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[MutationEffect](MutationEffect.md) | Effects of mutations and variants on protein structure and function |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PostTranslationalModification](PostTranslationalModification.md) | Post-translational modifications observed or predicted |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ProteinProteinInteraction](ProteinProteinInteraction.md) | Protein-protein interactions and interfaces |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[StructuralFeature](StructuralFeature.md) | Structural features and properties of protein regions |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Sample](Sample.md) | A biological sample used in structural biology experiments |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PlantSample](PlantSample.md) | Plant sample info for AIMS-LEAF |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[SamplePreparation](SamplePreparation.md) | A process that prepares a sample for imaging |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PlantSamplePreparation](PlantSamplePreparation.md) | A process that prepares a plant sample for analysis |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Study](Study.md) | A logical grouping of related experiments investigating a research question |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[WorkflowRun](WorkflowRun.md) | A computational processing workflow execution |
| [SampleDataAssociation](SampleDataAssociation.md) | M:N link between Sample and Data with role metadata |
| [StudyExperimentAssociation](StudyExperimentAssociation.md) | M:N link between Study and ExperimentRun |
| [StudySampleAssociation](StudySampleAssociation.md) | M:N link between Study and Sample with role metadata |
| [StudyWorkflowAssociation](StudyWorkflowAssociation.md) | M:N link between Study and WorkflowRun |
| [WorkflowExperimentAssociation](WorkflowExperimentAssociation.md) | M:N link between WorkflowRun and source ExperimentRuns |
| [WorkflowInputAssociation](WorkflowInputAssociation.md) | Links input DataFiles to WorkflowRun |
| [WorkflowOutputAssociation](WorkflowOutputAssociation.md) | Links output DataFiles to WorkflowRun |



## Slots

| Slot | Description |
| --- | --- |
| [accelerating_voltage](accelerating_voltage.md) | Accelerating voltage in kV |
| [acquisition_date](acquisition_date.md) | Date image was acquired |
| [acquisition_group](acquisition_group.md) | Acquisition group identifier (e |
| [acquisition_software](acquisition_software.md) | Acquisition software used (e |
| [acquisition_software_version](acquisition_software_version.md) | Version of acquisition software |
| [additional_software](additional_software.md) | Additional software used in pipeline |
| [additives](additives.md) | Additional additives in the buffer |
| [adhesive](adhesive.md) | Adhesive type (glue for sections if used, tape adhesives, gel |
| [affinity_column](affinity_column.md) | Affinity column specifications |
| [affinity_type](affinity_type.md) | Type of affinity chromatography |
| [aggregation_assessment](aggregation_assessment.md) | Assessment of protein aggregation state |
| [air_temperature_regimen](air_temperature_regimen.md) | Information about treatment involving an exposure to varying temperatures |
| [alignment_depth](alignment_depth.md) | Number of sequences in alignment |
| [aliquoting](aliquoting.md) | How the protein was aliquoted for storage |
| [allele_frequency](allele_frequency.md) | Population allele frequency (range: 0-1) |
| [amplitude_contrast](amplitude_contrast.md) | Amplitude contrast value |
| [anatomy](anatomy.md) | Anatomical part or tissue (e |
| [ancestral_data](ancestral_data.md) | Information about either pedigree or other description of ancestral informati... |
| [anisotropic_correction](anisotropic_correction.md) | Whether anisotropic motion correction was applied |
| [annotation_method](annotation_method.md) | Computational or experimental method used |
| [anom_corr](anom_corr.md) | Anomalous correlation |
| [anom_sig_ano](anom_sig_ano.md) | Anomalous signal strength |
| [anomalous_used](anomalous_used.md) | Whether anomalous signal was used |
| [antibiotic_regimen](antibiotic_regimen.md) | Information about treatment involving antibiotic administration |
| [antibiotic_selection](antibiotic_selection.md) | Antibiotic or selection agent used |
| [apodization_function](apodization_function.md) | Mathematical function used for apodization |
| [arabadopsis_phenotype_stage](arabadopsis_phenotype_stage.md) | Stage that takes into account effect of genotype & environment effects |
| [astigmatism](astigmatism.md) | Astigmatism value, typically specified in Angstroms |
| [astigmatism_target](astigmatism_target.md) | Target astigmatism in Angstroms |
| [atmosphere](atmosphere.md) | Storage atmosphere conditions |
| [attenuator](attenuator.md) | Attenuator setting used |
| [attribute](attribute.md) | The attribute being represented |
| [autoloader_capacity](autoloader_capacity.md) | Number of grids the autoloader can hold |
| [autoloader_slot](autoloader_slot.md) | Autoloader slot identifier |
| [average_b_factor_a2](average_b_factor_a2.md) | Average B-factor in Angstroms squared |
| [backbone_flexibility](backbone_flexibility.md) | B-factor or flexibility measure |
| [background_correction](background_correction.md) | Method used for background correction |
| [beam_center_x](beam_center_x.md) | Beam center X coordinate, typically specified in pixels ([px]) |
| [beam_center_x_px](beam_center_x_px.md) | Beam center X coordinate in pixels |
| [beam_center_y](beam_center_y.md) | Beam center Y coordinate, typically specified in pixels ([px]) |
| [beam_center_y_px](beam_center_y_px.md) | Beam center Y coordinate in pixels |
| [beam_energy](beam_energy.md) | X-ray beam energy, typically specified in kiloelectronvolts (keV) |
| [beam_shift_x](beam_shift_x.md) | Beam shift X in microradians |
| [beam_shift_y](beam_shift_y.md) | Beam shift Y in microradians |
| [beam_size](beam_size.md) | X-ray beam size, typically specified in micrometers |
| [beam_size_max](beam_size_max.md) | Maximum beam size in micrometers |
| [beam_size_min](beam_size_min.md) | Minimum beam size in micrometers |
| [beam_size_um](beam_size_um.md) | Beam size, typically specified in micrometers |
| [beam_size_x](beam_size_x.md) | Beam size X dimension, typically specified in micrometers (µm) |
| [beam_size_y](beam_size_y.md) | Beam size Y dimension, typically specified in micrometers (µm) |
| [beamline](beamline.md) | Beamline identifier (e |
| [beamline_id](beamline_id.md) | Beamline identifier at synchrotron/neutron facility |
| [beamline_parameters](beamline_parameters.md) | Relevant other motor positions of the beamline |
| [bfactor_dose_weighting](bfactor_dose_weighting.md) | B-factor for dose weighting, typically specified in Angstroms squared |
| [binding_affinity](binding_affinity.md) | Binding affinity value |
| [binding_affinity_type](binding_affinity_type.md) | Type of binding measurement (Kd, Ki, IC50) |
| [binding_affinity_unit](binding_affinity_unit.md) | Unit of binding affinity |
| [binding_energy](binding_energy.md) | Calculated binding energy (kcal/mol) |
| [binding_site_residues](binding_site_residues.md) | Residues involved in ligand binding |
| [binning](binning.md) | Binning factor applied during motion correction |
| [biological_assembly](biological_assembly.md) | Whether this represents a biological assembly |
| [biological_replicate_sample_group_name](biological_replicate_sample_group_name.md) | Samples that are biological replicates should have the same group name |
| [biophysical_properties](biophysical_properties.md) | All biophysical properties |
| [biotic_regimen](biotic_regimen.md) | Information about treatment involving use of biotic factors, such as bacteria... |
| [blot_force](blot_force.md) | Blotting force setting |
| [blot_number](blot_number.md) | Number of blots applied |
| [blot_time](blot_time.md) | Blotting time, typically specified in seconds (range: 0 |
| [blotter_height](blotter_height.md) | Blotter height setting |
| [blotter_setting](blotter_setting.md) | Blotter setting value |
| [box_size](box_size.md) | Particle box size in pixels |
| [broad_scale_environmental_context](broad_scale_environmental_context.md) | The major environmental system the sample or specimen came from |
| [buffer_composition](buffer_composition.md) | Buffer composition including pH, salts, additives |
| [c2_aperture](c2_aperture.md) | C2 aperture size in micrometers |
| [calibrated_pixel_size](calibrated_pixel_size.md) | Calibrated pixel size in Angstroms per pixel |
| [calibration_standard](calibration_standard.md) | Reference standard used for calibration |
| [camera_binning](camera_binning.md) | Camera binning factor |
| [cc_half](cc_half.md) | Half-set correlation coefficient CC(1/2) |
| [cell_type](cell_type.md) | Cell type if applicable (e |
| [chain_id](chain_id.md) | Chain identifier in the PDB structure |
| [chamber_temperature](chamber_temperature.md) | Chamber temperature, typically specified in degrees Celsius |
| [channel_name](channel_name.md) | Name of the fluorescence channel (e |
| [characteristic_features](characteristic_features.md) | Key features of this conformation |
| [checksum](checksum.md) | SHA-256 checksum for data integrity |
| [chemical_administration](chemical_administration.md) | List of chemical compounds administered to the host or site where sampling oc... |
| [chemical_mutagen](chemical_mutagen.md) | Treatment involving use of mutagens |
| [clashscore](clashscore.md) | MolProbity clashscore |
| [cleavage_temperature_c](cleavage_temperature_c.md) | Temperature during cleavage in Celsius |
| [cleavage_time_h](cleavage_time_h.md) | Duration of protease cleavage in hours |
| [clinical_significance](clinical_significance.md) | Clinical significance |
| [clustering_method](clustering_method.md) | Method used for conformational clustering |
| [coevolved_residues](coevolved_residues.md) | Pairs of coevolved residues |
| [collection_date_time](collection_date_time.md) | The time of sampling, either as an instance (single point in time) or interva... |
| [collection_mode](collection_mode.md) | Mode of data collection |
| [color_channels](color_channels.md) | Color channels present (e |
| [coma](coma.md) | Coma aberration in nanometers |
| [combined_tissue_description](combined_tissue_description.md) | The number and relationship between the tissues if multiple tissue samples we... |
| [completeness](completeness.md) | Data completeness, typically specified as a percentage (0-100) |
| [completeness_high_res_shell_percent](completeness_high_res_shell_percent.md) | Completeness in highest resolution shell, typically specified as a percentage... |
| [complex_stability](complex_stability.md) | Stability assessment of the complex |
| [components](components.md) | Buffer components and their concentrations |
| [concentration](concentration.md) | Sample concentration, typically specified in mg/mL or µM |
| [concentration_method](concentration_method.md) | Method used to concentrate protein |
| [confidence_score](confidence_score.md) | Confidence score for the annotation (range: 0-1) |
| [conformational_ensemble](conformational_ensemble.md) | Conformational ensemble data |
| [conformational_state](conformational_state.md) | Conformational state descriptor |
| [conformational_states](conformational_states.md) | Individual conformational states |
| [conservation_method](conservation_method.md) | Method used for conservation analysis |
| [conservation_score](conservation_score.md) | Evolutionary conservation score (range: 0-1) |
| [conserved_residues](conserved_residues.md) | Highly conserved residues |
| [contrast_method](contrast_method.md) | Contrast enhancement method used |
| [cpu_hours](cpu_hours.md) | CPU hours used, measured in hours |
| [creation_date](creation_date.md) | File creation date |
| [cross_references](cross_references.md) | Database cross-references |
| [cryoprotectant](cryoprotectant.md) | Cryoprotectant used |
| [cryoprotectant_concentration](cryoprotectant_concentration.md) | Cryoprotectant concentration, typically specified as a percentage |
| [crystal_cooling_capability](crystal_cooling_capability.md) | Crystal cooling system available |
| [crystal_notes](crystal_notes.md) | Additional notes about crystal quality and handling |
| [crystal_size_um](crystal_size_um.md) | Crystal dimensions in micrometers |
| [crystallization_method](crystallization_method.md) | Method used for crystallization |
| [cs](cs.md) | Spherical aberration (Cs) in millimeters |
| [cs_corrector](cs_corrector.md) | Spherical aberration corrector present |
| [cs_used_in_estimation](cs_used_in_estimation.md) | Spherical aberration (Cs) value used during CTF estimation, typically specifi... |
| [culture_volume_l](culture_volume_l.md) | Culture volume, typically specified in liters (L) |
| [current_status](current_status.md) | Current operational status |
| [data_collection_strategy](data_collection_strategy.md) | Strategy for data collection |
| [data_files](data_files.md) | All data files |
| [data_id](data_id.md) | Reference to the data |
| [data_type](data_type.md) | Type of data in the file |
| [database_id](database_id.md) | Identifier in the external database |
| [database_name](database_name.md) | Name of the external database |
| [database_url](database_url.md) | URL to the database entry |
| [date_added](date_added.md) | Date when sample was added to study |
| [definition](definition.md) | The formal definition or meaning of the ontology term |
| [defocus](defocus.md) | Defocus value, typically specified in micrometers |
| [defocus_range_increment](defocus_range_increment.md) | Defocus range increment in micrometers |
| [defocus_range_max](defocus_range_max.md) | Maximum defocus range in micrometers |
| [defocus_range_min](defocus_range_min.md) | Minimum defocus range in micrometers |
| [defocus_search_max](defocus_search_max.md) | Maximum defocus search range, typically specified in micrometers |
| [defocus_search_min](defocus_search_min.md) | Minimum defocus search range, typically specified in micrometers |
| [defocus_step](defocus_step.md) | Defocus search step, typically specified in micrometers |
| [defocus_target](defocus_target.md) | Target defocus value in micrometers |
| [delta_delta_g](delta_delta_g.md) | Change in folding free energy (kcal/mol) |
| [depth_meters](depth_meters.md) | The vertical distance (in meters) below local surface |
| [description](description.md) | A detailed textual description of this entity |
| [detector_dimensions](detector_dimensions.md) | Detector dimensions in pixels (e |
| [detector_distance](detector_distance.md) | Distance from sample to detector, typically specified in millimeters (mm) |
| [detector_distance_mm](detector_distance_mm.md) | Detector distance, typically specified in millimeters |
| [detector_manufacturer](detector_manufacturer.md) | Detector manufacturer (e |
| [detector_mode](detector_mode.md) | Supported or default detector operating mode |
| [detector_model](detector_model.md) | Detector model (e |
| [detector_position](detector_position.md) | Physical position of detector in microscope (e |
| [detector_technology](detector_technology.md) | Generic detector technology type |
| [developmental_stage](developmental_stage.md) | The developmental stage of the plant from which the tissue was sampled |
| [dimensions_x](dimensions_x.md) | Image width, typically specified in pixels |
| [dimensions_y](dimensions_y.md) | Image height, typically specified in pixels |
| [dimensions_z](dimensions_z.md) | Image depth, typically specified in pixels or slices |
| [disease_association](disease_association.md) | Associated disease or phenotype |
| [disorder_probability](disorder_probability.md) | Probability of disorder (range: 0-1) |
| [dissociation_constant](dissociation_constant.md) | Experimental Kd if available |
| [domain_assignment](domain_assignment.md) | Domain database assignment (CATH, SCOP, Pfam) |
| [domain_id](domain_id.md) | Domain identifier from domain database |
| [dose](dose.md) | Electron dose in e-/Å² |
| [dose_per_frame](dose_per_frame.md) | Electron dose per frame in e-/Angstrom^2 |
| [dose_rate](dose_rate.md) | Dose rate in e-/pixel/s or e-/Angstrom^2/s |
| [dose_weighting](dose_weighting.md) | Whether dose weighting was applied |
| [drift_total](drift_total.md) | Total drift, typically specified in Angstroms |
| [drop_ratio_protein_to_reservoir](drop_ratio_protein_to_reservoir.md) | Ratio of protein to reservoir solution in drop (e |
| [drop_volume_nl](drop_volume_nl.md) | Total drop volume, typically specified in nanoliters |
| [druggability_score](druggability_score.md) | Druggability score of the binding site (range: 0-1) |
| [duration](duration.md) | Storage duration |
| [dwell_time](dwell_time.md) | Dwell time per pixel, typically specified in milli-seconds (ms) |
| [ec_number](ec_number.md) | Enzyme Commission number for catalytic sites |
| [effect_on_function](effect_on_function.md) | Effect on protein function |
| [effect_on_stability](effect_on_stability.md) | Effect on protein stability |
| [elements_measured](elements_measured.md) | Elements detected and measured |
| [elevation_meters](elevation_meters.md) | Elevation (in meters) of the sampling site as measured by the vertical distan... |
| [elution_buffer](elution_buffer.md) | Buffer composition for elution |
| [embedding_material](embedding_material.md) | Material used to stabilize for sectioning, e |
| [emission_filter](emission_filter.md) | Specifications of the emission filter |
| [emission_wavelength](emission_wavelength.md) | Emission wavelength, typically specified in nanometers |
| [end_time](end_time.md) | Data collection end timestamp |
| [energy](energy.md) | X-ray energy, typically specified in eV |
| [energy_filter_make](energy_filter_make.md) | Energy filter manufacturer |
| [energy_filter_model](energy_filter_model.md) | Energy filter model |
| [energy_filter_present](energy_filter_present.md) | Whether energy filter is present |
| [energy_filter_slit_width](energy_filter_slit_width.md) | Energy filter slit width in eV |
| [energy_landscape](energy_landscape.md) | Description of the energy landscape |
| [energy_max](energy_max.md) | Maximum X-ray energy in keV |
| [energy_min](energy_min.md) | Minimum X-ray energy in keV |
| [environmental_medium](environmental_medium.md) | The environmental material(s) immediately surrounding the sample or specimen ... |
| [enzyme](enzyme.md) | Enzyme responsible for modification |
| [error](error.md) | Experimental error or uncertainty |
| [estimated_genome_size_mb](estimated_genome_size_mb.md) | Estimated genome size of the primary species being sampled, between 1-100000 |
| [ethane_temperature](ethane_temperature.md) | Ethane temperature, typically specified in degrees Celsius |
| [evidence_code](evidence_code.md) | Evidence and Conclusion Ontology (ECO) code |
| [evidence_type](evidence_type.md) | Type of evidence supporting this annotation |
| [evolutionary_conservation](evolutionary_conservation.md) | Conservation analysis |
| [excitation_filter](excitation_filter.md) | Specifications of the excitation filter |
| [excitation_wavelength](excitation_wavelength.md) | Excitation wavelength, typically specified in nanometers |
| [experiment_code](experiment_code.md) | Human-friendly laboratory or facility identifier for the experiment (e |
| [experiment_date](experiment_date.md) | Date of the experiment |
| [experiment_id](experiment_id.md) | Reference to the experiment run |
| [experiment_instrument_associations](experiment_instrument_associations.md) | Links between experiments and instruments (M:N) |
| [experiment_runs](experiment_runs.md) | All experiment runs (data collection sessions) |
| [experiment_sample_associations](experiment_sample_associations.md) | Links between experiments and samples (M:N with role) |
| [experimental_conditions](experimental_conditions.md) | Environmental and experimental conditions |
| [experimental_method](experimental_method.md) | Method used for measurement |
| [experimental_time_point_description](experimental_time_point_description.md) | Description of the time point sampled, applicable to samples that are part of... |
| [experimental_time_point_number](experimental_time_point_number.md) | Integer number representing the sequential numbering of time points, applicab... |
| [exposure_time](exposure_time.md) | Exposure time per image, typically specified in seconds (s) |
| [exposure_time_per_frame](exposure_time_per_frame.md) | Exposure time per frame in milliseconds |
| [facility_name](facility_name.md) | Name of the research facility where the instrument is located |
| [facility_ror](facility_ror.md) | Research Organization Registry (ROR) identifier for the facility |
| [feature_type](feature_type.md) | Type of structural feature |
| [fertilizer_administration](fertilizer_administration.md) | Detailed description of fertilizer application |
| [file_format](file_format.md) | File format |
| [file_id](file_id.md) | Reference to the input data file |
| [file_name](file_name.md) | Name of the file |
| [file_path](file_path.md) | Path to the file |
| [file_role](file_role.md) | Role of the file (raw, intermediate, final, diagnostic, metadata) |
| [file_size_bytes](file_size_bytes.md) | File size in bytes |
| [final_buffer](final_buffer.md) | Final buffer composition after purification |
| [final_concentration_mg_per_ml](final_concentration_mg_per_ml.md) | Final protein concentration in mg/mL |
| [flash_cooling_method](flash_cooling_method.md) | Flash cooling protocol |
| [fluorophore](fluorophore.md) | Name or type of fluorophore used |
| [flux](flux.md) | Photon flux at sample position, typically specified in photons per second |
| [flux_density](flux_density.md) | Photon flux density in photons/s/mm² |
| [flux_end](flux_end.md) | Photon flux at end of data collection, typically specified in photons per sec... |
| [flux_photons_per_s](flux_photons_per_s.md) | Photon flux, typically specified in photons per second |
| [frame_grouping](frame_grouping.md) | Number of frames grouped together |
| [frame_rate](frame_rate.md) | Frame rate, typically specified in frames per second |
| [frames](frames.md) | Number of frames in the movie |
| [frames_per_movie](frames_per_movie.md) | Number of frames per movie |
| [free_energy](free_energy.md) | Relative free energy (kcal/mol) |
| [functional_effect](functional_effect.md) | Known functional effect of this PTM |
| [functional_impact_description](functional_impact_description.md) | Description of functional impact |
| [functional_importance](functional_importance.md) | Description of functional importance |
| [functional_sites](functional_sites.md) | All functional site annotations |
| [fungicide_regimen](fungicide_regimen.md) | Information about treatment involving use of fungicides |
| [gaseous_environment](gaseous_environment.md) | Use of conditions with differing gaseous environments |
| [gc_content_percent](gc_content_percent.md) | Estimated GC content of the genome of the primary species being sampled, nume... |
| [genetic_modification](genetic_modification.md) | Genetic modifications of the genome of an organism, which may occur naturally... |
| [genus](genus.md) |  |
| [germplasm_collection_id](germplasm_collection_id.md) | Culture collection name and ID from which the original plant germplasm was so... |
| [glow_discharge_applied](glow_discharge_applied.md) | Whether glow discharge treatment was applied |
| [glow_discharge_atmosphere](glow_discharge_atmosphere.md) | Glow discharge atmosphere (air, amylamine) |
| [glow_discharge_current](glow_discharge_current.md) | Glow discharge current, typically specified in milliamperes |
| [glow_discharge_pressure](glow_discharge_pressure.md) | Glow discharge pressure, typically specified in millibars |
| [glow_discharge_time](glow_discharge_time.md) | Glow discharge time, typically specified in seconds |
| [go_terms](go_terms.md) | Associated Gene Ontology terms |
| [gold_standard](gold_standard.md) | Whether gold-standard refinement was used |
| [goniometer_type](goniometer_type.md) | Type of goniometer |
| [gpu_hours](gpu_hours.md) | GPU hours used, measured in hours |
| [grid_material](grid_material.md) | Grid material |
| [grid_square_id](grid_square_id.md) | Grid square identifier |
| [grid_type](grid_type.md) | Type of EM grid used |
| [growth_facility](growth_facility.md) | Type of facility where the sampled plant was grown |
| [growth_hormone_regimen](growth_hormone_regimen.md) | Information about treatment involving use of growth hormones |
| [growth_medium](growth_medium.md) | General specification of the media for growing the plants or tissue cultured ... |
| [growth_medium_composition](growth_medium_composition.md) | Detailed description of the makeup of the plant growth medium |
| [growth_temperature_c](growth_temperature_c.md) | Growth temperature, typically specified in degrees Celsius |
| [gunlens](gunlens.md) | Gun lens setting |
| [harvest_timepoint](harvest_timepoint.md) | Time point when cells were harvested |
| [harvest_to_preservation_time](harvest_to_preservation_time.md) | The time between sampling and sample preservation, minutes |
| [herbicide_regimen](herbicide_regimen.md) | Information about treatment involving use of herbicides |
| [hic_column](hic_column.md) | Hydrophobic interaction column used |
| [hole_id](hole_id.md) | Hole identifier within grid square |
| [hole_size](hole_size.md) | Hole size, typically specified in micrometers (range: 0 |
| [holes_per_group](holes_per_group.md) | Number of holes per group |
| [host_strain_or_cell_line](host_strain_or_cell_line.md) | Specific strain or cell line used (e |
| [humidity](humidity.md) | Humidity, typically specified as a percentage (0-100) |
| [humidity_percentage](humidity_percentage.md) | Chamber humidity during vitrification (range: 0-100), typically specified as ... |
| [humidity_regimen](humidity_regimen.md) | Information about treatment involving an exposure to varying degree of humidi... |
| [i_zero](i_zero.md) | Forward scattering intensity I(0) |
| [ice_thickness_estimate](ice_thickness_estimate.md) | Estimated ice thickness, typically specified in nanometers |
| [id](id.md) | Globally unique identifier as an IRI or CURIE for machine processing and exte... |
| [iex_column](iex_column.md) | Ion-exchange column used |
| [illumination_type](illumination_type.md) | Type of illumination (brightfield, darkfield, phase contrast, DIC) |
| [images](images.md) | All images |
| [imaging_mode](imaging_mode.md) | Imaging mode for electron microscopy |
| [inducer_concentration](inducer_concentration.md) | Concentration of induction agent |
| [induction_agent](induction_agent.md) | Agent used to induce expression (e |
| [induction_temperature_c](induction_temperature_c.md) | Temperature during induction, typically specified in degrees Celsius |
| [induction_time_h](induction_time_h.md) | Duration of induction, typically specified in hours |
| [initial_hit_condition](initial_hit_condition.md) | Description of initial crystallization hit condition |
| [inoculation_method](inoculation_method.md) | Method and material used for inoculation or infiltration with a biotic agent |
| [input_type](input_type.md) | Type of input for the workflow |
| [insecticide_regimen](insecticide_regimen.md) | Information about treatment involving use of insecticides |
| [installation_date](installation_date.md) | Date of instrument installation |
| [instrument_category](instrument_category.md) | Category distinguishing beamlines from laboratory equipment |
| [instrument_code](instrument_code.md) | Human-friendly facility or laboratory identifier for the instrument (e |
| [instrument_id](instrument_id.md) | Reference to the instrument |
| [instruments](instruments.md) | All instruments used across studies |
| [interaction_distance](interaction_distance.md) | Distance criteria for interaction (Angstroms) |
| [interaction_evidence](interaction_evidence.md) | Evidence for this interaction |
| [interaction_type](interaction_type.md) | Type of interaction |
| [interface_area](interface_area.md) | Buried surface area at interface (Ų) |
| [interface_residues](interface_residues.md) | Residues at the interaction interface |
| [ionic_strength](ionic_strength.md) | Ionic strength, typically specified in molar (mol/L) |
| [is_cofactor](is_cofactor.md) | Whether the ligand is a cofactor |
| [is_drug_like](is_drug_like.md) | Whether the ligand has drug-like properties |
| [isolate](isolate.md) | Isolate or mutant name |
| [ispyb_data_collection_id](ispyb_data_collection_id.md) | ISPyB DataCollection |
| [ispyb_session_id](ispyb_session_id.md) | ISPyB BLSession |
| [keywords](keywords.md) | Keywords or tags describing the dataset for search and categorization |
| [label](label.md) | The human-readable label or name of the ontology term |
| [laser_power](laser_power.md) | Laser power, typically specified in milliwatts |
| [last_light_transition_type](last_light_transition_type.md) | The most recent light transition before sampling |
| [last_updated](last_updated.md) | Date of last update |
| [latitude](latitude.md) | The geographical origin of the sample as defined by latitude |
| [ligand_id](ligand_id.md) | Ligand identifier (ChEMBL, ChEBI, PubChem) |
| [ligand_interactions](ligand_interactions.md) | Ligands that interact with this site |
| [ligand_name](ligand_name.md) | Common name of the ligand |
| [ligand_smiles](ligand_smiles.md) | SMILES representation of the ligand |
| [light_regimen](light_regimen.md) | Information about treatment involving an exposure to light, including intensi... |
| [local_environmental_context](local_environmental_context.md) | The entity or entities which are in the sample or specimen's local vicinity a... |
| [longitude](longitude.md) | The geographical origin of the sample as defined by longitude |
| [loop_size](loop_size.md) | Loop size, typically specified in micrometers |
| [lysis_buffer](lysis_buffer.md) | Buffer composition for lysis |
| [lysis_method](lysis_method.md) | Method used for cell lysis |
| [magnification](magnification.md) | Magnification used during data collection |
| [manufacturer](manufacturer.md) | Instrument manufacturer |
| [map_sharpening_bfactor](map_sharpening_bfactor.md) | B-factor used for map sharpening, typically specified in Angstroms squared (Å... |
| [mass_shift](mass_shift.md) | Mass change due to modification (Da) |
| [maximum_numeric_value](maximum_numeric_value.md) | The maximum value part, expressed as a number, of the quantity value when the... |
| [mean_i_over_sigma_i](mean_i_over_sigma_i.md) | Mean I/sigma(I) |
| [measurement_conditions](measurement_conditions.md) | Conditions under which measurement was made |
| [mechanical_damage](mechanical_damage.md) | Information about any mechanical damage exerted on the plant |
| [medium](medium.md) | Growth medium used |
| [memory_gb](memory_gb.md) | Maximum memory used, typically specified in gigabytes (GB) |
| [microscope_software](microscope_software.md) | Microscope control software (e |
| [microscope_software_version](microscope_software_version.md) | Software version |
| [minimum_numeric_value](minimum_numeric_value.md) | The minimum value part, expressed as a number, of the quantity value when the... |
| [model](model.md) | Instrument model |
| [model_file_path](model_file_path.md) | Path to deep learning model file if using a local or custom trained model fil... |
| [model_name](model_name.md) | Name or identifier of the deep learning model (e |
| [model_source](model_source.md) | Source or software associated with the model (e |
| [modification_group](modification_group.md) | Chemical group added (e |
| [modification_type](modification_type.md) | Type of PTM |
| [modified_residue](modified_residue.md) | Residue that is modified |
| [molecular_signatures](molecular_signatures.md) | Identified molecular signatures or peaks |
| [molecular_weight](molecular_weight.md) | Molecular weight, typically specified in kilodaltons (kDa) |
| [molprobity_score](molprobity_score.md) | Overall MolProbity score |
| [monochromator_type](monochromator_type.md) | Type of monochromator |
| [mounting_method](mounting_method.md) | Crystal mounting method |
| [mounting_temperature](mounting_temperature.md) | Temperature during mounting, typically specified in Kelvin |
| [multiplicity](multiplicity.md) | Data multiplicity (redundancy) |
| [mutation](mutation.md) | Mutation in standard notation (e |
| [mutation_type](mutation_type.md) | Type of mutation |
| [mutations](mutations.md) | All mutation annotations |
| [ncbi_taxonomy_id](ncbi_taxonomy_id.md) | Unique identifier from the NCBI taxonomy database |
| [ncc_score](ncc_score.md) | Normalized cross-correlation score threshold |
| [nominal_defocus](nominal_defocus.md) | Nominal defocus value, typically specified in micrometers |
| [number_of_images](number_of_images.md) | Total number of diffraction images collected |
| [number_of_scans](number_of_scans.md) | Number of scans averaged for the spectrum |
| [numeric_value](numeric_value.md) | The numerical part of a quantity value, expressed as a number |
| [numerical_aperture](numerical_aperture.md) | Numerical aperture of the objective lens |
| [objective_aperture](objective_aperture.md) | Objective aperture size in micrometers |
| [observed_host_symbionts](observed_host_symbionts.md) | The taxonomic name of the organism(s) found living in mutualistic, commensali... |
| [od600_at_induction](od600_at_induction.md) | Optical density at 600nm when induction was started |
| [omim_id](omim_id.md) | OMIM database identifier |
| [ontology](ontology.md) | The ontology or controlled vocabulary this term comes from (e |
| [operator_id](operator_id.md) | Identifier or name of the person who performed the sample preparation (e |
| [optimization_strategy](optimization_strategy.md) | Strategy used to optimize crystals |
| [optimized_condition](optimized_condition.md) | Final optimized crystallization condition |
| [organism](organism.md) | Source organism for the sample (e |
| [organism_id](organism_id.md) | NCBI taxonomy ID |
| [oscillation_angle](oscillation_angle.md) | Oscillation angle per image, typically specified in degrees |
| [oscillation_per_image_deg](oscillation_per_image_deg.md) | Oscillation angle per image, typically specified in degrees |
| [other_treatment_regimen](other_treatment_regimen.md) | Use this field to provide information about treatments that are not captured ... |
| [output_binning](output_binning.md) | Output binning factor |
| [output_type](output_type.md) | Type of output from the workflow |
| [parameters_file_path](parameters_file_path.md) | Path to parameters file or text of key parameters |
| [parent_sample_id](parent_sample_id.md) | Reference to parent sample for derivation tracking |
| [partner_chain_id](partner_chain_id.md) | Chain ID of interacting partner |
| [partner_interface_residues](partner_interface_residues.md) | Partner residues at the interaction interface |
| [partner_protein_id](partner_protein_id.md) | UniProt ID of interacting partner |
| [patch_size](patch_size.md) | Patch size for local motion correction |
| [pdb_entries](pdb_entries.md) | PDB entries representing this state |
| [pdb_entry](pdb_entry.md) | PDB identifier |
| [perturbation](perturbation.md) | Type of perturbation, e |
| [ph](ph.md) | pH of the buffer (range: 0-14) |
| [phase_plate](phase_plate.md) | Phase plate available |
| [phase_plate_type](phase_plate_type.md) | Type of phase plate if present |
| [picking_method](picking_method.md) | Method used (manual, template_matching, deep_learning, LoG, Topaz, other) |
| [pinhole_size](pinhole_size.md) | Pinhole size, typically specified in Airy units for confocal microscopy |
| [pixel_size](pixel_size.md) | Pixel size, typically specified in Angstroms |
| [pixel_size_calibrated](pixel_size_calibrated.md) | Calibrated pixel size for this experiment, typically specified in Angstroms (... |
| [pixel_size_physical](pixel_size_physical.md) | Physical pixel size in micrometers |
| [pixel_size_physical_um](pixel_size_physical_um.md) | Physical pixel size of the detector in micrometers |
| [pixel_size_unbinned](pixel_size_unbinned.md) | Unbinned pixel size, typically specified in Angstroms per pixel |
| [pixel_size_x](pixel_size_x.md) | Pixel size X dimension, typically specified in micrometers (µm) |
| [pixel_size_y](pixel_size_y.md) | Pixel size Y dimension, typically specified in micrometers (µm) |
| [plane_of_section](plane_of_section.md) | plane of section: cross section / transverse section, longitudinal section, r... |
| [plant_age](plant_age.md) | The age of the plant from which the tissue was sampled |
| [plant_sample_preparations](plant_sample_preparations.md) | All plant specific sample preparations |
| [plant_sex](plant_sex.md) | Sex of the reproductive parts on the whole plant, e |
| [plantsamples](plantsamples.md) | All samples across all studies |
| [plasma_treatment](plasma_treatment.md) | Plasma treatment details |
| [ploidy](ploidy.md) | The ploidy level of the genome |
| [population](population.md) | Relative population of this state (range: 0-1) |
| [power_score](power_score.md) | Power score threshold |
| [preparation_date](preparation_date.md) | Date of sample preparation |
| [preparation_id](preparation_id.md) | Specific preparation used for this sample in this experiment |
| [preparation_method](preparation_method.md) | Method used to prepare the sample |
| [preparation_type](preparation_type.md) | Type of sample preparation |
| [pressure](pressure.md) | Pressure, typically specified in kilopascals (kPa) |
| [principal_motions](principal_motions.md) | Description of principal motions |
| [processing_level](processing_level.md) | Processing level (0=raw, 1=corrected, 2=derived, 3=model) |
| [processing_parameters](processing_parameters.md) | Parameters used in processing |
| [processing_status](processing_status.md) | Current processing status |
| [property_type](property_type.md) | Type of biophysical property |
| [protease](protease.md) | Protease used for tag cleavage |
| [protease_inhibitors](protease_inhibitors.md) | Protease inhibitors added |
| [protease_ratio](protease_ratio.md) | Ratio of protease to protein |
| [protein_buffer](protein_buffer.md) | Buffer composition for protein solution |
| [protein_concentration_mg_per_ml](protein_concentration_mg_per_ml.md) | Protein concentration for crystallization in mg/mL |
| [protein_id](protein_id.md) | UniProt accession number |
| [protein_interactions](protein_interactions.md) | All protein-protein interactions |
| [protein_name](protein_name.md) | Protein name |
| [protocol_description](protocol_description.md) | Detailed protocol description |
| [ptms](ptms.md) | All post-translational modifications |
| [publication_ids](publication_ids.md) | IDs of one or more publications supporting this annotation |
| [purity_by_sds_page_percent](purity_by_sds_page_percent.md) | Purity percentage by SDS-PAGE |
| [purity_percentage](purity_percentage.md) | Sample purity, typically specified as a percentage (range: 0-100) |
| [quality_metrics](quality_metrics.md) | Quality control metrics for the sample |
| [quantum_yield](quantum_yield.md) | Quantum yield of the fluorophore |
| [r_factor](r_factor.md) | R-factor for crystallography (deprecated, use r_work) |
| [r_free](r_free.md) | R-free (test set) |
| [r_merge](r_merge.md) | Rmerge - merge R-factor |
| [r_pim](r_pim.md) | Rpim - precision-indicating merging R-factor |
| [r_work](r_work.md) | Refinement R-factor (working set) |
| [radiation_regimen](radiation_regimen.md) | Information about treatment involving exposure of plant or a plant part to a ... |
| [rainfall_regimen](rainfall_regimen.md) | Information about treatment involving an exposure to a given amount of rainfa... |
| [ramachandran_favored_percent](ramachandran_favored_percent.md) | Percentage of residues in favored Ramachandran regions |
| [ramachandran_outliers_percent](ramachandran_outliers_percent.md) | Percentage of Ramachandran outliers |
| [raw_data_location](raw_data_location.md) | Location of raw data files |
| [raw_value](raw_value.md) | The value that was specified in raw form, i |
| [reconstruction_method](reconstruction_method.md) | Method used for 3D reconstruction |
| [reference_genome](reference_genome.md) | Reference genome and annotation to be used for analysis |
| [region_locality](region_locality.md) | The geographical origin of the sample as defined by the country or sea name f... |
| [regulatory_role](regulatory_role.md) | Role in regulation |
| [related_entity](related_entity.md) | ID of the entity that owns this file |
| [removal_enzyme](removal_enzyme.md) | Enzyme that removes modification |
| [reservoir_volume_ul](reservoir_volume_ul.md) | Reservoir volume, typically specified in microliters |
| [residue_range](residue_range.md) | Range of residues (e |
| [residues](residues.md) | List of residues forming the functional site |
| [resolution](resolution.md) | Resolution at edge of detector, typically specified in Angstroms (Å) |
| [resolution_0_143](resolution_0_143.md) | Resolution at FSC=0 |
| [resolution_0_5](resolution_0_5.md) | Resolution at FSC=0 |
| [resolution_at_corner](resolution_at_corner.md) | Resolution at corner of detector, typically specified in Angstroms (Å) |
| [resolution_high_shell_a](resolution_high_shell_a.md) | High resolution shell limit, typically specified in Angstroms |
| [resolution_low_a](resolution_low_a.md) | Low resolution limit, typically specified in Angstroms |
| [rg](rg.md) | Radius of gyration, typically specified in Angstroms |
| [rmsd_from_reference](rmsd_from_reference.md) | RMSD from reference structure |
| [rmsd_threshold](rmsd_threshold.md) | RMSD threshold for clustering (Angstroms) |
| [role](role.md) | Role of sample in study (e |
| [salt_regimen](salt_regimen.md) | Information about treatment involving use of salts as supplement to liquid an... |
| [sample_applied_volume](sample_applied_volume.md) | Volume of sample applied, typically specified in microliters |
| [sample_code](sample_code.md) | Human-friendly laboratory identifier or facility code for the sample (e |
| [sample_datafile_associations](sample_datafile_associations.md) | Links between samples and datafiles (M:N) |
| [sample_disease_stage](sample_disease_stage.md) | Stage of the disease at the time of sample collection, e |
| [sample_disease_staus](sample_disease_staus.md) | List of diseases with which the subject has been diagnosed at the time of sam... |
| [sample_id](sample_id.md) | Reference to the sample being prepared |
| [sample_material_processing](sample_material_processing.md) | A brief description of any processing applied to the sample during or after r... |
| [sample_preparations](sample_preparations.md) | All sample preparations |
| [sample_preservation_method](sample_preservation_method.md) | The method employed for preserving or fixing the tissue |
| [sample_size](sample_size.md) | The total amount or size (volume (ml), mass (g) or area (m2)) of sample colle... |
| [sample_storage_temperature](sample_storage_temperature.md) | Temperature at which sample was stored (in degrees Celsius) |
| [sample_type](sample_type.md) | Type of biological sample |
| [samples](samples.md) | All samples across all studies |
| [screen_name](screen_name.md) | Name of crystallization screen used |
| [sec_buffer](sec_buffer.md) | Buffer for size-exclusion chromatography |
| [sec_column](sec_column.md) | Size-exclusion column used |
| [second_affinity_reverse](second_affinity_reverse.md) | Second affinity or reverse affinity step |
| [secondary_structure](secondary_structure.md) | Secondary structure assignment |
| [section_thickness](section_thickness.md) | Thickness of sample section |
| [seed_stock_dilution](seed_stock_dilution.md) | Dilution factor for seed stock |
| [seeding_type](seeding_type.md) | Type of seeding used (micro, macro, streak) |
| [shots_per_hole](shots_per_hole.md) | Number of shots taken per hole |
| [signal_to_noise](signal_to_noise.md) | Signal to noise ratio |
| [site_name](site_name.md) | Common name for this site |
| [site_type](site_type.md) | Type of functional site |
| [slit_gap_horizontal](slit_gap_horizontal.md) | Horizontal slit gap aperture, typically specified in micrometers (µm) |
| [slit_gap_vertical](slit_gap_vertical.md) | Vertical slit gap aperture, typically specified in micrometers (µm) |
| [soak_compound](soak_compound.md) | Compound used for soaking (ligand, heavy atom) |
| [soak_conditions](soak_conditions.md) | Conditions for crystal soaking |
| [software_name](software_name.md) | Software used for processing |
| [software_version](software_version.md) | Software version |
| [solvent_accessibility](solvent_accessibility.md) | Relative solvent accessible surface area (range: 0-1) |
| [source_database](source_database.md) | Source database or resource that provided this annotation |
| [source_type](source_type.md) | Type of X-ray source |
| [space_group](space_group.md) | Crystallographic space group |
| [species](species.md) |  |
| [spectral_resolution](spectral_resolution.md) | Spectral resolution, typically specified in inverse centimeters (cm⁻¹) |
| [split_strategy](split_strategy.md) | Strategy for data splitting |
| [spotsize](spotsize.md) | Electron beam spot size setting |
| [stage_position_x](stage_position_x.md) | Stage X position, typically specified in micrometers |
| [stage_position_y](stage_position_y.md) | Stage Y position, typically specified in micrometers |
| [stage_position_z](stage_position_z.md) | Stage Z position, typically specified in micrometers |
| [stage_tilt](stage_tilt.md) | Stage tilt angle in degrees |
| [start_angle](start_angle.md) | Starting rotation angle, typically specified in degrees |
| [start_time](start_time.md) | Data collection start timestamp |
| [state_id](state_id.md) | Identifier for this state |
| [state_name](state_name.md) | Descriptive name (e |
| [storage_conditions](storage_conditions.md) | Storage conditions for the sample |
| [storage_gb](storage_gb.md) | Storage used, typically specified in gigabytes (GB) |
| [storage_uri](storage_uri.md) | Storage URI (S3, Globus, etc |
| [strain_variety_cultivar](strain_variety_cultivar.md) | Name or ID of the cultivar, variety, strain, or other similar designation of ... |
| [strategy_notes](strategy_notes.md) | Notes about data collection strategy |
| [structural_features](structural_features.md) | All structural feature annotations |
| [structural_motif](structural_motif.md) | Known structural motif |
| [studies](studies.md) | All studies in this dataset |
| [study_experiment_associations](study_experiment_associations.md) | Links between studies and experiments (M:N) |
| [study_id](study_id.md) | Reference to the study |
| [study_sample_associations](study_sample_associations.md) | Links between studies and samples (M:N) |
| [study_workflow_associations](study_workflow_associations.md) | Links between studies and workflows (M:N) |
| [super_resolution](super_resolution.md) | Whether super-resolution mode was used |
| [support_film](support_film.md) | Support film type |
| [support_thickness](support_thickness.md) | Thickness of support layer |
| [support_type](support_type.md) | type of support for sample sections (quartz, lexan, thermonox, Ge, MgF2 |
| [symmetry](symmetry.md) | Symmetry applied (C1, Cn, Dn, T, O, I) |
| [synchrotron_mode](synchrotron_mode.md) | Synchrotron storage ring fill mode |
| [tag_removal](tag_removal.md) | Whether and how affinity tag was removed |
| [taxonomic_range](taxonomic_range.md) | Taxonomic range of conservation |
| [technique](technique.md) | Technique used for data collection |
| [tem_beam_diameter](tem_beam_diameter.md) | TEM beam diameter in micrometers |
| [temperature](temperature.md) | Storage temperature, typically specified in degrees Celsius |
| [temperature_c](temperature_c.md) | Crystallization temperature, typically specified in degrees Celsius |
| [temperature_k](temperature_k.md) | Data collection temperature, typically specified in Kelvin |
| [terms](terms.md) | Ontology terms describing features identified in the image |
| [threshold](threshold.md) | Picking threshold |
| [time_after_last_light_transition](time_after_last_light_transition.md) | The time between sampling and the most recent light transition, specified as ... |
| [time_post_inoculation](time_post_inoculation.md) | The time between inoculation with the biotic agent and sample collection, spe... |
| [timestamp](timestamp.md) | Acquisition timestamp |
| [tissue](tissue.md) | Detailed description of the organ or type of tissue sampled |
| [tissue_plant_ontology_term](tissue_plant_ontology_term.md) | Plant ontology term corresponding to plant structure sampled; see https://pla... |
| [title](title.md) | A human-readable name or title for this entity |
| [top_layer](top_layer.md) | type of film for top layer, if present (mylar, polyproylene, none |
| [top_layer_thickness](top_layer_thickness.md) | Thickness of top layer |
| [total_dose](total_dose.md) | Total electron dose in e-/Angstrom^2 |
| [total_exposure_time](total_exposure_time.md) | Total exposure time in milliseconds |
| [total_frames](total_frames.md) | Total number of frames/images |
| [total_rotation](total_rotation.md) | Total rotation range collected, typically specified in degrees |
| [total_rotation_deg](total_rotation_deg.md) | Total rotation range, typically specified in degrees |
| [transition_pathways](transition_pathways.md) | Description of transition pathways between states |
| [transmission](transmission.md) | X-ray beam transmission as a percentage (0-100) |
| [transmission_percent](transmission_percent.md) | Beam transmission, typically specified as a percentage (0-100) |
| [undulator_gap](undulator_gap.md) | Undulator gap setting, typically specified in millimeters (mm) |
| [uniprot_id](uniprot_id.md) | UniProt accession |
| [unit](unit.md) | The unit of measurement |
| [unit_cell_a](unit_cell_a.md) | Unit cell parameter a, typically specified in Angstroms |
| [unit_cell_alpha](unit_cell_alpha.md) | Unit cell angle alpha, typically specified in degrees |
| [unit_cell_b](unit_cell_b.md) | Unit cell parameter b, typically specified in Angstroms |
| [unit_cell_beta](unit_cell_beta.md) | Unit cell angle beta, typically specified in degrees |
| [unit_cell_c](unit_cell_c.md) | Unit cell parameter c, typically specified in Angstroms |
| [unit_cell_gamma](unit_cell_gamma.md) | Unit cell angle gamma, typically specified in degrees |
| [unit_cv_id](unit_cv_id.md) | The unit of the quantity, expressed as a CURIE from the Unit Ontology (e |
| [value](value.md) | The value, as a text string |
| [value_cv_id](value_cv_id.md) | For values that are in a controlled vocabulary (CV), this attribute should ca... |
| [variable_residues](variable_residues.md) | Highly variable residues |
| [vitrification_instrument](vitrification_instrument.md) | Vitrification instrument used (e |
| [vitrification_method](vitrification_method.md) | Method used for vitrification |
| [voltage_used_in_estimation](voltage_used_in_estimation.md) | Accelerating voltage value used during CTF estimation, typically specified in... |
| [voxel_size](voxel_size.md) | Voxel size, typically specified in Angstroms |
| [wait_time](wait_time.md) | Wait time before blotting, typically specified in seconds |
| [wash_buffer](wash_buffer.md) | Buffer composition for washing |
| [watering_regimen](watering_regimen.md) | Information about treatment involving an exposure to watering frequencies |
| [wavelength](wavelength.md) | X-ray wavelength, typically specified in Angstroms (Å) |
| [wavelength_a](wavelength_a.md) | X-ray wavelength, typically specified in Angstroms |
| [wavenumber_max](wavenumber_max.md) | Maximum wavenumber, typically specified in inverse centimeters (cm⁻¹) |
| [wavenumber_min](wavenumber_min.md) | Minimum wavenumber, typically specified in inverse centimeters (cm⁻¹) |
| [white_balance](white_balance.md) | White balance settings |
| [wilson_b_factor_a2](wilson_b_factor_a2.md) | Wilson B-factor in Angstroms squared |
| [workflow_code](workflow_code.md) | Human-friendly identifier for the computational workflow run (e |
| [workflow_experiment_associations](workflow_experiment_associations.md) | Links between workflows and source experiments (M:N) |
| [workflow_id](workflow_id.md) | Reference to the workflow run |
| [workflow_input_associations](workflow_input_associations.md) | Links between workflows and input files |
| [workflow_output_associations](workflow_output_associations.md) | Links between workflows and output files |
| [workflow_runs](workflow_runs.md) | All workflow runs (computational processing) |
| [workflow_type](workflow_type.md) | Type of processing workflow |
| [yield_mg](yield_mg.md) | Total yield in milligrams |


## Enumerations

| Enumeration | Description |
| --- | --- |
| [AffinityUnitEnum](AffinityUnitEnum.md) | Units for affinity measurements |
| [AnnotationSourceEnum](AnnotationSourceEnum.md) | Sources of functional annotations |
| [ArabadopsisStageEnum](ArabadopsisStageEnum.md) | Stage that takes into account effect of genotype & environment effects |
| [BeamlineEnum](BeamlineEnum.md) | Specific beamline instances at DOE and other major structural biology facilit... |
| [BindingAffinityTypeEnum](BindingAffinityTypeEnum.md) | Types of binding affinity measurements |
| [BiophysicalMethodEnum](BiophysicalMethodEnum.md) | Methods for biophysical measurements |
| [BiophysicalPropertyEnum](BiophysicalPropertyEnum.md) | Types of biophysical properties |
| [ClinicalSignificanceEnum](ClinicalSignificanceEnum.md) | Clinical significance of variants |
| [CollectionModeEnum](CollectionModeEnum.md) | Data collection modes |
| [ComplexStabilityEnum](ComplexStabilityEnum.md) | Stability of protein complexes |
| [ConformationalStateEnum](ConformationalStateEnum.md) | Conformational states |
| [CrystallizationMethodEnum](CrystallizationMethodEnum.md) | Methods for protein crystallization |
| [DatabaseNameEnum](DatabaseNameEnum.md) | External database names |
| [DataTypeEnum](DataTypeEnum.md) | Types of data |
| [DetectorModeEnum](DetectorModeEnum.md) | Operating modes for detectors during data collection |
| [DetectorTechnologyEnum](DetectorTechnologyEnum.md) | Generic detector technologies for structural biology imaging |
| [DetectorTypeEnum](DetectorTypeEnum.md) | DEPRECATED: Use DetectorTechnologyEnum instead |
| [EvidenceTypeEnum](EvidenceTypeEnum.md) | Types of evidence |
| [ExperimentalMethodEnum](ExperimentalMethodEnum.md) | Experimental methods for structure determination |
| [ExperimentSampleRoleEnum](ExperimentSampleRoleEnum.md) | Role of a sample in an experiment |
| [FacilityEnum](FacilityEnum.md) | Major synchrotron and structural biology research facilities worldwide |
| [FacilityTypeEnum](FacilityTypeEnum.md) | Types of research facilities |
| [FileFormatEnum](FileFormatEnum.md) | File formats |
| [FunctionalEffectEnum](FunctionalEffectEnum.md) | Effect on protein function |
| [FunctionalSiteTypeEnum](FunctionalSiteTypeEnum.md) | Types of functional sites in proteins |
| [GridMaterialEnum](GridMaterialEnum.md) | Materials used for EM grids |
| [GridTypeEnum](GridTypeEnum.md) | Types of EM grids |
| [GrowthFacilityEnum](GrowthFacilityEnum.md) | Type of facility where the sampled plant was grown (e |
| [IlluminationTypeEnum](IlluminationTypeEnum.md) | Types of illumination for optical microscopy |
| [ImagingModeEnum](ImagingModeEnum.md) | Imaging modes for electron microscopy |
| [InputTypeEnum](InputTypeEnum.md) | Type of input for a workflow |
| [InstrumentCategoryEnum](InstrumentCategoryEnum.md) | Categories of instruments based on their nature and location |
| [InstrumentRoleEnum](InstrumentRoleEnum.md) | Role of an instrument in an experiment |
| [InstrumentStatusEnum](InstrumentStatusEnum.md) | Operational status of instruments |
| [InteractionEvidenceEnum](InteractionEvidenceEnum.md) | Evidence for interactions |
| [InteractionTypeEnum](InteractionTypeEnum.md) | Types of molecular interactions |
| [MutationTypeEnum](MutationTypeEnum.md) | Types of mutations |
| [OutputTypeEnum](OutputTypeEnum.md) | Types of outputs from computational workflows |
| [PloidyTypeEnum](PloidyTypeEnum.md) | The ploidy level of the genome |
| [PreparationTypeEnum](PreparationTypeEnum.md) | Types of sample preparation |
| [ProcessingStatusEnum](ProcessingStatusEnum.md) | Processing status |
| [PTMTypeEnum](PTMTypeEnum.md) | Types of post-translational modifications |
| [SamplePreservationEnum](SamplePreservationEnum.md) | The method employed for preserving or fixing the tissue |
| [SampleRoleEnum](SampleRoleEnum.md) | Role of a sample in a study |
| [SampleTypeEnum](SampleTypeEnum.md) | Types of biological samples |
| [SecondaryStructureEnum](SecondaryStructureEnum.md) | Secondary structure types |
| [StabilityEffectEnum](StabilityEffectEnum.md) | Effect on protein stability |
| [StructuralFeatureTypeEnum](StructuralFeatureTypeEnum.md) | Types of structural features |
| [SymmetryEnum](SymmetryEnum.md) | Crystallographic and non-crystallographic symmetry groups for cryo-EM |
| [TechniqueEnum](TechniqueEnum.md) | Structural biology techniques |
| [VitrificationMethodEnum](VitrificationMethodEnum.md) | Methods for vitrification |
| [WorkflowTypeEnum](WorkflowTypeEnum.md) | Types of processing workflows |
| [XRaySourceTypeEnum](XRaySourceTypeEnum.md) | Types of X-ray sources |


## Types

| Type | Description |
| --- | --- |
| [Boolean](Boolean.md) | A binary (true or false) value |
| [Curie](Curie.md) | a compact URI |
| [Date](Date.md) | a date (year, month and day) in an idealized calendar |
| [DateOrDatetime](DateOrDatetime.md) | Either a date or a datetime |
| [Datetime](Datetime.md) | The combination of a date and time |
| [Decimal](Decimal.md) | A real number with arbitrary precision that conforms to the xsd:decimal speci... |
| [DecimalDegree](DecimalDegree.md) | A decimal degree expresses latitude or longitude as decimal fractions |
| [Double](Double.md) | A real number that conforms to the xsd:double specification |
| [Float](Float.md) | A real number that conforms to the xsd:float specification |
| [Integer](Integer.md) | An integer |
| [Jsonpath](Jsonpath.md) | A string encoding a JSON Path |
| [Jsonpointer](Jsonpointer.md) | A string encoding a JSON Pointer |
| [Ncname](Ncname.md) | Prefix part of CURIE |
| [Nodeidentifier](Nodeidentifier.md) | A URI, CURIE or BNODE that represents a node in a model |
| [Objectidentifier](Objectidentifier.md) | A URI or CURIE that represents an object in the model |
| [SmilesString](SmilesString.md) | A SMILES representation of a chemical structure |
| [Sparqlpath](Sparqlpath.md) | A string encoding a SPARQL Property Path |
| [String](String.md) | A character string |
| [Time](Time.md) | A time object represents a (local) time of day, independent of any particular... |
| [Uri](Uri.md) | a complete URI |
| [Uriorcurie](Uriorcurie.md) | a URI or a CURIE |


## Subsets

| Subset | Description |
| --- | --- |
