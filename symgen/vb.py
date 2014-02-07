"""
vb
--

Trivial transformations from TVB's simulator class to IR nodes

"""

from . import ir


class TVBNode(ir.Node):
    """
    An IR Node representing an object from TVB.

    """


class Coupling(TVBNode):
    """
    An IR node representing a TVB Coupling instance.

    """


class Integrator(TVBNode):
    """
    An IR node representing a TVB Integrator instance.

    """


class Model(TVBNode):
    """
    An IR node representing a TVB Model instance.

    """


class Monitor(TVBNode):
    """
    An IR node representing a TVB Monitor instance.

    """


class Noise(TVBNode):
    """
    An IR node representing a TVB Noise instance.

    """


class Stimulus(TVBNode):
    """
    An IR node representing a TVB Stimulus instance.

    """

    # broadcasts temporal & spatial vector : expr + idx


class Simulator(TVBNode):
    """
    An IR node representing a TVB Simulator instance.

    """


