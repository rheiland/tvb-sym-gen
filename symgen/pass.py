
"""
pass
----

Passes manipulating IR in various ways. Generally, three kinds of passes will
be used, simulation-specific, backend-specific and agnostic passes that deal 
primarily with optimization. 

"""

import abc
import copy


class Pass(object):
    """
    Passes walk the IR and perform certain transformations.

    """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def match(self, node):
        """
        Test whether `self` should transform `node`.

        """

        pass

    @abc.abstractmethod
    def transform(self, node):
        """
        Transform `node`.

        """

        pass


    def __call__(self, node, seen=None, copy=copy.copy):
        """
        Perform pass on node, walking depth first.

        """

        for parent, child in node:
            if self.match(child):
                parent.replace(child, self.transform(copy(child)))

