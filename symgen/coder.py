
"""
symgen.gen
==========

Provide base classes for code generation.

"""


class DAGTransform(object):
    "Traverse graph, transform nodes & subgraphs"
    pass

class ExpandLoops(DAGTransform):
    pass

class Coder(object):
    transforms = [ExpandLoops] # for example
    def __call__(self, dag):
        for t in self.transforms:
            dag = t(dag)
        nodes = dag.sort()
        for n in nodes:
            kind = n.__class__.__name__.lower()
            yield getattr(self, 'gen_'+kind)(n)

