# OME (Open Microscopy Environment) and aims-leaf Alignment

## Executive Summary

The Open Microscopy Environment (OME) provides established standards for biological imaging data, while aims-leaf extends these concepts to structural biology techniques. This document outlines how aims-leaf aligns with and complements OME standards, enabling interoperability between light/fluorescence microscopy and structural biology data.

## OME Overview

### What is OME?

The Open Microscopy Environment is a consortium developing open-source software and format standards for biological microscopy data. Established in 2005, OME has become the de facto standard for microscopy data management in the life sciences.

### Core Components

1. **OME Data Model**: A comprehensive specification for storing biological imaging data
2. **Bio-Formats**: Library translating 160+ proprietary formats into the common OME model
3. **OMERO**: Server platform for managing, visualizing, and analyzing microscopy data
4. **OME-TIFF**: Standard file format combining TIFF images with OME-XML metadata
5. **OME-NGFF**: Next-generation cloud-native formats (Zarr-based)

### OME Data Model Structure

The OME model centers around these key entities:

```
Image
├── Pixels (dimensional and type information)
│   ├── Channel (wavelength, fluorophore)
│   ├── Plane (2D slice with timing)
│   └── BinData/TiffData (raw pixel data)
├── Instrument (microscope configuration)
│   ├── Microscope
│   ├── Objective
│   ├── Detector
│   └── LightSource
├── Experiment (experimental context)
├── Experimenter (person metadata)
└── ROI (Regions of Interest)
    └── Shape (rectangles, polygons, etc.)
```

## aims-leaf-OME Alignment

### Shared Concepts

aims-leaf intentionally aligns with OME in several fundamental areas:

#### 1. Image-Centric Data Model

**OME Approach:**
- Images are first-class entities with rich metadata
- Hierarchical structure from Image → Pixels → Planes

**aims-leaf Alignment:**
```yaml
Image (abstract base)
├── Image2D (micrographs, diffraction patterns)
├── Image3D (volumes, tomograms)
├── FluorescenceImage (OME-compatible fluorescence)
├── OpticalImage (brightfield, phase contrast)
├── FTIRImage (spectroscopy imaging)
└── XRFImage (elemental mapping)
```

#### 2. Instrument Metadata

**OME Model:**
```xml
<Instrument ID="Instrument:1">
  <Microscope Type="Inverted"/>
  <Objective ID="Objective:1" LensNA="1.4"/>
  <Detector Type="PMT"/>
</Instrument>
```

**aims-leaf Parallel:**
```yaml
Instrument (abstract base)
├── CryoEMInstrument
│   ├── voltage: 300kV
│   ├── detector_type: direct_electron
│   └── pixel_size: 0.83Å
├── XRayInstrument
│   ├── source_type: synchrotron
│   └── wavelength: 0.97Å
└── SAXSInstrument
    ├── q_range: 0.01-4.0 Å⁻¹
    └── detector_type: hybrid_pixel
```

#### 3. Experimental Context

Both models capture:
- Experimenter information
- Acquisition parameters
- Sample preparation details
- Processing workflows

### Complementary Extensions

aims-leaf extends OME concepts for structural biology:

#### 1. Multi-Technique Integration

While OME focuses on light microscopy, aims-leaf adds:
- Cryo-EM specific parameters (defocus, CTF, particle picking)
- X-ray crystallography (space groups, unit cells, phasing)
- Small-angle scattering (Guinier analysis, P(r) distributions)
- Spectroscopy imaging (FTIR, XRF)

#### 2. Molecular Composition

aims-leaf adds detailed biomolecular information:
```yaml
MolecularComposition:
  sequences: [amino acid/nucleotide sequences]
  modifications: [PTMs, chemical modifications]
  ligands: [bound cofactors, substrates]
```

OME typically handles this through structured annotations.

#### 3. Processing Workflows

aims-leaf explicitly models computational workflows:
```yaml
WorkflowRun:
  workflow_type: refinement
  software_name: RELION
  processing_level: 3  # raw→processed→refined
```

OME uses AnalysisModule for similar purposes but with less domain specificity.

## Interoperability Strategies

### 1. Direct Mapping for Shared Concepts

| OME Entity | aims-leaf Entity | Notes |
|------------|------------------|-------|
| Image | Image | Base class alignment |
| Pixels | Image2D/3D dimensions | Dimensional metadata |
| Channel | FluorescenceImage.excitation_wavelength | Spectral information |
| Instrument | Instrument | Polymorphic specialization |
| Experimenter | Study.principal_investigator | Personnel tracking |
| ROI | Not yet implemented | Future enhancement |

### 2. OME-Compatible Subclasses

aims-leaf's `FluorescenceImage` and `OpticalImage` classes are designed to be OME-compatible:

```yaml
FluorescenceImage:
  excitation_wavelength: 488  # nm, maps to OME Channel
  emission_wavelength: 520    # nm
  fluorophore: "GFP"          # OME Fluor
  exposure_time: 100           # ms, OME Plane.ExposureTime
```

### 3. Bio-Formats Integration Points

aims-leaf data can interface with Bio-Formats through:
- Standard image formats (TIFF, PNG, JPEG)
- OME-TIFF export for compatible image types
- Metadata translation layers

### 4. OMERO Compatibility

Structural biology images can be stored in OMERO with:
- Custom annotations for technique-specific metadata
- Tag-based organization for multi-technique studies
- Integration with existing OMERO analysis workflows

## Practical Integration Examples

### Example 1: Correlative Microscopy

Study combining fluorescence microscopy (OME) with cryo-EM (aims-leaf):

```yaml
Study:
  images:
    - id: fluor-001
      _type: FluorescenceImage  # OME-compatible
      file_name: "cells_gfp.ome.tiff"
      excitation_wavelength: 488
      emission_wavelength: 520
      
    - id: cryoem-001
      _type: Image2D  # aims-leaf cryo-EM
      file_name: "micrograph_001.mrc"
      defocus: -2.5
      pixel_size: 1.06
```

### Example 2: Multi-Scale Imaging

Linking OME light microscopy with aims-leaf X-ray imaging:

```yaml
images:
  - id: optical-overview
    _type: OpticalImage
    illumination_type: brightfield
    magnification: 10
    # Compatible with OME Objective.NominalMagnification
    
  - id: xrf-map
    _type: XRFImage  
    beam_energy: 12.4  # keV
    beam_size: 2.0     # μm
    # aims-leaf-specific X-ray fluorescence
```

## Benefits of Alignment

### For Users
1. **Familiar concepts**: Users experienced with OME find similar patterns in aims-leaf
2. **Tool reuse**: Existing OME tools can process compatible aims-leaf data
3. **Unified workflows**: Correlative studies span both frameworks seamlessly

### For Developers
1. **Established patterns**: Leverage proven OME design patterns
2. **Interoperability**: Data exchange between OME and aims-leaf systems
3. **Community standards**: Build on 15+ years of OME community experience

### For Facilities
1. **Integrated management**: Single platform for light and structural biology
2. **Metadata consistency**: Unified approach across techniques
3. **Compliance**: Meet FAIR data principles through established standards

## Future Convergence Opportunities

### 1. OME-NGFF for Structural Biology

Extend OME's Next-Generation File Format (Zarr-based) for:
- Large cryo-EM datasets
- Multi-resolution electron tomography
- Cloud-native structural biology workflows

### 2. Shared Ontologies

Develop common controlled vocabularies:
- Sample types (cells, proteins, complexes)
- Preparation methods
- Quality metrics

### 3. Analysis Pipeline Integration

Create adapters between:
- OMERO.scripts ↔ aims-leaf WorkflowRuns
- Bio-Formats readers ↔ Structural biology formats
- ImageJ/Fiji plugins ↔ Structural biology tools

### 4. Unified Visualization

Develop viewers supporting both:
- OME pyramidal TIFF for large 2D images
- aims-leaf MRC/MAP files for 3D densities
- Correlative overlay capabilities

## Implementation Recommendations

### Phase 1: Core Compatibility
- Ensure base Image class alignment
- Implement OME-TIFF export for applicable images
- Create Bio-Formats metadata translators

### Phase 2: Enhanced Integration
- Develop OMERO.table definitions for aims-leaf metadata
- Create Bio-Formats readers for common structural formats
- Implement OME-XML serialization for compatible entities

### Phase 3: Full Convergence
- Contribute structural biology extensions to OME model
- Develop unified OME-NGFF specification
- Create reference implementation and validators

## Conclusion

aims-leaf's alignment with OME standards creates a bridge between traditional microscopy and structural biology data management. This alignment enables:

1. **Reuse** of established tools and workflows
2. **Interoperability** between imaging modalities
3. **Unified** data management strategies
4. **Community** convergence around common standards

By building on OME's successful foundation while extending it for structural biology's unique needs, aims-leaf facilitates the integration of multi-scale, multi-modal biological imaging data essential for modern integrative structural biology.

## References

- OME Data Model Specification: https://docs.openmicroscopy.org/ome-model/
- Bio-Formats Documentation: https://docs.openmicroscopy.org/bio-formats/
- OMERO Platform: https://www.openmicroscopy.org/omero/
- OME-NGFF Specification: https://ngff.openmicroscopy.org/
- Goldberg et al. (2005) "The Open Microscopy Environment (OME) Data Model and XML file" Genome Biology 6:R47