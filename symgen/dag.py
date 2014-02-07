class Node(object):
    def __init__(self, *deps, **meta):
        self.deps = deps
        self.meta = meta

class Shaped(object):
    """
    If vectorization handled explicitly, useful to track shapes & types along
    dataflow. This forces us to handle broadcasting, reductions, etc. correctly.
    If none is given, we can assume scalar? Idx and Assign would be informed.

    """

    def __init__(self, *deps, **meta):
        for k, v in (('shape', ()), ('dtype', 'f32')):
            meta[k] = meta.get(k, v)
        super(Shape, self).__init__(*deps, **meta)

class Idx(Node, Shaped):
    def __init__(self, *deps, **meta):
        meta['dtype'] = meta.get('dtype', 'i32')
        super(Idx, self).__init__(*deps, **meta)

class Indexable(object):
    def __getitem__(self, key):
        return Idx(self, key)

class Expr(Node, Shaped):
    arith = lambda op: lambda s, o: Expr(s, o, op=op)
    for op in 'mul add div sub'.split(' '):
        locals()['__%s__' % op] = arith(op)

class Assign(Node, Shaped):
    "Depend on an assignment, not symbol, for the assigned value"
    pass

class Sym(Expr, Shaped):
    pass

class Const(Node, Shaped):
    pass

class Par(Node, Shaped):
    pass

# Coupling (summation is a reduction)
class Reduce(Node):
    pass

class DenseReduce(Node):
    pass

class SparseReduce(Node):
    pass

# Noise : Randn + Expr
class Randn(Node, Shaped):
    pass

# Monitors
class Buffer(Node, Shaped):
    pass

class Filter(Node, Shaped):
    pass

class SpatialFilter(Filter):
    pass

class TemporalFilter(Filter):
    pass

# Stimulus is broadcasting temporal & spatial vector : expr + idx
class Stimulus(Node):
    pass

