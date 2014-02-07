"""
symgen.tvb
----------

Trivial transformations from TVB's simulator class to IR nodes

"""

from tvb.simulator import (
        coupling, integrators, models, monitors, noise, simulator
    )


from . import ir

class Coupling(ir.Node, coupling.Coupling):
    """
    An IR node representing a TVB Coupling instance.

    """


class Integrator(ir.Node, integrators.Integrator):
    """
    An IR node representing a TVB Integrator instance.

    """


class Model(ir.Node, models.Model):
    """
    An IR node representing a TVB Model instance.

    """


class Monitor(ir.Node, monitors.Monitor):
    """
    An IR node representing a TVB Monitor instance.

    """


class Noise(ir.Node, noise.Noise):
    """
    An IR node representing a TVB Noise instance.

    """


class Simulator(ir.Node, simulator.Simulator):
    """
    An IR node representing a TVB Simulator instance.

    """



