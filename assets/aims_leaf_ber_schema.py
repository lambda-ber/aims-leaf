# Auto generated from aims_leaf_ber_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-20T14:43:18
# Schema: aims-leaf
#
# id: https://w3id.org/aims-leaf/
# description: aims-leaf is a comprehensive schema for representing multimodal structural biology imaging data,
#   from atomic-resolution structures to tissue-level organization. It supports diverse experimental
#   techniques including cryo-EM, X-ray crystallography, SAXS/SANS, fluorescence microscopy, and
#   spectroscopic imaging.
#
#   ## Schema Organization
#
#   The schema follows a **relational design** with flat entity collections and explicit association
#   tables for many-to-many relationships. This maps cleanly to SQL databases while supporting
#   flexible data reuse across studies.
#
#   The top-level entity is a [Dataset](Dataset.md), which serves as a container for related research.
#   A dataset might represent all data from a specific grant, collaboration, or publication.
#
#   ### Entity Tables
#
#   All entities are stored in flat collections at the Dataset level:
#
#   **Biological Materials**
#   - [Samples](Sample.md): The biological specimens being studied (proteins, nucleic acids, complexes,
#     cells, tissues). Each sample includes detailed molecular composition, buffer conditions, and
#     storage information. For example, a purified protein with its sequence, concentration, and buffer pH.
#
#   - [Sample Preparations](SamplePreparation.md): How samples were prepared for specific techniques.
#     This includes cryo-EM grid preparation (vitrification parameters), crystallization conditions for
#     X-ray studies, or staining protocols for fluorescence microscopy.
#
#   **Data Collection**
#   - [Instruments](Instrument.md): The equipment used, from Titan Krios microscopes to synchrotron
#     beamlines. Each instrument type ([CryoEMInstrument](CryoEMInstrument.md),
#     [XRayInstrument](XRayInstrument.md), [SAXSInstrument](SAXSInstrument.md)) has specific parameters
#     like accelerating voltage, detector type, or beam energy.
#
#   - [Experiment Runs](ExperimentRun.md): Individual data collection sessions. An experiment run
#     captures when, how, and under what conditions data was collected, including quality metrics
#     like resolution and completeness.
#
#   **Data Processing**
#   - [Workflow Runs](WorkflowRun.md): Computational processing steps applied to raw data. This includes
#     motion correction for cryo-EM movies, 3D reconstruction, model building, or phase determination
#     for crystallography. Each workflow tracks the software used, parameters, and computational resources.
#
#   **Data Products**
#   - [Data Files](DataFile.md): Any files generated or used, from raw data to final models. Each file
#     is tracked with checksums for data integrity and typed (micrograph, particles, volume, model).
#
#   - [Images](Image.md): Specialized classes for different imaging modalities:
#     - [Image2D](Image2D.md): Micrographs, diffraction patterns
#     - [Image3D](Image3D.md): 3D reconstructions, tomograms
#     - [FTIRImage](FTIRImage.md): Molecular composition maps from infrared spectroscopy
#     - [FluorescenceImage](FluorescenceImage.md): Fluorophore-labeled cellular components
#     - [OpticalImage](OpticalImage.md): Brightfield/phase contrast microscopy
#     - [XRFImage](XRFImage.md): Elemental distribution maps
#
#   **Logical Groupings**
#   - [Studies](Study.md): Lightweight groupings representing focused investigations of specific
#     biological questions. For example, a study might investigate "Heat stress response in Arabidopsis"
#     or "Structure of the human ribosome under different conditions."
#
#   ### Association Tables
#
#   Many-to-many relationships are represented via explicit association tables, which can carry
#   relationship metadata (e.g., the role of a sample in an experiment):
#
#   - **StudySampleAssociation**: Links samples to studies (with role: target, control, reference)
#   - **StudyExperimentAssociation**: Links experiments to studies
#   - **StudyWorkflowAssociation**: Links workflows to studies
#   - **ExperimentSampleAssociation**: Links samples to experiments (with role and preparation used)
#   - **ExperimentInstrumentAssociation**: Links instruments to experiments (with role: primary, detector)
#   - **WorkflowExperimentAssociation**: Links source experiments to workflows
#   - **WorkflowInputAssociation**: Links input files to workflows
#   - **WorkflowOutputAssociation**: Links output files to workflows
#
#   This relational design enables:
#   - **Sample reuse**: The same sample can be used in multiple studies and experiments
#   - **Multi-instrument experiments**: An experiment can use multiple instruments with different roles
#   - **Integrative workflows**: A workflow can combine data from multiple experiments
#
#   ## Example Usage
#
#   A typical cryo-EM study of a protein complex would include:
#   1. Sample records for the purified complex with molecular weight and buffer composition
#   2. Grid preparation details with vitrification parameters
#   3. Microscope specifications and data collection parameters
#   4. Processing workflows from motion correction through 3D refinement
#   5. Final reconstructed volumes and fitted atomic models
#
#   A multimodal plant imaging study might combine:
#   1. Whole plant optical imaging for morphology
#   2. XRF imaging to map nutrient distribution
#   3. FTIR spectroscopy to identify stress-related molecular changes
#   4. Fluorescence microscopy to track specific protein responses
#   5. Cryo-EM of isolated organelles for ultrastructural details
#
#   ## Key Features
#
#   - **Relational design**: Flat entity tables with explicit association tables for M:N relationships
#   - **SQL-friendly**: Maps directly to normalized database tables
#   - **Technique-agnostic core**: The same schema handles data from any structural biology method
#   - **Rich metadata**: Comprehensive tracking from sample to structure
#   - **Workflow provenance**: Complete computational reproducibility
#   - **Multimodal support**: Seamlessly integrate data across scales and techniques
#   - **Standards-compliant**: Follows FAIR principles and integrates with existing ontologies
#
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Curie, Date, Float, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, Curie, URI, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = "0.0.0.post2.dev0+ec8ec92"

# Namespaces
CHMO = CurieNamespace('CHMO', 'http://purl.obolibrary.org/obo/CHMO_')
CL = CurieNamespace('CL', 'http://purl.obolibrary.org/obo/CL_')
GO = CurieNamespace('GO', 'http://purl.obolibrary.org/obo/GO_')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
PANET = CurieNamespace('PaNET', 'http://purl.org/pan-science/PaNET/PaNET')
ROR = CurieNamespace('ROR', 'https://ror.org/')
UBERON = CurieNamespace('UBERON', 'http://purl.obolibrary.org/obo/UBERON_')
UO = CurieNamespace('UO', 'http://purl.obolibrary.org/obo/UO_')
AIMSLEAF = CurieNamespace('aimsleaf', 'https://w3id.org/aims-leaf/')
AIMSPLANT = CurieNamespace('aimsplant', 'https://w3id.org/aims-leaf/plant/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
IMGCIF = CurieNamespace('imgCIF', 'https://github.com/dials/cbflib/blob/main/doc/cif_img_1.8.6.dic#')
ISPYB = CurieNamespace('ispyb', 'https://ispyb.github.io/ISPyB/')
LAMBDABER = CurieNamespace('lambdaber', 'https://w3id.org/aims-leaf/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MMCIF = CurieNamespace('mmCIF', 'http://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/')
NMDC = CurieNamespace('nmdc', 'https://w3id.org/nmdc/')
NSLS2 = CurieNamespace('nsls2', 'https://github.com/NSLS2/BER-LAMBDA/')
PDB = CurieNamespace('pdb', 'https://files.rcsb.org/download/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
QUD = CurieNamespace('qud', 'http://qudt.org/1.1/schema/qudt#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'https://schema.org/')
SIMPLESCATTERING = CurieNamespace('simplescattering', 'https://www.simplescattering.com/open_dataset/')
SIO = CurieNamespace('sio', 'http://semanticscience.org/resource/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
WIKIDATA = CurieNamespace('wikidata', 'http://www.wikidata.org/entity/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = AIMSLEAF


# Types
class DecimalDegree(float):
    """ A decimal degree expresses latitude or longitude as decimal fractions. """
    type_class_uri = XSD["decimal"]
    type_class_curie = "xsd:decimal"
    type_name = "decimal degree"
    type_model_uri = AIMSLEAF.DecimalDegree


class SmilesString(String):
    """ A SMILES representation of a chemical structure """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "smiles_string"
    type_model_uri = AIMSLEAF.SmilesString


# Class references
class NamedThingId(URIorCURIE):
    pass


class DatasetId(NamedThingId):
    pass


class StudyId(NamedThingId):
    pass


class SampleId(NamedThingId):
    pass


class SamplePreparationId(NamedThingId):
    pass


class InstrumentId(NamedThingId):
    pass


class CryoEMInstrumentId(InstrumentId):
    pass


class XRayInstrumentId(InstrumentId):
    pass


class ExperimentRunId(NamedThingId):
    pass


class WorkflowRunId(NamedThingId):
    pass


class DataFileId(NamedThingId):
    pass


class ImageId(NamedThingId):
    pass


class Image2DId(ImageId):
    pass


class Image3DId(ImageId):
    pass


class MovieId(Image2DId):
    pass


class FTIRImageId(DataFileId):
    pass


class FluorescenceImageId(Image2DId):
    pass


class OpticalImageId(Image2DId):
    pass


class XRFImageId(DataFileId):
    pass


class OntologyTermId(NamedThingId):
    pass


class ProteinAnnotationId(NamedThingId):
    pass


class FunctionalSiteId(ProteinAnnotationId):
    pass


class StructuralFeatureId(ProteinAnnotationId):
    pass


class ProteinProteinInteractionId(ProteinAnnotationId):
    pass


class MutationEffectId(ProteinAnnotationId):
    pass


class ConformationalEnsembleId(NamedThingId):
    pass


class PostTranslationalModificationId(ProteinAnnotationId):
    pass


class EvolutionaryConservationId(ProteinAnnotationId):
    pass


class AggregatedProteinViewId(NamedThingId):
    pass


class MeasurementConditionsId(NamedThingId):
    pass


class PlantSampleId(SampleId):
    pass


class PlantSamplePreparationId(SamplePreparationId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A named thing
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["NamedThing"]
    class_class_curie: ClassVar[str] = "aimsleaf:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.NamedThing

    id: Union[str, NamedThingId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AttributeGroup(YAMLRoot):
    """
    A grouping of related data attributes that form a logical unit
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["AttributeGroup"]
    class_class_curie: ClassVar[str] = "aimsleaf:AttributeGroup"
    class_name: ClassVar[str] = "AttributeGroup"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.AttributeGroup

    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Dataset(NamedThing):
    """
    Root container holding flat entity collections and association tables. Follows relational database design patterns
    for structural biology data.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["Dataset"]
    class_class_curie: ClassVar[str] = "aimsleaf:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.Dataset

    id: Union[str, DatasetId] = None
    keywords: Optional[Union[str, list[str]]] = empty_list()
    studies: Optional[Union[dict[Union[str, StudyId], Union[dict, "Study"]], list[Union[dict, "Study"]]]] = empty_dict()
    instruments: Optional[Union[dict[Union[str, InstrumentId], Union[dict, "Instrument"]], list[Union[dict, "Instrument"]]]] = empty_dict()
    samples: Optional[Union[dict[Union[str, SampleId], Union[dict, "Sample"]], list[Union[dict, "Sample"]]]] = empty_dict()
    plantsamples: Optional[Union[dict[Union[str, PlantSampleId], Union[dict, "PlantSample"]], list[Union[dict, "PlantSample"]]]] = empty_dict()
    sample_preparations: Optional[Union[dict[Union[str, SamplePreparationId], Union[dict, "SamplePreparation"]], list[Union[dict, "SamplePreparation"]]]] = empty_dict()
    plant_sample_preparations: Optional[Union[dict[Union[str, PlantSamplePreparationId], Union[dict, "PlantSamplePreparation"]], list[Union[dict, "PlantSamplePreparation"]]]] = empty_dict()
    experiment_runs: Optional[Union[dict[Union[str, ExperimentRunId], Union[dict, "ExperimentRun"]], list[Union[dict, "ExperimentRun"]]]] = empty_dict()
    workflow_runs: Optional[Union[dict[Union[str, WorkflowRunId], Union[dict, "WorkflowRun"]], list[Union[dict, "WorkflowRun"]]]] = empty_dict()
    data_files: Optional[Union[dict[Union[str, DataFileId], Union[dict, "DataFile"]], list[Union[dict, "DataFile"]]]] = empty_dict()
    images: Optional[Union[dict[Union[str, ImageId], Union[dict, "Image"]], list[Union[dict, "Image"]]]] = empty_dict()
    sample_datafile_associations: Optional[Union[Union[dict, "SampleDataAssociation"], list[Union[dict, "SampleDataAssociation"]]]] = empty_list()
    study_sample_associations: Optional[Union[Union[dict, "StudySampleAssociation"], list[Union[dict, "StudySampleAssociation"]]]] = empty_list()
    study_experiment_associations: Optional[Union[Union[dict, "StudyExperimentAssociation"], list[Union[dict, "StudyExperimentAssociation"]]]] = empty_list()
    study_workflow_associations: Optional[Union[Union[dict, "StudyWorkflowAssociation"], list[Union[dict, "StudyWorkflowAssociation"]]]] = empty_list()
    experiment_sample_associations: Optional[Union[Union[dict, "ExperimentSampleAssociation"], list[Union[dict, "ExperimentSampleAssociation"]]]] = empty_list()
    experiment_instrument_associations: Optional[Union[Union[dict, "ExperimentInstrumentAssociation"], list[Union[dict, "ExperimentInstrumentAssociation"]]]] = empty_list()
    workflow_experiment_associations: Optional[Union[Union[dict, "WorkflowExperimentAssociation"], list[Union[dict, "WorkflowExperimentAssociation"]]]] = empty_list()
    workflow_input_associations: Optional[Union[Union[dict, "WorkflowInputAssociation"], list[Union[dict, "WorkflowInputAssociation"]]]] = empty_list()
    workflow_output_associations: Optional[Union[Union[dict, "WorkflowOutputAssociation"], list[Union[dict, "WorkflowOutputAssociation"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetId):
            self.id = DatasetId(self.id)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        self._normalize_inlined_as_list(slot_name="studies", slot_type=Study, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="instruments", slot_type=Instrument, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="samples", slot_type=Sample, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="plantsamples", slot_type=PlantSample, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sample_preparations", slot_type=SamplePreparation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="plant_sample_preparations", slot_type=PlantSamplePreparation, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="experiment_runs", slot_type=ExperimentRun, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="workflow_runs", slot_type=WorkflowRun, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="data_files", slot_type=DataFile, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="images", slot_type=Image, key_name="id", keyed=True)

        if not isinstance(self.sample_datafile_associations, list):
            self.sample_datafile_associations = [self.sample_datafile_associations] if self.sample_datafile_associations is not None else []
        self.sample_datafile_associations = [v if isinstance(v, SampleDataAssociation) else SampleDataAssociation(**as_dict(v)) for v in self.sample_datafile_associations]

        if not isinstance(self.study_sample_associations, list):
            self.study_sample_associations = [self.study_sample_associations] if self.study_sample_associations is not None else []
        self.study_sample_associations = [v if isinstance(v, StudySampleAssociation) else StudySampleAssociation(**as_dict(v)) for v in self.study_sample_associations]

        if not isinstance(self.study_experiment_associations, list):
            self.study_experiment_associations = [self.study_experiment_associations] if self.study_experiment_associations is not None else []
        self.study_experiment_associations = [v if isinstance(v, StudyExperimentAssociation) else StudyExperimentAssociation(**as_dict(v)) for v in self.study_experiment_associations]

        if not isinstance(self.study_workflow_associations, list):
            self.study_workflow_associations = [self.study_workflow_associations] if self.study_workflow_associations is not None else []
        self.study_workflow_associations = [v if isinstance(v, StudyWorkflowAssociation) else StudyWorkflowAssociation(**as_dict(v)) for v in self.study_workflow_associations]

        if not isinstance(self.experiment_sample_associations, list):
            self.experiment_sample_associations = [self.experiment_sample_associations] if self.experiment_sample_associations is not None else []
        self.experiment_sample_associations = [v if isinstance(v, ExperimentSampleAssociation) else ExperimentSampleAssociation(**as_dict(v)) for v in self.experiment_sample_associations]

        if not isinstance(self.experiment_instrument_associations, list):
            self.experiment_instrument_associations = [self.experiment_instrument_associations] if self.experiment_instrument_associations is not None else []
        self.experiment_instrument_associations = [v if isinstance(v, ExperimentInstrumentAssociation) else ExperimentInstrumentAssociation(**as_dict(v)) for v in self.experiment_instrument_associations]

        if not isinstance(self.workflow_experiment_associations, list):
            self.workflow_experiment_associations = [self.workflow_experiment_associations] if self.workflow_experiment_associations is not None else []
        self.workflow_experiment_associations = [v if isinstance(v, WorkflowExperimentAssociation) else WorkflowExperimentAssociation(**as_dict(v)) for v in self.workflow_experiment_associations]

        if not isinstance(self.workflow_input_associations, list):
            self.workflow_input_associations = [self.workflow_input_associations] if self.workflow_input_associations is not None else []
        self.workflow_input_associations = [v if isinstance(v, WorkflowInputAssociation) else WorkflowInputAssociation(**as_dict(v)) for v in self.workflow_input_associations]

        if not isinstance(self.workflow_output_associations, list):
            self.workflow_output_associations = [self.workflow_output_associations] if self.workflow_output_associations is not None else []
        self.workflow_output_associations = [v if isinstance(v, WorkflowOutputAssociation) else WorkflowOutputAssociation(**as_dict(v)) for v in self.workflow_output_associations]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Study(NamedThing):
    """
    A logical grouping of related experiments investigating a research question. In the relational model, Study is
    lightweight - all relationships are via association tables.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["Study"]
    class_class_curie: ClassVar[str] = "aimsleaf:Study"
    class_name: ClassVar[str] = "Study"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.Study

    id: Union[str, StudyId] = None
    keywords: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StudyId):
            self.id = StudyId(self.id)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(NamedThing):
    """
    A biological sample used in structural biology experiments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["Sample"]
    class_class_curie: ClassVar[str] = "aimsleaf:Sample"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.Sample

    id: Union[str, SampleId] = None
    sample_code: str = None
    sample_type: Union[str, "SampleTypeEnum"] = None
    molecular_weight: Optional[Union[dict, "QuantityValue"]] = None
    concentration: Optional[Union[dict, "QuantityValue"]] = None
    buffer_composition: Optional[Union[dict, "BufferComposition"]] = None
    preparation_method: Optional[str] = None
    storage_conditions: Optional[Union[dict, "StorageConditions"]] = None
    organism: Optional[Union[str, OntologyTermId]] = None
    anatomy: Optional[Union[str, OntologyTermId]] = None
    cell_type: Optional[Union[str, OntologyTermId]] = None
    parent_sample_id: Optional[Union[str, SampleId]] = None
    purity_percentage: Optional[Union[dict, "QuantityValue"]] = None
    quality_metrics: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self._is_empty(self.sample_code):
            self.MissingRequiredField("sample_code")
        if not isinstance(self.sample_code, str):
            self.sample_code = str(self.sample_code)

        if self._is_empty(self.sample_type):
            self.MissingRequiredField("sample_type")
        if not isinstance(self.sample_type, SampleTypeEnum):
            self.sample_type = SampleTypeEnum(self.sample_type)

        if self.molecular_weight is not None and not isinstance(self.molecular_weight, QuantityValue):
            self.molecular_weight = QuantityValue(**as_dict(self.molecular_weight))

        if self.concentration is not None and not isinstance(self.concentration, QuantityValue):
            self.concentration = QuantityValue(**as_dict(self.concentration))

        if self.buffer_composition is not None and not isinstance(self.buffer_composition, BufferComposition):
            self.buffer_composition = BufferComposition(**as_dict(self.buffer_composition))

        if self.preparation_method is not None and not isinstance(self.preparation_method, str):
            self.preparation_method = str(self.preparation_method)

        if self.storage_conditions is not None and not isinstance(self.storage_conditions, StorageConditions):
            self.storage_conditions = StorageConditions(**as_dict(self.storage_conditions))

        if self.organism is not None and not isinstance(self.organism, OntologyTermId):
            self.organism = OntologyTermId(self.organism)

        if self.anatomy is not None and not isinstance(self.anatomy, OntologyTermId):
            self.anatomy = OntologyTermId(self.anatomy)

        if self.cell_type is not None and not isinstance(self.cell_type, OntologyTermId):
            self.cell_type = OntologyTermId(self.cell_type)

        if self.parent_sample_id is not None and not isinstance(self.parent_sample_id, SampleId):
            self.parent_sample_id = SampleId(self.parent_sample_id)

        if self.purity_percentage is not None and not isinstance(self.purity_percentage, QuantityValue):
            self.purity_percentage = QuantityValue(**as_dict(self.purity_percentage))

        if self.quality_metrics is not None and not isinstance(self.quality_metrics, str):
            self.quality_metrics = str(self.quality_metrics)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SamplePreparation(NamedThing):
    """
    A process that prepares a sample for imaging
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["SamplePreparation"]
    class_class_curie: ClassVar[str] = "aimsleaf:SamplePreparation"
    class_name: ClassVar[str] = "SamplePreparation"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.SamplePreparation

    id: Union[str, SamplePreparationId] = None
    preparation_type: Union[str, "PreparationTypeEnum"] = None
    sample_id: Optional[str] = None
    preparation_date: Optional[Union[str, XSDDate]] = None
    operator_id: Optional[str] = None
    protocol_description: Optional[str] = None
    host_strain_or_cell_line: Optional[str] = None
    culture_volume_l: Optional[Union[dict, "QuantityValue"]] = None
    medium: Optional[str] = None
    antibiotic_selection: Optional[str] = None
    growth_temperature_c: Optional[Union[dict, "QuantityValue"]] = None
    induction_agent: Optional[str] = None
    inducer_concentration: Optional[str] = None
    induction_temperature_c: Optional[Union[dict, "QuantityValue"]] = None
    induction_time_h: Optional[Union[dict, "QuantityValue"]] = None
    od600_at_induction: Optional[Union[dict, "QuantityValue"]] = None
    harvest_timepoint: Optional[str] = None
    lysis_method: Optional[str] = None
    protease_inhibitors: Optional[str] = None
    affinity_type: Optional[str] = None
    affinity_column: Optional[str] = None
    lysis_buffer: Optional[str] = None
    wash_buffer: Optional[str] = None
    elution_buffer: Optional[str] = None
    tag_removal: Optional[Union[bool, Bool]] = None
    protease: Optional[str] = None
    protease_ratio: Optional[str] = None
    cleavage_time_h: Optional[Union[dict, "QuantityValue"]] = None
    cleavage_temperature_c: Optional[Union[dict, "QuantityValue"]] = None
    second_affinity_reverse: Optional[str] = None
    iex_column: Optional[str] = None
    hic_column: Optional[str] = None
    sec_column: Optional[str] = None
    sec_buffer: Optional[str] = None
    concentration_method: Optional[str] = None
    final_buffer: Optional[str] = None
    final_concentration_mg_per_ml: Optional[Union[dict, "QuantityValue"]] = None
    yield_mg: Optional[Union[dict, "QuantityValue"]] = None
    purity_by_sds_page_percent: Optional[Union[dict, "QuantityValue"]] = None
    aggregation_assessment: Optional[str] = None
    aliquoting: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SamplePreparationId):
            self.id = SamplePreparationId(self.id)

        if self._is_empty(self.preparation_type):
            self.MissingRequiredField("preparation_type")
        if not isinstance(self.preparation_type, PreparationTypeEnum):
            self.preparation_type = PreparationTypeEnum(self.preparation_type)

        if self.sample_id is not None and not isinstance(self.sample_id, str):
            self.sample_id = str(self.sample_id)

        if self.preparation_date is not None and not isinstance(self.preparation_date, XSDDate):
            self.preparation_date = XSDDate(self.preparation_date)

        if self.operator_id is not None and not isinstance(self.operator_id, str):
            self.operator_id = str(self.operator_id)

        if self.protocol_description is not None and not isinstance(self.protocol_description, str):
            self.protocol_description = str(self.protocol_description)

        if self.host_strain_or_cell_line is not None and not isinstance(self.host_strain_or_cell_line, str):
            self.host_strain_or_cell_line = str(self.host_strain_or_cell_line)

        if self.culture_volume_l is not None and not isinstance(self.culture_volume_l, QuantityValue):
            self.culture_volume_l = QuantityValue(**as_dict(self.culture_volume_l))

        if self.medium is not None and not isinstance(self.medium, str):
            self.medium = str(self.medium)

        if self.antibiotic_selection is not None and not isinstance(self.antibiotic_selection, str):
            self.antibiotic_selection = str(self.antibiotic_selection)

        if self.growth_temperature_c is not None and not isinstance(self.growth_temperature_c, QuantityValue):
            self.growth_temperature_c = QuantityValue(**as_dict(self.growth_temperature_c))

        if self.induction_agent is not None and not isinstance(self.induction_agent, str):
            self.induction_agent = str(self.induction_agent)

        if self.inducer_concentration is not None and not isinstance(self.inducer_concentration, str):
            self.inducer_concentration = str(self.inducer_concentration)

        if self.induction_temperature_c is not None and not isinstance(self.induction_temperature_c, QuantityValue):
            self.induction_temperature_c = QuantityValue(**as_dict(self.induction_temperature_c))

        if self.induction_time_h is not None and not isinstance(self.induction_time_h, QuantityValue):
            self.induction_time_h = QuantityValue(**as_dict(self.induction_time_h))

        if self.od600_at_induction is not None and not isinstance(self.od600_at_induction, QuantityValue):
            self.od600_at_induction = QuantityValue(**as_dict(self.od600_at_induction))

        if self.harvest_timepoint is not None and not isinstance(self.harvest_timepoint, str):
            self.harvest_timepoint = str(self.harvest_timepoint)

        if self.lysis_method is not None and not isinstance(self.lysis_method, str):
            self.lysis_method = str(self.lysis_method)

        if self.protease_inhibitors is not None and not isinstance(self.protease_inhibitors, str):
            self.protease_inhibitors = str(self.protease_inhibitors)

        if self.affinity_type is not None and not isinstance(self.affinity_type, str):
            self.affinity_type = str(self.affinity_type)

        if self.affinity_column is not None and not isinstance(self.affinity_column, str):
            self.affinity_column = str(self.affinity_column)

        if self.lysis_buffer is not None and not isinstance(self.lysis_buffer, str):
            self.lysis_buffer = str(self.lysis_buffer)

        if self.wash_buffer is not None and not isinstance(self.wash_buffer, str):
            self.wash_buffer = str(self.wash_buffer)

        if self.elution_buffer is not None and not isinstance(self.elution_buffer, str):
            self.elution_buffer = str(self.elution_buffer)

        if self.tag_removal is not None and not isinstance(self.tag_removal, Bool):
            self.tag_removal = Bool(self.tag_removal)

        if self.protease is not None and not isinstance(self.protease, str):
            self.protease = str(self.protease)

        if self.protease_ratio is not None and not isinstance(self.protease_ratio, str):
            self.protease_ratio = str(self.protease_ratio)

        if self.cleavage_time_h is not None and not isinstance(self.cleavage_time_h, QuantityValue):
            self.cleavage_time_h = QuantityValue(**as_dict(self.cleavage_time_h))

        if self.cleavage_temperature_c is not None and not isinstance(self.cleavage_temperature_c, QuantityValue):
            self.cleavage_temperature_c = QuantityValue(**as_dict(self.cleavage_temperature_c))

        if self.second_affinity_reverse is not None and not isinstance(self.second_affinity_reverse, str):
            self.second_affinity_reverse = str(self.second_affinity_reverse)

        if self.iex_column is not None and not isinstance(self.iex_column, str):
            self.iex_column = str(self.iex_column)

        if self.hic_column is not None and not isinstance(self.hic_column, str):
            self.hic_column = str(self.hic_column)

        if self.sec_column is not None and not isinstance(self.sec_column, str):
            self.sec_column = str(self.sec_column)

        if self.sec_buffer is not None and not isinstance(self.sec_buffer, str):
            self.sec_buffer = str(self.sec_buffer)

        if self.concentration_method is not None and not isinstance(self.concentration_method, str):
            self.concentration_method = str(self.concentration_method)

        if self.final_buffer is not None and not isinstance(self.final_buffer, str):
            self.final_buffer = str(self.final_buffer)

        if self.final_concentration_mg_per_ml is not None and not isinstance(self.final_concentration_mg_per_ml, QuantityValue):
            self.final_concentration_mg_per_ml = QuantityValue(**as_dict(self.final_concentration_mg_per_ml))

        if self.yield_mg is not None and not isinstance(self.yield_mg, QuantityValue):
            self.yield_mg = QuantityValue(**as_dict(self.yield_mg))

        if self.purity_by_sds_page_percent is not None and not isinstance(self.purity_by_sds_page_percent, QuantityValue):
            self.purity_by_sds_page_percent = QuantityValue(**as_dict(self.purity_by_sds_page_percent))

        if self.aggregation_assessment is not None and not isinstance(self.aggregation_assessment, str):
            self.aggregation_assessment = str(self.aggregation_assessment)

        if self.aliquoting is not None and not isinstance(self.aliquoting, str):
            self.aliquoting = str(self.aliquoting)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Instrument(NamedThing):
    """
    An instrument used to collect data
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["Instrument"]
    class_class_curie: ClassVar[str] = "aimsleaf:Instrument"
    class_name: ClassVar[str] = "Instrument"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.Instrument

    id: Union[str, InstrumentId] = None
    instrument_code: str = None
    instrument_category: Optional[Union[str, "InstrumentCategoryEnum"]] = None
    facility_name: Optional[Union[str, "FacilityEnum"]] = None
    facility_ror: Optional[Union[str, URIorCURIE]] = None
    beamline_id: Optional[str] = None
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    installation_date: Optional[Union[str, XSDDate]] = None
    current_status: Optional[Union[str, "InstrumentStatusEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InstrumentId):
            self.id = InstrumentId(self.id)

        if self._is_empty(self.instrument_code):
            self.MissingRequiredField("instrument_code")
        if not isinstance(self.instrument_code, str):
            self.instrument_code = str(self.instrument_code)

        if self.instrument_category is not None and not isinstance(self.instrument_category, InstrumentCategoryEnum):
            self.instrument_category = InstrumentCategoryEnum(self.instrument_category)

        if self.facility_name is not None and not isinstance(self.facility_name, FacilityEnum):
            self.facility_name = FacilityEnum(self.facility_name)

        if self.facility_ror is not None and not isinstance(self.facility_ror, URIorCURIE):
            self.facility_ror = URIorCURIE(self.facility_ror)

        if self.beamline_id is not None and not isinstance(self.beamline_id, str):
            self.beamline_id = str(self.beamline_id)

        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        if self.model is not None and not isinstance(self.model, str):
            self.model = str(self.model)

        if self.installation_date is not None and not isinstance(self.installation_date, XSDDate):
            self.installation_date = XSDDate(self.installation_date)

        if self.current_status is not None and not isinstance(self.current_status, InstrumentStatusEnum):
            self.current_status = InstrumentStatusEnum(self.current_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CryoEMInstrument(Instrument):
    """
    Cryo-EM microscope specifications
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["CryoEMInstrument"]
    class_class_curie: ClassVar[str] = "aimsleaf:CryoEMInstrument"
    class_name: ClassVar[str] = "CryoEMInstrument"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.CryoEMInstrument

    id: Union[str, CryoEMInstrumentId] = None
    instrument_code: str = None
    accelerating_voltage: Optional[Union[dict, "QuantityValue"]] = None
    cs_corrector: Optional[Union[bool, Bool]] = None
    phase_plate: Optional[Union[bool, Bool]] = None
    detector_technology: Optional[Union[str, "DetectorTechnologyEnum"]] = None
    detector_manufacturer: Optional[str] = None
    detector_model: Optional[str] = None
    detector_mode: Optional[Union[str, "DetectorModeEnum"]] = None
    detector_position: Optional[str] = None
    detector_dimensions: Optional[str] = None
    pixel_size_physical_um: Optional[Union[dict, "QuantityValue"]] = None
    autoloader_capacity: Optional[Union[dict, "QuantityValue"]] = None
    cs: Optional[Union[dict, "QuantityValue"]] = None
    c2_aperture: Optional[Union[dict, "QuantityValue"]] = None
    objective_aperture: Optional[Union[dict, "QuantityValue"]] = None
    phase_plate_type: Optional[str] = None
    energy_filter_present: Optional[Union[bool, Bool]] = None
    energy_filter_make: Optional[str] = None
    energy_filter_model: Optional[str] = None
    energy_filter_slit_width: Optional[Union[dict, "QuantityValue"]] = None
    pixel_size_physical: Optional[Union[dict, "QuantityValue"]] = None
    microscope_software: Optional[str] = None
    microscope_software_version: Optional[str] = None
    spotsize: Optional[Union[dict, "QuantityValue"]] = None
    gunlens: Optional[Union[dict, "QuantityValue"]] = None
    imaging_mode: Optional[Union[str, "ImagingModeEnum"]] = None
    tem_beam_diameter: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CryoEMInstrumentId):
            self.id = CryoEMInstrumentId(self.id)

        if self.accelerating_voltage is not None and not isinstance(self.accelerating_voltage, QuantityValue):
            self.accelerating_voltage = QuantityValue(**as_dict(self.accelerating_voltage))

        if self.cs_corrector is not None and not isinstance(self.cs_corrector, Bool):
            self.cs_corrector = Bool(self.cs_corrector)

        if self.phase_plate is not None and not isinstance(self.phase_plate, Bool):
            self.phase_plate = Bool(self.phase_plate)

        if self.detector_technology is not None and not isinstance(self.detector_technology, DetectorTechnologyEnum):
            self.detector_technology = DetectorTechnologyEnum(self.detector_technology)

        if self.detector_manufacturer is not None and not isinstance(self.detector_manufacturer, str):
            self.detector_manufacturer = str(self.detector_manufacturer)

        if self.detector_model is not None and not isinstance(self.detector_model, str):
            self.detector_model = str(self.detector_model)

        if self.detector_mode is not None and not isinstance(self.detector_mode, DetectorModeEnum):
            self.detector_mode = DetectorModeEnum(self.detector_mode)

        if self.detector_position is not None and not isinstance(self.detector_position, str):
            self.detector_position = str(self.detector_position)

        if self.detector_dimensions is not None and not isinstance(self.detector_dimensions, str):
            self.detector_dimensions = str(self.detector_dimensions)

        if self.pixel_size_physical_um is not None and not isinstance(self.pixel_size_physical_um, QuantityValue):
            self.pixel_size_physical_um = QuantityValue(**as_dict(self.pixel_size_physical_um))

        if self.autoloader_capacity is not None and not isinstance(self.autoloader_capacity, QuantityValue):
            self.autoloader_capacity = QuantityValue(**as_dict(self.autoloader_capacity))

        if self.cs is not None and not isinstance(self.cs, QuantityValue):
            self.cs = QuantityValue(**as_dict(self.cs))

        if self.c2_aperture is not None and not isinstance(self.c2_aperture, QuantityValue):
            self.c2_aperture = QuantityValue(**as_dict(self.c2_aperture))

        if self.objective_aperture is not None and not isinstance(self.objective_aperture, QuantityValue):
            self.objective_aperture = QuantityValue(**as_dict(self.objective_aperture))

        if self.phase_plate_type is not None and not isinstance(self.phase_plate_type, str):
            self.phase_plate_type = str(self.phase_plate_type)

        if self.energy_filter_present is not None and not isinstance(self.energy_filter_present, Bool):
            self.energy_filter_present = Bool(self.energy_filter_present)

        if self.energy_filter_make is not None and not isinstance(self.energy_filter_make, str):
            self.energy_filter_make = str(self.energy_filter_make)

        if self.energy_filter_model is not None and not isinstance(self.energy_filter_model, str):
            self.energy_filter_model = str(self.energy_filter_model)

        if self.energy_filter_slit_width is not None and not isinstance(self.energy_filter_slit_width, QuantityValue):
            self.energy_filter_slit_width = QuantityValue(**as_dict(self.energy_filter_slit_width))

        if self.pixel_size_physical is not None and not isinstance(self.pixel_size_physical, QuantityValue):
            self.pixel_size_physical = QuantityValue(**as_dict(self.pixel_size_physical))

        if self.microscope_software is not None and not isinstance(self.microscope_software, str):
            self.microscope_software = str(self.microscope_software)

        if self.microscope_software_version is not None and not isinstance(self.microscope_software_version, str):
            self.microscope_software_version = str(self.microscope_software_version)

        if self.spotsize is not None and not isinstance(self.spotsize, QuantityValue):
            self.spotsize = QuantityValue(**as_dict(self.spotsize))

        if self.gunlens is not None and not isinstance(self.gunlens, QuantityValue):
            self.gunlens = QuantityValue(**as_dict(self.gunlens))

        if self.imaging_mode is not None and not isinstance(self.imaging_mode, ImagingModeEnum):
            self.imaging_mode = ImagingModeEnum(self.imaging_mode)

        if self.tem_beam_diameter is not None and not isinstance(self.tem_beam_diameter, QuantityValue):
            self.tem_beam_diameter = QuantityValue(**as_dict(self.tem_beam_diameter))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class XRayInstrument(Instrument):
    """
    X-ray diffractometer or synchrotron beamline specifications
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["XRayInstrument"]
    class_class_curie: ClassVar[str] = "aimsleaf:XRayInstrument"
    class_name: ClassVar[str] = "XRayInstrument"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.XRayInstrument

    id: Union[str, XRayInstrumentId] = None
    instrument_code: str = None
    source_type: Optional[Union[str, "XRaySourceTypeEnum"]] = None
    detector_technology: Optional[Union[str, "DetectorTechnologyEnum"]] = None
    detector_manufacturer: Optional[str] = None
    detector_model: Optional[str] = None
    energy_min: Optional[Union[dict, "QuantityValue"]] = None
    energy_max: Optional[Union[dict, "QuantityValue"]] = None
    beam_size_min: Optional[Union[dict, "QuantityValue"]] = None
    beam_size_max: Optional[Union[dict, "QuantityValue"]] = None
    flux_density: Optional[Union[dict, "QuantityValue"]] = None
    monochromator_type: Optional[str] = None
    goniometer_type: Optional[str] = None
    crystal_cooling_capability: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, XRayInstrumentId):
            self.id = XRayInstrumentId(self.id)

        if self.source_type is not None and not isinstance(self.source_type, XRaySourceTypeEnum):
            self.source_type = XRaySourceTypeEnum(self.source_type)

        if self.detector_technology is not None and not isinstance(self.detector_technology, DetectorTechnologyEnum):
            self.detector_technology = DetectorTechnologyEnum(self.detector_technology)

        if self.detector_manufacturer is not None and not isinstance(self.detector_manufacturer, str):
            self.detector_manufacturer = str(self.detector_manufacturer)

        if self.detector_model is not None and not isinstance(self.detector_model, str):
            self.detector_model = str(self.detector_model)

        if self.energy_min is not None and not isinstance(self.energy_min, QuantityValue):
            self.energy_min = QuantityValue(**as_dict(self.energy_min))

        if self.energy_max is not None and not isinstance(self.energy_max, QuantityValue):
            self.energy_max = QuantityValue(**as_dict(self.energy_max))

        if self.beam_size_min is not None and not isinstance(self.beam_size_min, QuantityValue):
            self.beam_size_min = QuantityValue(**as_dict(self.beam_size_min))

        if self.beam_size_max is not None and not isinstance(self.beam_size_max, QuantityValue):
            self.beam_size_max = QuantityValue(**as_dict(self.beam_size_max))

        if self.flux_density is not None and not isinstance(self.flux_density, QuantityValue):
            self.flux_density = QuantityValue(**as_dict(self.flux_density))

        if self.monochromator_type is not None and not isinstance(self.monochromator_type, str):
            self.monochromator_type = str(self.monochromator_type)

        if self.goniometer_type is not None and not isinstance(self.goniometer_type, str):
            self.goniometer_type = str(self.goniometer_type)

        if self.crystal_cooling_capability is not None and not isinstance(self.crystal_cooling_capability, Bool):
            self.crystal_cooling_capability = Bool(self.crystal_cooling_capability)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentRun(NamedThing):
    """
    An experimental data collection session
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["ExperimentRun"]
    class_class_curie: ClassVar[str] = "aimsleaf:ExperimentRun"
    class_name: ClassVar[str] = "ExperimentRun"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.ExperimentRun

    id: Union[str, ExperimentRunId] = None
    experiment_code: str = None
    technique: Union[str, "TechniqueEnum"] = None
    experiment_date: Optional[Union[str, XSDDate]] = None
    operator_id: Optional[str] = None
    experimental_conditions: Optional[Union[dict, "ExperimentalConditions"]] = None
    data_collection_strategy: Optional[Union[dict, "DataCollectionStrategy"]] = None
    raw_data_location: Optional[str] = None
    processing_status: Optional[Union[str, "ProcessingStatusEnum"]] = None
    magnification: Optional[Union[dict, "QuantityValue"]] = None
    calibrated_pixel_size: Optional[Union[dict, "QuantityValue"]] = None
    camera_binning: Optional[Union[dict, "QuantityValue"]] = None
    exposure_time_per_frame: Optional[Union[dict, "QuantityValue"]] = None
    frames_per_movie: Optional[Union[dict, "QuantityValue"]] = None
    total_exposure_time: Optional[Union[dict, "QuantityValue"]] = None
    total_dose: Optional[Union[dict, "QuantityValue"]] = None
    dose_rate: Optional[Union[dict, "QuantityValue"]] = None
    defocus_target: Optional[Union[dict, "QuantityValue"]] = None
    defocus_range_min: Optional[Union[dict, "QuantityValue"]] = None
    defocus_range_max: Optional[Union[dict, "QuantityValue"]] = None
    defocus_range_increment: Optional[Union[dict, "QuantityValue"]] = None
    astigmatism_target: Optional[Union[dict, "QuantityValue"]] = None
    coma: Optional[Union[dict, "QuantityValue"]] = None
    stage_tilt: Optional[Union[dict, "QuantityValue"]] = None
    autoloader_slot: Optional[str] = None
    shots_per_hole: Optional[Union[dict, "QuantityValue"]] = None
    holes_per_group: Optional[Union[dict, "QuantityValue"]] = None
    acquisition_software: Optional[str] = None
    acquisition_software_version: Optional[str] = None
    wavelength: Optional[Union[dict, "QuantityValue"]] = None
    oscillation_angle: Optional[Union[dict, "QuantityValue"]] = None
    start_angle: Optional[Union[dict, "QuantityValue"]] = None
    number_of_images: Optional[Union[dict, "QuantityValue"]] = None
    beam_center_x: Optional[Union[dict, "QuantityValue"]] = None
    beam_center_y: Optional[Union[dict, "QuantityValue"]] = None
    detector_distance: Optional[Union[dict, "QuantityValue"]] = None
    pixel_size_x: Optional[Union[dict, "QuantityValue"]] = None
    pixel_size_y: Optional[Union[dict, "QuantityValue"]] = None
    total_rotation: Optional[Union[dict, "QuantityValue"]] = None
    beamline: Optional[str] = None
    transmission: Optional[Union[dict, "QuantityValue"]] = None
    flux: Optional[Union[dict, "QuantityValue"]] = None
    flux_end: Optional[Union[dict, "QuantityValue"]] = None
    slit_gap_horizontal: Optional[Union[dict, "QuantityValue"]] = None
    slit_gap_vertical: Optional[Union[dict, "QuantityValue"]] = None
    undulator_gap: Optional[Union[dict, "QuantityValue"]] = None
    synchrotron_mode: Optional[str] = None
    exposure_time: Optional[Union[dict, "QuantityValue"]] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    resolution: Optional[Union[dict, "QuantityValue"]] = None
    resolution_at_corner: Optional[Union[dict, "QuantityValue"]] = None
    ispyb_data_collection_id: Optional[Union[dict, "QuantityValue"]] = None
    ispyb_session_id: Optional[Union[dict, "QuantityValue"]] = None
    beam_size_x: Optional[Union[dict, "QuantityValue"]] = None
    beam_size_y: Optional[Union[dict, "QuantityValue"]] = None
    dwell_time: Optional[Union[dict, "QuantityValue"]] = None
    energy: Optional[Union[dict, "QuantityValue"]] = None
    beamline_parameters: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExperimentRunId):
            self.id = ExperimentRunId(self.id)

        if self._is_empty(self.experiment_code):
            self.MissingRequiredField("experiment_code")
        if not isinstance(self.experiment_code, str):
            self.experiment_code = str(self.experiment_code)

        if self._is_empty(self.technique):
            self.MissingRequiredField("technique")
        if not isinstance(self.technique, TechniqueEnum):
            self.technique = TechniqueEnum(self.technique)

        if self.experiment_date is not None and not isinstance(self.experiment_date, XSDDate):
            self.experiment_date = XSDDate(self.experiment_date)

        if self.operator_id is not None and not isinstance(self.operator_id, str):
            self.operator_id = str(self.operator_id)

        if self.experimental_conditions is not None and not isinstance(self.experimental_conditions, ExperimentalConditions):
            self.experimental_conditions = ExperimentalConditions(**as_dict(self.experimental_conditions))

        if self.data_collection_strategy is not None and not isinstance(self.data_collection_strategy, DataCollectionStrategy):
            self.data_collection_strategy = DataCollectionStrategy(**as_dict(self.data_collection_strategy))

        if self.raw_data_location is not None and not isinstance(self.raw_data_location, str):
            self.raw_data_location = str(self.raw_data_location)

        if self.processing_status is not None and not isinstance(self.processing_status, ProcessingStatusEnum):
            self.processing_status = ProcessingStatusEnum(self.processing_status)

        if self.magnification is not None and not isinstance(self.magnification, QuantityValue):
            self.magnification = QuantityValue(**as_dict(self.magnification))

        if self.calibrated_pixel_size is not None and not isinstance(self.calibrated_pixel_size, QuantityValue):
            self.calibrated_pixel_size = QuantityValue(**as_dict(self.calibrated_pixel_size))

        if self.camera_binning is not None and not isinstance(self.camera_binning, QuantityValue):
            self.camera_binning = QuantityValue(**as_dict(self.camera_binning))

        if self.exposure_time_per_frame is not None and not isinstance(self.exposure_time_per_frame, QuantityValue):
            self.exposure_time_per_frame = QuantityValue(**as_dict(self.exposure_time_per_frame))

        if self.frames_per_movie is not None and not isinstance(self.frames_per_movie, QuantityValue):
            self.frames_per_movie = QuantityValue(**as_dict(self.frames_per_movie))

        if self.total_exposure_time is not None and not isinstance(self.total_exposure_time, QuantityValue):
            self.total_exposure_time = QuantityValue(**as_dict(self.total_exposure_time))

        if self.total_dose is not None and not isinstance(self.total_dose, QuantityValue):
            self.total_dose = QuantityValue(**as_dict(self.total_dose))

        if self.dose_rate is not None and not isinstance(self.dose_rate, QuantityValue):
            self.dose_rate = QuantityValue(**as_dict(self.dose_rate))

        if self.defocus_target is not None and not isinstance(self.defocus_target, QuantityValue):
            self.defocus_target = QuantityValue(**as_dict(self.defocus_target))

        if self.defocus_range_min is not None and not isinstance(self.defocus_range_min, QuantityValue):
            self.defocus_range_min = QuantityValue(**as_dict(self.defocus_range_min))

        if self.defocus_range_max is not None and not isinstance(self.defocus_range_max, QuantityValue):
            self.defocus_range_max = QuantityValue(**as_dict(self.defocus_range_max))

        if self.defocus_range_increment is not None and not isinstance(self.defocus_range_increment, QuantityValue):
            self.defocus_range_increment = QuantityValue(**as_dict(self.defocus_range_increment))

        if self.astigmatism_target is not None and not isinstance(self.astigmatism_target, QuantityValue):
            self.astigmatism_target = QuantityValue(**as_dict(self.astigmatism_target))

        if self.coma is not None and not isinstance(self.coma, QuantityValue):
            self.coma = QuantityValue(**as_dict(self.coma))

        if self.stage_tilt is not None and not isinstance(self.stage_tilt, QuantityValue):
            self.stage_tilt = QuantityValue(**as_dict(self.stage_tilt))

        if self.autoloader_slot is not None and not isinstance(self.autoloader_slot, str):
            self.autoloader_slot = str(self.autoloader_slot)

        if self.shots_per_hole is not None and not isinstance(self.shots_per_hole, QuantityValue):
            self.shots_per_hole = QuantityValue(**as_dict(self.shots_per_hole))

        if self.holes_per_group is not None and not isinstance(self.holes_per_group, QuantityValue):
            self.holes_per_group = QuantityValue(**as_dict(self.holes_per_group))

        if self.acquisition_software is not None and not isinstance(self.acquisition_software, str):
            self.acquisition_software = str(self.acquisition_software)

        if self.acquisition_software_version is not None and not isinstance(self.acquisition_software_version, str):
            self.acquisition_software_version = str(self.acquisition_software_version)

        if self.wavelength is not None and not isinstance(self.wavelength, QuantityValue):
            self.wavelength = QuantityValue(**as_dict(self.wavelength))

        if self.oscillation_angle is not None and not isinstance(self.oscillation_angle, QuantityValue):
            self.oscillation_angle = QuantityValue(**as_dict(self.oscillation_angle))

        if self.start_angle is not None and not isinstance(self.start_angle, QuantityValue):
            self.start_angle = QuantityValue(**as_dict(self.start_angle))

        if self.number_of_images is not None and not isinstance(self.number_of_images, QuantityValue):
            self.number_of_images = QuantityValue(**as_dict(self.number_of_images))

        if self.beam_center_x is not None and not isinstance(self.beam_center_x, QuantityValue):
            self.beam_center_x = QuantityValue(**as_dict(self.beam_center_x))

        if self.beam_center_y is not None and not isinstance(self.beam_center_y, QuantityValue):
            self.beam_center_y = QuantityValue(**as_dict(self.beam_center_y))

        if self.detector_distance is not None and not isinstance(self.detector_distance, QuantityValue):
            self.detector_distance = QuantityValue(**as_dict(self.detector_distance))

        if self.pixel_size_x is not None and not isinstance(self.pixel_size_x, QuantityValue):
            self.pixel_size_x = QuantityValue(**as_dict(self.pixel_size_x))

        if self.pixel_size_y is not None and not isinstance(self.pixel_size_y, QuantityValue):
            self.pixel_size_y = QuantityValue(**as_dict(self.pixel_size_y))

        if self.total_rotation is not None and not isinstance(self.total_rotation, QuantityValue):
            self.total_rotation = QuantityValue(**as_dict(self.total_rotation))

        if self.beamline is not None and not isinstance(self.beamline, str):
            self.beamline = str(self.beamline)

        if self.transmission is not None and not isinstance(self.transmission, QuantityValue):
            self.transmission = QuantityValue(**as_dict(self.transmission))

        if self.flux is not None and not isinstance(self.flux, QuantityValue):
            self.flux = QuantityValue(**as_dict(self.flux))

        if self.flux_end is not None and not isinstance(self.flux_end, QuantityValue):
            self.flux_end = QuantityValue(**as_dict(self.flux_end))

        if self.slit_gap_horizontal is not None and not isinstance(self.slit_gap_horizontal, QuantityValue):
            self.slit_gap_horizontal = QuantityValue(**as_dict(self.slit_gap_horizontal))

        if self.slit_gap_vertical is not None and not isinstance(self.slit_gap_vertical, QuantityValue):
            self.slit_gap_vertical = QuantityValue(**as_dict(self.slit_gap_vertical))

        if self.undulator_gap is not None and not isinstance(self.undulator_gap, QuantityValue):
            self.undulator_gap = QuantityValue(**as_dict(self.undulator_gap))

        if self.synchrotron_mode is not None and not isinstance(self.synchrotron_mode, str):
            self.synchrotron_mode = str(self.synchrotron_mode)

        if self.exposure_time is not None and not isinstance(self.exposure_time, QuantityValue):
            self.exposure_time = QuantityValue(**as_dict(self.exposure_time))

        if self.start_time is not None and not isinstance(self.start_time, str):
            self.start_time = str(self.start_time)

        if self.end_time is not None and not isinstance(self.end_time, str):
            self.end_time = str(self.end_time)

        if self.resolution is not None and not isinstance(self.resolution, QuantityValue):
            self.resolution = QuantityValue(**as_dict(self.resolution))

        if self.resolution_at_corner is not None and not isinstance(self.resolution_at_corner, QuantityValue):
            self.resolution_at_corner = QuantityValue(**as_dict(self.resolution_at_corner))

        if self.ispyb_data_collection_id is not None and not isinstance(self.ispyb_data_collection_id, QuantityValue):
            self.ispyb_data_collection_id = QuantityValue(**as_dict(self.ispyb_data_collection_id))

        if self.ispyb_session_id is not None and not isinstance(self.ispyb_session_id, QuantityValue):
            self.ispyb_session_id = QuantityValue(**as_dict(self.ispyb_session_id))

        if self.beam_size_x is not None and not isinstance(self.beam_size_x, QuantityValue):
            self.beam_size_x = QuantityValue(**as_dict(self.beam_size_x))

        if self.beam_size_y is not None and not isinstance(self.beam_size_y, QuantityValue):
            self.beam_size_y = QuantityValue(**as_dict(self.beam_size_y))

        if self.dwell_time is not None and not isinstance(self.dwell_time, QuantityValue):
            self.dwell_time = QuantityValue(**as_dict(self.dwell_time))

        if self.energy is not None and not isinstance(self.energy, QuantityValue):
            self.energy = QuantityValue(**as_dict(self.energy))

        if self.beamline_parameters is not None and not isinstance(self.beamline_parameters, QuantityValue):
            self.beamline_parameters = QuantityValue(**as_dict(self.beamline_parameters))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WorkflowRun(NamedThing):
    """
    A computational processing workflow execution
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["WorkflowRun"]
    class_class_curie: ClassVar[str] = "aimsleaf:WorkflowRun"
    class_name: ClassVar[str] = "WorkflowRun"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.WorkflowRun

    id: Union[str, WorkflowRunId] = None
    workflow_code: str = None
    workflow_type: Union[str, "WorkflowTypeEnum"] = None
    software_name: str = None
    processing_level: Optional[Union[dict, "QuantityValue"]] = None
    software_version: Optional[str] = None
    additional_software: Optional[str] = None
    processing_parameters: Optional[str] = None
    parameters_file_path: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkflowRunId):
            self.id = WorkflowRunId(self.id)

        if self._is_empty(self.workflow_code):
            self.MissingRequiredField("workflow_code")
        if not isinstance(self.workflow_code, str):
            self.workflow_code = str(self.workflow_code)

        if self._is_empty(self.workflow_type):
            self.MissingRequiredField("workflow_type")
        if not isinstance(self.workflow_type, WorkflowTypeEnum):
            self.workflow_type = WorkflowTypeEnum(self.workflow_type)

        if self._is_empty(self.software_name):
            self.MissingRequiredField("software_name")
        if not isinstance(self.software_name, str):
            self.software_name = str(self.software_name)

        if self.processing_level is not None and not isinstance(self.processing_level, QuantityValue):
            self.processing_level = QuantityValue(**as_dict(self.processing_level))

        if self.software_version is not None and not isinstance(self.software_version, str):
            self.software_version = str(self.software_version)

        if self.additional_software is not None and not isinstance(self.additional_software, str):
            self.additional_software = str(self.additional_software)

        if self.processing_parameters is not None and not isinstance(self.processing_parameters, str):
            self.processing_parameters = str(self.processing_parameters)

        if self.parameters_file_path is not None and not isinstance(self.parameters_file_path, str):
            self.parameters_file_path = str(self.parameters_file_path)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataFile(NamedThing):
    """
    A data file generated or used in the study
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["DataFile"]
    class_class_curie: ClassVar[str] = "aimsleaf:DataFile"
    class_name: ClassVar[str] = "DataFile"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.DataFile

    id: Union[str, DataFileId] = None
    file_name: str = None
    file_format: Union[str, "FileFormatEnum"] = None
    file_path: Optional[str] = None
    file_size_bytes: Optional[Union[dict, "QuantityValue"]] = None
    checksum: Optional[str] = None
    creation_date: Optional[Union[str, XSDDate]] = None
    data_type: Optional[Union[str, "DataTypeEnum"]] = None
    storage_uri: Optional[str] = None
    related_entity: Optional[str] = None
    file_role: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataFileId):
            self.id = DataFileId(self.id)

        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self._is_empty(self.file_format):
            self.MissingRequiredField("file_format")
        if not isinstance(self.file_format, FileFormatEnum):
            self.file_format = FileFormatEnum(self.file_format)

        if self.file_path is not None and not isinstance(self.file_path, str):
            self.file_path = str(self.file_path)

        if self.file_size_bytes is not None and not isinstance(self.file_size_bytes, QuantityValue):
            self.file_size_bytes = QuantityValue(**as_dict(self.file_size_bytes))

        if self.checksum is not None and not isinstance(self.checksum, str):
            self.checksum = str(self.checksum)

        if self.creation_date is not None and not isinstance(self.creation_date, XSDDate):
            self.creation_date = XSDDate(self.creation_date)

        if self.data_type is not None and not isinstance(self.data_type, DataTypeEnum):
            self.data_type = DataTypeEnum(self.data_type)

        if self.storage_uri is not None and not isinstance(self.storage_uri, str):
            self.storage_uri = str(self.storage_uri)

        if self.related_entity is not None and not isinstance(self.related_entity, str):
            self.related_entity = str(self.related_entity)

        if self.file_role is not None and not isinstance(self.file_role, str):
            self.file_role = str(self.file_role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Image(NamedThing):
    """
    An image file from structural biology experiments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["Image"]
    class_class_curie: ClassVar[str] = "aimsleaf:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.Image

    id: Union[str, ImageId] = None
    file_name: str = None
    acquisition_date: Optional[Union[str, XSDDate]] = None
    pixel_size: Optional[Union[dict, "QuantityValue"]] = None
    dimensions_x: Optional[Union[dict, "QuantityValue"]] = None
    dimensions_y: Optional[Union[dict, "QuantityValue"]] = None
    exposure_time: Optional[Union[dict, "QuantityValue"]] = None
    dose: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImageId):
            self.id = ImageId(self.id)

        if self._is_empty(self.file_name):
            self.MissingRequiredField("file_name")
        if not isinstance(self.file_name, str):
            self.file_name = str(self.file_name)

        if self.acquisition_date is not None and not isinstance(self.acquisition_date, XSDDate):
            self.acquisition_date = XSDDate(self.acquisition_date)

        if self.pixel_size is not None and not isinstance(self.pixel_size, QuantityValue):
            self.pixel_size = QuantityValue(**as_dict(self.pixel_size))

        if self.dimensions_x is not None and not isinstance(self.dimensions_x, QuantityValue):
            self.dimensions_x = QuantityValue(**as_dict(self.dimensions_x))

        if self.dimensions_y is not None and not isinstance(self.dimensions_y, QuantityValue):
            self.dimensions_y = QuantityValue(**as_dict(self.dimensions_y))

        if self.exposure_time is not None and not isinstance(self.exposure_time, QuantityValue):
            self.exposure_time = QuantityValue(**as_dict(self.exposure_time))

        if self.dose is not None and not isinstance(self.dose, QuantityValue):
            self.dose = QuantityValue(**as_dict(self.dose))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Image2D(Image):
    """
    A 2D image (micrograph, diffraction pattern)
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["Image2D"]
    class_class_curie: ClassVar[str] = "aimsleaf:Image2D"
    class_name: ClassVar[str] = "Image2D"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.Image2D

    id: Union[str, Image2DId] = None
    file_name: str = None
    defocus: Optional[Union[dict, "QuantityValue"]] = None
    astigmatism: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Image2DId):
            self.id = Image2DId(self.id)

        if self.defocus is not None and not isinstance(self.defocus, QuantityValue):
            self.defocus = QuantityValue(**as_dict(self.defocus))

        if self.astigmatism is not None and not isinstance(self.astigmatism, QuantityValue):
            self.astigmatism = QuantityValue(**as_dict(self.astigmatism))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Image3D(Image):
    """
    A 3D volume or tomogram
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["Image3D"]
    class_class_curie: ClassVar[str] = "aimsleaf:Image3D"
    class_name: ClassVar[str] = "Image3D"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.Image3D

    id: Union[str, Image3DId] = None
    file_name: str = None
    dimensions_z: Optional[Union[dict, "QuantityValue"]] = None
    voxel_size: Optional[Union[dict, "QuantityValue"]] = None
    reconstruction_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, Image3DId):
            self.id = Image3DId(self.id)

        if self.dimensions_z is not None and not isinstance(self.dimensions_z, QuantityValue):
            self.dimensions_z = QuantityValue(**as_dict(self.dimensions_z))

        if self.voxel_size is not None and not isinstance(self.voxel_size, QuantityValue):
            self.voxel_size = QuantityValue(**as_dict(self.voxel_size))

        if self.reconstruction_method is not None and not isinstance(self.reconstruction_method, str):
            self.reconstruction_method = str(self.reconstruction_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Movie(Image2D):
    """
    Raw cryo-EM movie with frame-by-frame metadata for motion correction
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["Movie"]
    class_class_curie: ClassVar[str] = "aimsleaf:Movie"
    class_name: ClassVar[str] = "Movie"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.Movie

    id: Union[str, MovieId] = None
    file_name: str = None
    frames: Optional[Union[dict, "QuantityValue"]] = None
    super_resolution: Optional[Union[bool, Bool]] = None
    pixel_size_unbinned: Optional[Union[dict, "QuantityValue"]] = None
    timestamp: Optional[str] = None
    stage_position_x: Optional[Union[dict, "QuantityValue"]] = None
    stage_position_y: Optional[Union[dict, "QuantityValue"]] = None
    stage_position_z: Optional[Union[dict, "QuantityValue"]] = None
    nominal_defocus: Optional[Union[dict, "QuantityValue"]] = None
    dose_per_frame: Optional[Union[dict, "QuantityValue"]] = None
    beam_shift_x: Optional[Union[dict, "QuantityValue"]] = None
    beam_shift_y: Optional[Union[dict, "QuantityValue"]] = None
    ice_thickness_estimate: Optional[Union[dict, "QuantityValue"]] = None
    grid_square_id: Optional[str] = None
    hole_id: Optional[str] = None
    acquisition_group: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MovieId):
            self.id = MovieId(self.id)

        if self.frames is not None and not isinstance(self.frames, QuantityValue):
            self.frames = QuantityValue(**as_dict(self.frames))

        if self.super_resolution is not None and not isinstance(self.super_resolution, Bool):
            self.super_resolution = Bool(self.super_resolution)

        if self.pixel_size_unbinned is not None and not isinstance(self.pixel_size_unbinned, QuantityValue):
            self.pixel_size_unbinned = QuantityValue(**as_dict(self.pixel_size_unbinned))

        if self.timestamp is not None and not isinstance(self.timestamp, str):
            self.timestamp = str(self.timestamp)

        if self.stage_position_x is not None and not isinstance(self.stage_position_x, QuantityValue):
            self.stage_position_x = QuantityValue(**as_dict(self.stage_position_x))

        if self.stage_position_y is not None and not isinstance(self.stage_position_y, QuantityValue):
            self.stage_position_y = QuantityValue(**as_dict(self.stage_position_y))

        if self.stage_position_z is not None and not isinstance(self.stage_position_z, QuantityValue):
            self.stage_position_z = QuantityValue(**as_dict(self.stage_position_z))

        if self.nominal_defocus is not None and not isinstance(self.nominal_defocus, QuantityValue):
            self.nominal_defocus = QuantityValue(**as_dict(self.nominal_defocus))

        if self.dose_per_frame is not None and not isinstance(self.dose_per_frame, QuantityValue):
            self.dose_per_frame = QuantityValue(**as_dict(self.dose_per_frame))

        if self.beam_shift_x is not None and not isinstance(self.beam_shift_x, QuantityValue):
            self.beam_shift_x = QuantityValue(**as_dict(self.beam_shift_x))

        if self.beam_shift_y is not None and not isinstance(self.beam_shift_y, QuantityValue):
            self.beam_shift_y = QuantityValue(**as_dict(self.beam_shift_y))

        if self.ice_thickness_estimate is not None and not isinstance(self.ice_thickness_estimate, QuantityValue):
            self.ice_thickness_estimate = QuantityValue(**as_dict(self.ice_thickness_estimate))

        if self.grid_square_id is not None and not isinstance(self.grid_square_id, str):
            self.grid_square_id = str(self.grid_square_id)

        if self.hole_id is not None and not isinstance(self.hole_id, str):
            self.hole_id = str(self.hole_id)

        if self.acquisition_group is not None and not isinstance(self.acquisition_group, str):
            self.acquisition_group = str(self.acquisition_group)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FTIRImage(DataFile):
    """
    Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular composition through vibrational
    spectroscopy
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["FTIRImage"]
    class_class_curie: ClassVar[str] = "aimsleaf:FTIRImage"
    class_name: ClassVar[str] = "FTIRImage"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.FTIRImage

    id: Union[str, FTIRImageId] = None
    file_name: str = None
    file_format: Union[str, "FileFormatEnum"] = None
    pixel_size: Optional[Union[dict, "QuantityValue"]] = None
    dimensions_x: Optional[Union[dict, "QuantityValue"]] = None
    dimensions_y: Optional[Union[dict, "QuantityValue"]] = None
    wavenumber_min: Optional[Union[dict, "QuantityValue"]] = None
    wavenumber_max: Optional[Union[dict, "QuantityValue"]] = None
    spectral_resolution: Optional[Union[dict, "QuantityValue"]] = None
    number_of_scans: Optional[Union[dict, "QuantityValue"]] = None
    apodization_function: Optional[str] = None
    molecular_signatures: Optional[Union[str, list[str]]] = empty_list()
    background_correction: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FTIRImageId):
            self.id = FTIRImageId(self.id)

        if self.pixel_size is not None and not isinstance(self.pixel_size, QuantityValue):
            self.pixel_size = QuantityValue(**as_dict(self.pixel_size))

        if self.dimensions_x is not None and not isinstance(self.dimensions_x, QuantityValue):
            self.dimensions_x = QuantityValue(**as_dict(self.dimensions_x))

        if self.dimensions_y is not None and not isinstance(self.dimensions_y, QuantityValue):
            self.dimensions_y = QuantityValue(**as_dict(self.dimensions_y))

        if self.wavenumber_min is not None and not isinstance(self.wavenumber_min, QuantityValue):
            self.wavenumber_min = QuantityValue(**as_dict(self.wavenumber_min))

        if self.wavenumber_max is not None and not isinstance(self.wavenumber_max, QuantityValue):
            self.wavenumber_max = QuantityValue(**as_dict(self.wavenumber_max))

        if self.spectral_resolution is not None and not isinstance(self.spectral_resolution, QuantityValue):
            self.spectral_resolution = QuantityValue(**as_dict(self.spectral_resolution))

        if self.number_of_scans is not None and not isinstance(self.number_of_scans, QuantityValue):
            self.number_of_scans = QuantityValue(**as_dict(self.number_of_scans))

        if self.apodization_function is not None and not isinstance(self.apodization_function, str):
            self.apodization_function = str(self.apodization_function)

        if not isinstance(self.molecular_signatures, list):
            self.molecular_signatures = [self.molecular_signatures] if self.molecular_signatures is not None else []
        self.molecular_signatures = [v if isinstance(v, str) else str(v) for v in self.molecular_signatures]

        if self.background_correction is not None and not isinstance(self.background_correction, str):
            self.background_correction = str(self.background_correction)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FluorescenceImage(Image2D):
    """
    Fluorescence microscopy image capturing specific molecular targets through fluorescent labeling
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["FluorescenceImage"]
    class_class_curie: ClassVar[str] = "aimsleaf:FluorescenceImage"
    class_name: ClassVar[str] = "FluorescenceImage"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.FluorescenceImage

    id: Union[str, FluorescenceImageId] = None
    file_name: str = None
    excitation_wavelength: Optional[Union[dict, "QuantityValue"]] = None
    emission_wavelength: Optional[Union[dict, "QuantityValue"]] = None
    excitation_filter: Optional[str] = None
    emission_filter: Optional[str] = None
    fluorophore: Optional[str] = None
    channel_name: Optional[str] = None
    laser_power: Optional[Union[dict, "QuantityValue"]] = None
    pinhole_size: Optional[Union[dict, "QuantityValue"]] = None
    quantum_yield: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FluorescenceImageId):
            self.id = FluorescenceImageId(self.id)

        if self.excitation_wavelength is not None and not isinstance(self.excitation_wavelength, QuantityValue):
            self.excitation_wavelength = QuantityValue(**as_dict(self.excitation_wavelength))

        if self.emission_wavelength is not None and not isinstance(self.emission_wavelength, QuantityValue):
            self.emission_wavelength = QuantityValue(**as_dict(self.emission_wavelength))

        if self.excitation_filter is not None and not isinstance(self.excitation_filter, str):
            self.excitation_filter = str(self.excitation_filter)

        if self.emission_filter is not None and not isinstance(self.emission_filter, str):
            self.emission_filter = str(self.emission_filter)

        if self.fluorophore is not None and not isinstance(self.fluorophore, str):
            self.fluorophore = str(self.fluorophore)

        if self.channel_name is not None and not isinstance(self.channel_name, str):
            self.channel_name = str(self.channel_name)

        if self.laser_power is not None and not isinstance(self.laser_power, QuantityValue):
            self.laser_power = QuantityValue(**as_dict(self.laser_power))

        if self.pinhole_size is not None and not isinstance(self.pinhole_size, QuantityValue):
            self.pinhole_size = QuantityValue(**as_dict(self.pinhole_size))

        if self.quantum_yield is not None and not isinstance(self.quantum_yield, QuantityValue):
            self.quantum_yield = QuantityValue(**as_dict(self.quantum_yield))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OpticalImage(Image2D):
    """
    Visible light optical microscopy or photography image
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["OpticalImage"]
    class_class_curie: ClassVar[str] = "aimsleaf:OpticalImage"
    class_name: ClassVar[str] = "OpticalImage"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.OpticalImage

    id: Union[str, OpticalImageId] = None
    file_name: str = None
    illumination_type: Optional[Union[str, "IlluminationTypeEnum"]] = None
    magnification: Optional[Union[dict, "QuantityValue"]] = None
    numerical_aperture: Optional[Union[dict, "QuantityValue"]] = None
    color_channels: Optional[Union[str, list[str]]] = empty_list()
    white_balance: Optional[str] = None
    contrast_method: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OpticalImageId):
            self.id = OpticalImageId(self.id)

        if self.illumination_type is not None and not isinstance(self.illumination_type, IlluminationTypeEnum):
            self.illumination_type = IlluminationTypeEnum(self.illumination_type)

        if self.magnification is not None and not isinstance(self.magnification, QuantityValue):
            self.magnification = QuantityValue(**as_dict(self.magnification))

        if self.numerical_aperture is not None and not isinstance(self.numerical_aperture, QuantityValue):
            self.numerical_aperture = QuantityValue(**as_dict(self.numerical_aperture))

        if not isinstance(self.color_channels, list):
            self.color_channels = [self.color_channels] if self.color_channels is not None else []
        self.color_channels = [v if isinstance(v, str) else str(v) for v in self.color_channels]

        if self.white_balance is not None and not isinstance(self.white_balance, str):
            self.white_balance = str(self.white_balance)

        if self.contrast_method is not None and not isinstance(self.contrast_method, str):
            self.contrast_method = str(self.contrast_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class XRFImage(DataFile):
    """
    X-ray fluorescence (XRF) image showing elemental distribution
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["XRFImage"]
    class_class_curie: ClassVar[str] = "aimsleaf:XRFImage"
    class_name: ClassVar[str] = "XRFImage"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.XRFImage

    id: Union[str, XRFImageId] = None
    file_name: str = None
    file_format: Union[str, "FileFormatEnum"] = None
    pixel_size: Optional[Union[dict, "QuantityValue"]] = None
    dimensions_x: Optional[Union[dict, "QuantityValue"]] = None
    dimensions_y: Optional[Union[dict, "QuantityValue"]] = None
    beam_energy: Optional[Union[dict, "QuantityValue"]] = None
    beam_size: Optional[Union[dict, "QuantityValue"]] = None
    dwell_time: Optional[Union[dict, "QuantityValue"]] = None
    elements_measured: Optional[Union[str, list[str]]] = empty_list()
    source_type: Optional[Union[str, "XRaySourceTypeEnum"]] = None
    detector_technology: Optional[Union[str, "DetectorTechnologyEnum"]] = None
    detector_model: Optional[str] = None
    flux: Optional[Union[dict, "QuantityValue"]] = None
    calibration_standard: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, XRFImageId):
            self.id = XRFImageId(self.id)

        if self.pixel_size is not None and not isinstance(self.pixel_size, QuantityValue):
            self.pixel_size = QuantityValue(**as_dict(self.pixel_size))

        if self.dimensions_x is not None and not isinstance(self.dimensions_x, QuantityValue):
            self.dimensions_x = QuantityValue(**as_dict(self.dimensions_x))

        if self.dimensions_y is not None and not isinstance(self.dimensions_y, QuantityValue):
            self.dimensions_y = QuantityValue(**as_dict(self.dimensions_y))

        if self.beam_energy is not None and not isinstance(self.beam_energy, QuantityValue):
            self.beam_energy = QuantityValue(**as_dict(self.beam_energy))

        if self.beam_size is not None and not isinstance(self.beam_size, QuantityValue):
            self.beam_size = QuantityValue(**as_dict(self.beam_size))

        if self.dwell_time is not None and not isinstance(self.dwell_time, QuantityValue):
            self.dwell_time = QuantityValue(**as_dict(self.dwell_time))

        if not isinstance(self.elements_measured, list):
            self.elements_measured = [self.elements_measured] if self.elements_measured is not None else []
        self.elements_measured = [v if isinstance(v, str) else str(v) for v in self.elements_measured]

        if self.source_type is not None and not isinstance(self.source_type, XRaySourceTypeEnum):
            self.source_type = XRaySourceTypeEnum(self.source_type)

        if self.detector_technology is not None and not isinstance(self.detector_technology, DetectorTechnologyEnum):
            self.detector_technology = DetectorTechnologyEnum(self.detector_technology)

        if self.detector_model is not None and not isinstance(self.detector_model, str):
            self.detector_model = str(self.detector_model)

        if self.flux is not None and not isinstance(self.flux, QuantityValue):
            self.flux = QuantityValue(**as_dict(self.flux))

        if self.calibration_standard is not None and not isinstance(self.calibration_standard, str):
            self.calibration_standard = str(self.calibration_standard)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ImageFeature(AttributeGroup):
    """
    Semantic annotations describing features identified in images using controlled vocabulary terms
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["ImageFeature"]
    class_class_curie: ClassVar[str] = "aimsleaf:ImageFeature"
    class_name: ClassVar[str] = "ImageFeature"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.ImageFeature

    terms: Optional[Union[dict[Union[str, OntologyTermId], Union[dict, "OntologyTerm"]], list[Union[dict, "OntologyTerm"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="terms", slot_type=OntologyTerm, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OntologyTerm(NamedThing):
    """
    A term from a controlled vocabulary or ontology
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["OntologyTerm"]
    class_class_curie: ClassVar[str] = "aimsleaf:OntologyTerm"
    class_name: ClassVar[str] = "OntologyTerm"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.OntologyTerm

    id: Union[str, OntologyTermId] = None
    terms: Optional[Union[dict[Union[str, OntologyTermId], Union[dict, "OntologyTerm"]], list[Union[dict, "OntologyTerm"]]]] = empty_dict()
    label: Optional[str] = None
    definition: Optional[str] = None
    ontology: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OntologyTermId):
            self.id = OntologyTermId(self.id)

        self._normalize_inlined_as_list(slot_name="terms", slot_type=OntologyTerm, key_name="id", keyed=True)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        if self.definition is not None and not isinstance(self.definition, str):
            self.definition = str(self.definition)

        if self.ontology is not None and not isinstance(self.ontology, str):
            self.ontology = str(self.ontology)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BufferComposition(AttributeGroup):
    """
    Buffer composition for sample storage
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["BufferComposition"]
    class_class_curie: ClassVar[str] = "aimsleaf:BufferComposition"
    class_name: ClassVar[str] = "BufferComposition"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.BufferComposition

    ph: Optional[Union[dict, "QuantityValue"]] = None
    components: Optional[Union[str, list[str]]] = empty_list()
    additives: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.ph is not None and not isinstance(self.ph, QuantityValue):
            self.ph = QuantityValue(**as_dict(self.ph))

        if not isinstance(self.components, list):
            self.components = [self.components] if self.components is not None else []
        self.components = [v if isinstance(v, str) else str(v) for v in self.components]

        if not isinstance(self.additives, list):
            self.additives = [self.additives] if self.additives is not None else []
        self.additives = [v if isinstance(v, str) else str(v) for v in self.additives]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StorageConditions(AttributeGroup):
    """
    Storage conditions for samples
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["StorageConditions"]
    class_class_curie: ClassVar[str] = "aimsleaf:StorageConditions"
    class_name: ClassVar[str] = "StorageConditions"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.StorageConditions

    temperature: Optional[Union[dict, "QuantityValue"]] = None
    duration: Optional[str] = None
    atmosphere: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.temperature is not None and not isinstance(self.temperature, QuantityValue):
            self.temperature = QuantityValue(**as_dict(self.temperature))

        if self.duration is not None and not isinstance(self.duration, str):
            self.duration = str(self.duration)

        if self.atmosphere is not None and not isinstance(self.atmosphere, str):
            self.atmosphere = str(self.atmosphere)

        super().__post_init__(**kwargs)


class TechniqueSpecificPreparation(AttributeGroup):
    """
    Base class for technique-specific preparation details
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["TechniqueSpecificPreparation"]
    class_class_curie: ClassVar[str] = "aimsleaf:TechniqueSpecificPreparation"
    class_name: ClassVar[str] = "TechniqueSpecificPreparation"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.TechniqueSpecificPreparation


@dataclass(repr=False)
class CryoEMPreparation(TechniqueSpecificPreparation):
    """
    Cryo-EM specific sample preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["CryoEMPreparation"]
    class_class_curie: ClassVar[str] = "aimsleaf:CryoEMPreparation"
    class_name: ClassVar[str] = "CryoEMPreparation"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.CryoEMPreparation

    grid_type: Optional[Union[str, "GridTypeEnum"]] = None
    support_film: Optional[str] = None
    hole_size: Optional[Union[dict, "QuantityValue"]] = None
    vitrification_method: Optional[Union[str, "VitrificationMethodEnum"]] = None
    blot_time: Optional[Union[dict, "QuantityValue"]] = None
    blot_force: Optional[Union[dict, "QuantityValue"]] = None
    humidity_percentage: Optional[Union[dict, "QuantityValue"]] = None
    chamber_temperature: Optional[Union[dict, "QuantityValue"]] = None
    grid_material: Optional[Union[str, "GridMaterialEnum"]] = None
    glow_discharge_applied: Optional[Union[bool, Bool]] = None
    glow_discharge_time: Optional[Union[dict, "QuantityValue"]] = None
    glow_discharge_current: Optional[Union[dict, "QuantityValue"]] = None
    glow_discharge_atmosphere: Optional[str] = None
    glow_discharge_pressure: Optional[Union[dict, "QuantityValue"]] = None
    vitrification_instrument: Optional[str] = None
    blot_number: Optional[Union[dict, "QuantityValue"]] = None
    wait_time: Optional[Union[dict, "QuantityValue"]] = None
    blotter_height: Optional[Union[dict, "QuantityValue"]] = None
    blotter_setting: Optional[Union[dict, "QuantityValue"]] = None
    sample_applied_volume: Optional[Union[dict, "QuantityValue"]] = None
    ethane_temperature: Optional[Union[dict, "QuantityValue"]] = None
    plasma_treatment: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.grid_type is not None and not isinstance(self.grid_type, GridTypeEnum):
            self.grid_type = GridTypeEnum(self.grid_type)

        if self.support_film is not None and not isinstance(self.support_film, str):
            self.support_film = str(self.support_film)

        if self.hole_size is not None and not isinstance(self.hole_size, QuantityValue):
            self.hole_size = QuantityValue(**as_dict(self.hole_size))

        if self.vitrification_method is not None and not isinstance(self.vitrification_method, VitrificationMethodEnum):
            self.vitrification_method = VitrificationMethodEnum(self.vitrification_method)

        if self.blot_time is not None and not isinstance(self.blot_time, QuantityValue):
            self.blot_time = QuantityValue(**as_dict(self.blot_time))

        if self.blot_force is not None and not isinstance(self.blot_force, QuantityValue):
            self.blot_force = QuantityValue(**as_dict(self.blot_force))

        if self.humidity_percentage is not None and not isinstance(self.humidity_percentage, QuantityValue):
            self.humidity_percentage = QuantityValue(**as_dict(self.humidity_percentage))

        if self.chamber_temperature is not None and not isinstance(self.chamber_temperature, QuantityValue):
            self.chamber_temperature = QuantityValue(**as_dict(self.chamber_temperature))

        if self.grid_material is not None and not isinstance(self.grid_material, GridMaterialEnum):
            self.grid_material = GridMaterialEnum(self.grid_material)

        if self.glow_discharge_applied is not None and not isinstance(self.glow_discharge_applied, Bool):
            self.glow_discharge_applied = Bool(self.glow_discharge_applied)

        if self.glow_discharge_time is not None and not isinstance(self.glow_discharge_time, QuantityValue):
            self.glow_discharge_time = QuantityValue(**as_dict(self.glow_discharge_time))

        if self.glow_discharge_current is not None and not isinstance(self.glow_discharge_current, QuantityValue):
            self.glow_discharge_current = QuantityValue(**as_dict(self.glow_discharge_current))

        if self.glow_discharge_atmosphere is not None and not isinstance(self.glow_discharge_atmosphere, str):
            self.glow_discharge_atmosphere = str(self.glow_discharge_atmosphere)

        if self.glow_discharge_pressure is not None and not isinstance(self.glow_discharge_pressure, QuantityValue):
            self.glow_discharge_pressure = QuantityValue(**as_dict(self.glow_discharge_pressure))

        if self.vitrification_instrument is not None and not isinstance(self.vitrification_instrument, str):
            self.vitrification_instrument = str(self.vitrification_instrument)

        if self.blot_number is not None and not isinstance(self.blot_number, QuantityValue):
            self.blot_number = QuantityValue(**as_dict(self.blot_number))

        if self.wait_time is not None and not isinstance(self.wait_time, QuantityValue):
            self.wait_time = QuantityValue(**as_dict(self.wait_time))

        if self.blotter_height is not None and not isinstance(self.blotter_height, QuantityValue):
            self.blotter_height = QuantityValue(**as_dict(self.blotter_height))

        if self.blotter_setting is not None and not isinstance(self.blotter_setting, QuantityValue):
            self.blotter_setting = QuantityValue(**as_dict(self.blotter_setting))

        if self.sample_applied_volume is not None and not isinstance(self.sample_applied_volume, QuantityValue):
            self.sample_applied_volume = QuantityValue(**as_dict(self.sample_applied_volume))

        if self.ethane_temperature is not None and not isinstance(self.ethane_temperature, QuantityValue):
            self.ethane_temperature = QuantityValue(**as_dict(self.ethane_temperature))

        if self.plasma_treatment is not None and not isinstance(self.plasma_treatment, str):
            self.plasma_treatment = str(self.plasma_treatment)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class XRayPreparation(TechniqueSpecificPreparation):
    """
    X-ray crystallography specific preparation
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["XRayPreparation"]
    class_class_curie: ClassVar[str] = "aimsleaf:XRayPreparation"
    class_name: ClassVar[str] = "XRayPreparation"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.XRayPreparation

    protein_concentration_mg_per_ml: Optional[Union[dict, "QuantityValue"]] = None
    protein_buffer: Optional[str] = None
    additives: Optional[str] = None
    crystallization_method: Optional[Union[str, "CrystallizationMethodEnum"]] = None
    screen_name: Optional[str] = None
    temperature_c: Optional[Union[dict, "QuantityValue"]] = None
    drop_ratio_protein_to_reservoir: Optional[str] = None
    drop_volume_nl: Optional[Union[dict, "QuantityValue"]] = None
    reservoir_volume_ul: Optional[Union[dict, "QuantityValue"]] = None
    seeding_type: Optional[str] = None
    seed_stock_dilution: Optional[str] = None
    initial_hit_condition: Optional[str] = None
    optimization_strategy: Optional[str] = None
    optimized_condition: Optional[str] = None
    crystal_size_um: Optional[str] = None
    cryoprotectant: Optional[str] = None
    cryoprotectant_concentration: Optional[Union[dict, "QuantityValue"]] = None
    soak_compound: Optional[str] = None
    soak_conditions: Optional[str] = None
    mounting_method: Optional[str] = None
    flash_cooling_method: Optional[str] = None
    crystal_notes: Optional[str] = None
    loop_size: Optional[Union[dict, "QuantityValue"]] = None
    mounting_temperature: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.protein_concentration_mg_per_ml is not None and not isinstance(self.protein_concentration_mg_per_ml, QuantityValue):
            self.protein_concentration_mg_per_ml = QuantityValue(**as_dict(self.protein_concentration_mg_per_ml))

        if self.protein_buffer is not None and not isinstance(self.protein_buffer, str):
            self.protein_buffer = str(self.protein_buffer)

        if self.additives is not None and not isinstance(self.additives, str):
            self.additives = str(self.additives)

        if self.crystallization_method is not None and not isinstance(self.crystallization_method, CrystallizationMethodEnum):
            self.crystallization_method = CrystallizationMethodEnum(self.crystallization_method)

        if self.screen_name is not None and not isinstance(self.screen_name, str):
            self.screen_name = str(self.screen_name)

        if self.temperature_c is not None and not isinstance(self.temperature_c, QuantityValue):
            self.temperature_c = QuantityValue(**as_dict(self.temperature_c))

        if self.drop_ratio_protein_to_reservoir is not None and not isinstance(self.drop_ratio_protein_to_reservoir, str):
            self.drop_ratio_protein_to_reservoir = str(self.drop_ratio_protein_to_reservoir)

        if self.drop_volume_nl is not None and not isinstance(self.drop_volume_nl, QuantityValue):
            self.drop_volume_nl = QuantityValue(**as_dict(self.drop_volume_nl))

        if self.reservoir_volume_ul is not None and not isinstance(self.reservoir_volume_ul, QuantityValue):
            self.reservoir_volume_ul = QuantityValue(**as_dict(self.reservoir_volume_ul))

        if self.seeding_type is not None and not isinstance(self.seeding_type, str):
            self.seeding_type = str(self.seeding_type)

        if self.seed_stock_dilution is not None and not isinstance(self.seed_stock_dilution, str):
            self.seed_stock_dilution = str(self.seed_stock_dilution)

        if self.initial_hit_condition is not None and not isinstance(self.initial_hit_condition, str):
            self.initial_hit_condition = str(self.initial_hit_condition)

        if self.optimization_strategy is not None and not isinstance(self.optimization_strategy, str):
            self.optimization_strategy = str(self.optimization_strategy)

        if self.optimized_condition is not None and not isinstance(self.optimized_condition, str):
            self.optimized_condition = str(self.optimized_condition)

        if self.crystal_size_um is not None and not isinstance(self.crystal_size_um, str):
            self.crystal_size_um = str(self.crystal_size_um)

        if self.cryoprotectant is not None and not isinstance(self.cryoprotectant, str):
            self.cryoprotectant = str(self.cryoprotectant)

        if self.cryoprotectant_concentration is not None and not isinstance(self.cryoprotectant_concentration, QuantityValue):
            self.cryoprotectant_concentration = QuantityValue(**as_dict(self.cryoprotectant_concentration))

        if self.soak_compound is not None and not isinstance(self.soak_compound, str):
            self.soak_compound = str(self.soak_compound)

        if self.soak_conditions is not None and not isinstance(self.soak_conditions, str):
            self.soak_conditions = str(self.soak_conditions)

        if self.mounting_method is not None and not isinstance(self.mounting_method, str):
            self.mounting_method = str(self.mounting_method)

        if self.flash_cooling_method is not None and not isinstance(self.flash_cooling_method, str):
            self.flash_cooling_method = str(self.flash_cooling_method)

        if self.crystal_notes is not None and not isinstance(self.crystal_notes, str):
            self.crystal_notes = str(self.crystal_notes)

        if self.loop_size is not None and not isinstance(self.loop_size, QuantityValue):
            self.loop_size = QuantityValue(**as_dict(self.loop_size))

        if self.mounting_temperature is not None and not isinstance(self.mounting_temperature, QuantityValue):
            self.mounting_temperature = QuantityValue(**as_dict(self.mounting_temperature))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentalConditions(AttributeGroup):
    """
    Environmental and experimental conditions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["ExperimentalConditions"]
    class_class_curie: ClassVar[str] = "aimsleaf:ExperimentalConditions"
    class_name: ClassVar[str] = "ExperimentalConditions"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.ExperimentalConditions

    temperature: Optional[Union[dict, "QuantityValue"]] = None
    humidity: Optional[Union[dict, "QuantityValue"]] = None
    pressure: Optional[Union[dict, "QuantityValue"]] = None
    atmosphere: Optional[str] = None
    beam_energy: Optional[Union[dict, "QuantityValue"]] = None
    exposure_time: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.temperature is not None and not isinstance(self.temperature, QuantityValue):
            self.temperature = QuantityValue(**as_dict(self.temperature))

        if self.humidity is not None and not isinstance(self.humidity, QuantityValue):
            self.humidity = QuantityValue(**as_dict(self.humidity))

        if self.pressure is not None and not isinstance(self.pressure, QuantityValue):
            self.pressure = QuantityValue(**as_dict(self.pressure))

        if self.atmosphere is not None and not isinstance(self.atmosphere, str):
            self.atmosphere = str(self.atmosphere)

        if self.beam_energy is not None and not isinstance(self.beam_energy, QuantityValue):
            self.beam_energy = QuantityValue(**as_dict(self.beam_energy))

        if self.exposure_time is not None and not isinstance(self.exposure_time, QuantityValue):
            self.exposure_time = QuantityValue(**as_dict(self.exposure_time))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataCollectionStrategy(AttributeGroup):
    """
    Strategy for data collection
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["DataCollectionStrategy"]
    class_class_curie: ClassVar[str] = "aimsleaf:DataCollectionStrategy"
    class_name: ClassVar[str] = "DataCollectionStrategy"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.DataCollectionStrategy

    collection_mode: Optional[Union[str, "CollectionModeEnum"]] = None
    total_frames: Optional[Union[dict, "QuantityValue"]] = None
    frame_rate: Optional[Union[dict, "QuantityValue"]] = None
    total_dose: Optional[Union[dict, "QuantityValue"]] = None
    dose_per_frame: Optional[Union[dict, "QuantityValue"]] = None
    wavelength_a: Optional[Union[dict, "QuantityValue"]] = None
    detector_mode: Optional[Union[str, "DetectorModeEnum"]] = None
    pixel_size_calibrated: Optional[Union[dict, "QuantityValue"]] = None
    detector_distance_mm: Optional[Union[dict, "QuantityValue"]] = None
    beam_center_x_px: Optional[Union[dict, "QuantityValue"]] = None
    beam_center_y_px: Optional[Union[dict, "QuantityValue"]] = None
    beam_size_um: Optional[Union[dict, "QuantityValue"]] = None
    flux_photons_per_s: Optional[Union[dict, "QuantityValue"]] = None
    transmission_percent: Optional[Union[dict, "QuantityValue"]] = None
    attenuator: Optional[str] = None
    temperature_k: Optional[Union[dict, "QuantityValue"]] = None
    oscillation_per_image_deg: Optional[Union[dict, "QuantityValue"]] = None
    total_rotation_deg: Optional[Union[dict, "QuantityValue"]] = None
    strategy_notes: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.collection_mode is not None and not isinstance(self.collection_mode, CollectionModeEnum):
            self.collection_mode = CollectionModeEnum(self.collection_mode)

        if self.total_frames is not None and not isinstance(self.total_frames, QuantityValue):
            self.total_frames = QuantityValue(**as_dict(self.total_frames))

        if self.frame_rate is not None and not isinstance(self.frame_rate, QuantityValue):
            self.frame_rate = QuantityValue(**as_dict(self.frame_rate))

        if self.total_dose is not None and not isinstance(self.total_dose, QuantityValue):
            self.total_dose = QuantityValue(**as_dict(self.total_dose))

        if self.dose_per_frame is not None and not isinstance(self.dose_per_frame, QuantityValue):
            self.dose_per_frame = QuantityValue(**as_dict(self.dose_per_frame))

        if self.wavelength_a is not None and not isinstance(self.wavelength_a, QuantityValue):
            self.wavelength_a = QuantityValue(**as_dict(self.wavelength_a))

        if self.detector_mode is not None and not isinstance(self.detector_mode, DetectorModeEnum):
            self.detector_mode = DetectorModeEnum(self.detector_mode)

        if self.pixel_size_calibrated is not None and not isinstance(self.pixel_size_calibrated, QuantityValue):
            self.pixel_size_calibrated = QuantityValue(**as_dict(self.pixel_size_calibrated))

        if self.detector_distance_mm is not None and not isinstance(self.detector_distance_mm, QuantityValue):
            self.detector_distance_mm = QuantityValue(**as_dict(self.detector_distance_mm))

        if self.beam_center_x_px is not None and not isinstance(self.beam_center_x_px, QuantityValue):
            self.beam_center_x_px = QuantityValue(**as_dict(self.beam_center_x_px))

        if self.beam_center_y_px is not None and not isinstance(self.beam_center_y_px, QuantityValue):
            self.beam_center_y_px = QuantityValue(**as_dict(self.beam_center_y_px))

        if self.beam_size_um is not None and not isinstance(self.beam_size_um, QuantityValue):
            self.beam_size_um = QuantityValue(**as_dict(self.beam_size_um))

        if self.flux_photons_per_s is not None and not isinstance(self.flux_photons_per_s, QuantityValue):
            self.flux_photons_per_s = QuantityValue(**as_dict(self.flux_photons_per_s))

        if self.transmission_percent is not None and not isinstance(self.transmission_percent, QuantityValue):
            self.transmission_percent = QuantityValue(**as_dict(self.transmission_percent))

        if self.attenuator is not None and not isinstance(self.attenuator, str):
            self.attenuator = str(self.attenuator)

        if self.temperature_k is not None and not isinstance(self.temperature_k, QuantityValue):
            self.temperature_k = QuantityValue(**as_dict(self.temperature_k))

        if self.oscillation_per_image_deg is not None and not isinstance(self.oscillation_per_image_deg, QuantityValue):
            self.oscillation_per_image_deg = QuantityValue(**as_dict(self.oscillation_per_image_deg))

        if self.total_rotation_deg is not None and not isinstance(self.total_rotation_deg, QuantityValue):
            self.total_rotation_deg = QuantityValue(**as_dict(self.total_rotation_deg))

        if self.strategy_notes is not None and not isinstance(self.strategy_notes, str):
            self.strategy_notes = str(self.strategy_notes)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QualityMetrics(AttributeGroup):
    """
    Quality metrics for experiments
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["QualityMetrics"]
    class_class_curie: ClassVar[str] = "aimsleaf:QualityMetrics"
    class_name: ClassVar[str] = "QualityMetrics"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.QualityMetrics

    resolution: Optional[Union[dict, "QuantityValue"]] = None
    resolution_high_shell_a: Optional[Union[dict, "QuantityValue"]] = None
    resolution_low_a: Optional[Union[dict, "QuantityValue"]] = None
    completeness: Optional[Union[dict, "QuantityValue"]] = None
    completeness_high_res_shell_percent: Optional[Union[dict, "QuantityValue"]] = None
    signal_to_noise: Optional[Union[dict, "QuantityValue"]] = None
    mean_i_over_sigma_i: Optional[Union[dict, "QuantityValue"]] = None
    space_group: Optional[str] = None
    unit_cell_a: Optional[Union[dict, "QuantityValue"]] = None
    unit_cell_b: Optional[Union[dict, "QuantityValue"]] = None
    unit_cell_c: Optional[Union[dict, "QuantityValue"]] = None
    unit_cell_alpha: Optional[Union[dict, "QuantityValue"]] = None
    unit_cell_beta: Optional[Union[dict, "QuantityValue"]] = None
    unit_cell_gamma: Optional[Union[dict, "QuantityValue"]] = None
    multiplicity: Optional[Union[dict, "QuantityValue"]] = None
    cc_half: Optional[Union[dict, "QuantityValue"]] = None
    r_merge: Optional[Union[dict, "QuantityValue"]] = None
    r_pim: Optional[Union[dict, "QuantityValue"]] = None
    wilson_b_factor_a2: Optional[Union[dict, "QuantityValue"]] = None
    anomalous_used: Optional[Union[bool, Bool]] = None
    anom_corr: Optional[Union[dict, "QuantityValue"]] = None
    anom_sig_ano: Optional[Union[dict, "QuantityValue"]] = None
    r_work: Optional[Union[dict, "QuantityValue"]] = None
    r_free: Optional[Union[dict, "QuantityValue"]] = None
    ramachandran_favored_percent: Optional[Union[dict, "QuantityValue"]] = None
    ramachandran_outliers_percent: Optional[Union[dict, "QuantityValue"]] = None
    clashscore: Optional[Union[dict, "QuantityValue"]] = None
    molprobity_score: Optional[Union[dict, "QuantityValue"]] = None
    average_b_factor_a2: Optional[Union[dict, "QuantityValue"]] = None
    i_zero: Optional[Union[dict, "QuantityValue"]] = None
    rg: Optional[Union[dict, "QuantityValue"]] = None
    r_factor: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.resolution is not None and not isinstance(self.resolution, QuantityValue):
            self.resolution = QuantityValue(**as_dict(self.resolution))

        if self.resolution_high_shell_a is not None and not isinstance(self.resolution_high_shell_a, QuantityValue):
            self.resolution_high_shell_a = QuantityValue(**as_dict(self.resolution_high_shell_a))

        if self.resolution_low_a is not None and not isinstance(self.resolution_low_a, QuantityValue):
            self.resolution_low_a = QuantityValue(**as_dict(self.resolution_low_a))

        if self.completeness is not None and not isinstance(self.completeness, QuantityValue):
            self.completeness = QuantityValue(**as_dict(self.completeness))

        if self.completeness_high_res_shell_percent is not None and not isinstance(self.completeness_high_res_shell_percent, QuantityValue):
            self.completeness_high_res_shell_percent = QuantityValue(**as_dict(self.completeness_high_res_shell_percent))

        if self.signal_to_noise is not None and not isinstance(self.signal_to_noise, QuantityValue):
            self.signal_to_noise = QuantityValue(**as_dict(self.signal_to_noise))

        if self.mean_i_over_sigma_i is not None and not isinstance(self.mean_i_over_sigma_i, QuantityValue):
            self.mean_i_over_sigma_i = QuantityValue(**as_dict(self.mean_i_over_sigma_i))

        if self.space_group is not None and not isinstance(self.space_group, str):
            self.space_group = str(self.space_group)

        if self.unit_cell_a is not None and not isinstance(self.unit_cell_a, QuantityValue):
            self.unit_cell_a = QuantityValue(**as_dict(self.unit_cell_a))

        if self.unit_cell_b is not None and not isinstance(self.unit_cell_b, QuantityValue):
            self.unit_cell_b = QuantityValue(**as_dict(self.unit_cell_b))

        if self.unit_cell_c is not None and not isinstance(self.unit_cell_c, QuantityValue):
            self.unit_cell_c = QuantityValue(**as_dict(self.unit_cell_c))

        if self.unit_cell_alpha is not None and not isinstance(self.unit_cell_alpha, QuantityValue):
            self.unit_cell_alpha = QuantityValue(**as_dict(self.unit_cell_alpha))

        if self.unit_cell_beta is not None and not isinstance(self.unit_cell_beta, QuantityValue):
            self.unit_cell_beta = QuantityValue(**as_dict(self.unit_cell_beta))

        if self.unit_cell_gamma is not None and not isinstance(self.unit_cell_gamma, QuantityValue):
            self.unit_cell_gamma = QuantityValue(**as_dict(self.unit_cell_gamma))

        if self.multiplicity is not None and not isinstance(self.multiplicity, QuantityValue):
            self.multiplicity = QuantityValue(**as_dict(self.multiplicity))

        if self.cc_half is not None and not isinstance(self.cc_half, QuantityValue):
            self.cc_half = QuantityValue(**as_dict(self.cc_half))

        if self.r_merge is not None and not isinstance(self.r_merge, QuantityValue):
            self.r_merge = QuantityValue(**as_dict(self.r_merge))

        if self.r_pim is not None and not isinstance(self.r_pim, QuantityValue):
            self.r_pim = QuantityValue(**as_dict(self.r_pim))

        if self.wilson_b_factor_a2 is not None and not isinstance(self.wilson_b_factor_a2, QuantityValue):
            self.wilson_b_factor_a2 = QuantityValue(**as_dict(self.wilson_b_factor_a2))

        if self.anomalous_used is not None and not isinstance(self.anomalous_used, Bool):
            self.anomalous_used = Bool(self.anomalous_used)

        if self.anom_corr is not None and not isinstance(self.anom_corr, QuantityValue):
            self.anom_corr = QuantityValue(**as_dict(self.anom_corr))

        if self.anom_sig_ano is not None and not isinstance(self.anom_sig_ano, QuantityValue):
            self.anom_sig_ano = QuantityValue(**as_dict(self.anom_sig_ano))

        if self.r_work is not None and not isinstance(self.r_work, QuantityValue):
            self.r_work = QuantityValue(**as_dict(self.r_work))

        if self.r_free is not None and not isinstance(self.r_free, QuantityValue):
            self.r_free = QuantityValue(**as_dict(self.r_free))

        if self.ramachandran_favored_percent is not None and not isinstance(self.ramachandran_favored_percent, QuantityValue):
            self.ramachandran_favored_percent = QuantityValue(**as_dict(self.ramachandran_favored_percent))

        if self.ramachandran_outliers_percent is not None and not isinstance(self.ramachandran_outliers_percent, QuantityValue):
            self.ramachandran_outliers_percent = QuantityValue(**as_dict(self.ramachandran_outliers_percent))

        if self.clashscore is not None and not isinstance(self.clashscore, QuantityValue):
            self.clashscore = QuantityValue(**as_dict(self.clashscore))

        if self.molprobity_score is not None and not isinstance(self.molprobity_score, QuantityValue):
            self.molprobity_score = QuantityValue(**as_dict(self.molprobity_score))

        if self.average_b_factor_a2 is not None and not isinstance(self.average_b_factor_a2, QuantityValue):
            self.average_b_factor_a2 = QuantityValue(**as_dict(self.average_b_factor_a2))

        if self.i_zero is not None and not isinstance(self.i_zero, QuantityValue):
            self.i_zero = QuantityValue(**as_dict(self.i_zero))

        if self.rg is not None and not isinstance(self.rg, QuantityValue):
            self.rg = QuantityValue(**as_dict(self.rg))

        if self.r_factor is not None and not isinstance(self.r_factor, QuantityValue):
            self.r_factor = QuantityValue(**as_dict(self.r_factor))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ComputeResources(AttributeGroup):
    """
    Computational resources used
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["ComputeResources"]
    class_class_curie: ClassVar[str] = "aimsleaf:ComputeResources"
    class_name: ClassVar[str] = "ComputeResources"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.ComputeResources

    cpu_hours: Optional[Union[dict, "QuantityValue"]] = None
    gpu_hours: Optional[Union[dict, "QuantityValue"]] = None
    memory_gb: Optional[Union[dict, "QuantityValue"]] = None
    storage_gb: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.cpu_hours is not None and not isinstance(self.cpu_hours, QuantityValue):
            self.cpu_hours = QuantityValue(**as_dict(self.cpu_hours))

        if self.gpu_hours is not None and not isinstance(self.gpu_hours, QuantityValue):
            self.gpu_hours = QuantityValue(**as_dict(self.gpu_hours))

        if self.memory_gb is not None and not isinstance(self.memory_gb, QuantityValue):
            self.memory_gb = QuantityValue(**as_dict(self.memory_gb))

        if self.storage_gb is not None and not isinstance(self.storage_gb, QuantityValue):
            self.storage_gb = QuantityValue(**as_dict(self.storage_gb))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MotionCorrectionParameters(AttributeGroup):
    """
    Parameters specific to motion correction workflows
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["MotionCorrectionParameters"]
    class_class_curie: ClassVar[str] = "aimsleaf:MotionCorrectionParameters"
    class_name: ClassVar[str] = "MotionCorrectionParameters"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.MotionCorrectionParameters

    patch_size: Optional[Union[dict, "QuantityValue"]] = None
    binning: Optional[Union[dict, "QuantityValue"]] = None
    dose_weighting: Optional[Union[bool, Bool]] = None
    bfactor_dose_weighting: Optional[Union[dict, "QuantityValue"]] = None
    anisotropic_correction: Optional[Union[bool, Bool]] = None
    frame_grouping: Optional[Union[dict, "QuantityValue"]] = None
    output_binning: Optional[Union[dict, "QuantityValue"]] = None
    drift_total: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.patch_size is not None and not isinstance(self.patch_size, QuantityValue):
            self.patch_size = QuantityValue(**as_dict(self.patch_size))

        if self.binning is not None and not isinstance(self.binning, QuantityValue):
            self.binning = QuantityValue(**as_dict(self.binning))

        if self.dose_weighting is not None and not isinstance(self.dose_weighting, Bool):
            self.dose_weighting = Bool(self.dose_weighting)

        if self.bfactor_dose_weighting is not None and not isinstance(self.bfactor_dose_weighting, QuantityValue):
            self.bfactor_dose_weighting = QuantityValue(**as_dict(self.bfactor_dose_weighting))

        if self.anisotropic_correction is not None and not isinstance(self.anisotropic_correction, Bool):
            self.anisotropic_correction = Bool(self.anisotropic_correction)

        if self.frame_grouping is not None and not isinstance(self.frame_grouping, QuantityValue):
            self.frame_grouping = QuantityValue(**as_dict(self.frame_grouping))

        if self.output_binning is not None and not isinstance(self.output_binning, QuantityValue):
            self.output_binning = QuantityValue(**as_dict(self.output_binning))

        if self.drift_total is not None and not isinstance(self.drift_total, QuantityValue):
            self.drift_total = QuantityValue(**as_dict(self.drift_total))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CTFEstimationParameters(AttributeGroup):
    """
    Parameters specific to CTF estimation workflows
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["CTFEstimationParameters"]
    class_class_curie: ClassVar[str] = "aimsleaf:CTFEstimationParameters"
    class_name: ClassVar[str] = "CTFEstimationParameters"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.CTFEstimationParameters

    defocus_search_min: Optional[Union[dict, "QuantityValue"]] = None
    defocus_search_max: Optional[Union[dict, "QuantityValue"]] = None
    defocus_step: Optional[Union[dict, "QuantityValue"]] = None
    amplitude_contrast: Optional[Union[dict, "QuantityValue"]] = None
    cs_used_in_estimation: Optional[Union[dict, "QuantityValue"]] = None
    voltage_used_in_estimation: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.defocus_search_min is not None and not isinstance(self.defocus_search_min, QuantityValue):
            self.defocus_search_min = QuantityValue(**as_dict(self.defocus_search_min))

        if self.defocus_search_max is not None and not isinstance(self.defocus_search_max, QuantityValue):
            self.defocus_search_max = QuantityValue(**as_dict(self.defocus_search_max))

        if self.defocus_step is not None and not isinstance(self.defocus_step, QuantityValue):
            self.defocus_step = QuantityValue(**as_dict(self.defocus_step))

        if self.amplitude_contrast is not None and not isinstance(self.amplitude_contrast, QuantityValue):
            self.amplitude_contrast = QuantityValue(**as_dict(self.amplitude_contrast))

        if self.cs_used_in_estimation is not None and not isinstance(self.cs_used_in_estimation, QuantityValue):
            self.cs_used_in_estimation = QuantityValue(**as_dict(self.cs_used_in_estimation))

        if self.voltage_used_in_estimation is not None and not isinstance(self.voltage_used_in_estimation, QuantityValue):
            self.voltage_used_in_estimation = QuantityValue(**as_dict(self.voltage_used_in_estimation))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ParticlePickingParameters(AttributeGroup):
    """
    Parameters specific to particle picking workflows
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["ParticlePickingParameters"]
    class_class_curie: ClassVar[str] = "aimsleaf:ParticlePickingParameters"
    class_name: ClassVar[str] = "ParticlePickingParameters"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.ParticlePickingParameters

    picking_method: Optional[str] = None
    box_size: Optional[Union[dict, "QuantityValue"]] = None
    threshold: Optional[Union[dict, "QuantityValue"]] = None
    power_score: Optional[Union[dict, "QuantityValue"]] = None
    ncc_score: Optional[Union[dict, "QuantityValue"]] = None
    model_name: Optional[str] = None
    model_file_path: Optional[str] = None
    model_source: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.picking_method is not None and not isinstance(self.picking_method, str):
            self.picking_method = str(self.picking_method)

        if self.box_size is not None and not isinstance(self.box_size, QuantityValue):
            self.box_size = QuantityValue(**as_dict(self.box_size))

        if self.threshold is not None and not isinstance(self.threshold, QuantityValue):
            self.threshold = QuantityValue(**as_dict(self.threshold))

        if self.power_score is not None and not isinstance(self.power_score, QuantityValue):
            self.power_score = QuantityValue(**as_dict(self.power_score))

        if self.ncc_score is not None and not isinstance(self.ncc_score, QuantityValue):
            self.ncc_score = QuantityValue(**as_dict(self.ncc_score))

        if self.model_name is not None and not isinstance(self.model_name, str):
            self.model_name = str(self.model_name)

        if self.model_file_path is not None and not isinstance(self.model_file_path, str):
            self.model_file_path = str(self.model_file_path)

        if self.model_source is not None and not isinstance(self.model_source, str):
            self.model_source = str(self.model_source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RefinementParameters(AttributeGroup):
    """
    Parameters specific to 3D refinement workflows
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["RefinementParameters"]
    class_class_curie: ClassVar[str] = "aimsleaf:RefinementParameters"
    class_name: ClassVar[str] = "RefinementParameters"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.RefinementParameters

    symmetry: Optional[Union[str, "SymmetryEnum"]] = None
    pixel_size: Optional[Union[dict, "QuantityValue"]] = None
    box_size: Optional[Union[dict, "QuantityValue"]] = None
    gold_standard: Optional[Union[bool, Bool]] = None
    split_strategy: Optional[str] = None
    resolution_0_143: Optional[Union[dict, "QuantityValue"]] = None
    resolution_0_5: Optional[Union[dict, "QuantityValue"]] = None
    map_sharpening_bfactor: Optional[Union[dict, "QuantityValue"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.symmetry is not None and not isinstance(self.symmetry, SymmetryEnum):
            self.symmetry = SymmetryEnum(self.symmetry)

        if self.pixel_size is not None and not isinstance(self.pixel_size, QuantityValue):
            self.pixel_size = QuantityValue(**as_dict(self.pixel_size))

        if self.box_size is not None and not isinstance(self.box_size, QuantityValue):
            self.box_size = QuantityValue(**as_dict(self.box_size))

        if self.gold_standard is not None and not isinstance(self.gold_standard, Bool):
            self.gold_standard = Bool(self.gold_standard)

        if self.split_strategy is not None and not isinstance(self.split_strategy, str):
            self.split_strategy = str(self.split_strategy)

        if self.resolution_0_143 is not None and not isinstance(self.resolution_0_143, QuantityValue):
            self.resolution_0_143 = QuantityValue(**as_dict(self.resolution_0_143))

        if self.resolution_0_5 is not None and not isinstance(self.resolution_0_5, QuantityValue):
            self.resolution_0_5 = QuantityValue(**as_dict(self.resolution_0_5))

        if self.map_sharpening_bfactor is not None and not isinstance(self.map_sharpening_bfactor, QuantityValue):
            self.map_sharpening_bfactor = QuantityValue(**as_dict(self.map_sharpening_bfactor))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StudySampleAssociation(YAMLRoot):
    """
    M:N link between Study and Sample with role metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["StudySampleAssociation"]
    class_class_curie: ClassVar[str] = "aimsleaf:StudySampleAssociation"
    class_name: ClassVar[str] = "StudySampleAssociation"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.StudySampleAssociation

    study_id: Union[str, StudyId] = None
    sample_id: Union[str, SampleId] = None
    role: Optional[Union[str, "SampleRoleEnum"]] = None
    date_added: Optional[Union[str, XSDDate]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.study_id):
            self.MissingRequiredField("study_id")
        if not isinstance(self.study_id, StudyId):
            self.study_id = StudyId(self.study_id)

        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, SampleId):
            self.sample_id = SampleId(self.sample_id)

        if self.role is not None and not isinstance(self.role, SampleRoleEnum):
            self.role = SampleRoleEnum(self.role)

        if self.date_added is not None and not isinstance(self.date_added, XSDDate):
            self.date_added = XSDDate(self.date_added)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SampleDataAssociation(YAMLRoot):
    """
    M:N link between Sample and Data with role metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["SampleDataAssociation"]
    class_class_curie: ClassVar[str] = "aimsleaf:SampleDataAssociation"
    class_name: ClassVar[str] = "SampleDataAssociation"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.SampleDataAssociation

    sample_id: Union[str, SampleId] = None
    data_id: Union[str, DataFileId] = None
    role: Optional[Union[str, "SampleRoleEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, SampleId):
            self.sample_id = SampleId(self.sample_id)

        if self._is_empty(self.data_id):
            self.MissingRequiredField("data_id")
        if not isinstance(self.data_id, DataFileId):
            self.data_id = DataFileId(self.data_id)

        if self.role is not None and not isinstance(self.role, SampleRoleEnum):
            self.role = SampleRoleEnum(self.role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StudyExperimentAssociation(YAMLRoot):
    """
    M:N link between Study and ExperimentRun
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["StudyExperimentAssociation"]
    class_class_curie: ClassVar[str] = "aimsleaf:StudyExperimentAssociation"
    class_name: ClassVar[str] = "StudyExperimentAssociation"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.StudyExperimentAssociation

    study_id: Union[str, StudyId] = None
    experiment_id: Union[str, ExperimentRunId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.study_id):
            self.MissingRequiredField("study_id")
        if not isinstance(self.study_id, StudyId):
            self.study_id = StudyId(self.study_id)

        if self._is_empty(self.experiment_id):
            self.MissingRequiredField("experiment_id")
        if not isinstance(self.experiment_id, ExperimentRunId):
            self.experiment_id = ExperimentRunId(self.experiment_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StudyWorkflowAssociation(YAMLRoot):
    """
    M:N link between Study and WorkflowRun
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["StudyWorkflowAssociation"]
    class_class_curie: ClassVar[str] = "aimsleaf:StudyWorkflowAssociation"
    class_name: ClassVar[str] = "StudyWorkflowAssociation"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.StudyWorkflowAssociation

    study_id: Union[str, StudyId] = None
    workflow_id: Union[str, WorkflowRunId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.study_id):
            self.MissingRequiredField("study_id")
        if not isinstance(self.study_id, StudyId):
            self.study_id = StudyId(self.study_id)

        if self._is_empty(self.workflow_id):
            self.MissingRequiredField("workflow_id")
        if not isinstance(self.workflow_id, WorkflowRunId):
            self.workflow_id = WorkflowRunId(self.workflow_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentSampleAssociation(YAMLRoot):
    """
    M:N link between ExperimentRun and Sample with role metadata
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["ExperimentSampleAssociation"]
    class_class_curie: ClassVar[str] = "aimsleaf:ExperimentSampleAssociation"
    class_name: ClassVar[str] = "ExperimentSampleAssociation"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.ExperimentSampleAssociation

    experiment_id: Union[str, ExperimentRunId] = None
    sample_id: Union[str, SampleId] = None
    role: Optional[Union[str, "ExperimentSampleRoleEnum"]] = None
    preparation_id: Optional[Union[str, SamplePreparationId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.experiment_id):
            self.MissingRequiredField("experiment_id")
        if not isinstance(self.experiment_id, ExperimentRunId):
            self.experiment_id = ExperimentRunId(self.experiment_id)

        if self._is_empty(self.sample_id):
            self.MissingRequiredField("sample_id")
        if not isinstance(self.sample_id, SampleId):
            self.sample_id = SampleId(self.sample_id)

        if self.role is not None and not isinstance(self.role, ExperimentSampleRoleEnum):
            self.role = ExperimentSampleRoleEnum(self.role)

        if self.preparation_id is not None and not isinstance(self.preparation_id, SamplePreparationId):
            self.preparation_id = SamplePreparationId(self.preparation_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ExperimentInstrumentAssociation(YAMLRoot):
    """
    M:N link between ExperimentRun and Instrument
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["ExperimentInstrumentAssociation"]
    class_class_curie: ClassVar[str] = "aimsleaf:ExperimentInstrumentAssociation"
    class_name: ClassVar[str] = "ExperimentInstrumentAssociation"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.ExperimentInstrumentAssociation

    experiment_id: Union[str, ExperimentRunId] = None
    instrument_id: Union[str, InstrumentId] = None
    role: Optional[Union[str, "InstrumentRoleEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.experiment_id):
            self.MissingRequiredField("experiment_id")
        if not isinstance(self.experiment_id, ExperimentRunId):
            self.experiment_id = ExperimentRunId(self.experiment_id)

        if self._is_empty(self.instrument_id):
            self.MissingRequiredField("instrument_id")
        if not isinstance(self.instrument_id, InstrumentId):
            self.instrument_id = InstrumentId(self.instrument_id)

        if self.role is not None and not isinstance(self.role, InstrumentRoleEnum):
            self.role = InstrumentRoleEnum(self.role)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WorkflowExperimentAssociation(YAMLRoot):
    """
    M:N link between WorkflowRun and source ExperimentRuns
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["WorkflowExperimentAssociation"]
    class_class_curie: ClassVar[str] = "aimsleaf:WorkflowExperimentAssociation"
    class_name: ClassVar[str] = "WorkflowExperimentAssociation"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.WorkflowExperimentAssociation

    workflow_id: Union[str, WorkflowRunId] = None
    experiment_id: Union[str, ExperimentRunId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.workflow_id):
            self.MissingRequiredField("workflow_id")
        if not isinstance(self.workflow_id, WorkflowRunId):
            self.workflow_id = WorkflowRunId(self.workflow_id)

        if self._is_empty(self.experiment_id):
            self.MissingRequiredField("experiment_id")
        if not isinstance(self.experiment_id, ExperimentRunId):
            self.experiment_id = ExperimentRunId(self.experiment_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WorkflowInputAssociation(YAMLRoot):
    """
    Links input DataFiles to WorkflowRun
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["WorkflowInputAssociation"]
    class_class_curie: ClassVar[str] = "aimsleaf:WorkflowInputAssociation"
    class_name: ClassVar[str] = "WorkflowInputAssociation"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.WorkflowInputAssociation

    workflow_id: Union[str, WorkflowRunId] = None
    file_id: Union[str, DataFileId] = None
    input_type: Optional[Union[str, "InputTypeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.workflow_id):
            self.MissingRequiredField("workflow_id")
        if not isinstance(self.workflow_id, WorkflowRunId):
            self.workflow_id = WorkflowRunId(self.workflow_id)

        if self._is_empty(self.file_id):
            self.MissingRequiredField("file_id")
        if not isinstance(self.file_id, DataFileId):
            self.file_id = DataFileId(self.file_id)

        if self.input_type is not None and not isinstance(self.input_type, InputTypeEnum):
            self.input_type = InputTypeEnum(self.input_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class WorkflowOutputAssociation(YAMLRoot):
    """
    Links output DataFiles to WorkflowRun
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["WorkflowOutputAssociation"]
    class_class_curie: ClassVar[str] = "aimsleaf:WorkflowOutputAssociation"
    class_name: ClassVar[str] = "WorkflowOutputAssociation"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.WorkflowOutputAssociation

    workflow_id: Union[str, WorkflowRunId] = None
    file_id: Union[str, DataFileId] = None
    output_type: Optional[Union[str, "OutputTypeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.workflow_id):
            self.MissingRequiredField("workflow_id")
        if not isinstance(self.workflow_id, WorkflowRunId):
            self.workflow_id = WorkflowRunId(self.workflow_id)

        if self._is_empty(self.file_id):
            self.MissingRequiredField("file_id")
        if not isinstance(self.file_id, DataFileId):
            self.file_id = DataFileId(self.file_id)

        if self.output_type is not None and not isinstance(self.output_type, OutputTypeEnum):
            self.output_type = OutputTypeEnum(self.output_type)

        super().__post_init__(**kwargs)


Any = Any

@dataclass(repr=False)
class AttributeValue(YAMLRoot):
    """
    The value for any attribute of an entity. This object can hold both the un-normalized atomic value and the
    structured value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["AttributeValue"]
    class_class_curie: ClassVar[str] = "nmdc:AttributeValue"
    class_name: ClassVar[str] = "AttributeValue"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.AttributeValue

    attribute: Optional[Union[dict, "Attribute"]] = None
    raw_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.attribute is not None and not isinstance(self.attribute, Attribute):
            self.attribute = Attribute(**as_dict(self.attribute))

        if self.raw_value is not None and not isinstance(self.raw_value, str):
            self.raw_value = str(self.raw_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Attribute(YAMLRoot):
    """
    A domain, measurement, attribute, property, or any descriptor for additional properties to be added to an entity.
    Where available, please use OBO Foundry ontologies or other controlled vocabularies for attributes; the label
    should be the term name from the ontology and the id should be the fully-qualified CURIE.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["Attribute"]
    class_class_curie: ClassVar[str] = "aimsleaf:Attribute"
    class_name: ClassVar[str] = "Attribute"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.Attribute

    label: str = None
    id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.label):
            self.MissingRequiredField("label")
        if not isinstance(self.label, str):
            self.label = str(self.label)

        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class QuantityValue(AttributeValue):
    """
    A simple quantity value, representing a measurement with a numeric value and unit. This allows data providers to
    specify measurements in their preferred unit while enabling standardized interpretation. For example, a pixel size
    could be specified as 1.5 micrometers or 15 Angstroms, with the unit clearly specified.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["QuantityValue"]
    class_class_curie: ClassVar[str] = "nmdc:QuantityValue"
    class_name: ClassVar[str] = "QuantityValue"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.QuantityValue

    unit: str = None
    maximum_numeric_value: Optional[float] = None
    minimum_numeric_value: Optional[float] = None
    numeric_value: Optional[float] = None
    unit_cv_id: Optional[Union[str, Curie]] = None
    raw_value: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.maximum_numeric_value is not None and not isinstance(self.maximum_numeric_value, float):
            self.maximum_numeric_value = float(self.maximum_numeric_value)

        if self.minimum_numeric_value is not None and not isinstance(self.minimum_numeric_value, float):
            self.minimum_numeric_value = float(self.minimum_numeric_value)

        if self.numeric_value is not None and not isinstance(self.numeric_value, float):
            self.numeric_value = float(self.numeric_value)

        if self.unit_cv_id is not None and not isinstance(self.unit_cv_id, Curie):
            self.unit_cv_id = Curie(self.unit_cv_id)

        if self.raw_value is not None and not isinstance(self.raw_value, str):
            self.raw_value = str(self.raw_value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TextValue(AttributeValue):
    """
    A value described using a text string, optionally with a controlled vocabulary ID.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["TextValue"]
    class_class_curie: ClassVar[str] = "nmdc:TextValue"
    class_name: ClassVar[str] = "TextValue"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.TextValue

    value: str = None
    value_cv_id: Optional[Union[str, Curie]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        if self.value_cv_id is not None and not isinstance(self.value_cv_id, Curie):
            self.value_cv_id = Curie(self.value_cv_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DateTimeValue(AttributeValue):
    """
    A date or date and time value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NMDC["DateTimeValue"]
    class_class_curie: ClassVar[str] = "nmdc:DateTimeValue"
    class_name: ClassVar[str] = "DateTimeValue"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.DateTimeValue

    value: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, str):
            self.value = str(self.value)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProteinAnnotation(NamedThing):
    """
    Base class for all protein-related functional and structural annotations
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["functional_annotation/ProteinAnnotation"]
    class_class_curie: ClassVar[str] = "aimsleaf:functional_annotation/ProteinAnnotation"
    class_name: ClassVar[str] = "ProteinAnnotation"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.ProteinAnnotation

    id: Union[str, ProteinAnnotationId] = None
    protein_id: str = None
    pdb_entry: Optional[str] = None
    chain_id: Optional[str] = None
    residue_range: Optional[str] = None
    confidence_score: Optional[float] = None
    evidence_type: Optional[Union[str, "EvidenceTypeEnum"]] = None
    evidence_code: Optional[Union[str, URIorCURIE]] = None
    source_database: Optional[Union[str, "AnnotationSourceEnum"]] = None
    annotation_method: Optional[str] = None
    publication_ids: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinAnnotationId):
            self.id = ProteinAnnotationId(self.id)

        if self._is_empty(self.protein_id):
            self.MissingRequiredField("protein_id")
        if not isinstance(self.protein_id, str):
            self.protein_id = str(self.protein_id)

        if self.pdb_entry is not None and not isinstance(self.pdb_entry, str):
            self.pdb_entry = str(self.pdb_entry)

        if self.chain_id is not None and not isinstance(self.chain_id, str):
            self.chain_id = str(self.chain_id)

        if self.residue_range is not None and not isinstance(self.residue_range, str):
            self.residue_range = str(self.residue_range)

        if self.confidence_score is not None and not isinstance(self.confidence_score, float):
            self.confidence_score = float(self.confidence_score)

        if self.evidence_type is not None and not isinstance(self.evidence_type, EvidenceTypeEnum):
            self.evidence_type = EvidenceTypeEnum(self.evidence_type)

        if self.evidence_code is not None and not isinstance(self.evidence_code, URIorCURIE):
            self.evidence_code = URIorCURIE(self.evidence_code)

        if self.source_database is not None and not isinstance(self.source_database, AnnotationSourceEnum):
            self.source_database = AnnotationSourceEnum(self.source_database)

        if self.annotation_method is not None and not isinstance(self.annotation_method, str):
            self.annotation_method = str(self.annotation_method)

        if not isinstance(self.publication_ids, list):
            self.publication_ids = [self.publication_ids] if self.publication_ids is not None else []
        self.publication_ids = [v if isinstance(v, str) else str(v) for v in self.publication_ids]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class FunctionalSite(ProteinAnnotation):
    """
    Functional sites including catalytic, binding, and regulatory sites
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["functional_annotation/FunctionalSite"]
    class_class_curie: ClassVar[str] = "aimsleaf:functional_annotation/FunctionalSite"
    class_name: ClassVar[str] = "FunctionalSite"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.FunctionalSite

    id: Union[str, FunctionalSiteId] = None
    protein_id: str = None
    site_type: Union[str, "FunctionalSiteTypeEnum"] = None
    site_name: Optional[str] = None
    residues: Optional[Union[str, list[str]]] = empty_list()
    ligand_interactions: Optional[Union[Union[dict, "LigandInteraction"], list[Union[dict, "LigandInteraction"]]]] = empty_list()
    conservation_score: Optional[float] = None
    functional_importance: Optional[str] = None
    go_terms: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()
    ec_number: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FunctionalSiteId):
            self.id = FunctionalSiteId(self.id)

        if self._is_empty(self.site_type):
            self.MissingRequiredField("site_type")
        if not isinstance(self.site_type, FunctionalSiteTypeEnum):
            self.site_type = FunctionalSiteTypeEnum(self.site_type)

        if self.site_name is not None and not isinstance(self.site_name, str):
            self.site_name = str(self.site_name)

        if not isinstance(self.residues, list):
            self.residues = [self.residues] if self.residues is not None else []
        self.residues = [v if isinstance(v, str) else str(v) for v in self.residues]

        if not isinstance(self.ligand_interactions, list):
            self.ligand_interactions = [self.ligand_interactions] if self.ligand_interactions is not None else []
        self.ligand_interactions = [v if isinstance(v, LigandInteraction) else LigandInteraction(**as_dict(v)) for v in self.ligand_interactions]

        if self.conservation_score is not None and not isinstance(self.conservation_score, float):
            self.conservation_score = float(self.conservation_score)

        if self.functional_importance is not None and not isinstance(self.functional_importance, str):
            self.functional_importance = str(self.functional_importance)

        if not isinstance(self.go_terms, list):
            self.go_terms = [self.go_terms] if self.go_terms is not None else []
        self.go_terms = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.go_terms]

        if self.ec_number is not None and not isinstance(self.ec_number, str):
            self.ec_number = str(self.ec_number)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StructuralFeature(ProteinAnnotation):
    """
    Structural features and properties of protein regions
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["functional_annotation/StructuralFeature"]
    class_class_curie: ClassVar[str] = "aimsleaf:functional_annotation/StructuralFeature"
    class_name: ClassVar[str] = "StructuralFeature"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.StructuralFeature

    id: Union[str, StructuralFeatureId] = None
    protein_id: str = None
    feature_type: Union[str, "StructuralFeatureTypeEnum"] = None
    secondary_structure: Optional[Union[str, "SecondaryStructureEnum"]] = None
    solvent_accessibility: Optional[float] = None
    backbone_flexibility: Optional[float] = None
    disorder_probability: Optional[float] = None
    conformational_state: Optional[Union[str, "ConformationalStateEnum"]] = None
    structural_motif: Optional[str] = None
    domain_assignment: Optional[str] = None
    domain_id: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StructuralFeatureId):
            self.id = StructuralFeatureId(self.id)

        if self._is_empty(self.feature_type):
            self.MissingRequiredField("feature_type")
        if not isinstance(self.feature_type, StructuralFeatureTypeEnum):
            self.feature_type = StructuralFeatureTypeEnum(self.feature_type)

        if self.secondary_structure is not None and not isinstance(self.secondary_structure, SecondaryStructureEnum):
            self.secondary_structure = SecondaryStructureEnum(self.secondary_structure)

        if self.solvent_accessibility is not None and not isinstance(self.solvent_accessibility, float):
            self.solvent_accessibility = float(self.solvent_accessibility)

        if self.backbone_flexibility is not None and not isinstance(self.backbone_flexibility, float):
            self.backbone_flexibility = float(self.backbone_flexibility)

        if self.disorder_probability is not None and not isinstance(self.disorder_probability, float):
            self.disorder_probability = float(self.disorder_probability)

        if self.conformational_state is not None and not isinstance(self.conformational_state, ConformationalStateEnum):
            self.conformational_state = ConformationalStateEnum(self.conformational_state)

        if self.structural_motif is not None and not isinstance(self.structural_motif, str):
            self.structural_motif = str(self.structural_motif)

        if self.domain_assignment is not None and not isinstance(self.domain_assignment, str):
            self.domain_assignment = str(self.domain_assignment)

        if self.domain_id is not None and not isinstance(self.domain_id, str):
            self.domain_id = str(self.domain_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class LigandInteraction(AttributeGroup):
    """
    Small molecule/ligand interactions with proteins
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["functional_annotation/LigandInteraction"]
    class_class_curie: ClassVar[str] = "aimsleaf:functional_annotation/LigandInteraction"
    class_name: ClassVar[str] = "LigandInteraction"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.LigandInteraction

    ligand_id: Union[str, URIorCURIE] = None
    ligand_name: str = None
    ligand_smiles: Optional[Union[str, SmilesString]] = None
    binding_affinity: Optional[float] = None
    binding_affinity_type: Optional[Union[str, "BindingAffinityTypeEnum"]] = None
    binding_affinity_unit: Optional[Union[str, "AffinityUnitEnum"]] = None
    interaction_type: Optional[Union[str, "InteractionTypeEnum"]] = None
    binding_site_residues: Optional[Union[str, list[str]]] = empty_list()
    is_cofactor: Optional[Union[bool, Bool]] = None
    is_drug_like: Optional[Union[bool, Bool]] = None
    druggability_score: Optional[float] = None
    interaction_distance: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ligand_id):
            self.MissingRequiredField("ligand_id")
        if not isinstance(self.ligand_id, URIorCURIE):
            self.ligand_id = URIorCURIE(self.ligand_id)

        if self._is_empty(self.ligand_name):
            self.MissingRequiredField("ligand_name")
        if not isinstance(self.ligand_name, str):
            self.ligand_name = str(self.ligand_name)

        if self.ligand_smiles is not None and not isinstance(self.ligand_smiles, SmilesString):
            self.ligand_smiles = SmilesString(self.ligand_smiles)

        if self.binding_affinity is not None and not isinstance(self.binding_affinity, float):
            self.binding_affinity = float(self.binding_affinity)

        if self.binding_affinity_type is not None and not isinstance(self.binding_affinity_type, BindingAffinityTypeEnum):
            self.binding_affinity_type = BindingAffinityTypeEnum(self.binding_affinity_type)

        if self.binding_affinity_unit is not None and not isinstance(self.binding_affinity_unit, AffinityUnitEnum):
            self.binding_affinity_unit = AffinityUnitEnum(self.binding_affinity_unit)

        if self.interaction_type is not None and not isinstance(self.interaction_type, InteractionTypeEnum):
            self.interaction_type = InteractionTypeEnum(self.interaction_type)

        if not isinstance(self.binding_site_residues, list):
            self.binding_site_residues = [self.binding_site_residues] if self.binding_site_residues is not None else []
        self.binding_site_residues = [v if isinstance(v, str) else str(v) for v in self.binding_site_residues]

        if self.is_cofactor is not None and not isinstance(self.is_cofactor, Bool):
            self.is_cofactor = Bool(self.is_cofactor)

        if self.is_drug_like is not None and not isinstance(self.is_drug_like, Bool):
            self.is_drug_like = Bool(self.is_drug_like)

        if self.druggability_score is not None and not isinstance(self.druggability_score, float):
            self.druggability_score = float(self.druggability_score)

        if self.interaction_distance is not None and not isinstance(self.interaction_distance, float):
            self.interaction_distance = float(self.interaction_distance)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ProteinProteinInteraction(ProteinAnnotation):
    """
    Protein-protein interactions and interfaces
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["functional_annotation/ProteinProteinInteraction"]
    class_class_curie: ClassVar[str] = "aimsleaf:functional_annotation/ProteinProteinInteraction"
    class_name: ClassVar[str] = "ProteinProteinInteraction"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.ProteinProteinInteraction

    id: Union[str, ProteinProteinInteractionId] = None
    protein_id: str = None
    partner_protein_id: str = None
    partner_chain_id: Optional[str] = None
    interface_residues: Optional[Union[str, list[str]]] = empty_list()
    partner_interface_residues: Optional[Union[str, list[str]]] = empty_list()
    interface_area: Optional[float] = None
    binding_energy: Optional[float] = None
    dissociation_constant: Optional[float] = None
    complex_stability: Optional[Union[str, "ComplexStabilityEnum"]] = None
    biological_assembly: Optional[Union[bool, Bool]] = None
    interaction_evidence: Optional[Union[Union[str, "InteractionEvidenceEnum"], list[Union[str, "InteractionEvidenceEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProteinProteinInteractionId):
            self.id = ProteinProteinInteractionId(self.id)

        if self._is_empty(self.partner_protein_id):
            self.MissingRequiredField("partner_protein_id")
        if not isinstance(self.partner_protein_id, str):
            self.partner_protein_id = str(self.partner_protein_id)

        if self.partner_chain_id is not None and not isinstance(self.partner_chain_id, str):
            self.partner_chain_id = str(self.partner_chain_id)

        if not isinstance(self.interface_residues, list):
            self.interface_residues = [self.interface_residues] if self.interface_residues is not None else []
        self.interface_residues = [v if isinstance(v, str) else str(v) for v in self.interface_residues]

        if not isinstance(self.partner_interface_residues, list):
            self.partner_interface_residues = [self.partner_interface_residues] if self.partner_interface_residues is not None else []
        self.partner_interface_residues = [v if isinstance(v, str) else str(v) for v in self.partner_interface_residues]

        if self.interface_area is not None and not isinstance(self.interface_area, float):
            self.interface_area = float(self.interface_area)

        if self.binding_energy is not None and not isinstance(self.binding_energy, float):
            self.binding_energy = float(self.binding_energy)

        if self.dissociation_constant is not None and not isinstance(self.dissociation_constant, float):
            self.dissociation_constant = float(self.dissociation_constant)

        if self.complex_stability is not None and not isinstance(self.complex_stability, ComplexStabilityEnum):
            self.complex_stability = ComplexStabilityEnum(self.complex_stability)

        if self.biological_assembly is not None and not isinstance(self.biological_assembly, Bool):
            self.biological_assembly = Bool(self.biological_assembly)

        if not isinstance(self.interaction_evidence, list):
            self.interaction_evidence = [self.interaction_evidence] if self.interaction_evidence is not None else []
        self.interaction_evidence = [v if isinstance(v, InteractionEvidenceEnum) else InteractionEvidenceEnum(v) for v in self.interaction_evidence]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MutationEffect(ProteinAnnotation):
    """
    Effects of mutations and variants on protein structure and function
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["functional_annotation/MutationEffect"]
    class_class_curie: ClassVar[str] = "aimsleaf:functional_annotation/MutationEffect"
    class_name: ClassVar[str] = "MutationEffect"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.MutationEffect

    id: Union[str, MutationEffectId] = None
    protein_id: str = None
    mutation: str = None
    mutation_type: Optional[Union[str, "MutationTypeEnum"]] = None
    effect_on_stability: Optional[Union[str, "StabilityEffectEnum"]] = None
    delta_delta_g: Optional[float] = None
    effect_on_function: Optional[Union[str, "FunctionalEffectEnum"]] = None
    functional_impact_description: Optional[str] = None
    disease_association: Optional[str] = None
    omim_id: Optional[str] = None
    clinical_significance: Optional[Union[str, "ClinicalSignificanceEnum"]] = None
    allele_frequency: Optional[float] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MutationEffectId):
            self.id = MutationEffectId(self.id)

        if self._is_empty(self.mutation):
            self.MissingRequiredField("mutation")
        if not isinstance(self.mutation, str):
            self.mutation = str(self.mutation)

        if self.mutation_type is not None and not isinstance(self.mutation_type, MutationTypeEnum):
            self.mutation_type = MutationTypeEnum(self.mutation_type)

        if self.effect_on_stability is not None and not isinstance(self.effect_on_stability, StabilityEffectEnum):
            self.effect_on_stability = StabilityEffectEnum(self.effect_on_stability)

        if self.delta_delta_g is not None and not isinstance(self.delta_delta_g, float):
            self.delta_delta_g = float(self.delta_delta_g)

        if self.effect_on_function is not None and not isinstance(self.effect_on_function, FunctionalEffectEnum):
            self.effect_on_function = FunctionalEffectEnum(self.effect_on_function)

        if self.functional_impact_description is not None and not isinstance(self.functional_impact_description, str):
            self.functional_impact_description = str(self.functional_impact_description)

        if self.disease_association is not None and not isinstance(self.disease_association, str):
            self.disease_association = str(self.disease_association)

        if self.omim_id is not None and not isinstance(self.omim_id, str):
            self.omim_id = str(self.omim_id)

        if self.clinical_significance is not None and not isinstance(self.clinical_significance, ClinicalSignificanceEnum):
            self.clinical_significance = ClinicalSignificanceEnum(self.clinical_significance)

        if self.allele_frequency is not None and not isinstance(self.allele_frequency, float):
            self.allele_frequency = float(self.allele_frequency)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BiophysicalProperty(AttributeGroup):
    """
    Measured or calculated biophysical properties
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["functional_annotation/BiophysicalProperty"]
    class_class_curie: ClassVar[str] = "aimsleaf:functional_annotation/BiophysicalProperty"
    class_name: ClassVar[str] = "BiophysicalProperty"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.BiophysicalProperty

    property_type: Union[str, "BiophysicalPropertyEnum"] = None
    value: float = None
    unit: str = None
    error: Optional[float] = None
    measurement_conditions: Optional[Union[dict[Union[str, MeasurementConditionsId], Union[dict, "MeasurementConditions"]], list[Union[dict, "MeasurementConditions"]]]] = empty_dict()
    experimental_method: Optional[Union[str, "BiophysicalMethodEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.property_type):
            self.MissingRequiredField("property_type")
        if not isinstance(self.property_type, BiophysicalPropertyEnum):
            self.property_type = BiophysicalPropertyEnum(self.property_type)

        if self._is_empty(self.value):
            self.MissingRequiredField("value")
        if not isinstance(self.value, float):
            self.value = float(self.value)

        if self._is_empty(self.unit):
            self.MissingRequiredField("unit")
        if not isinstance(self.unit, str):
            self.unit = str(self.unit)

        if self.error is not None and not isinstance(self.error, float):
            self.error = float(self.error)

        self._normalize_inlined_as_list(slot_name="measurement_conditions", slot_type=MeasurementConditions, key_name="id", keyed=True)

        if self.experimental_method is not None and not isinstance(self.experimental_method, BiophysicalMethodEnum):
            self.experimental_method = BiophysicalMethodEnum(self.experimental_method)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConformationalEnsemble(NamedThing):
    """
    Ensemble of conformational states for a protein
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["functional_annotation/ConformationalEnsemble"]
    class_class_curie: ClassVar[str] = "aimsleaf:functional_annotation/ConformationalEnsemble"
    class_name: ClassVar[str] = "ConformationalEnsemble"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.ConformationalEnsemble

    id: Union[str, ConformationalEnsembleId] = None
    protein_id: str = None
    conformational_states: Optional[Union[Union[dict, "ConformationalState"], list[Union[dict, "ConformationalState"]]]] = empty_list()
    clustering_method: Optional[str] = None
    rmsd_threshold: Optional[float] = None
    transition_pathways: Optional[str] = None
    energy_landscape: Optional[str] = None
    principal_motions: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ConformationalEnsembleId):
            self.id = ConformationalEnsembleId(self.id)

        if self._is_empty(self.protein_id):
            self.MissingRequiredField("protein_id")
        if not isinstance(self.protein_id, str):
            self.protein_id = str(self.protein_id)

        if not isinstance(self.conformational_states, list):
            self.conformational_states = [self.conformational_states] if self.conformational_states is not None else []
        self.conformational_states = [v if isinstance(v, ConformationalState) else ConformationalState(**as_dict(v)) for v in self.conformational_states]

        if self.clustering_method is not None and not isinstance(self.clustering_method, str):
            self.clustering_method = str(self.clustering_method)

        if self.rmsd_threshold is not None and not isinstance(self.rmsd_threshold, float):
            self.rmsd_threshold = float(self.rmsd_threshold)

        if self.transition_pathways is not None and not isinstance(self.transition_pathways, str):
            self.transition_pathways = str(self.transition_pathways)

        if self.energy_landscape is not None and not isinstance(self.energy_landscape, str):
            self.energy_landscape = str(self.energy_landscape)

        if not isinstance(self.principal_motions, list):
            self.principal_motions = [self.principal_motions] if self.principal_motions is not None else []
        self.principal_motions = [v if isinstance(v, str) else str(v) for v in self.principal_motions]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ConformationalState(AttributeGroup):
    """
    Individual conformational state
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["functional_annotation/ConformationalState"]
    class_class_curie: ClassVar[str] = "aimsleaf:functional_annotation/ConformationalState"
    class_name: ClassVar[str] = "ConformationalState"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.ConformationalState

    state_id: str = None
    state_name: Optional[str] = None
    pdb_entries: Optional[Union[str, list[str]]] = empty_list()
    population: Optional[float] = None
    free_energy: Optional[float] = None
    rmsd_from_reference: Optional[float] = None
    characteristic_features: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.state_id):
            self.MissingRequiredField("state_id")
        if not isinstance(self.state_id, str):
            self.state_id = str(self.state_id)

        if self.state_name is not None and not isinstance(self.state_name, str):
            self.state_name = str(self.state_name)

        if not isinstance(self.pdb_entries, list):
            self.pdb_entries = [self.pdb_entries] if self.pdb_entries is not None else []
        self.pdb_entries = [v if isinstance(v, str) else str(v) for v in self.pdb_entries]

        if self.population is not None and not isinstance(self.population, float):
            self.population = float(self.population)

        if self.free_energy is not None and not isinstance(self.free_energy, float):
            self.free_energy = float(self.free_energy)

        if self.rmsd_from_reference is not None and not isinstance(self.rmsd_from_reference, float):
            self.rmsd_from_reference = float(self.rmsd_from_reference)

        if not isinstance(self.characteristic_features, list):
            self.characteristic_features = [self.characteristic_features] if self.characteristic_features is not None else []
        self.characteristic_features = [v if isinstance(v, str) else str(v) for v in self.characteristic_features]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PostTranslationalModification(ProteinAnnotation):
    """
    Post-translational modifications observed or predicted
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["functional_annotation/PostTranslationalModification"]
    class_class_curie: ClassVar[str] = "aimsleaf:functional_annotation/PostTranslationalModification"
    class_name: ClassVar[str] = "PostTranslationalModification"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.PostTranslationalModification

    id: Union[str, PostTranslationalModificationId] = None
    protein_id: str = None
    modification_type: Union[str, "PTMTypeEnum"] = None
    modified_residue: str = None
    modification_group: Optional[str] = None
    mass_shift: Optional[float] = None
    functional_effect: Optional[str] = None
    regulatory_role: Optional[str] = None
    enzyme: Optional[str] = None
    removal_enzyme: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PostTranslationalModificationId):
            self.id = PostTranslationalModificationId(self.id)

        if self._is_empty(self.modification_type):
            self.MissingRequiredField("modification_type")
        if not isinstance(self.modification_type, PTMTypeEnum):
            self.modification_type = PTMTypeEnum(self.modification_type)

        if self._is_empty(self.modified_residue):
            self.MissingRequiredField("modified_residue")
        if not isinstance(self.modified_residue, str):
            self.modified_residue = str(self.modified_residue)

        if self.modification_group is not None and not isinstance(self.modification_group, str):
            self.modification_group = str(self.modification_group)

        if self.mass_shift is not None and not isinstance(self.mass_shift, float):
            self.mass_shift = float(self.mass_shift)

        if self.functional_effect is not None and not isinstance(self.functional_effect, str):
            self.functional_effect = str(self.functional_effect)

        if self.regulatory_role is not None and not isinstance(self.regulatory_role, str):
            self.regulatory_role = str(self.regulatory_role)

        if self.enzyme is not None and not isinstance(self.enzyme, str):
            self.enzyme = str(self.enzyme)

        if self.removal_enzyme is not None and not isinstance(self.removal_enzyme, str):
            self.removal_enzyme = str(self.removal_enzyme)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DatabaseCrossReference(AttributeGroup):
    """
    Cross-references to external databases
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["functional_annotation/DatabaseCrossReference"]
    class_class_curie: ClassVar[str] = "aimsleaf:functional_annotation/DatabaseCrossReference"
    class_name: ClassVar[str] = "DatabaseCrossReference"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.DatabaseCrossReference

    database_name: Union[str, "DatabaseNameEnum"] = None
    database_id: str = None
    database_url: Optional[Union[str, URI]] = None
    last_updated: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.database_name):
            self.MissingRequiredField("database_name")
        if not isinstance(self.database_name, DatabaseNameEnum):
            self.database_name = DatabaseNameEnum(self.database_name)

        if self._is_empty(self.database_id):
            self.MissingRequiredField("database_id")
        if not isinstance(self.database_id, str):
            self.database_id = str(self.database_id)

        if self.database_url is not None and not isinstance(self.database_url, URI):
            self.database_url = URI(self.database_url)

        if self.last_updated is not None and not isinstance(self.last_updated, str):
            self.last_updated = str(self.last_updated)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EvolutionaryConservation(ProteinAnnotation):
    """
    Evolutionary conservation information
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["functional_annotation/EvolutionaryConservation"]
    class_class_curie: ClassVar[str] = "aimsleaf:functional_annotation/EvolutionaryConservation"
    class_name: ClassVar[str] = "EvolutionaryConservation"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.EvolutionaryConservation

    id: Union[str, EvolutionaryConservationId] = None
    protein_id: str = None
    conservation_score: Optional[float] = None
    conserved_residues: Optional[Union[str, list[str]]] = empty_list()
    variable_residues: Optional[Union[str, list[str]]] = empty_list()
    conservation_method: Optional[str] = None
    alignment_depth: Optional[int] = None
    taxonomic_range: Optional[str] = None
    coevolved_residues: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EvolutionaryConservationId):
            self.id = EvolutionaryConservationId(self.id)

        if self.conservation_score is not None and not isinstance(self.conservation_score, float):
            self.conservation_score = float(self.conservation_score)

        if not isinstance(self.conserved_residues, list):
            self.conserved_residues = [self.conserved_residues] if self.conserved_residues is not None else []
        self.conserved_residues = [v if isinstance(v, str) else str(v) for v in self.conserved_residues]

        if not isinstance(self.variable_residues, list):
            self.variable_residues = [self.variable_residues] if self.variable_residues is not None else []
        self.variable_residues = [v if isinstance(v, str) else str(v) for v in self.variable_residues]

        if self.conservation_method is not None and not isinstance(self.conservation_method, str):
            self.conservation_method = str(self.conservation_method)

        if self.alignment_depth is not None and not isinstance(self.alignment_depth, int):
            self.alignment_depth = int(self.alignment_depth)

        if self.taxonomic_range is not None and not isinstance(self.taxonomic_range, str):
            self.taxonomic_range = str(self.taxonomic_range)

        if not isinstance(self.coevolved_residues, list):
            self.coevolved_residues = [self.coevolved_residues] if self.coevolved_residues is not None else []
        self.coevolved_residues = [v if isinstance(v, str) else str(v) for v in self.coevolved_residues]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AggregatedProteinView(NamedThing):
    """
    Aggregated view of all structural and functional data for a protein
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["functional_annotation/AggregatedProteinView"]
    class_class_curie: ClassVar[str] = "aimsleaf:functional_annotation/AggregatedProteinView"
    class_name: ClassVar[str] = "AggregatedProteinView"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.AggregatedProteinView

    id: Union[str, AggregatedProteinViewId] = None
    uniprot_id: str = None
    protein_name: str = None
    organism: Optional[str] = None
    organism_id: Optional[int] = None
    pdb_entries: Optional[Union[str, list[str]]] = empty_list()
    functional_sites: Optional[Union[dict[Union[str, FunctionalSiteId], Union[dict, FunctionalSite]], list[Union[dict, FunctionalSite]]]] = empty_dict()
    structural_features: Optional[Union[dict[Union[str, StructuralFeatureId], Union[dict, StructuralFeature]], list[Union[dict, StructuralFeature]]]] = empty_dict()
    protein_interactions: Optional[Union[dict[Union[str, ProteinProteinInteractionId], Union[dict, ProteinProteinInteraction]], list[Union[dict, ProteinProteinInteraction]]]] = empty_dict()
    ligand_interactions: Optional[Union[Union[dict, LigandInteraction], list[Union[dict, LigandInteraction]]]] = empty_list()
    mutations: Optional[Union[dict[Union[str, MutationEffectId], Union[dict, MutationEffect]], list[Union[dict, MutationEffect]]]] = empty_dict()
    ptms: Optional[Union[dict[Union[str, PostTranslationalModificationId], Union[dict, PostTranslationalModification]], list[Union[dict, PostTranslationalModification]]]] = empty_dict()
    biophysical_properties: Optional[Union[Union[dict, BiophysicalProperty], list[Union[dict, BiophysicalProperty]]]] = empty_list()
    conformational_ensemble: Optional[Union[dict, ConformationalEnsemble]] = None
    evolutionary_conservation: Optional[Union[dict, EvolutionaryConservation]] = None
    cross_references: Optional[Union[Union[dict, DatabaseCrossReference], list[Union[dict, DatabaseCrossReference]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AggregatedProteinViewId):
            self.id = AggregatedProteinViewId(self.id)

        if self._is_empty(self.uniprot_id):
            self.MissingRequiredField("uniprot_id")
        if not isinstance(self.uniprot_id, str):
            self.uniprot_id = str(self.uniprot_id)

        if self._is_empty(self.protein_name):
            self.MissingRequiredField("protein_name")
        if not isinstance(self.protein_name, str):
            self.protein_name = str(self.protein_name)

        if self.organism is not None and not isinstance(self.organism, str):
            self.organism = str(self.organism)

        if self.organism_id is not None and not isinstance(self.organism_id, int):
            self.organism_id = int(self.organism_id)

        if not isinstance(self.pdb_entries, list):
            self.pdb_entries = [self.pdb_entries] if self.pdb_entries is not None else []
        self.pdb_entries = [v if isinstance(v, str) else str(v) for v in self.pdb_entries]

        self._normalize_inlined_as_list(slot_name="functional_sites", slot_type=FunctionalSite, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="structural_features", slot_type=StructuralFeature, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="protein_interactions", slot_type=ProteinProteinInteraction, key_name="id", keyed=True)

        if not isinstance(self.ligand_interactions, list):
            self.ligand_interactions = [self.ligand_interactions] if self.ligand_interactions is not None else []
        self.ligand_interactions = [v if isinstance(v, LigandInteraction) else LigandInteraction(**as_dict(v)) for v in self.ligand_interactions]

        self._normalize_inlined_as_list(slot_name="mutations", slot_type=MutationEffect, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ptms", slot_type=PostTranslationalModification, key_name="id", keyed=True)

        if not isinstance(self.biophysical_properties, list):
            self.biophysical_properties = [self.biophysical_properties] if self.biophysical_properties is not None else []
        self.biophysical_properties = [v if isinstance(v, BiophysicalProperty) else BiophysicalProperty(**as_dict(v)) for v in self.biophysical_properties]

        if self.conformational_ensemble is not None and not isinstance(self.conformational_ensemble, ConformationalEnsemble):
            self.conformational_ensemble = ConformationalEnsemble(**as_dict(self.conformational_ensemble))

        if self.evolutionary_conservation is not None and not isinstance(self.evolutionary_conservation, EvolutionaryConservation):
            self.evolutionary_conservation = EvolutionaryConservation(**as_dict(self.evolutionary_conservation))

        if not isinstance(self.cross_references, list):
            self.cross_references = [self.cross_references] if self.cross_references is not None else []
        self.cross_references = [v if isinstance(v, DatabaseCrossReference) else DatabaseCrossReference(**as_dict(v)) for v in self.cross_references]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MeasurementConditions(NamedThing):
    """
    Conditions under which biophysical measurements were made
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSLEAF["functional_annotation/MeasurementConditions"]
    class_class_curie: ClassVar[str] = "aimsleaf:functional_annotation/MeasurementConditions"
    class_name: ClassVar[str] = "MeasurementConditions"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.MeasurementConditions

    id: Union[str, MeasurementConditionsId] = None
    buffer_composition: Optional[Union[dict, BufferComposition]] = None
    ph: Optional[Union[dict, QuantityValue]] = None
    ionic_strength: Optional[Union[dict, QuantityValue]] = None
    temperature: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MeasurementConditionsId):
            self.id = MeasurementConditionsId(self.id)

        if self.buffer_composition is not None and not isinstance(self.buffer_composition, BufferComposition):
            self.buffer_composition = BufferComposition(**as_dict(self.buffer_composition))

        if self.ph is not None and not isinstance(self.ph, QuantityValue):
            self.ph = QuantityValue(**as_dict(self.ph))

        if self.ionic_strength is not None and not isinstance(self.ionic_strength, QuantityValue):
            self.ionic_strength = QuantityValue(**as_dict(self.ionic_strength))

        if self.temperature is not None and not isinstance(self.temperature, QuantityValue):
            self.temperature = QuantityValue(**as_dict(self.temperature))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PlantSample(Sample):
    """
    Plant sample info for AIMS-LEAF
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSPLANT["PlantSample"]
    class_class_curie: ClassVar[str] = "aimsplant:PlantSample"
    class_name: ClassVar[str] = "PlantSample"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.PlantSample

    id: Union[str, PlantSampleId] = None
    sample_code: str = None
    sample_type: Union[str, "SampleTypeEnum"] = None
    genus: str = None
    species: str = None
    collection_date_time: str = None
    tissue: str = None
    growth_facility: Union[str, "GrowthFacilityEnum"] = None
    growth_medium: str = None
    developmental_stage: str = None
    biological_replicate_sample_group_name: Optional[str] = None
    combined_tissue_description: Optional[str] = None
    experimental_time_point_number: Optional[int] = None
    experimental_time_point_description: Optional[str] = None
    strain_variety_cultivar: Optional[str] = None
    isolate: Optional[str] = None
    germplasm_collection_id: Optional[str] = None
    ncbi_taxonomy_id: Optional[int] = None
    ancestral_data: Optional[str] = None
    genetic_modification: Optional[str] = None
    estimated_genome_size_mb: Optional[Union[dict, QuantityValue]] = None
    gc_content_percent: Optional[Union[dict, QuantityValue]] = None
    ploidy: Optional[Union[str, "PloidyTypeEnum"]] = None
    reference_genome: Optional[str] = None
    sample_size: Optional[Union[dict, QuantityValue]] = None
    tissue_plant_ontology_term: Optional[str] = None
    region_locality: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    depth_meters: Optional[Union[dict, QuantityValue]] = None
    elevation_meters: Optional[Union[dict, QuantityValue]] = None
    temperature: Optional[Union[dict, QuantityValue]] = None
    broad_scale_environmental_context: Optional[str] = None
    local_environmental_context: Optional[str] = None
    environmental_medium: Optional[str] = None
    growth_medium_composition: Optional[str] = None
    plant_age: Optional[str] = None
    arabadopsis_phenotype_stage: Optional[Union[str, "ArabadopsisStageEnum"]] = None
    air_temperature_regimen: Optional[str] = None
    antibiotic_regimen: Optional[str] = None
    biotic_regimen: Optional[str] = None
    inoculation_method: Optional[str] = None
    time_post_inoculation: Optional[str] = None
    chemical_administration: Optional[str] = None
    chemical_mutagen: Optional[str] = None
    fertilizer_administration: Optional[str] = None
    insecticide_regimen: Optional[str] = None
    fungicide_regimen: Optional[str] = None
    gaseous_environment: Optional[str] = None
    growth_hormone_regimen: Optional[str] = None
    herbicide_regimen: Optional[str] = None
    humidity_regimen: Optional[str] = None
    radiation_regimen: Optional[str] = None
    light_regimen: Optional[str] = None
    last_light_transition_type: Optional[str] = None
    time_after_last_light_transition: Optional[str] = None
    salt_regimen: Optional[str] = None
    rainfall_regimen: Optional[str] = None
    watering_regimen: Optional[str] = None
    other_treatment_regimen: Optional[str] = None
    perturbation: Optional[str] = None
    mechanical_damage: Optional[str] = None
    observed_host_symbionts: Optional[str] = None
    plant_sex: Optional[str] = None
    sample_disease_staus: Optional[str] = None
    sample_disease_stage: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlantSampleId):
            self.id = PlantSampleId(self.id)

        if self._is_empty(self.genus):
            self.MissingRequiredField("genus")
        if not isinstance(self.genus, str):
            self.genus = str(self.genus)

        if self._is_empty(self.species):
            self.MissingRequiredField("species")
        if not isinstance(self.species, str):
            self.species = str(self.species)

        if self._is_empty(self.collection_date_time):
            self.MissingRequiredField("collection_date_time")
        if not isinstance(self.collection_date_time, str):
            self.collection_date_time = str(self.collection_date_time)

        if self._is_empty(self.tissue):
            self.MissingRequiredField("tissue")
        if not isinstance(self.tissue, str):
            self.tissue = str(self.tissue)

        if self._is_empty(self.growth_facility):
            self.MissingRequiredField("growth_facility")
        if not isinstance(self.growth_facility, GrowthFacilityEnum):
            self.growth_facility = GrowthFacilityEnum(self.growth_facility)

        if self._is_empty(self.growth_medium):
            self.MissingRequiredField("growth_medium")
        if not isinstance(self.growth_medium, str):
            self.growth_medium = str(self.growth_medium)

        if self._is_empty(self.developmental_stage):
            self.MissingRequiredField("developmental_stage")
        if not isinstance(self.developmental_stage, str):
            self.developmental_stage = str(self.developmental_stage)

        if self.biological_replicate_sample_group_name is not None and not isinstance(self.biological_replicate_sample_group_name, str):
            self.biological_replicate_sample_group_name = str(self.biological_replicate_sample_group_name)

        if self.combined_tissue_description is not None and not isinstance(self.combined_tissue_description, str):
            self.combined_tissue_description = str(self.combined_tissue_description)

        if self.experimental_time_point_number is not None and not isinstance(self.experimental_time_point_number, int):
            self.experimental_time_point_number = int(self.experimental_time_point_number)

        if self.experimental_time_point_description is not None and not isinstance(self.experimental_time_point_description, str):
            self.experimental_time_point_description = str(self.experimental_time_point_description)

        if self.strain_variety_cultivar is not None and not isinstance(self.strain_variety_cultivar, str):
            self.strain_variety_cultivar = str(self.strain_variety_cultivar)

        if self.isolate is not None and not isinstance(self.isolate, str):
            self.isolate = str(self.isolate)

        if self.germplasm_collection_id is not None and not isinstance(self.germplasm_collection_id, str):
            self.germplasm_collection_id = str(self.germplasm_collection_id)

        if self.ncbi_taxonomy_id is not None and not isinstance(self.ncbi_taxonomy_id, int):
            self.ncbi_taxonomy_id = int(self.ncbi_taxonomy_id)

        if self.ancestral_data is not None and not isinstance(self.ancestral_data, str):
            self.ancestral_data = str(self.ancestral_data)

        if self.genetic_modification is not None and not isinstance(self.genetic_modification, str):
            self.genetic_modification = str(self.genetic_modification)

        if self.estimated_genome_size_mb is not None and not isinstance(self.estimated_genome_size_mb, QuantityValue):
            self.estimated_genome_size_mb = QuantityValue(**as_dict(self.estimated_genome_size_mb))

        if self.gc_content_percent is not None and not isinstance(self.gc_content_percent, QuantityValue):
            self.gc_content_percent = QuantityValue(**as_dict(self.gc_content_percent))

        if self.ploidy is not None and not isinstance(self.ploidy, PloidyTypeEnum):
            self.ploidy = PloidyTypeEnum(self.ploidy)

        if self.reference_genome is not None and not isinstance(self.reference_genome, str):
            self.reference_genome = str(self.reference_genome)

        if self.sample_size is not None and not isinstance(self.sample_size, QuantityValue):
            self.sample_size = QuantityValue(**as_dict(self.sample_size))

        if self.tissue_plant_ontology_term is not None and not isinstance(self.tissue_plant_ontology_term, str):
            self.tissue_plant_ontology_term = str(self.tissue_plant_ontology_term)

        if self.region_locality is not None and not isinstance(self.region_locality, str):
            self.region_locality = str(self.region_locality)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.depth_meters is not None and not isinstance(self.depth_meters, QuantityValue):
            self.depth_meters = QuantityValue(**as_dict(self.depth_meters))

        if self.elevation_meters is not None and not isinstance(self.elevation_meters, QuantityValue):
            self.elevation_meters = QuantityValue(**as_dict(self.elevation_meters))

        if self.temperature is not None and not isinstance(self.temperature, QuantityValue):
            self.temperature = QuantityValue(**as_dict(self.temperature))

        if self.broad_scale_environmental_context is not None and not isinstance(self.broad_scale_environmental_context, str):
            self.broad_scale_environmental_context = str(self.broad_scale_environmental_context)

        if self.local_environmental_context is not None and not isinstance(self.local_environmental_context, str):
            self.local_environmental_context = str(self.local_environmental_context)

        if self.environmental_medium is not None and not isinstance(self.environmental_medium, str):
            self.environmental_medium = str(self.environmental_medium)

        if self.growth_medium_composition is not None and not isinstance(self.growth_medium_composition, str):
            self.growth_medium_composition = str(self.growth_medium_composition)

        if self.plant_age is not None and not isinstance(self.plant_age, str):
            self.plant_age = str(self.plant_age)

        if self.arabadopsis_phenotype_stage is not None and not isinstance(self.arabadopsis_phenotype_stage, ArabadopsisStageEnum):
            self.arabadopsis_phenotype_stage = ArabadopsisStageEnum(self.arabadopsis_phenotype_stage)

        if self.air_temperature_regimen is not None and not isinstance(self.air_temperature_regimen, str):
            self.air_temperature_regimen = str(self.air_temperature_regimen)

        if self.antibiotic_regimen is not None and not isinstance(self.antibiotic_regimen, str):
            self.antibiotic_regimen = str(self.antibiotic_regimen)

        if self.biotic_regimen is not None and not isinstance(self.biotic_regimen, str):
            self.biotic_regimen = str(self.biotic_regimen)

        if self.inoculation_method is not None and not isinstance(self.inoculation_method, str):
            self.inoculation_method = str(self.inoculation_method)

        if self.time_post_inoculation is not None and not isinstance(self.time_post_inoculation, str):
            self.time_post_inoculation = str(self.time_post_inoculation)

        if self.chemical_administration is not None and not isinstance(self.chemical_administration, str):
            self.chemical_administration = str(self.chemical_administration)

        if self.chemical_mutagen is not None and not isinstance(self.chemical_mutagen, str):
            self.chemical_mutagen = str(self.chemical_mutagen)

        if self.fertilizer_administration is not None and not isinstance(self.fertilizer_administration, str):
            self.fertilizer_administration = str(self.fertilizer_administration)

        if self.insecticide_regimen is not None and not isinstance(self.insecticide_regimen, str):
            self.insecticide_regimen = str(self.insecticide_regimen)

        if self.fungicide_regimen is not None and not isinstance(self.fungicide_regimen, str):
            self.fungicide_regimen = str(self.fungicide_regimen)

        if self.gaseous_environment is not None and not isinstance(self.gaseous_environment, str):
            self.gaseous_environment = str(self.gaseous_environment)

        if self.growth_hormone_regimen is not None and not isinstance(self.growth_hormone_regimen, str):
            self.growth_hormone_regimen = str(self.growth_hormone_regimen)

        if self.herbicide_regimen is not None and not isinstance(self.herbicide_regimen, str):
            self.herbicide_regimen = str(self.herbicide_regimen)

        if self.humidity_regimen is not None and not isinstance(self.humidity_regimen, str):
            self.humidity_regimen = str(self.humidity_regimen)

        if self.radiation_regimen is not None and not isinstance(self.radiation_regimen, str):
            self.radiation_regimen = str(self.radiation_regimen)

        if self.light_regimen is not None and not isinstance(self.light_regimen, str):
            self.light_regimen = str(self.light_regimen)

        if self.last_light_transition_type is not None and not isinstance(self.last_light_transition_type, str):
            self.last_light_transition_type = str(self.last_light_transition_type)

        if self.time_after_last_light_transition is not None and not isinstance(self.time_after_last_light_transition, str):
            self.time_after_last_light_transition = str(self.time_after_last_light_transition)

        if self.salt_regimen is not None and not isinstance(self.salt_regimen, str):
            self.salt_regimen = str(self.salt_regimen)

        if self.rainfall_regimen is not None and not isinstance(self.rainfall_regimen, str):
            self.rainfall_regimen = str(self.rainfall_regimen)

        if self.watering_regimen is not None and not isinstance(self.watering_regimen, str):
            self.watering_regimen = str(self.watering_regimen)

        if self.other_treatment_regimen is not None and not isinstance(self.other_treatment_regimen, str):
            self.other_treatment_regimen = str(self.other_treatment_regimen)

        if self.perturbation is not None and not isinstance(self.perturbation, str):
            self.perturbation = str(self.perturbation)

        if self.mechanical_damage is not None and not isinstance(self.mechanical_damage, str):
            self.mechanical_damage = str(self.mechanical_damage)

        if self.observed_host_symbionts is not None and not isinstance(self.observed_host_symbionts, str):
            self.observed_host_symbionts = str(self.observed_host_symbionts)

        if self.plant_sex is not None and not isinstance(self.plant_sex, str):
            self.plant_sex = str(self.plant_sex)

        if self.sample_disease_staus is not None and not isinstance(self.sample_disease_staus, str):
            self.sample_disease_staus = str(self.sample_disease_staus)

        if self.sample_disease_stage is not None and not isinstance(self.sample_disease_stage, str):
            self.sample_disease_stage = str(self.sample_disease_stage)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PlantSamplePreparation(SamplePreparation):
    """
    A process that prepares a plant sample for analysis
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = AIMSPLANT["PlantSamplePreparation"]
    class_class_curie: ClassVar[str] = "aimsplant:PlantSamplePreparation"
    class_name: ClassVar[str] = "PlantSamplePreparation"
    class_model_uri: ClassVar[URIRef] = AIMSLEAF.PlantSamplePreparation

    id: Union[str, PlantSamplePreparationId] = None
    preparation_type: Union[str, "PreparationTypeEnum"] = None
    support_type: str = None
    sample_material_processing: Optional[str] = None
    sample_storage_temperature: Optional[Union[dict, QuantityValue]] = None
    sample_preservation_method: Optional[Union[str, "SamplePreservationEnum"]] = None
    harvest_to_preservation_time: Optional[Union[dict, QuantityValue]] = None
    embedding_material: Optional[str] = None
    plane_of_section: Optional[str] = None
    section_thickness: Optional[Union[dict, QuantityValue]] = None
    support_thickness: Optional[Union[dict, QuantityValue]] = None
    adhesive: Optional[str] = None
    top_layer: Optional[str] = None
    top_layer_thickness: Optional[Union[dict, QuantityValue]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlantSamplePreparationId):
            self.id = PlantSamplePreparationId(self.id)

        if self._is_empty(self.support_type):
            self.MissingRequiredField("support_type")
        if not isinstance(self.support_type, str):
            self.support_type = str(self.support_type)

        if self.sample_material_processing is not None and not isinstance(self.sample_material_processing, str):
            self.sample_material_processing = str(self.sample_material_processing)

        if self.sample_storage_temperature is not None and not isinstance(self.sample_storage_temperature, QuantityValue):
            self.sample_storage_temperature = QuantityValue(**as_dict(self.sample_storage_temperature))

        if self.sample_preservation_method is not None and not isinstance(self.sample_preservation_method, SamplePreservationEnum):
            self.sample_preservation_method = SamplePreservationEnum(self.sample_preservation_method)

        if self.harvest_to_preservation_time is not None and not isinstance(self.harvest_to_preservation_time, QuantityValue):
            self.harvest_to_preservation_time = QuantityValue(**as_dict(self.harvest_to_preservation_time))

        if self.embedding_material is not None and not isinstance(self.embedding_material, str):
            self.embedding_material = str(self.embedding_material)

        if self.plane_of_section is not None and not isinstance(self.plane_of_section, str):
            self.plane_of_section = str(self.plane_of_section)

        if self.section_thickness is not None and not isinstance(self.section_thickness, QuantityValue):
            self.section_thickness = QuantityValue(**as_dict(self.section_thickness))

        if self.support_thickness is not None and not isinstance(self.support_thickness, QuantityValue):
            self.support_thickness = QuantityValue(**as_dict(self.support_thickness))

        if self.adhesive is not None and not isinstance(self.adhesive, str):
            self.adhesive = str(self.adhesive)

        if self.top_layer is not None and not isinstance(self.top_layer, str):
            self.top_layer = str(self.top_layer)

        if self.top_layer_thickness is not None and not isinstance(self.top_layer_thickness, QuantityValue):
            self.top_layer_thickness = QuantityValue(**as_dict(self.top_layer_thickness))

        super().__post_init__(**kwargs)


# Enumerations
class FacilityEnum(EnumDefinitionImpl):
    """
    Major synchrotron and structural biology research facilities worldwide
    """
    NSLS_II = PermissibleValue(
        text="NSLS_II",
        title="National Synchrotron Light Source II",
        description="Fourth-generation synchrotron light source at Brookhaven National Laboratory, Upton, NY, USA",
        meaning=ROR["01q47ea17"])
    ALS = PermissibleValue(
        text="ALS",
        title="Advanced Light Source",
        description="""Third-generation synchrotron light source at Lawrence Berkeley National Laboratory, Berkeley, CA, USA""",
        meaning=ROR["02jbv0t02"])
    SSRL = PermissibleValue(
        text="SSRL",
        title="Stanford Synchrotron Radiation Lightsource",
        description="Synchrotron radiation facility at SLAC National Accelerator Laboratory, Menlo Park, CA, USA",
        meaning=ROR["05gzmn429"])
    ESRF = PermissibleValue(
        text="ESRF",
        title="European Synchrotron Radiation Facility",
        description="High-energy synchrotron facility in Grenoble, France - world's most intense X-ray source",
        meaning=ROR["02550n020"])
    DIAMOND = PermissibleValue(
        text="DIAMOND",
        title="Diamond Light Source",
        description="""UK's national synchrotron science facility at Harwell Science and Innovation Campus, Oxfordshire, UK""",
        meaning=ROR["05etxs293"])
    PHOTON_FACTORY = PermissibleValue(
        text="PHOTON_FACTORY",
        title="Photon Factory",
        description="""Synchrotron radiation facility at KEK (High Energy Accelerator Research Organization), Tsukuba, Japan""",
        meaning=ROR["01g5y5k24"])
    APS = PermissibleValue(
        text="APS",
        title="Advanced Photon Source",
        description="High-energy synchrotron at Argonne National Laboratory, Lemont, IL, USA",
        meaning=ROR["05gvnxz63"])
    SPRING8 = PermissibleValue(
        text="SPRING8",
        title="SPring-8",
        description="Large-scale synchrotron radiation facility in Harima Science Park City, Hyogo, Japan",
        meaning=ROR["01xjv7358"])
    PETRA_III = PermissibleValue(
        text="PETRA_III",
        title="PETRA III",
        description="High-brilliance synchrotron radiation source at DESY, Hamburg, Germany",
        meaning=ROR["01js2sh04"])
    SOLEIL = PermissibleValue(
        text="SOLEIL",
        title="Synchrotron SOLEIL",
        description="French national synchrotron facility near Paris, France",
        meaning=ROR["01ydb3330"])
    AUSTRALIAN_SYNCHROTRON = PermissibleValue(
        text="AUSTRALIAN_SYNCHROTRON",
        title="Australian Synchrotron",
        description="Australia's national synchrotron facility in Melbourne, Victoria",
        meaning=ROR["03vk18a84"])
    EMSL = PermissibleValue(
        text="EMSL",
        title="Environmental Molecular Sciences Laboratory",
        description="DOE Office of Science user facility at PNNL with cryo-EM capabilities",
        meaning=ROR["05h992307"])
    SNS = PermissibleValue(
        text="SNS",
        title="Spallation Neutron Source",
        description="Accelerator-based pulsed neutron source at ORNL providing intense neutron beams",
        meaning=ROR["01qz5mb56"])
    HFIR = PermissibleValue(
        text="HFIR",
        title="High Flux Isotope Reactor",
        description="Reactor-based neutron source at ORNL with dedicated biology beamlines",
        meaning=ROR["01qz5mb56"])

    _defn = EnumDefinition(
        name="FacilityEnum",
        description="Major synchrotron and structural biology research facilities worldwide",
    )

class SampleTypeEnum(EnumDefinitionImpl):
    """
    Types of biological samples
    """
    protein = PermissibleValue(
        text="protein",
        description="Protein sample")
    nucleic_acid = PermissibleValue(
        text="nucleic_acid",
        description="Nucleic acid sample (DNA or RNA)")
    complex = PermissibleValue(
        text="complex",
        description="Protein-protein or protein-nucleic acid complex")
    membrane_protein = PermissibleValue(
        text="membrane_protein",
        description="Membrane protein sample")
    virus = PermissibleValue(
        text="virus",
        description="Viral particle")
    organelle = PermissibleValue(
        text="organelle",
        description="Cellular organelle")
    tissue_section = PermissibleValue(
        text="tissue_section",
        description="Tissue section sample")
    tissue = PermissibleValue(
        text="tissue",
        description="Tissue sample")
    organism = PermissibleValue(
        text="organism",
        description="Whole organism")
    soil = PermissibleValue(
        text="soil",
        description="Soil sample")
    rock = PermissibleValue(
        text="rock",
        description="Rock sample")

    _defn = EnumDefinition(
        name="SampleTypeEnum",
        description="Types of biological samples",
    )

class PreparationTypeEnum(EnumDefinitionImpl):
    """
    Types of sample preparation
    """
    cryo_em = PermissibleValue(
        text="cryo_em",
        description="Cryo-EM preparation")
    xray_crystallography = PermissibleValue(
        text="xray_crystallography",
        description="X-ray crystallography preparation")
    saxs = PermissibleValue(
        text="saxs",
        description="SAXS/WAXS preparation")
    sans = PermissibleValue(
        text="sans",
        description="SANS preparation")
    protein_expression = PermissibleValue(
        text="protein_expression",
        description="Protein expression in host cells")
    protein_purification = PermissibleValue(
        text="protein_purification",
        description="Protein purification")
    negative_stain = PermissibleValue(
        text="negative_stain",
        description="Negative stain EM preparation")
    thin_section = PermissibleValue(
        text="thin_section",
        description="Petrographic thin-section preparation")
    thick_section = PermissibleValue(
        text="thick_section",
        description="Petrographic thick-section preparation")
    microtome_section = PermissibleValue(
        text="microtome_section",
        description="Microtome preparation")
    cryo_section = PermissibleValue(
        text="cryo_section",
        description="Cryo-section microtome preparation")
    ultratome_section = PermissibleValue(
        text="ultratome_section",
        description="Ultra-Microtome preparation")
    whole_mount = PermissibleValue(
        text="whole_mount",
        description="Whole mount of sample")
    other_mount = PermissibleValue(
        text="other_mount",
        description="Other mount of sample")

    _defn = EnumDefinition(
        name="PreparationTypeEnum",
        description="Types of sample preparation",
    )

class GridTypeEnum(EnumDefinitionImpl):
    """
    Types of EM grids
    """
    c_flat = PermissibleValue(
        text="c_flat",
        description="C-flat holey carbon grid")
    quantifoil = PermissibleValue(
        text="quantifoil",
        description="Quantifoil holey carbon grid")
    lacey_carbon = PermissibleValue(
        text="lacey_carbon",
        description="Lacey carbon grid")
    ultrathin_carbon = PermissibleValue(
        text="ultrathin_carbon",
        description="Ultrathin carbon film")
    gold = PermissibleValue(
        text="gold",
        description="Gold grid")

    _defn = EnumDefinition(
        name="GridTypeEnum",
        description="Types of EM grids",
    )

class GridMaterialEnum(EnumDefinitionImpl):
    """
    Materials used for EM grids
    """
    carbon = PermissibleValue(
        text="carbon",
        description="Carbon grid")
    gold = PermissibleValue(
        text="gold",
        description="Gold grid")
    graphene = PermissibleValue(
        text="graphene",
        description="Graphene grid")
    silicon_nitride = PermissibleValue(
        text="silicon_nitride",
        description="Silicon nitride grid")

    _defn = EnumDefinition(
        name="GridMaterialEnum",
        description="Materials used for EM grids",
    )

class VitrificationMethodEnum(EnumDefinitionImpl):
    """
    Methods for vitrification
    """
    plunge_freezing = PermissibleValue(
        text="plunge_freezing",
        description="Plunge freezing in liquid ethane")
    high_pressure_freezing = PermissibleValue(
        text="high_pressure_freezing",
        description="High pressure freezing")
    slam_freezing = PermissibleValue(
        text="slam_freezing",
        description="Slam freezing")

    _defn = EnumDefinition(
        name="VitrificationMethodEnum",
        description="Methods for vitrification",
    )

class SymmetryEnum(EnumDefinitionImpl):
    """
    Crystallographic and non-crystallographic symmetry groups for cryo-EM
    """
    C1 = PermissibleValue(
        text="C1",
        description="C1 symmetry (no symmetry)")
    C2 = PermissibleValue(
        text="C2",
        description="C2 cyclic symmetry (2-fold)")
    C3 = PermissibleValue(
        text="C3",
        description="C3 cyclic symmetry (3-fold)")
    C4 = PermissibleValue(
        text="C4",
        description="C4 cyclic symmetry (4-fold)")
    C5 = PermissibleValue(
        text="C5",
        description="C5 cyclic symmetry (5-fold)")
    C6 = PermissibleValue(
        text="C6",
        description="C6 cyclic symmetry (6-fold)")
    C7 = PermissibleValue(
        text="C7",
        description="C7 cyclic symmetry (7-fold)")
    C8 = PermissibleValue(
        text="C8",
        description="C8 cyclic symmetry (8-fold)")
    C9 = PermissibleValue(
        text="C9",
        description="C9 cyclic symmetry (9-fold)")
    C10 = PermissibleValue(
        text="C10",
        description="C10 cyclic symmetry (10-fold)")
    D2 = PermissibleValue(
        text="D2",
        description="D2 dihedral symmetry (2-fold)")
    D3 = PermissibleValue(
        text="D3",
        description="D3 dihedral symmetry (3-fold)")
    D4 = PermissibleValue(
        text="D4",
        description="D4 dihedral symmetry (4-fold)")
    D5 = PermissibleValue(
        text="D5",
        description="D5 dihedral symmetry (5-fold)")
    D6 = PermissibleValue(
        text="D6",
        description="D6 dihedral symmetry (6-fold)")
    D7 = PermissibleValue(
        text="D7",
        description="D7 dihedral symmetry (7-fold)")
    D8 = PermissibleValue(
        text="D8",
        description="D8 dihedral symmetry (8-fold)")
    D9 = PermissibleValue(
        text="D9",
        description="D9 dihedral symmetry (9-fold)")
    D10 = PermissibleValue(
        text="D10",
        description="D10 dihedral symmetry (10-fold)")
    T = PermissibleValue(
        text="T",
        description="Tetrahedral symmetry")
    O = PermissibleValue(
        text="O",
        description="Octahedral symmetry")
    I = PermissibleValue(
        text="I",
        description="Icosahedral symmetry")

    _defn = EnumDefinition(
        name="SymmetryEnum",
        description="Crystallographic and non-crystallographic symmetry groups for cryo-EM",
    )

class CrystallizationMethodEnum(EnumDefinitionImpl):
    """
    Methods for protein crystallization
    """
    vapor_diffusion_hanging = PermissibleValue(
        text="vapor_diffusion_hanging",
        description="Vapor diffusion hanging drop")
    vapor_diffusion_sitting = PermissibleValue(
        text="vapor_diffusion_sitting",
        description="Vapor diffusion sitting drop")
    batch = PermissibleValue(
        text="batch",
        description="Batch crystallization")
    microbatch = PermissibleValue(
        text="microbatch",
        description="Microbatch under oil")
    lcp = PermissibleValue(
        text="lcp",
        description="Lipidic cubic phase (LCP)")
    dialysis = PermissibleValue(
        text="dialysis",
        description="Dialysis method")
    free_interface_diffusion = PermissibleValue(
        text="free_interface_diffusion",
        description="Free interface diffusion")

    _defn = EnumDefinition(
        name="CrystallizationMethodEnum",
        description="Methods for protein crystallization",
    )

class InstrumentStatusEnum(EnumDefinitionImpl):
    """
    Operational status of instruments
    """
    operational = PermissibleValue(
        text="operational",
        description="Instrument is operational")
    maintenance = PermissibleValue(
        text="maintenance",
        description="Instrument under maintenance")
    offline = PermissibleValue(
        text="offline",
        description="Instrument is offline")
    commissioning = PermissibleValue(
        text="commissioning",
        description="Instrument being commissioned")

    _defn = EnumDefinition(
        name="InstrumentStatusEnum",
        description="Operational status of instruments",
    )

class InstrumentCategoryEnum(EnumDefinitionImpl):
    """
    Categories of instruments based on their nature and location
    """
    SYNCHROTRON_BEAMLINE = PermissibleValue(
        text="SYNCHROTRON_BEAMLINE",
        description="Beamline at a synchrotron light source",
        meaning=CHMO["0001084"])
    NEUTRON_BEAMLINE = PermissibleValue(
        text="NEUTRON_BEAMLINE",
        description="Beamline at a neutron source")
    XFEL_BEAMLINE = PermissibleValue(
        text="XFEL_BEAMLINE",
        description="Beamline at a free electron laser (X-ray FEL)")
    ELECTRON_MICROSCOPE = PermissibleValue(
        text="ELECTRON_MICROSCOPE",
        description="Electron microscope (TEM, SEM, cryo-EM)")
    BENCHTOP_XRAY = PermissibleValue(
        text="BENCHTOP_XRAY",
        description="Benchtop X-ray diffractometer or other laboratory X-ray source")
    OPTICAL_MICROSCOPE = PermissibleValue(
        text="OPTICAL_MICROSCOPE",
        description="Optical or fluorescence microscope")
    SPECTROMETER = PermissibleValue(
        text="SPECTROMETER",
        description="Spectroscopy instrument (FTIR, Raman, mass spec, etc.)")

    _defn = EnumDefinition(
        name="InstrumentCategoryEnum",
        description="Categories of instruments based on their nature and location",
    )

class FacilityTypeEnum(EnumDefinitionImpl):
    """
    Types of research facilities
    """
    SYNCHROTRON = PermissibleValue(
        text="SYNCHROTRON",
        description="Synchrotron light source facility")
    NEUTRON_SOURCE = PermissibleValue(
        text="NEUTRON_SOURCE",
        description="Neutron scattering facility (reactor or spallation source)")
    FREE_ELECTRON_LASER = PermissibleValue(
        text="FREE_ELECTRON_LASER",
        description="Free electron laser facility (XFEL)")
    CRYOEM_CENTER = PermissibleValue(
        text="CRYOEM_CENTER",
        description="Dedicated cryo-electron microscopy center")

    _defn = EnumDefinition(
        name="FacilityTypeEnum",
        description="Types of research facilities",
    )

class BeamlineEnum(EnumDefinitionImpl):
    """
    Specific beamline instances at DOE and other major structural biology facilities
    """
    ALS_SIBYLS = PermissibleValue(
        text="ALS_SIBYLS",
        title="SIBYLS (BL12.3.1)",
        description="""Structurally Integrated Biology for Life Sciences - dual SAXS/WAXS and macromolecular crystallography beamline""")
    ALS_BL501 = PermissibleValue(
        text="ALS_BL501",
        title="ALS BL5.0.1",
        description="Protein crystallography beamline at the Advanced Light Source")
    ALS_BL502 = PermissibleValue(
        text="ALS_BL502",
        title="ALS BL5.0.2",
        description="Protein crystallography beamline at the Advanced Light Source")
    ALS_BL821 = PermissibleValue(
        text="ALS_BL821",
        title="ALS BL8.2.1",
        description="Protein crystallography beamline at the Advanced Light Source")
    ALS_BL822 = PermissibleValue(
        text="ALS_BL822",
        title="ALS BL8.2.2",
        description="Protein crystallography beamline at the Advanced Light Source")
    ALS_BL831 = PermissibleValue(
        text="ALS_BL831",
        title="ALS BL8.3.1",
        description="High-throughput macromolecular crystallography beamline")
    ALS_BL832 = PermissibleValue(
        text="ALS_BL832",
        title="ALS BL8.3.2",
        description="""Hard X-ray micro-tomography beamline for non-destructive 3D imaging. Provides high-resolution micro-CT capabilities for biological, geological, and materials samples. Supports absorption and phase contrast imaging modes.""")
    ALS_BL1222 = PermissibleValue(
        text="ALS_BL1222",
        title="ALS BL12.2.2",
        description="High-throughput macromolecular crystallography beamline")
    NSLS2_FMX = PermissibleValue(
        text="NSLS2_FMX",
        title="FMX (17-ID-1)",
        description="Frontier Microfocus Macromolecular Crystallography beamline for challenging small crystals")
    NSLS2_AMX = PermissibleValue(
        text="NSLS2_AMX",
        title="AMX (17-ID-2)",
        description="Automated Macromolecular Crystallography beamline for high-throughput structure determination")
    NSLS2_NYX = PermissibleValue(
        text="NSLS2_NYX",
        title="NYX (19-ID)",
        description="Newest crystallography beamline for rapid data collection")
    NSLS2_LIX = PermissibleValue(
        text="NSLS2_LIX",
        title="LiX (16-ID)",
        description="Life Science X-ray Scattering beamline for solution SAXS/WAXS")
    APS_GMCA_23IDB = PermissibleValue(
        text="APS_GMCA_23IDB",
        title="GM/CA 23-ID-B",
        description="General Medical Sciences and Cancer Institutes Collaborative Access Team - microfocus beamline")
    APS_GMCA_23IDD = PermissibleValue(
        text="APS_GMCA_23IDD",
        title="GM/CA 23-ID-D",
        description="General Medical Sciences and Cancer Institutes Collaborative Access Team - standard beamline")
    APS_LSCAT_21ID = PermissibleValue(
        text="APS_LSCAT_21ID",
        title="LS-CAT (21-ID)",
        description="Life Sciences Collaborative Access Team beamline")
    APS_NECAT_24IDC = PermissibleValue(
        text="APS_NECAT_24IDC",
        title="NE-CAT 24-ID-C",
        description="Northeastern Collaborative Access Team - microfocus beamline")
    APS_NECAT_24IDE = PermissibleValue(
        text="APS_NECAT_24IDE",
        title="NE-CAT 24-ID-E",
        description="Northeastern Collaborative Access Team - standard beamline")
    APS_SERCAT_22ID = PermissibleValue(
        text="APS_SERCAT_22ID",
        title="SER-CAT (22-ID)",
        description="Southeast Regional Collaborative Access Team - insertion device beamline")
    APS_SERCAT_22BM = PermissibleValue(
        text="APS_SERCAT_22BM",
        title="SER-CAT (22-BM)",
        description="Southeast Regional Collaborative Access Team - bending magnet beamline")
    APS_SBCCAT_19ID = PermissibleValue(
        text="APS_SBCCAT_19ID",
        title="SBC-CAT (19-ID)",
        description="Structural Biology Center Collaborative Access Team beamline")
    APS_BIOCARS_14ID = PermissibleValue(
        text="APS_BIOCARS_14ID",
        title="BioCARS (14-ID)",
        description="Center for Advanced Radiation Sources - time-resolved crystallography")
    APS_BIOCAT_18ID = PermissibleValue(
        text="APS_BIOCAT_18ID",
        title="BioCAT (18-ID)",
        description="Biophysics Collaborative Access Team - fiber diffraction and SAXS")
    APS_IMCACAT_17ID = PermissibleValue(
        text="APS_IMCACAT_17ID",
        title="IMCA-CAT (17-ID)",
        description="Industrial Macromolecular Crystallography Association Collaborative Access Team")
    SSRL_BL92 = PermissibleValue(
        text="SSRL_BL92",
        title="SSRL BL9-2",
        description="Macromolecular crystallography beamline at Stanford Synchrotron Radiation Lightsource")
    SSRL_BL122 = PermissibleValue(
        text="SSRL_BL122",
        title="SSRL BL12-2",
        description="Solution scattering beamline for SAXS/WAXS at Stanford Synchrotron Radiation Lightsource")
    SSRL_BL141 = PermissibleValue(
        text="SSRL_BL141",
        title="SSRL BL14-1",
        description="Macromolecular crystallography beamline at Stanford Synchrotron Radiation Lightsource")
    SSRL_BL143 = PermissibleValue(
        text="SSRL_BL143",
        title="SSRL BL14-3",
        description="Tender X-ray Microprobe and XAS beamline at Stanford Synchrotron Radiation Lightsource")
    SSRL_BL23 = PermissibleValue(
        text="SSRL_BL23",
        title="SSRL BL2-3",
        description="Hard X-ray Microprobe and XAS beamline at Stanford Synchrotron Radiation Lightsource")
    SSRL_BL72 = PermissibleValue(
        text="SSRL_BL72",
        title="SSRL BL7-2",
        description="Lage Format XFM beamline at Stanford Synchrotron Radiation Lightsource")
    SSRL_BL62b = PermissibleValue(
        text="SSRL_BL62b",
        title="SSRL BL6-2b",
        description="HERFD XFM beamline at Stanford Synchrotron Radiation Lightsource")
    SNS_MANDI = PermissibleValue(
        text="SNS_MANDI",
        title="MaNDi",
        description="Macromolecular Neutron Diffractometer for neutron protein crystallography")
    HFIR_IMAGINE = PermissibleValue(
        text="HFIR_IMAGINE",
        title="IMAGINE",
        description="Image plate single crystal diffractometer for neutron protein crystallography")
    SNS_BIOSANS = PermissibleValue(
        text="SNS_BIOSANS",
        title="Bio-SANS",
        description="Biological Small-Angle Neutron Scattering instrument")
    SNS_EQSANS = PermissibleValue(
        text="SNS_EQSANS",
        title="EQ-SANS",
        description="Extended Q-Range Small-Angle Neutron Scattering instrument")

    _defn = EnumDefinition(
        name="BeamlineEnum",
        description="Specific beamline instances at DOE and other major structural biology facilities",
    )

class ImagingModeEnum(EnumDefinitionImpl):
    """
    Imaging modes for electron microscopy
    """
    EFTEM = PermissibleValue(
        text="EFTEM",
        description="Energy-filtered transmission electron microscopy")
    TEM = PermissibleValue(
        text="TEM",
        description="Transmission electron microscopy")
    STEM = PermissibleValue(
        text="STEM",
        description="Scanning transmission electron microscopy")

    _defn = EnumDefinition(
        name="ImagingModeEnum",
        description="Imaging modes for electron microscopy",
    )

class DetectorTypeEnum(EnumDefinitionImpl):
    """
    DEPRECATED: Use DetectorTechnologyEnum instead. Legacy enum mixing technologies and brands.
    """
    direct_electron = PermissibleValue(
        text="direct_electron",
        description="Direct electron detector")
    ccd = PermissibleValue(
        text="ccd",
        description="CCD camera")
    cmos = PermissibleValue(
        text="cmos",
        description="CMOS detector")
    hybrid_pixel = PermissibleValue(
        text="hybrid_pixel",
        description="Hybrid pixel detector")
    eiger = PermissibleValue(
        text="eiger",
        description="Dectris EIGER detector (hybrid photon counting)")
    pilatus = PermissibleValue(
        text="pilatus",
        description="Dectris PILATUS detector")
    rayonix = PermissibleValue(
        text="rayonix",
        description="Rayonix CCD detector")
    adsc = PermissibleValue(
        text="adsc",
        description="ADSC CCD detector")
    mar = PermissibleValue(
        text="mar",
        description="MAR CCD or imaging plate detector")

    _defn = EnumDefinition(
        name="DetectorTypeEnum",
        description="DEPRECATED: Use DetectorTechnologyEnum instead. Legacy enum mixing technologies and brands.",
    )

class DetectorTechnologyEnum(EnumDefinitionImpl):
    """
    Generic detector technologies for structural biology imaging
    """
    direct_electron_detector = PermissibleValue(
        text="direct_electron_detector",
        description="""Direct electron detector for cryo-EM (e.g., Gatan K2/K3, ThermoFisher Falcon, DirectElectron DE-64)""")
    ccd = PermissibleValue(
        text="ccd",
        description="Charge-coupled device camera")
    cmos = PermissibleValue(
        text="cmos",
        description="Complementary metal-oxide-semiconductor detector")
    hybrid_photon_counting = PermissibleValue(
        text="hybrid_photon_counting",
        description="Hybrid pixel photon counting detector for X-ray crystallography")
    scintillator_coupled = PermissibleValue(
        text="scintillator_coupled",
        description="Scintillator-coupled indirect detection")
    imaging_plate = PermissibleValue(
        text="imaging_plate",
        description="Imaging plate detector")
    film = PermissibleValue(
        text="film",
        description="Photographic film")
    ion_chamber = PermissibleValue(
        text="ion_chamber",
        description="gas-filled ionchamber")
    sdd = PermissibleValue(
        text="sdd",
        description="Silicon drift detector for fluorescence")
    sili = PermissibleValue(
        text="sili",
        description="Si(Li) detector for fluorescence")
    hpge = PermissibleValue(
        text="hpge",
        description="HPGe multi-element detector for fluorescence")
    photodiode = PermissibleValue(
        text="photodiode",
        description="Photodiode for direct beam or fluorescence detection")
    maia = PermissibleValue(
        text="maia",
        description="MAIA multi-element detector film")

    _defn = EnumDefinition(
        name="DetectorTechnologyEnum",
        description="Generic detector technologies for structural biology imaging",
    )

class DetectorModeEnum(EnumDefinitionImpl):
    """
    Operating modes for detectors during data collection
    """
    counting = PermissibleValue(
        text="counting",
        description="Electron/photon counting mode")
    integrating = PermissibleValue(
        text="integrating",
        description="Integrating mode (analog)")
    super_resolution = PermissibleValue(
        text="super_resolution",
        description="Super-resolution mode with oversampling")
    linear = PermissibleValue(
        text="linear",
        description="Linear response mode")
    correlated_double_sampling = PermissibleValue(
        text="correlated_double_sampling",
        description="Correlated double sampling mode")

    _defn = EnumDefinition(
        name="DetectorModeEnum",
        description="Operating modes for detectors during data collection",
    )

class XRaySourceTypeEnum(EnumDefinitionImpl):
    """
    Types of X-ray sources
    """
    synchrotron = PermissibleValue(
        text="synchrotron",
        description="Synchrotron radiation source")
    rotating_anode = PermissibleValue(
        text="rotating_anode",
        description="Rotating anode generator")
    microfocus = PermissibleValue(
        text="microfocus",
        description="Microfocus sealed tube")
    metal_jet = PermissibleValue(
        text="metal_jet",
        description="Liquid metal jet source")

    _defn = EnumDefinition(
        name="XRaySourceTypeEnum",
        description="Types of X-ray sources",
    )

class TechniqueEnum(EnumDefinitionImpl):
    """
    Structural biology techniques
    """
    cryo_em = PermissibleValue(
        text="cryo_em",
        description="Cryo-electron microscopy",
        meaning=CHMO["0002413"])
    xray_crystallography = PermissibleValue(
        text="xray_crystallography",
        description="X-ray crystallography",
        meaning=CHMO["0000156"])
    saxs = PermissibleValue(
        text="saxs",
        description="Small-angle X-ray scattering",
        meaning=CHMO["0000204"])
    waxs = PermissibleValue(
        text="waxs",
        description="Wide-angle X-ray scattering",
        meaning=CHMO["0000207"])
    sans = PermissibleValue(
        text="sans",
        description="Small-angle neutron scattering",
        meaning=CHMO["0000184"])
    cryo_et = PermissibleValue(
        text="cryo_et",
        description="Cryo-electron tomography",
        meaning=CHMO["0002413"])
    electron_microscopy = PermissibleValue(
        text="electron_microscopy",
        description="General electron microscopy",
        meaning=CHMO["0000068"])
    mass_spectrometry = PermissibleValue(
        text="mass_spectrometry",
        description="Mass spectrometry",
        meaning=CHMO["0000470"])
    xas = PermissibleValue(
        text="xas",
        description="X-ray absorption spectroscopy",
        meaning=CHMO["0000298"])
    xanes = PermissibleValue(
        text="xanes",
        description="X-ray absorption near edge structure spectroscopy",
        meaning=CHMO["0000305"])
    exafs = PermissibleValue(
        text="exafs",
        description="Extended X-ray absorption fine structure spectroscopy",
        meaning=CHMO["0000300"])
    xmcd = PermissibleValue(
        text="xmcd",
        description="X-ray magnetic circular dichroism")
    neutron_crystallography = PermissibleValue(
        text="neutron_crystallography",
        description="Neutron macromolecular crystallography",
        meaning=CHMO["0000182"])
    fiber_diffraction = PermissibleValue(
        text="fiber_diffraction",
        description="Fiber diffraction for structural analysis of fibrous samples",
        meaning=CHMO["0000156"])
    time_resolved_crystallography = PermissibleValue(
        text="time_resolved_crystallography",
        description="Time-resolved macromolecular crystallography",
        meaning=CHMO["0000156"])
    xray_tomography = PermissibleValue(
        text="xray_tomography",
        description="X-ray computed tomography (micro-CT) for 3D imaging",
        meaning=CHMO["0002743"])
    xray_microprobe = PermissibleValue(
        text="xray_microprobe",
        description="X-ray fluorescence microprobe imaging",
        meaning=CHMO["0002311"])
    ftir_imaging = PermissibleValue(
        text="ftir_imaging",
        description="FTIR microscopy",
        meaning=CHMO["0000051"])
    light_microscopy = PermissibleValue(
        text="light_microscopy",
        description="Brightfield microscopy",
        meaning=CHMO["0000104"])
    fluorescence_microscopy = PermissibleValue(
        text="fluorescence_microscopy",
        description="UV-visible fluorescence microscopy",
        meaning=CHMO["0000087"])
    confocal_microscopy = PermissibleValue(
        text="confocal_microscopy",
        description="X-ray fluorescence microprobe imaging",
        meaning=CHMO["0000089"])
    raman_microscopy = PermissibleValue(
        text="raman_microscopy",
        description="Raman microscopy",
        meaning=CHMO["0000056"])

    _defn = EnumDefinition(
        name="TechniqueEnum",
        description="Structural biology techniques",
    )

class ProcessingStatusEnum(EnumDefinitionImpl):
    """
    Processing status
    """
    collected = PermissibleValue(
        text="collected",
        description="Data has been collected but not yet processed")
    raw = PermissibleValue(
        text="raw",
        description="Raw data")
    preprocessing = PermissibleValue(
        text="preprocessing",
        description="Being preprocessed")
    processing = PermissibleValue(
        text="processing",
        description="Being processed")
    completed = PermissibleValue(
        text="completed",
        description="Processing completed")
    failed = PermissibleValue(
        text="failed",
        description="Processing failed")

    _defn = EnumDefinition(
        name="ProcessingStatusEnum",
        description="Processing status",
    )

class WorkflowTypeEnum(EnumDefinitionImpl):
    """
    Types of processing workflows
    """
    motion_correction = PermissibleValue(
        text="motion_correction",
        description="Motion correction for cryo-EM")
    ctf_estimation = PermissibleValue(
        text="ctf_estimation",
        description="CTF estimation")
    particle_picking = PermissibleValue(
        text="particle_picking",
        description="Particle picking")
    classification_2d = PermissibleValue(
        text="classification_2d",
        description="2D classification")
    classification_3d = PermissibleValue(
        text="classification_3d",
        description="3D classification")
    refinement = PermissibleValue(
        text="refinement",
        description="3D refinement")
    model_building = PermissibleValue(
        text="model_building",
        description="Atomic model building")
    phasing = PermissibleValue(
        text="phasing",
        description="Phase determination")
    integration = PermissibleValue(
        text="integration",
        description="Data integration")
    scaling = PermissibleValue(
        text="scaling",
        description="Data scaling")
    saxs_analysis = PermissibleValue(
        text="saxs_analysis",
        description="SAXS data analysis")
    xas_normalization = PermissibleValue(
        text="xas_normalization",
        description="XAS data normalization and background subtraction")
    xanes_analysis = PermissibleValue(
        text="xanes_analysis",
        description="XANES spectral analysis and edge fitting")
    exafs_analysis = PermissibleValue(
        text="exafs_analysis",
        description="EXAFS data analysis and shell fitting")
    em_2d_classification = PermissibleValue(
        text="em_2d_classification",
        description="EM 2D classification")
    mass_spec_deconvolution = PermissibleValue(
        text="mass_spec_deconvolution",
        description="Mass spectrometry deconvolution")
    particle_extraction = PermissibleValue(
        text="particle_extraction",
        description="Particle extraction from micrographs")
    ab_initio = PermissibleValue(
        text="ab_initio",
        description="Ab initio 3D reconstruction")
    postprocessing = PermissibleValue(
        text="postprocessing",
        description="Map post-processing and sharpening")
    map_validation = PermissibleValue(
        text="map_validation",
        description="3D map validation")
    model_refinement = PermissibleValue(
        text="model_refinement",
        description="Atomic model refinement")
    model_validation = PermissibleValue(
        text="model_validation",
        description="Model validation and quality assessment")
    xrf_analysis = PermissibleValue(
        text="xrf_analysis",
        description="XRF peak fitting analysis")
    ftir_analysis = PermissibleValue(
        text="ftir_analysis",
        description="FTIR peak fitting analysis")
    image_processing = PermissibleValue(
        text="image_processing",
        description="image pre/post processing workflow")

    _defn = EnumDefinition(
        name="WorkflowTypeEnum",
        description="Types of processing workflows",
    )

class FileFormatEnum(EnumDefinitionImpl):
    """
    File formats
    """
    mrc = PermissibleValue(
        text="mrc",
        description="MRC format for EM data")
    tiff = PermissibleValue(
        text="tiff",
        description="TIFF image format")
    ometiff = PermissibleValue(
        text="ometiff",
        description="OME TIFF image format")
    hdf5 = PermissibleValue(
        text="hdf5",
        description="HDF5 hierarchical data format")
    star = PermissibleValue(
        text="star",
        description="STAR format for metadata")
    pdb = PermissibleValue(
        text="pdb",
        description="PDB coordinate format")
    mmcif = PermissibleValue(
        text="mmcif",
        description="mmCIF format")
    mtz = PermissibleValue(
        text="mtz",
        description="MTZ reflection format")
    cbf = PermissibleValue(
        text="cbf",
        description="Crystallographic Binary Format")
    cbf_zst = PermissibleValue(
        text="cbf_zst",
        description="Zstandard-compressed CBF format")
    img = PermissibleValue(
        text="img",
        description="Generic diffraction image format")
    h5 = PermissibleValue(
        text="h5",
        description="HDF5 format (alternative extension)")
    ascii = PermissibleValue(
        text="ascii",
        description="ASCII text format")
    thermo_raw = PermissibleValue(
        text="thermo_raw",
        description="Thermo Fisher RAW format")
    zip = PermissibleValue(
        text="zip",
        description="ZIP compressed archive")
    mrcs = PermissibleValue(
        text="mrcs",
        description="MRC stack format for particle stacks")
    eer = PermissibleValue(
        text="eer",
        description="EER format for electron counting")
    cs = PermissibleValue(
        text="cs",
        description="CryoSPARC format")
    json = PermissibleValue(
        text="json",
        description="JSON data format")
    csv = PermissibleValue(
        text="csv",
        description="Comma-separated values format")
    ccp4 = PermissibleValue(
        text="ccp4",
        description="CCP4 map format")
    gz = PermissibleValue(
        text="gz",
        description="Gzip compressed format")

    _defn = EnumDefinition(
        name="FileFormatEnum",
        description="File formats",
    )

class DataTypeEnum(EnumDefinitionImpl):
    """
    Types of data
    """
    micrograph = PermissibleValue(
        text="micrograph",
        description="Electron micrograph")
    diffraction = PermissibleValue(
        text="diffraction",
        description="Diffraction pattern")
    scattering = PermissibleValue(
        text="scattering",
        description="Scattering data")
    particles = PermissibleValue(
        text="particles",
        description="Particle stack")
    volume = PermissibleValue(
        text="volume",
        description="3D volume")
    model = PermissibleValue(
        text="model",
        description="Atomic model")
    metadata = PermissibleValue(
        text="metadata",
        description="Metadata file")
    raw_data = PermissibleValue(
        text="raw_data",
        description="Raw experimental data")
    processed_data = PermissibleValue(
        text="processed_data",
        description="Processed data")
    movie = PermissibleValue(
        text="movie",
        description="Raw cryo-EM movie")
    motion_corrected = PermissibleValue(
        text="motion_corrected",
        description="Motion-corrected micrograph")
    ctf_estimation = PermissibleValue(
        text="ctf_estimation",
        description="CTF estimation results")
    particle_coordinates = PermissibleValue(
        text="particle_coordinates",
        description="Particle picking coordinates")
    class_averages = PermissibleValue(
        text="class_averages",
        description="2D or 3D class averages")
    fsc_curve = PermissibleValue(
        text="fsc_curve",
        description="Fourier Shell Correlation data")
    map_half = PermissibleValue(
        text="map_half",
        description="Half-map for gold-standard refinement")
    validation_report = PermissibleValue(
        text="validation_report",
        description="Validation report")
    xrf_image = PermissibleValue(
        text="xrf_image",
        description="XRF elemental image")
    ir_image = PermissibleValue(
        text="ir_image",
        description="IR/Raman vibrational band image")
    chemical_image = PermissibleValue(
        text="chemical_image",
        description="Image of specific chemical species, from XRF-XAS Imaging ir FTIR/Raman Imaging")

    _defn = EnumDefinition(
        name="DataTypeEnum",
        description="Types of data",
    )

class CollectionModeEnum(EnumDefinitionImpl):
    """
    Data collection modes
    """
    counting = PermissibleValue(
        text="counting",
        description="Counting mode")
    super_resolution = PermissibleValue(
        text="super_resolution",
        description="Super-resolution mode")
    continuous = PermissibleValue(
        text="continuous",
        description="Continuous collection")
    oscillation = PermissibleValue(
        text="oscillation",
        description="Oscillation method")
    still = PermissibleValue(
        text="still",
        description="Still images")
    batch = PermissibleValue(
        text="batch",
        description="Batch mode collection")
    sec_saxs = PermissibleValue(
        text="sec_saxs",
        description="SEC-SAXS collection mode")
    single_particle = PermissibleValue(
        text="single_particle",
        description="Single particle analysis mode")

    _defn = EnumDefinition(
        name="CollectionModeEnum",
        description="Data collection modes",
    )

class IlluminationTypeEnum(EnumDefinitionImpl):
    """
    Types of illumination for optical microscopy
    """
    brightfield = PermissibleValue(
        text="brightfield",
        description="Brightfield illumination")
    darkfield = PermissibleValue(
        text="darkfield",
        description="Darkfield illumination")
    phase_contrast = PermissibleValue(
        text="phase_contrast",
        description="Phase contrast microscopy")
    dic = PermissibleValue(
        text="dic",
        description="Differential interference contrast (DIC/Nomarski)")
    fluorescence = PermissibleValue(
        text="fluorescence",
        description="Fluorescence illumination")
    confocal = PermissibleValue(
        text="confocal",
        description="Confocal laser scanning")
    polarized = PermissibleValue(
        text="polarized",
        description="Polarized light microscopy")
    oblique = PermissibleValue(
        text="oblique",
        description="Oblique illumination")

    _defn = EnumDefinition(
        name="IlluminationTypeEnum",
        description="Types of illumination for optical microscopy",
    )

class ExperimentalMethodEnum(EnumDefinitionImpl):
    """
    Experimental methods for structure determination
    """
    x_ray_diffraction = PermissibleValue(
        text="x_ray_diffraction",
        description="X-ray diffraction",
        meaning=CHMO["0000156"])
    neutron_diffraction = PermissibleValue(
        text="neutron_diffraction",
        description="Neutron diffraction")
    electron_diffraction = PermissibleValue(
        text="electron_diffraction",
        description="Electron diffraction (e.g., microED)")
    fiber_diffraction = PermissibleValue(
        text="fiber_diffraction",
        description="Fiber diffraction")

    _defn = EnumDefinition(
        name="ExperimentalMethodEnum",
        description="Experimental methods for structure determination",
    )

class SampleRoleEnum(EnumDefinitionImpl):
    """
    Role of a sample in a study
    """
    target = PermissibleValue(
        text="target",
        description="Primary sample under investigation")
    control = PermissibleValue(
        text="control",
        description="Control sample for comparison")
    reference = PermissibleValue(
        text="reference",
        description="Reference standard or calibrant")
    blank = PermissibleValue(
        text="blank",
        description="Buffer blank or negative control")

    _defn = EnumDefinition(
        name="SampleRoleEnum",
        description="Role of a sample in a study",
    )

class ExperimentSampleRoleEnum(EnumDefinitionImpl):
    """
    Role of a sample in an experiment
    """
    target = PermissibleValue(
        text="target",
        description="Primary target of measurement")
    buffer_blank = PermissibleValue(
        text="buffer_blank",
        description="Buffer-only measurement for subtraction")
    standard = PermissibleValue(
        text="standard",
        description="Calibration or reference standard")
    size_marker = PermissibleValue(
        text="size_marker",
        description="Molecular weight marker")

    _defn = EnumDefinition(
        name="ExperimentSampleRoleEnum",
        description="Role of a sample in an experiment",
    )

class InstrumentRoleEnum(EnumDefinitionImpl):
    """
    Role of an instrument in an experiment
    """
    primary = PermissibleValue(
        text="primary",
        description="Primary data collection instrument")
    detector = PermissibleValue(
        text="detector",
        description="Secondary detector or detection component")
    sample_handler = PermissibleValue(
        text="sample_handler",
        description="Automated sample handling or positioning")

    _defn = EnumDefinition(
        name="InstrumentRoleEnum",
        description="Role of an instrument in an experiment",
    )

class InputTypeEnum(EnumDefinitionImpl):
    """
    Type of input for a workflow
    """
    raw_data = PermissibleValue(
        text="raw_data",
        description="Raw experimental data")
    reference = PermissibleValue(
        text="reference",
        description="Reference data (e.g., PDB model, database)")
    parameters = PermissibleValue(
        text="parameters",
        description="Processing parameters file")
    mask = PermissibleValue(
        text="mask",
        description="Mask or selection file")

    _defn = EnumDefinition(
        name="InputTypeEnum",
        description="Type of input for a workflow",
    )

class OutputTypeEnum(EnumDefinitionImpl):
    """
    Types of outputs from computational workflows
    """
    map = PermissibleValue(
        text="map",
        description="Density map or reconstructed volume")
    model = PermissibleValue(
        text="model",
        description="Atomic model or coordinates")
    particles = PermissibleValue(
        text="particles",
        description="Particle stack or extracted particles")
    micrographs = PermissibleValue(
        text="micrographs",
        description="Motion-corrected micrographs")
    ctf_estimates = PermissibleValue(
        text="ctf_estimates",
        description="CTF estimation results")
    metadata = PermissibleValue(
        text="metadata",
        description="Metadata or parameter files")
    statistics = PermissibleValue(
        text="statistics",
        description="Processing statistics or quality metrics")
    processed_data = PermissibleValue(
        text="processed_data",
        description="Processed or derived data files")
    log = PermissibleValue(
        text="log",
        description="Processing log files")
    image = PermissibleValue(
        text="image",
        description="Processed image files")

    _defn = EnumDefinition(
        name="OutputTypeEnum",
        description="Types of outputs from computational workflows",
    )

class FunctionalSiteTypeEnum(EnumDefinitionImpl):
    """
    Types of functional sites in proteins
    """
    active_site = PermissibleValue(
        text="active_site",
        description="Enzyme active site")
    catalytic_site = PermissibleValue(
        text="catalytic_site",
        description="Catalytic residues")
    binding_site = PermissibleValue(
        text="binding_site",
        description="General binding site")
    allosteric_site = PermissibleValue(
        text="allosteric_site",
        description="Allosteric regulation site")
    substrate_binding = PermissibleValue(
        text="substrate_binding",
        description="Substrate binding site")
    cofactor_binding = PermissibleValue(
        text="cofactor_binding",
        description="Cofactor binding site")
    inhibitor_binding = PermissibleValue(
        text="inhibitor_binding",
        description="Inhibitor binding site")
    metal_binding = PermissibleValue(
        text="metal_binding",
        description="Metal ion binding site")
    nucleotide_binding = PermissibleValue(
        text="nucleotide_binding",
        description="Nucleotide binding site")
    phosphorylation_site = PermissibleValue(
        text="phosphorylation_site",
        description="Phosphorylation site")
    glycosylation_site = PermissibleValue(
        text="glycosylation_site",
        description="Glycosylation site")
    ubiquitination_site = PermissibleValue(
        text="ubiquitination_site",
        description="Ubiquitination site")
    sumoylation_site = PermissibleValue(
        text="sumoylation_site",
        description="SUMOylation site")
    acetylation_site = PermissibleValue(
        text="acetylation_site",
        description="Acetylation site")
    methylation_site = PermissibleValue(
        text="methylation_site",
        description="Methylation site")
    protein_binding = PermissibleValue(
        text="protein_binding",
        description="Protein-protein interaction site")
    dna_binding = PermissibleValue(
        text="dna_binding",
        description="DNA binding site")
    rna_binding = PermissibleValue(
        text="rna_binding",
        description="RNA binding site")
    lipid_binding = PermissibleValue(
        text="lipid_binding",
        description="Lipid binding site")

    _defn = EnumDefinition(
        name="FunctionalSiteTypeEnum",
        description="Types of functional sites in proteins",
    )

class StructuralFeatureTypeEnum(EnumDefinitionImpl):
    """
    Types of structural features
    """
    alpha_helix = PermissibleValue(
        text="alpha_helix",
        description="Alpha helix")
    beta_sheet = PermissibleValue(
        text="beta_sheet",
        description="Beta sheet")
    beta_strand = PermissibleValue(
        text="beta_strand",
        description="Beta strand")
    turn = PermissibleValue(
        text="turn",
        description="Turn structure")
    coil = PermissibleValue(
        text="coil",
        description="Random coil")
    disordered_region = PermissibleValue(
        text="disordered_region",
        description="Intrinsically disordered region")
    transmembrane_helix = PermissibleValue(
        text="transmembrane_helix",
        description="Transmembrane helix")
    signal_peptide = PermissibleValue(
        text="signal_peptide",
        description="Signal peptide")
    transit_peptide = PermissibleValue(
        text="transit_peptide",
        description="Transit peptide")
    domain = PermissibleValue(
        text="domain",
        description="Protein domain")
    repeat = PermissibleValue(
        text="repeat",
        description="Sequence repeat")
    zinc_finger = PermissibleValue(
        text="zinc_finger",
        description="Zinc finger motif")
    zinc_binding = PermissibleValue(
        text="zinc_binding",
        description="Zinc binding site")
    coiled_coil = PermissibleValue(
        text="coiled_coil",
        description="Coiled coil")
    motif = PermissibleValue(
        text="motif",
        description="Structural motif")
    cavity = PermissibleValue(
        text="cavity",
        description="Structural cavity")
    channel = PermissibleValue(
        text="channel",
        description="Molecular channel")
    pore = PermissibleValue(
        text="pore",
        description="Molecular pore")
    hinge = PermissibleValue(
        text="hinge",
        description="Hinge region")
    linker = PermissibleValue(
        text="linker",
        description="Linker region")

    _defn = EnumDefinition(
        name="StructuralFeatureTypeEnum",
        description="Types of structural features",
    )

class SecondaryStructureEnum(EnumDefinitionImpl):
    """
    Secondary structure types
    """
    helix = PermissibleValue(
        text="helix",
        description="Helix structure")
    sheet = PermissibleValue(
        text="sheet",
        description="Beta sheet")
    turn = PermissibleValue(
        text="turn",
        description="Turn")
    coil = PermissibleValue(
        text="coil",
        description="Random coil")
    helix_310 = PermissibleValue(
        text="helix_310",
        description="3-10 helix")
    helix_pi = PermissibleValue(
        text="helix_pi",
        description="Pi helix")
    bend = PermissibleValue(
        text="bend",
        description="Bend")
    bridge = PermissibleValue(
        text="bridge",
        description="Beta bridge")

    _defn = EnumDefinition(
        name="SecondaryStructureEnum",
        description="Secondary structure types",
    )

class ConformationalStateEnum(EnumDefinitionImpl):
    """
    Conformational states
    """
    open = PermissibleValue(
        text="open",
        description="Open conformation")
    closed = PermissibleValue(
        text="closed",
        description="Closed conformation")
    intermediate = PermissibleValue(
        text="intermediate",
        description="Intermediate state")
    active = PermissibleValue(
        text="active",
        description="Active conformation")
    inactive = PermissibleValue(
        text="inactive",
        description="Inactive conformation")
    apo = PermissibleValue(
        text="apo",
        description="Apo form")
    holo = PermissibleValue(
        text="holo",
        description="Holo form")
    substrate_bound = PermissibleValue(
        text="substrate_bound",
        description="Substrate-bound")
    product_bound = PermissibleValue(
        text="product_bound",
        description="Product-bound")
    inhibitor_bound = PermissibleValue(
        text="inhibitor_bound",
        description="Inhibitor-bound")
    partially_open = PermissibleValue(
        text="partially_open",
        description="Partially open")
    partially_closed = PermissibleValue(
        text="partially_closed",
        description="Partially closed")
    disordered = PermissibleValue(
        text="disordered",
        description="Disordered state")

    _defn = EnumDefinition(
        name="ConformationalStateEnum",
        description="Conformational states",
    )

class InteractionTypeEnum(EnumDefinitionImpl):
    """
    Types of molecular interactions
    """
    covalent = PermissibleValue(
        text="covalent",
        description="Covalent bond")
    hydrogen_bond = PermissibleValue(
        text="hydrogen_bond",
        description="Hydrogen bond")
    ionic = PermissibleValue(
        text="ionic",
        description="Ionic interaction")
    van_der_waals = PermissibleValue(
        text="van_der_waals",
        description="Van der Waals interaction")
    hydrophobic = PermissibleValue(
        text="hydrophobic",
        description="Hydrophobic interaction")
    aromatic = PermissibleValue(
        text="aromatic",
        description="Aromatic interaction")
    pi_stacking = PermissibleValue(
        text="pi_stacking",
        description="Pi-pi stacking")
    cation_pi = PermissibleValue(
        text="cation_pi",
        description="Cation-pi interaction")
    metal_coordination = PermissibleValue(
        text="metal_coordination",
        description="Metal coordination")
    disulfide = PermissibleValue(
        text="disulfide",
        description="Disulfide bond")

    _defn = EnumDefinition(
        name="InteractionTypeEnum",
        description="Types of molecular interactions",
    )

class BindingAffinityTypeEnum(EnumDefinitionImpl):
    """
    Types of binding affinity measurements
    """
    kd = PermissibleValue(
        text="kd",
        description="Dissociation constant")
    ki = PermissibleValue(
        text="ki",
        description="Inhibition constant")
    ic50 = PermissibleValue(
        text="ic50",
        description="Half maximal inhibitory concentration")
    ec50 = PermissibleValue(
        text="ec50",
        description="Half maximal effective concentration")
    ka = PermissibleValue(
        text="ka",
        description="Association constant")
    km = PermissibleValue(
        text="km",
        description="Michaelis constant")

    _defn = EnumDefinition(
        name="BindingAffinityTypeEnum",
        description="Types of binding affinity measurements",
    )

class AffinityUnitEnum(EnumDefinitionImpl):
    """
    Units for affinity measurements
    """
    molar = PermissibleValue(
        text="molar",
        description="Molar (M)")
    millimolar = PermissibleValue(
        text="millimolar",
        description="Millimolar (mM)")
    micromolar = PermissibleValue(
        text="micromolar",
        description="Micromolar (µM)")
    nanomolar = PermissibleValue(
        text="nanomolar",
        description="Nanomolar (nM)")
    picomolar = PermissibleValue(
        text="picomolar",
        description="Picomolar (pM)")

    _defn = EnumDefinition(
        name="AffinityUnitEnum",
        description="Units for affinity measurements",
    )

class ComplexStabilityEnum(EnumDefinitionImpl):
    """
    Stability of protein complexes
    """
    stable = PermissibleValue(
        text="stable",
        description="Stable complex")
    transient = PermissibleValue(
        text="transient",
        description="Transient interaction")
    weak = PermissibleValue(
        text="weak",
        description="Weak interaction")
    strong = PermissibleValue(
        text="strong",
        description="Strong interaction")
    obligate = PermissibleValue(
        text="obligate",
        description="Obligate complex")
    non_obligate = PermissibleValue(
        text="non_obligate",
        description="Non-obligate complex")

    _defn = EnumDefinition(
        name="ComplexStabilityEnum",
        description="Stability of protein complexes",
    )

class InteractionEvidenceEnum(EnumDefinitionImpl):
    """
    Evidence for interactions
    """
    experimental = PermissibleValue(
        text="experimental",
        description="Experimental evidence")
    predicted = PermissibleValue(
        text="predicted",
        description="Computational prediction")
    homology = PermissibleValue(
        text="homology",
        description="Homology-based")
    coexpression = PermissibleValue(
        text="coexpression",
        description="Co-expression data")
    colocalization = PermissibleValue(
        text="colocalization",
        description="Co-localization")
    genetic = PermissibleValue(
        text="genetic",
        description="Genetic evidence")
    physical = PermissibleValue(
        text="physical",
        description="Physical interaction")
    functional = PermissibleValue(
        text="functional",
        description="Functional association")

    _defn = EnumDefinition(
        name="InteractionEvidenceEnum",
        description="Evidence for interactions",
    )

class MutationTypeEnum(EnumDefinitionImpl):
    """
    Types of mutations
    """
    missense = PermissibleValue(
        text="missense",
        description="Missense mutation")
    nonsense = PermissibleValue(
        text="nonsense",
        description="Nonsense mutation")
    frameshift = PermissibleValue(
        text="frameshift",
        description="Frameshift mutation")
    deletion = PermissibleValue(
        text="deletion",
        description="Deletion")
    insertion = PermissibleValue(
        text="insertion",
        description="Insertion")
    duplication = PermissibleValue(
        text="duplication",
        description="Duplication")
    substitution = PermissibleValue(
        text="substitution",
        description="Substitution")

    _defn = EnumDefinition(
        name="MutationTypeEnum",
        description="Types of mutations",
    )

class StabilityEffectEnum(EnumDefinitionImpl):
    """
    Effect on protein stability
    """
    stabilizing = PermissibleValue(
        text="stabilizing",
        description="Increases stability")
    destabilizing = PermissibleValue(
        text="destabilizing",
        description="Decreases stability")
    neutral = PermissibleValue(
        text="neutral",
        description="No significant effect")
    highly_stabilizing = PermissibleValue(
        text="highly_stabilizing",
        description="Strongly increases stability")
    highly_destabilizing = PermissibleValue(
        text="highly_destabilizing",
        description="Strongly decreases stability")

    _defn = EnumDefinition(
        name="StabilityEffectEnum",
        description="Effect on protein stability",
    )

class FunctionalEffectEnum(EnumDefinitionImpl):
    """
    Effect on protein function
    """
    loss_of_function = PermissibleValue(
        text="loss_of_function",
        description="Loss of function")
    gain_of_function = PermissibleValue(
        text="gain_of_function",
        description="Gain of function")
    altered_function = PermissibleValue(
        text="altered_function",
        description="Altered function")
    no_effect = PermissibleValue(
        text="no_effect",
        description="No functional effect")
    partial_loss = PermissibleValue(
        text="partial_loss",
        description="Partial loss of function")
    enhanced_function = PermissibleValue(
        text="enhanced_function",
        description="Enhanced function")

    _defn = EnumDefinition(
        name="FunctionalEffectEnum",
        description="Effect on protein function",
    )

class ClinicalSignificanceEnum(EnumDefinitionImpl):
    """
    Clinical significance of variants
    """
    pathogenic = PermissibleValue(
        text="pathogenic",
        description="Pathogenic")
    likely_pathogenic = PermissibleValue(
        text="likely_pathogenic",
        description="Likely pathogenic")
    benign = PermissibleValue(
        text="benign",
        description="Benign")
    likely_benign = PermissibleValue(
        text="likely_benign",
        description="Likely benign")
    uncertain_significance = PermissibleValue(
        text="uncertain_significance",
        description="Uncertain significance")

    _defn = EnumDefinition(
        name="ClinicalSignificanceEnum",
        description="Clinical significance of variants",
    )

class BiophysicalPropertyEnum(EnumDefinitionImpl):
    """
    Types of biophysical properties
    """
    melting_temperature = PermissibleValue(
        text="melting_temperature",
        description="Melting temperature (Tm)")
    stability = PermissibleValue(
        text="stability",
        description="Thermodynamic stability")
    folding_rate = PermissibleValue(
        text="folding_rate",
        description="Folding rate")
    unfolding_rate = PermissibleValue(
        text="unfolding_rate",
        description="Unfolding rate")
    aggregation_propensity = PermissibleValue(
        text="aggregation_propensity",
        description="Aggregation propensity")
    solubility = PermissibleValue(
        text="solubility",
        description="Solubility")
    hydrophobicity = PermissibleValue(
        text="hydrophobicity",
        description="Hydrophobicity")
    isoelectric_point = PermissibleValue(
        text="isoelectric_point",
        description="Isoelectric point (pI)")
    extinction_coefficient = PermissibleValue(
        text="extinction_coefficient",
        description="Extinction coefficient")
    molecular_weight = PermissibleValue(
        text="molecular_weight",
        description="Molecular weight")
    diffusion_coefficient = PermissibleValue(
        text="diffusion_coefficient",
        description="Diffusion coefficient")
    sedimentation_coefficient = PermissibleValue(
        text="sedimentation_coefficient",
        description="Sedimentation coefficient")
    radius_of_gyration = PermissibleValue(
        text="radius_of_gyration",
        description="Radius of gyration")
    hydrodynamic_radius = PermissibleValue(
        text="hydrodynamic_radius",
        description="Hydrodynamic radius")

    _defn = EnumDefinition(
        name="BiophysicalPropertyEnum",
        description="Types of biophysical properties",
    )

class BiophysicalMethodEnum(EnumDefinitionImpl):
    """
    Methods for biophysical measurements
    """
    differential_scanning_calorimetry = PermissibleValue(
        text="differential_scanning_calorimetry",
        description="DSC")
    isothermal_titration_calorimetry = PermissibleValue(
        text="isothermal_titration_calorimetry",
        description="ITC")
    circular_dichroism = PermissibleValue(
        text="circular_dichroism",
        description="CD spectroscopy")
    fluorescence_spectroscopy = PermissibleValue(
        text="fluorescence_spectroscopy",
        description="Fluorescence")
    surface_plasmon_resonance = PermissibleValue(
        text="surface_plasmon_resonance",
        description="SPR")
    dynamic_light_scattering = PermissibleValue(
        text="dynamic_light_scattering",
        description="DLS")
    analytical_ultracentrifugation = PermissibleValue(
        text="analytical_ultracentrifugation",
        description="AUC")
    nuclear_magnetic_resonance = PermissibleValue(
        text="nuclear_magnetic_resonance",
        description="NMR")
    mass_spectrometry = PermissibleValue(
        text="mass_spectrometry",
        description="MS")

    _defn = EnumDefinition(
        name="BiophysicalMethodEnum",
        description="Methods for biophysical measurements",
    )

class PTMTypeEnum(EnumDefinitionImpl):
    """
    Types of post-translational modifications
    """
    acetylation = PermissibleValue(
        text="acetylation",
        description="protein acetylation",
        meaning=GO["0006473"])
    acylation = PermissibleValue(
        text="acylation",
        description="protein acylation",
        meaning=GO["0043543"])
    adp_ribosylation = PermissibleValue(
        text="adp_ribosylation",
        description="ADP-ribosylation")
    alkylation = PermissibleValue(
        text="alkylation",
        description="protein alkylation",
        meaning=GO["0008213"])
    arginylation = PermissibleValue(
        text="arginylation",
        description="protein arginylation",
        meaning=GO["0016598"])
    carbamoylation = PermissibleValue(
        text="carbamoylation",
        description="protein carbamoylation",
        meaning=GO["0046944"])
    carboxylation = PermissibleValue(
        text="carboxylation",
        description="protein carboxylation",
        meaning=GO["0018214"])
    deacylation = PermissibleValue(
        text="deacylation",
        description="protein deacylation",
        meaning=GO["0035601"])
    dealkylation = PermissibleValue(
        text="dealkylation",
        description="protein dealkylation",
        meaning=GO["0008214"])
    deamidation = PermissibleValue(
        text="deamidation",
        description="deamidation")
    deamination = PermissibleValue(
        text="deamination",
        description="protein deamination",
        meaning=GO["0018277"])
    deglutathionylation = PermissibleValue(
        text="deglutathionylation",
        description="protein deglutathionylation",
        meaning=GO["0080058"])
    deglycation = PermissibleValue(
        text="deglycation",
        description="protein deglycation",
        meaning=GO["0036525"])
    deglycosylation = PermissibleValue(
        text="deglycosylation",
        description="protein deglycosylation",
        meaning=GO["0006517"])
    dephosphorylation = PermissibleValue(
        text="dephosphorylation",
        description="protein dephosphorylation",
        meaning=GO["0006470"])
    flavinylation = PermissibleValue(
        text="flavinylation",
        description="protein flavinylation",
        meaning=GO["0017013"])
    glutathionylation = PermissibleValue(
        text="glutathionylation",
        description="protein glutathionylation",
        meaning=GO["0010731"])
    glycosylation = PermissibleValue(
        text="glycosylation",
        description="protein glycosylation")
    hydroxylation = PermissibleValue(
        text="hydroxylation",
        description="protein hydroxylation",
        meaning=GO["0018126"])
    lipidation = PermissibleValue(
        text="lipidation",
        description="protein lipidation",
        meaning=GO["0006497"])
    methylation = PermissibleValue(
        text="methylation",
        description="protein methylation",
        meaning=GO["0006479"])
    myristoylation = PermissibleValue(
        text="myristoylation",
        description="protein myristoylation",
        meaning=GO["0018377"])
    nitrosylation = PermissibleValue(
        text="nitrosylation",
        description="protein nitrosylation",
        meaning=GO["0017014"])
    oxidation = PermissibleValue(
        text="oxidation",
        description="protein oxidation",
        meaning=GO["0018158"])
    palmitoylation = PermissibleValue(
        text="palmitoylation",
        description="protein palmitoylation",
        meaning=GO["0018345"])
    peptidyl_amino_acid_modification = PermissibleValue(
        text="peptidyl_amino_acid_modification",
        description="peptidyl-amino acid modification",
        meaning=GO["0018193"])
    phosphorylation = PermissibleValue(
        text="phosphorylation",
        description="protein phosphorylation",
        meaning=GO["0006468"])
    post_translational_protein_modification = PermissibleValue(
        text="post_translational_protein_modification",
        description="post-translational protein modification",
        meaning=GO["0043687"])
    prenylation = PermissibleValue(
        text="prenylation",
        description="protein prenylation",
        meaning=GO["0018342"])
    proteolysis = PermissibleValue(
        text="proteolysis",
        description="proteolysis",
        meaning=GO["0006508"])
    sulfation = PermissibleValue(
        text="sulfation",
        description="protein sulfation",
        meaning=GO["0006477"])
    sulfhydration = PermissibleValue(
        text="sulfhydration",
        description="protein sulfhydration",
        meaning=GO["0044524"])
    sumoylation = PermissibleValue(
        text="sumoylation",
        description="protein sumoylation",
        meaning=GO["0016925"])
    ubiquitination = PermissibleValue(
        text="ubiquitination",
        description="protein ubiquitination",
        meaning=GO["0016567"])

    _defn = EnumDefinition(
        name="PTMTypeEnum",
        description="Types of post-translational modifications",
    )

class EvidenceTypeEnum(EnumDefinitionImpl):
    """
    Types of evidence
    """
    experimental = PermissibleValue(
        text="experimental",
        description="Direct experimental evidence")
    predicted = PermissibleValue(
        text="predicted",
        description="Computational prediction")
    inferred = PermissibleValue(
        text="inferred",
        description="Inferred from homology")
    literature = PermissibleValue(
        text="literature",
        description="Literature curation")
    author_statement = PermissibleValue(
        text="author_statement",
        description="Author statement")
    curator_inference = PermissibleValue(
        text="curator_inference",
        description="Curator inference")

    _defn = EnumDefinition(
        name="EvidenceTypeEnum",
        description="Types of evidence",
    )

class AnnotationSourceEnum(EnumDefinitionImpl):
    """
    Sources of functional annotations
    """
    pdbe = PermissibleValue(
        text="pdbe",
        description="PDBe")
    pdbe_kb = PermissibleValue(
        text="pdbe_kb",
        description="PDBe-KB")
    uniprot = PermissibleValue(
        text="uniprot",
        description="UniProt")
    pfam = PermissibleValue(
        text="pfam",
        description="Pfam")
    cath = PermissibleValue(
        text="cath",
        description="CATH")
    scop = PermissibleValue(
        text="scop",
        description="SCOP")
    interpro = PermissibleValue(
        text="interpro",
        description="InterPro")
    channelsdb = PermissibleValue(
        text="channelsdb",
        description="ChannelsDB")
    dynamine = PermissibleValue(
        text="dynamine",
        description="DynaMine")
    foldx = PermissibleValue(
        text="foldx",
        description="FoldX")
    p2rank = PermissibleValue(
        text="p2rank",
        description="P2rank")
    arpeggio = PermissibleValue(
        text="arpeggio",
        description="Arpeggio")
    covalentizer = PermissibleValue(
        text="covalentizer",
        description="Covalentizer")
    depth = PermissibleValue(
        text="depth",
        description="DEPTH")
    elmpdb = PermissibleValue(
        text="elmpdb",
        description="ELM-PDB")
    frustration = PermissibleValue(
        text="frustration",
        description="Frustration")
    kincore = PermissibleValue(
        text="kincore",
        description="KinCore")
    membranome = PermissibleValue(
        text="membranome",
        description="Membranome")
    missense3d = PermissibleValue(
        text="missense3d",
        description="Missense3D")
    mobi = PermissibleValue(
        text="mobi",
        description="MobiDB")
    nucleos = PermissibleValue(
        text="nucleos",
        description="Nucleos")
    akid = PermissibleValue(
        text="akid",
        description="AKID")
    camkinet = PermissibleValue(
        text="camkinet",
        description="CamKiNet")
    cansar = PermissibleValue(
        text="cansar",
        description="canSAR")
    credo = PermissibleValue(
        text="credo",
        description="CREDO")
    klifs = PermissibleValue(
        text="klifs",
        description="KLIFS")
    m_csm = PermissibleValue(
        text="m_csm",
        description="mCSM")
    moondb = PermissibleValue(
        text="moondb",
        description="MoonDB")
    pocketome = PermissibleValue(
        text="pocketome",
        description="Pocketome")
    propka = PermissibleValue(
        text="propka",
        description="PROPKA")
    proteins_api = PermissibleValue(
        text="proteins_api",
        description="Proteins API")
    validation = PermissibleValue(
        text="validation",
        description="Validation")
    alphafold = PermissibleValue(
        text="alphafold",
        description="AlphaFold")
    modbase = PermissibleValue(
        text="modbase",
        description="ModBase")
    swiss_model = PermissibleValue(
        text="swiss_model",
        description="SWISS-MODEL")
    intact = PermissibleValue(
        text="intact",
        description="IntAct")
    cosmic = PermissibleValue(
        text="cosmic",
        description="COSMIC")
    clinvar = PermissibleValue(
        text="clinvar",
        description="ClinVar")

    _defn = EnumDefinition(
        name="AnnotationSourceEnum",
        description="Sources of functional annotations",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "3dligandsite",
            PermissibleValue(
                text="3dligandsite",
                description="3D-LigandSite"))
        setattr(cls, "14_3_3_pred",
            PermissibleValue(
                text="14_3_3_pred",
                description="14-3-3-Pred"))

class DatabaseNameEnum(EnumDefinitionImpl):
    """
    External database names
    """
    uniprot = PermissibleValue(
        text="uniprot",
        description="UniProt")
    pdb = PermissibleValue(
        text="pdb",
        description="Protein Data Bank")
    pfam = PermissibleValue(
        text="pfam",
        description="Pfam")
    cath = PermissibleValue(
        text="cath",
        description="CATH")
    scop = PermissibleValue(
        text="scop",
        description="SCOP")
    interpro = PermissibleValue(
        text="interpro",
        description="InterPro")
    chembl = PermissibleValue(
        text="chembl",
        description="ChEMBL")
    chebi = PermissibleValue(
        text="chebi",
        description="ChEBI")
    pubchem = PermissibleValue(
        text="pubchem",
        description="PubChem")
    drugbank = PermissibleValue(
        text="drugbank",
        description="DrugBank")
    omim = PermissibleValue(
        text="omim",
        description="OMIM")
    clinvar = PermissibleValue(
        text="clinvar",
        description="ClinVar")
    cosmic = PermissibleValue(
        text="cosmic",
        description="COSMIC")
    gnomad = PermissibleValue(
        text="gnomad",
        description="gnomAD")
    intact = PermissibleValue(
        text="intact",
        description="IntAct")
    string = PermissibleValue(
        text="string",
        description="STRING")
    biogrid = PermissibleValue(
        text="biogrid",
        description="BioGRID")
    reactome = PermissibleValue(
        text="reactome",
        description="Reactome")
    kegg = PermissibleValue(
        text="kegg",
        description="KEGG")
    go = PermissibleValue(
        text="go",
        description="Gene Ontology")

    _defn = EnumDefinition(
        name="DatabaseNameEnum",
        description="External database names",
    )

class PloidyTypeEnum(EnumDefinitionImpl):
    """
    The ploidy level of the genome
    """
    haploid = PermissibleValue(text="haploid")
    diploid = PermissibleValue(text="diploid")
    triploid = PermissibleValue(text="triploid")
    tetraploid = PermissibleValue(text="tetraploid")
    pentaploid = PermissibleValue(text="pentaploid")
    hexaploid = PermissibleValue(text="hexaploid")
    octoploid = PermissibleValue(text="octoploid")
    allopolyploid = PermissibleValue(text="allopolyploid")
    autopolyploid = PermissibleValue(text="autopolyploid")
    aneuploid = PermissibleValue(text="aneuploid")

    _defn = EnumDefinition(
        name="PloidyTypeEnum",
        description="The ploidy level of the genome",
    )

class SamplePreservationEnum(EnumDefinitionImpl):
    """
    The method employed for preserving or fixing the tissue. Use Fresh if the sample was harvested immdiately before
    processing. Select from the following options: [Formaldehyde, N2 Freeze, FFPE, Fresh]
    """
    N2_freeze = PermissibleValue(
        text="N2_freeze",
        description="Plunge freezing in liquid nitrogen")
    Formaldehyde = PermissibleValue(
        text="Formaldehyde",
        description="Formeldehyde fixation")
    FFPE = PermissibleValue(
        text="FFPE",
        description="FFPE")
    Fresh = PermissibleValue(
        text="Fresh",
        description="Fresh harvest")
    Other = PermissibleValue(
        text="Other",
        description="Other, leave details in comment")

    _defn = EnumDefinition(
        name="SamplePreservationEnum",
        description="""The method employed for preserving or fixing the tissue. Use Fresh if the sample was harvested immdiately before processing. Select from the following options: [Formaldehyde, N2 Freeze, FFPE, Fresh]""",
    )

class GrowthFacilityEnum(EnumDefinitionImpl):
    """
    Type of facility where the sampled plant was grown (e.g. growth chamber, greenhouse, irrigated field, wild)
    """
    growth_chamber = PermissibleValue(text="growth_chamber")
    greenhouse = PermissibleValue(text="greenhouse")
    irrigated_field = PermissibleValue(text="irrigated_field")
    wild = PermissibleValue(text="wild")
    laboratory = PermissibleValue(text="laboratory")
    field = PermissibleValue(text="field")
    other = PermissibleValue(text="other")

    _defn = EnumDefinition(
        name="GrowthFacilityEnum",
        description="""Type of facility where the sampled plant was grown (e.g. growth chamber, greenhouse, irrigated field, wild)""",
    )

class ArabadopsisStageEnum(EnumDefinitionImpl):
    """
    Stage that takes into account effect of genotype & environment effects. Requires in depth knowledge about features
    of model organism doi: 10.1105/TPC.010011
    """
    Stage_0 = PermissibleValue(
        text="Stage_0",
        description="principal growth stage - seed germination")
    Stage_1 = PermissibleValue(
        text="Stage_1",
        description="principal growth stage - leaf development")
    Stage_3 = PermissibleValue(
        text="Stage_3",
        description="principal growth stage - rosette growth")
    Stage_5 = PermissibleValue(
        text="Stage_5",
        description="principal growth stage - inflorescence emergence")
    Stage_6 = PermissibleValue(
        text="Stage_6",
        description="principal growth stage - flower production")
    Stage_8 = PermissibleValue(
        text="Stage_8",
        description="principal growth stage - silique ripening")
    Stage_9 = PermissibleValue(
        text="Stage_9",
        description="principal growth stage - senescence")

    _defn = EnumDefinition(
        name="ArabadopsisStageEnum",
        description="""Stage that takes into account effect of genotype & environment effects. Requires in depth knowledge about features of model organism doi: 10.1105/TPC.010011""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Stage_0.10",
            PermissibleValue(
                text="Stage_0.10",
                description="seed imbibition"))
        setattr(cls, "Stage_0.50",
            PermissibleValue(
                text="Stage_0.50",
                description="radicle emergence"))
        setattr(cls, "Stage_0.70",
            PermissibleValue(
                text="Stage_0.70",
                description="hypocotyl and cotyledon emergence"))
        setattr(cls, "Stage_1.02",
            PermissibleValue(
                text="Stage_1.02",
                description="2 rosette leaves > 1mm in length"))
        setattr(cls, "Stage_1.03",
            PermissibleValue(
                text="Stage_1.03",
                description="3 rosette leaves > 1mm in length"))
        setattr(cls, "Stage_1.04",
            PermissibleValue(
                text="Stage_1.04",
                description="4 rosette leaves > 1mm in length"))
        setattr(cls, "Stage_1.05",
            PermissibleValue(
                text="Stage_1.05",
                description="5 rosette leaves > 1mm in length"))
        setattr(cls, "Stage_1.06",
            PermissibleValue(
                text="Stage_1.06",
                description="6 rosette leaves > 1mm in length"))
        setattr(cls, "Stage_1.07",
            PermissibleValue(
                text="Stage_1.07",
                description="7 rosette leaves > 1mm in length"))
        setattr(cls, "Stage_1.08",
            PermissibleValue(
                text="Stage_1.08",
                description="8 rosette leaves > 1mm in length"))
        setattr(cls, "Stage_1.09",
            PermissibleValue(
                text="Stage_1.09",
                description="9 rosette leaves > 1mm in length"))
        setattr(cls, "Stage_1.10",
            PermissibleValue(
                text="Stage_1.10",
                description="10 rosette leaves > 1mm in length"))
        setattr(cls, "Stage_1.11",
            PermissibleValue(
                text="Stage_1.11",
                description="11 rosette leaves > 1mm in length"))
        setattr(cls, "Stage_1.12",
            PermissibleValue(
                text="Stage_1.12",
                description="12 rosette leaves > 1mm in length"))
        setattr(cls, "Stage_1.13",
            PermissibleValue(
                text="Stage_1.13",
                description="13 rosette leaves > 1mm in length"))
        setattr(cls, "Stage_1.14",
            PermissibleValue(
                text="Stage_1.14",
                description="14 rosette leaves > 1mm in length"))
        setattr(cls, "Stage_3.20",
            PermissibleValue(
                text="Stage_3.20",
                description="rosette is 20% of final size"))
        setattr(cls, "Stage_3.50",
            PermissibleValue(
                text="Stage_3.50",
                description="rosette is 50% of final size"))
        setattr(cls, "Stage_3.70",
            PermissibleValue(
                text="Stage_3.70",
                description="rosette is 70% of final size"))
        setattr(cls, "Stage_3.90",
            PermissibleValue(
                text="Stage_3.90",
                description="rosette is 90% of final size"))
        setattr(cls, "Stage_5.10",
            PermissibleValue(
                text="Stage_5.10",
                description="first flower buds visible"))
        setattr(cls, "Stage_6.00",
            PermissibleValue(
                text="Stage_6.00",
                description="first flower open"))
        setattr(cls, "Stage_6.10",
            PermissibleValue(
                text="Stage_6.10",
                description="10% of flowers to be produced have opened"))
        setattr(cls, "Stage_6.30",
            PermissibleValue(
                text="Stage_6.30",
                description="30% of flowers to be produced have opened"))
        setattr(cls, "Stage_6.50",
            PermissibleValue(
                text="Stage_6.50",
                description="50% of flowers to be produced have opened"))
        setattr(cls, "Stage_6.90",
            PermissibleValue(
                text="Stage_6.90",
                description="flowering complete"))
        setattr(cls, "Stage_8.00",
            PermissibleValue(
                text="Stage_8.00",
                description="first silique shattered"))
        setattr(cls, "Stage_9.70",
            PermissibleValue(
                text="Stage_9.70",
                description="senesence complete; ready for seed harvest"))

# Slots
class slots:
    pass

slots.attribute = Slot(uri=AIMSLEAF.attribute, name="attribute", curie=AIMSLEAF.curie('attribute'),
                   model_uri=AIMSLEAF.attribute, domain=None, range=Union[dict, Attribute])

slots.numeric_value = Slot(uri=AIMSLEAF.numeric_value, name="numeric_value", curie=AIMSLEAF.curie('numeric_value'),
                   model_uri=AIMSLEAF.numeric_value, domain=None, range=Optional[float], mappings = [NMDC["numeric_value"], QUD["quantityValue"], SCHEMA["value"]])

slots.minimum_numeric_value = Slot(uri=AIMSLEAF.minimum_numeric_value, name="minimum_numeric_value", curie=AIMSLEAF.curie('minimum_numeric_value'),
                   model_uri=AIMSLEAF.minimum_numeric_value, domain=None, range=Optional[float], mappings = [NMDC["minimum_numeric_value"]])

slots.maximum_numeric_value = Slot(uri=AIMSLEAF.maximum_numeric_value, name="maximum_numeric_value", curie=AIMSLEAF.curie('maximum_numeric_value'),
                   model_uri=AIMSLEAF.maximum_numeric_value, domain=None, range=Optional[float], mappings = [NMDC["maximum_numeric_value"]])

slots.raw_value = Slot(uri=AIMSLEAF.raw_value, name="raw_value", curie=AIMSLEAF.curie('raw_value'),
                   model_uri=AIMSLEAF.raw_value, domain=None, range=Optional[str], mappings = [NMDC["raw_value"]])

slots.unit = Slot(uri=AIMSLEAF.unit, name="unit", curie=AIMSLEAF.curie('unit'),
                   model_uri=AIMSLEAF.unit, domain=None, range=Optional[str], mappings = [NMDC["unit"], QUD["unit"], SCHEMA["unitCode"], UO["0000000"]])

slots.unit_cv_id = Slot(uri=AIMSLEAF.unit_cv_id, name="unit_cv_id", curie=AIMSLEAF.curie('unit_cv_id'),
                   model_uri=AIMSLEAF.unit_cv_id, domain=None, range=Optional[Union[str, Curie]])

slots.value = Slot(uri=AIMSLEAF.value, name="value", curie=AIMSLEAF.curie('value'),
                   model_uri=AIMSLEAF.value, domain=None, range=Optional[str])

slots.value_cv_id = Slot(uri=AIMSLEAF.value_cv_id, name="value_cv_id", curie=AIMSLEAF.curie('value_cv_id'),
                   model_uri=AIMSLEAF.value_cv_id, domain=None, range=Optional[Union[str, Curie]])

slots.namedThing__id = Slot(uri=AIMSLEAF.id, name="namedThing__id", curie=AIMSLEAF.curie('id'),
                   model_uri=AIMSLEAF.namedThing__id, domain=None, range=URIRef)

slots.namedThing__title = Slot(uri=DCTERMS.title, name="namedThing__title", curie=DCTERMS.curie('title'),
                   model_uri=AIMSLEAF.namedThing__title, domain=None, range=Optional[str])

slots.namedThing__description = Slot(uri=AIMSLEAF.description, name="namedThing__description", curie=AIMSLEAF.curie('description'),
                   model_uri=AIMSLEAF.namedThing__description, domain=None, range=Optional[str])

slots.attributeGroup__description = Slot(uri=AIMSLEAF.description, name="attributeGroup__description", curie=AIMSLEAF.curie('description'),
                   model_uri=AIMSLEAF.attributeGroup__description, domain=None, range=Optional[str])

slots.dataset__keywords = Slot(uri=AIMSLEAF.keywords, name="dataset__keywords", curie=AIMSLEAF.curie('keywords'),
                   model_uri=AIMSLEAF.dataset__keywords, domain=None, range=Optional[Union[str, list[str]]])

slots.dataset__studies = Slot(uri=AIMSLEAF.studies, name="dataset__studies", curie=AIMSLEAF.curie('studies'),
                   model_uri=AIMSLEAF.dataset__studies, domain=None, range=Optional[Union[dict[Union[str, StudyId], Union[dict, Study]], list[Union[dict, Study]]]])

slots.dataset__instruments = Slot(uri=AIMSLEAF.instruments, name="dataset__instruments", curie=AIMSLEAF.curie('instruments'),
                   model_uri=AIMSLEAF.dataset__instruments, domain=None, range=Optional[Union[dict[Union[str, InstrumentId], Union[dict, Instrument]], list[Union[dict, Instrument]]]])

slots.dataset__samples = Slot(uri=AIMSLEAF.samples, name="dataset__samples", curie=AIMSLEAF.curie('samples'),
                   model_uri=AIMSLEAF.dataset__samples, domain=None, range=Optional[Union[dict[Union[str, SampleId], Union[dict, Sample]], list[Union[dict, Sample]]]])

slots.dataset__plantsamples = Slot(uri=AIMSLEAF.plantsamples, name="dataset__plantsamples", curie=AIMSLEAF.curie('plantsamples'),
                   model_uri=AIMSLEAF.dataset__plantsamples, domain=None, range=Optional[Union[dict[Union[str, PlantSampleId], Union[dict, PlantSample]], list[Union[dict, PlantSample]]]])

slots.dataset__sample_preparations = Slot(uri=AIMSLEAF.sample_preparations, name="dataset__sample_preparations", curie=AIMSLEAF.curie('sample_preparations'),
                   model_uri=AIMSLEAF.dataset__sample_preparations, domain=None, range=Optional[Union[dict[Union[str, SamplePreparationId], Union[dict, SamplePreparation]], list[Union[dict, SamplePreparation]]]])

slots.dataset__plant_sample_preparations = Slot(uri=AIMSLEAF.plant_sample_preparations, name="dataset__plant_sample_preparations", curie=AIMSLEAF.curie('plant_sample_preparations'),
                   model_uri=AIMSLEAF.dataset__plant_sample_preparations, domain=None, range=Optional[Union[dict[Union[str, PlantSamplePreparationId], Union[dict, PlantSamplePreparation]], list[Union[dict, PlantSamplePreparation]]]])

slots.dataset__experiment_runs = Slot(uri=AIMSLEAF.experiment_runs, name="dataset__experiment_runs", curie=AIMSLEAF.curie('experiment_runs'),
                   model_uri=AIMSLEAF.dataset__experiment_runs, domain=None, range=Optional[Union[dict[Union[str, ExperimentRunId], Union[dict, ExperimentRun]], list[Union[dict, ExperimentRun]]]])

slots.dataset__workflow_runs = Slot(uri=AIMSLEAF.workflow_runs, name="dataset__workflow_runs", curie=AIMSLEAF.curie('workflow_runs'),
                   model_uri=AIMSLEAF.dataset__workflow_runs, domain=None, range=Optional[Union[dict[Union[str, WorkflowRunId], Union[dict, WorkflowRun]], list[Union[dict, WorkflowRun]]]])

slots.dataset__data_files = Slot(uri=AIMSLEAF.data_files, name="dataset__data_files", curie=AIMSLEAF.curie('data_files'),
                   model_uri=AIMSLEAF.dataset__data_files, domain=None, range=Optional[Union[dict[Union[str, DataFileId], Union[dict, DataFile]], list[Union[dict, DataFile]]]])

slots.dataset__images = Slot(uri=AIMSLEAF.images, name="dataset__images", curie=AIMSLEAF.curie('images'),
                   model_uri=AIMSLEAF.dataset__images, domain=None, range=Optional[Union[dict[Union[str, ImageId], Union[dict, Image]], list[Union[dict, Image]]]])

slots.dataset__sample_datafile_associations = Slot(uri=AIMSLEAF.sample_datafile_associations, name="dataset__sample_datafile_associations", curie=AIMSLEAF.curie('sample_datafile_associations'),
                   model_uri=AIMSLEAF.dataset__sample_datafile_associations, domain=None, range=Optional[Union[Union[dict, SampleDataAssociation], list[Union[dict, SampleDataAssociation]]]])

slots.dataset__study_sample_associations = Slot(uri=AIMSLEAF.study_sample_associations, name="dataset__study_sample_associations", curie=AIMSLEAF.curie('study_sample_associations'),
                   model_uri=AIMSLEAF.dataset__study_sample_associations, domain=None, range=Optional[Union[Union[dict, StudySampleAssociation], list[Union[dict, StudySampleAssociation]]]])

slots.dataset__study_experiment_associations = Slot(uri=AIMSLEAF.study_experiment_associations, name="dataset__study_experiment_associations", curie=AIMSLEAF.curie('study_experiment_associations'),
                   model_uri=AIMSLEAF.dataset__study_experiment_associations, domain=None, range=Optional[Union[Union[dict, StudyExperimentAssociation], list[Union[dict, StudyExperimentAssociation]]]])

slots.dataset__study_workflow_associations = Slot(uri=AIMSLEAF.study_workflow_associations, name="dataset__study_workflow_associations", curie=AIMSLEAF.curie('study_workflow_associations'),
                   model_uri=AIMSLEAF.dataset__study_workflow_associations, domain=None, range=Optional[Union[Union[dict, StudyWorkflowAssociation], list[Union[dict, StudyWorkflowAssociation]]]])

slots.dataset__experiment_sample_associations = Slot(uri=AIMSLEAF.experiment_sample_associations, name="dataset__experiment_sample_associations", curie=AIMSLEAF.curie('experiment_sample_associations'),
                   model_uri=AIMSLEAF.dataset__experiment_sample_associations, domain=None, range=Optional[Union[Union[dict, ExperimentSampleAssociation], list[Union[dict, ExperimentSampleAssociation]]]])

slots.dataset__experiment_instrument_associations = Slot(uri=AIMSLEAF.experiment_instrument_associations, name="dataset__experiment_instrument_associations", curie=AIMSLEAF.curie('experiment_instrument_associations'),
                   model_uri=AIMSLEAF.dataset__experiment_instrument_associations, domain=None, range=Optional[Union[Union[dict, ExperimentInstrumentAssociation], list[Union[dict, ExperimentInstrumentAssociation]]]])

slots.dataset__workflow_experiment_associations = Slot(uri=AIMSLEAF.workflow_experiment_associations, name="dataset__workflow_experiment_associations", curie=AIMSLEAF.curie('workflow_experiment_associations'),
                   model_uri=AIMSLEAF.dataset__workflow_experiment_associations, domain=None, range=Optional[Union[Union[dict, WorkflowExperimentAssociation], list[Union[dict, WorkflowExperimentAssociation]]]])

slots.dataset__workflow_input_associations = Slot(uri=AIMSLEAF.workflow_input_associations, name="dataset__workflow_input_associations", curie=AIMSLEAF.curie('workflow_input_associations'),
                   model_uri=AIMSLEAF.dataset__workflow_input_associations, domain=None, range=Optional[Union[Union[dict, WorkflowInputAssociation], list[Union[dict, WorkflowInputAssociation]]]])

slots.dataset__workflow_output_associations = Slot(uri=AIMSLEAF.workflow_output_associations, name="dataset__workflow_output_associations", curie=AIMSLEAF.curie('workflow_output_associations'),
                   model_uri=AIMSLEAF.dataset__workflow_output_associations, domain=None, range=Optional[Union[Union[dict, WorkflowOutputAssociation], list[Union[dict, WorkflowOutputAssociation]]]])

slots.study__keywords = Slot(uri=AIMSLEAF.keywords, name="study__keywords", curie=AIMSLEAF.curie('keywords'),
                   model_uri=AIMSLEAF.study__keywords, domain=None, range=Optional[Union[str, list[str]]])

slots.sample__sample_code = Slot(uri=AIMSLEAF.sample_code, name="sample__sample_code", curie=AIMSLEAF.curie('sample_code'),
                   model_uri=AIMSLEAF.sample__sample_code, domain=None, range=str)

slots.sample__sample_type = Slot(uri=AIMSLEAF.sample_type, name="sample__sample_type", curie=AIMSLEAF.curie('sample_type'),
                   model_uri=AIMSLEAF.sample__sample_type, domain=None, range=Union[str, "SampleTypeEnum"])

slots.sample__molecular_weight = Slot(uri=AIMSLEAF.molecular_weight, name="sample__molecular_weight", curie=AIMSLEAF.curie('molecular_weight'),
                   model_uri=AIMSLEAF.sample__molecular_weight, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sample__concentration = Slot(uri=AIMSLEAF.concentration, name="sample__concentration", curie=AIMSLEAF.curie('concentration'),
                   model_uri=AIMSLEAF.sample__concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sample__buffer_composition = Slot(uri=AIMSLEAF.buffer_composition, name="sample__buffer_composition", curie=AIMSLEAF.curie('buffer_composition'),
                   model_uri=AIMSLEAF.sample__buffer_composition, domain=None, range=Optional[Union[dict, BufferComposition]])

slots.sample__preparation_method = Slot(uri=AIMSLEAF.preparation_method, name="sample__preparation_method", curie=AIMSLEAF.curie('preparation_method'),
                   model_uri=AIMSLEAF.sample__preparation_method, domain=None, range=Optional[str])

slots.sample__storage_conditions = Slot(uri=AIMSLEAF.storage_conditions, name="sample__storage_conditions", curie=AIMSLEAF.curie('storage_conditions'),
                   model_uri=AIMSLEAF.sample__storage_conditions, domain=None, range=Optional[Union[dict, StorageConditions]])

slots.sample__organism = Slot(uri=AIMSLEAF.organism, name="sample__organism", curie=AIMSLEAF.curie('organism'),
                   model_uri=AIMSLEAF.sample__organism, domain=None, range=Optional[Union[str, OntologyTermId]])

slots.sample__anatomy = Slot(uri=AIMSLEAF.anatomy, name="sample__anatomy", curie=AIMSLEAF.curie('anatomy'),
                   model_uri=AIMSLEAF.sample__anatomy, domain=None, range=Optional[Union[str, OntologyTermId]])

slots.sample__cell_type = Slot(uri=AIMSLEAF.cell_type, name="sample__cell_type", curie=AIMSLEAF.curie('cell_type'),
                   model_uri=AIMSLEAF.sample__cell_type, domain=None, range=Optional[Union[str, OntologyTermId]])

slots.sample__parent_sample_id = Slot(uri=AIMSLEAF.parent_sample_id, name="sample__parent_sample_id", curie=AIMSLEAF.curie('parent_sample_id'),
                   model_uri=AIMSLEAF.sample__parent_sample_id, domain=None, range=Optional[Union[str, SampleId]])

slots.sample__purity_percentage = Slot(uri=AIMSLEAF.purity_percentage, name="sample__purity_percentage", curie=AIMSLEAF.curie('purity_percentage'),
                   model_uri=AIMSLEAF.sample__purity_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.sample__quality_metrics = Slot(uri=AIMSLEAF.quality_metrics, name="sample__quality_metrics", curie=AIMSLEAF.curie('quality_metrics'),
                   model_uri=AIMSLEAF.sample__quality_metrics, domain=None, range=Optional[str])

slots.samplePreparation__preparation_type = Slot(uri=AIMSLEAF.preparation_type, name="samplePreparation__preparation_type", curie=AIMSLEAF.curie('preparation_type'),
                   model_uri=AIMSLEAF.samplePreparation__preparation_type, domain=None, range=Union[str, "PreparationTypeEnum"])

slots.samplePreparation__sample_id = Slot(uri=AIMSLEAF.sample_id, name="samplePreparation__sample_id", curie=AIMSLEAF.curie('sample_id'),
                   model_uri=AIMSLEAF.samplePreparation__sample_id, domain=None, range=Optional[str])

slots.samplePreparation__preparation_date = Slot(uri=AIMSLEAF.preparation_date, name="samplePreparation__preparation_date", curie=AIMSLEAF.curie('preparation_date'),
                   model_uri=AIMSLEAF.samplePreparation__preparation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.samplePreparation__operator_id = Slot(uri=AIMSLEAF.operator_id, name="samplePreparation__operator_id", curie=AIMSLEAF.curie('operator_id'),
                   model_uri=AIMSLEAF.samplePreparation__operator_id, domain=None, range=Optional[str])

slots.samplePreparation__protocol_description = Slot(uri=AIMSLEAF.protocol_description, name="samplePreparation__protocol_description", curie=AIMSLEAF.curie('protocol_description'),
                   model_uri=AIMSLEAF.samplePreparation__protocol_description, domain=None, range=Optional[str])

slots.samplePreparation__host_strain_or_cell_line = Slot(uri=AIMSLEAF.host_strain_or_cell_line, name="samplePreparation__host_strain_or_cell_line", curie=AIMSLEAF.curie('host_strain_or_cell_line'),
                   model_uri=AIMSLEAF.samplePreparation__host_strain_or_cell_line, domain=None, range=Optional[str])

slots.samplePreparation__culture_volume_l = Slot(uri=AIMSLEAF.culture_volume_l, name="samplePreparation__culture_volume_l", curie=AIMSLEAF.curie('culture_volume_l'),
                   model_uri=AIMSLEAF.samplePreparation__culture_volume_l, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samplePreparation__medium = Slot(uri=AIMSLEAF.medium, name="samplePreparation__medium", curie=AIMSLEAF.curie('medium'),
                   model_uri=AIMSLEAF.samplePreparation__medium, domain=None, range=Optional[str])

slots.samplePreparation__antibiotic_selection = Slot(uri=AIMSLEAF.antibiotic_selection, name="samplePreparation__antibiotic_selection", curie=AIMSLEAF.curie('antibiotic_selection'),
                   model_uri=AIMSLEAF.samplePreparation__antibiotic_selection, domain=None, range=Optional[str])

slots.samplePreparation__growth_temperature_c = Slot(uri=AIMSLEAF.growth_temperature_c, name="samplePreparation__growth_temperature_c", curie=AIMSLEAF.curie('growth_temperature_c'),
                   model_uri=AIMSLEAF.samplePreparation__growth_temperature_c, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samplePreparation__induction_agent = Slot(uri=AIMSLEAF.induction_agent, name="samplePreparation__induction_agent", curie=AIMSLEAF.curie('induction_agent'),
                   model_uri=AIMSLEAF.samplePreparation__induction_agent, domain=None, range=Optional[str])

slots.samplePreparation__inducer_concentration = Slot(uri=AIMSLEAF.inducer_concentration, name="samplePreparation__inducer_concentration", curie=AIMSLEAF.curie('inducer_concentration'),
                   model_uri=AIMSLEAF.samplePreparation__inducer_concentration, domain=None, range=Optional[str])

slots.samplePreparation__induction_temperature_c = Slot(uri=AIMSLEAF.induction_temperature_c, name="samplePreparation__induction_temperature_c", curie=AIMSLEAF.curie('induction_temperature_c'),
                   model_uri=AIMSLEAF.samplePreparation__induction_temperature_c, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samplePreparation__induction_time_h = Slot(uri=AIMSLEAF.induction_time_h, name="samplePreparation__induction_time_h", curie=AIMSLEAF.curie('induction_time_h'),
                   model_uri=AIMSLEAF.samplePreparation__induction_time_h, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samplePreparation__od600_at_induction = Slot(uri=AIMSLEAF.od600_at_induction, name="samplePreparation__od600_at_induction", curie=AIMSLEAF.curie('od600_at_induction'),
                   model_uri=AIMSLEAF.samplePreparation__od600_at_induction, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samplePreparation__harvest_timepoint = Slot(uri=AIMSLEAF.harvest_timepoint, name="samplePreparation__harvest_timepoint", curie=AIMSLEAF.curie('harvest_timepoint'),
                   model_uri=AIMSLEAF.samplePreparation__harvest_timepoint, domain=None, range=Optional[str])

slots.samplePreparation__lysis_method = Slot(uri=AIMSLEAF.lysis_method, name="samplePreparation__lysis_method", curie=AIMSLEAF.curie('lysis_method'),
                   model_uri=AIMSLEAF.samplePreparation__lysis_method, domain=None, range=Optional[str])

slots.samplePreparation__protease_inhibitors = Slot(uri=AIMSLEAF.protease_inhibitors, name="samplePreparation__protease_inhibitors", curie=AIMSLEAF.curie('protease_inhibitors'),
                   model_uri=AIMSLEAF.samplePreparation__protease_inhibitors, domain=None, range=Optional[str])

slots.samplePreparation__affinity_type = Slot(uri=AIMSLEAF.affinity_type, name="samplePreparation__affinity_type", curie=AIMSLEAF.curie('affinity_type'),
                   model_uri=AIMSLEAF.samplePreparation__affinity_type, domain=None, range=Optional[str])

slots.samplePreparation__affinity_column = Slot(uri=AIMSLEAF.affinity_column, name="samplePreparation__affinity_column", curie=AIMSLEAF.curie('affinity_column'),
                   model_uri=AIMSLEAF.samplePreparation__affinity_column, domain=None, range=Optional[str])

slots.samplePreparation__lysis_buffer = Slot(uri=AIMSLEAF.lysis_buffer, name="samplePreparation__lysis_buffer", curie=AIMSLEAF.curie('lysis_buffer'),
                   model_uri=AIMSLEAF.samplePreparation__lysis_buffer, domain=None, range=Optional[str])

slots.samplePreparation__wash_buffer = Slot(uri=AIMSLEAF.wash_buffer, name="samplePreparation__wash_buffer", curie=AIMSLEAF.curie('wash_buffer'),
                   model_uri=AIMSLEAF.samplePreparation__wash_buffer, domain=None, range=Optional[str])

slots.samplePreparation__elution_buffer = Slot(uri=AIMSLEAF.elution_buffer, name="samplePreparation__elution_buffer", curie=AIMSLEAF.curie('elution_buffer'),
                   model_uri=AIMSLEAF.samplePreparation__elution_buffer, domain=None, range=Optional[str])

slots.samplePreparation__tag_removal = Slot(uri=AIMSLEAF.tag_removal, name="samplePreparation__tag_removal", curie=AIMSLEAF.curie('tag_removal'),
                   model_uri=AIMSLEAF.samplePreparation__tag_removal, domain=None, range=Optional[Union[bool, Bool]])

slots.samplePreparation__protease = Slot(uri=AIMSLEAF.protease, name="samplePreparation__protease", curie=AIMSLEAF.curie('protease'),
                   model_uri=AIMSLEAF.samplePreparation__protease, domain=None, range=Optional[str])

slots.samplePreparation__protease_ratio = Slot(uri=AIMSLEAF.protease_ratio, name="samplePreparation__protease_ratio", curie=AIMSLEAF.curie('protease_ratio'),
                   model_uri=AIMSLEAF.samplePreparation__protease_ratio, domain=None, range=Optional[str])

slots.samplePreparation__cleavage_time_h = Slot(uri=AIMSLEAF.cleavage_time_h, name="samplePreparation__cleavage_time_h", curie=AIMSLEAF.curie('cleavage_time_h'),
                   model_uri=AIMSLEAF.samplePreparation__cleavage_time_h, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samplePreparation__cleavage_temperature_c = Slot(uri=AIMSLEAF.cleavage_temperature_c, name="samplePreparation__cleavage_temperature_c", curie=AIMSLEAF.curie('cleavage_temperature_c'),
                   model_uri=AIMSLEAF.samplePreparation__cleavage_temperature_c, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samplePreparation__second_affinity_reverse = Slot(uri=AIMSLEAF.second_affinity_reverse, name="samplePreparation__second_affinity_reverse", curie=AIMSLEAF.curie('second_affinity_reverse'),
                   model_uri=AIMSLEAF.samplePreparation__second_affinity_reverse, domain=None, range=Optional[str])

slots.samplePreparation__iex_column = Slot(uri=AIMSLEAF.iex_column, name="samplePreparation__iex_column", curie=AIMSLEAF.curie('iex_column'),
                   model_uri=AIMSLEAF.samplePreparation__iex_column, domain=None, range=Optional[str])

slots.samplePreparation__hic_column = Slot(uri=AIMSLEAF.hic_column, name="samplePreparation__hic_column", curie=AIMSLEAF.curie('hic_column'),
                   model_uri=AIMSLEAF.samplePreparation__hic_column, domain=None, range=Optional[str])

slots.samplePreparation__sec_column = Slot(uri=AIMSLEAF.sec_column, name="samplePreparation__sec_column", curie=AIMSLEAF.curie('sec_column'),
                   model_uri=AIMSLEAF.samplePreparation__sec_column, domain=None, range=Optional[str])

slots.samplePreparation__sec_buffer = Slot(uri=AIMSLEAF.sec_buffer, name="samplePreparation__sec_buffer", curie=AIMSLEAF.curie('sec_buffer'),
                   model_uri=AIMSLEAF.samplePreparation__sec_buffer, domain=None, range=Optional[str])

slots.samplePreparation__concentration_method = Slot(uri=AIMSLEAF.concentration_method, name="samplePreparation__concentration_method", curie=AIMSLEAF.curie('concentration_method'),
                   model_uri=AIMSLEAF.samplePreparation__concentration_method, domain=None, range=Optional[str])

slots.samplePreparation__final_buffer = Slot(uri=AIMSLEAF.final_buffer, name="samplePreparation__final_buffer", curie=AIMSLEAF.curie('final_buffer'),
                   model_uri=AIMSLEAF.samplePreparation__final_buffer, domain=None, range=Optional[str])

slots.samplePreparation__final_concentration_mg_per_ml = Slot(uri=AIMSLEAF.final_concentration_mg_per_ml, name="samplePreparation__final_concentration_mg_per_ml", curie=AIMSLEAF.curie('final_concentration_mg_per_ml'),
                   model_uri=AIMSLEAF.samplePreparation__final_concentration_mg_per_ml, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samplePreparation__yield_mg = Slot(uri=AIMSLEAF.yield_mg, name="samplePreparation__yield_mg", curie=AIMSLEAF.curie('yield_mg'),
                   model_uri=AIMSLEAF.samplePreparation__yield_mg, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samplePreparation__purity_by_sds_page_percent = Slot(uri=AIMSLEAF.purity_by_sds_page_percent, name="samplePreparation__purity_by_sds_page_percent", curie=AIMSLEAF.curie('purity_by_sds_page_percent'),
                   model_uri=AIMSLEAF.samplePreparation__purity_by_sds_page_percent, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.samplePreparation__aggregation_assessment = Slot(uri=AIMSLEAF.aggregation_assessment, name="samplePreparation__aggregation_assessment", curie=AIMSLEAF.curie('aggregation_assessment'),
                   model_uri=AIMSLEAF.samplePreparation__aggregation_assessment, domain=None, range=Optional[str])

slots.samplePreparation__aliquoting = Slot(uri=AIMSLEAF.aliquoting, name="samplePreparation__aliquoting", curie=AIMSLEAF.curie('aliquoting'),
                   model_uri=AIMSLEAF.samplePreparation__aliquoting, domain=None, range=Optional[str])

slots.instrument__instrument_code = Slot(uri=AIMSLEAF.instrument_code, name="instrument__instrument_code", curie=AIMSLEAF.curie('instrument_code'),
                   model_uri=AIMSLEAF.instrument__instrument_code, domain=None, range=str)

slots.instrument__instrument_category = Slot(uri=AIMSLEAF.instrument_category, name="instrument__instrument_category", curie=AIMSLEAF.curie('instrument_category'),
                   model_uri=AIMSLEAF.instrument__instrument_category, domain=None, range=Optional[Union[str, "InstrumentCategoryEnum"]])

slots.instrument__facility_name = Slot(uri=AIMSLEAF.facility_name, name="instrument__facility_name", curie=AIMSLEAF.curie('facility_name'),
                   model_uri=AIMSLEAF.instrument__facility_name, domain=None, range=Optional[Union[str, "FacilityEnum"]])

slots.instrument__facility_ror = Slot(uri=AIMSLEAF.facility_ror, name="instrument__facility_ror", curie=AIMSLEAF.curie('facility_ror'),
                   model_uri=AIMSLEAF.instrument__facility_ror, domain=None, range=Optional[Union[str, URIorCURIE]],
                   pattern=re.compile(r'^https://ror\.org/\w+$'))

slots.instrument__beamline_id = Slot(uri=MMCIF['_diffrn_source.pdbx_synchrotron_beamline'], name="instrument__beamline_id", curie=MMCIF.curie('_diffrn_source.pdbx_synchrotron_beamline'),
                   model_uri=AIMSLEAF.instrument__beamline_id, domain=None, range=Optional[str])

slots.instrument__manufacturer = Slot(uri=AIMSLEAF.manufacturer, name="instrument__manufacturer", curie=AIMSLEAF.curie('manufacturer'),
                   model_uri=AIMSLEAF.instrument__manufacturer, domain=None, range=Optional[str])

slots.instrument__model = Slot(uri=AIMSLEAF.model, name="instrument__model", curie=AIMSLEAF.curie('model'),
                   model_uri=AIMSLEAF.instrument__model, domain=None, range=Optional[str])

slots.instrument__installation_date = Slot(uri=AIMSLEAF.installation_date, name="instrument__installation_date", curie=AIMSLEAF.curie('installation_date'),
                   model_uri=AIMSLEAF.instrument__installation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.instrument__current_status = Slot(uri=AIMSLEAF.current_status, name="instrument__current_status", curie=AIMSLEAF.curie('current_status'),
                   model_uri=AIMSLEAF.instrument__current_status, domain=None, range=Optional[Union[str, "InstrumentStatusEnum"]])

slots.cryoEMInstrument__accelerating_voltage = Slot(uri=AIMSLEAF.accelerating_voltage, name="cryoEMInstrument__accelerating_voltage", curie=AIMSLEAF.curie('accelerating_voltage'),
                   model_uri=AIMSLEAF.cryoEMInstrument__accelerating_voltage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMInstrument__cs_corrector = Slot(uri=AIMSLEAF.cs_corrector, name="cryoEMInstrument__cs_corrector", curie=AIMSLEAF.curie('cs_corrector'),
                   model_uri=AIMSLEAF.cryoEMInstrument__cs_corrector, domain=None, range=Optional[Union[bool, Bool]])

slots.cryoEMInstrument__phase_plate = Slot(uri=AIMSLEAF.phase_plate, name="cryoEMInstrument__phase_plate", curie=AIMSLEAF.curie('phase_plate'),
                   model_uri=AIMSLEAF.cryoEMInstrument__phase_plate, domain=None, range=Optional[Union[bool, Bool]])

slots.cryoEMInstrument__detector_technology = Slot(uri=AIMSLEAF.detector_technology, name="cryoEMInstrument__detector_technology", curie=AIMSLEAF.curie('detector_technology'),
                   model_uri=AIMSLEAF.cryoEMInstrument__detector_technology, domain=None, range=Optional[Union[str, "DetectorTechnologyEnum"]])

slots.cryoEMInstrument__detector_manufacturer = Slot(uri=AIMSLEAF.detector_manufacturer, name="cryoEMInstrument__detector_manufacturer", curie=AIMSLEAF.curie('detector_manufacturer'),
                   model_uri=AIMSLEAF.cryoEMInstrument__detector_manufacturer, domain=None, range=Optional[str])

slots.cryoEMInstrument__detector_model = Slot(uri=AIMSLEAF.detector_model, name="cryoEMInstrument__detector_model", curie=AIMSLEAF.curie('detector_model'),
                   model_uri=AIMSLEAF.cryoEMInstrument__detector_model, domain=None, range=Optional[str])

slots.cryoEMInstrument__detector_mode = Slot(uri=AIMSLEAF.detector_mode, name="cryoEMInstrument__detector_mode", curie=AIMSLEAF.curie('detector_mode'),
                   model_uri=AIMSLEAF.cryoEMInstrument__detector_mode, domain=None, range=Optional[Union[str, "DetectorModeEnum"]])

slots.cryoEMInstrument__detector_position = Slot(uri=AIMSLEAF.detector_position, name="cryoEMInstrument__detector_position", curie=AIMSLEAF.curie('detector_position'),
                   model_uri=AIMSLEAF.cryoEMInstrument__detector_position, domain=None, range=Optional[str])

slots.cryoEMInstrument__detector_dimensions = Slot(uri=AIMSLEAF.detector_dimensions, name="cryoEMInstrument__detector_dimensions", curie=AIMSLEAF.curie('detector_dimensions'),
                   model_uri=AIMSLEAF.cryoEMInstrument__detector_dimensions, domain=None, range=Optional[str])

slots.cryoEMInstrument__pixel_size_physical_um = Slot(uri=AIMSLEAF.pixel_size_physical_um, name="cryoEMInstrument__pixel_size_physical_um", curie=AIMSLEAF.curie('pixel_size_physical_um'),
                   model_uri=AIMSLEAF.cryoEMInstrument__pixel_size_physical_um, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMInstrument__autoloader_capacity = Slot(uri=AIMSLEAF.autoloader_capacity, name="cryoEMInstrument__autoloader_capacity", curie=AIMSLEAF.curie('autoloader_capacity'),
                   model_uri=AIMSLEAF.cryoEMInstrument__autoloader_capacity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMInstrument__cs = Slot(uri=AIMSLEAF.cs, name="cryoEMInstrument__cs", curie=AIMSLEAF.curie('cs'),
                   model_uri=AIMSLEAF.cryoEMInstrument__cs, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMInstrument__c2_aperture = Slot(uri=AIMSLEAF.c2_aperture, name="cryoEMInstrument__c2_aperture", curie=AIMSLEAF.curie('c2_aperture'),
                   model_uri=AIMSLEAF.cryoEMInstrument__c2_aperture, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMInstrument__objective_aperture = Slot(uri=AIMSLEAF.objective_aperture, name="cryoEMInstrument__objective_aperture", curie=AIMSLEAF.curie('objective_aperture'),
                   model_uri=AIMSLEAF.cryoEMInstrument__objective_aperture, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMInstrument__phase_plate_type = Slot(uri=AIMSLEAF.phase_plate_type, name="cryoEMInstrument__phase_plate_type", curie=AIMSLEAF.curie('phase_plate_type'),
                   model_uri=AIMSLEAF.cryoEMInstrument__phase_plate_type, domain=None, range=Optional[str])

slots.cryoEMInstrument__energy_filter_present = Slot(uri=AIMSLEAF.energy_filter_present, name="cryoEMInstrument__energy_filter_present", curie=AIMSLEAF.curie('energy_filter_present'),
                   model_uri=AIMSLEAF.cryoEMInstrument__energy_filter_present, domain=None, range=Optional[Union[bool, Bool]])

slots.cryoEMInstrument__energy_filter_make = Slot(uri=AIMSLEAF.energy_filter_make, name="cryoEMInstrument__energy_filter_make", curie=AIMSLEAF.curie('energy_filter_make'),
                   model_uri=AIMSLEAF.cryoEMInstrument__energy_filter_make, domain=None, range=Optional[str])

slots.cryoEMInstrument__energy_filter_model = Slot(uri=AIMSLEAF.energy_filter_model, name="cryoEMInstrument__energy_filter_model", curie=AIMSLEAF.curie('energy_filter_model'),
                   model_uri=AIMSLEAF.cryoEMInstrument__energy_filter_model, domain=None, range=Optional[str])

slots.cryoEMInstrument__energy_filter_slit_width = Slot(uri=AIMSLEAF.energy_filter_slit_width, name="cryoEMInstrument__energy_filter_slit_width", curie=AIMSLEAF.curie('energy_filter_slit_width'),
                   model_uri=AIMSLEAF.cryoEMInstrument__energy_filter_slit_width, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMInstrument__pixel_size_physical = Slot(uri=AIMSLEAF.pixel_size_physical, name="cryoEMInstrument__pixel_size_physical", curie=AIMSLEAF.curie('pixel_size_physical'),
                   model_uri=AIMSLEAF.cryoEMInstrument__pixel_size_physical, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMInstrument__microscope_software = Slot(uri=AIMSLEAF.microscope_software, name="cryoEMInstrument__microscope_software", curie=AIMSLEAF.curie('microscope_software'),
                   model_uri=AIMSLEAF.cryoEMInstrument__microscope_software, domain=None, range=Optional[str])

slots.cryoEMInstrument__microscope_software_version = Slot(uri=AIMSLEAF.microscope_software_version, name="cryoEMInstrument__microscope_software_version", curie=AIMSLEAF.curie('microscope_software_version'),
                   model_uri=AIMSLEAF.cryoEMInstrument__microscope_software_version, domain=None, range=Optional[str])

slots.cryoEMInstrument__spotsize = Slot(uri=AIMSLEAF.spotsize, name="cryoEMInstrument__spotsize", curie=AIMSLEAF.curie('spotsize'),
                   model_uri=AIMSLEAF.cryoEMInstrument__spotsize, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMInstrument__gunlens = Slot(uri=AIMSLEAF.gunlens, name="cryoEMInstrument__gunlens", curie=AIMSLEAF.curie('gunlens'),
                   model_uri=AIMSLEAF.cryoEMInstrument__gunlens, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMInstrument__imaging_mode = Slot(uri=AIMSLEAF.imaging_mode, name="cryoEMInstrument__imaging_mode", curie=AIMSLEAF.curie('imaging_mode'),
                   model_uri=AIMSLEAF.cryoEMInstrument__imaging_mode, domain=None, range=Optional[Union[str, "ImagingModeEnum"]])

slots.cryoEMInstrument__tem_beam_diameter = Slot(uri=AIMSLEAF.tem_beam_diameter, name="cryoEMInstrument__tem_beam_diameter", curie=AIMSLEAF.curie('tem_beam_diameter'),
                   model_uri=AIMSLEAF.cryoEMInstrument__tem_beam_diameter, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRayInstrument__source_type = Slot(uri=AIMSLEAF.source_type, name="xRayInstrument__source_type", curie=AIMSLEAF.curie('source_type'),
                   model_uri=AIMSLEAF.xRayInstrument__source_type, domain=None, range=Optional[Union[str, "XRaySourceTypeEnum"]])

slots.xRayInstrument__detector_technology = Slot(uri=NSLS2.Detector, name="xRayInstrument__detector_technology", curie=NSLS2.curie('Detector'),
                   model_uri=AIMSLEAF.xRayInstrument__detector_technology, domain=None, range=Optional[Union[str, "DetectorTechnologyEnum"]])

slots.xRayInstrument__detector_manufacturer = Slot(uri=AIMSLEAF.detector_manufacturer, name="xRayInstrument__detector_manufacturer", curie=AIMSLEAF.curie('detector_manufacturer'),
                   model_uri=AIMSLEAF.xRayInstrument__detector_manufacturer, domain=None, range=Optional[str])

slots.xRayInstrument__detector_model = Slot(uri=AIMSLEAF.detector_model, name="xRayInstrument__detector_model", curie=AIMSLEAF.curie('detector_model'),
                   model_uri=AIMSLEAF.xRayInstrument__detector_model, domain=None, range=Optional[str])

slots.xRayInstrument__energy_min = Slot(uri=AIMSLEAF.energy_min, name="xRayInstrument__energy_min", curie=AIMSLEAF.curie('energy_min'),
                   model_uri=AIMSLEAF.xRayInstrument__energy_min, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRayInstrument__energy_max = Slot(uri=AIMSLEAF.energy_max, name="xRayInstrument__energy_max", curie=AIMSLEAF.curie('energy_max'),
                   model_uri=AIMSLEAF.xRayInstrument__energy_max, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRayInstrument__beam_size_min = Slot(uri=AIMSLEAF.beam_size_min, name="xRayInstrument__beam_size_min", curie=AIMSLEAF.curie('beam_size_min'),
                   model_uri=AIMSLEAF.xRayInstrument__beam_size_min, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRayInstrument__beam_size_max = Slot(uri=AIMSLEAF.beam_size_max, name="xRayInstrument__beam_size_max", curie=AIMSLEAF.curie('beam_size_max'),
                   model_uri=AIMSLEAF.xRayInstrument__beam_size_max, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRayInstrument__flux_density = Slot(uri=AIMSLEAF.flux_density, name="xRayInstrument__flux_density", curie=AIMSLEAF.curie('flux_density'),
                   model_uri=AIMSLEAF.xRayInstrument__flux_density, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRayInstrument__monochromator_type = Slot(uri=AIMSLEAF.monochromator_type, name="xRayInstrument__monochromator_type", curie=AIMSLEAF.curie('monochromator_type'),
                   model_uri=AIMSLEAF.xRayInstrument__monochromator_type, domain=None, range=Optional[str])

slots.xRayInstrument__goniometer_type = Slot(uri=AIMSLEAF.goniometer_type, name="xRayInstrument__goniometer_type", curie=AIMSLEAF.curie('goniometer_type'),
                   model_uri=AIMSLEAF.xRayInstrument__goniometer_type, domain=None, range=Optional[str])

slots.xRayInstrument__crystal_cooling_capability = Slot(uri=AIMSLEAF.crystal_cooling_capability, name="xRayInstrument__crystal_cooling_capability", curie=AIMSLEAF.curie('crystal_cooling_capability'),
                   model_uri=AIMSLEAF.xRayInstrument__crystal_cooling_capability, domain=None, range=Optional[Union[bool, Bool]])

slots.experimentRun__experiment_code = Slot(uri=AIMSLEAF.experiment_code, name="experimentRun__experiment_code", curie=AIMSLEAF.curie('experiment_code'),
                   model_uri=AIMSLEAF.experimentRun__experiment_code, domain=None, range=str)

slots.experimentRun__experiment_date = Slot(uri=AIMSLEAF.experiment_date, name="experimentRun__experiment_date", curie=AIMSLEAF.curie('experiment_date'),
                   model_uri=AIMSLEAF.experimentRun__experiment_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.experimentRun__operator_id = Slot(uri=AIMSLEAF.operator_id, name="experimentRun__operator_id", curie=AIMSLEAF.curie('operator_id'),
                   model_uri=AIMSLEAF.experimentRun__operator_id, domain=None, range=Optional[str])

slots.experimentRun__technique = Slot(uri=AIMSLEAF.technique, name="experimentRun__technique", curie=AIMSLEAF.curie('technique'),
                   model_uri=AIMSLEAF.experimentRun__technique, domain=None, range=Union[str, "TechniqueEnum"])

slots.experimentRun__experimental_conditions = Slot(uri=AIMSLEAF.experimental_conditions, name="experimentRun__experimental_conditions", curie=AIMSLEAF.curie('experimental_conditions'),
                   model_uri=AIMSLEAF.experimentRun__experimental_conditions, domain=None, range=Optional[Union[dict, ExperimentalConditions]])

slots.experimentRun__data_collection_strategy = Slot(uri=AIMSLEAF.data_collection_strategy, name="experimentRun__data_collection_strategy", curie=AIMSLEAF.curie('data_collection_strategy'),
                   model_uri=AIMSLEAF.experimentRun__data_collection_strategy, domain=None, range=Optional[Union[dict, DataCollectionStrategy]])

slots.experimentRun__raw_data_location = Slot(uri=AIMSLEAF.raw_data_location, name="experimentRun__raw_data_location", curie=AIMSLEAF.curie('raw_data_location'),
                   model_uri=AIMSLEAF.experimentRun__raw_data_location, domain=None, range=Optional[str])

slots.experimentRun__processing_status = Slot(uri=AIMSLEAF.processing_status, name="experimentRun__processing_status", curie=AIMSLEAF.curie('processing_status'),
                   model_uri=AIMSLEAF.experimentRun__processing_status, domain=None, range=Optional[Union[str, "ProcessingStatusEnum"]])

slots.experimentRun__magnification = Slot(uri=AIMSLEAF.magnification, name="experimentRun__magnification", curie=AIMSLEAF.curie('magnification'),
                   model_uri=AIMSLEAF.experimentRun__magnification, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__calibrated_pixel_size = Slot(uri=AIMSLEAF.calibrated_pixel_size, name="experimentRun__calibrated_pixel_size", curie=AIMSLEAF.curie('calibrated_pixel_size'),
                   model_uri=AIMSLEAF.experimentRun__calibrated_pixel_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__camera_binning = Slot(uri=AIMSLEAF.camera_binning, name="experimentRun__camera_binning", curie=AIMSLEAF.curie('camera_binning'),
                   model_uri=AIMSLEAF.experimentRun__camera_binning, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__exposure_time_per_frame = Slot(uri=AIMSLEAF.exposure_time_per_frame, name="experimentRun__exposure_time_per_frame", curie=AIMSLEAF.curie('exposure_time_per_frame'),
                   model_uri=AIMSLEAF.experimentRun__exposure_time_per_frame, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__frames_per_movie = Slot(uri=AIMSLEAF.frames_per_movie, name="experimentRun__frames_per_movie", curie=AIMSLEAF.curie('frames_per_movie'),
                   model_uri=AIMSLEAF.experimentRun__frames_per_movie, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__total_exposure_time = Slot(uri=AIMSLEAF.total_exposure_time, name="experimentRun__total_exposure_time", curie=AIMSLEAF.curie('total_exposure_time'),
                   model_uri=AIMSLEAF.experimentRun__total_exposure_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__total_dose = Slot(uri=AIMSLEAF.total_dose, name="experimentRun__total_dose", curie=AIMSLEAF.curie('total_dose'),
                   model_uri=AIMSLEAF.experimentRun__total_dose, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__dose_rate = Slot(uri=AIMSLEAF.dose_rate, name="experimentRun__dose_rate", curie=AIMSLEAF.curie('dose_rate'),
                   model_uri=AIMSLEAF.experimentRun__dose_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__defocus_target = Slot(uri=AIMSLEAF.defocus_target, name="experimentRun__defocus_target", curie=AIMSLEAF.curie('defocus_target'),
                   model_uri=AIMSLEAF.experimentRun__defocus_target, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__defocus_range_min = Slot(uri=AIMSLEAF.defocus_range_min, name="experimentRun__defocus_range_min", curie=AIMSLEAF.curie('defocus_range_min'),
                   model_uri=AIMSLEAF.experimentRun__defocus_range_min, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__defocus_range_max = Slot(uri=AIMSLEAF.defocus_range_max, name="experimentRun__defocus_range_max", curie=AIMSLEAF.curie('defocus_range_max'),
                   model_uri=AIMSLEAF.experimentRun__defocus_range_max, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__defocus_range_increment = Slot(uri=AIMSLEAF.defocus_range_increment, name="experimentRun__defocus_range_increment", curie=AIMSLEAF.curie('defocus_range_increment'),
                   model_uri=AIMSLEAF.experimentRun__defocus_range_increment, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__astigmatism_target = Slot(uri=AIMSLEAF.astigmatism_target, name="experimentRun__astigmatism_target", curie=AIMSLEAF.curie('astigmatism_target'),
                   model_uri=AIMSLEAF.experimentRun__astigmatism_target, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__coma = Slot(uri=AIMSLEAF.coma, name="experimentRun__coma", curie=AIMSLEAF.curie('coma'),
                   model_uri=AIMSLEAF.experimentRun__coma, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__stage_tilt = Slot(uri=AIMSLEAF.stage_tilt, name="experimentRun__stage_tilt", curie=AIMSLEAF.curie('stage_tilt'),
                   model_uri=AIMSLEAF.experimentRun__stage_tilt, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__autoloader_slot = Slot(uri=AIMSLEAF.autoloader_slot, name="experimentRun__autoloader_slot", curie=AIMSLEAF.curie('autoloader_slot'),
                   model_uri=AIMSLEAF.experimentRun__autoloader_slot, domain=None, range=Optional[str])

slots.experimentRun__shots_per_hole = Slot(uri=AIMSLEAF.shots_per_hole, name="experimentRun__shots_per_hole", curie=AIMSLEAF.curie('shots_per_hole'),
                   model_uri=AIMSLEAF.experimentRun__shots_per_hole, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__holes_per_group = Slot(uri=AIMSLEAF.holes_per_group, name="experimentRun__holes_per_group", curie=AIMSLEAF.curie('holes_per_group'),
                   model_uri=AIMSLEAF.experimentRun__holes_per_group, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__acquisition_software = Slot(uri=AIMSLEAF.acquisition_software, name="experimentRun__acquisition_software", curie=AIMSLEAF.curie('acquisition_software'),
                   model_uri=AIMSLEAF.experimentRun__acquisition_software, domain=None, range=Optional[str])

slots.experimentRun__acquisition_software_version = Slot(uri=AIMSLEAF.acquisition_software_version, name="experimentRun__acquisition_software_version", curie=AIMSLEAF.curie('acquisition_software_version'),
                   model_uri=AIMSLEAF.experimentRun__acquisition_software_version, domain=None, range=Optional[str])

slots.experimentRun__wavelength = Slot(uri=AIMSLEAF.wavelength, name="experimentRun__wavelength", curie=AIMSLEAF.curie('wavelength'),
                   model_uri=AIMSLEAF.experimentRun__wavelength, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__oscillation_angle = Slot(uri=AIMSLEAF.oscillation_angle, name="experimentRun__oscillation_angle", curie=AIMSLEAF.curie('oscillation_angle'),
                   model_uri=AIMSLEAF.experimentRun__oscillation_angle, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__start_angle = Slot(uri=AIMSLEAF.start_angle, name="experimentRun__start_angle", curie=AIMSLEAF.curie('start_angle'),
                   model_uri=AIMSLEAF.experimentRun__start_angle, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__number_of_images = Slot(uri=AIMSLEAF.number_of_images, name="experimentRun__number_of_images", curie=AIMSLEAF.curie('number_of_images'),
                   model_uri=AIMSLEAF.experimentRun__number_of_images, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__beam_center_x = Slot(uri=AIMSLEAF.beam_center_x, name="experimentRun__beam_center_x", curie=AIMSLEAF.curie('beam_center_x'),
                   model_uri=AIMSLEAF.experimentRun__beam_center_x, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__beam_center_y = Slot(uri=AIMSLEAF.beam_center_y, name="experimentRun__beam_center_y", curie=AIMSLEAF.curie('beam_center_y'),
                   model_uri=AIMSLEAF.experimentRun__beam_center_y, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__detector_distance = Slot(uri=AIMSLEAF.detector_distance, name="experimentRun__detector_distance", curie=AIMSLEAF.curie('detector_distance'),
                   model_uri=AIMSLEAF.experimentRun__detector_distance, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__pixel_size_x = Slot(uri=AIMSLEAF.pixel_size_x, name="experimentRun__pixel_size_x", curie=AIMSLEAF.curie('pixel_size_x'),
                   model_uri=AIMSLEAF.experimentRun__pixel_size_x, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__pixel_size_y = Slot(uri=AIMSLEAF.pixel_size_y, name="experimentRun__pixel_size_y", curie=AIMSLEAF.curie('pixel_size_y'),
                   model_uri=AIMSLEAF.experimentRun__pixel_size_y, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__total_rotation = Slot(uri=AIMSLEAF.total_rotation, name="experimentRun__total_rotation", curie=AIMSLEAF.curie('total_rotation'),
                   model_uri=AIMSLEAF.experimentRun__total_rotation, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__beamline = Slot(uri=AIMSLEAF.beamline, name="experimentRun__beamline", curie=AIMSLEAF.curie('beamline'),
                   model_uri=AIMSLEAF.experimentRun__beamline, domain=None, range=Optional[str])

slots.experimentRun__transmission = Slot(uri=AIMSLEAF.transmission, name="experimentRun__transmission", curie=AIMSLEAF.curie('transmission'),
                   model_uri=AIMSLEAF.experimentRun__transmission, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__flux = Slot(uri=AIMSLEAF.flux, name="experimentRun__flux", curie=AIMSLEAF.curie('flux'),
                   model_uri=AIMSLEAF.experimentRun__flux, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__flux_end = Slot(uri=AIMSLEAF.flux_end, name="experimentRun__flux_end", curie=AIMSLEAF.curie('flux_end'),
                   model_uri=AIMSLEAF.experimentRun__flux_end, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__slit_gap_horizontal = Slot(uri=AIMSLEAF.slit_gap_horizontal, name="experimentRun__slit_gap_horizontal", curie=AIMSLEAF.curie('slit_gap_horizontal'),
                   model_uri=AIMSLEAF.experimentRun__slit_gap_horizontal, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__slit_gap_vertical = Slot(uri=AIMSLEAF.slit_gap_vertical, name="experimentRun__slit_gap_vertical", curie=AIMSLEAF.curie('slit_gap_vertical'),
                   model_uri=AIMSLEAF.experimentRun__slit_gap_vertical, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__undulator_gap = Slot(uri=AIMSLEAF.undulator_gap, name="experimentRun__undulator_gap", curie=AIMSLEAF.curie('undulator_gap'),
                   model_uri=AIMSLEAF.experimentRun__undulator_gap, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__synchrotron_mode = Slot(uri=AIMSLEAF.synchrotron_mode, name="experimentRun__synchrotron_mode", curie=AIMSLEAF.curie('synchrotron_mode'),
                   model_uri=AIMSLEAF.experimentRun__synchrotron_mode, domain=None, range=Optional[str])

slots.experimentRun__exposure_time = Slot(uri=AIMSLEAF.exposure_time, name="experimentRun__exposure_time", curie=AIMSLEAF.curie('exposure_time'),
                   model_uri=AIMSLEAF.experimentRun__exposure_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__start_time = Slot(uri=AIMSLEAF.start_time, name="experimentRun__start_time", curie=AIMSLEAF.curie('start_time'),
                   model_uri=AIMSLEAF.experimentRun__start_time, domain=None, range=Optional[str])

slots.experimentRun__end_time = Slot(uri=AIMSLEAF.end_time, name="experimentRun__end_time", curie=AIMSLEAF.curie('end_time'),
                   model_uri=AIMSLEAF.experimentRun__end_time, domain=None, range=Optional[str])

slots.experimentRun__resolution = Slot(uri=AIMSLEAF.resolution, name="experimentRun__resolution", curie=AIMSLEAF.curie('resolution'),
                   model_uri=AIMSLEAF.experimentRun__resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__resolution_at_corner = Slot(uri=AIMSLEAF.resolution_at_corner, name="experimentRun__resolution_at_corner", curie=AIMSLEAF.curie('resolution_at_corner'),
                   model_uri=AIMSLEAF.experimentRun__resolution_at_corner, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__ispyb_data_collection_id = Slot(uri=AIMSLEAF.ispyb_data_collection_id, name="experimentRun__ispyb_data_collection_id", curie=AIMSLEAF.curie('ispyb_data_collection_id'),
                   model_uri=AIMSLEAF.experimentRun__ispyb_data_collection_id, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__ispyb_session_id = Slot(uri=AIMSLEAF.ispyb_session_id, name="experimentRun__ispyb_session_id", curie=AIMSLEAF.curie('ispyb_session_id'),
                   model_uri=AIMSLEAF.experimentRun__ispyb_session_id, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__beam_size_x = Slot(uri=AIMSLEAF.beam_size_x, name="experimentRun__beam_size_x", curie=AIMSLEAF.curie('beam_size_x'),
                   model_uri=AIMSLEAF.experimentRun__beam_size_x, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__beam_size_y = Slot(uri=AIMSLEAF.beam_size_y, name="experimentRun__beam_size_y", curie=AIMSLEAF.curie('beam_size_y'),
                   model_uri=AIMSLEAF.experimentRun__beam_size_y, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__dwell_time = Slot(uri=AIMSLEAF.dwell_time, name="experimentRun__dwell_time", curie=AIMSLEAF.curie('dwell_time'),
                   model_uri=AIMSLEAF.experimentRun__dwell_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__energy = Slot(uri=AIMSLEAF.energy, name="experimentRun__energy", curie=AIMSLEAF.curie('energy'),
                   model_uri=AIMSLEAF.experimentRun__energy, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentRun__beamline_parameters = Slot(uri=AIMSLEAF.beamline_parameters, name="experimentRun__beamline_parameters", curie=AIMSLEAF.curie('beamline_parameters'),
                   model_uri=AIMSLEAF.experimentRun__beamline_parameters, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.workflowRun__workflow_code = Slot(uri=AIMSLEAF.workflow_code, name="workflowRun__workflow_code", curie=AIMSLEAF.curie('workflow_code'),
                   model_uri=AIMSLEAF.workflowRun__workflow_code, domain=None, range=str)

slots.workflowRun__workflow_type = Slot(uri=AIMSLEAF.workflow_type, name="workflowRun__workflow_type", curie=AIMSLEAF.curie('workflow_type'),
                   model_uri=AIMSLEAF.workflowRun__workflow_type, domain=None, range=Union[str, "WorkflowTypeEnum"])

slots.workflowRun__processing_level = Slot(uri=AIMSLEAF.processing_level, name="workflowRun__processing_level", curie=AIMSLEAF.curie('processing_level'),
                   model_uri=AIMSLEAF.workflowRun__processing_level, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.workflowRun__software_name = Slot(uri=AIMSLEAF.software_name, name="workflowRun__software_name", curie=AIMSLEAF.curie('software_name'),
                   model_uri=AIMSLEAF.workflowRun__software_name, domain=None, range=str)

slots.workflowRun__software_version = Slot(uri=AIMSLEAF.software_version, name="workflowRun__software_version", curie=AIMSLEAF.curie('software_version'),
                   model_uri=AIMSLEAF.workflowRun__software_version, domain=None, range=Optional[str])

slots.workflowRun__additional_software = Slot(uri=AIMSLEAF.additional_software, name="workflowRun__additional_software", curie=AIMSLEAF.curie('additional_software'),
                   model_uri=AIMSLEAF.workflowRun__additional_software, domain=None, range=Optional[str])

slots.workflowRun__processing_parameters = Slot(uri=AIMSLEAF.processing_parameters, name="workflowRun__processing_parameters", curie=AIMSLEAF.curie('processing_parameters'),
                   model_uri=AIMSLEAF.workflowRun__processing_parameters, domain=None, range=Optional[str])

slots.workflowRun__parameters_file_path = Slot(uri=AIMSLEAF.parameters_file_path, name="workflowRun__parameters_file_path", curie=AIMSLEAF.curie('parameters_file_path'),
                   model_uri=AIMSLEAF.workflowRun__parameters_file_path, domain=None, range=Optional[str])

slots.dataFile__file_name = Slot(uri=AIMSLEAF.file_name, name="dataFile__file_name", curie=AIMSLEAF.curie('file_name'),
                   model_uri=AIMSLEAF.dataFile__file_name, domain=None, range=str)

slots.dataFile__file_path = Slot(uri=AIMSLEAF.file_path, name="dataFile__file_path", curie=AIMSLEAF.curie('file_path'),
                   model_uri=AIMSLEAF.dataFile__file_path, domain=None, range=Optional[str])

slots.dataFile__file_format = Slot(uri=AIMSLEAF.file_format, name="dataFile__file_format", curie=AIMSLEAF.curie('file_format'),
                   model_uri=AIMSLEAF.dataFile__file_format, domain=None, range=Union[str, "FileFormatEnum"])

slots.dataFile__file_size_bytes = Slot(uri=AIMSLEAF.file_size_bytes, name="dataFile__file_size_bytes", curie=AIMSLEAF.curie('file_size_bytes'),
                   model_uri=AIMSLEAF.dataFile__file_size_bytes, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataFile__checksum = Slot(uri=AIMSLEAF.checksum, name="dataFile__checksum", curie=AIMSLEAF.curie('checksum'),
                   model_uri=AIMSLEAF.dataFile__checksum, domain=None, range=Optional[str])

slots.dataFile__creation_date = Slot(uri=AIMSLEAF.creation_date, name="dataFile__creation_date", curie=AIMSLEAF.curie('creation_date'),
                   model_uri=AIMSLEAF.dataFile__creation_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.dataFile__data_type = Slot(uri=AIMSLEAF.data_type, name="dataFile__data_type", curie=AIMSLEAF.curie('data_type'),
                   model_uri=AIMSLEAF.dataFile__data_type, domain=None, range=Optional[Union[str, "DataTypeEnum"]])

slots.dataFile__storage_uri = Slot(uri=AIMSLEAF.storage_uri, name="dataFile__storage_uri", curie=AIMSLEAF.curie('storage_uri'),
                   model_uri=AIMSLEAF.dataFile__storage_uri, domain=None, range=Optional[str])

slots.dataFile__related_entity = Slot(uri=AIMSLEAF.related_entity, name="dataFile__related_entity", curie=AIMSLEAF.curie('related_entity'),
                   model_uri=AIMSLEAF.dataFile__related_entity, domain=None, range=Optional[str])

slots.dataFile__file_role = Slot(uri=AIMSLEAF.file_role, name="dataFile__file_role", curie=AIMSLEAF.curie('file_role'),
                   model_uri=AIMSLEAF.dataFile__file_role, domain=None, range=Optional[str])

slots.image__file_name = Slot(uri=AIMSLEAF.file_name, name="image__file_name", curie=AIMSLEAF.curie('file_name'),
                   model_uri=AIMSLEAF.image__file_name, domain=None, range=str)

slots.image__acquisition_date = Slot(uri=AIMSLEAF.acquisition_date, name="image__acquisition_date", curie=AIMSLEAF.curie('acquisition_date'),
                   model_uri=AIMSLEAF.image__acquisition_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.image__pixel_size = Slot(uri=AIMSLEAF.pixel_size, name="image__pixel_size", curie=AIMSLEAF.curie('pixel_size'),
                   model_uri=AIMSLEAF.image__pixel_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.image__dimensions_x = Slot(uri=AIMSLEAF.dimensions_x, name="image__dimensions_x", curie=AIMSLEAF.curie('dimensions_x'),
                   model_uri=AIMSLEAF.image__dimensions_x, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.image__dimensions_y = Slot(uri=AIMSLEAF.dimensions_y, name="image__dimensions_y", curie=AIMSLEAF.curie('dimensions_y'),
                   model_uri=AIMSLEAF.image__dimensions_y, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.image__exposure_time = Slot(uri=AIMSLEAF.exposure_time, name="image__exposure_time", curie=AIMSLEAF.curie('exposure_time'),
                   model_uri=AIMSLEAF.image__exposure_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.image__dose = Slot(uri=AIMSLEAF.dose, name="image__dose", curie=AIMSLEAF.curie('dose'),
                   model_uri=AIMSLEAF.image__dose, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.image2D__defocus = Slot(uri=AIMSLEAF.defocus, name="image2D__defocus", curie=AIMSLEAF.curie('defocus'),
                   model_uri=AIMSLEAF.image2D__defocus, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.image2D__astigmatism = Slot(uri=AIMSLEAF.astigmatism, name="image2D__astigmatism", curie=AIMSLEAF.curie('astigmatism'),
                   model_uri=AIMSLEAF.image2D__astigmatism, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.image3D__dimensions_z = Slot(uri=AIMSLEAF.dimensions_z, name="image3D__dimensions_z", curie=AIMSLEAF.curie('dimensions_z'),
                   model_uri=AIMSLEAF.image3D__dimensions_z, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.image3D__voxel_size = Slot(uri=AIMSLEAF.voxel_size, name="image3D__voxel_size", curie=AIMSLEAF.curie('voxel_size'),
                   model_uri=AIMSLEAF.image3D__voxel_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.image3D__reconstruction_method = Slot(uri=AIMSLEAF.reconstruction_method, name="image3D__reconstruction_method", curie=AIMSLEAF.curie('reconstruction_method'),
                   model_uri=AIMSLEAF.image3D__reconstruction_method, domain=None, range=Optional[str])

slots.movie__frames = Slot(uri=AIMSLEAF.frames, name="movie__frames", curie=AIMSLEAF.curie('frames'),
                   model_uri=AIMSLEAF.movie__frames, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.movie__super_resolution = Slot(uri=AIMSLEAF.super_resolution, name="movie__super_resolution", curie=AIMSLEAF.curie('super_resolution'),
                   model_uri=AIMSLEAF.movie__super_resolution, domain=None, range=Optional[Union[bool, Bool]])

slots.movie__pixel_size_unbinned = Slot(uri=AIMSLEAF.pixel_size_unbinned, name="movie__pixel_size_unbinned", curie=AIMSLEAF.curie('pixel_size_unbinned'),
                   model_uri=AIMSLEAF.movie__pixel_size_unbinned, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.movie__timestamp = Slot(uri=AIMSLEAF.timestamp, name="movie__timestamp", curie=AIMSLEAF.curie('timestamp'),
                   model_uri=AIMSLEAF.movie__timestamp, domain=None, range=Optional[str])

slots.movie__stage_position_x = Slot(uri=AIMSLEAF.stage_position_x, name="movie__stage_position_x", curie=AIMSLEAF.curie('stage_position_x'),
                   model_uri=AIMSLEAF.movie__stage_position_x, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.movie__stage_position_y = Slot(uri=AIMSLEAF.stage_position_y, name="movie__stage_position_y", curie=AIMSLEAF.curie('stage_position_y'),
                   model_uri=AIMSLEAF.movie__stage_position_y, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.movie__stage_position_z = Slot(uri=AIMSLEAF.stage_position_z, name="movie__stage_position_z", curie=AIMSLEAF.curie('stage_position_z'),
                   model_uri=AIMSLEAF.movie__stage_position_z, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.movie__nominal_defocus = Slot(uri=AIMSLEAF.nominal_defocus, name="movie__nominal_defocus", curie=AIMSLEAF.curie('nominal_defocus'),
                   model_uri=AIMSLEAF.movie__nominal_defocus, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.movie__dose_per_frame = Slot(uri=AIMSLEAF.dose_per_frame, name="movie__dose_per_frame", curie=AIMSLEAF.curie('dose_per_frame'),
                   model_uri=AIMSLEAF.movie__dose_per_frame, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.movie__beam_shift_x = Slot(uri=AIMSLEAF.beam_shift_x, name="movie__beam_shift_x", curie=AIMSLEAF.curie('beam_shift_x'),
                   model_uri=AIMSLEAF.movie__beam_shift_x, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.movie__beam_shift_y = Slot(uri=AIMSLEAF.beam_shift_y, name="movie__beam_shift_y", curie=AIMSLEAF.curie('beam_shift_y'),
                   model_uri=AIMSLEAF.movie__beam_shift_y, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.movie__ice_thickness_estimate = Slot(uri=AIMSLEAF.ice_thickness_estimate, name="movie__ice_thickness_estimate", curie=AIMSLEAF.curie('ice_thickness_estimate'),
                   model_uri=AIMSLEAF.movie__ice_thickness_estimate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.movie__grid_square_id = Slot(uri=AIMSLEAF.grid_square_id, name="movie__grid_square_id", curie=AIMSLEAF.curie('grid_square_id'),
                   model_uri=AIMSLEAF.movie__grid_square_id, domain=None, range=Optional[str])

slots.movie__hole_id = Slot(uri=AIMSLEAF.hole_id, name="movie__hole_id", curie=AIMSLEAF.curie('hole_id'),
                   model_uri=AIMSLEAF.movie__hole_id, domain=None, range=Optional[str])

slots.movie__acquisition_group = Slot(uri=AIMSLEAF.acquisition_group, name="movie__acquisition_group", curie=AIMSLEAF.curie('acquisition_group'),
                   model_uri=AIMSLEAF.movie__acquisition_group, domain=None, range=Optional[str])

slots.fTIRImage__pixel_size = Slot(uri=AIMSLEAF.pixel_size, name="fTIRImage__pixel_size", curie=AIMSLEAF.curie('pixel_size'),
                   model_uri=AIMSLEAF.fTIRImage__pixel_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fTIRImage__dimensions_x = Slot(uri=AIMSLEAF.dimensions_x, name="fTIRImage__dimensions_x", curie=AIMSLEAF.curie('dimensions_x'),
                   model_uri=AIMSLEAF.fTIRImage__dimensions_x, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fTIRImage__dimensions_y = Slot(uri=AIMSLEAF.dimensions_y, name="fTIRImage__dimensions_y", curie=AIMSLEAF.curie('dimensions_y'),
                   model_uri=AIMSLEAF.fTIRImage__dimensions_y, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fTIRImage__wavenumber_min = Slot(uri=AIMSLEAF.wavenumber_min, name="fTIRImage__wavenumber_min", curie=AIMSLEAF.curie('wavenumber_min'),
                   model_uri=AIMSLEAF.fTIRImage__wavenumber_min, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fTIRImage__wavenumber_max = Slot(uri=AIMSLEAF.wavenumber_max, name="fTIRImage__wavenumber_max", curie=AIMSLEAF.curie('wavenumber_max'),
                   model_uri=AIMSLEAF.fTIRImage__wavenumber_max, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fTIRImage__spectral_resolution = Slot(uri=AIMSLEAF.spectral_resolution, name="fTIRImage__spectral_resolution", curie=AIMSLEAF.curie('spectral_resolution'),
                   model_uri=AIMSLEAF.fTIRImage__spectral_resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fTIRImage__number_of_scans = Slot(uri=AIMSLEAF.number_of_scans, name="fTIRImage__number_of_scans", curie=AIMSLEAF.curie('number_of_scans'),
                   model_uri=AIMSLEAF.fTIRImage__number_of_scans, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fTIRImage__apodization_function = Slot(uri=AIMSLEAF.apodization_function, name="fTIRImage__apodization_function", curie=AIMSLEAF.curie('apodization_function'),
                   model_uri=AIMSLEAF.fTIRImage__apodization_function, domain=None, range=Optional[str])

slots.fTIRImage__molecular_signatures = Slot(uri=AIMSLEAF.molecular_signatures, name="fTIRImage__molecular_signatures", curie=AIMSLEAF.curie('molecular_signatures'),
                   model_uri=AIMSLEAF.fTIRImage__molecular_signatures, domain=None, range=Optional[Union[str, list[str]]])

slots.fTIRImage__background_correction = Slot(uri=AIMSLEAF.background_correction, name="fTIRImage__background_correction", curie=AIMSLEAF.curie('background_correction'),
                   model_uri=AIMSLEAF.fTIRImage__background_correction, domain=None, range=Optional[str])

slots.fluorescenceImage__excitation_wavelength = Slot(uri=AIMSLEAF.excitation_wavelength, name="fluorescenceImage__excitation_wavelength", curie=AIMSLEAF.curie('excitation_wavelength'),
                   model_uri=AIMSLEAF.fluorescenceImage__excitation_wavelength, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fluorescenceImage__emission_wavelength = Slot(uri=AIMSLEAF.emission_wavelength, name="fluorescenceImage__emission_wavelength", curie=AIMSLEAF.curie('emission_wavelength'),
                   model_uri=AIMSLEAF.fluorescenceImage__emission_wavelength, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fluorescenceImage__excitation_filter = Slot(uri=AIMSLEAF.excitation_filter, name="fluorescenceImage__excitation_filter", curie=AIMSLEAF.curie('excitation_filter'),
                   model_uri=AIMSLEAF.fluorescenceImage__excitation_filter, domain=None, range=Optional[str])

slots.fluorescenceImage__emission_filter = Slot(uri=AIMSLEAF.emission_filter, name="fluorescenceImage__emission_filter", curie=AIMSLEAF.curie('emission_filter'),
                   model_uri=AIMSLEAF.fluorescenceImage__emission_filter, domain=None, range=Optional[str])

slots.fluorescenceImage__fluorophore = Slot(uri=AIMSLEAF.fluorophore, name="fluorescenceImage__fluorophore", curie=AIMSLEAF.curie('fluorophore'),
                   model_uri=AIMSLEAF.fluorescenceImage__fluorophore, domain=None, range=Optional[str])

slots.fluorescenceImage__channel_name = Slot(uri=AIMSLEAF.channel_name, name="fluorescenceImage__channel_name", curie=AIMSLEAF.curie('channel_name'),
                   model_uri=AIMSLEAF.fluorescenceImage__channel_name, domain=None, range=Optional[str])

slots.fluorescenceImage__laser_power = Slot(uri=AIMSLEAF.laser_power, name="fluorescenceImage__laser_power", curie=AIMSLEAF.curie('laser_power'),
                   model_uri=AIMSLEAF.fluorescenceImage__laser_power, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fluorescenceImage__pinhole_size = Slot(uri=AIMSLEAF.pinhole_size, name="fluorescenceImage__pinhole_size", curie=AIMSLEAF.curie('pinhole_size'),
                   model_uri=AIMSLEAF.fluorescenceImage__pinhole_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.fluorescenceImage__quantum_yield = Slot(uri=AIMSLEAF.quantum_yield, name="fluorescenceImage__quantum_yield", curie=AIMSLEAF.curie('quantum_yield'),
                   model_uri=AIMSLEAF.fluorescenceImage__quantum_yield, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.opticalImage__illumination_type = Slot(uri=AIMSLEAF.illumination_type, name="opticalImage__illumination_type", curie=AIMSLEAF.curie('illumination_type'),
                   model_uri=AIMSLEAF.opticalImage__illumination_type, domain=None, range=Optional[Union[str, "IlluminationTypeEnum"]])

slots.opticalImage__magnification = Slot(uri=AIMSLEAF.magnification, name="opticalImage__magnification", curie=AIMSLEAF.curie('magnification'),
                   model_uri=AIMSLEAF.opticalImage__magnification, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.opticalImage__numerical_aperture = Slot(uri=AIMSLEAF.numerical_aperture, name="opticalImage__numerical_aperture", curie=AIMSLEAF.curie('numerical_aperture'),
                   model_uri=AIMSLEAF.opticalImage__numerical_aperture, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.opticalImage__color_channels = Slot(uri=AIMSLEAF.color_channels, name="opticalImage__color_channels", curie=AIMSLEAF.curie('color_channels'),
                   model_uri=AIMSLEAF.opticalImage__color_channels, domain=None, range=Optional[Union[str, list[str]]])

slots.opticalImage__white_balance = Slot(uri=AIMSLEAF.white_balance, name="opticalImage__white_balance", curie=AIMSLEAF.curie('white_balance'),
                   model_uri=AIMSLEAF.opticalImage__white_balance, domain=None, range=Optional[str])

slots.opticalImage__contrast_method = Slot(uri=AIMSLEAF.contrast_method, name="opticalImage__contrast_method", curie=AIMSLEAF.curie('contrast_method'),
                   model_uri=AIMSLEAF.opticalImage__contrast_method, domain=None, range=Optional[str])

slots.xRFImage__pixel_size = Slot(uri=AIMSLEAF.pixel_size, name="xRFImage__pixel_size", curie=AIMSLEAF.curie('pixel_size'),
                   model_uri=AIMSLEAF.xRFImage__pixel_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRFImage__dimensions_x = Slot(uri=AIMSLEAF.dimensions_x, name="xRFImage__dimensions_x", curie=AIMSLEAF.curie('dimensions_x'),
                   model_uri=AIMSLEAF.xRFImage__dimensions_x, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRFImage__dimensions_y = Slot(uri=AIMSLEAF.dimensions_y, name="xRFImage__dimensions_y", curie=AIMSLEAF.curie('dimensions_y'),
                   model_uri=AIMSLEAF.xRFImage__dimensions_y, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRFImage__beam_energy = Slot(uri=AIMSLEAF.beam_energy, name="xRFImage__beam_energy", curie=AIMSLEAF.curie('beam_energy'),
                   model_uri=AIMSLEAF.xRFImage__beam_energy, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRFImage__beam_size = Slot(uri=AIMSLEAF.beam_size, name="xRFImage__beam_size", curie=AIMSLEAF.curie('beam_size'),
                   model_uri=AIMSLEAF.xRFImage__beam_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRFImage__dwell_time = Slot(uri=AIMSLEAF.dwell_time, name="xRFImage__dwell_time", curie=AIMSLEAF.curie('dwell_time'),
                   model_uri=AIMSLEAF.xRFImage__dwell_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRFImage__elements_measured = Slot(uri=AIMSLEAF.elements_measured, name="xRFImage__elements_measured", curie=AIMSLEAF.curie('elements_measured'),
                   model_uri=AIMSLEAF.xRFImage__elements_measured, domain=None, range=Optional[Union[str, list[str]]])

slots.xRFImage__source_type = Slot(uri=AIMSLEAF.source_type, name="xRFImage__source_type", curie=AIMSLEAF.curie('source_type'),
                   model_uri=AIMSLEAF.xRFImage__source_type, domain=None, range=Optional[Union[str, "XRaySourceTypeEnum"]])

slots.xRFImage__detector_technology = Slot(uri=AIMSLEAF.detector_technology, name="xRFImage__detector_technology", curie=AIMSLEAF.curie('detector_technology'),
                   model_uri=AIMSLEAF.xRFImage__detector_technology, domain=None, range=Optional[Union[str, "DetectorTechnologyEnum"]])

slots.xRFImage__detector_model = Slot(uri=AIMSLEAF.detector_model, name="xRFImage__detector_model", curie=AIMSLEAF.curie('detector_model'),
                   model_uri=AIMSLEAF.xRFImage__detector_model, domain=None, range=Optional[str])

slots.xRFImage__flux = Slot(uri=AIMSLEAF.flux, name="xRFImage__flux", curie=AIMSLEAF.curie('flux'),
                   model_uri=AIMSLEAF.xRFImage__flux, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRFImage__calibration_standard = Slot(uri=AIMSLEAF.calibration_standard, name="xRFImage__calibration_standard", curie=AIMSLEAF.curie('calibration_standard'),
                   model_uri=AIMSLEAF.xRFImage__calibration_standard, domain=None, range=Optional[str])

slots.imageFeature__terms = Slot(uri=AIMSLEAF.terms, name="imageFeature__terms", curie=AIMSLEAF.curie('terms'),
                   model_uri=AIMSLEAF.imageFeature__terms, domain=None, range=Optional[Union[dict[Union[str, OntologyTermId], Union[dict, OntologyTerm]], list[Union[dict, OntologyTerm]]]])

slots.ontologyTerm__terms = Slot(uri=AIMSLEAF.terms, name="ontologyTerm__terms", curie=AIMSLEAF.curie('terms'),
                   model_uri=AIMSLEAF.ontologyTerm__terms, domain=None, range=Optional[Union[dict[Union[str, OntologyTermId], Union[dict, OntologyTerm]], list[Union[dict, OntologyTerm]]]])

slots.ontologyTerm__label = Slot(uri=AIMSLEAF.label, name="ontologyTerm__label", curie=AIMSLEAF.curie('label'),
                   model_uri=AIMSLEAF.ontologyTerm__label, domain=None, range=Optional[str])

slots.ontologyTerm__definition = Slot(uri=AIMSLEAF.definition, name="ontologyTerm__definition", curie=AIMSLEAF.curie('definition'),
                   model_uri=AIMSLEAF.ontologyTerm__definition, domain=None, range=Optional[str])

slots.ontologyTerm__ontology = Slot(uri=AIMSLEAF.ontology, name="ontologyTerm__ontology", curie=AIMSLEAF.curie('ontology'),
                   model_uri=AIMSLEAF.ontologyTerm__ontology, domain=None, range=Optional[str])

slots.bufferComposition__ph = Slot(uri=AIMSLEAF.ph, name="bufferComposition__ph", curie=AIMSLEAF.curie('ph'),
                   model_uri=AIMSLEAF.bufferComposition__ph, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.bufferComposition__components = Slot(uri=AIMSLEAF.components, name="bufferComposition__components", curie=AIMSLEAF.curie('components'),
                   model_uri=AIMSLEAF.bufferComposition__components, domain=None, range=Optional[Union[str, list[str]]])

slots.bufferComposition__additives = Slot(uri=AIMSLEAF.additives, name="bufferComposition__additives", curie=AIMSLEAF.curie('additives'),
                   model_uri=AIMSLEAF.bufferComposition__additives, domain=None, range=Optional[Union[str, list[str]]])

slots.storageConditions__temperature = Slot(uri=AIMSLEAF.temperature, name="storageConditions__temperature", curie=AIMSLEAF.curie('temperature'),
                   model_uri=AIMSLEAF.storageConditions__temperature, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.storageConditions__duration = Slot(uri=AIMSLEAF.duration, name="storageConditions__duration", curie=AIMSLEAF.curie('duration'),
                   model_uri=AIMSLEAF.storageConditions__duration, domain=None, range=Optional[str])

slots.storageConditions__atmosphere = Slot(uri=AIMSLEAF.atmosphere, name="storageConditions__atmosphere", curie=AIMSLEAF.curie('atmosphere'),
                   model_uri=AIMSLEAF.storageConditions__atmosphere, domain=None, range=Optional[str])

slots.cryoEMPreparation__grid_type = Slot(uri=AIMSLEAF.grid_type, name="cryoEMPreparation__grid_type", curie=AIMSLEAF.curie('grid_type'),
                   model_uri=AIMSLEAF.cryoEMPreparation__grid_type, domain=None, range=Optional[Union[str, "GridTypeEnum"]])

slots.cryoEMPreparation__support_film = Slot(uri=AIMSLEAF.support_film, name="cryoEMPreparation__support_film", curie=AIMSLEAF.curie('support_film'),
                   model_uri=AIMSLEAF.cryoEMPreparation__support_film, domain=None, range=Optional[str])

slots.cryoEMPreparation__hole_size = Slot(uri=AIMSLEAF.hole_size, name="cryoEMPreparation__hole_size", curie=AIMSLEAF.curie('hole_size'),
                   model_uri=AIMSLEAF.cryoEMPreparation__hole_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMPreparation__vitrification_method = Slot(uri=AIMSLEAF.vitrification_method, name="cryoEMPreparation__vitrification_method", curie=AIMSLEAF.curie('vitrification_method'),
                   model_uri=AIMSLEAF.cryoEMPreparation__vitrification_method, domain=None, range=Optional[Union[str, "VitrificationMethodEnum"]])

slots.cryoEMPreparation__blot_time = Slot(uri=AIMSLEAF.blot_time, name="cryoEMPreparation__blot_time", curie=AIMSLEAF.curie('blot_time'),
                   model_uri=AIMSLEAF.cryoEMPreparation__blot_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMPreparation__blot_force = Slot(uri=AIMSLEAF.blot_force, name="cryoEMPreparation__blot_force", curie=AIMSLEAF.curie('blot_force'),
                   model_uri=AIMSLEAF.cryoEMPreparation__blot_force, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMPreparation__humidity_percentage = Slot(uri=AIMSLEAF.humidity_percentage, name="cryoEMPreparation__humidity_percentage", curie=AIMSLEAF.curie('humidity_percentage'),
                   model_uri=AIMSLEAF.cryoEMPreparation__humidity_percentage, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMPreparation__chamber_temperature = Slot(uri=AIMSLEAF.chamber_temperature, name="cryoEMPreparation__chamber_temperature", curie=AIMSLEAF.curie('chamber_temperature'),
                   model_uri=AIMSLEAF.cryoEMPreparation__chamber_temperature, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMPreparation__grid_material = Slot(uri=AIMSLEAF.grid_material, name="cryoEMPreparation__grid_material", curie=AIMSLEAF.curie('grid_material'),
                   model_uri=AIMSLEAF.cryoEMPreparation__grid_material, domain=None, range=Optional[Union[str, "GridMaterialEnum"]])

slots.cryoEMPreparation__glow_discharge_applied = Slot(uri=AIMSLEAF.glow_discharge_applied, name="cryoEMPreparation__glow_discharge_applied", curie=AIMSLEAF.curie('glow_discharge_applied'),
                   model_uri=AIMSLEAF.cryoEMPreparation__glow_discharge_applied, domain=None, range=Optional[Union[bool, Bool]])

slots.cryoEMPreparation__glow_discharge_time = Slot(uri=AIMSLEAF.glow_discharge_time, name="cryoEMPreparation__glow_discharge_time", curie=AIMSLEAF.curie('glow_discharge_time'),
                   model_uri=AIMSLEAF.cryoEMPreparation__glow_discharge_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMPreparation__glow_discharge_current = Slot(uri=AIMSLEAF.glow_discharge_current, name="cryoEMPreparation__glow_discharge_current", curie=AIMSLEAF.curie('glow_discharge_current'),
                   model_uri=AIMSLEAF.cryoEMPreparation__glow_discharge_current, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMPreparation__glow_discharge_atmosphere = Slot(uri=AIMSLEAF.glow_discharge_atmosphere, name="cryoEMPreparation__glow_discharge_atmosphere", curie=AIMSLEAF.curie('glow_discharge_atmosphere'),
                   model_uri=AIMSLEAF.cryoEMPreparation__glow_discharge_atmosphere, domain=None, range=Optional[str])

slots.cryoEMPreparation__glow_discharge_pressure = Slot(uri=AIMSLEAF.glow_discharge_pressure, name="cryoEMPreparation__glow_discharge_pressure", curie=AIMSLEAF.curie('glow_discharge_pressure'),
                   model_uri=AIMSLEAF.cryoEMPreparation__glow_discharge_pressure, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMPreparation__vitrification_instrument = Slot(uri=AIMSLEAF.vitrification_instrument, name="cryoEMPreparation__vitrification_instrument", curie=AIMSLEAF.curie('vitrification_instrument'),
                   model_uri=AIMSLEAF.cryoEMPreparation__vitrification_instrument, domain=None, range=Optional[str])

slots.cryoEMPreparation__blot_number = Slot(uri=AIMSLEAF.blot_number, name="cryoEMPreparation__blot_number", curie=AIMSLEAF.curie('blot_number'),
                   model_uri=AIMSLEAF.cryoEMPreparation__blot_number, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMPreparation__wait_time = Slot(uri=AIMSLEAF.wait_time, name="cryoEMPreparation__wait_time", curie=AIMSLEAF.curie('wait_time'),
                   model_uri=AIMSLEAF.cryoEMPreparation__wait_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMPreparation__blotter_height = Slot(uri=AIMSLEAF.blotter_height, name="cryoEMPreparation__blotter_height", curie=AIMSLEAF.curie('blotter_height'),
                   model_uri=AIMSLEAF.cryoEMPreparation__blotter_height, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMPreparation__blotter_setting = Slot(uri=AIMSLEAF.blotter_setting, name="cryoEMPreparation__blotter_setting", curie=AIMSLEAF.curie('blotter_setting'),
                   model_uri=AIMSLEAF.cryoEMPreparation__blotter_setting, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMPreparation__sample_applied_volume = Slot(uri=AIMSLEAF.sample_applied_volume, name="cryoEMPreparation__sample_applied_volume", curie=AIMSLEAF.curie('sample_applied_volume'),
                   model_uri=AIMSLEAF.cryoEMPreparation__sample_applied_volume, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMPreparation__ethane_temperature = Slot(uri=AIMSLEAF.ethane_temperature, name="cryoEMPreparation__ethane_temperature", curie=AIMSLEAF.curie('ethane_temperature'),
                   model_uri=AIMSLEAF.cryoEMPreparation__ethane_temperature, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cryoEMPreparation__plasma_treatment = Slot(uri=AIMSLEAF.plasma_treatment, name="cryoEMPreparation__plasma_treatment", curie=AIMSLEAF.curie('plasma_treatment'),
                   model_uri=AIMSLEAF.cryoEMPreparation__plasma_treatment, domain=None, range=Optional[str])

slots.xRayPreparation__protein_concentration_mg_per_ml = Slot(uri=AIMSLEAF.protein_concentration_mg_per_ml, name="xRayPreparation__protein_concentration_mg_per_ml", curie=AIMSLEAF.curie('protein_concentration_mg_per_ml'),
                   model_uri=AIMSLEAF.xRayPreparation__protein_concentration_mg_per_ml, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRayPreparation__protein_buffer = Slot(uri=AIMSLEAF.protein_buffer, name="xRayPreparation__protein_buffer", curie=AIMSLEAF.curie('protein_buffer'),
                   model_uri=AIMSLEAF.xRayPreparation__protein_buffer, domain=None, range=Optional[str])

slots.xRayPreparation__additives = Slot(uri=AIMSLEAF.additives, name="xRayPreparation__additives", curie=AIMSLEAF.curie('additives'),
                   model_uri=AIMSLEAF.xRayPreparation__additives, domain=None, range=Optional[str])

slots.xRayPreparation__crystallization_method = Slot(uri=AIMSLEAF.crystallization_method, name="xRayPreparation__crystallization_method", curie=AIMSLEAF.curie('crystallization_method'),
                   model_uri=AIMSLEAF.xRayPreparation__crystallization_method, domain=None, range=Optional[Union[str, "CrystallizationMethodEnum"]])

slots.xRayPreparation__screen_name = Slot(uri=AIMSLEAF.screen_name, name="xRayPreparation__screen_name", curie=AIMSLEAF.curie('screen_name'),
                   model_uri=AIMSLEAF.xRayPreparation__screen_name, domain=None, range=Optional[str])

slots.xRayPreparation__temperature_c = Slot(uri=AIMSLEAF.temperature_c, name="xRayPreparation__temperature_c", curie=AIMSLEAF.curie('temperature_c'),
                   model_uri=AIMSLEAF.xRayPreparation__temperature_c, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRayPreparation__drop_ratio_protein_to_reservoir = Slot(uri=AIMSLEAF.drop_ratio_protein_to_reservoir, name="xRayPreparation__drop_ratio_protein_to_reservoir", curie=AIMSLEAF.curie('drop_ratio_protein_to_reservoir'),
                   model_uri=AIMSLEAF.xRayPreparation__drop_ratio_protein_to_reservoir, domain=None, range=Optional[str])

slots.xRayPreparation__drop_volume_nl = Slot(uri=AIMSLEAF.drop_volume_nl, name="xRayPreparation__drop_volume_nl", curie=AIMSLEAF.curie('drop_volume_nl'),
                   model_uri=AIMSLEAF.xRayPreparation__drop_volume_nl, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRayPreparation__reservoir_volume_ul = Slot(uri=AIMSLEAF.reservoir_volume_ul, name="xRayPreparation__reservoir_volume_ul", curie=AIMSLEAF.curie('reservoir_volume_ul'),
                   model_uri=AIMSLEAF.xRayPreparation__reservoir_volume_ul, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRayPreparation__seeding_type = Slot(uri=AIMSLEAF.seeding_type, name="xRayPreparation__seeding_type", curie=AIMSLEAF.curie('seeding_type'),
                   model_uri=AIMSLEAF.xRayPreparation__seeding_type, domain=None, range=Optional[str])

slots.xRayPreparation__seed_stock_dilution = Slot(uri=AIMSLEAF.seed_stock_dilution, name="xRayPreparation__seed_stock_dilution", curie=AIMSLEAF.curie('seed_stock_dilution'),
                   model_uri=AIMSLEAF.xRayPreparation__seed_stock_dilution, domain=None, range=Optional[str])

slots.xRayPreparation__initial_hit_condition = Slot(uri=AIMSLEAF.initial_hit_condition, name="xRayPreparation__initial_hit_condition", curie=AIMSLEAF.curie('initial_hit_condition'),
                   model_uri=AIMSLEAF.xRayPreparation__initial_hit_condition, domain=None, range=Optional[str])

slots.xRayPreparation__optimization_strategy = Slot(uri=AIMSLEAF.optimization_strategy, name="xRayPreparation__optimization_strategy", curie=AIMSLEAF.curie('optimization_strategy'),
                   model_uri=AIMSLEAF.xRayPreparation__optimization_strategy, domain=None, range=Optional[str])

slots.xRayPreparation__optimized_condition = Slot(uri=AIMSLEAF.optimized_condition, name="xRayPreparation__optimized_condition", curie=AIMSLEAF.curie('optimized_condition'),
                   model_uri=AIMSLEAF.xRayPreparation__optimized_condition, domain=None, range=Optional[str])

slots.xRayPreparation__crystal_size_um = Slot(uri=AIMSLEAF.crystal_size_um, name="xRayPreparation__crystal_size_um", curie=AIMSLEAF.curie('crystal_size_um'),
                   model_uri=AIMSLEAF.xRayPreparation__crystal_size_um, domain=None, range=Optional[str])

slots.xRayPreparation__cryoprotectant = Slot(uri=AIMSLEAF.cryoprotectant, name="xRayPreparation__cryoprotectant", curie=AIMSLEAF.curie('cryoprotectant'),
                   model_uri=AIMSLEAF.xRayPreparation__cryoprotectant, domain=None, range=Optional[str])

slots.xRayPreparation__cryoprotectant_concentration = Slot(uri=AIMSLEAF.cryoprotectant_concentration, name="xRayPreparation__cryoprotectant_concentration", curie=AIMSLEAF.curie('cryoprotectant_concentration'),
                   model_uri=AIMSLEAF.xRayPreparation__cryoprotectant_concentration, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRayPreparation__soak_compound = Slot(uri=AIMSLEAF.soak_compound, name="xRayPreparation__soak_compound", curie=AIMSLEAF.curie('soak_compound'),
                   model_uri=AIMSLEAF.xRayPreparation__soak_compound, domain=None, range=Optional[str])

slots.xRayPreparation__soak_conditions = Slot(uri=AIMSLEAF.soak_conditions, name="xRayPreparation__soak_conditions", curie=AIMSLEAF.curie('soak_conditions'),
                   model_uri=AIMSLEAF.xRayPreparation__soak_conditions, domain=None, range=Optional[str])

slots.xRayPreparation__mounting_method = Slot(uri=NSLS2.Mount_Type, name="xRayPreparation__mounting_method", curie=NSLS2.curie('Mount_Type'),
                   model_uri=AIMSLEAF.xRayPreparation__mounting_method, domain=None, range=Optional[str])

slots.xRayPreparation__flash_cooling_method = Slot(uri=AIMSLEAF.flash_cooling_method, name="xRayPreparation__flash_cooling_method", curie=AIMSLEAF.curie('flash_cooling_method'),
                   model_uri=AIMSLEAF.xRayPreparation__flash_cooling_method, domain=None, range=Optional[str])

slots.xRayPreparation__crystal_notes = Slot(uri=AIMSLEAF.crystal_notes, name="xRayPreparation__crystal_notes", curie=AIMSLEAF.curie('crystal_notes'),
                   model_uri=AIMSLEAF.xRayPreparation__crystal_notes, domain=None, range=Optional[str])

slots.xRayPreparation__loop_size = Slot(uri=NSLS2.Loop_Size, name="xRayPreparation__loop_size", curie=NSLS2.curie('Loop_Size'),
                   model_uri=AIMSLEAF.xRayPreparation__loop_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.xRayPreparation__mounting_temperature = Slot(uri=NSLS2.Temperature, name="xRayPreparation__mounting_temperature", curie=NSLS2.curie('Temperature'),
                   model_uri=AIMSLEAF.xRayPreparation__mounting_temperature, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentalConditions__temperature = Slot(uri=AIMSLEAF.temperature, name="experimentalConditions__temperature", curie=AIMSLEAF.curie('temperature'),
                   model_uri=AIMSLEAF.experimentalConditions__temperature, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentalConditions__humidity = Slot(uri=AIMSLEAF.humidity, name="experimentalConditions__humidity", curie=AIMSLEAF.curie('humidity'),
                   model_uri=AIMSLEAF.experimentalConditions__humidity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentalConditions__pressure = Slot(uri=AIMSLEAF.pressure, name="experimentalConditions__pressure", curie=AIMSLEAF.curie('pressure'),
                   model_uri=AIMSLEAF.experimentalConditions__pressure, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentalConditions__atmosphere = Slot(uri=AIMSLEAF.atmosphere, name="experimentalConditions__atmosphere", curie=AIMSLEAF.curie('atmosphere'),
                   model_uri=AIMSLEAF.experimentalConditions__atmosphere, domain=None, range=Optional[str])

slots.experimentalConditions__beam_energy = Slot(uri=AIMSLEAF.beam_energy, name="experimentalConditions__beam_energy", curie=AIMSLEAF.curie('beam_energy'),
                   model_uri=AIMSLEAF.experimentalConditions__beam_energy, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.experimentalConditions__exposure_time = Slot(uri=AIMSLEAF.exposure_time, name="experimentalConditions__exposure_time", curie=AIMSLEAF.curie('exposure_time'),
                   model_uri=AIMSLEAF.experimentalConditions__exposure_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataCollectionStrategy__collection_mode = Slot(uri=AIMSLEAF.collection_mode, name="dataCollectionStrategy__collection_mode", curie=AIMSLEAF.curie('collection_mode'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__collection_mode, domain=None, range=Optional[Union[str, "CollectionModeEnum"]])

slots.dataCollectionStrategy__total_frames = Slot(uri=AIMSLEAF.total_frames, name="dataCollectionStrategy__total_frames", curie=AIMSLEAF.curie('total_frames'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__total_frames, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataCollectionStrategy__frame_rate = Slot(uri=AIMSLEAF.frame_rate, name="dataCollectionStrategy__frame_rate", curie=AIMSLEAF.curie('frame_rate'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__frame_rate, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataCollectionStrategy__total_dose = Slot(uri=AIMSLEAF.total_dose, name="dataCollectionStrategy__total_dose", curie=AIMSLEAF.curie('total_dose'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__total_dose, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataCollectionStrategy__dose_per_frame = Slot(uri=AIMSLEAF.dose_per_frame, name="dataCollectionStrategy__dose_per_frame", curie=AIMSLEAF.curie('dose_per_frame'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__dose_per_frame, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataCollectionStrategy__wavelength_a = Slot(uri=AIMSLEAF.wavelength_a, name="dataCollectionStrategy__wavelength_a", curie=AIMSLEAF.curie('wavelength_a'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__wavelength_a, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataCollectionStrategy__detector_mode = Slot(uri=AIMSLEAF.detector_mode, name="dataCollectionStrategy__detector_mode", curie=AIMSLEAF.curie('detector_mode'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__detector_mode, domain=None, range=Optional[Union[str, "DetectorModeEnum"]])

slots.dataCollectionStrategy__pixel_size_calibrated = Slot(uri=AIMSLEAF.pixel_size_calibrated, name="dataCollectionStrategy__pixel_size_calibrated", curie=AIMSLEAF.curie('pixel_size_calibrated'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__pixel_size_calibrated, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataCollectionStrategy__detector_distance_mm = Slot(uri=AIMSLEAF.detector_distance_mm, name="dataCollectionStrategy__detector_distance_mm", curie=AIMSLEAF.curie('detector_distance_mm'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__detector_distance_mm, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataCollectionStrategy__beam_center_x_px = Slot(uri=AIMSLEAF.beam_center_x_px, name="dataCollectionStrategy__beam_center_x_px", curie=AIMSLEAF.curie('beam_center_x_px'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__beam_center_x_px, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataCollectionStrategy__beam_center_y_px = Slot(uri=AIMSLEAF.beam_center_y_px, name="dataCollectionStrategy__beam_center_y_px", curie=AIMSLEAF.curie('beam_center_y_px'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__beam_center_y_px, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataCollectionStrategy__beam_size_um = Slot(uri=AIMSLEAF.beam_size_um, name="dataCollectionStrategy__beam_size_um", curie=AIMSLEAF.curie('beam_size_um'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__beam_size_um, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataCollectionStrategy__flux_photons_per_s = Slot(uri=AIMSLEAF.flux_photons_per_s, name="dataCollectionStrategy__flux_photons_per_s", curie=AIMSLEAF.curie('flux_photons_per_s'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__flux_photons_per_s, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataCollectionStrategy__transmission_percent = Slot(uri=AIMSLEAF.transmission_percent, name="dataCollectionStrategy__transmission_percent", curie=AIMSLEAF.curie('transmission_percent'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__transmission_percent, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataCollectionStrategy__attenuator = Slot(uri=AIMSLEAF.attenuator, name="dataCollectionStrategy__attenuator", curie=AIMSLEAF.curie('attenuator'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__attenuator, domain=None, range=Optional[str])

slots.dataCollectionStrategy__temperature_k = Slot(uri=AIMSLEAF.temperature_k, name="dataCollectionStrategy__temperature_k", curie=AIMSLEAF.curie('temperature_k'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__temperature_k, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataCollectionStrategy__oscillation_per_image_deg = Slot(uri=AIMSLEAF.oscillation_per_image_deg, name="dataCollectionStrategy__oscillation_per_image_deg", curie=AIMSLEAF.curie('oscillation_per_image_deg'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__oscillation_per_image_deg, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataCollectionStrategy__total_rotation_deg = Slot(uri=AIMSLEAF.total_rotation_deg, name="dataCollectionStrategy__total_rotation_deg", curie=AIMSLEAF.curie('total_rotation_deg'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__total_rotation_deg, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.dataCollectionStrategy__strategy_notes = Slot(uri=AIMSLEAF.strategy_notes, name="dataCollectionStrategy__strategy_notes", curie=AIMSLEAF.curie('strategy_notes'),
                   model_uri=AIMSLEAF.dataCollectionStrategy__strategy_notes, domain=None, range=Optional[str])

slots.qualityMetrics__resolution = Slot(uri=AIMSLEAF.resolution, name="qualityMetrics__resolution", curie=AIMSLEAF.curie('resolution'),
                   model_uri=AIMSLEAF.qualityMetrics__resolution, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__resolution_high_shell_a = Slot(uri=AIMSLEAF.resolution_high_shell_a, name="qualityMetrics__resolution_high_shell_a", curie=AIMSLEAF.curie('resolution_high_shell_a'),
                   model_uri=AIMSLEAF.qualityMetrics__resolution_high_shell_a, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__resolution_low_a = Slot(uri=AIMSLEAF.resolution_low_a, name="qualityMetrics__resolution_low_a", curie=AIMSLEAF.curie('resolution_low_a'),
                   model_uri=AIMSLEAF.qualityMetrics__resolution_low_a, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__completeness = Slot(uri=AIMSLEAF.completeness, name="qualityMetrics__completeness", curie=AIMSLEAF.curie('completeness'),
                   model_uri=AIMSLEAF.qualityMetrics__completeness, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__completeness_high_res_shell_percent = Slot(uri=AIMSLEAF.completeness_high_res_shell_percent, name="qualityMetrics__completeness_high_res_shell_percent", curie=AIMSLEAF.curie('completeness_high_res_shell_percent'),
                   model_uri=AIMSLEAF.qualityMetrics__completeness_high_res_shell_percent, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__signal_to_noise = Slot(uri=AIMSLEAF.signal_to_noise, name="qualityMetrics__signal_to_noise", curie=AIMSLEAF.curie('signal_to_noise'),
                   model_uri=AIMSLEAF.qualityMetrics__signal_to_noise, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__mean_i_over_sigma_i = Slot(uri=AIMSLEAF.mean_i_over_sigma_i, name="qualityMetrics__mean_i_over_sigma_i", curie=AIMSLEAF.curie('mean_i_over_sigma_i'),
                   model_uri=AIMSLEAF.qualityMetrics__mean_i_over_sigma_i, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__space_group = Slot(uri=AIMSLEAF.space_group, name="qualityMetrics__space_group", curie=AIMSLEAF.curie('space_group'),
                   model_uri=AIMSLEAF.qualityMetrics__space_group, domain=None, range=Optional[str])

slots.qualityMetrics__unit_cell_a = Slot(uri=AIMSLEAF.unit_cell_a, name="qualityMetrics__unit_cell_a", curie=AIMSLEAF.curie('unit_cell_a'),
                   model_uri=AIMSLEAF.qualityMetrics__unit_cell_a, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__unit_cell_b = Slot(uri=AIMSLEAF.unit_cell_b, name="qualityMetrics__unit_cell_b", curie=AIMSLEAF.curie('unit_cell_b'),
                   model_uri=AIMSLEAF.qualityMetrics__unit_cell_b, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__unit_cell_c = Slot(uri=AIMSLEAF.unit_cell_c, name="qualityMetrics__unit_cell_c", curie=AIMSLEAF.curie('unit_cell_c'),
                   model_uri=AIMSLEAF.qualityMetrics__unit_cell_c, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__unit_cell_alpha = Slot(uri=AIMSLEAF.unit_cell_alpha, name="qualityMetrics__unit_cell_alpha", curie=AIMSLEAF.curie('unit_cell_alpha'),
                   model_uri=AIMSLEAF.qualityMetrics__unit_cell_alpha, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__unit_cell_beta = Slot(uri=AIMSLEAF.unit_cell_beta, name="qualityMetrics__unit_cell_beta", curie=AIMSLEAF.curie('unit_cell_beta'),
                   model_uri=AIMSLEAF.qualityMetrics__unit_cell_beta, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__unit_cell_gamma = Slot(uri=AIMSLEAF.unit_cell_gamma, name="qualityMetrics__unit_cell_gamma", curie=AIMSLEAF.curie('unit_cell_gamma'),
                   model_uri=AIMSLEAF.qualityMetrics__unit_cell_gamma, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__multiplicity = Slot(uri=AIMSLEAF.multiplicity, name="qualityMetrics__multiplicity", curie=AIMSLEAF.curie('multiplicity'),
                   model_uri=AIMSLEAF.qualityMetrics__multiplicity, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__cc_half = Slot(uri=AIMSLEAF.cc_half, name="qualityMetrics__cc_half", curie=AIMSLEAF.curie('cc_half'),
                   model_uri=AIMSLEAF.qualityMetrics__cc_half, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__r_merge = Slot(uri=AIMSLEAF.r_merge, name="qualityMetrics__r_merge", curie=AIMSLEAF.curie('r_merge'),
                   model_uri=AIMSLEAF.qualityMetrics__r_merge, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__r_pim = Slot(uri=AIMSLEAF.r_pim, name="qualityMetrics__r_pim", curie=AIMSLEAF.curie('r_pim'),
                   model_uri=AIMSLEAF.qualityMetrics__r_pim, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__wilson_b_factor_a2 = Slot(uri=AIMSLEAF.wilson_b_factor_a2, name="qualityMetrics__wilson_b_factor_a2", curie=AIMSLEAF.curie('wilson_b_factor_a2'),
                   model_uri=AIMSLEAF.qualityMetrics__wilson_b_factor_a2, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__anomalous_used = Slot(uri=AIMSLEAF.anomalous_used, name="qualityMetrics__anomalous_used", curie=AIMSLEAF.curie('anomalous_used'),
                   model_uri=AIMSLEAF.qualityMetrics__anomalous_used, domain=None, range=Optional[Union[bool, Bool]])

slots.qualityMetrics__anom_corr = Slot(uri=AIMSLEAF.anom_corr, name="qualityMetrics__anom_corr", curie=AIMSLEAF.curie('anom_corr'),
                   model_uri=AIMSLEAF.qualityMetrics__anom_corr, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__anom_sig_ano = Slot(uri=AIMSLEAF.anom_sig_ano, name="qualityMetrics__anom_sig_ano", curie=AIMSLEAF.curie('anom_sig_ano'),
                   model_uri=AIMSLEAF.qualityMetrics__anom_sig_ano, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__r_work = Slot(uri=AIMSLEAF.r_work, name="qualityMetrics__r_work", curie=AIMSLEAF.curie('r_work'),
                   model_uri=AIMSLEAF.qualityMetrics__r_work, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__r_free = Slot(uri=AIMSLEAF.r_free, name="qualityMetrics__r_free", curie=AIMSLEAF.curie('r_free'),
                   model_uri=AIMSLEAF.qualityMetrics__r_free, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__ramachandran_favored_percent = Slot(uri=AIMSLEAF.ramachandran_favored_percent, name="qualityMetrics__ramachandran_favored_percent", curie=AIMSLEAF.curie('ramachandran_favored_percent'),
                   model_uri=AIMSLEAF.qualityMetrics__ramachandran_favored_percent, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__ramachandran_outliers_percent = Slot(uri=AIMSLEAF.ramachandran_outliers_percent, name="qualityMetrics__ramachandran_outliers_percent", curie=AIMSLEAF.curie('ramachandran_outliers_percent'),
                   model_uri=AIMSLEAF.qualityMetrics__ramachandran_outliers_percent, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__clashscore = Slot(uri=AIMSLEAF.clashscore, name="qualityMetrics__clashscore", curie=AIMSLEAF.curie('clashscore'),
                   model_uri=AIMSLEAF.qualityMetrics__clashscore, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__molprobity_score = Slot(uri=AIMSLEAF.molprobity_score, name="qualityMetrics__molprobity_score", curie=AIMSLEAF.curie('molprobity_score'),
                   model_uri=AIMSLEAF.qualityMetrics__molprobity_score, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__average_b_factor_a2 = Slot(uri=AIMSLEAF.average_b_factor_a2, name="qualityMetrics__average_b_factor_a2", curie=AIMSLEAF.curie('average_b_factor_a2'),
                   model_uri=AIMSLEAF.qualityMetrics__average_b_factor_a2, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__i_zero = Slot(uri=AIMSLEAF.i_zero, name="qualityMetrics__i_zero", curie=AIMSLEAF.curie('i_zero'),
                   model_uri=AIMSLEAF.qualityMetrics__i_zero, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__rg = Slot(uri=AIMSLEAF.rg, name="qualityMetrics__rg", curie=AIMSLEAF.curie('rg'),
                   model_uri=AIMSLEAF.qualityMetrics__rg, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.qualityMetrics__r_factor = Slot(uri=AIMSLEAF.r_factor, name="qualityMetrics__r_factor", curie=AIMSLEAF.curie('r_factor'),
                   model_uri=AIMSLEAF.qualityMetrics__r_factor, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.computeResources__cpu_hours = Slot(uri=AIMSLEAF.cpu_hours, name="computeResources__cpu_hours", curie=AIMSLEAF.curie('cpu_hours'),
                   model_uri=AIMSLEAF.computeResources__cpu_hours, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.computeResources__gpu_hours = Slot(uri=AIMSLEAF.gpu_hours, name="computeResources__gpu_hours", curie=AIMSLEAF.curie('gpu_hours'),
                   model_uri=AIMSLEAF.computeResources__gpu_hours, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.computeResources__memory_gb = Slot(uri=AIMSLEAF.memory_gb, name="computeResources__memory_gb", curie=AIMSLEAF.curie('memory_gb'),
                   model_uri=AIMSLEAF.computeResources__memory_gb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.computeResources__storage_gb = Slot(uri=AIMSLEAF.storage_gb, name="computeResources__storage_gb", curie=AIMSLEAF.curie('storage_gb'),
                   model_uri=AIMSLEAF.computeResources__storage_gb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.motionCorrectionParameters__patch_size = Slot(uri=AIMSLEAF.patch_size, name="motionCorrectionParameters__patch_size", curie=AIMSLEAF.curie('patch_size'),
                   model_uri=AIMSLEAF.motionCorrectionParameters__patch_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.motionCorrectionParameters__binning = Slot(uri=AIMSLEAF.binning, name="motionCorrectionParameters__binning", curie=AIMSLEAF.curie('binning'),
                   model_uri=AIMSLEAF.motionCorrectionParameters__binning, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.motionCorrectionParameters__dose_weighting = Slot(uri=AIMSLEAF.dose_weighting, name="motionCorrectionParameters__dose_weighting", curie=AIMSLEAF.curie('dose_weighting'),
                   model_uri=AIMSLEAF.motionCorrectionParameters__dose_weighting, domain=None, range=Optional[Union[bool, Bool]])

slots.motionCorrectionParameters__bfactor_dose_weighting = Slot(uri=AIMSLEAF.bfactor_dose_weighting, name="motionCorrectionParameters__bfactor_dose_weighting", curie=AIMSLEAF.curie('bfactor_dose_weighting'),
                   model_uri=AIMSLEAF.motionCorrectionParameters__bfactor_dose_weighting, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.motionCorrectionParameters__anisotropic_correction = Slot(uri=AIMSLEAF.anisotropic_correction, name="motionCorrectionParameters__anisotropic_correction", curie=AIMSLEAF.curie('anisotropic_correction'),
                   model_uri=AIMSLEAF.motionCorrectionParameters__anisotropic_correction, domain=None, range=Optional[Union[bool, Bool]])

slots.motionCorrectionParameters__frame_grouping = Slot(uri=AIMSLEAF.frame_grouping, name="motionCorrectionParameters__frame_grouping", curie=AIMSLEAF.curie('frame_grouping'),
                   model_uri=AIMSLEAF.motionCorrectionParameters__frame_grouping, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.motionCorrectionParameters__output_binning = Slot(uri=AIMSLEAF.output_binning, name="motionCorrectionParameters__output_binning", curie=AIMSLEAF.curie('output_binning'),
                   model_uri=AIMSLEAF.motionCorrectionParameters__output_binning, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.motionCorrectionParameters__drift_total = Slot(uri=AIMSLEAF.drift_total, name="motionCorrectionParameters__drift_total", curie=AIMSLEAF.curie('drift_total'),
                   model_uri=AIMSLEAF.motionCorrectionParameters__drift_total, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cTFEstimationParameters__defocus_search_min = Slot(uri=AIMSLEAF.defocus_search_min, name="cTFEstimationParameters__defocus_search_min", curie=AIMSLEAF.curie('defocus_search_min'),
                   model_uri=AIMSLEAF.cTFEstimationParameters__defocus_search_min, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cTFEstimationParameters__defocus_search_max = Slot(uri=AIMSLEAF.defocus_search_max, name="cTFEstimationParameters__defocus_search_max", curie=AIMSLEAF.curie('defocus_search_max'),
                   model_uri=AIMSLEAF.cTFEstimationParameters__defocus_search_max, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cTFEstimationParameters__defocus_step = Slot(uri=AIMSLEAF.defocus_step, name="cTFEstimationParameters__defocus_step", curie=AIMSLEAF.curie('defocus_step'),
                   model_uri=AIMSLEAF.cTFEstimationParameters__defocus_step, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cTFEstimationParameters__amplitude_contrast = Slot(uri=AIMSLEAF.amplitude_contrast, name="cTFEstimationParameters__amplitude_contrast", curie=AIMSLEAF.curie('amplitude_contrast'),
                   model_uri=AIMSLEAF.cTFEstimationParameters__amplitude_contrast, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cTFEstimationParameters__cs_used_in_estimation = Slot(uri=AIMSLEAF.cs_used_in_estimation, name="cTFEstimationParameters__cs_used_in_estimation", curie=AIMSLEAF.curie('cs_used_in_estimation'),
                   model_uri=AIMSLEAF.cTFEstimationParameters__cs_used_in_estimation, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.cTFEstimationParameters__voltage_used_in_estimation = Slot(uri=AIMSLEAF.voltage_used_in_estimation, name="cTFEstimationParameters__voltage_used_in_estimation", curie=AIMSLEAF.curie('voltage_used_in_estimation'),
                   model_uri=AIMSLEAF.cTFEstimationParameters__voltage_used_in_estimation, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.particlePickingParameters__picking_method = Slot(uri=AIMSLEAF.picking_method, name="particlePickingParameters__picking_method", curie=AIMSLEAF.curie('picking_method'),
                   model_uri=AIMSLEAF.particlePickingParameters__picking_method, domain=None, range=Optional[str])

slots.particlePickingParameters__box_size = Slot(uri=AIMSLEAF.box_size, name="particlePickingParameters__box_size", curie=AIMSLEAF.curie('box_size'),
                   model_uri=AIMSLEAF.particlePickingParameters__box_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.particlePickingParameters__threshold = Slot(uri=AIMSLEAF.threshold, name="particlePickingParameters__threshold", curie=AIMSLEAF.curie('threshold'),
                   model_uri=AIMSLEAF.particlePickingParameters__threshold, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.particlePickingParameters__power_score = Slot(uri=AIMSLEAF.power_score, name="particlePickingParameters__power_score", curie=AIMSLEAF.curie('power_score'),
                   model_uri=AIMSLEAF.particlePickingParameters__power_score, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.particlePickingParameters__ncc_score = Slot(uri=AIMSLEAF.ncc_score, name="particlePickingParameters__ncc_score", curie=AIMSLEAF.curie('ncc_score'),
                   model_uri=AIMSLEAF.particlePickingParameters__ncc_score, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.particlePickingParameters__model_name = Slot(uri=AIMSLEAF.model_name, name="particlePickingParameters__model_name", curie=AIMSLEAF.curie('model_name'),
                   model_uri=AIMSLEAF.particlePickingParameters__model_name, domain=None, range=Optional[str])

slots.particlePickingParameters__model_file_path = Slot(uri=AIMSLEAF.model_file_path, name="particlePickingParameters__model_file_path", curie=AIMSLEAF.curie('model_file_path'),
                   model_uri=AIMSLEAF.particlePickingParameters__model_file_path, domain=None, range=Optional[str])

slots.particlePickingParameters__model_source = Slot(uri=AIMSLEAF.model_source, name="particlePickingParameters__model_source", curie=AIMSLEAF.curie('model_source'),
                   model_uri=AIMSLEAF.particlePickingParameters__model_source, domain=None, range=Optional[str])

slots.refinementParameters__symmetry = Slot(uri=AIMSLEAF.symmetry, name="refinementParameters__symmetry", curie=AIMSLEAF.curie('symmetry'),
                   model_uri=AIMSLEAF.refinementParameters__symmetry, domain=None, range=Optional[Union[str, "SymmetryEnum"]])

slots.refinementParameters__pixel_size = Slot(uri=AIMSLEAF.pixel_size, name="refinementParameters__pixel_size", curie=AIMSLEAF.curie('pixel_size'),
                   model_uri=AIMSLEAF.refinementParameters__pixel_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.refinementParameters__box_size = Slot(uri=AIMSLEAF.box_size, name="refinementParameters__box_size", curie=AIMSLEAF.curie('box_size'),
                   model_uri=AIMSLEAF.refinementParameters__box_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.refinementParameters__gold_standard = Slot(uri=AIMSLEAF.gold_standard, name="refinementParameters__gold_standard", curie=AIMSLEAF.curie('gold_standard'),
                   model_uri=AIMSLEAF.refinementParameters__gold_standard, domain=None, range=Optional[Union[bool, Bool]])

slots.refinementParameters__split_strategy = Slot(uri=AIMSLEAF.split_strategy, name="refinementParameters__split_strategy", curie=AIMSLEAF.curie('split_strategy'),
                   model_uri=AIMSLEAF.refinementParameters__split_strategy, domain=None, range=Optional[str])

slots.refinementParameters__resolution_0_143 = Slot(uri=AIMSLEAF.resolution_0_143, name="refinementParameters__resolution_0_143", curie=AIMSLEAF.curie('resolution_0_143'),
                   model_uri=AIMSLEAF.refinementParameters__resolution_0_143, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.refinementParameters__resolution_0_5 = Slot(uri=AIMSLEAF.resolution_0_5, name="refinementParameters__resolution_0_5", curie=AIMSLEAF.curie('resolution_0_5'),
                   model_uri=AIMSLEAF.refinementParameters__resolution_0_5, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.refinementParameters__map_sharpening_bfactor = Slot(uri=AIMSLEAF.map_sharpening_bfactor, name="refinementParameters__map_sharpening_bfactor", curie=AIMSLEAF.curie('map_sharpening_bfactor'),
                   model_uri=AIMSLEAF.refinementParameters__map_sharpening_bfactor, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.studySampleAssociation__study_id = Slot(uri=AIMSLEAF.study_id, name="studySampleAssociation__study_id", curie=AIMSLEAF.curie('study_id'),
                   model_uri=AIMSLEAF.studySampleAssociation__study_id, domain=None, range=Union[str, StudyId])

slots.studySampleAssociation__sample_id = Slot(uri=AIMSLEAF.sample_id, name="studySampleAssociation__sample_id", curie=AIMSLEAF.curie('sample_id'),
                   model_uri=AIMSLEAF.studySampleAssociation__sample_id, domain=None, range=Union[str, SampleId])

slots.studySampleAssociation__role = Slot(uri=AIMSLEAF.role, name="studySampleAssociation__role", curie=AIMSLEAF.curie('role'),
                   model_uri=AIMSLEAF.studySampleAssociation__role, domain=None, range=Optional[Union[str, "SampleRoleEnum"]])

slots.studySampleAssociation__date_added = Slot(uri=AIMSLEAF.date_added, name="studySampleAssociation__date_added", curie=AIMSLEAF.curie('date_added'),
                   model_uri=AIMSLEAF.studySampleAssociation__date_added, domain=None, range=Optional[Union[str, XSDDate]])

slots.sampleDataAssociation__sample_id = Slot(uri=AIMSLEAF.sample_id, name="sampleDataAssociation__sample_id", curie=AIMSLEAF.curie('sample_id'),
                   model_uri=AIMSLEAF.sampleDataAssociation__sample_id, domain=None, range=Union[str, SampleId])

slots.sampleDataAssociation__data_id = Slot(uri=AIMSLEAF.data_id, name="sampleDataAssociation__data_id", curie=AIMSLEAF.curie('data_id'),
                   model_uri=AIMSLEAF.sampleDataAssociation__data_id, domain=None, range=Union[str, DataFileId])

slots.sampleDataAssociation__role = Slot(uri=AIMSLEAF.role, name="sampleDataAssociation__role", curie=AIMSLEAF.curie('role'),
                   model_uri=AIMSLEAF.sampleDataAssociation__role, domain=None, range=Optional[Union[str, "SampleRoleEnum"]])

slots.studyExperimentAssociation__study_id = Slot(uri=AIMSLEAF.study_id, name="studyExperimentAssociation__study_id", curie=AIMSLEAF.curie('study_id'),
                   model_uri=AIMSLEAF.studyExperimentAssociation__study_id, domain=None, range=Union[str, StudyId])

slots.studyExperimentAssociation__experiment_id = Slot(uri=AIMSLEAF.experiment_id, name="studyExperimentAssociation__experiment_id", curie=AIMSLEAF.curie('experiment_id'),
                   model_uri=AIMSLEAF.studyExperimentAssociation__experiment_id, domain=None, range=Union[str, ExperimentRunId])

slots.studyWorkflowAssociation__study_id = Slot(uri=AIMSLEAF.study_id, name="studyWorkflowAssociation__study_id", curie=AIMSLEAF.curie('study_id'),
                   model_uri=AIMSLEAF.studyWorkflowAssociation__study_id, domain=None, range=Union[str, StudyId])

slots.studyWorkflowAssociation__workflow_id = Slot(uri=AIMSLEAF.workflow_id, name="studyWorkflowAssociation__workflow_id", curie=AIMSLEAF.curie('workflow_id'),
                   model_uri=AIMSLEAF.studyWorkflowAssociation__workflow_id, domain=None, range=Union[str, WorkflowRunId])

slots.experimentSampleAssociation__experiment_id = Slot(uri=AIMSLEAF.experiment_id, name="experimentSampleAssociation__experiment_id", curie=AIMSLEAF.curie('experiment_id'),
                   model_uri=AIMSLEAF.experimentSampleAssociation__experiment_id, domain=None, range=Union[str, ExperimentRunId])

slots.experimentSampleAssociation__sample_id = Slot(uri=AIMSLEAF.sample_id, name="experimentSampleAssociation__sample_id", curie=AIMSLEAF.curie('sample_id'),
                   model_uri=AIMSLEAF.experimentSampleAssociation__sample_id, domain=None, range=Union[str, SampleId])

slots.experimentSampleAssociation__role = Slot(uri=AIMSLEAF.role, name="experimentSampleAssociation__role", curie=AIMSLEAF.curie('role'),
                   model_uri=AIMSLEAF.experimentSampleAssociation__role, domain=None, range=Optional[Union[str, "ExperimentSampleRoleEnum"]])

slots.experimentSampleAssociation__preparation_id = Slot(uri=AIMSLEAF.preparation_id, name="experimentSampleAssociation__preparation_id", curie=AIMSLEAF.curie('preparation_id'),
                   model_uri=AIMSLEAF.experimentSampleAssociation__preparation_id, domain=None, range=Optional[Union[str, SamplePreparationId]])

slots.experimentInstrumentAssociation__experiment_id = Slot(uri=AIMSLEAF.experiment_id, name="experimentInstrumentAssociation__experiment_id", curie=AIMSLEAF.curie('experiment_id'),
                   model_uri=AIMSLEAF.experimentInstrumentAssociation__experiment_id, domain=None, range=Union[str, ExperimentRunId])

slots.experimentInstrumentAssociation__instrument_id = Slot(uri=AIMSLEAF.instrument_id, name="experimentInstrumentAssociation__instrument_id", curie=AIMSLEAF.curie('instrument_id'),
                   model_uri=AIMSLEAF.experimentInstrumentAssociation__instrument_id, domain=None, range=Union[str, InstrumentId])

slots.experimentInstrumentAssociation__role = Slot(uri=AIMSLEAF.role, name="experimentInstrumentAssociation__role", curie=AIMSLEAF.curie('role'),
                   model_uri=AIMSLEAF.experimentInstrumentAssociation__role, domain=None, range=Optional[Union[str, "InstrumentRoleEnum"]])

slots.workflowExperimentAssociation__workflow_id = Slot(uri=AIMSLEAF.workflow_id, name="workflowExperimentAssociation__workflow_id", curie=AIMSLEAF.curie('workflow_id'),
                   model_uri=AIMSLEAF.workflowExperimentAssociation__workflow_id, domain=None, range=Union[str, WorkflowRunId])

slots.workflowExperimentAssociation__experiment_id = Slot(uri=AIMSLEAF.experiment_id, name="workflowExperimentAssociation__experiment_id", curie=AIMSLEAF.curie('experiment_id'),
                   model_uri=AIMSLEAF.workflowExperimentAssociation__experiment_id, domain=None, range=Union[str, ExperimentRunId])

slots.workflowInputAssociation__workflow_id = Slot(uri=AIMSLEAF.workflow_id, name="workflowInputAssociation__workflow_id", curie=AIMSLEAF.curie('workflow_id'),
                   model_uri=AIMSLEAF.workflowInputAssociation__workflow_id, domain=None, range=Union[str, WorkflowRunId])

slots.workflowInputAssociation__file_id = Slot(uri=AIMSLEAF.file_id, name="workflowInputAssociation__file_id", curie=AIMSLEAF.curie('file_id'),
                   model_uri=AIMSLEAF.workflowInputAssociation__file_id, domain=None, range=Union[str, DataFileId])

slots.workflowInputAssociation__input_type = Slot(uri=AIMSLEAF.input_type, name="workflowInputAssociation__input_type", curie=AIMSLEAF.curie('input_type'),
                   model_uri=AIMSLEAF.workflowInputAssociation__input_type, domain=None, range=Optional[Union[str, "InputTypeEnum"]])

slots.workflowOutputAssociation__workflow_id = Slot(uri=AIMSLEAF.workflow_id, name="workflowOutputAssociation__workflow_id", curie=AIMSLEAF.curie('workflow_id'),
                   model_uri=AIMSLEAF.workflowOutputAssociation__workflow_id, domain=None, range=Union[str, WorkflowRunId])

slots.workflowOutputAssociation__file_id = Slot(uri=AIMSLEAF.file_id, name="workflowOutputAssociation__file_id", curie=AIMSLEAF.curie('file_id'),
                   model_uri=AIMSLEAF.workflowOutputAssociation__file_id, domain=None, range=Union[str, DataFileId])

slots.workflowOutputAssociation__output_type = Slot(uri=AIMSLEAF.output_type, name="workflowOutputAssociation__output_type", curie=AIMSLEAF.curie('output_type'),
                   model_uri=AIMSLEAF.workflowOutputAssociation__output_type, domain=None, range=Optional[Union[str, "OutputTypeEnum"]])

slots.attributeValue__attribute = Slot(uri=AIMSLEAF.attribute, name="attributeValue__attribute", curie=AIMSLEAF.curie('attribute'),
                   model_uri=AIMSLEAF.attributeValue__attribute, domain=None, range=Optional[Union[dict, Attribute]])

slots.attributeValue__raw_value = Slot(uri=AIMSLEAF.raw_value, name="attributeValue__raw_value", curie=AIMSLEAF.curie('raw_value'),
                   model_uri=AIMSLEAF.attributeValue__raw_value, domain=None, range=Optional[str])

slots.attribute__id = Slot(uri=AIMSLEAF.id, name="attribute__id", curie=AIMSLEAF.curie('id'),
                   model_uri=AIMSLEAF.attribute__id, domain=None, range=Optional[str])

slots.attribute__label = Slot(uri=AIMSLEAF.label, name="attribute__label", curie=AIMSLEAF.curie('label'),
                   model_uri=AIMSLEAF.attribute__label, domain=None, range=str)

slots.textValue__value = Slot(uri=AIMSLEAF.value, name="textValue__value", curie=AIMSLEAF.curie('value'),
                   model_uri=AIMSLEAF.textValue__value, domain=None, range=str)

slots.textValue__value_cv_id = Slot(uri=AIMSLEAF.value_cv_id, name="textValue__value_cv_id", curie=AIMSLEAF.curie('value_cv_id'),
                   model_uri=AIMSLEAF.textValue__value_cv_id, domain=None, range=Optional[Union[str, Curie]])

slots.dateTimeValue__value = Slot(uri=AIMSLEAF.value, name="dateTimeValue__value", curie=AIMSLEAF.curie('value'),
                   model_uri=AIMSLEAF.dateTimeValue__value, domain=None, range=str)

slots.proteinAnnotation__protein_id = Slot(uri=AIMSLEAF['functional_annotation/protein_id'], name="proteinAnnotation__protein_id", curie=AIMSLEAF.curie('functional_annotation/protein_id'),
                   model_uri=AIMSLEAF.proteinAnnotation__protein_id, domain=None, range=str,
                   pattern=re.compile(r'^[A-Z][0-9][A-Z0-9]{3}[0-9]|[A-Z][0-9][A-Z0-9]{3}[0-9]-[0-9]+$'))

slots.proteinAnnotation__pdb_entry = Slot(uri=AIMSLEAF['functional_annotation/pdb_entry'], name="proteinAnnotation__pdb_entry", curie=AIMSLEAF.curie('functional_annotation/pdb_entry'),
                   model_uri=AIMSLEAF.proteinAnnotation__pdb_entry, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[0-9][A-Za-z0-9]{3}$'))

slots.proteinAnnotation__chain_id = Slot(uri=AIMSLEAF['functional_annotation/chain_id'], name="proteinAnnotation__chain_id", curie=AIMSLEAF.curie('functional_annotation/chain_id'),
                   model_uri=AIMSLEAF.proteinAnnotation__chain_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[A-Za-z0-9]+$'))

slots.proteinAnnotation__residue_range = Slot(uri=AIMSLEAF['functional_annotation/residue_range'], name="proteinAnnotation__residue_range", curie=AIMSLEAF.curie('functional_annotation/residue_range'),
                   model_uri=AIMSLEAF.proteinAnnotation__residue_range, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[0-9,\-]+$'))

slots.proteinAnnotation__confidence_score = Slot(uri=AIMSLEAF['functional_annotation/confidence_score'], name="proteinAnnotation__confidence_score", curie=AIMSLEAF.curie('functional_annotation/confidence_score'),
                   model_uri=AIMSLEAF.proteinAnnotation__confidence_score, domain=None, range=Optional[float])

slots.proteinAnnotation__evidence_type = Slot(uri=AIMSLEAF['functional_annotation/evidence_type'], name="proteinAnnotation__evidence_type", curie=AIMSLEAF.curie('functional_annotation/evidence_type'),
                   model_uri=AIMSLEAF.proteinAnnotation__evidence_type, domain=None, range=Optional[Union[str, "EvidenceTypeEnum"]])

slots.proteinAnnotation__evidence_code = Slot(uri=AIMSLEAF['functional_annotation/evidence_code'], name="proteinAnnotation__evidence_code", curie=AIMSLEAF.curie('functional_annotation/evidence_code'),
                   model_uri=AIMSLEAF.proteinAnnotation__evidence_code, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.proteinAnnotation__source_database = Slot(uri=AIMSLEAF['functional_annotation/source_database'], name="proteinAnnotation__source_database", curie=AIMSLEAF.curie('functional_annotation/source_database'),
                   model_uri=AIMSLEAF.proteinAnnotation__source_database, domain=None, range=Optional[Union[str, "AnnotationSourceEnum"]])

slots.proteinAnnotation__annotation_method = Slot(uri=AIMSLEAF['functional_annotation/annotation_method'], name="proteinAnnotation__annotation_method", curie=AIMSLEAF.curie('functional_annotation/annotation_method'),
                   model_uri=AIMSLEAF.proteinAnnotation__annotation_method, domain=None, range=Optional[str])

slots.proteinAnnotation__publication_ids = Slot(uri=AIMSLEAF['functional_annotation/publication_ids'], name="proteinAnnotation__publication_ids", curie=AIMSLEAF.curie('functional_annotation/publication_ids'),
                   model_uri=AIMSLEAF.proteinAnnotation__publication_ids, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^(PMID:[0-9]+|DOI:10\.[0-9]{4,}/[-._;()/:A-Za-z0-9]+)$'))

slots.functionalSite__site_type = Slot(uri=AIMSLEAF['functional_annotation/site_type'], name="functionalSite__site_type", curie=AIMSLEAF.curie('functional_annotation/site_type'),
                   model_uri=AIMSLEAF.functionalSite__site_type, domain=None, range=Union[str, "FunctionalSiteTypeEnum"])

slots.functionalSite__site_name = Slot(uri=AIMSLEAF['functional_annotation/site_name'], name="functionalSite__site_name", curie=AIMSLEAF.curie('functional_annotation/site_name'),
                   model_uri=AIMSLEAF.functionalSite__site_name, domain=None, range=Optional[str])

slots.functionalSite__residues = Slot(uri=AIMSLEAF['functional_annotation/residues'], name="functionalSite__residues", curie=AIMSLEAF.curie('functional_annotation/residues'),
                   model_uri=AIMSLEAF.functionalSite__residues, domain=None, range=Optional[Union[str, list[str]]])

slots.functionalSite__ligand_interactions = Slot(uri=AIMSLEAF['functional_annotation/ligand_interactions'], name="functionalSite__ligand_interactions", curie=AIMSLEAF.curie('functional_annotation/ligand_interactions'),
                   model_uri=AIMSLEAF.functionalSite__ligand_interactions, domain=None, range=Optional[Union[Union[dict, LigandInteraction], list[Union[dict, LigandInteraction]]]])

slots.functionalSite__conservation_score = Slot(uri=AIMSLEAF['functional_annotation/conservation_score'], name="functionalSite__conservation_score", curie=AIMSLEAF.curie('functional_annotation/conservation_score'),
                   model_uri=AIMSLEAF.functionalSite__conservation_score, domain=None, range=Optional[float])

slots.functionalSite__functional_importance = Slot(uri=AIMSLEAF['functional_annotation/functional_importance'], name="functionalSite__functional_importance", curie=AIMSLEAF.curie('functional_annotation/functional_importance'),
                   model_uri=AIMSLEAF.functionalSite__functional_importance, domain=None, range=Optional[str])

slots.functionalSite__go_terms = Slot(uri=AIMSLEAF['functional_annotation/go_terms'], name="functionalSite__go_terms", curie=AIMSLEAF.curie('functional_annotation/go_terms'),
                   model_uri=AIMSLEAF.functionalSite__go_terms, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.functionalSite__ec_number = Slot(uri=AIMSLEAF['functional_annotation/ec_number'], name="functionalSite__ec_number", curie=AIMSLEAF.curie('functional_annotation/ec_number'),
                   model_uri=AIMSLEAF.functionalSite__ec_number, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$'))

slots.structuralFeature__feature_type = Slot(uri=AIMSLEAF['functional_annotation/feature_type'], name="structuralFeature__feature_type", curie=AIMSLEAF.curie('functional_annotation/feature_type'),
                   model_uri=AIMSLEAF.structuralFeature__feature_type, domain=None, range=Union[str, "StructuralFeatureTypeEnum"])

slots.structuralFeature__secondary_structure = Slot(uri=AIMSLEAF['functional_annotation/secondary_structure'], name="structuralFeature__secondary_structure", curie=AIMSLEAF.curie('functional_annotation/secondary_structure'),
                   model_uri=AIMSLEAF.structuralFeature__secondary_structure, domain=None, range=Optional[Union[str, "SecondaryStructureEnum"]])

slots.structuralFeature__solvent_accessibility = Slot(uri=AIMSLEAF['functional_annotation/solvent_accessibility'], name="structuralFeature__solvent_accessibility", curie=AIMSLEAF.curie('functional_annotation/solvent_accessibility'),
                   model_uri=AIMSLEAF.structuralFeature__solvent_accessibility, domain=None, range=Optional[float])

slots.structuralFeature__backbone_flexibility = Slot(uri=AIMSLEAF['functional_annotation/backbone_flexibility'], name="structuralFeature__backbone_flexibility", curie=AIMSLEAF.curie('functional_annotation/backbone_flexibility'),
                   model_uri=AIMSLEAF.structuralFeature__backbone_flexibility, domain=None, range=Optional[float])

slots.structuralFeature__disorder_probability = Slot(uri=AIMSLEAF['functional_annotation/disorder_probability'], name="structuralFeature__disorder_probability", curie=AIMSLEAF.curie('functional_annotation/disorder_probability'),
                   model_uri=AIMSLEAF.structuralFeature__disorder_probability, domain=None, range=Optional[float])

slots.structuralFeature__conformational_state = Slot(uri=AIMSLEAF['functional_annotation/conformational_state'], name="structuralFeature__conformational_state", curie=AIMSLEAF.curie('functional_annotation/conformational_state'),
                   model_uri=AIMSLEAF.structuralFeature__conformational_state, domain=None, range=Optional[Union[str, "ConformationalStateEnum"]])

slots.structuralFeature__structural_motif = Slot(uri=AIMSLEAF['functional_annotation/structural_motif'], name="structuralFeature__structural_motif", curie=AIMSLEAF.curie('functional_annotation/structural_motif'),
                   model_uri=AIMSLEAF.structuralFeature__structural_motif, domain=None, range=Optional[str])

slots.structuralFeature__domain_assignment = Slot(uri=AIMSLEAF['functional_annotation/domain_assignment'], name="structuralFeature__domain_assignment", curie=AIMSLEAF.curie('functional_annotation/domain_assignment'),
                   model_uri=AIMSLEAF.structuralFeature__domain_assignment, domain=None, range=Optional[str])

slots.structuralFeature__domain_id = Slot(uri=AIMSLEAF['functional_annotation/domain_id'], name="structuralFeature__domain_id", curie=AIMSLEAF.curie('functional_annotation/domain_id'),
                   model_uri=AIMSLEAF.structuralFeature__domain_id, domain=None, range=Optional[str])

slots.ligandInteraction__ligand_id = Slot(uri=AIMSLEAF['functional_annotation/ligand_id'], name="ligandInteraction__ligand_id", curie=AIMSLEAF.curie('functional_annotation/ligand_id'),
                   model_uri=AIMSLEAF.ligandInteraction__ligand_id, domain=None, range=Union[str, URIorCURIE])

slots.ligandInteraction__ligand_name = Slot(uri=AIMSLEAF['functional_annotation/ligand_name'], name="ligandInteraction__ligand_name", curie=AIMSLEAF.curie('functional_annotation/ligand_name'),
                   model_uri=AIMSLEAF.ligandInteraction__ligand_name, domain=None, range=str)

slots.ligandInteraction__ligand_smiles = Slot(uri=AIMSLEAF['functional_annotation/ligand_smiles'], name="ligandInteraction__ligand_smiles", curie=AIMSLEAF.curie('functional_annotation/ligand_smiles'),
                   model_uri=AIMSLEAF.ligandInteraction__ligand_smiles, domain=None, range=Optional[Union[str, SmilesString]])

slots.ligandInteraction__binding_affinity = Slot(uri=AIMSLEAF['functional_annotation/binding_affinity'], name="ligandInteraction__binding_affinity", curie=AIMSLEAF.curie('functional_annotation/binding_affinity'),
                   model_uri=AIMSLEAF.ligandInteraction__binding_affinity, domain=None, range=Optional[float])

slots.ligandInteraction__binding_affinity_type = Slot(uri=AIMSLEAF['functional_annotation/binding_affinity_type'], name="ligandInteraction__binding_affinity_type", curie=AIMSLEAF.curie('functional_annotation/binding_affinity_type'),
                   model_uri=AIMSLEAF.ligandInteraction__binding_affinity_type, domain=None, range=Optional[Union[str, "BindingAffinityTypeEnum"]])

slots.ligandInteraction__binding_affinity_unit = Slot(uri=AIMSLEAF['functional_annotation/binding_affinity_unit'], name="ligandInteraction__binding_affinity_unit", curie=AIMSLEAF.curie('functional_annotation/binding_affinity_unit'),
                   model_uri=AIMSLEAF.ligandInteraction__binding_affinity_unit, domain=None, range=Optional[Union[str, "AffinityUnitEnum"]])

slots.ligandInteraction__interaction_type = Slot(uri=AIMSLEAF['functional_annotation/interaction_type'], name="ligandInteraction__interaction_type", curie=AIMSLEAF.curie('functional_annotation/interaction_type'),
                   model_uri=AIMSLEAF.ligandInteraction__interaction_type, domain=None, range=Optional[Union[str, "InteractionTypeEnum"]])

slots.ligandInteraction__binding_site_residues = Slot(uri=AIMSLEAF['functional_annotation/binding_site_residues'], name="ligandInteraction__binding_site_residues", curie=AIMSLEAF.curie('functional_annotation/binding_site_residues'),
                   model_uri=AIMSLEAF.ligandInteraction__binding_site_residues, domain=None, range=Optional[Union[str, list[str]]])

slots.ligandInteraction__is_cofactor = Slot(uri=AIMSLEAF['functional_annotation/is_cofactor'], name="ligandInteraction__is_cofactor", curie=AIMSLEAF.curie('functional_annotation/is_cofactor'),
                   model_uri=AIMSLEAF.ligandInteraction__is_cofactor, domain=None, range=Optional[Union[bool, Bool]])

slots.ligandInteraction__is_drug_like = Slot(uri=AIMSLEAF['functional_annotation/is_drug_like'], name="ligandInteraction__is_drug_like", curie=AIMSLEAF.curie('functional_annotation/is_drug_like'),
                   model_uri=AIMSLEAF.ligandInteraction__is_drug_like, domain=None, range=Optional[Union[bool, Bool]])

slots.ligandInteraction__druggability_score = Slot(uri=AIMSLEAF['functional_annotation/druggability_score'], name="ligandInteraction__druggability_score", curie=AIMSLEAF.curie('functional_annotation/druggability_score'),
                   model_uri=AIMSLEAF.ligandInteraction__druggability_score, domain=None, range=Optional[float])

slots.ligandInteraction__interaction_distance = Slot(uri=AIMSLEAF['functional_annotation/interaction_distance'], name="ligandInteraction__interaction_distance", curie=AIMSLEAF.curie('functional_annotation/interaction_distance'),
                   model_uri=AIMSLEAF.ligandInteraction__interaction_distance, domain=None, range=Optional[float])

slots.proteinProteinInteraction__partner_protein_id = Slot(uri=AIMSLEAF['functional_annotation/partner_protein_id'], name="proteinProteinInteraction__partner_protein_id", curie=AIMSLEAF.curie('functional_annotation/partner_protein_id'),
                   model_uri=AIMSLEAF.proteinProteinInteraction__partner_protein_id, domain=None, range=str)

slots.proteinProteinInteraction__partner_chain_id = Slot(uri=AIMSLEAF['functional_annotation/partner_chain_id'], name="proteinProteinInteraction__partner_chain_id", curie=AIMSLEAF.curie('functional_annotation/partner_chain_id'),
                   model_uri=AIMSLEAF.proteinProteinInteraction__partner_chain_id, domain=None, range=Optional[str])

slots.proteinProteinInteraction__interface_residues = Slot(uri=AIMSLEAF['functional_annotation/interface_residues'], name="proteinProteinInteraction__interface_residues", curie=AIMSLEAF.curie('functional_annotation/interface_residues'),
                   model_uri=AIMSLEAF.proteinProteinInteraction__interface_residues, domain=None, range=Optional[Union[str, list[str]]])

slots.proteinProteinInteraction__partner_interface_residues = Slot(uri=AIMSLEAF['functional_annotation/partner_interface_residues'], name="proteinProteinInteraction__partner_interface_residues", curie=AIMSLEAF.curie('functional_annotation/partner_interface_residues'),
                   model_uri=AIMSLEAF.proteinProteinInteraction__partner_interface_residues, domain=None, range=Optional[Union[str, list[str]]])

slots.proteinProteinInteraction__interface_area = Slot(uri=AIMSLEAF['functional_annotation/interface_area'], name="proteinProteinInteraction__interface_area", curie=AIMSLEAF.curie('functional_annotation/interface_area'),
                   model_uri=AIMSLEAF.proteinProteinInteraction__interface_area, domain=None, range=Optional[float])

slots.proteinProteinInteraction__binding_energy = Slot(uri=AIMSLEAF['functional_annotation/binding_energy'], name="proteinProteinInteraction__binding_energy", curie=AIMSLEAF.curie('functional_annotation/binding_energy'),
                   model_uri=AIMSLEAF.proteinProteinInteraction__binding_energy, domain=None, range=Optional[float])

slots.proteinProteinInteraction__dissociation_constant = Slot(uri=AIMSLEAF['functional_annotation/dissociation_constant'], name="proteinProteinInteraction__dissociation_constant", curie=AIMSLEAF.curie('functional_annotation/dissociation_constant'),
                   model_uri=AIMSLEAF.proteinProteinInteraction__dissociation_constant, domain=None, range=Optional[float])

slots.proteinProteinInteraction__complex_stability = Slot(uri=AIMSLEAF['functional_annotation/complex_stability'], name="proteinProteinInteraction__complex_stability", curie=AIMSLEAF.curie('functional_annotation/complex_stability'),
                   model_uri=AIMSLEAF.proteinProteinInteraction__complex_stability, domain=None, range=Optional[Union[str, "ComplexStabilityEnum"]])

slots.proteinProteinInteraction__biological_assembly = Slot(uri=AIMSLEAF['functional_annotation/biological_assembly'], name="proteinProteinInteraction__biological_assembly", curie=AIMSLEAF.curie('functional_annotation/biological_assembly'),
                   model_uri=AIMSLEAF.proteinProteinInteraction__biological_assembly, domain=None, range=Optional[Union[bool, Bool]])

slots.proteinProteinInteraction__interaction_evidence = Slot(uri=AIMSLEAF['functional_annotation/interaction_evidence'], name="proteinProteinInteraction__interaction_evidence", curie=AIMSLEAF.curie('functional_annotation/interaction_evidence'),
                   model_uri=AIMSLEAF.proteinProteinInteraction__interaction_evidence, domain=None, range=Optional[Union[Union[str, "InteractionEvidenceEnum"], list[Union[str, "InteractionEvidenceEnum"]]]])

slots.mutationEffect__mutation = Slot(uri=AIMSLEAF['functional_annotation/mutation'], name="mutationEffect__mutation", curie=AIMSLEAF.curie('functional_annotation/mutation'),
                   model_uri=AIMSLEAF.mutationEffect__mutation, domain=None, range=str,
                   pattern=re.compile(r'^[A-Z][0-9]+[A-Z]$'))

slots.mutationEffect__mutation_type = Slot(uri=AIMSLEAF['functional_annotation/mutation_type'], name="mutationEffect__mutation_type", curie=AIMSLEAF.curie('functional_annotation/mutation_type'),
                   model_uri=AIMSLEAF.mutationEffect__mutation_type, domain=None, range=Optional[Union[str, "MutationTypeEnum"]])

slots.mutationEffect__effect_on_stability = Slot(uri=AIMSLEAF['functional_annotation/effect_on_stability'], name="mutationEffect__effect_on_stability", curie=AIMSLEAF.curie('functional_annotation/effect_on_stability'),
                   model_uri=AIMSLEAF.mutationEffect__effect_on_stability, domain=None, range=Optional[Union[str, "StabilityEffectEnum"]])

slots.mutationEffect__delta_delta_g = Slot(uri=AIMSLEAF['functional_annotation/delta_delta_g'], name="mutationEffect__delta_delta_g", curie=AIMSLEAF.curie('functional_annotation/delta_delta_g'),
                   model_uri=AIMSLEAF.mutationEffect__delta_delta_g, domain=None, range=Optional[float])

slots.mutationEffect__effect_on_function = Slot(uri=AIMSLEAF['functional_annotation/effect_on_function'], name="mutationEffect__effect_on_function", curie=AIMSLEAF.curie('functional_annotation/effect_on_function'),
                   model_uri=AIMSLEAF.mutationEffect__effect_on_function, domain=None, range=Optional[Union[str, "FunctionalEffectEnum"]])

slots.mutationEffect__functional_impact_description = Slot(uri=AIMSLEAF['functional_annotation/functional_impact_description'], name="mutationEffect__functional_impact_description", curie=AIMSLEAF.curie('functional_annotation/functional_impact_description'),
                   model_uri=AIMSLEAF.mutationEffect__functional_impact_description, domain=None, range=Optional[str])

slots.mutationEffect__disease_association = Slot(uri=AIMSLEAF['functional_annotation/disease_association'], name="mutationEffect__disease_association", curie=AIMSLEAF.curie('functional_annotation/disease_association'),
                   model_uri=AIMSLEAF.mutationEffect__disease_association, domain=None, range=Optional[str])

slots.mutationEffect__omim_id = Slot(uri=AIMSLEAF['functional_annotation/omim_id'], name="mutationEffect__omim_id", curie=AIMSLEAF.curie('functional_annotation/omim_id'),
                   model_uri=AIMSLEAF.mutationEffect__omim_id, domain=None, range=Optional[str],
                   pattern=re.compile(r'^[0-9]{6}$'))

slots.mutationEffect__clinical_significance = Slot(uri=AIMSLEAF['functional_annotation/clinical_significance'], name="mutationEffect__clinical_significance", curie=AIMSLEAF.curie('functional_annotation/clinical_significance'),
                   model_uri=AIMSLEAF.mutationEffect__clinical_significance, domain=None, range=Optional[Union[str, "ClinicalSignificanceEnum"]])

slots.mutationEffect__allele_frequency = Slot(uri=AIMSLEAF['functional_annotation/allele_frequency'], name="mutationEffect__allele_frequency", curie=AIMSLEAF.curie('functional_annotation/allele_frequency'),
                   model_uri=AIMSLEAF.mutationEffect__allele_frequency, domain=None, range=Optional[float])

slots.biophysicalProperty__property_type = Slot(uri=AIMSLEAF['functional_annotation/property_type'], name="biophysicalProperty__property_type", curie=AIMSLEAF.curie('functional_annotation/property_type'),
                   model_uri=AIMSLEAF.biophysicalProperty__property_type, domain=None, range=Union[str, "BiophysicalPropertyEnum"])

slots.biophysicalProperty__value = Slot(uri=AIMSLEAF['functional_annotation/value'], name="biophysicalProperty__value", curie=AIMSLEAF.curie('functional_annotation/value'),
                   model_uri=AIMSLEAF.biophysicalProperty__value, domain=None, range=float)

slots.biophysicalProperty__unit = Slot(uri=AIMSLEAF['functional_annotation/unit'], name="biophysicalProperty__unit", curie=AIMSLEAF.curie('functional_annotation/unit'),
                   model_uri=AIMSLEAF.biophysicalProperty__unit, domain=None, range=str)

slots.biophysicalProperty__error = Slot(uri=AIMSLEAF['functional_annotation/error'], name="biophysicalProperty__error", curie=AIMSLEAF.curie('functional_annotation/error'),
                   model_uri=AIMSLEAF.biophysicalProperty__error, domain=None, range=Optional[float])

slots.biophysicalProperty__measurement_conditions = Slot(uri=AIMSLEAF['functional_annotation/measurement_conditions'], name="biophysicalProperty__measurement_conditions", curie=AIMSLEAF.curie('functional_annotation/measurement_conditions'),
                   model_uri=AIMSLEAF.biophysicalProperty__measurement_conditions, domain=None, range=Optional[Union[dict[Union[str, MeasurementConditionsId], Union[dict, MeasurementConditions]], list[Union[dict, MeasurementConditions]]]])

slots.biophysicalProperty__experimental_method = Slot(uri=AIMSLEAF['functional_annotation/experimental_method'], name="biophysicalProperty__experimental_method", curie=AIMSLEAF.curie('functional_annotation/experimental_method'),
                   model_uri=AIMSLEAF.biophysicalProperty__experimental_method, domain=None, range=Optional[Union[str, "BiophysicalMethodEnum"]])

slots.conformationalEnsemble__protein_id = Slot(uri=AIMSLEAF['functional_annotation/protein_id'], name="conformationalEnsemble__protein_id", curie=AIMSLEAF.curie('functional_annotation/protein_id'),
                   model_uri=AIMSLEAF.conformationalEnsemble__protein_id, domain=None, range=str)

slots.conformationalEnsemble__conformational_states = Slot(uri=AIMSLEAF['functional_annotation/conformational_states'], name="conformationalEnsemble__conformational_states", curie=AIMSLEAF.curie('functional_annotation/conformational_states'),
                   model_uri=AIMSLEAF.conformationalEnsemble__conformational_states, domain=None, range=Optional[Union[Union[dict, ConformationalState], list[Union[dict, ConformationalState]]]])

slots.conformationalEnsemble__clustering_method = Slot(uri=AIMSLEAF['functional_annotation/clustering_method'], name="conformationalEnsemble__clustering_method", curie=AIMSLEAF.curie('functional_annotation/clustering_method'),
                   model_uri=AIMSLEAF.conformationalEnsemble__clustering_method, domain=None, range=Optional[str])

slots.conformationalEnsemble__rmsd_threshold = Slot(uri=AIMSLEAF['functional_annotation/rmsd_threshold'], name="conformationalEnsemble__rmsd_threshold", curie=AIMSLEAF.curie('functional_annotation/rmsd_threshold'),
                   model_uri=AIMSLEAF.conformationalEnsemble__rmsd_threshold, domain=None, range=Optional[float])

slots.conformationalEnsemble__transition_pathways = Slot(uri=AIMSLEAF['functional_annotation/transition_pathways'], name="conformationalEnsemble__transition_pathways", curie=AIMSLEAF.curie('functional_annotation/transition_pathways'),
                   model_uri=AIMSLEAF.conformationalEnsemble__transition_pathways, domain=None, range=Optional[str])

slots.conformationalEnsemble__energy_landscape = Slot(uri=AIMSLEAF['functional_annotation/energy_landscape'], name="conformationalEnsemble__energy_landscape", curie=AIMSLEAF.curie('functional_annotation/energy_landscape'),
                   model_uri=AIMSLEAF.conformationalEnsemble__energy_landscape, domain=None, range=Optional[str])

slots.conformationalEnsemble__principal_motions = Slot(uri=AIMSLEAF['functional_annotation/principal_motions'], name="conformationalEnsemble__principal_motions", curie=AIMSLEAF.curie('functional_annotation/principal_motions'),
                   model_uri=AIMSLEAF.conformationalEnsemble__principal_motions, domain=None, range=Optional[Union[str, list[str]]])

slots.conformationalState__state_id = Slot(uri=AIMSLEAF['functional_annotation/state_id'], name="conformationalState__state_id", curie=AIMSLEAF.curie('functional_annotation/state_id'),
                   model_uri=AIMSLEAF.conformationalState__state_id, domain=None, range=str)

slots.conformationalState__state_name = Slot(uri=AIMSLEAF['functional_annotation/state_name'], name="conformationalState__state_name", curie=AIMSLEAF.curie('functional_annotation/state_name'),
                   model_uri=AIMSLEAF.conformationalState__state_name, domain=None, range=Optional[str])

slots.conformationalState__pdb_entries = Slot(uri=AIMSLEAF['functional_annotation/pdb_entries'], name="conformationalState__pdb_entries", curie=AIMSLEAF.curie('functional_annotation/pdb_entries'),
                   model_uri=AIMSLEAF.conformationalState__pdb_entries, domain=None, range=Optional[Union[str, list[str]]])

slots.conformationalState__population = Slot(uri=AIMSLEAF['functional_annotation/population'], name="conformationalState__population", curie=AIMSLEAF.curie('functional_annotation/population'),
                   model_uri=AIMSLEAF.conformationalState__population, domain=None, range=Optional[float])

slots.conformationalState__free_energy = Slot(uri=AIMSLEAF['functional_annotation/free_energy'], name="conformationalState__free_energy", curie=AIMSLEAF.curie('functional_annotation/free_energy'),
                   model_uri=AIMSLEAF.conformationalState__free_energy, domain=None, range=Optional[float])

slots.conformationalState__rmsd_from_reference = Slot(uri=AIMSLEAF['functional_annotation/rmsd_from_reference'], name="conformationalState__rmsd_from_reference", curie=AIMSLEAF.curie('functional_annotation/rmsd_from_reference'),
                   model_uri=AIMSLEAF.conformationalState__rmsd_from_reference, domain=None, range=Optional[float])

slots.conformationalState__characteristic_features = Slot(uri=AIMSLEAF['functional_annotation/characteristic_features'], name="conformationalState__characteristic_features", curie=AIMSLEAF.curie('functional_annotation/characteristic_features'),
                   model_uri=AIMSLEAF.conformationalState__characteristic_features, domain=None, range=Optional[Union[str, list[str]]])

slots.postTranslationalModification__modification_type = Slot(uri=AIMSLEAF['functional_annotation/modification_type'], name="postTranslationalModification__modification_type", curie=AIMSLEAF.curie('functional_annotation/modification_type'),
                   model_uri=AIMSLEAF.postTranslationalModification__modification_type, domain=None, range=Union[str, "PTMTypeEnum"])

slots.postTranslationalModification__modified_residue = Slot(uri=AIMSLEAF['functional_annotation/modified_residue'], name="postTranslationalModification__modified_residue", curie=AIMSLEAF.curie('functional_annotation/modified_residue'),
                   model_uri=AIMSLEAF.postTranslationalModification__modified_residue, domain=None, range=str)

slots.postTranslationalModification__modification_group = Slot(uri=AIMSLEAF['functional_annotation/modification_group'], name="postTranslationalModification__modification_group", curie=AIMSLEAF.curie('functional_annotation/modification_group'),
                   model_uri=AIMSLEAF.postTranslationalModification__modification_group, domain=None, range=Optional[str])

slots.postTranslationalModification__mass_shift = Slot(uri=AIMSLEAF['functional_annotation/mass_shift'], name="postTranslationalModification__mass_shift", curie=AIMSLEAF.curie('functional_annotation/mass_shift'),
                   model_uri=AIMSLEAF.postTranslationalModification__mass_shift, domain=None, range=Optional[float])

slots.postTranslationalModification__functional_effect = Slot(uri=AIMSLEAF['functional_annotation/functional_effect'], name="postTranslationalModification__functional_effect", curie=AIMSLEAF.curie('functional_annotation/functional_effect'),
                   model_uri=AIMSLEAF.postTranslationalModification__functional_effect, domain=None, range=Optional[str])

slots.postTranslationalModification__regulatory_role = Slot(uri=AIMSLEAF['functional_annotation/regulatory_role'], name="postTranslationalModification__regulatory_role", curie=AIMSLEAF.curie('functional_annotation/regulatory_role'),
                   model_uri=AIMSLEAF.postTranslationalModification__regulatory_role, domain=None, range=Optional[str])

slots.postTranslationalModification__enzyme = Slot(uri=AIMSLEAF['functional_annotation/enzyme'], name="postTranslationalModification__enzyme", curie=AIMSLEAF.curie('functional_annotation/enzyme'),
                   model_uri=AIMSLEAF.postTranslationalModification__enzyme, domain=None, range=Optional[str])

slots.postTranslationalModification__removal_enzyme = Slot(uri=AIMSLEAF['functional_annotation/removal_enzyme'], name="postTranslationalModification__removal_enzyme", curie=AIMSLEAF.curie('functional_annotation/removal_enzyme'),
                   model_uri=AIMSLEAF.postTranslationalModification__removal_enzyme, domain=None, range=Optional[str])

slots.databaseCrossReference__database_name = Slot(uri=AIMSLEAF['functional_annotation/database_name'], name="databaseCrossReference__database_name", curie=AIMSLEAF.curie('functional_annotation/database_name'),
                   model_uri=AIMSLEAF.databaseCrossReference__database_name, domain=None, range=Union[str, "DatabaseNameEnum"])

slots.databaseCrossReference__database_id = Slot(uri=AIMSLEAF['functional_annotation/database_id'], name="databaseCrossReference__database_id", curie=AIMSLEAF.curie('functional_annotation/database_id'),
                   model_uri=AIMSLEAF.databaseCrossReference__database_id, domain=None, range=str)

slots.databaseCrossReference__database_url = Slot(uri=AIMSLEAF['functional_annotation/database_url'], name="databaseCrossReference__database_url", curie=AIMSLEAF.curie('functional_annotation/database_url'),
                   model_uri=AIMSLEAF.databaseCrossReference__database_url, domain=None, range=Optional[Union[str, URI]])

slots.databaseCrossReference__last_updated = Slot(uri=AIMSLEAF['functional_annotation/last_updated'], name="databaseCrossReference__last_updated", curie=AIMSLEAF.curie('functional_annotation/last_updated'),
                   model_uri=AIMSLEAF.databaseCrossReference__last_updated, domain=None, range=Optional[str])

slots.evolutionaryConservation__conservation_score = Slot(uri=AIMSLEAF['functional_annotation/conservation_score'], name="evolutionaryConservation__conservation_score", curie=AIMSLEAF.curie('functional_annotation/conservation_score'),
                   model_uri=AIMSLEAF.evolutionaryConservation__conservation_score, domain=None, range=Optional[float])

slots.evolutionaryConservation__conserved_residues = Slot(uri=AIMSLEAF['functional_annotation/conserved_residues'], name="evolutionaryConservation__conserved_residues", curie=AIMSLEAF.curie('functional_annotation/conserved_residues'),
                   model_uri=AIMSLEAF.evolutionaryConservation__conserved_residues, domain=None, range=Optional[Union[str, list[str]]])

slots.evolutionaryConservation__variable_residues = Slot(uri=AIMSLEAF['functional_annotation/variable_residues'], name="evolutionaryConservation__variable_residues", curie=AIMSLEAF.curie('functional_annotation/variable_residues'),
                   model_uri=AIMSLEAF.evolutionaryConservation__variable_residues, domain=None, range=Optional[Union[str, list[str]]])

slots.evolutionaryConservation__conservation_method = Slot(uri=AIMSLEAF['functional_annotation/conservation_method'], name="evolutionaryConservation__conservation_method", curie=AIMSLEAF.curie('functional_annotation/conservation_method'),
                   model_uri=AIMSLEAF.evolutionaryConservation__conservation_method, domain=None, range=Optional[str])

slots.evolutionaryConservation__alignment_depth = Slot(uri=AIMSLEAF['functional_annotation/alignment_depth'], name="evolutionaryConservation__alignment_depth", curie=AIMSLEAF.curie('functional_annotation/alignment_depth'),
                   model_uri=AIMSLEAF.evolutionaryConservation__alignment_depth, domain=None, range=Optional[int])

slots.evolutionaryConservation__taxonomic_range = Slot(uri=AIMSLEAF['functional_annotation/taxonomic_range'], name="evolutionaryConservation__taxonomic_range", curie=AIMSLEAF.curie('functional_annotation/taxonomic_range'),
                   model_uri=AIMSLEAF.evolutionaryConservation__taxonomic_range, domain=None, range=Optional[str])

slots.evolutionaryConservation__coevolved_residues = Slot(uri=AIMSLEAF['functional_annotation/coevolved_residues'], name="evolutionaryConservation__coevolved_residues", curie=AIMSLEAF.curie('functional_annotation/coevolved_residues'),
                   model_uri=AIMSLEAF.evolutionaryConservation__coevolved_residues, domain=None, range=Optional[Union[str, list[str]]])

slots.aggregatedProteinView__uniprot_id = Slot(uri=AIMSLEAF['functional_annotation/uniprot_id'], name="aggregatedProteinView__uniprot_id", curie=AIMSLEAF.curie('functional_annotation/uniprot_id'),
                   model_uri=AIMSLEAF.aggregatedProteinView__uniprot_id, domain=None, range=str)

slots.aggregatedProteinView__protein_name = Slot(uri=AIMSLEAF['functional_annotation/protein_name'], name="aggregatedProteinView__protein_name", curie=AIMSLEAF.curie('functional_annotation/protein_name'),
                   model_uri=AIMSLEAF.aggregatedProteinView__protein_name, domain=None, range=str)

slots.aggregatedProteinView__organism = Slot(uri=AIMSLEAF['functional_annotation/organism'], name="aggregatedProteinView__organism", curie=AIMSLEAF.curie('functional_annotation/organism'),
                   model_uri=AIMSLEAF.aggregatedProteinView__organism, domain=None, range=Optional[str])

slots.aggregatedProteinView__organism_id = Slot(uri=AIMSLEAF['functional_annotation/organism_id'], name="aggregatedProteinView__organism_id", curie=AIMSLEAF.curie('functional_annotation/organism_id'),
                   model_uri=AIMSLEAF.aggregatedProteinView__organism_id, domain=None, range=Optional[int])

slots.aggregatedProteinView__pdb_entries = Slot(uri=AIMSLEAF['functional_annotation/pdb_entries'], name="aggregatedProteinView__pdb_entries", curie=AIMSLEAF.curie('functional_annotation/pdb_entries'),
                   model_uri=AIMSLEAF.aggregatedProteinView__pdb_entries, domain=None, range=Optional[Union[str, list[str]]])

slots.aggregatedProteinView__functional_sites = Slot(uri=AIMSLEAF['functional_annotation/functional_sites'], name="aggregatedProteinView__functional_sites", curie=AIMSLEAF.curie('functional_annotation/functional_sites'),
                   model_uri=AIMSLEAF.aggregatedProteinView__functional_sites, domain=None, range=Optional[Union[dict[Union[str, FunctionalSiteId], Union[dict, FunctionalSite]], list[Union[dict, FunctionalSite]]]])

slots.aggregatedProteinView__structural_features = Slot(uri=AIMSLEAF['functional_annotation/structural_features'], name="aggregatedProteinView__structural_features", curie=AIMSLEAF.curie('functional_annotation/structural_features'),
                   model_uri=AIMSLEAF.aggregatedProteinView__structural_features, domain=None, range=Optional[Union[dict[Union[str, StructuralFeatureId], Union[dict, StructuralFeature]], list[Union[dict, StructuralFeature]]]])

slots.aggregatedProteinView__protein_interactions = Slot(uri=AIMSLEAF['functional_annotation/protein_interactions'], name="aggregatedProteinView__protein_interactions", curie=AIMSLEAF.curie('functional_annotation/protein_interactions'),
                   model_uri=AIMSLEAF.aggregatedProteinView__protein_interactions, domain=None, range=Optional[Union[dict[Union[str, ProteinProteinInteractionId], Union[dict, ProteinProteinInteraction]], list[Union[dict, ProteinProteinInteraction]]]])

slots.aggregatedProteinView__ligand_interactions = Slot(uri=AIMSLEAF['functional_annotation/ligand_interactions'], name="aggregatedProteinView__ligand_interactions", curie=AIMSLEAF.curie('functional_annotation/ligand_interactions'),
                   model_uri=AIMSLEAF.aggregatedProteinView__ligand_interactions, domain=None, range=Optional[Union[Union[dict, LigandInteraction], list[Union[dict, LigandInteraction]]]])

slots.aggregatedProteinView__mutations = Slot(uri=AIMSLEAF['functional_annotation/mutations'], name="aggregatedProteinView__mutations", curie=AIMSLEAF.curie('functional_annotation/mutations'),
                   model_uri=AIMSLEAF.aggregatedProteinView__mutations, domain=None, range=Optional[Union[dict[Union[str, MutationEffectId], Union[dict, MutationEffect]], list[Union[dict, MutationEffect]]]])

slots.aggregatedProteinView__ptms = Slot(uri=AIMSLEAF['functional_annotation/ptms'], name="aggregatedProteinView__ptms", curie=AIMSLEAF.curie('functional_annotation/ptms'),
                   model_uri=AIMSLEAF.aggregatedProteinView__ptms, domain=None, range=Optional[Union[dict[Union[str, PostTranslationalModificationId], Union[dict, PostTranslationalModification]], list[Union[dict, PostTranslationalModification]]]])

slots.aggregatedProteinView__biophysical_properties = Slot(uri=AIMSLEAF['functional_annotation/biophysical_properties'], name="aggregatedProteinView__biophysical_properties", curie=AIMSLEAF.curie('functional_annotation/biophysical_properties'),
                   model_uri=AIMSLEAF.aggregatedProteinView__biophysical_properties, domain=None, range=Optional[Union[Union[dict, BiophysicalProperty], list[Union[dict, BiophysicalProperty]]]])

slots.aggregatedProteinView__conformational_ensemble = Slot(uri=AIMSLEAF['functional_annotation/conformational_ensemble'], name="aggregatedProteinView__conformational_ensemble", curie=AIMSLEAF.curie('functional_annotation/conformational_ensemble'),
                   model_uri=AIMSLEAF.aggregatedProteinView__conformational_ensemble, domain=None, range=Optional[Union[dict, ConformationalEnsemble]])

slots.aggregatedProteinView__evolutionary_conservation = Slot(uri=AIMSLEAF['functional_annotation/evolutionary_conservation'], name="aggregatedProteinView__evolutionary_conservation", curie=AIMSLEAF.curie('functional_annotation/evolutionary_conservation'),
                   model_uri=AIMSLEAF.aggregatedProteinView__evolutionary_conservation, domain=None, range=Optional[Union[dict, EvolutionaryConservation]])

slots.aggregatedProteinView__cross_references = Slot(uri=AIMSLEAF['functional_annotation/cross_references'], name="aggregatedProteinView__cross_references", curie=AIMSLEAF.curie('functional_annotation/cross_references'),
                   model_uri=AIMSLEAF.aggregatedProteinView__cross_references, domain=None, range=Optional[Union[Union[dict, DatabaseCrossReference], list[Union[dict, DatabaseCrossReference]]]])

slots.measurementConditions__buffer_composition = Slot(uri=AIMSLEAF['functional_annotation/buffer_composition'], name="measurementConditions__buffer_composition", curie=AIMSLEAF.curie('functional_annotation/buffer_composition'),
                   model_uri=AIMSLEAF.measurementConditions__buffer_composition, domain=None, range=Optional[Union[dict, BufferComposition]])

slots.measurementConditions__ph = Slot(uri=AIMSLEAF['functional_annotation/ph'], name="measurementConditions__ph", curie=AIMSLEAF.curie('functional_annotation/ph'),
                   model_uri=AIMSLEAF.measurementConditions__ph, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.measurementConditions__ionic_strength = Slot(uri=AIMSLEAF['functional_annotation/ionic_strength'], name="measurementConditions__ionic_strength", curie=AIMSLEAF.curie('functional_annotation/ionic_strength'),
                   model_uri=AIMSLEAF.measurementConditions__ionic_strength, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.measurementConditions__temperature = Slot(uri=AIMSLEAF['functional_annotation/temperature'], name="measurementConditions__temperature", curie=AIMSLEAF.curie('functional_annotation/temperature'),
                   model_uri=AIMSLEAF.measurementConditions__temperature, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.plantSample__biological_replicate_sample_group_name = Slot(uri=AIMSPLANT.biological_replicate_sample_group_name, name="plantSample__biological_replicate_sample_group_name", curie=AIMSPLANT.curie('biological_replicate_sample_group_name'),
                   model_uri=AIMSLEAF.plantSample__biological_replicate_sample_group_name, domain=None, range=Optional[str])

slots.plantSample__combined_tissue_description = Slot(uri=AIMSPLANT.combined_tissue_description, name="plantSample__combined_tissue_description", curie=AIMSPLANT.curie('combined_tissue_description'),
                   model_uri=AIMSLEAF.plantSample__combined_tissue_description, domain=None, range=Optional[str])

slots.plantSample__experimental_time_point_number = Slot(uri=AIMSPLANT.experimental_time_point_number, name="plantSample__experimental_time_point_number", curie=AIMSPLANT.curie('experimental_time_point_number'),
                   model_uri=AIMSLEAF.plantSample__experimental_time_point_number, domain=None, range=Optional[int])

slots.plantSample__experimental_time_point_description = Slot(uri=AIMSPLANT.experimental_time_point_description, name="plantSample__experimental_time_point_description", curie=AIMSPLANT.curie('experimental_time_point_description'),
                   model_uri=AIMSLEAF.plantSample__experimental_time_point_description, domain=None, range=Optional[str])

slots.plantSample__genus = Slot(uri=AIMSPLANT.genus, name="plantSample__genus", curie=AIMSPLANT.curie('genus'),
                   model_uri=AIMSLEAF.plantSample__genus, domain=None, range=str)

slots.plantSample__species = Slot(uri=AIMSPLANT.species, name="plantSample__species", curie=AIMSPLANT.curie('species'),
                   model_uri=AIMSLEAF.plantSample__species, domain=None, range=str)

slots.plantSample__strain_variety_cultivar = Slot(uri=AIMSPLANT.strain_variety_cultivar, name="plantSample__strain_variety_cultivar", curie=AIMSPLANT.curie('strain_variety_cultivar'),
                   model_uri=AIMSLEAF.plantSample__strain_variety_cultivar, domain=None, range=Optional[str])

slots.plantSample__isolate = Slot(uri=AIMSPLANT.isolate, name="plantSample__isolate", curie=AIMSPLANT.curie('isolate'),
                   model_uri=AIMSLEAF.plantSample__isolate, domain=None, range=Optional[str])

slots.plantSample__germplasm_collection_id = Slot(uri=AIMSPLANT.germplasm_collection_id, name="plantSample__germplasm_collection_id", curie=AIMSPLANT.curie('germplasm_collection_id'),
                   model_uri=AIMSLEAF.plantSample__germplasm_collection_id, domain=None, range=Optional[str])

slots.plantSample__ncbi_taxonomy_id = Slot(uri=AIMSPLANT.ncbi_taxonomy_id, name="plantSample__ncbi_taxonomy_id", curie=AIMSPLANT.curie('ncbi_taxonomy_id'),
                   model_uri=AIMSLEAF.plantSample__ncbi_taxonomy_id, domain=None, range=Optional[int])

slots.plantSample__ancestral_data = Slot(uri=AIMSPLANT.ancestral_data, name="plantSample__ancestral_data", curie=AIMSPLANT.curie('ancestral_data'),
                   model_uri=AIMSLEAF.plantSample__ancestral_data, domain=None, range=Optional[str])

slots.plantSample__genetic_modification = Slot(uri=AIMSPLANT.genetic_modification, name="plantSample__genetic_modification", curie=AIMSPLANT.curie('genetic_modification'),
                   model_uri=AIMSLEAF.plantSample__genetic_modification, domain=None, range=Optional[str])

slots.plantSample__estimated_genome_size_mb = Slot(uri=AIMSPLANT.estimated_genome_size_mb, name="plantSample__estimated_genome_size_mb", curie=AIMSPLANT.curie('estimated_genome_size_mb'),
                   model_uri=AIMSLEAF.plantSample__estimated_genome_size_mb, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.plantSample__gc_content_percent = Slot(uri=AIMSPLANT.gc_content_percent, name="plantSample__gc_content_percent", curie=AIMSPLANT.curie('gc_content_percent'),
                   model_uri=AIMSLEAF.plantSample__gc_content_percent, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.plantSample__ploidy = Slot(uri=AIMSPLANT.ploidy, name="plantSample__ploidy", curie=AIMSPLANT.curie('ploidy'),
                   model_uri=AIMSLEAF.plantSample__ploidy, domain=None, range=Optional[Union[str, "PloidyTypeEnum"]])

slots.plantSample__reference_genome = Slot(uri=AIMSPLANT.reference_genome, name="plantSample__reference_genome", curie=AIMSPLANT.curie('reference_genome'),
                   model_uri=AIMSLEAF.plantSample__reference_genome, domain=None, range=Optional[str])

slots.plantSample__collection_date_time = Slot(uri=AIMSPLANT.collection_date_time, name="plantSample__collection_date_time", curie=AIMSPLANT.curie('collection_date_time'),
                   model_uri=AIMSLEAF.plantSample__collection_date_time, domain=None, range=str)

slots.plantSample__sample_size = Slot(uri=AIMSPLANT.sample_size, name="plantSample__sample_size", curie=AIMSPLANT.curie('sample_size'),
                   model_uri=AIMSLEAF.plantSample__sample_size, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.plantSample__tissue = Slot(uri=AIMSPLANT.tissue, name="plantSample__tissue", curie=AIMSPLANT.curie('tissue'),
                   model_uri=AIMSLEAF.plantSample__tissue, domain=None, range=str)

slots.plantSample__tissue_plant_ontology_term = Slot(uri=AIMSPLANT.tissue_plant_ontology_term, name="plantSample__tissue_plant_ontology_term", curie=AIMSPLANT.curie('tissue_plant_ontology_term'),
                   model_uri=AIMSLEAF.plantSample__tissue_plant_ontology_term, domain=None, range=Optional[str])

slots.plantSample__region_locality = Slot(uri=AIMSPLANT.region_locality, name="plantSample__region_locality", curie=AIMSPLANT.curie('region_locality'),
                   model_uri=AIMSLEAF.plantSample__region_locality, domain=None, range=Optional[str])

slots.plantSample__latitude = Slot(uri=AIMSPLANT.latitude, name="plantSample__latitude", curie=AIMSPLANT.curie('latitude'),
                   model_uri=AIMSLEAF.plantSample__latitude, domain=None, range=Optional[float])

slots.plantSample__longitude = Slot(uri=AIMSPLANT.longitude, name="plantSample__longitude", curie=AIMSPLANT.curie('longitude'),
                   model_uri=AIMSLEAF.plantSample__longitude, domain=None, range=Optional[float])

slots.plantSample__depth_meters = Slot(uri=AIMSPLANT.depth_meters, name="plantSample__depth_meters", curie=AIMSPLANT.curie('depth_meters'),
                   model_uri=AIMSLEAF.plantSample__depth_meters, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.plantSample__elevation_meters = Slot(uri=AIMSPLANT.elevation_meters, name="plantSample__elevation_meters", curie=AIMSPLANT.curie('elevation_meters'),
                   model_uri=AIMSLEAF.plantSample__elevation_meters, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.plantSample__temperature = Slot(uri=AIMSPLANT.temperature, name="plantSample__temperature", curie=AIMSPLANT.curie('temperature'),
                   model_uri=AIMSLEAF.plantSample__temperature, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.plantSample__broad_scale_environmental_context = Slot(uri=AIMSPLANT.broad_scale_environmental_context, name="plantSample__broad_scale_environmental_context", curie=AIMSPLANT.curie('broad_scale_environmental_context'),
                   model_uri=AIMSLEAF.plantSample__broad_scale_environmental_context, domain=None, range=Optional[str],
                   pattern=re.compile(r'.*\[ENVO:\d+\]$'))

slots.plantSample__local_environmental_context = Slot(uri=AIMSPLANT.local_environmental_context, name="plantSample__local_environmental_context", curie=AIMSPLANT.curie('local_environmental_context'),
                   model_uri=AIMSLEAF.plantSample__local_environmental_context, domain=None, range=Optional[str],
                   pattern=re.compile(r'.*\[ENVO:\d+\]$'))

slots.plantSample__environmental_medium = Slot(uri=AIMSPLANT.environmental_medium, name="plantSample__environmental_medium", curie=AIMSPLANT.curie('environmental_medium'),
                   model_uri=AIMSLEAF.plantSample__environmental_medium, domain=None, range=Optional[str],
                   pattern=re.compile(r'.*\[ENVO:\d+\]$'))

slots.plantSample__growth_facility = Slot(uri=AIMSPLANT.growth_facility, name="plantSample__growth_facility", curie=AIMSPLANT.curie('growth_facility'),
                   model_uri=AIMSLEAF.plantSample__growth_facility, domain=None, range=Union[str, "GrowthFacilityEnum"])

slots.plantSample__growth_medium = Slot(uri=AIMSPLANT.growth_medium, name="plantSample__growth_medium", curie=AIMSPLANT.curie('growth_medium'),
                   model_uri=AIMSLEAF.plantSample__growth_medium, domain=None, range=str)

slots.plantSample__growth_medium_composition = Slot(uri=AIMSPLANT.growth_medium_composition, name="plantSample__growth_medium_composition", curie=AIMSPLANT.curie('growth_medium_composition'),
                   model_uri=AIMSLEAF.plantSample__growth_medium_composition, domain=None, range=Optional[str])

slots.plantSample__plant_age = Slot(uri=AIMSPLANT.plant_age, name="plantSample__plant_age", curie=AIMSPLANT.curie('plant_age'),
                   model_uri=AIMSLEAF.plantSample__plant_age, domain=None, range=Optional[str])

slots.plantSample__developmental_stage = Slot(uri=AIMSPLANT.developmental_stage, name="plantSample__developmental_stage", curie=AIMSPLANT.curie('developmental_stage'),
                   model_uri=AIMSLEAF.plantSample__developmental_stage, domain=None, range=str)

slots.plantSample__arabadopsis_phenotype_stage = Slot(uri=AIMSPLANT.arabadopsis_phenotype_stage, name="plantSample__arabadopsis_phenotype_stage", curie=AIMSPLANT.curie('arabadopsis_phenotype_stage'),
                   model_uri=AIMSLEAF.plantSample__arabadopsis_phenotype_stage, domain=None, range=Optional[Union[str, "ArabadopsisStageEnum"]])

slots.plantSample__air_temperature_regimen = Slot(uri=AIMSPLANT.air_temperature_regimen, name="plantSample__air_temperature_regimen", curie=AIMSPLANT.curie('air_temperature_regimen'),
                   model_uri=AIMSLEAF.plantSample__air_temperature_regimen, domain=None, range=Optional[str])

slots.plantSample__antibiotic_regimen = Slot(uri=AIMSPLANT.antibiotic_regimen, name="plantSample__antibiotic_regimen", curie=AIMSPLANT.curie('antibiotic_regimen'),
                   model_uri=AIMSLEAF.plantSample__antibiotic_regimen, domain=None, range=Optional[str])

slots.plantSample__biotic_regimen = Slot(uri=AIMSPLANT.biotic_regimen, name="plantSample__biotic_regimen", curie=AIMSPLANT.curie('biotic_regimen'),
                   model_uri=AIMSLEAF.plantSample__biotic_regimen, domain=None, range=Optional[str])

slots.plantSample__inoculation_method = Slot(uri=AIMSPLANT.inoculation_method, name="plantSample__inoculation_method", curie=AIMSPLANT.curie('inoculation_method'),
                   model_uri=AIMSLEAF.plantSample__inoculation_method, domain=None, range=Optional[str])

slots.plantSample__time_post_inoculation = Slot(uri=AIMSPLANT.time_post_inoculation, name="plantSample__time_post_inoculation", curie=AIMSPLANT.curie('time_post_inoculation'),
                   model_uri=AIMSLEAF.plantSample__time_post_inoculation, domain=None, range=Optional[str])

slots.plantSample__chemical_administration = Slot(uri=AIMSPLANT.chemical_administration, name="plantSample__chemical_administration", curie=AIMSPLANT.curie('chemical_administration'),
                   model_uri=AIMSLEAF.plantSample__chemical_administration, domain=None, range=Optional[str])

slots.plantSample__chemical_mutagen = Slot(uri=AIMSPLANT.chemical_mutagen, name="plantSample__chemical_mutagen", curie=AIMSPLANT.curie('chemical_mutagen'),
                   model_uri=AIMSLEAF.plantSample__chemical_mutagen, domain=None, range=Optional[str])

slots.plantSample__fertilizer_administration = Slot(uri=AIMSPLANT.fertilizer_administration, name="plantSample__fertilizer_administration", curie=AIMSPLANT.curie('fertilizer_administration'),
                   model_uri=AIMSLEAF.plantSample__fertilizer_administration, domain=None, range=Optional[str])

slots.plantSample__insecticide_regimen = Slot(uri=AIMSPLANT.insecticide_regimen, name="plantSample__insecticide_regimen", curie=AIMSPLANT.curie('insecticide_regimen'),
                   model_uri=AIMSLEAF.plantSample__insecticide_regimen, domain=None, range=Optional[str])

slots.plantSample__fungicide_regimen = Slot(uri=AIMSPLANT.fungicide_regimen, name="plantSample__fungicide_regimen", curie=AIMSPLANT.curie('fungicide_regimen'),
                   model_uri=AIMSLEAF.plantSample__fungicide_regimen, domain=None, range=Optional[str])

slots.plantSample__gaseous_environment = Slot(uri=AIMSPLANT.gaseous_environment, name="plantSample__gaseous_environment", curie=AIMSPLANT.curie('gaseous_environment'),
                   model_uri=AIMSLEAF.plantSample__gaseous_environment, domain=None, range=Optional[str])

slots.plantSample__growth_hormone_regimen = Slot(uri=AIMSPLANT.growth_hormone_regimen, name="plantSample__growth_hormone_regimen", curie=AIMSPLANT.curie('growth_hormone_regimen'),
                   model_uri=AIMSLEAF.plantSample__growth_hormone_regimen, domain=None, range=Optional[str])

slots.plantSample__herbicide_regimen = Slot(uri=AIMSPLANT.herbicide_regimen, name="plantSample__herbicide_regimen", curie=AIMSPLANT.curie('herbicide_regimen'),
                   model_uri=AIMSLEAF.plantSample__herbicide_regimen, domain=None, range=Optional[str])

slots.plantSample__humidity_regimen = Slot(uri=AIMSPLANT.humidity_regimen, name="plantSample__humidity_regimen", curie=AIMSPLANT.curie('humidity_regimen'),
                   model_uri=AIMSLEAF.plantSample__humidity_regimen, domain=None, range=Optional[str])

slots.plantSample__radiation_regimen = Slot(uri=AIMSPLANT.radiation_regimen, name="plantSample__radiation_regimen", curie=AIMSPLANT.curie('radiation_regimen'),
                   model_uri=AIMSLEAF.plantSample__radiation_regimen, domain=None, range=Optional[str])

slots.plantSample__light_regimen = Slot(uri=AIMSPLANT.light_regimen, name="plantSample__light_regimen", curie=AIMSPLANT.curie('light_regimen'),
                   model_uri=AIMSLEAF.plantSample__light_regimen, domain=None, range=Optional[str])

slots.plantSample__last_light_transition_type = Slot(uri=AIMSPLANT.last_light_transition_type, name="plantSample__last_light_transition_type", curie=AIMSPLANT.curie('last_light_transition_type'),
                   model_uri=AIMSLEAF.plantSample__last_light_transition_type, domain=None, range=Optional[str])

slots.plantSample__time_after_last_light_transition = Slot(uri=AIMSPLANT.time_after_last_light_transition, name="plantSample__time_after_last_light_transition", curie=AIMSPLANT.curie('time_after_last_light_transition'),
                   model_uri=AIMSLEAF.plantSample__time_after_last_light_transition, domain=None, range=Optional[str])

slots.plantSample__salt_regimen = Slot(uri=AIMSPLANT.salt_regimen, name="plantSample__salt_regimen", curie=AIMSPLANT.curie('salt_regimen'),
                   model_uri=AIMSLEAF.plantSample__salt_regimen, domain=None, range=Optional[str])

slots.plantSample__rainfall_regimen = Slot(uri=AIMSPLANT.rainfall_regimen, name="plantSample__rainfall_regimen", curie=AIMSPLANT.curie('rainfall_regimen'),
                   model_uri=AIMSLEAF.plantSample__rainfall_regimen, domain=None, range=Optional[str])

slots.plantSample__watering_regimen = Slot(uri=AIMSPLANT.watering_regimen, name="plantSample__watering_regimen", curie=AIMSPLANT.curie('watering_regimen'),
                   model_uri=AIMSLEAF.plantSample__watering_regimen, domain=None, range=Optional[str])

slots.plantSample__other_treatment_regimen = Slot(uri=AIMSPLANT.other_treatment_regimen, name="plantSample__other_treatment_regimen", curie=AIMSPLANT.curie('other_treatment_regimen'),
                   model_uri=AIMSLEAF.plantSample__other_treatment_regimen, domain=None, range=Optional[str])

slots.plantSample__perturbation = Slot(uri=AIMSPLANT.perturbation, name="plantSample__perturbation", curie=AIMSPLANT.curie('perturbation'),
                   model_uri=AIMSLEAF.plantSample__perturbation, domain=None, range=Optional[str])

slots.plantSample__mechanical_damage = Slot(uri=AIMSPLANT.mechanical_damage, name="plantSample__mechanical_damage", curie=AIMSPLANT.curie('mechanical_damage'),
                   model_uri=AIMSLEAF.plantSample__mechanical_damage, domain=None, range=Optional[str])

slots.plantSample__observed_host_symbionts = Slot(uri=AIMSPLANT.observed_host_symbionts, name="plantSample__observed_host_symbionts", curie=AIMSPLANT.curie('observed_host_symbionts'),
                   model_uri=AIMSLEAF.plantSample__observed_host_symbionts, domain=None, range=Optional[str])

slots.plantSample__plant_sex = Slot(uri=AIMSPLANT.plant_sex, name="plantSample__plant_sex", curie=AIMSPLANT.curie('plant_sex'),
                   model_uri=AIMSLEAF.plantSample__plant_sex, domain=None, range=Optional[str])

slots.plantSample__sample_disease_staus = Slot(uri=AIMSPLANT.sample_disease_staus, name="plantSample__sample_disease_staus", curie=AIMSPLANT.curie('sample_disease_staus'),
                   model_uri=AIMSLEAF.plantSample__sample_disease_staus, domain=None, range=Optional[str])

slots.plantSample__sample_disease_stage = Slot(uri=AIMSPLANT.sample_disease_stage, name="plantSample__sample_disease_stage", curie=AIMSPLANT.curie('sample_disease_stage'),
                   model_uri=AIMSLEAF.plantSample__sample_disease_stage, domain=None, range=Optional[str])

slots.plantSamplePreparation__sample_material_processing = Slot(uri=AIMSPLANT.sample_material_processing, name="plantSamplePreparation__sample_material_processing", curie=AIMSPLANT.curie('sample_material_processing'),
                   model_uri=AIMSLEAF.plantSamplePreparation__sample_material_processing, domain=None, range=Optional[str])

slots.plantSamplePreparation__sample_storage_temperature = Slot(uri=AIMSPLANT.sample_storage_temperature, name="plantSamplePreparation__sample_storage_temperature", curie=AIMSPLANT.curie('sample_storage_temperature'),
                   model_uri=AIMSLEAF.plantSamplePreparation__sample_storage_temperature, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.plantSamplePreparation__sample_preservation_method = Slot(uri=AIMSPLANT.sample_preservation_method, name="plantSamplePreparation__sample_preservation_method", curie=AIMSPLANT.curie('sample_preservation_method'),
                   model_uri=AIMSLEAF.plantSamplePreparation__sample_preservation_method, domain=None, range=Optional[Union[str, "SamplePreservationEnum"]])

slots.plantSamplePreparation__harvest_to_preservation_time = Slot(uri=AIMSPLANT.harvest_to_preservation_time, name="plantSamplePreparation__harvest_to_preservation_time", curie=AIMSPLANT.curie('harvest_to_preservation_time'),
                   model_uri=AIMSLEAF.plantSamplePreparation__harvest_to_preservation_time, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.plantSamplePreparation__embedding_material = Slot(uri=AIMSPLANT.embedding_material, name="plantSamplePreparation__embedding_material", curie=AIMSPLANT.curie('embedding_material'),
                   model_uri=AIMSLEAF.plantSamplePreparation__embedding_material, domain=None, range=Optional[str])

slots.plantSamplePreparation__plane_of_section = Slot(uri=AIMSPLANT.plane_of_section, name="plantSamplePreparation__plane_of_section", curie=AIMSPLANT.curie('plane_of_section'),
                   model_uri=AIMSLEAF.plantSamplePreparation__plane_of_section, domain=None, range=Optional[str])

slots.plantSamplePreparation__section_thickness = Slot(uri=AIMSPLANT.section_thickness, name="plantSamplePreparation__section_thickness", curie=AIMSPLANT.curie('section_thickness'),
                   model_uri=AIMSLEAF.plantSamplePreparation__section_thickness, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.plantSamplePreparation__support_type = Slot(uri=AIMSPLANT.support_type, name="plantSamplePreparation__support_type", curie=AIMSPLANT.curie('support_type'),
                   model_uri=AIMSLEAF.plantSamplePreparation__support_type, domain=None, range=str)

slots.plantSamplePreparation__support_thickness = Slot(uri=AIMSPLANT.support_thickness, name="plantSamplePreparation__support_thickness", curie=AIMSPLANT.curie('support_thickness'),
                   model_uri=AIMSLEAF.plantSamplePreparation__support_thickness, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.plantSamplePreparation__adhesive = Slot(uri=AIMSPLANT.adhesive, name="plantSamplePreparation__adhesive", curie=AIMSPLANT.curie('adhesive'),
                   model_uri=AIMSLEAF.plantSamplePreparation__adhesive, domain=None, range=Optional[str])

slots.plantSamplePreparation__top_layer = Slot(uri=AIMSPLANT.top_layer, name="plantSamplePreparation__top_layer", curie=AIMSPLANT.curie('top_layer'),
                   model_uri=AIMSLEAF.plantSamplePreparation__top_layer, domain=None, range=Optional[str])

slots.plantSamplePreparation__top_layer_thickness = Slot(uri=AIMSPLANT.top_layer_thickness, name="plantSamplePreparation__top_layer_thickness", curie=AIMSPLANT.curie('top_layer_thickness'),
                   model_uri=AIMSLEAF.plantSamplePreparation__top_layer_thickness, domain=None, range=Optional[Union[dict, QuantityValue]])

slots.QuantityValue_numeric_value = Slot(uri=AIMSLEAF.numeric_value, name="QuantityValue_numeric_value", curie=AIMSLEAF.curie('numeric_value'),
                   model_uri=AIMSLEAF.QuantityValue_numeric_value, domain=QuantityValue, range=Optional[float], mappings = [NMDC["numeric_value"], QUD["quantityValue"], SCHEMA["value"]])

slots.QuantityValue_unit = Slot(uri=AIMSLEAF.unit, name="QuantityValue_unit", curie=AIMSLEAF.curie('unit'),
                   model_uri=AIMSLEAF.QuantityValue_unit, domain=QuantityValue, range=str, mappings = [NMDC["unit"], QUD["unit"], SCHEMA["unitCode"], UO["0000000"]])

slots.QuantityValue_raw_value = Slot(uri=AIMSLEAF.raw_value, name="QuantityValue_raw_value", curie=AIMSLEAF.curie('raw_value'),
                   model_uri=AIMSLEAF.QuantityValue_raw_value, domain=QuantityValue, range=Optional[str], mappings = [NMDC["raw_value"]])
