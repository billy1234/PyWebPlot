import os, pkgutil
import matplotlib
matplotlib.use('agg')
__all__ = list(module for _, module, _ in pkgutil.iter_modules([os.path.dirname(__file__)]))