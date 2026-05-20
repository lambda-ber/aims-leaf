"""
ETL loaders for importing data from external structural biology repositories.

Available loaders:
- SASBDBLoader: Small Angle Scattering Biological Data Bank
- SimpleScatteringLoader: Simple Scattering (SEC-SAXS from SIBYLS)
- EMSLLoader: EMSL public API transactions and metadata

Example:
    >>> from aims_leaf_schema.loaders import SASBDBLoader
    >>> loader = SASBDBLoader()
    >>> result = loader.load("SASDA52")
    >>> result.dataset.id
    'sasbdb:SASDA52'
"""

from aims_leaf_schema.loaders.base import BaseLoader, LoaderResult
from aims_leaf_schema.loaders.batch import BatchLoader, BatchProgress
from aims_leaf_schema.loaders.cache import ResponseCache
from aims_leaf_schema.loaders.emsl import EMSLLoader
from aims_leaf_schema.loaders.pdb import PDBLoader

try:
    from aims_leaf_schema.loaders.sasbdb import SASBDBLoader
except ImportError:
    SASBDBLoader = None

try:
    from aims_leaf_schema.loaders.simplescattering import SimpleScatteringLoader
except ImportError:
    SimpleScatteringLoader = None

__all__ = [
    "BaseLoader",
    "BatchLoader",
    "BatchProgress",
    "LoaderResult",
    "ResponseCache",
    "EMSLLoader",
    "PDBLoader",
    "SASBDBLoader",
    "SimpleScatteringLoader",
]
