import os

__all__ = ['__version__']

DIR = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(DIR, 'VERSION')) as f:
    __version__ = str(f.read().strip())
