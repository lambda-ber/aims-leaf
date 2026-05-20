-- # Abstract Class: NamedThing Description: A named thing
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
-- # Abstract Class: AttributeGroup Description: A grouping of related data attributes that form a logical unit
--     * Slot: id
--     * Slot: description
-- # Class: Dataset Description: Root container holding flat entity collections and association tables. Follows relational database design patterns for structural biology data.
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
-- # Class: Study Description: A logical grouping of related experiments investigating a research question. In the relational model, Study is lightweight - all relationships are via association tables.
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: Sample Description: A biological sample used in structural biology experiments
--     * Slot: sample_code Description: Human-friendly laboratory identifier or facility code for the sample (e.g., 'ALS-12.3.1-SAMPLE-001', 'LAB-PROT-2024-01'). Used for local reference and tracking within laboratory workflows.
--     * Slot: sample_type Description: Type of biological sample
--     * Slot: preparation_method Description: Method used to prepare the sample
--     * Slot: organism Description: Source organism for the sample (e.g., NCBITaxon:3702 for Arabidopsis thaliana)
--     * Slot: anatomy Description: Anatomical part or tissue (e.g., UBERON:0008945 for leaf)
--     * Slot: cell_type Description: Cell type if applicable (e.g., CL:0000057 for fibroblast)
--     * Slot: parent_sample_id Description: Reference to parent sample for derivation tracking
--     * Slot: quality_metrics Description: Quality control metrics for the sample
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: molecular_weight_id Description: Molecular weight, typically specified in kilodaltons (kDa). Data providers may specify alternative units (e.g., Daltons, g/mol) by including the unit in the QuantityValue.
--     * Slot: concentration_id Description: Sample concentration, typically specified in mg/mL or µM. Data providers may specify alternative units (e.g., molar, g/L) by including the unit in the QuantityValue.
--     * Slot: buffer_composition_id Description: Buffer composition including pH, salts, additives
--     * Slot: storage_conditions_id Description: Storage conditions for the sample
--     * Slot: purity_percentage_id Description: Sample purity, typically specified as a percentage (range: 0-100). Data providers may specify as decimal fraction by including the unit in the QuantityValue.
-- # Class: SamplePreparation Description: A process that prepares a sample for imaging
--     * Slot: preparation_type Description: Type of sample preparation
--     * Slot: sample_id Description: Reference to the sample being prepared
--     * Slot: preparation_date Description: Date of sample preparation
--     * Slot: operator_id Description: Identifier or name of the person who performed the sample preparation (e.g., 'jsmith', 'John Smith', or personnel ID)
--     * Slot: protocol_description Description: Detailed protocol description
--     * Slot: host_strain_or_cell_line Description: Specific strain or cell line used (e.g., BL21(DE3), Sf9, HEK293F)
--     * Slot: medium Description: Growth medium used
--     * Slot: antibiotic_selection Description: Antibiotic or selection agent used
--     * Slot: induction_agent Description: Agent used to induce expression (e.g., IPTG, tetracycline)
--     * Slot: inducer_concentration Description: Concentration of induction agent
--     * Slot: harvest_timepoint Description: Time point when cells were harvested
--     * Slot: lysis_method Description: Method used for cell lysis
--     * Slot: protease_inhibitors Description: Protease inhibitors added
--     * Slot: affinity_type Description: Type of affinity chromatography
--     * Slot: affinity_column Description: Affinity column specifications
--     * Slot: lysis_buffer Description: Buffer composition for lysis
--     * Slot: wash_buffer Description: Buffer composition for washing
--     * Slot: elution_buffer Description: Buffer composition for elution
--     * Slot: tag_removal Description: Whether and how affinity tag was removed
--     * Slot: protease Description: Protease used for tag cleavage
--     * Slot: protease_ratio Description: Ratio of protease to protein
--     * Slot: second_affinity_reverse Description: Second affinity or reverse affinity step
--     * Slot: iex_column Description: Ion-exchange column used
--     * Slot: hic_column Description: Hydrophobic interaction column used
--     * Slot: sec_column Description: Size-exclusion column used
--     * Slot: sec_buffer Description: Buffer for size-exclusion chromatography
--     * Slot: concentration_method Description: Method used to concentrate protein
--     * Slot: final_buffer Description: Final buffer composition after purification
--     * Slot: aggregation_assessment Description: Assessment of protein aggregation state
--     * Slot: aliquoting Description: How the protein was aliquoted for storage
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: culture_volume_l_id Description: Culture volume, typically specified in liters (L). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: growth_temperature_c_id Description: Growth temperature, typically specified in degrees Celsius. Data providers may specify alternative units (e.g., Kelvin) by including the unit in the QuantityValue.
--     * Slot: induction_temperature_c_id Description: Temperature during induction, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: induction_time_h_id Description: Duration of induction, typically specified in hours. Data providers may specify alternative units (e.g., minutes, seconds) by including the unit in the QuantityValue.
--     * Slot: od600_at_induction_id Description: Optical density at 600nm when induction was started. Data providers may include unit information in the QuantityValue if needed.
--     * Slot: cleavage_time_h_id Description: Duration of protease cleavage in hours
--     * Slot: cleavage_temperature_c_id Description: Temperature during cleavage in Celsius
--     * Slot: final_concentration_mg_per_ml_id Description: Final protein concentration in mg/mL
--     * Slot: yield_mg_id Description: Total yield in milligrams
--     * Slot: purity_by_sds_page_percent_id Description: Purity percentage by SDS-PAGE
-- # Class: Instrument Description: An instrument used to collect data
--     * Slot: instrument_code Description: Human-friendly facility or laboratory identifier for the instrument (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and equipment tracking.
--     * Slot: instrument_category Description: Category distinguishing beamlines from laboratory equipment
--     * Slot: facility_name Description: Name of the research facility where the instrument is located
--     * Slot: facility_ror Description: Research Organization Registry (ROR) identifier for the facility
--     * Slot: beamline_id Description: Beamline identifier at synchrotron/neutron facility
--     * Slot: manufacturer Description: Instrument manufacturer
--     * Slot: model Description: Instrument model
--     * Slot: installation_date Description: Date of instrument installation
--     * Slot: current_status Description: Current operational status
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: CryoEMInstrument Description: Cryo-EM microscope specifications
--     * Slot: cs_corrector Description: Spherical aberration corrector present
--     * Slot: phase_plate Description: Phase plate available
--     * Slot: detector_technology Description: Generic detector technology type
--     * Slot: detector_manufacturer Description: Detector manufacturer (e.g., Gatan, ThermoFisher, DirectElectron)
--     * Slot: detector_model Description: Detector model (e.g., K3, Falcon 4i, DE-64)
--     * Slot: detector_mode Description: Supported or default detector operating mode
--     * Slot: detector_position Description: Physical position of detector in microscope (e.g., post-GIF, pre-column)
--     * Slot: detector_dimensions Description: Detector dimensions in pixels (e.g., 4096x4096, 5760x4092)
--     * Slot: phase_plate_type Description: Type of phase plate if present
--     * Slot: energy_filter_present Description: Whether energy filter is present
--     * Slot: energy_filter_make Description: Energy filter manufacturer
--     * Slot: energy_filter_model Description: Energy filter model
--     * Slot: microscope_software Description: Microscope control software (e.g., SerialEM, EPU, Leginon)
--     * Slot: microscope_software_version Description: Software version
--     * Slot: imaging_mode Description: Imaging mode for electron microscopy
--     * Slot: instrument_code Description: Human-friendly facility or laboratory identifier for the instrument (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and equipment tracking.
--     * Slot: instrument_category Description: Category distinguishing beamlines from laboratory equipment
--     * Slot: facility_name Description: Name of the research facility where the instrument is located
--     * Slot: facility_ror Description: Research Organization Registry (ROR) identifier for the facility
--     * Slot: beamline_id Description: Beamline identifier at synchrotron/neutron facility
--     * Slot: manufacturer Description: Instrument manufacturer
--     * Slot: model Description: Instrument model
--     * Slot: installation_date Description: Date of instrument installation
--     * Slot: current_status Description: Current operational status
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: accelerating_voltage_id Description: Accelerating voltage in kV
--     * Slot: pixel_size_physical_um_id Description: Physical pixel size of the detector in micrometers
--     * Slot: autoloader_capacity_id Description: Number of grids the autoloader can hold
--     * Slot: cs_id Description: Spherical aberration (Cs) in millimeters
--     * Slot: c2_aperture_id Description: C2 aperture size in micrometers
--     * Slot: objective_aperture_id Description: Objective aperture size in micrometers
--     * Slot: energy_filter_slit_width_id Description: Energy filter slit width in eV
--     * Slot: pixel_size_physical_id Description: Physical pixel size in micrometers
--     * Slot: spotsize_id Description: Electron beam spot size setting
--     * Slot: gunlens_id Description: Gun lens setting
--     * Slot: tem_beam_diameter_id Description: TEM beam diameter in micrometers
-- # Class: XRayInstrument Description: X-ray diffractometer or synchrotron beamline specifications
--     * Slot: source_type Description: Type of X-ray source
--     * Slot: detector_technology Description: Generic detector technology type
--     * Slot: detector_manufacturer Description: Detector manufacturer (e.g., Dectris, Bruker, Rigaku, Rayonix)
--     * Slot: detector_model Description: Detector model (e.g., EIGER2 X 16M, PILATUS3 X 6M, PHOTON III)
--     * Slot: monochromator_type Description: Type of monochromator
--     * Slot: goniometer_type Description: Type of goniometer
--     * Slot: crystal_cooling_capability Description: Crystal cooling system available
--     * Slot: instrument_code Description: Human-friendly facility or laboratory identifier for the instrument (e.g., 'TITAN-KRIOS-1', 'ALS-12.3.1-SIBYLS', 'RIGAKU-FR-E'). Used for local reference and equipment tracking.
--     * Slot: instrument_category Description: Category distinguishing beamlines from laboratory equipment
--     * Slot: facility_name Description: Name of the research facility where the instrument is located
--     * Slot: facility_ror Description: Research Organization Registry (ROR) identifier for the facility
--     * Slot: beamline_id Description: Beamline identifier at synchrotron/neutron facility
--     * Slot: manufacturer Description: Instrument manufacturer
--     * Slot: model Description: Instrument model
--     * Slot: installation_date Description: Date of instrument installation
--     * Slot: current_status Description: Current operational status
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: energy_min_id Description: Minimum X-ray energy in keV
--     * Slot: energy_max_id Description: Maximum X-ray energy in keV
--     * Slot: beam_size_min_id Description: Minimum beam size in micrometers
--     * Slot: beam_size_max_id Description: Maximum beam size in micrometers
--     * Slot: flux_density_id Description: Photon flux density in photons/s/mm²
-- # Class: ExperimentRun Description: An experimental data collection session
--     * Slot: experiment_code Description: Human-friendly laboratory or facility identifier for the experiment (e.g., 'SIBYLS-2024-02-01-hetBGL', 'CRYOEM-RUN-240815-001'). Used for local tracking and cross-referencing within laboratory systems.
--     * Slot: experiment_date Description: Date of the experiment
--     * Slot: operator_id Description: Identifier or name of the person who performed the experiment data collection (e.g., 'jsmith', 'John Smith', or personnel ID)
--     * Slot: technique Description: Technique used for data collection
--     * Slot: raw_data_location Description: Location of raw data files
--     * Slot: processing_status Description: Current processing status
--     * Slot: autoloader_slot Description: Autoloader slot identifier
--     * Slot: acquisition_software Description: Acquisition software used (e.g., SerialEM, EPU, Leginon)
--     * Slot: acquisition_software_version Description: Version of acquisition software
--     * Slot: beamline Description: Beamline identifier (e.g., FMX, AMX, 12.3.1)
--     * Slot: synchrotron_mode Description: Synchrotron storage ring fill mode
--     * Slot: start_time Description: Data collection start timestamp
--     * Slot: end_time Description: Data collection end timestamp
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: experimental_conditions_id Description: Environmental and experimental conditions
--     * Slot: data_collection_strategy_id Description: Strategy for data collection
--     * Slot: magnification_id Description: Magnification used during data collection
--     * Slot: calibrated_pixel_size_id Description: Calibrated pixel size in Angstroms per pixel
--     * Slot: camera_binning_id Description: Camera binning factor. This must be a positive float value (e.g., 1, 1.5, 2, 3).
--     * Slot: exposure_time_per_frame_id Description: Exposure time per frame in milliseconds
--     * Slot: frames_per_movie_id Description: Number of frames per movie
--     * Slot: total_exposure_time_id Description: Total exposure time in milliseconds
--     * Slot: total_dose_id Description: Total electron dose in e-/Angstrom^2
--     * Slot: dose_rate_id Description: Dose rate in e-/pixel/s or e-/Angstrom^2/s
--     * Slot: defocus_target_id Description: Target defocus value in micrometers
--     * Slot: defocus_range_min_id Description: Minimum defocus range in micrometers
--     * Slot: defocus_range_max_id Description: Maximum defocus range in micrometers
--     * Slot: defocus_range_increment_id Description: Defocus range increment in micrometers
--     * Slot: astigmatism_target_id Description: Target astigmatism in Angstroms
--     * Slot: coma_id Description: Coma aberration in nanometers
--     * Slot: stage_tilt_id Description: Stage tilt angle in degrees
--     * Slot: shots_per_hole_id Description: Number of shots taken per hole
--     * Slot: holes_per_group_id Description: Number of holes per group. Data providers may include unit information in the QuantityValue if needed.
--     * Slot: wavelength_id Description: X-ray wavelength, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: oscillation_angle_id Description: Oscillation angle per image, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: start_angle_id Description: Starting rotation angle, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: number_of_images_id Description: Total number of diffraction images collected
--     * Slot: beam_center_x_id Description: Beam center X coordinate, typically specified in pixels ([px]). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: beam_center_y_id Description: Beam center Y coordinate, typically specified in pixels ([px]). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: detector_distance_id Description: Distance from sample to detector, typically specified in millimeters (mm). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: pixel_size_x_id Description: Pixel size X dimension, typically specified in micrometers (µm). Data providers may specify alternative units (e.g., Angstroms) by including the unit in the QuantityValue.
--     * Slot: pixel_size_y_id Description: Pixel size Y dimension, typically specified in micrometers (µm). Data providers may specify alternative units (e.g., Angstroms) by including the unit in the QuantityValue.
--     * Slot: total_rotation_id Description: Total rotation range collected, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: transmission_id Description: X-ray beam transmission as a percentage (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue.
--     * Slot: flux_id Description: Photon flux at sample position, typically specified in photons per second. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: flux_end_id Description: Photon flux at end of data collection, typically specified in photons per second. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: slit_gap_horizontal_id Description: Horizontal slit gap aperture, typically specified in micrometers (µm). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: slit_gap_vertical_id Description: Vertical slit gap aperture, typically specified in micrometers (µm). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: undulator_gap_id Description: Undulator gap setting, typically specified in millimeters (mm). Data providers may specify alternative units by including the unit in the QuantityValue. Primary undulator gap for beamlines with insertion devices.
--     * Slot: exposure_time_id Description: Exposure time per image, typically specified in seconds (s). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: resolution_id Description: Resolution at edge of detector, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: resolution_at_corner_id Description: Resolution at corner of detector, typically specified in Angstroms (Å). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: ispyb_data_collection_id_id Description: ISPyB DataCollection.dataCollectionId for traceability
--     * Slot: ispyb_session_id_id Description: ISPyB BLSession.sessionId
--     * Slot: beam_size_x_id Description: Beam size X dimension, typically specified in micrometers (µm). Data providers may specify alternative units (e.g., Angstroms) by including the unit in the QuantityValue.
--     * Slot: beam_size_y_id Description: Beam size Y dimension, typically specified in micrometers (µm). Data providers may specify alternative units (e.g., Angstroms) by including the unit in the QuantityValue.
--     * Slot: dwell_time_id Description: Dwell time per pixel, typically specified in milli-seconds (ms). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: energy_id Description: X-ray energy, typically specified in eV. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: beamline_parameters_id Description: Relevant other motor positions of the beamline
-- # Class: WorkflowRun Description: A computational processing workflow execution
--     * Slot: workflow_code Description: Human-friendly identifier for the computational workflow run (e.g., 'MOTION-CORR-RUN-001', 'RELION-REFINE-240815'). Used for tracking processing pipelines and computational provenance.
--     * Slot: workflow_type Description: Type of processing workflow
--     * Slot: software_name Description: Software used for processing
--     * Slot: software_version Description: Software version
--     * Slot: additional_software Description: Additional software used in pipeline
--     * Slot: processing_parameters Description: Parameters used in processing
--     * Slot: parameters_file_path Description: Path to parameters file or text of key parameters
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: processing_level_id Description: Processing level (0=raw, 1=corrected, 2=derived, 3=model)
-- # Class: DataFile Description: A data file generated or used in the study
--     * Slot: file_name Description: Name of the file
--     * Slot: file_path Description: Path to the file
--     * Slot: file_format Description: File format
--     * Slot: checksum Description: SHA-256 checksum for data integrity
--     * Slot: creation_date Description: File creation date
--     * Slot: data_type Description: Type of data in the file
--     * Slot: storage_uri Description: Storage URI (S3, Globus, etc.)
--     * Slot: related_entity Description: ID of the entity that owns this file
--     * Slot: file_role Description: Role of the file (raw, intermediate, final, diagnostic, metadata)
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: file_size_bytes_id Description: File size in bytes
-- # Class: Image Description: An image file from structural biology experiments
--     * Slot: file_name Description: Image file name
--     * Slot: acquisition_date Description: Date image was acquired
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: pixel_size_id Description: Pixel size, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dimensions_x_id Description: Image width, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dimensions_y_id Description: Image height, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: exposure_time_id Description: Exposure time, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dose_id Description: Electron dose in e-/Å²
-- # Class: Image2D Description: A 2D image (micrograph, diffraction pattern)
--     * Slot: file_name Description: Image file name
--     * Slot: acquisition_date Description: Date image was acquired
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: defocus_id Description: Defocus value, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: astigmatism_id Description: Astigmatism value, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: pixel_size_id Description: Pixel size, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dimensions_x_id Description: Image width, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dimensions_y_id Description: Image height, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: exposure_time_id Description: Exposure time, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dose_id Description: Electron dose in e-/Å²
-- # Class: Image3D Description: A 3D volume or tomogram
--     * Slot: reconstruction_method Description: Method used for 3D reconstruction
--     * Slot: file_name Description: Image file name
--     * Slot: acquisition_date Description: Date image was acquired
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: dimensions_z_id Description: Image depth, typically specified in pixels or slices. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: voxel_size_id Description: Voxel size, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: pixel_size_id Description: Pixel size, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dimensions_x_id Description: Image width, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dimensions_y_id Description: Image height, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: exposure_time_id Description: Exposure time, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dose_id Description: Electron dose in e-/Å²
-- # Class: Movie Description: Raw cryo-EM movie with frame-by-frame metadata for motion correction
--     * Slot: super_resolution Description: Whether super-resolution mode was used
--     * Slot: timestamp Description: Acquisition timestamp
--     * Slot: grid_square_id Description: Grid square identifier
--     * Slot: hole_id Description: Hole identifier within grid square
--     * Slot: acquisition_group Description: Acquisition group identifier (e.g., template or area)
--     * Slot: file_name Description: Image file name
--     * Slot: acquisition_date Description: Date image was acquired
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: frames_id Description: Number of frames in the movie
--     * Slot: pixel_size_unbinned_id Description: Unbinned pixel size, typically specified in Angstroms per pixel. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: stage_position_x_id Description: Stage X position, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: stage_position_y_id Description: Stage Y position, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: stage_position_z_id Description: Stage Z position, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: nominal_defocus_id Description: Nominal defocus value, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dose_per_frame_id Description: Electron dose per frame in e-/Angstrom^2
--     * Slot: beam_shift_x_id Description: Beam shift X in microradians
--     * Slot: beam_shift_y_id Description: Beam shift Y in microradians
--     * Slot: ice_thickness_estimate_id Description: Estimated ice thickness, typically specified in nanometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: defocus_id Description: Defocus value, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: astigmatism_id Description: Astigmatism value, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: pixel_size_id Description: Pixel size, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dimensions_x_id Description: Image width, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dimensions_y_id Description: Image height, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: exposure_time_id Description: Exposure time, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dose_id Description: Electron dose in e-/Å²
-- # Class: FTIRImage Description: Fourier Transform Infrared (FTIR) spectroscopy image capturing molecular composition through vibrational spectroscopy
--     * Slot: apodization_function Description: Mathematical function used for apodization
--     * Slot: background_correction Description: Method used for background correction
--     * Slot: file_name Description: Name of the file
--     * Slot: file_path Description: Path to the file
--     * Slot: file_format Description: File format
--     * Slot: checksum Description: SHA-256 checksum for data integrity
--     * Slot: creation_date Description: File creation date
--     * Slot: data_type Description: Type of data in the file
--     * Slot: storage_uri Description: Storage URI (S3, Globus, etc.)
--     * Slot: related_entity Description: ID of the entity that owns this file
--     * Slot: file_role Description: Role of the file (raw, intermediate, final, diagnostic, metadata)
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: pixel_size_id Description: Pixel size, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dimensions_x_id Description: Image width, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dimensions_y_id Description: Image height, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: wavenumber_min_id Description: Minimum wavenumber, typically specified in inverse centimeters (cm⁻¹). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: wavenumber_max_id Description: Maximum wavenumber, typically specified in inverse centimeters (cm⁻¹). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: spectral_resolution_id Description: Spectral resolution, typically specified in inverse centimeters (cm⁻¹). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: number_of_scans_id Description: Number of scans averaged for the spectrum
--     * Slot: file_size_bytes_id Description: File size in bytes
-- # Class: FluorescenceImage Description: Fluorescence microscopy image capturing specific molecular targets through fluorescent labeling
--     * Slot: excitation_filter Description: Specifications of the excitation filter
--     * Slot: emission_filter Description: Specifications of the emission filter
--     * Slot: fluorophore Description: Name or type of fluorophore used
--     * Slot: channel_name Description: Name of the fluorescence channel (e.g., DAPI, GFP, RFP)
--     * Slot: file_name Description: Image file name
--     * Slot: acquisition_date Description: Date image was acquired
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: excitation_wavelength_id Description: Excitation wavelength, typically specified in nanometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: emission_wavelength_id Description: Emission wavelength, typically specified in nanometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: laser_power_id Description: Laser power, typically specified in milliwatts. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: pinhole_size_id Description: Pinhole size, typically specified in Airy units for confocal microscopy. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: quantum_yield_id Description: Quantum yield of the fluorophore
--     * Slot: defocus_id Description: Defocus value, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: astigmatism_id Description: Astigmatism value, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: pixel_size_id Description: Pixel size, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dimensions_x_id Description: Image width, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dimensions_y_id Description: Image height, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: exposure_time_id Description: Exposure time, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dose_id Description: Electron dose in e-/Å²
-- # Class: OpticalImage Description: Visible light optical microscopy or photography image
--     * Slot: illumination_type Description: Type of illumination (brightfield, darkfield, phase contrast, DIC)
--     * Slot: white_balance Description: White balance settings
--     * Slot: contrast_method Description: Contrast enhancement method used
--     * Slot: file_name Description: Image file name
--     * Slot: acquisition_date Description: Date image was acquired
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: magnification_id Description: Optical magnification factor. Data providers may specify the unit (e.g., times, X) in the QuantityValue.
--     * Slot: numerical_aperture_id Description: Numerical aperture of the objective lens. Data providers may include unit information in the QuantityValue if needed.
--     * Slot: defocus_id Description: Defocus value, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: astigmatism_id Description: Astigmatism value, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: pixel_size_id Description: Pixel size, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dimensions_x_id Description: Image width, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dimensions_y_id Description: Image height, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: exposure_time_id Description: Exposure time, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dose_id Description: Electron dose in e-/Å²
-- # Class: XRFImage Description: X-ray fluorescence (XRF) image showing elemental distribution
--     * Slot: source_type Description: X-ray source type (synchrotron or lab-source)
--     * Slot: detector_technology Description: Type of X-ray detector technology used
--     * Slot: detector_model Description: Specific detector model used for XRF measurement
--     * Slot: calibration_standard Description: Reference standard used for calibration
--     * Slot: file_name Description: Name of the file
--     * Slot: file_path Description: Path to the file
--     * Slot: file_format Description: File format
--     * Slot: checksum Description: SHA-256 checksum for data integrity
--     * Slot: creation_date Description: File creation date
--     * Slot: data_type Description: Type of data in the file
--     * Slot: storage_uri Description: Storage URI (S3, Globus, etc.)
--     * Slot: related_entity Description: ID of the entity that owns this file
--     * Slot: file_role Description: Role of the file (raw, intermediate, final, diagnostic, metadata)
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: pixel_size_id Description: Pixel size, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dimensions_x_id Description: Image width, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dimensions_y_id Description: Image height, typically specified in pixels. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: beam_energy_id Description: X-ray beam energy, typically specified in kiloelectronvolts (keV). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: beam_size_id Description: X-ray beam size, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dwell_time_id Description: Dwell time per pixel, typically specified in milliseconds. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: flux_id Description: Photon flux, typically specified in photons per second. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: file_size_bytes_id Description: File size in bytes
-- # Class: ImageFeature Description: Semantic annotations describing features identified in images using controlled vocabulary terms
--     * Slot: id
--     * Slot: description
-- # Class: OntologyTerm Description: A term from a controlled vocabulary or ontology
--     * Slot: label Description: The human-readable label or name of the ontology term
--     * Slot: definition Description: The formal definition or meaning of the ontology term
--     * Slot: ontology Description: The ontology or controlled vocabulary this term comes from (e.g., GO, SO, UBERON)
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: ImageFeature_id Description: Autocreated FK slot
--     * Slot: OntologyTerm_id Description: Autocreated FK slot
-- # Class: BufferComposition Description: Buffer composition for sample storage
--     * Slot: id
--     * Slot: description
--     * Slot: ph_id Description: pH of the buffer (range: 0-14)
-- # Class: StorageConditions Description: Storage conditions for samples
--     * Slot: id
--     * Slot: duration Description: Storage duration
--     * Slot: atmosphere Description: Storage atmosphere conditions
--     * Slot: description
--     * Slot: temperature_id Description: Storage temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
-- # Abstract Class: TechniqueSpecificPreparation Description: Base class for technique-specific preparation details
--     * Slot: id
--     * Slot: description
-- # Class: CryoEMPreparation Description: Cryo-EM specific sample preparation
--     * Slot: id
--     * Slot: grid_type Description: Type of EM grid used
--     * Slot: support_film Description: Support film type
--     * Slot: vitrification_method Description: Method used for vitrification
--     * Slot: grid_material Description: Grid material
--     * Slot: glow_discharge_applied Description: Whether glow discharge treatment was applied
--     * Slot: glow_discharge_atmosphere Description: Glow discharge atmosphere (air, amylamine)
--     * Slot: vitrification_instrument Description: Vitrification instrument used (e.g., Vitrobot)
--     * Slot: plasma_treatment Description: Plasma treatment details
--     * Slot: description
--     * Slot: hole_size_id Description: Hole size, typically specified in micrometers (range: 0.5-5.0). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: blot_time_id Description: Blotting time, typically specified in seconds (range: 0.5-10.0). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: blot_force_id Description: Blotting force setting
--     * Slot: humidity_percentage_id Description: Chamber humidity during vitrification (range: 0-100), typically specified as a percentage. Data providers may specify as decimal fraction by including the unit in the QuantityValue.
--     * Slot: chamber_temperature_id Description: Chamber temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: glow_discharge_time_id Description: Glow discharge time, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: glow_discharge_current_id Description: Glow discharge current, typically specified in milliamperes. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: glow_discharge_pressure_id Description: Glow discharge pressure, typically specified in millibars. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: blot_number_id Description: Number of blots applied
--     * Slot: wait_time_id Description: Wait time before blotting, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: blotter_height_id Description: Blotter height setting. Data providers may include unit information in the QuantityValue if needed.
--     * Slot: blotter_setting_id Description: Blotter setting value. Data providers may include unit information in the QuantityValue if needed.
--     * Slot: sample_applied_volume_id Description: Volume of sample applied, typically specified in microliters. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: ethane_temperature_id Description: Ethane temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
-- # Class: XRayPreparation Description: X-ray crystallography specific preparation
--     * Slot: id
--     * Slot: protein_buffer Description: Buffer composition for protein solution
--     * Slot: additives Description: Additives mixed with protein before crystallization
--     * Slot: crystallization_method Description: Method used for crystallization
--     * Slot: screen_name Description: Name of crystallization screen used
--     * Slot: drop_ratio_protein_to_reservoir Description: Ratio of protein to reservoir solution in drop (e.g., 1:1, 2:1)
--     * Slot: seeding_type Description: Type of seeding used (micro, macro, streak)
--     * Slot: seed_stock_dilution Description: Dilution factor for seed stock
--     * Slot: initial_hit_condition Description: Description of initial crystallization hit condition
--     * Slot: optimization_strategy Description: Strategy used to optimize crystals
--     * Slot: optimized_condition Description: Final optimized crystallization condition
--     * Slot: crystal_size_um Description: Crystal dimensions in micrometers
--     * Slot: cryoprotectant Description: Cryoprotectant used
--     * Slot: soak_compound Description: Compound used for soaking (ligand, heavy atom)
--     * Slot: soak_conditions Description: Conditions for crystal soaking
--     * Slot: mounting_method Description: Crystal mounting method
--     * Slot: flash_cooling_method Description: Flash cooling protocol
--     * Slot: crystal_notes Description: Additional notes about crystal quality and handling
--     * Slot: description
--     * Slot: protein_concentration_mg_per_ml_id Description: Protein concentration for crystallization in mg/mL
--     * Slot: temperature_c_id Description: Crystallization temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: drop_volume_nl_id Description: Total drop volume, typically specified in nanoliters. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: reservoir_volume_ul_id Description: Reservoir volume, typically specified in microliters. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: cryoprotectant_concentration_id Description: Cryoprotectant concentration, typically specified as a percentage. Data providers may specify as decimal fraction by including the unit in the QuantityValue.
--     * Slot: loop_size_id Description: Loop size, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: mounting_temperature_id Description: Temperature during mounting, typically specified in Kelvin. Data providers may specify alternative units by including the unit in the QuantityValue.
-- # Class: ExperimentalConditions Description: Environmental and experimental conditions
--     * Slot: id
--     * Slot: atmosphere Description: Atmosphere composition
--     * Slot: description
--     * Slot: temperature_id Description: Temperature, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: humidity_id Description: Humidity, typically specified as a percentage (0-100). Data providers may specify as a decimal fraction or percentage by including the unit in the QuantityValue.
--     * Slot: pressure_id Description: Pressure, typically specified in kilopascals (kPa). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: beam_energy_id Description: Beam energy, typically specified in kiloelectronvolts (keV). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: exposure_time_id Description: Exposure time, typically specified in seconds. Data providers may specify alternative units by including the unit in the QuantityValue.
-- # Class: DataCollectionStrategy Description: Strategy for data collection
--     * Slot: id
--     * Slot: collection_mode Description: Mode of data collection
--     * Slot: detector_mode Description: Detector operating mode used during this experiment
--     * Slot: attenuator Description: Attenuator setting used
--     * Slot: strategy_notes Description: Notes about data collection strategy
--     * Slot: description
--     * Slot: total_frames_id Description: Total number of frames/images
--     * Slot: frame_rate_id Description: Frame rate, typically specified in frames per second. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: total_dose_id Description: Total electron dose for cryo-EM, typically specified in electrons per Angstrom squared (e⁻/Å²). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: dose_per_frame_id Description: Dose per frame, typically specified in electrons per Angstrom squared (e⁻/Å²). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: wavelength_a_id Description: X-ray wavelength, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: pixel_size_calibrated_id Description: Calibrated pixel size for this experiment, typically specified in Angstroms (Å) per pixel. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: detector_distance_mm_id Description: Detector distance, typically specified in millimeters. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: beam_center_x_px_id Description: Beam center X coordinate in pixels
--     * Slot: beam_center_y_px_id Description: Beam center Y coordinate in pixels
--     * Slot: beam_size_um_id Description: Beam size, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: flux_photons_per_s_id Description: Photon flux, typically specified in photons per second. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: transmission_percent_id Description: Beam transmission, typically specified as a percentage (0-100). Data providers may specify as decimal fraction by including the unit in the QuantityValue.
--     * Slot: temperature_k_id Description: Data collection temperature, typically specified in Kelvin. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: oscillation_per_image_deg_id Description: Oscillation angle per image, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: total_rotation_deg_id Description: Total rotation range, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
-- # Class: QualityMetrics Description: Quality metrics for experiments
--     * Slot: id
--     * Slot: space_group Description: Crystallographic space group
--     * Slot: anomalous_used Description: Whether anomalous signal was used
--     * Slot: description
--     * Slot: resolution_id Description: Resolution, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: resolution_high_shell_a_id Description: High resolution shell limit, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: resolution_low_a_id Description: Low resolution limit, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: completeness_id Description: Data completeness, typically specified as a percentage (0-100). Data providers may specify as decimal fraction by including the unit in the QuantityValue.
--     * Slot: completeness_high_res_shell_percent_id Description: Completeness in highest resolution shell, typically specified as a percentage (0-100). Data providers may specify as decimal fraction by including the unit in the QuantityValue.
--     * Slot: signal_to_noise_id Description: Signal to noise ratio
--     * Slot: mean_i_over_sigma_i_id Description: Mean I/sigma(I)
--     * Slot: unit_cell_a_id Description: Unit cell parameter a, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: unit_cell_b_id Description: Unit cell parameter b, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: unit_cell_c_id Description: Unit cell parameter c, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: unit_cell_alpha_id Description: Unit cell angle alpha, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: unit_cell_beta_id Description: Unit cell angle beta, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: unit_cell_gamma_id Description: Unit cell angle gamma, typically specified in degrees. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: multiplicity_id Description: Data multiplicity (redundancy)
--     * Slot: cc_half_id Description: Half-set correlation coefficient CC(1/2)
--     * Slot: r_merge_id Description: Rmerge - merge R-factor
--     * Slot: r_pim_id Description: Rpim - precision-indicating merging R-factor
--     * Slot: wilson_b_factor_a2_id Description: Wilson B-factor in Angstroms squared
--     * Slot: anom_corr_id Description: Anomalous correlation
--     * Slot: anom_sig_ano_id Description: Anomalous signal strength
--     * Slot: r_work_id Description: Refinement R-factor (working set)
--     * Slot: r_free_id Description: R-free (test set)
--     * Slot: ramachandran_favored_percent_id Description: Percentage of residues in favored Ramachandran regions
--     * Slot: ramachandran_outliers_percent_id Description: Percentage of Ramachandran outliers
--     * Slot: clashscore_id Description: MolProbity clashscore
--     * Slot: molprobity_score_id Description: Overall MolProbity score
--     * Slot: average_b_factor_a2_id Description: Average B-factor in Angstroms squared
--     * Slot: i_zero_id Description: Forward scattering intensity I(0)
--     * Slot: rg_id Description: Radius of gyration, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: r_factor_id Description: R-factor for crystallography (deprecated, use r_work)
-- # Class: ComputeResources Description: Computational resources used
--     * Slot: id
--     * Slot: description
--     * Slot: cpu_hours_id Description: CPU hours used, measured in hours. Data providers may specify alternative time units by including the unit in the QuantityValue.
--     * Slot: gpu_hours_id Description: GPU hours used, measured in hours. Data providers may specify alternative time units by including the unit in the QuantityValue.
--     * Slot: memory_gb_id Description: Maximum memory used, typically specified in gigabytes (GB). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: storage_gb_id Description: Storage used, typically specified in gigabytes (GB). Data providers may specify alternative units by including the unit in the QuantityValue.
-- # Class: MotionCorrectionParameters Description: Parameters specific to motion correction workflows
--     * Slot: id
--     * Slot: dose_weighting Description: Whether dose weighting was applied
--     * Slot: anisotropic_correction Description: Whether anisotropic motion correction was applied
--     * Slot: description
--     * Slot: patch_size_id Description: Patch size for local motion correction
--     * Slot: binning_id Description: Binning factor applied during motion correction. This must be a positive float value (e.g., 1, 1.5, 2, 3).
--     * Slot: bfactor_dose_weighting_id Description: B-factor for dose weighting, typically specified in Angstroms squared. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: frame_grouping_id Description: Number of frames grouped together
--     * Slot: output_binning_id Description: Output binning factor. This must be a positive float value (e.g., 1, 1.5, 2, 3).
--     * Slot: drift_total_id Description: Total drift, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
-- # Class: CTFEstimationParameters Description: Parameters specific to CTF estimation workflows
--     * Slot: id
--     * Slot: description
--     * Slot: defocus_search_min_id Description: Minimum defocus search range, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: defocus_search_max_id Description: Maximum defocus search range, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: defocus_step_id Description: Defocus search step, typically specified in micrometers. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: amplitude_contrast_id Description: Amplitude contrast value
--     * Slot: cs_used_in_estimation_id Description: Spherical aberration (Cs) value used during CTF estimation, typically specified in millimeters; may differ from instrument specification. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: voltage_used_in_estimation_id Description: Accelerating voltage value used during CTF estimation, typically specified in kilovolts (kV); may differ from instrument specification. Data providers may specify alternative units by including the unit in the QuantityValue.
-- # Class: ParticlePickingParameters Description: Parameters specific to particle picking workflows
--     * Slot: id
--     * Slot: picking_method Description: Method used (manual, template_matching, deep_learning, LoG, Topaz, other)
--     * Slot: model_name Description: Name or identifier of the deep learning model (e.g., 'resnet16', 'resnet8', 'cryolo_general'). Use this for standard pretrained models. Either model_name or model_file_path should be provided when using deep learning methods.
--     * Slot: model_file_path Description: Path to deep learning model file if using a local or custom trained model file. Use this instead of model_name when pointing to a specific file on disk. Either model_name or model_file_path should be provided when using deep learning methods.
--     * Slot: model_source Description: Source or software associated with the model (e.g., 'topaz', 'cryolo', 'warp', 'custom', 'pretrained'). Helps track model provenance and should be provided alongside model_name or model_file_path to document which software/framework the model is for.
--     * Slot: description
--     * Slot: box_size_id Description: Particle box size in pixels
--     * Slot: threshold_id Description: Picking threshold
--     * Slot: power_score_id Description: Power score threshold
--     * Slot: ncc_score_id Description: Normalized cross-correlation score threshold
-- # Class: RefinementParameters Description: Parameters specific to 3D refinement workflows
--     * Slot: id
--     * Slot: symmetry Description: Symmetry applied (C1, Cn, Dn, T, O, I)
--     * Slot: gold_standard Description: Whether gold-standard refinement was used
--     * Slot: split_strategy Description: Strategy for data splitting
--     * Slot: description
--     * Slot: pixel_size_id Description: Pixel size, typically specified in Angstroms per pixel. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: box_size_id Description: Box size in pixels
--     * Slot: resolution_0_143_id Description: Resolution at FSC=0.143, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: resolution_0_5_id Description: Resolution at FSC=0.5, typically specified in Angstroms. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: map_sharpening_bfactor_id Description: B-factor used for map sharpening, typically specified in Angstroms squared (Å²). Data providers may specify alternative units by including the unit in the QuantityValue.
-- # Class: StudySampleAssociation Description: M:N link between Study and Sample with role metadata
--     * Slot: id
--     * Slot: study_id Description: Reference to the study
--     * Slot: sample_id Description: Reference to the sample
--     * Slot: role Description: Role of sample in study (e.g., target, control, reference)
--     * Slot: date_added Description: Date when sample was added to study
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: SampleDataAssociation Description: M:N link between Sample and Data with role metadata
--     * Slot: id
--     * Slot: sample_id Description: Reference to the sample
--     * Slot: data_id Description: Reference to the data
--     * Slot: role Description: Role of sample in study (e.g., target, control, reference)
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: StudyExperimentAssociation Description: M:N link between Study and ExperimentRun
--     * Slot: id
--     * Slot: study_id Description: Reference to the study
--     * Slot: experiment_id Description: Reference to the experiment run
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: StudyWorkflowAssociation Description: M:N link between Study and WorkflowRun
--     * Slot: id
--     * Slot: study_id Description: Reference to the study
--     * Slot: workflow_id Description: Reference to the workflow run
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: ExperimentSampleAssociation Description: M:N link between ExperimentRun and Sample with role metadata
--     * Slot: id
--     * Slot: experiment_id Description: Reference to the experiment run
--     * Slot: sample_id Description: Reference to the sample
--     * Slot: role Description: Role of sample in experiment
--     * Slot: preparation_id Description: Specific preparation used for this sample in this experiment
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: ExperimentInstrumentAssociation Description: M:N link between ExperimentRun and Instrument
--     * Slot: id
--     * Slot: experiment_id Description: Reference to the experiment run
--     * Slot: instrument_id Description: Reference to the instrument
--     * Slot: role Description: Role of instrument in experiment
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: WorkflowExperimentAssociation Description: M:N link between WorkflowRun and source ExperimentRuns
--     * Slot: id
--     * Slot: workflow_id Description: Reference to the workflow run
--     * Slot: experiment_id Description: Reference to the source experiment run
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: WorkflowInputAssociation Description: Links input DataFiles to WorkflowRun
--     * Slot: id
--     * Slot: workflow_id Description: Reference to the workflow run
--     * Slot: file_id Description: Reference to the input data file
--     * Slot: input_type Description: Type of input for the workflow
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: WorkflowOutputAssociation Description: Links output DataFiles to WorkflowRun
--     * Slot: id
--     * Slot: workflow_id Description: Reference to the workflow run
--     * Slot: file_id Description: Reference to the output data file
--     * Slot: output_type Description: Type of output from the workflow
--     * Slot: Dataset_id Description: Autocreated FK slot
-- # Class: Any
--     * Slot: id
-- # Abstract Class: AttributeValue Description: The value for any attribute of an entity. This object can hold both the un-normalized atomic value and the structured value.
--     * Slot: id
--     * Slot: raw_value Description: Unnormalized atomic string representation, suggested syntax {number} {unit}
--     * Slot: attribute_uid Description: The attribute being represented.
-- # Class: Attribute Description: A domain, measurement, attribute, property, or any descriptor for additional properties to be added to an entity. Where available, please use OBO Foundry ontologies or other controlled vocabularies for attributes; the label should be the term name from the ontology and the id should be the fully-qualified CURIE.
--     * Slot: uid
--     * Slot: id Description: A CURIE for the attribute, should one exist. Where available, please use OBO Foundry ontologies or other controlled vocabularies for labelling attributes; the id should be the term ID from the ontology.
--     * Slot: label Description: Text string to describe the attribute. Where available, please use OBO Foundry ontologies or other controlled vocabularies for labelling attributes; the label should be the term name from the ontology.
-- # Class: QuantityValue Description: A simple quantity value, representing a measurement with a numeric value and unit. This allows data providers to specify measurements in their preferred unit while enabling standardized interpretation. For example, a pixel size could be specified as 1.5 micrometers or 15 Angstroms, with the unit clearly specified.
--     * Slot: id
--     * Slot: maximum_numeric_value Description: The maximum value part, expressed as a number, of the quantity value when the value covers a range.
--     * Slot: minimum_numeric_value Description: The minimum value part, expressed as a number, of the quantity value when the value covers a range.
--     * Slot: numeric_value Description: The numerical value of the quantity. May be null if the value is unknown or not measured.
--     * Slot: unit Description: The unit of measurement (e.g., "Angstroms", "micrometers", "kilodaltons"). Should match the UCUM standard notation or Unit Ontology.
--     * Slot: unit_cv_id Description: The unit of the quantity, expressed as a CURIE from the Unit Ontology (e.g., UO:0000016 for micrometer).
--     * Slot: raw_value Description: Unnormalized atomic string representation, suggested syntax {number} {unit}
--     * Slot: attribute_uid Description: The attribute being represented.
-- # Class: TextValue Description: A value described using a text string, optionally with a controlled vocabulary ID.
--     * Slot: id
--     * Slot: value Description: The text value
--     * Slot: value_cv_id Description: For values in a controlled vocabulary, the CV ID for the value.
--     * Slot: raw_value Description: Unnormalized atomic string representation, suggested syntax {number} {unit}
--     * Slot: attribute_uid Description: The attribute being represented.
-- # Class: DateTimeValue Description: A date or date and time value.
--     * Slot: id
--     * Slot: value Description: The date or date/time value, expressed in ISO 8601-compatible form. Dates should be expressed as YYYY-MM-DD; times should be expressed as HH:MM:SS with optional milliseconds and an indication of the timezone.
--     * Slot: raw_value Description: Unnormalized atomic string representation, suggested syntax {number} {unit}
--     * Slot: attribute_uid Description: The attribute being represented.
-- # Class: ProteinAnnotation Description: Base class for all protein-related functional and structural annotations
--     * Slot: protein_id Description: UniProt accession number
--     * Slot: pdb_entry Description: PDB identifier
--     * Slot: chain_id Description: Chain identifier in the PDB structure
--     * Slot: residue_range Description: Range of residues (e.g., '1-100', '25,27,30-35')
--     * Slot: confidence_score Description: Confidence score for the annotation (range: 0-1)
--     * Slot: evidence_type Description: Type of evidence supporting this annotation
--     * Slot: evidence_code Description: Evidence and Conclusion Ontology (ECO) code
--     * Slot: source_database Description: Source database or resource that provided this annotation
--     * Slot: annotation_method Description: Computational or experimental method used
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
-- # Class: FunctionalSite Description: Functional sites including catalytic, binding, and regulatory sites
--     * Slot: site_type Description: Type of functional site
--     * Slot: site_name Description: Common name for this site
--     * Slot: conservation_score Description: Evolutionary conservation score (range: 0-1)
--     * Slot: functional_importance Description: Description of functional importance
--     * Slot: ec_number Description: Enzyme Commission number for catalytic sites
--     * Slot: protein_id Description: UniProt accession number
--     * Slot: pdb_entry Description: PDB identifier
--     * Slot: chain_id Description: Chain identifier in the PDB structure
--     * Slot: residue_range Description: Range of residues (e.g., '1-100', '25,27,30-35')
--     * Slot: confidence_score Description: Confidence score for the annotation (range: 0-1)
--     * Slot: evidence_type Description: Type of evidence supporting this annotation
--     * Slot: evidence_code Description: Evidence and Conclusion Ontology (ECO) code
--     * Slot: source_database Description: Source database or resource that provided this annotation
--     * Slot: annotation_method Description: Computational or experimental method used
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: AggregatedProteinView_id Description: Autocreated FK slot
-- # Class: StructuralFeature Description: Structural features and properties of protein regions
--     * Slot: feature_type Description: Type of structural feature
--     * Slot: secondary_structure Description: Secondary structure assignment
--     * Slot: solvent_accessibility Description: Relative solvent accessible surface area (range: 0-1)
--     * Slot: backbone_flexibility Description: B-factor or flexibility measure
--     * Slot: disorder_probability Description: Probability of disorder (range: 0-1)
--     * Slot: conformational_state Description: Conformational state descriptor
--     * Slot: structural_motif Description: Known structural motif
--     * Slot: domain_assignment Description: Domain database assignment (CATH, SCOP, Pfam)
--     * Slot: domain_id Description: Domain identifier from domain database
--     * Slot: protein_id Description: UniProt accession number
--     * Slot: pdb_entry Description: PDB identifier
--     * Slot: chain_id Description: Chain identifier in the PDB structure
--     * Slot: residue_range Description: Range of residues (e.g., '1-100', '25,27,30-35')
--     * Slot: confidence_score Description: Confidence score for the annotation (range: 0-1)
--     * Slot: evidence_type Description: Type of evidence supporting this annotation
--     * Slot: evidence_code Description: Evidence and Conclusion Ontology (ECO) code
--     * Slot: source_database Description: Source database or resource that provided this annotation
--     * Slot: annotation_method Description: Computational or experimental method used
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: AggregatedProteinView_id Description: Autocreated FK slot
-- # Class: LigandInteraction Description: Small molecule/ligand interactions with proteins
--     * Slot: id
--     * Slot: ligand_id Description: Ligand identifier (ChEMBL, ChEBI, PubChem)
--     * Slot: ligand_name Description: Common name of the ligand
--     * Slot: ligand_smiles Description: SMILES representation of the ligand
--     * Slot: binding_affinity Description: Binding affinity value
--     * Slot: binding_affinity_type Description: Type of binding measurement (Kd, Ki, IC50)
--     * Slot: binding_affinity_unit Description: Unit of binding affinity
--     * Slot: interaction_type Description: Type of interaction
--     * Slot: is_cofactor Description: Whether the ligand is a cofactor
--     * Slot: is_drug_like Description: Whether the ligand has drug-like properties
--     * Slot: druggability_score Description: Druggability score of the binding site (range: 0-1)
--     * Slot: interaction_distance Description: Distance criteria for interaction (Angstroms)
--     * Slot: description
--     * Slot: FunctionalSite_id Description: Autocreated FK slot
--     * Slot: AggregatedProteinView_id Description: Autocreated FK slot
-- # Class: ProteinProteinInteraction Description: Protein-protein interactions and interfaces
--     * Slot: partner_protein_id Description: UniProt ID of interacting partner
--     * Slot: partner_chain_id Description: Chain ID of interacting partner
--     * Slot: interface_area Description: Buried surface area at interface (Ų)
--     * Slot: binding_energy Description: Calculated binding energy (kcal/mol)
--     * Slot: dissociation_constant Description: Experimental Kd if available
--     * Slot: complex_stability Description: Stability assessment of the complex
--     * Slot: biological_assembly Description: Whether this represents a biological assembly
--     * Slot: protein_id Description: UniProt accession number
--     * Slot: pdb_entry Description: PDB identifier
--     * Slot: chain_id Description: Chain identifier in the PDB structure
--     * Slot: residue_range Description: Range of residues (e.g., '1-100', '25,27,30-35')
--     * Slot: confidence_score Description: Confidence score for the annotation (range: 0-1)
--     * Slot: evidence_type Description: Type of evidence supporting this annotation
--     * Slot: evidence_code Description: Evidence and Conclusion Ontology (ECO) code
--     * Slot: source_database Description: Source database or resource that provided this annotation
--     * Slot: annotation_method Description: Computational or experimental method used
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: AggregatedProteinView_id Description: Autocreated FK slot
-- # Class: MutationEffect Description: Effects of mutations and variants on protein structure and function
--     * Slot: mutation Description: Mutation in standard notation (e.g., 'A123V')
--     * Slot: mutation_type Description: Type of mutation
--     * Slot: effect_on_stability Description: Effect on protein stability
--     * Slot: delta_delta_g Description: Change in folding free energy (kcal/mol)
--     * Slot: effect_on_function Description: Effect on protein function
--     * Slot: functional_impact_description Description: Description of functional impact
--     * Slot: disease_association Description: Associated disease or phenotype
--     * Slot: omim_id Description: OMIM database identifier
--     * Slot: clinical_significance Description: Clinical significance
--     * Slot: allele_frequency Description: Population allele frequency (range: 0-1)
--     * Slot: protein_id Description: UniProt accession number
--     * Slot: pdb_entry Description: PDB identifier
--     * Slot: chain_id Description: Chain identifier in the PDB structure
--     * Slot: residue_range Description: Range of residues (e.g., '1-100', '25,27,30-35')
--     * Slot: confidence_score Description: Confidence score for the annotation (range: 0-1)
--     * Slot: evidence_type Description: Type of evidence supporting this annotation
--     * Slot: evidence_code Description: Evidence and Conclusion Ontology (ECO) code
--     * Slot: source_database Description: Source database or resource that provided this annotation
--     * Slot: annotation_method Description: Computational or experimental method used
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: AggregatedProteinView_id Description: Autocreated FK slot
-- # Class: BiophysicalProperty Description: Measured or calculated biophysical properties
--     * Slot: id
--     * Slot: property_type Description: Type of biophysical property
--     * Slot: value Description: Numerical value of the property
--     * Slot: unit Description: Unit of measurement
--     * Slot: error Description: Experimental error or uncertainty
--     * Slot: experimental_method Description: Method used for measurement
--     * Slot: description
--     * Slot: AggregatedProteinView_id Description: Autocreated FK slot
-- # Class: ConformationalEnsemble Description: Ensemble of conformational states for a protein
--     * Slot: protein_id Description: UniProt accession
--     * Slot: clustering_method Description: Method used for conformational clustering
--     * Slot: rmsd_threshold Description: RMSD threshold for clustering (Angstroms)
--     * Slot: transition_pathways Description: Description of transition pathways between states
--     * Slot: energy_landscape Description: Description of the energy landscape
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
-- # Class: ConformationalState Description: Individual conformational state
--     * Slot: id
--     * Slot: state_id Description: Identifier for this state
--     * Slot: state_name Description: Descriptive name (e.g., 'open', 'closed')
--     * Slot: population Description: Relative population of this state (range: 0-1)
--     * Slot: free_energy Description: Relative free energy (kcal/mol)
--     * Slot: rmsd_from_reference Description: RMSD from reference structure
--     * Slot: description
--     * Slot: ConformationalEnsemble_id Description: Autocreated FK slot
-- # Class: PostTranslationalModification Description: Post-translational modifications observed or predicted
--     * Slot: modification_type Description: Type of PTM
--     * Slot: modified_residue Description: Residue that is modified
--     * Slot: modification_group Description: Chemical group added (e.g., 'phosphate', 'methyl')
--     * Slot: mass_shift Description: Mass change due to modification (Da)
--     * Slot: functional_effect Description: Known functional effect of this PTM
--     * Slot: regulatory_role Description: Role in regulation
--     * Slot: enzyme Description: Enzyme responsible for modification
--     * Slot: removal_enzyme Description: Enzyme that removes modification
--     * Slot: protein_id Description: UniProt accession number
--     * Slot: pdb_entry Description: PDB identifier
--     * Slot: chain_id Description: Chain identifier in the PDB structure
--     * Slot: residue_range Description: Range of residues (e.g., '1-100', '25,27,30-35')
--     * Slot: confidence_score Description: Confidence score for the annotation (range: 0-1)
--     * Slot: evidence_type Description: Type of evidence supporting this annotation
--     * Slot: evidence_code Description: Evidence and Conclusion Ontology (ECO) code
--     * Slot: source_database Description: Source database or resource that provided this annotation
--     * Slot: annotation_method Description: Computational or experimental method used
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: AggregatedProteinView_id Description: Autocreated FK slot
-- # Class: DatabaseCrossReference Description: Cross-references to external databases
--     * Slot: id
--     * Slot: database_name Description: Name of the external database
--     * Slot: database_id Description: Identifier in the external database
--     * Slot: database_url Description: URL to the database entry
--     * Slot: last_updated Description: Date of last update
--     * Slot: description
--     * Slot: AggregatedProteinView_id Description: Autocreated FK slot
-- # Class: EvolutionaryConservation Description: Evolutionary conservation information
--     * Slot: conservation_score Description: Overall conservation score (range: 0-1)
--     * Slot: conservation_method Description: Method used for conservation analysis
--     * Slot: alignment_depth Description: Number of sequences in alignment
--     * Slot: taxonomic_range Description: Taxonomic range of conservation
--     * Slot: protein_id Description: UniProt accession number
--     * Slot: pdb_entry Description: PDB identifier
--     * Slot: chain_id Description: Chain identifier in the PDB structure
--     * Slot: residue_range Description: Range of residues (e.g., '1-100', '25,27,30-35')
--     * Slot: confidence_score Description: Confidence score for the annotation (range: 0-1)
--     * Slot: evidence_type Description: Type of evidence supporting this annotation
--     * Slot: evidence_code Description: Evidence and Conclusion Ontology (ECO) code
--     * Slot: source_database Description: Source database or resource that provided this annotation
--     * Slot: annotation_method Description: Computational or experimental method used
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
-- # Class: AggregatedProteinView Description: Aggregated view of all structural and functional data for a protein
--     * Slot: uniprot_id Description: UniProt accession
--     * Slot: protein_name Description: Protein name
--     * Slot: organism Description: Source organism
--     * Slot: organism_id Description: NCBI taxonomy ID
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: conformational_ensemble_id Description: Conformational ensemble data
--     * Slot: evolutionary_conservation_id Description: Conservation analysis
-- # Class: MeasurementConditions Description: Conditions under which biophysical measurements were made
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: BiophysicalProperty_id Description: Autocreated FK slot
--     * Slot: buffer_composition_id Description: Composition of the buffer used
--     * Slot: ph_id Description: pH value of the solution during measurement (range: 0-14), typically expressed in pH units. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: ionic_strength_id Description: Ionic strength, typically specified in molar (mol/L). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: temperature_id Description: Temperature during measurement, typically specified in Kelvin. Data providers may specify alternative units by including the unit in the QuantityValue.
-- # Class: PlantSample Description: Plant sample info for AIMS-LEAF
--     * Slot: biological_replicate_sample_group_name Description: Samples that are biological replicates should have the same group name
--     * Slot: combined_tissue_description Description: The number and relationship between the tissues if multiple tissue samples were combined into a single container
--     * Slot: experimental_time_point_number Description: Integer number representing the sequential numbering of time points, applicable to samples that are part of time course experiments
--     * Slot: experimental_time_point_description Description: Description of the time point sampled, applicable to samples that are part of time course experiments
--     * Slot: genus
--     * Slot: species
--     * Slot: strain_variety_cultivar Description: Name or ID of the cultivar, variety, strain, or other similar designation of the primary organism being sampled
--     * Slot: isolate Description: Isolate or mutant name
--     * Slot: germplasm_collection_id Description: Culture collection name and ID from which the original plant germplasm was sourced
--     * Slot: ncbi_taxonomy_id Description: Unique identifier from the NCBI taxonomy database
--     * Slot: ancestral_data Description: Information about either pedigree or other description of ancestral information
--     * Slot: genetic_modification Description: Genetic modifications of the genome of an organism, which may occur naturally by spontaneous mutation, or be introduced by some experimental means
--     * Slot: ploidy Description: The ploidy level of the genome. For terms, please select terms listed under class ploidy (PATO:001374) of Phenotypic Quality Ontology
--     * Slot: reference_genome Description: Reference genome and annotation to be used for analysis
--     * Slot: collection_date_time Description: The time of sampling, either as an instance (single point in time) or interval. All valid ISO8601 formats are acceptable
--     * Slot: tissue Description: Detailed description of the organ or type of tissue sampled
--     * Slot: tissue_plant_ontology_term Description: Plant ontology term corresponding to plant structure sampled; see https://planteome.org. May include multiple terms separated by semicolons
--     * Slot: region_locality Description: The geographical origin of the sample as defined by the country or sea name followed by specific region name
--     * Slot: latitude Description: The geographical origin of the sample as defined by latitude. The value should be reported in decimal degrees, limited to 8 decimal points, and in WGS84 system
--     * Slot: longitude Description: The geographical origin of the sample as defined by longitude. The value should be reported in decimal degrees, limited to 8 decimal points, and in WGS84 system
--     * Slot: broad_scale_environmental_context Description: The major environmental system the sample or specimen came from. The system(s) identified should have a coarse spatial grain
--     * Slot: local_environmental_context Description: The entity or entities which are in the sample or specimen's local vicinity and which you believe have significant causal influences on your sample or specimen
--     * Slot: environmental_medium Description: The environmental material(s) immediately surrounding the sample or specimen at the time of sampling
--     * Slot: growth_facility Description: Type of facility where the sampled plant was grown
--     * Slot: growth_medium Description: General specification of the media for growing the plants or tissue cultured samples
--     * Slot: growth_medium_composition Description: Detailed description of the makeup of the plant growth medium
--     * Slot: plant_age Description: The age of the plant from which the tissue was sampled
--     * Slot: developmental_stage Description: The developmental stage of the plant from which the tissue was sampled
--     * Slot: arabadopsis_phenotype_stage Description: Stage that takes into account effect of genotype & environment effects. Requires in depth knowledge about features of model organism doi: 10.1105/TPC.010011
--     * Slot: air_temperature_regimen Description: Information about treatment involving an exposure to varying temperatures
--     * Slot: antibiotic_regimen Description: Information about treatment involving antibiotic administration
--     * Slot: biotic_regimen Description: Information about treatment involving use of biotic factors, such as bacteria, viruses, or fungi
--     * Slot: inoculation_method Description: Method and material used for inoculation or infiltration with a biotic agent
--     * Slot: time_post_inoculation Description: The time between inoculation with the biotic agent and sample collection, specified as days:hours:minutes
--     * Slot: chemical_administration Description: List of chemical compounds administered to the host or site where sampling occurred, and when
--     * Slot: chemical_mutagen Description: Treatment involving use of mutagens
--     * Slot: fertilizer_administration Description: Detailed description of fertilizer application
--     * Slot: insecticide_regimen Description: Information about treatment involving use of insecticides
--     * Slot: fungicide_regimen Description: Information about treatment involving use of fungicides
--     * Slot: gaseous_environment Description: Use of conditions with differing gaseous environments
--     * Slot: growth_hormone_regimen Description: Information about treatment involving use of growth hormones
--     * Slot: herbicide_regimen Description: Information about treatment involving use of herbicides
--     * Slot: humidity_regimen Description: Information about treatment involving an exposure to varying degree of humidity
--     * Slot: radiation_regimen Description: Information about treatment involving exposure of plant or a plant part to a particular radiation regimen
--     * Slot: light_regimen Description: Information about treatment involving an exposure to light, including intensity, timing, and quality
--     * Slot: last_light_transition_type Description: The most recent light transition before sampling
--     * Slot: time_after_last_light_transition Description: The time between sampling and the most recent light transition, specified as hours:minutes
--     * Slot: salt_regimen Description: Information about treatment involving use of salts as supplement to liquid and soil growth media
--     * Slot: rainfall_regimen Description: Information about treatment involving an exposure to a given amount of rainfall
--     * Slot: watering_regimen Description: Information about treatment involving an exposure to watering frequencies
--     * Slot: other_treatment_regimen Description: Use this field to provide information about treatments that are not captured accurately by any of the other available treatment categories
--     * Slot: perturbation Description: Type of perturbation, e.g. chemical administration, physical disturbance, etc., coupled with perturbation regimen
--     * Slot: mechanical_damage Description: Information about any mechanical damage exerted on the plant
--     * Slot: observed_host_symbionts Description: The taxonomic name of the organism(s) found living in mutualistic, commensalistic, or parasitic symbiosis with the specific host.
--     * Slot: plant_sex Description: Sex of the reproductive parts on the whole plant, e.g. pistillate, staminate, monoecious, hermaphrodite
--     * Slot: sample_disease_staus Description: List of diseases with which the subject has been diagnosed at the time of sample collection; can include multiple diagnoses; e.g. Late wilt (Cephalosporium maydis)
--     * Slot: sample_disease_stage Description: Stage of the disease at the time of sample collection, e.g. inoculation, penetration, infection, growth and reproduction, dissemination of pathogen
--     * Slot: sample_code Description: Human-friendly laboratory identifier or facility code for the sample (e.g., 'ALS-12.3.1-SAMPLE-001', 'LAB-PROT-2024-01'). Used for local reference and tracking within laboratory workflows.
--     * Slot: sample_type Description: Type of biological sample
--     * Slot: preparation_method Description: Method used to prepare the sample
--     * Slot: organism Description: Source organism for the sample (e.g., NCBITaxon:3702 for Arabidopsis thaliana)
--     * Slot: anatomy Description: Anatomical part or tissue (e.g., UBERON:0008945 for leaf)
--     * Slot: cell_type Description: Cell type if applicable (e.g., CL:0000057 for fibroblast)
--     * Slot: parent_sample_id Description: Reference to parent sample for derivation tracking
--     * Slot: quality_metrics Description: Quality control metrics for the sample
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: estimated_genome_size_mb_id Description: Estimated genome size of the primary species being sampled, between 1-100000
--     * Slot: gc_content_percent_id Description: Estimated GC content of the genome of the primary species being sampled, numeric only
--     * Slot: sample_size_id Description: The total amount or size (volume (ml), mass (g) or area (m2)) of sample collected. Separate the number and unit by a single space
--     * Slot: depth_meters_id Description: The vertical distance (in meters) below local surface
--     * Slot: elevation_meters_id Description: Elevation (in meters) of the sampling site as measured by the vertical distance from mean sea level
--     * Slot: temperature_id Description: Temperature (in degrees Celsius) of the sample at time of sampling
--     * Slot: molecular_weight_id Description: Molecular weight, typically specified in kilodaltons (kDa). Data providers may specify alternative units (e.g., Daltons, g/mol) by including the unit in the QuantityValue.
--     * Slot: concentration_id Description: Sample concentration, typically specified in mg/mL or µM. Data providers may specify alternative units (e.g., molar, g/L) by including the unit in the QuantityValue.
--     * Slot: buffer_composition_id Description: Buffer composition including pH, salts, additives
--     * Slot: storage_conditions_id Description: Storage conditions for the sample
--     * Slot: purity_percentage_id Description: Sample purity, typically specified as a percentage (range: 0-100). Data providers may specify as decimal fraction by including the unit in the QuantityValue.
-- # Class: PlantSamplePreparation Description: A process that prepares a plant sample for analysis
--     * Slot: sample_material_processing Description: A brief description of any processing applied to the sample during or after retrieving the sample from environment, or a link to the relevant protocol(s) performed.
--     * Slot: sample_preservation_method Description: The method employed for preserving or fixing the tissue. Use Fresh if the sample was harvested immdiately before processing. Select from the following options: [Formaldehyde, N2 Freeze, FFPE, Fresh]
--     * Slot: embedding_material Description: Material used to stabilize for sectioning, e.g. OCT, parafin wax
--     * Slot: plane_of_section Description: plane of section: cross section / transverse section, longitudinal section, radial longitudinal section, tangental longitudinal section
--     * Slot: support_type Description: type of support for sample sections (quartz, lexan, thermonox, Ge, MgF2....)
--     * Slot: adhesive Description: Adhesive type (glue for sections if used, tape adhesives, gel
--     * Slot: top_layer Description: type of film for top layer, if present (mylar, polyproylene, none....)
--     * Slot: preparation_type Description: Type of sample preparation
--     * Slot: sample_id Description: Reference to the sample being prepared
--     * Slot: preparation_date Description: Date of sample preparation
--     * Slot: operator_id Description: Identifier or name of the person who performed the sample preparation (e.g., 'jsmith', 'John Smith', or personnel ID)
--     * Slot: protocol_description Description: Detailed protocol description
--     * Slot: host_strain_or_cell_line Description: Specific strain or cell line used (e.g., BL21(DE3), Sf9, HEK293F)
--     * Slot: medium Description: Growth medium used
--     * Slot: antibiotic_selection Description: Antibiotic or selection agent used
--     * Slot: induction_agent Description: Agent used to induce expression (e.g., IPTG, tetracycline)
--     * Slot: inducer_concentration Description: Concentration of induction agent
--     * Slot: harvest_timepoint Description: Time point when cells were harvested
--     * Slot: lysis_method Description: Method used for cell lysis
--     * Slot: protease_inhibitors Description: Protease inhibitors added
--     * Slot: affinity_type Description: Type of affinity chromatography
--     * Slot: affinity_column Description: Affinity column specifications
--     * Slot: lysis_buffer Description: Buffer composition for lysis
--     * Slot: wash_buffer Description: Buffer composition for washing
--     * Slot: elution_buffer Description: Buffer composition for elution
--     * Slot: tag_removal Description: Whether and how affinity tag was removed
--     * Slot: protease Description: Protease used for tag cleavage
--     * Slot: protease_ratio Description: Ratio of protease to protein
--     * Slot: second_affinity_reverse Description: Second affinity or reverse affinity step
--     * Slot: iex_column Description: Ion-exchange column used
--     * Slot: hic_column Description: Hydrophobic interaction column used
--     * Slot: sec_column Description: Size-exclusion column used
--     * Slot: sec_buffer Description: Buffer for size-exclusion chromatography
--     * Slot: concentration_method Description: Method used to concentrate protein
--     * Slot: final_buffer Description: Final buffer composition after purification
--     * Slot: aggregation_assessment Description: Assessment of protein aggregation state
--     * Slot: aliquoting Description: How the protein was aliquoted for storage
--     * Slot: id Description: Globally unique identifier as an IRI or CURIE for machine processing and external references. Used for linking data across systems and semantic web integration.
--     * Slot: title Description: A human-readable name or title for this entity
--     * Slot: description Description: A detailed textual description of this entity
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: sample_storage_temperature_id Description: Temperature at which sample was stored (in degrees Celsius)
--     * Slot: harvest_to_preservation_time_id Description: The time between sampling and sample preservation, minutes
--     * Slot: section_thickness_id Description: Thickness of sample section
--     * Slot: support_thickness_id Description: Thickness of support layer
--     * Slot: top_layer_thickness_id Description: Thickness of top layer
--     * Slot: culture_volume_l_id Description: Culture volume, typically specified in liters (L). Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: growth_temperature_c_id Description: Growth temperature, typically specified in degrees Celsius. Data providers may specify alternative units (e.g., Kelvin) by including the unit in the QuantityValue.
--     * Slot: induction_temperature_c_id Description: Temperature during induction, typically specified in degrees Celsius. Data providers may specify alternative units by including the unit in the QuantityValue.
--     * Slot: induction_time_h_id Description: Duration of induction, typically specified in hours. Data providers may specify alternative units (e.g., minutes, seconds) by including the unit in the QuantityValue.
--     * Slot: od600_at_induction_id Description: Optical density at 600nm when induction was started. Data providers may include unit information in the QuantityValue if needed.
--     * Slot: cleavage_time_h_id Description: Duration of protease cleavage in hours
--     * Slot: cleavage_temperature_c_id Description: Temperature during cleavage in Celsius
--     * Slot: final_concentration_mg_per_ml_id Description: Final protein concentration in mg/mL
--     * Slot: yield_mg_id Description: Total yield in milligrams
--     * Slot: purity_by_sds_page_percent_id Description: Purity percentage by SDS-PAGE
-- # Class: Dataset_keywords
--     * Slot: Dataset_id Description: Autocreated FK slot
--     * Slot: keywords Description: Keywords or tags describing the dataset for search and categorization
-- # Class: Study_keywords
--     * Slot: Study_id Description: Autocreated FK slot
--     * Slot: keywords Description: Keywords or tags describing the study for search and categorization
-- # Class: FTIRImage_molecular_signatures
--     * Slot: FTIRImage_id Description: Autocreated FK slot
--     * Slot: molecular_signatures Description: Identified molecular signatures or peaks
-- # Class: OpticalImage_color_channels
--     * Slot: OpticalImage_id Description: Autocreated FK slot
--     * Slot: color_channels Description: Color channels present (e.g., RGB, grayscale)
-- # Class: XRFImage_elements_measured
--     * Slot: XRFImage_id Description: Autocreated FK slot
--     * Slot: elements_measured Description: Elements detected and measured
-- # Class: BufferComposition_components
--     * Slot: BufferComposition_id Description: Autocreated FK slot
--     * Slot: components Description: Buffer components and their concentrations
-- # Class: BufferComposition_additives
--     * Slot: BufferComposition_id Description: Autocreated FK slot
--     * Slot: additives Description: Additional additives in the buffer
-- # Class: ProteinAnnotation_publication_ids
--     * Slot: ProteinAnnotation_id Description: Autocreated FK slot
--     * Slot: publication_ids Description: IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.
-- # Class: FunctionalSite_residues
--     * Slot: FunctionalSite_id Description: Autocreated FK slot
--     * Slot: residues Description: List of residues forming the functional site. Each should be specified as a string (e.g., "45", "120A").
-- # Class: FunctionalSite_go_terms
--     * Slot: FunctionalSite_id Description: Autocreated FK slot
--     * Slot: go_terms Description: Associated Gene Ontology terms
-- # Class: FunctionalSite_publication_ids
--     * Slot: FunctionalSite_id Description: Autocreated FK slot
--     * Slot: publication_ids Description: IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.
-- # Class: StructuralFeature_publication_ids
--     * Slot: StructuralFeature_id Description: Autocreated FK slot
--     * Slot: publication_ids Description: IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.
-- # Class: LigandInteraction_binding_site_residues
--     * Slot: LigandInteraction_id Description: Autocreated FK slot
--     * Slot: binding_site_residues Description: Residues involved in ligand binding
-- # Class: ProteinProteinInteraction_interface_residues
--     * Slot: ProteinProteinInteraction_id Description: Autocreated FK slot
--     * Slot: interface_residues Description: Residues at the interaction interface
-- # Class: ProteinProteinInteraction_partner_interface_residues
--     * Slot: ProteinProteinInteraction_id Description: Autocreated FK slot
--     * Slot: partner_interface_residues Description: Partner residues at the interaction interface
-- # Class: ProteinProteinInteraction_interaction_evidence
--     * Slot: ProteinProteinInteraction_id Description: Autocreated FK slot
--     * Slot: interaction_evidence Description: Evidence for this interaction
-- # Class: ProteinProteinInteraction_publication_ids
--     * Slot: ProteinProteinInteraction_id Description: Autocreated FK slot
--     * Slot: publication_ids Description: IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.
-- # Class: MutationEffect_publication_ids
--     * Slot: MutationEffect_id Description: Autocreated FK slot
--     * Slot: publication_ids Description: IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.
-- # Class: ConformationalEnsemble_principal_motions
--     * Slot: ConformationalEnsemble_id Description: Autocreated FK slot
--     * Slot: principal_motions Description: Description of principal motions
-- # Class: ConformationalState_pdb_entries
--     * Slot: ConformationalState_id Description: Autocreated FK slot
--     * Slot: pdb_entries Description: PDB entries representing this state
-- # Class: ConformationalState_characteristic_features
--     * Slot: ConformationalState_id Description: Autocreated FK slot
--     * Slot: characteristic_features Description: Key features of this conformation
-- # Class: PostTranslationalModification_publication_ids
--     * Slot: PostTranslationalModification_id Description: Autocreated FK slot
--     * Slot: publication_ids Description: IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.
-- # Class: EvolutionaryConservation_conserved_residues
--     * Slot: EvolutionaryConservation_id Description: Autocreated FK slot
--     * Slot: conserved_residues Description: Highly conserved residues
-- # Class: EvolutionaryConservation_variable_residues
--     * Slot: EvolutionaryConservation_id Description: Autocreated FK slot
--     * Slot: variable_residues Description: Highly variable residues
-- # Class: EvolutionaryConservation_coevolved_residues
--     * Slot: EvolutionaryConservation_id Description: Autocreated FK slot
--     * Slot: coevolved_residues Description: Pairs of coevolved residues
-- # Class: EvolutionaryConservation_publication_ids
--     * Slot: EvolutionaryConservation_id Description: Autocreated FK slot
--     * Slot: publication_ids Description: IDs of one or more publications supporting this annotation. Use PubMed IDs in the format 'PMID:XXXXXXX' or DOIs with 'DOI:' prefix.
-- # Class: AggregatedProteinView_pdb_entries
--     * Slot: AggregatedProteinView_id Description: Autocreated FK slot
--     * Slot: pdb_entries Description: All PDB entries for this protein

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_NamedThing_id" ON "NamedThing" (id);
CREATE TABLE "AttributeGroup" (
	id INTEGER NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_AttributeGroup_id" ON "AttributeGroup" (id);
CREATE TABLE "Dataset" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Dataset_id" ON "Dataset" (id);
CREATE TABLE "ImageFeature" (
	id INTEGER NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ImageFeature_id" ON "ImageFeature" (id);
CREATE TABLE "TechniqueSpecificPreparation" (
	id INTEGER NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_TechniqueSpecificPreparation_id" ON "TechniqueSpecificPreparation" (id);
CREATE TABLE "Any" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);CREATE INDEX "ix_Any_id" ON "Any" (id);
CREATE TABLE "Attribute" (
	uid INTEGER NOT NULL,
	id TEXT,
	label TEXT NOT NULL,
	PRIMARY KEY (uid)
);CREATE INDEX "ix_Attribute_uid" ON "Attribute" (uid);
CREATE TABLE "ProteinAnnotation" (
	protein_id TEXT NOT NULL,
	pdb_entry TEXT,
	chain_id TEXT,
	residue_range TEXT,
	confidence_score FLOAT,
	evidence_type VARCHAR(17),
	evidence_code TEXT,
	source_database VARCHAR(12),
	annotation_method TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ProteinAnnotation_id" ON "ProteinAnnotation" (id);
CREATE TABLE "ConformationalEnsemble" (
	protein_id TEXT NOT NULL,
	clustering_method TEXT,
	rmsd_threshold FLOAT,
	transition_pathways TEXT,
	energy_landscape TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_ConformationalEnsemble_id" ON "ConformationalEnsemble" (id);
CREATE TABLE "EvolutionaryConservation" (
	conservation_score FLOAT,
	conservation_method TEXT,
	alignment_depth INTEGER,
	taxonomic_range TEXT,
	protein_id TEXT NOT NULL,
	pdb_entry TEXT,
	chain_id TEXT,
	residue_range TEXT,
	confidence_score FLOAT,
	evidence_type VARCHAR(17),
	evidence_code TEXT,
	source_database VARCHAR(12),
	annotation_method TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);CREATE INDEX "ix_EvolutionaryConservation_id" ON "EvolutionaryConservation" (id);
CREATE TABLE "Study" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_Study_id" ON "Study" (id);
CREATE TABLE "Instrument" (
	instrument_code TEXT NOT NULL,
	instrument_category VARCHAR(20),
	facility_name VARCHAR(22),
	facility_ror TEXT,
	beamline_id TEXT,
	manufacturer TEXT,
	model TEXT,
	installation_date DATE,
	current_status VARCHAR(13),
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_Instrument_id" ON "Instrument" (id);
CREATE TABLE "OntologyTerm" (
	label TEXT,
	definition TEXT,
	ontology TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"ImageFeature_id" INTEGER,
	"OntologyTerm_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ImageFeature_id") REFERENCES "ImageFeature" (id),
	FOREIGN KEY("OntologyTerm_id") REFERENCES "OntologyTerm" (id)
);CREATE INDEX "ix_OntologyTerm_id" ON "OntologyTerm" (id);
CREATE TABLE "AttributeValue" (
	id INTEGER NOT NULL,
	raw_value TEXT,
	attribute_uid INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(attribute_uid) REFERENCES "Attribute" (uid)
);CREATE INDEX "ix_AttributeValue_id" ON "AttributeValue" (id);
CREATE TABLE "QuantityValue" (
	id INTEGER NOT NULL,
	maximum_numeric_value FLOAT,
	minimum_numeric_value FLOAT,
	numeric_value FLOAT,
	unit TEXT NOT NULL,
	unit_cv_id TEXT,
	raw_value TEXT,
	attribute_uid INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(attribute_uid) REFERENCES "Attribute" (uid)
);CREATE INDEX "ix_QuantityValue_id" ON "QuantityValue" (id);
CREATE TABLE "TextValue" (
	id INTEGER NOT NULL,
	value TEXT NOT NULL,
	value_cv_id TEXT,
	raw_value TEXT,
	attribute_uid INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(attribute_uid) REFERENCES "Attribute" (uid)
);CREATE INDEX "ix_TextValue_id" ON "TextValue" (id);
CREATE TABLE "DateTimeValue" (
	id INTEGER NOT NULL,
	value TEXT NOT NULL,
	raw_value TEXT,
	attribute_uid INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(attribute_uid) REFERENCES "Attribute" (uid)
);CREATE INDEX "ix_DateTimeValue_id" ON "DateTimeValue" (id);
CREATE TABLE "ConformationalState" (
	id INTEGER NOT NULL,
	state_id TEXT NOT NULL,
	state_name TEXT,
	population FLOAT,
	free_energy FLOAT,
	rmsd_from_reference FLOAT,
	description TEXT,
	"ConformationalEnsemble_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("ConformationalEnsemble_id") REFERENCES "ConformationalEnsemble" (id)
);CREATE INDEX "ix_ConformationalState_id" ON "ConformationalState" (id);
CREATE TABLE "AggregatedProteinView" (
	uniprot_id TEXT NOT NULL,
	protein_name TEXT NOT NULL,
	organism TEXT,
	organism_id INTEGER,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	conformational_ensemble_id TEXT,
	evolutionary_conservation_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(conformational_ensemble_id) REFERENCES "ConformationalEnsemble" (id),
	FOREIGN KEY(evolutionary_conservation_id) REFERENCES "EvolutionaryConservation" (id)
);CREATE INDEX "ix_AggregatedProteinView_id" ON "AggregatedProteinView" (id);
CREATE TABLE "Dataset_keywords" (
	"Dataset_id" TEXT,
	keywords TEXT,
	PRIMARY KEY ("Dataset_id", keywords),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_Dataset_keywords_keywords" ON "Dataset_keywords" (keywords);CREATE INDEX "ix_Dataset_keywords_Dataset_id" ON "Dataset_keywords" ("Dataset_id");
CREATE TABLE "ProteinAnnotation_publication_ids" (
	"ProteinAnnotation_id" TEXT,
	publication_ids TEXT,
	PRIMARY KEY ("ProteinAnnotation_id", publication_ids),
	FOREIGN KEY("ProteinAnnotation_id") REFERENCES "ProteinAnnotation" (id)
);CREATE INDEX "ix_ProteinAnnotation_publication_ids_publication_ids" ON "ProteinAnnotation_publication_ids" (publication_ids);CREATE INDEX "ix_ProteinAnnotation_publication_ids_ProteinAnnotation_id" ON "ProteinAnnotation_publication_ids" ("ProteinAnnotation_id");
CREATE TABLE "ConformationalEnsemble_principal_motions" (
	"ConformationalEnsemble_id" TEXT,
	principal_motions TEXT,
	PRIMARY KEY ("ConformationalEnsemble_id", principal_motions),
	FOREIGN KEY("ConformationalEnsemble_id") REFERENCES "ConformationalEnsemble" (id)
);CREATE INDEX "ix_ConformationalEnsemble_principal_motions_principal_motions" ON "ConformationalEnsemble_principal_motions" (principal_motions);CREATE INDEX "ix_ConformationalEnsemble_principal_motions_ConformationalEnsemble_id" ON "ConformationalEnsemble_principal_motions" ("ConformationalEnsemble_id");
CREATE TABLE "EvolutionaryConservation_conserved_residues" (
	"EvolutionaryConservation_id" TEXT,
	conserved_residues TEXT,
	PRIMARY KEY ("EvolutionaryConservation_id", conserved_residues),
	FOREIGN KEY("EvolutionaryConservation_id") REFERENCES "EvolutionaryConservation" (id)
);CREATE INDEX "ix_EvolutionaryConservation_conserved_residues_conserved_residues" ON "EvolutionaryConservation_conserved_residues" (conserved_residues);CREATE INDEX "ix_EvolutionaryConservation_conserved_residues_EvolutionaryConservation_id" ON "EvolutionaryConservation_conserved_residues" ("EvolutionaryConservation_id");
CREATE TABLE "EvolutionaryConservation_variable_residues" (
	"EvolutionaryConservation_id" TEXT,
	variable_residues TEXT,
	PRIMARY KEY ("EvolutionaryConservation_id", variable_residues),
	FOREIGN KEY("EvolutionaryConservation_id") REFERENCES "EvolutionaryConservation" (id)
);CREATE INDEX "ix_EvolutionaryConservation_variable_residues_variable_residues" ON "EvolutionaryConservation_variable_residues" (variable_residues);CREATE INDEX "ix_EvolutionaryConservation_variable_residues_EvolutionaryConservation_id" ON "EvolutionaryConservation_variable_residues" ("EvolutionaryConservation_id");
CREATE TABLE "EvolutionaryConservation_coevolved_residues" (
	"EvolutionaryConservation_id" TEXT,
	coevolved_residues TEXT,
	PRIMARY KEY ("EvolutionaryConservation_id", coevolved_residues),
	FOREIGN KEY("EvolutionaryConservation_id") REFERENCES "EvolutionaryConservation" (id)
);CREATE INDEX "ix_EvolutionaryConservation_coevolved_residues_coevolved_residues" ON "EvolutionaryConservation_coevolved_residues" (coevolved_residues);CREATE INDEX "ix_EvolutionaryConservation_coevolved_residues_EvolutionaryConservation_id" ON "EvolutionaryConservation_coevolved_residues" ("EvolutionaryConservation_id");
CREATE TABLE "EvolutionaryConservation_publication_ids" (
	"EvolutionaryConservation_id" TEXT,
	publication_ids TEXT,
	PRIMARY KEY ("EvolutionaryConservation_id", publication_ids),
	FOREIGN KEY("EvolutionaryConservation_id") REFERENCES "EvolutionaryConservation" (id)
);CREATE INDEX "ix_EvolutionaryConservation_publication_ids_publication_ids" ON "EvolutionaryConservation_publication_ids" (publication_ids);CREATE INDEX "ix_EvolutionaryConservation_publication_ids_EvolutionaryConservation_id" ON "EvolutionaryConservation_publication_ids" ("EvolutionaryConservation_id");
CREATE TABLE "SamplePreparation" (
	preparation_type VARCHAR(20) NOT NULL,
	sample_id TEXT,
	preparation_date DATE,
	operator_id TEXT,
	protocol_description TEXT,
	host_strain_or_cell_line TEXT,
	medium TEXT,
	antibiotic_selection TEXT,
	induction_agent TEXT,
	inducer_concentration TEXT,
	harvest_timepoint TEXT,
	lysis_method TEXT,
	protease_inhibitors TEXT,
	affinity_type TEXT,
	affinity_column TEXT,
	lysis_buffer TEXT,
	wash_buffer TEXT,
	elution_buffer TEXT,
	tag_removal BOOLEAN,
	protease TEXT,
	protease_ratio TEXT,
	second_affinity_reverse TEXT,
	iex_column TEXT,
	hic_column TEXT,
	sec_column TEXT,
	sec_buffer TEXT,
	concentration_method TEXT,
	final_buffer TEXT,
	aggregation_assessment TEXT,
	aliquoting TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Dataset_id" TEXT,
	culture_volume_l_id INTEGER,
	growth_temperature_c_id INTEGER,
	induction_temperature_c_id INTEGER,
	induction_time_h_id INTEGER,
	od600_at_induction_id INTEGER,
	cleavage_time_h_id INTEGER,
	cleavage_temperature_c_id INTEGER,
	final_concentration_mg_per_ml_id INTEGER,
	yield_mg_id INTEGER,
	purity_by_sds_page_percent_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(culture_volume_l_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(growth_temperature_c_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(induction_temperature_c_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(induction_time_h_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(od600_at_induction_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(cleavage_time_h_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(cleavage_temperature_c_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(final_concentration_mg_per_ml_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(yield_mg_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(purity_by_sds_page_percent_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_SamplePreparation_id" ON "SamplePreparation" (id);
CREATE TABLE "CryoEMInstrument" (
	cs_corrector BOOLEAN,
	phase_plate BOOLEAN,
	detector_technology VARCHAR(24),
	detector_manufacturer TEXT,
	detector_model TEXT,
	detector_mode VARCHAR(26),
	detector_position TEXT,
	detector_dimensions TEXT,
	phase_plate_type TEXT,
	energy_filter_present BOOLEAN,
	energy_filter_make TEXT,
	energy_filter_model TEXT,
	microscope_software TEXT,
	microscope_software_version TEXT,
	imaging_mode VARCHAR(5),
	instrument_code TEXT NOT NULL,
	instrument_category VARCHAR(20),
	facility_name VARCHAR(22),
	facility_ror TEXT,
	beamline_id TEXT,
	manufacturer TEXT,
	model TEXT,
	installation_date DATE,
	current_status VARCHAR(13),
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	accelerating_voltage_id INTEGER,
	pixel_size_physical_um_id INTEGER,
	autoloader_capacity_id INTEGER,
	cs_id INTEGER,
	c2_aperture_id INTEGER,
	objective_aperture_id INTEGER,
	energy_filter_slit_width_id INTEGER,
	pixel_size_physical_id INTEGER,
	spotsize_id INTEGER,
	gunlens_id INTEGER,
	tem_beam_diameter_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(accelerating_voltage_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(pixel_size_physical_um_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(autoloader_capacity_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(cs_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(c2_aperture_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(objective_aperture_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(energy_filter_slit_width_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(pixel_size_physical_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(spotsize_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(gunlens_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(tem_beam_diameter_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_CryoEMInstrument_id" ON "CryoEMInstrument" (id);
CREATE TABLE "XRayInstrument" (
	source_type VARCHAR(14),
	detector_technology VARCHAR(24),
	detector_manufacturer TEXT,
	detector_model TEXT,
	monochromator_type TEXT,
	goniometer_type TEXT,
	crystal_cooling_capability BOOLEAN,
	instrument_code TEXT NOT NULL,
	instrument_category VARCHAR(20),
	facility_name VARCHAR(22),
	facility_ror TEXT,
	beamline_id TEXT,
	manufacturer TEXT,
	model TEXT,
	installation_date DATE,
	current_status VARCHAR(13),
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	energy_min_id INTEGER,
	energy_max_id INTEGER,
	beam_size_min_id INTEGER,
	beam_size_max_id INTEGER,
	flux_density_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(energy_min_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(energy_max_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(beam_size_min_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(beam_size_max_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(flux_density_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_XRayInstrument_id" ON "XRayInstrument" (id);
CREATE TABLE "WorkflowRun" (
	workflow_code TEXT NOT NULL,
	workflow_type VARCHAR(23) NOT NULL,
	software_name TEXT NOT NULL,
	software_version TEXT,
	additional_software TEXT,
	processing_parameters TEXT,
	parameters_file_path TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Dataset_id" TEXT,
	processing_level_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(processing_level_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_WorkflowRun_id" ON "WorkflowRun" (id);
CREATE TABLE "DataFile" (
	file_name TEXT NOT NULL,
	file_path TEXT,
	file_format VARCHAR(10) NOT NULL,
	checksum TEXT,
	creation_date DATE,
	data_type VARCHAR(20),
	storage_uri TEXT,
	related_entity TEXT,
	file_role TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Dataset_id" TEXT,
	file_size_bytes_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(file_size_bytes_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_DataFile_id" ON "DataFile" (id);
CREATE TABLE "Image" (
	file_name TEXT NOT NULL,
	acquisition_date DATE,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Dataset_id" TEXT,
	pixel_size_id INTEGER,
	dimensions_x_id INTEGER,
	dimensions_y_id INTEGER,
	exposure_time_id INTEGER,
	dose_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dimensions_x_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dimensions_y_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dose_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_Image_id" ON "Image" (id);
CREATE TABLE "Image2D" (
	file_name TEXT NOT NULL,
	acquisition_date DATE,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	defocus_id INTEGER,
	astigmatism_id INTEGER,
	pixel_size_id INTEGER,
	dimensions_x_id INTEGER,
	dimensions_y_id INTEGER,
	exposure_time_id INTEGER,
	dose_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(defocus_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(astigmatism_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dimensions_x_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dimensions_y_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dose_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_Image2D_id" ON "Image2D" (id);
CREATE TABLE "Image3D" (
	reconstruction_method TEXT,
	file_name TEXT NOT NULL,
	acquisition_date DATE,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	dimensions_z_id INTEGER,
	voxel_size_id INTEGER,
	pixel_size_id INTEGER,
	dimensions_x_id INTEGER,
	dimensions_y_id INTEGER,
	exposure_time_id INTEGER,
	dose_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(dimensions_z_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(voxel_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dimensions_x_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dimensions_y_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dose_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_Image3D_id" ON "Image3D" (id);
CREATE TABLE "Movie" (
	super_resolution BOOLEAN,
	timestamp TEXT,
	grid_square_id TEXT,
	hole_id TEXT,
	acquisition_group TEXT,
	file_name TEXT NOT NULL,
	acquisition_date DATE,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	frames_id INTEGER,
	pixel_size_unbinned_id INTEGER,
	stage_position_x_id INTEGER,
	stage_position_y_id INTEGER,
	stage_position_z_id INTEGER,
	nominal_defocus_id INTEGER,
	dose_per_frame_id INTEGER,
	beam_shift_x_id INTEGER,
	beam_shift_y_id INTEGER,
	ice_thickness_estimate_id INTEGER,
	defocus_id INTEGER,
	astigmatism_id INTEGER,
	pixel_size_id INTEGER,
	dimensions_x_id INTEGER,
	dimensions_y_id INTEGER,
	exposure_time_id INTEGER,
	dose_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(frames_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(pixel_size_unbinned_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(stage_position_x_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(stage_position_y_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(stage_position_z_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(nominal_defocus_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dose_per_frame_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(beam_shift_x_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(beam_shift_y_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(ice_thickness_estimate_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(defocus_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(astigmatism_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dimensions_x_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dimensions_y_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dose_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_Movie_id" ON "Movie" (id);
CREATE TABLE "FTIRImage" (
	apodization_function TEXT,
	background_correction TEXT,
	file_name TEXT NOT NULL,
	file_path TEXT,
	file_format VARCHAR(10) NOT NULL,
	checksum TEXT,
	creation_date DATE,
	data_type VARCHAR(20),
	storage_uri TEXT,
	related_entity TEXT,
	file_role TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	pixel_size_id INTEGER,
	dimensions_x_id INTEGER,
	dimensions_y_id INTEGER,
	wavenumber_min_id INTEGER,
	wavenumber_max_id INTEGER,
	spectral_resolution_id INTEGER,
	number_of_scans_id INTEGER,
	file_size_bytes_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dimensions_x_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dimensions_y_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(wavenumber_min_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(wavenumber_max_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(spectral_resolution_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(number_of_scans_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(file_size_bytes_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_FTIRImage_id" ON "FTIRImage" (id);
CREATE TABLE "FluorescenceImage" (
	excitation_filter TEXT,
	emission_filter TEXT,
	fluorophore TEXT,
	channel_name TEXT,
	file_name TEXT NOT NULL,
	acquisition_date DATE,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	excitation_wavelength_id INTEGER,
	emission_wavelength_id INTEGER,
	laser_power_id INTEGER,
	pinhole_size_id INTEGER,
	quantum_yield_id INTEGER,
	defocus_id INTEGER,
	astigmatism_id INTEGER,
	pixel_size_id INTEGER,
	dimensions_x_id INTEGER,
	dimensions_y_id INTEGER,
	exposure_time_id INTEGER,
	dose_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(excitation_wavelength_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(emission_wavelength_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(laser_power_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(pinhole_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(quantum_yield_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(defocus_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(astigmatism_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dimensions_x_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dimensions_y_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dose_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_FluorescenceImage_id" ON "FluorescenceImage" (id);
CREATE TABLE "OpticalImage" (
	illumination_type VARCHAR(14),
	white_balance TEXT,
	contrast_method TEXT,
	file_name TEXT NOT NULL,
	acquisition_date DATE,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	magnification_id INTEGER,
	numerical_aperture_id INTEGER,
	defocus_id INTEGER,
	astigmatism_id INTEGER,
	pixel_size_id INTEGER,
	dimensions_x_id INTEGER,
	dimensions_y_id INTEGER,
	exposure_time_id INTEGER,
	dose_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(magnification_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(numerical_aperture_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(defocus_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(astigmatism_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dimensions_x_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dimensions_y_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dose_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_OpticalImage_id" ON "OpticalImage" (id);
CREATE TABLE "XRFImage" (
	source_type VARCHAR(14),
	detector_technology VARCHAR(24),
	detector_model TEXT,
	calibration_standard TEXT,
	file_name TEXT NOT NULL,
	file_path TEXT,
	file_format VARCHAR(10) NOT NULL,
	checksum TEXT,
	creation_date DATE,
	data_type VARCHAR(20),
	storage_uri TEXT,
	related_entity TEXT,
	file_role TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	pixel_size_id INTEGER,
	dimensions_x_id INTEGER,
	dimensions_y_id INTEGER,
	beam_energy_id INTEGER,
	beam_size_id INTEGER,
	dwell_time_id INTEGER,
	flux_id INTEGER,
	file_size_bytes_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dimensions_x_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dimensions_y_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(beam_energy_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(beam_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dwell_time_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(flux_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(file_size_bytes_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_XRFImage_id" ON "XRFImage" (id);
CREATE TABLE "BufferComposition" (
	id INTEGER NOT NULL,
	description TEXT,
	ph_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(ph_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_BufferComposition_id" ON "BufferComposition" (id);
CREATE TABLE "StorageConditions" (
	id INTEGER NOT NULL,
	duration TEXT,
	atmosphere TEXT,
	description TEXT,
	temperature_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(temperature_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_StorageConditions_id" ON "StorageConditions" (id);
CREATE TABLE "CryoEMPreparation" (
	id INTEGER NOT NULL,
	grid_type VARCHAR(16),
	support_film TEXT,
	vitrification_method VARCHAR(22),
	grid_material VARCHAR(15),
	glow_discharge_applied BOOLEAN,
	glow_discharge_atmosphere TEXT,
	vitrification_instrument TEXT,
	plasma_treatment TEXT,
	description TEXT,
	hole_size_id INTEGER,
	blot_time_id INTEGER,
	blot_force_id INTEGER,
	humidity_percentage_id INTEGER,
	chamber_temperature_id INTEGER,
	glow_discharge_time_id INTEGER,
	glow_discharge_current_id INTEGER,
	glow_discharge_pressure_id INTEGER,
	blot_number_id INTEGER,
	wait_time_id INTEGER,
	blotter_height_id INTEGER,
	blotter_setting_id INTEGER,
	sample_applied_volume_id INTEGER,
	ethane_temperature_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(hole_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(blot_time_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(blot_force_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(humidity_percentage_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(chamber_temperature_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(glow_discharge_time_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(glow_discharge_current_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(glow_discharge_pressure_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(blot_number_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(wait_time_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(blotter_height_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(blotter_setting_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(sample_applied_volume_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(ethane_temperature_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_CryoEMPreparation_id" ON "CryoEMPreparation" (id);
CREATE TABLE "XRayPreparation" (
	id INTEGER NOT NULL,
	protein_buffer TEXT,
	additives TEXT,
	crystallization_method VARCHAR(24),
	screen_name TEXT,
	drop_ratio_protein_to_reservoir TEXT,
	seeding_type TEXT,
	seed_stock_dilution TEXT,
	initial_hit_condition TEXT,
	optimization_strategy TEXT,
	optimized_condition TEXT,
	crystal_size_um TEXT,
	cryoprotectant TEXT,
	soak_compound TEXT,
	soak_conditions TEXT,
	mounting_method TEXT,
	flash_cooling_method TEXT,
	crystal_notes TEXT,
	description TEXT,
	protein_concentration_mg_per_ml_id INTEGER,
	temperature_c_id INTEGER,
	drop_volume_nl_id INTEGER,
	reservoir_volume_ul_id INTEGER,
	cryoprotectant_concentration_id INTEGER,
	loop_size_id INTEGER,
	mounting_temperature_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(protein_concentration_mg_per_ml_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(temperature_c_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(drop_volume_nl_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(reservoir_volume_ul_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(cryoprotectant_concentration_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(loop_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(mounting_temperature_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_XRayPreparation_id" ON "XRayPreparation" (id);
CREATE TABLE "ExperimentalConditions" (
	id INTEGER NOT NULL,
	atmosphere TEXT,
	description TEXT,
	temperature_id INTEGER,
	humidity_id INTEGER,
	pressure_id INTEGER,
	beam_energy_id INTEGER,
	exposure_time_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(temperature_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(humidity_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(pressure_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(beam_energy_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_ExperimentalConditions_id" ON "ExperimentalConditions" (id);
CREATE TABLE "DataCollectionStrategy" (
	id INTEGER NOT NULL,
	collection_mode VARCHAR(16),
	detector_mode VARCHAR(26),
	attenuator TEXT,
	strategy_notes TEXT,
	description TEXT,
	total_frames_id INTEGER,
	frame_rate_id INTEGER,
	total_dose_id INTEGER,
	dose_per_frame_id INTEGER,
	wavelength_a_id INTEGER,
	pixel_size_calibrated_id INTEGER,
	detector_distance_mm_id INTEGER,
	beam_center_x_px_id INTEGER,
	beam_center_y_px_id INTEGER,
	beam_size_um_id INTEGER,
	flux_photons_per_s_id INTEGER,
	transmission_percent_id INTEGER,
	temperature_k_id INTEGER,
	oscillation_per_image_deg_id INTEGER,
	total_rotation_deg_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(total_frames_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(frame_rate_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(total_dose_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dose_per_frame_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(wavelength_a_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(pixel_size_calibrated_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(detector_distance_mm_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(beam_center_x_px_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(beam_center_y_px_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(beam_size_um_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(flux_photons_per_s_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(transmission_percent_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(temperature_k_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(oscillation_per_image_deg_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(total_rotation_deg_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_DataCollectionStrategy_id" ON "DataCollectionStrategy" (id);
CREATE TABLE "QualityMetrics" (
	id INTEGER NOT NULL,
	space_group TEXT,
	anomalous_used BOOLEAN,
	description TEXT,
	resolution_id INTEGER,
	resolution_high_shell_a_id INTEGER,
	resolution_low_a_id INTEGER,
	completeness_id INTEGER,
	completeness_high_res_shell_percent_id INTEGER,
	signal_to_noise_id INTEGER,
	mean_i_over_sigma_i_id INTEGER,
	unit_cell_a_id INTEGER,
	unit_cell_b_id INTEGER,
	unit_cell_c_id INTEGER,
	unit_cell_alpha_id INTEGER,
	unit_cell_beta_id INTEGER,
	unit_cell_gamma_id INTEGER,
	multiplicity_id INTEGER,
	cc_half_id INTEGER,
	r_merge_id INTEGER,
	r_pim_id INTEGER,
	wilson_b_factor_a2_id INTEGER,
	anom_corr_id INTEGER,
	anom_sig_ano_id INTEGER,
	r_work_id INTEGER,
	r_free_id INTEGER,
	ramachandran_favored_percent_id INTEGER,
	ramachandran_outliers_percent_id INTEGER,
	clashscore_id INTEGER,
	molprobity_score_id INTEGER,
	average_b_factor_a2_id INTEGER,
	i_zero_id INTEGER,
	rg_id INTEGER,
	r_factor_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(resolution_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(resolution_high_shell_a_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(resolution_low_a_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(completeness_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(completeness_high_res_shell_percent_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(signal_to_noise_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(mean_i_over_sigma_i_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(unit_cell_a_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(unit_cell_b_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(unit_cell_c_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(unit_cell_alpha_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(unit_cell_beta_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(unit_cell_gamma_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(multiplicity_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(cc_half_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(r_merge_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(r_pim_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(wilson_b_factor_a2_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(anom_corr_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(anom_sig_ano_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(r_work_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(r_free_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(ramachandran_favored_percent_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(ramachandran_outliers_percent_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(clashscore_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(molprobity_score_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(average_b_factor_a2_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(i_zero_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(rg_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(r_factor_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_QualityMetrics_id" ON "QualityMetrics" (id);
CREATE TABLE "ComputeResources" (
	id INTEGER NOT NULL,
	description TEXT,
	cpu_hours_id INTEGER,
	gpu_hours_id INTEGER,
	memory_gb_id INTEGER,
	storage_gb_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(cpu_hours_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(gpu_hours_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(memory_gb_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(storage_gb_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_ComputeResources_id" ON "ComputeResources" (id);
CREATE TABLE "MotionCorrectionParameters" (
	id INTEGER NOT NULL,
	dose_weighting BOOLEAN,
	anisotropic_correction BOOLEAN,
	description TEXT,
	patch_size_id INTEGER,
	binning_id INTEGER,
	bfactor_dose_weighting_id INTEGER,
	frame_grouping_id INTEGER,
	output_binning_id INTEGER,
	drift_total_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(patch_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(binning_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(bfactor_dose_weighting_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(frame_grouping_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(output_binning_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(drift_total_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_MotionCorrectionParameters_id" ON "MotionCorrectionParameters" (id);
CREATE TABLE "CTFEstimationParameters" (
	id INTEGER NOT NULL,
	description TEXT,
	defocus_search_min_id INTEGER,
	defocus_search_max_id INTEGER,
	defocus_step_id INTEGER,
	amplitude_contrast_id INTEGER,
	cs_used_in_estimation_id INTEGER,
	voltage_used_in_estimation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(defocus_search_min_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(defocus_search_max_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(defocus_step_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(amplitude_contrast_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(cs_used_in_estimation_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(voltage_used_in_estimation_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_CTFEstimationParameters_id" ON "CTFEstimationParameters" (id);
CREATE TABLE "ParticlePickingParameters" (
	id INTEGER NOT NULL,
	picking_method TEXT,
	model_name TEXT,
	model_file_path TEXT,
	model_source TEXT,
	description TEXT,
	box_size_id INTEGER,
	threshold_id INTEGER,
	power_score_id INTEGER,
	ncc_score_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(box_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(threshold_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(power_score_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(ncc_score_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_ParticlePickingParameters_id" ON "ParticlePickingParameters" (id);
CREATE TABLE "RefinementParameters" (
	id INTEGER NOT NULL,
	symmetry VARCHAR(3),
	gold_standard BOOLEAN,
	split_strategy TEXT,
	description TEXT,
	pixel_size_id INTEGER,
	box_size_id INTEGER,
	resolution_0_143_id INTEGER,
	resolution_0_5_id INTEGER,
	map_sharpening_bfactor_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(pixel_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(box_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(resolution_0_143_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(resolution_0_5_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(map_sharpening_bfactor_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_RefinementParameters_id" ON "RefinementParameters" (id);
CREATE TABLE "FunctionalSite" (
	site_type VARCHAR(20) NOT NULL,
	site_name TEXT,
	conservation_score FLOAT,
	functional_importance TEXT,
	ec_number TEXT,
	protein_id TEXT NOT NULL,
	pdb_entry TEXT,
	chain_id TEXT,
	residue_range TEXT,
	confidence_score FLOAT,
	evidence_type VARCHAR(17),
	evidence_code TEXT,
	source_database VARCHAR(12),
	annotation_method TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"AggregatedProteinView_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AggregatedProteinView_id") REFERENCES "AggregatedProteinView" (id)
);CREATE INDEX "ix_FunctionalSite_id" ON "FunctionalSite" (id);
CREATE TABLE "StructuralFeature" (
	feature_type VARCHAR(19) NOT NULL,
	secondary_structure VARCHAR(9),
	solvent_accessibility FLOAT,
	backbone_flexibility FLOAT,
	disorder_probability FLOAT,
	conformational_state VARCHAR(16),
	structural_motif TEXT,
	domain_assignment TEXT,
	domain_id TEXT,
	protein_id TEXT NOT NULL,
	pdb_entry TEXT,
	chain_id TEXT,
	residue_range TEXT,
	confidence_score FLOAT,
	evidence_type VARCHAR(17),
	evidence_code TEXT,
	source_database VARCHAR(12),
	annotation_method TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"AggregatedProteinView_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AggregatedProteinView_id") REFERENCES "AggregatedProteinView" (id)
);CREATE INDEX "ix_StructuralFeature_id" ON "StructuralFeature" (id);
CREATE TABLE "ProteinProteinInteraction" (
	partner_protein_id TEXT NOT NULL,
	partner_chain_id TEXT,
	interface_area FLOAT,
	binding_energy FLOAT,
	dissociation_constant FLOAT,
	complex_stability VARCHAR(12),
	biological_assembly BOOLEAN,
	protein_id TEXT NOT NULL,
	pdb_entry TEXT,
	chain_id TEXT,
	residue_range TEXT,
	confidence_score FLOAT,
	evidence_type VARCHAR(17),
	evidence_code TEXT,
	source_database VARCHAR(12),
	annotation_method TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"AggregatedProteinView_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AggregatedProteinView_id") REFERENCES "AggregatedProteinView" (id)
);CREATE INDEX "ix_ProteinProteinInteraction_id" ON "ProteinProteinInteraction" (id);
CREATE TABLE "MutationEffect" (
	mutation TEXT NOT NULL,
	mutation_type VARCHAR(12),
	effect_on_stability VARCHAR(20),
	delta_delta_g FLOAT,
	effect_on_function VARCHAR(17),
	functional_impact_description TEXT,
	disease_association TEXT,
	omim_id TEXT,
	clinical_significance VARCHAR(22),
	allele_frequency FLOAT,
	protein_id TEXT NOT NULL,
	pdb_entry TEXT,
	chain_id TEXT,
	residue_range TEXT,
	confidence_score FLOAT,
	evidence_type VARCHAR(17),
	evidence_code TEXT,
	source_database VARCHAR(12),
	annotation_method TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"AggregatedProteinView_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AggregatedProteinView_id") REFERENCES "AggregatedProteinView" (id)
);CREATE INDEX "ix_MutationEffect_id" ON "MutationEffect" (id);
CREATE TABLE "BiophysicalProperty" (
	id INTEGER NOT NULL,
	property_type VARCHAR(25) NOT NULL,
	value FLOAT NOT NULL,
	unit TEXT NOT NULL,
	error FLOAT,
	experimental_method VARCHAR(33),
	description TEXT,
	"AggregatedProteinView_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AggregatedProteinView_id") REFERENCES "AggregatedProteinView" (id)
);CREATE INDEX "ix_BiophysicalProperty_id" ON "BiophysicalProperty" (id);
CREATE TABLE "PostTranslationalModification" (
	modification_type VARCHAR(39) NOT NULL,
	modified_residue TEXT NOT NULL,
	modification_group TEXT,
	mass_shift FLOAT,
	functional_effect TEXT,
	regulatory_role TEXT,
	enzyme TEXT,
	removal_enzyme TEXT,
	protein_id TEXT NOT NULL,
	pdb_entry TEXT,
	chain_id TEXT,
	residue_range TEXT,
	confidence_score FLOAT,
	evidence_type VARCHAR(17),
	evidence_code TEXT,
	source_database VARCHAR(12),
	annotation_method TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"AggregatedProteinView_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AggregatedProteinView_id") REFERENCES "AggregatedProteinView" (id)
);CREATE INDEX "ix_PostTranslationalModification_id" ON "PostTranslationalModification" (id);
CREATE TABLE "DatabaseCrossReference" (
	id INTEGER NOT NULL,
	database_name VARCHAR(8) NOT NULL,
	database_id TEXT NOT NULL,
	database_url TEXT,
	last_updated TEXT,
	description TEXT,
	"AggregatedProteinView_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AggregatedProteinView_id") REFERENCES "AggregatedProteinView" (id)
);CREATE INDEX "ix_DatabaseCrossReference_id" ON "DatabaseCrossReference" (id);
CREATE TABLE "PlantSamplePreparation" (
	sample_material_processing TEXT,
	sample_preservation_method VARCHAR(12),
	embedding_material TEXT,
	plane_of_section TEXT,
	support_type TEXT NOT NULL,
	adhesive TEXT,
	top_layer TEXT,
	preparation_type VARCHAR(20) NOT NULL,
	sample_id TEXT,
	preparation_date DATE,
	operator_id TEXT,
	protocol_description TEXT,
	host_strain_or_cell_line TEXT,
	medium TEXT,
	antibiotic_selection TEXT,
	induction_agent TEXT,
	inducer_concentration TEXT,
	harvest_timepoint TEXT,
	lysis_method TEXT,
	protease_inhibitors TEXT,
	affinity_type TEXT,
	affinity_column TEXT,
	lysis_buffer TEXT,
	wash_buffer TEXT,
	elution_buffer TEXT,
	tag_removal BOOLEAN,
	protease TEXT,
	protease_ratio TEXT,
	second_affinity_reverse TEXT,
	iex_column TEXT,
	hic_column TEXT,
	sec_column TEXT,
	sec_buffer TEXT,
	concentration_method TEXT,
	final_buffer TEXT,
	aggregation_assessment TEXT,
	aliquoting TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Dataset_id" TEXT,
	sample_storage_temperature_id INTEGER,
	harvest_to_preservation_time_id INTEGER,
	section_thickness_id INTEGER,
	support_thickness_id INTEGER,
	top_layer_thickness_id INTEGER,
	culture_volume_l_id INTEGER,
	growth_temperature_c_id INTEGER,
	induction_temperature_c_id INTEGER,
	induction_time_h_id INTEGER,
	od600_at_induction_id INTEGER,
	cleavage_time_h_id INTEGER,
	cleavage_temperature_c_id INTEGER,
	final_concentration_mg_per_ml_id INTEGER,
	yield_mg_id INTEGER,
	purity_by_sds_page_percent_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(sample_storage_temperature_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(harvest_to_preservation_time_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(section_thickness_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(support_thickness_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(top_layer_thickness_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(culture_volume_l_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(growth_temperature_c_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(induction_temperature_c_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(induction_time_h_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(od600_at_induction_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(cleavage_time_h_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(cleavage_temperature_c_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(final_concentration_mg_per_ml_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(yield_mg_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(purity_by_sds_page_percent_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_PlantSamplePreparation_id" ON "PlantSamplePreparation" (id);
CREATE TABLE "Study_keywords" (
	"Study_id" TEXT,
	keywords TEXT,
	PRIMARY KEY ("Study_id", keywords),
	FOREIGN KEY("Study_id") REFERENCES "Study" (id)
);CREATE INDEX "ix_Study_keywords_keywords" ON "Study_keywords" (keywords);CREATE INDEX "ix_Study_keywords_Study_id" ON "Study_keywords" ("Study_id");
CREATE TABLE "ConformationalState_pdb_entries" (
	"ConformationalState_id" INTEGER,
	pdb_entries TEXT,
	PRIMARY KEY ("ConformationalState_id", pdb_entries),
	FOREIGN KEY("ConformationalState_id") REFERENCES "ConformationalState" (id)
);CREATE INDEX "ix_ConformationalState_pdb_entries_pdb_entries" ON "ConformationalState_pdb_entries" (pdb_entries);CREATE INDEX "ix_ConformationalState_pdb_entries_ConformationalState_id" ON "ConformationalState_pdb_entries" ("ConformationalState_id");
CREATE TABLE "ConformationalState_characteristic_features" (
	"ConformationalState_id" INTEGER,
	characteristic_features TEXT,
	PRIMARY KEY ("ConformationalState_id", characteristic_features),
	FOREIGN KEY("ConformationalState_id") REFERENCES "ConformationalState" (id)
);CREATE INDEX "ix_ConformationalState_characteristic_features_characteristic_features" ON "ConformationalState_characteristic_features" (characteristic_features);CREATE INDEX "ix_ConformationalState_characteristic_features_ConformationalState_id" ON "ConformationalState_characteristic_features" ("ConformationalState_id");
CREATE TABLE "AggregatedProteinView_pdb_entries" (
	"AggregatedProteinView_id" TEXT,
	pdb_entries TEXT,
	PRIMARY KEY ("AggregatedProteinView_id", pdb_entries),
	FOREIGN KEY("AggregatedProteinView_id") REFERENCES "AggregatedProteinView" (id)
);CREATE INDEX "ix_AggregatedProteinView_pdb_entries_AggregatedProteinView_id" ON "AggregatedProteinView_pdb_entries" ("AggregatedProteinView_id");CREATE INDEX "ix_AggregatedProteinView_pdb_entries_pdb_entries" ON "AggregatedProteinView_pdb_entries" (pdb_entries);
CREATE TABLE "Sample" (
	sample_code TEXT NOT NULL,
	sample_type VARCHAR(16) NOT NULL,
	preparation_method TEXT,
	organism TEXT,
	anatomy TEXT,
	cell_type TEXT,
	parent_sample_id TEXT,
	quality_metrics TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Dataset_id" TEXT,
	molecular_weight_id INTEGER,
	concentration_id INTEGER,
	buffer_composition_id INTEGER,
	storage_conditions_id INTEGER,
	purity_percentage_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(organism) REFERENCES "OntologyTerm" (id),
	FOREIGN KEY(anatomy) REFERENCES "OntologyTerm" (id),
	FOREIGN KEY(cell_type) REFERENCES "OntologyTerm" (id),
	FOREIGN KEY(parent_sample_id) REFERENCES "Sample" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(molecular_weight_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(concentration_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(buffer_composition_id) REFERENCES "BufferComposition" (id),
	FOREIGN KEY(storage_conditions_id) REFERENCES "StorageConditions" (id),
	FOREIGN KEY(purity_percentage_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_Sample_id" ON "Sample" (id);
CREATE TABLE "ExperimentRun" (
	experiment_code TEXT NOT NULL,
	experiment_date DATE,
	operator_id TEXT,
	technique VARCHAR(29) NOT NULL,
	raw_data_location TEXT,
	processing_status VARCHAR(13),
	autoloader_slot TEXT,
	acquisition_software TEXT,
	acquisition_software_version TEXT,
	beamline TEXT,
	synchrotron_mode TEXT,
	start_time TEXT,
	end_time TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Dataset_id" TEXT,
	experimental_conditions_id INTEGER,
	data_collection_strategy_id INTEGER,
	magnification_id INTEGER,
	calibrated_pixel_size_id INTEGER,
	camera_binning_id INTEGER,
	exposure_time_per_frame_id INTEGER,
	frames_per_movie_id INTEGER,
	total_exposure_time_id INTEGER,
	total_dose_id INTEGER,
	dose_rate_id INTEGER,
	defocus_target_id INTEGER,
	defocus_range_min_id INTEGER,
	defocus_range_max_id INTEGER,
	defocus_range_increment_id INTEGER,
	astigmatism_target_id INTEGER,
	coma_id INTEGER,
	stage_tilt_id INTEGER,
	shots_per_hole_id INTEGER,
	holes_per_group_id INTEGER,
	wavelength_id INTEGER,
	oscillation_angle_id INTEGER,
	start_angle_id INTEGER,
	number_of_images_id INTEGER,
	beam_center_x_id INTEGER,
	beam_center_y_id INTEGER,
	detector_distance_id INTEGER,
	pixel_size_x_id INTEGER,
	pixel_size_y_id INTEGER,
	total_rotation_id INTEGER,
	transmission_id INTEGER,
	flux_id INTEGER,
	flux_end_id INTEGER,
	slit_gap_horizontal_id INTEGER,
	slit_gap_vertical_id INTEGER,
	undulator_gap_id INTEGER,
	exposure_time_id INTEGER,
	resolution_id INTEGER,
	resolution_at_corner_id INTEGER,
	ispyb_data_collection_id_id INTEGER,
	ispyb_session_id_id INTEGER,
	beam_size_x_id INTEGER,
	beam_size_y_id INTEGER,
	dwell_time_id INTEGER,
	energy_id INTEGER,
	beamline_parameters_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(experimental_conditions_id) REFERENCES "ExperimentalConditions" (id),
	FOREIGN KEY(data_collection_strategy_id) REFERENCES "DataCollectionStrategy" (id),
	FOREIGN KEY(magnification_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(calibrated_pixel_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(camera_binning_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(exposure_time_per_frame_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(frames_per_movie_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(total_exposure_time_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(total_dose_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dose_rate_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(defocus_target_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(defocus_range_min_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(defocus_range_max_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(defocus_range_increment_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(astigmatism_target_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(coma_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(stage_tilt_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(shots_per_hole_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(holes_per_group_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(wavelength_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(oscillation_angle_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(start_angle_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(number_of_images_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(beam_center_x_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(beam_center_y_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(detector_distance_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(pixel_size_x_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(pixel_size_y_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(total_rotation_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(transmission_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(flux_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(flux_end_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(slit_gap_horizontal_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(slit_gap_vertical_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(undulator_gap_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(exposure_time_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(resolution_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(resolution_at_corner_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(ispyb_data_collection_id_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(ispyb_session_id_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(beam_size_x_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(beam_size_y_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(dwell_time_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(energy_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(beamline_parameters_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_ExperimentRun_id" ON "ExperimentRun" (id);
CREATE TABLE "StudyWorkflowAssociation" (
	id INTEGER NOT NULL,
	study_id TEXT NOT NULL,
	workflow_id TEXT NOT NULL,
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(study_id) REFERENCES "Study" (id),
	FOREIGN KEY(workflow_id) REFERENCES "WorkflowRun" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_StudyWorkflowAssociation_id" ON "StudyWorkflowAssociation" (id);
CREATE TABLE "WorkflowInputAssociation" (
	id INTEGER NOT NULL,
	workflow_id TEXT NOT NULL,
	file_id TEXT NOT NULL,
	input_type VARCHAR(10),
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(workflow_id) REFERENCES "WorkflowRun" (id),
	FOREIGN KEY(file_id) REFERENCES "DataFile" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_WorkflowInputAssociation_id" ON "WorkflowInputAssociation" (id);
CREATE TABLE "WorkflowOutputAssociation" (
	id INTEGER NOT NULL,
	workflow_id TEXT NOT NULL,
	file_id TEXT NOT NULL,
	output_type VARCHAR(14),
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(workflow_id) REFERENCES "WorkflowRun" (id),
	FOREIGN KEY(file_id) REFERENCES "DataFile" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_WorkflowOutputAssociation_id" ON "WorkflowOutputAssociation" (id);
CREATE TABLE "LigandInteraction" (
	id INTEGER NOT NULL,
	ligand_id TEXT NOT NULL,
	ligand_name TEXT NOT NULL,
	ligand_smiles TEXT,
	binding_affinity FLOAT,
	binding_affinity_type VARCHAR(4),
	binding_affinity_unit VARCHAR(10),
	interaction_type VARCHAR(18),
	is_cofactor BOOLEAN,
	is_drug_like BOOLEAN,
	druggability_score FLOAT,
	interaction_distance FLOAT,
	description TEXT,
	"FunctionalSite_id" TEXT,
	"AggregatedProteinView_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("FunctionalSite_id") REFERENCES "FunctionalSite" (id),
	FOREIGN KEY("AggregatedProteinView_id") REFERENCES "AggregatedProteinView" (id)
);CREATE INDEX "ix_LigandInteraction_id" ON "LigandInteraction" (id);
CREATE TABLE "MeasurementConditions" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"BiophysicalProperty_id" INTEGER,
	buffer_composition_id INTEGER,
	ph_id INTEGER,
	ionic_strength_id INTEGER,
	temperature_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BiophysicalProperty_id") REFERENCES "BiophysicalProperty" (id),
	FOREIGN KEY(buffer_composition_id) REFERENCES "BufferComposition" (id),
	FOREIGN KEY(ph_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(ionic_strength_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(temperature_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_MeasurementConditions_id" ON "MeasurementConditions" (id);
CREATE TABLE "FTIRImage_molecular_signatures" (
	"FTIRImage_id" TEXT,
	molecular_signatures TEXT,
	PRIMARY KEY ("FTIRImage_id", molecular_signatures),
	FOREIGN KEY("FTIRImage_id") REFERENCES "FTIRImage" (id)
);CREATE INDEX "ix_FTIRImage_molecular_signatures_molecular_signatures" ON "FTIRImage_molecular_signatures" (molecular_signatures);CREATE INDEX "ix_FTIRImage_molecular_signatures_FTIRImage_id" ON "FTIRImage_molecular_signatures" ("FTIRImage_id");
CREATE TABLE "OpticalImage_color_channels" (
	"OpticalImage_id" TEXT,
	color_channels TEXT,
	PRIMARY KEY ("OpticalImage_id", color_channels),
	FOREIGN KEY("OpticalImage_id") REFERENCES "OpticalImage" (id)
);CREATE INDEX "ix_OpticalImage_color_channels_color_channels" ON "OpticalImage_color_channels" (color_channels);CREATE INDEX "ix_OpticalImage_color_channels_OpticalImage_id" ON "OpticalImage_color_channels" ("OpticalImage_id");
CREATE TABLE "XRFImage_elements_measured" (
	"XRFImage_id" TEXT,
	elements_measured TEXT,
	PRIMARY KEY ("XRFImage_id", elements_measured),
	FOREIGN KEY("XRFImage_id") REFERENCES "XRFImage" (id)
);CREATE INDEX "ix_XRFImage_elements_measured_elements_measured" ON "XRFImage_elements_measured" (elements_measured);CREATE INDEX "ix_XRFImage_elements_measured_XRFImage_id" ON "XRFImage_elements_measured" ("XRFImage_id");
CREATE TABLE "BufferComposition_components" (
	"BufferComposition_id" INTEGER,
	components TEXT,
	PRIMARY KEY ("BufferComposition_id", components),
	FOREIGN KEY("BufferComposition_id") REFERENCES "BufferComposition" (id)
);CREATE INDEX "ix_BufferComposition_components_components" ON "BufferComposition_components" (components);CREATE INDEX "ix_BufferComposition_components_BufferComposition_id" ON "BufferComposition_components" ("BufferComposition_id");
CREATE TABLE "BufferComposition_additives" (
	"BufferComposition_id" INTEGER,
	additives TEXT,
	PRIMARY KEY ("BufferComposition_id", additives),
	FOREIGN KEY("BufferComposition_id") REFERENCES "BufferComposition" (id)
);CREATE INDEX "ix_BufferComposition_additives_additives" ON "BufferComposition_additives" (additives);CREATE INDEX "ix_BufferComposition_additives_BufferComposition_id" ON "BufferComposition_additives" ("BufferComposition_id");
CREATE TABLE "FunctionalSite_residues" (
	"FunctionalSite_id" TEXT,
	residues TEXT,
	PRIMARY KEY ("FunctionalSite_id", residues),
	FOREIGN KEY("FunctionalSite_id") REFERENCES "FunctionalSite" (id)
);CREATE INDEX "ix_FunctionalSite_residues_residues" ON "FunctionalSite_residues" (residues);CREATE INDEX "ix_FunctionalSite_residues_FunctionalSite_id" ON "FunctionalSite_residues" ("FunctionalSite_id");
CREATE TABLE "FunctionalSite_go_terms" (
	"FunctionalSite_id" TEXT,
	go_terms TEXT,
	PRIMARY KEY ("FunctionalSite_id", go_terms),
	FOREIGN KEY("FunctionalSite_id") REFERENCES "FunctionalSite" (id)
);CREATE INDEX "ix_FunctionalSite_go_terms_FunctionalSite_id" ON "FunctionalSite_go_terms" ("FunctionalSite_id");CREATE INDEX "ix_FunctionalSite_go_terms_go_terms" ON "FunctionalSite_go_terms" (go_terms);
CREATE TABLE "FunctionalSite_publication_ids" (
	"FunctionalSite_id" TEXT,
	publication_ids TEXT,
	PRIMARY KEY ("FunctionalSite_id", publication_ids),
	FOREIGN KEY("FunctionalSite_id") REFERENCES "FunctionalSite" (id)
);CREATE INDEX "ix_FunctionalSite_publication_ids_FunctionalSite_id" ON "FunctionalSite_publication_ids" ("FunctionalSite_id");CREATE INDEX "ix_FunctionalSite_publication_ids_publication_ids" ON "FunctionalSite_publication_ids" (publication_ids);
CREATE TABLE "StructuralFeature_publication_ids" (
	"StructuralFeature_id" TEXT,
	publication_ids TEXT,
	PRIMARY KEY ("StructuralFeature_id", publication_ids),
	FOREIGN KEY("StructuralFeature_id") REFERENCES "StructuralFeature" (id)
);CREATE INDEX "ix_StructuralFeature_publication_ids_StructuralFeature_id" ON "StructuralFeature_publication_ids" ("StructuralFeature_id");CREATE INDEX "ix_StructuralFeature_publication_ids_publication_ids" ON "StructuralFeature_publication_ids" (publication_ids);
CREATE TABLE "ProteinProteinInteraction_interface_residues" (
	"ProteinProteinInteraction_id" TEXT,
	interface_residues TEXT,
	PRIMARY KEY ("ProteinProteinInteraction_id", interface_residues),
	FOREIGN KEY("ProteinProteinInteraction_id") REFERENCES "ProteinProteinInteraction" (id)
);CREATE INDEX "ix_ProteinProteinInteraction_interface_residues_ProteinProteinInteraction_id" ON "ProteinProteinInteraction_interface_residues" ("ProteinProteinInteraction_id");CREATE INDEX "ix_ProteinProteinInteraction_interface_residues_interface_residues" ON "ProteinProteinInteraction_interface_residues" (interface_residues);
CREATE TABLE "ProteinProteinInteraction_partner_interface_residues" (
	"ProteinProteinInteraction_id" TEXT,
	partner_interface_residues TEXT,
	PRIMARY KEY ("ProteinProteinInteraction_id", partner_interface_residues),
	FOREIGN KEY("ProteinProteinInteraction_id") REFERENCES "ProteinProteinInteraction" (id)
);CREATE INDEX "ix_ProteinProteinInteraction_partner_interface_residues_ProteinProteinInteraction_id" ON "ProteinProteinInteraction_partner_interface_residues" ("ProteinProteinInteraction_id");CREATE INDEX "ix_ProteinProteinInteraction_partner_interface_residues_partner_interface_residues" ON "ProteinProteinInteraction_partner_interface_residues" (partner_interface_residues);
CREATE TABLE "ProteinProteinInteraction_interaction_evidence" (
	"ProteinProteinInteraction_id" TEXT,
	interaction_evidence VARCHAR(14),
	PRIMARY KEY ("ProteinProteinInteraction_id", interaction_evidence),
	FOREIGN KEY("ProteinProteinInteraction_id") REFERENCES "ProteinProteinInteraction" (id)
);CREATE INDEX "ix_ProteinProteinInteraction_interaction_evidence_interaction_evidence" ON "ProteinProteinInteraction_interaction_evidence" (interaction_evidence);CREATE INDEX "ix_ProteinProteinInteraction_interaction_evidence_ProteinProteinInteraction_id" ON "ProteinProteinInteraction_interaction_evidence" ("ProteinProteinInteraction_id");
CREATE TABLE "ProteinProteinInteraction_publication_ids" (
	"ProteinProteinInteraction_id" TEXT,
	publication_ids TEXT,
	PRIMARY KEY ("ProteinProteinInteraction_id", publication_ids),
	FOREIGN KEY("ProteinProteinInteraction_id") REFERENCES "ProteinProteinInteraction" (id)
);CREATE INDEX "ix_ProteinProteinInteraction_publication_ids_ProteinProteinInteraction_id" ON "ProteinProteinInteraction_publication_ids" ("ProteinProteinInteraction_id");CREATE INDEX "ix_ProteinProteinInteraction_publication_ids_publication_ids" ON "ProteinProteinInteraction_publication_ids" (publication_ids);
CREATE TABLE "MutationEffect_publication_ids" (
	"MutationEffect_id" TEXT,
	publication_ids TEXT,
	PRIMARY KEY ("MutationEffect_id", publication_ids),
	FOREIGN KEY("MutationEffect_id") REFERENCES "MutationEffect" (id)
);CREATE INDEX "ix_MutationEffect_publication_ids_publication_ids" ON "MutationEffect_publication_ids" (publication_ids);CREATE INDEX "ix_MutationEffect_publication_ids_MutationEffect_id" ON "MutationEffect_publication_ids" ("MutationEffect_id");
CREATE TABLE "PostTranslationalModification_publication_ids" (
	"PostTranslationalModification_id" TEXT,
	publication_ids TEXT,
	PRIMARY KEY ("PostTranslationalModification_id", publication_ids),
	FOREIGN KEY("PostTranslationalModification_id") REFERENCES "PostTranslationalModification" (id)
);CREATE INDEX "ix_PostTranslationalModification_publication_ids_publication_ids" ON "PostTranslationalModification_publication_ids" (publication_ids);CREATE INDEX "ix_PostTranslationalModification_publication_ids_PostTranslationalModification_id" ON "PostTranslationalModification_publication_ids" ("PostTranslationalModification_id");
CREATE TABLE "StudySampleAssociation" (
	id INTEGER NOT NULL,
	study_id TEXT NOT NULL,
	sample_id TEXT NOT NULL,
	role VARCHAR(9),
	date_added DATE,
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(study_id) REFERENCES "Study" (id),
	FOREIGN KEY(sample_id) REFERENCES "Sample" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_StudySampleAssociation_id" ON "StudySampleAssociation" (id);
CREATE TABLE "SampleDataAssociation" (
	id INTEGER NOT NULL,
	sample_id TEXT NOT NULL,
	data_id TEXT NOT NULL,
	role VARCHAR(9),
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(sample_id) REFERENCES "Sample" (id),
	FOREIGN KEY(data_id) REFERENCES "DataFile" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_SampleDataAssociation_id" ON "SampleDataAssociation" (id);
CREATE TABLE "StudyExperimentAssociation" (
	id INTEGER NOT NULL,
	study_id TEXT NOT NULL,
	experiment_id TEXT NOT NULL,
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(study_id) REFERENCES "Study" (id),
	FOREIGN KEY(experiment_id) REFERENCES "ExperimentRun" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_StudyExperimentAssociation_id" ON "StudyExperimentAssociation" (id);
CREATE TABLE "ExperimentSampleAssociation" (
	id INTEGER NOT NULL,
	experiment_id TEXT NOT NULL,
	sample_id TEXT NOT NULL,
	role VARCHAR(12),
	preparation_id TEXT,
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(experiment_id) REFERENCES "ExperimentRun" (id),
	FOREIGN KEY(sample_id) REFERENCES "Sample" (id),
	FOREIGN KEY(preparation_id) REFERENCES "SamplePreparation" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_ExperimentSampleAssociation_id" ON "ExperimentSampleAssociation" (id);
CREATE TABLE "ExperimentInstrumentAssociation" (
	id INTEGER NOT NULL,
	experiment_id TEXT NOT NULL,
	instrument_id TEXT NOT NULL,
	role VARCHAR(14),
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(experiment_id) REFERENCES "ExperimentRun" (id),
	FOREIGN KEY(instrument_id) REFERENCES "Instrument" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_ExperimentInstrumentAssociation_id" ON "ExperimentInstrumentAssociation" (id);
CREATE TABLE "WorkflowExperimentAssociation" (
	id INTEGER NOT NULL,
	workflow_id TEXT NOT NULL,
	experiment_id TEXT NOT NULL,
	"Dataset_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(workflow_id) REFERENCES "WorkflowRun" (id),
	FOREIGN KEY(experiment_id) REFERENCES "ExperimentRun" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id)
);CREATE INDEX "ix_WorkflowExperimentAssociation_id" ON "WorkflowExperimentAssociation" (id);
CREATE TABLE "PlantSample" (
	biological_replicate_sample_group_name TEXT,
	combined_tissue_description TEXT,
	experimental_time_point_number INTEGER,
	experimental_time_point_description TEXT,
	genus TEXT NOT NULL,
	species TEXT NOT NULL,
	strain_variety_cultivar TEXT,
	isolate TEXT,
	germplasm_collection_id TEXT,
	ncbi_taxonomy_id INTEGER,
	ancestral_data TEXT,
	genetic_modification TEXT,
	ploidy VARCHAR(13),
	reference_genome TEXT,
	collection_date_time TEXT NOT NULL,
	tissue TEXT NOT NULL,
	tissue_plant_ontology_term TEXT,
	region_locality TEXT,
	latitude FLOAT,
	longitude FLOAT,
	broad_scale_environmental_context TEXT,
	local_environmental_context TEXT,
	environmental_medium TEXT,
	growth_facility VARCHAR(15) NOT NULL,
	growth_medium TEXT NOT NULL,
	growth_medium_composition TEXT,
	plant_age TEXT,
	developmental_stage TEXT NOT NULL,
	arabadopsis_phenotype_stage VARCHAR(10),
	air_temperature_regimen TEXT,
	antibiotic_regimen TEXT,
	biotic_regimen TEXT,
	inoculation_method TEXT,
	time_post_inoculation TEXT,
	chemical_administration TEXT,
	chemical_mutagen TEXT,
	fertilizer_administration TEXT,
	insecticide_regimen TEXT,
	fungicide_regimen TEXT,
	gaseous_environment TEXT,
	growth_hormone_regimen TEXT,
	herbicide_regimen TEXT,
	humidity_regimen TEXT,
	radiation_regimen TEXT,
	light_regimen TEXT,
	last_light_transition_type TEXT,
	time_after_last_light_transition TEXT,
	salt_regimen TEXT,
	rainfall_regimen TEXT,
	watering_regimen TEXT,
	other_treatment_regimen TEXT,
	perturbation TEXT,
	mechanical_damage TEXT,
	observed_host_symbionts TEXT,
	plant_sex TEXT,
	sample_disease_staus TEXT,
	sample_disease_stage TEXT,
	sample_code TEXT NOT NULL,
	sample_type VARCHAR(16) NOT NULL,
	preparation_method TEXT,
	organism TEXT,
	anatomy TEXT,
	cell_type TEXT,
	parent_sample_id TEXT,
	quality_metrics TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"Dataset_id" TEXT,
	estimated_genome_size_mb_id INTEGER,
	gc_content_percent_id INTEGER,
	sample_size_id INTEGER,
	depth_meters_id INTEGER,
	elevation_meters_id INTEGER,
	temperature_id INTEGER,
	molecular_weight_id INTEGER,
	concentration_id INTEGER,
	buffer_composition_id INTEGER,
	storage_conditions_id INTEGER,
	purity_percentage_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(organism) REFERENCES "OntologyTerm" (id),
	FOREIGN KEY(anatomy) REFERENCES "OntologyTerm" (id),
	FOREIGN KEY(cell_type) REFERENCES "OntologyTerm" (id),
	FOREIGN KEY(parent_sample_id) REFERENCES "Sample" (id),
	FOREIGN KEY("Dataset_id") REFERENCES "Dataset" (id),
	FOREIGN KEY(estimated_genome_size_mb_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(gc_content_percent_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(sample_size_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(depth_meters_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(elevation_meters_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(temperature_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(molecular_weight_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(concentration_id) REFERENCES "QuantityValue" (id),
	FOREIGN KEY(buffer_composition_id) REFERENCES "BufferComposition" (id),
	FOREIGN KEY(storage_conditions_id) REFERENCES "StorageConditions" (id),
	FOREIGN KEY(purity_percentage_id) REFERENCES "QuantityValue" (id)
);CREATE INDEX "ix_PlantSample_id" ON "PlantSample" (id);
CREATE TABLE "LigandInteraction_binding_site_residues" (
	"LigandInteraction_id" INTEGER,
	binding_site_residues TEXT,
	PRIMARY KEY ("LigandInteraction_id", binding_site_residues),
	FOREIGN KEY("LigandInteraction_id") REFERENCES "LigandInteraction" (id)
);CREATE INDEX "ix_LigandInteraction_binding_site_residues_LigandInteraction_id" ON "LigandInteraction_binding_site_residues" ("LigandInteraction_id");CREATE INDEX "ix_LigandInteraction_binding_site_residues_binding_site_residues" ON "LigandInteraction_binding_site_residues" (binding_site_residues);
