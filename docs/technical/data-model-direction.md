# Data Model Direction

This page captures the intended direction for the AIMS-LEAF data model during the current documentation-first refactor.

## Near-Term Modeling Priorities

The model should make it straightforward to represent:

- plant or host identity
- genotype or engineered modification
- stress treatment and environmental context
- multiscale observations from sequencing and imaging
- phenotype outcomes and response labels
- derived features, model artifacts, and predictions

## Recommended Structural Pattern

A practical direction is to separate the model into a few stable layers:

1. biological entities and interventions
2. observations and assay outputs
3. derived analytical products
4. model training, evaluation, and prediction artifacts

This keeps source measurements distinct from interpretation while preserving traceability across the pipeline.

## Refactor Constraint

The inherited repository still contains schema classes and generated documentation from the previous project scope. Those inherited assets should be treated as transitional rather than normative for the current project direction.

## Documentation Role

Because the markdown pages in `docs/` are the current source of truth for the site, they should describe the target model and project scope clearly even before the underlying schema refactor is complete.