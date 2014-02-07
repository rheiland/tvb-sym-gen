"""
symgen.tvb
----------

Trivial transformations from TVB's simulator class to IR nodes

"""

from . import ir


class Coupling(ir.Node):
    """
    An IR node representing a TVB Coupling instance.

    """


class Integrator(ir.Node):
    """
    An IR node representing a TVB Integrator instance.

    """


class Model(ir.Node):
    """
    An IR node representing a TVB Model instance.

    """


class Monitor(ir.Node):
    """
    An IR node representing a TVB Monitor instance.

    """


class Noise(ir.Node):
    """
    An IR node representing a TVB Noise instance.

    """


class Simulator(ir.Node):
    """
    An IR node representing a TVB Simulator instance.

    """



