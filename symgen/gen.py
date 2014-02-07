
"""
symgen.gen
==========

Provide base classes for code generation.

"""

import abc


class Gen(object):
    """
    Base class for code generators. 

    """

    __metaclass__ = abc.ABCMeta


class Cee(Gen):
    pass


class CL(Cee):
    pass


class CUDA(Cee):
    pass


class Cython(Gen):
    pass


class JS(Gen):
    pass


