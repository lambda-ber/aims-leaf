# Data Model Overview

This page describes the AIMS-LEAF modeling direction at a conceptual level. It is intentionally centered on plant heat stress tolerance and multimodal predictive modeling rather than the inherited legacy emphasis.

## Modeling Objective

The project needs a data model that can support learning across linked biological scales. The core unit is not a single assay type. It is the relationship between intervention, context, observation, and outcome.

## Core Modeling Areas

### Biological Context

- host organism and plant line
- genotype, edited locus, or other engineered change
- treatment and environmental exposure
- developmental stage and sampling context

### Data Acquisition

- sequencing-based measurements
- cellular, tissue, and organism-scale imaging
- phenotype observations and assay summaries
- experimental metadata needed to compare measurements across runs and sites

### Computational Layer

- preprocessing and feature extraction workflows
- model-ready derived tables and embeddings
- predictive outputs, confidence values, and evaluation metrics
- provenance connecting raw inputs to downstream inference

## Design Principles

### Flexible by Modality

The model should not assume one preferred instrument or assay family. It should be able to accommodate new imaging pipelines, sequencing assays, and derived feature sets without forcing a redesign of the entire schema.

### Scalable by Resolution

AIMS-LEAF needs to support multiscale linkage, from gene-level perturbation through image-derived traits and whole-host phenotype.

### Explicit About Provenance

Predictive modeling is only useful if inputs and transformations are traceable. The model therefore needs to preserve links between source observations, feature engineering, trained models, and evaluated predictions.

### Suitable for AI/ML Workflows

The schema should make it straightforward to assemble analysis tables, training sets, validation sets, and cross-modal feature views without extensive manual reshaping.

## Example Conceptual Flow

1. Register a plant line and its genetic modification.
2. Record heat stress treatment conditions and sampling schedule.
3. Link sequencing outputs, imaging outputs, and phenotype measurements to the same biological context.
4. Track feature extraction and model training workflows.
5. Store predictions and observed outcomes so the project can compare expected and actual host response.

## Current Refactor Status

The inherited repository still contains schema artifacts from its previous project scope. Documentation in this site now reflects the intended AIMS-LEAF direction and will guide subsequent schema refactoring.
