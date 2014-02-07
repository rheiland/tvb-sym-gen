
"""
Code generation from a dag. 

- dag should be dumpable & diffable
- debug logging should be able to dump dag in between 
    passes so we can incrementally debug the passes
- transforms / passes should distinct from coder
- but coder can spec required passes 
- need a graph-subgarph isomorphism test (matching)?
- simplegeneric + tuple approach?

- three phases of transforms
  - simulator primitives translate themselves to ir
  - various transforms for optimization?
  - pre-coder transforms required 
- then coder generates actual code

- what about runtime & allocation?

"""

import dag

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

