class Node(object):
    def __init__(self, *deps, **meta):
        self.deps = deps
        self.meta = meta

class Idx(Node):
    pass

class Indexable(object):
    def __getitem__(self, key):
        return Idx(self, key)

class Expr(Node):
    arith = lambda op: lambda s, o: Expr(s, o, op=op)
    for op in 'mul add div sub'.split(' '):
        locals()['__%s__' % op] = arith(op)

class Assign(Node):
    pass

class Sym(Expr):
    pass

class Const(Node):
    pass

class Par(Node):
    pass

class Sum(Node):
    pass

class DenseSum(Node):
    pass

class SparseSum(Node):
    pass

class Randn(Node):
    pass

"""
n, m = Dim(name="n"), Dim(name="m")
x = Sym(name='x', shape=(n, ))
dt = Const(value=0.1)
i = Sym(name='i')
x_i = x[i]
set_x = Assign(x_i, x_i + dt*(-x_i))

But normally we'd indicate dependence of symbol on expression, not assignment
on expression. How ot resolve? Indicate that a symbol binds to value. For the
purposes of the loop body, we can assume single assignent, so

>>> dx = Sym(-x, name='dx', shape=(n, ))
>>> x = 

Nope, we need to rep the Assign explicitly, and ref it. The dependence of the
sequence needs to be part of the graph.

If vectorization handled explicitly, useful to track shapes & types along
dataflow. This forces us to handle broadcasting, reductions, etc. correctly.
If none is given, we can assume scalar? Idx and Assign would be informed.

"""
