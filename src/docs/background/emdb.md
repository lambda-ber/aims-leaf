# aims-leaf and EMDB/EMPIAR Alignment Analysis

> **Note**: This document was generated using Claude (Anthropic's AI assistant) through automated analysis of documentation and web sources. While efforts have been made to ensure accuracy, there may be errors or outdated information. Please verify critical details with official EMDB/EMPIAR documentation.

## Overview

This document analyzes the alignment between the aims-leaf schema and the EMDB (Electron Microscopy Data Bank) / EMPIAR (Electron Microscopy Public Image Archive) ecosystem, examining compatibility, complementary features, and integration strategies for cryo-EM data management.

## Introduction to EMDB/EMPIAR

### What is EMDB?

The Electron Microscopy Data Bank (EMDB) is the global archive for 3D electron microscopy density maps and tomograms. Key characteristics:

- **Purpose**: Archive 3D cryo-EM maps, tomograms, and associated metadata
- **Governance**: Managed by wwPDB consortium since 2021
- **Content**: >30,000 entries (October 2023), doubling every ~2.5 years
- **Format**: CCP4/MRC map format with XML metadata headers
- **Integration**: ~55% of entries have associated PDB atomic models

### What is EMPIAR?

The Electron Microscopy Public Image Archive complements EMDB:

- **Purpose**: Archive raw EM data (movies, micrographs, particle stacks)
- **Content**: >1,000 entries totaling >2 petabytes
- **Relationship**: Raw data underpinning EMDB 3D reconstructions
- **Scope**: Single particle, tomography, 2D crystallography data

### Current Status (2024)

- **Growth**: EMDB projected to reach 50,000 entries by 2025
- **Dominance**: 3DEM releases expected to surpass crystallography in 2025
- **Evolution**: XML schema v3.0 with enhanced detector and sample metadata
- **Integration**: Unified OneDep deposition system with PDB

## Fundamental Differences in Scope and Purpose

### EMDB/EMPIAR
- **Primary domain**: 3D cryo-EM reconstructions and raw EM data
- **Data model**: XML metadata + CCP4 maps (EMDB), raw images (EMPIAR)
- **Focus**: Final maps, half-maps, and underlying image data
- **Standardization**: wwPDB Core Archive with community governance
- **Target users**: Cryo-EM practitioners, structural biologists

### aims-leaf
- **Primary domain**: Multi-modal structural biology workflows
- **Data model**: LinkML semantic schema (generates multiple formats)
- **Focus**: Sample-to-structure workflow tracking
- **Standardization**: Research schema for data integration
- **Target users**: Integrative structural biology researchers

## Structural Alignment

| EMDB/EMPIAR Concept | aims-leaf Equivalent | Alignment Notes |
|---------------------|---------------------|-----------------|
| **EMDB Entry** | **Study** | Both represent complete experimental datasets |
| **em_admin** | **Dataset metadata** | Administrative and submission information |
| **em_sample** | **Sample** | ✅ Strong alignment - specimen preparation details |
| **em_imaging** | **CryoEMInstrument + ExperimentRun** | ✅ Microscope parameters and data collection |
| **em_software** | **WorkflowRun.software_name** | Processing software tracking |
| **em_image_processing** | **WorkflowRun** | ✅ Processing workflows and parameters |
| **Half-maps** | **DataFile** (type: volume) | Validation data products |
| **FSC curves** | **QualityMetrics.resolution** | Resolution assessment |
| **Segmentation** | **DataFile** (type: segmentation) | Interpreted volumes |
| **EMPIAR raw data** | **DataFile** (type: micrograph) | ✅ Raw image data references |

## Detailed Metadata Mapping

### Sample Preparation

**EMDB XML Schema v3.0:**
```xml
<em_sample>
  <macromolecule>
    <sciSpeciesName>
    <syntheticFlag>
    <mutantFlag>
  </macromolecule>
  <specimen_preparation>
    <specimen_state>
    <vitrification>
      <cryogen_name>
      <chamber_temperature>
      <chamber_humidity>
    </vitrification>
  </specimen_preparation>
</em_sample>
```

**aims-leaf Equivalent:**
```yaml
Sample:
  sample_type: protein/complex
  molecular_composition:
    sequences: [...]
    modifications: [...]
  
SamplePreparation:
  preparation_type: cryo_em
  
CryoEMPreparation:
  vitrification_method: plunge_freezing
  chamber_temperature: 4.0
  humidity_percentage: 95.0
```

### Data Collection

**EMDB Categories:**
```xml
<em_imaging>
  <microscope>TITAN KRIOS</microscope>
  <accelerating_voltage>300</accelerating_voltage>
  <detector>GATAN K3 (6k x 4k)</detector>
  <electron_dose>40.0</electron_dose>
  <pixel_size>0.85</pixel_size>
</em_imaging>
```

**aims-leaf Equivalent:**
```yaml
CryoEMInstrument:
  model: "Titan Krios G4"
  accelerating_voltage: 300
  detector_type: direct_electron
  detector_dimensions: "5760x4092"

ExperimentRun:
  technique: cryo_em
  data_collection_strategy:
    total_dose: 40.0
    
Image2D:
  pixel_size: 0.85
  dose: 40.0
```

### Processing Workflow

**EMDB Processing:**
```xml
<em_image_processing>
  <reconstruction_method>SINGLE PARTICLE</reconstruction_method>
  <software>
    <name>cryoSPARC</name>
    <version>4.4.0</version>
  </software>
  <resolution>2.8</resolution>
  <resolution_method>FSC 0.143 CUT-OFF</resolution_method>
</em_image_processing>
```

**aims-leaf Equivalent:**
```yaml
WorkflowRun:
  workflow_type: refinement
  software_name: "cryoSPARC"
  software_version: "4.4.0"
  
QualityMetrics:
  resolution: 2.8
  completeness: 99.5
```

## Key Differences

### 1. Data Granularity

**EMDB/EMPIAR**: Map-centric with raw data separation
- Final 3D reconstructions (EMDB)
- Half-maps for validation
- Raw images in separate archive (EMPIAR)
- FSC curves and validation metrics

**aims-leaf**: Workflow-centric integration
- Unified tracking across data types
- Sample lineage and preparation history
- Processing attempts and parameters
- Multi-technique integration

### 2. Validation Focus

**EMDB**: Extensive validation infrastructure
- Mandatory half-map deposition (since 2022)
- FSC validation (0.143 criterion)
- Map-model fit assessment
- Visual analysis pages

**aims-leaf**: Workflow validation
- Data integrity (checksums)
- Processing provenance
- Parameter tracking
- Quality metrics capture

### 3. Archive Philosophy

**EMDB/EMPIAR**: Specialized repositories
- EMDB: Processed maps
- EMPIAR: Raw data
- PDB: Atomic models
- Federated but separate

**aims-leaf**: Unified schema
- Single coherent model
- References to external data
- Integrated metadata
- Multi-modal support

### 4. Community Standards

**EMDB**: Established community practices
- EM Validation Task Force (EM-VTF)
- Community-driven schema evolution
- Standardized deposition via OneDep

**aims-leaf**: Emerging integration framework
- Flexible for new techniques
- Cross-technique harmonization
- Research-driven development

## Integration Strategies

### aims-leaf → EMDB/EMPIAR Export

```python
# Conceptual mapping for EMDB deposition
def aims-leaf_to_emdb(study):
    emdb_metadata = {
        'em_admin': {
            'title': study.title,
            'authors': extract_operators(study)
        },
        'em_sample': {
            'macromolecule': extract_molecular_info(study.samples),
            'specimen_preparation': extract_prep(study.sample_preparations)
        },
        'em_imaging': {
            'microscope': study.instrument.model,
            'detector': study.instrument.detector_type,
            'pixel_size': study.images[0].pixel_size
        },
        'em_image_processing': {
            'software': extract_software(study.workflow_runs),
            'resolution': study.quality_metrics.resolution
        }
    }
    return generate_xml(emdb_metadata)
```

### EMDB/EMPIAR → aims-leaf Import

```yaml
# aims-leaf representation of EMDB/EMPIAR data
Study:
  title: "Imported from EMDB-12345"
  
  samples:
    - id: "from_emdb_sample"
      molecular_composition: # From em_sample
      
  instrument_runs:
    - technique: cryo_em
      instrument_id: # From em_imaging.microscope
      
  data_files:
    - file_name: "emd_12345.map"
      file_format: mrc
      data_type: volume
      external_ids:
        emdb_id: "EMD-12345"
    - file_name: "empiar_10789_movies.tar"
      data_type: micrograph
      external_ids:
        empiar_id: "EMPIAR-10789"
```

### Hybrid Workflow

1. **Data Collection**: Use aims-leaf to track samples and experiments
2. **Raw Data**: Deposit movies/micrographs to EMPIAR
3. **Processing**: Track workflows in aims-leaf
4. **Map Deposition**: Submit final maps to EMDB
5. **Model Deposition**: Submit coordinates to PDB
6. **Integration**: Link all components via aims-leaf

## Complementary Strengths

### EMDB/EMPIAR Strengths
- **Established repository**: 20+ years of community trust
- **Validation pipeline**: Comprehensive map validation
- **Raw data archive**: Petabyte-scale EMPIAR storage
- **Community standards**: EM-VTF recommendations
- **Global accessibility**: wwPDB integration

### aims-leaf Strengths
- **Workflow tracking**: Complete experimental history
- **Multi-modal support**: Beyond just cryo-EM
- **Sample management**: Detailed preparation tracking
- **Processing flexibility**: Multiple attempts/parameters
- **Semantic integration**: Knowledge graph compatibility

## Validation and Quality Control

### EMDB Validation Components

1. **Map Validation**
   - Half-map FSC curves
   - Resolution estimation
   - Map statistics

2. **Map-Model Validation**
   - FSC between map and model
   - Atom inclusion analysis
   - 3D-Strudel scores

3. **Visual Analysis**
   - Orthogonal projections
   - Surface views
   - Density distributions

### aims-leaf Quality Tracking

```yaml
QualityMetrics:
  resolution: 2.8  # Maps to EMDB resolution
  completeness: 99.5
  signal_to_noise: 4.2
  
DataFile:
  checksum: "sha256:..."  # Data integrity
  file_format: mrc
  processing_level: 3  # Final reconstruction
```

## Recommended Integration Approach

### 1. Pre-deposition Phase
Use aims-leaf for:
- Sample preparation documentation
- Instrument configuration tracking
- Data collection parameters
- Processing workflow management

### 2. Deposition Preparation
```yaml
# Link aims-leaf to EMDB/EMPIAR
DataFile:
  file_name: "final_map.mrc"
  external_ids:
    emdb_id: "EMD-12345"  # After deposition
    empiar_id: "EMPIAR-10789"
    pdb_id: "7XYZ"
```

### 3. Post-deposition Integration
- Maintain aims-leaf records for complete provenance
- Update with deposition IDs
- Enable cross-archive queries
- Support reprocessing efforts

## Future Directions

### Emerging Trends

1. **Volume Growth**: EMDB doubling every 2.5 years
2. **Method Diversity**: Beyond single particle (tomography, MicroED)
3. **Multimodal Integration**: Combining EM with other techniques
4. **AI/ML Models**: AlphaFold integration, ModelArchive

### Opportunities for Alignment

1. **Metadata Harmonization**
   - Align sample preparation vocabularies
   - Standardize instrument specifications
   - Common quality metrics

2. **Workflow Standards**
   - Processing pipeline descriptions
   - Software parameter capture
   - Validation criteria

3. **Cross-Archive Queries**
   - Federated search capabilities
   - Linked data approaches
   - Semantic integration

### Technical Development Needs

1. **Conversion Tools**
   - `aims-leaf2emdb`: Generate EMDB XML from aims-leaf
   - `empiar_linker`: Connect aims-leaf to EMPIAR datasets
   - `validation_bridge`: Map validation metrics

2. **Schema Extensions**
   - Add EMDB-specific validation metrics to aims-leaf
   - Include half-map tracking
   - Support segmentation references

## Best Practices

### For Researchers

1. **Use aims-leaf** during active research for comprehensive tracking
2. **Prepare for deposition** early with required EMDB metadata
3. **Maintain links** between aims-leaf records and archive IDs
4. **Document workflows** thoroughly for reproducibility

### For Developers

1. **Implement validators** for EMDB compliance
2. **Build converters** for seamless data flow
3. **Maintain mappings** as schemas evolve
4. **Support community** standards and practices

## Conclusion

aims-leaf and EMDB/EMPIAR serve **complementary and essential roles** in the cryo-EM data ecosystem:

- **EMDB/EMPIAR** provides the definitive archives for 3D maps and raw EM data with established validation
- **aims-leaf** offers comprehensive workflow tracking and multi-modal integration capabilities

The optimal approach involves:
1. Using aims-leaf for experiment management and workflow tracking
2. Depositing to EMDB/EMPIAR for long-term archival and community access
3. Maintaining bidirectional links for complete data provenance
4. Leveraging each system's strengths throughout the research lifecycle

This complementary relationship ensures that both the experimental journey (aims-leaf) and the scientific products (EMDB/EMPIAR) are properly documented, validated, and preserved for the global research community. As cryo-EM continues its explosive growth, the integration of these systems becomes increasingly important for managing the complexity and scale of modern structural biology research.