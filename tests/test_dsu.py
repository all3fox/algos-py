import random

from itertools import product
from nose.tools import raises

from dsu import DisjointSetUnion as dsu


class CheckDisjointSetUnion:
    @raises(KeyError)
    def check_empty_find(self, DSU):
        DSU().find(0)

    @raises(KeyError)
    def check_empty_union(self, DSU):
        DSU().union(0, 0)

    def check_xs_ys(self, DSU, xs=range(10), ys=range(10)):
        assert len(xs) == len(ys)
        for y in ys: assert y in xs

        dsu = DSU(xs)

        for x, y in zip(xs, ys):
            dsu.union(x, y)

        for x, y in zip(xs, ys):
            assert dsu.find(x) == dsu.find(y)

    def check_random(self, DSU, N=10, seed=0):
        assert N > 0

        random.seed(seed)

        xs = list(range(N))
        ys = [random.randrange(0, N) for i in range(N)]

        self.check_xs_ys(DSU, xs, ys)

    def check_transitive_union(self, DSU, N=10):
        assert N > 1

        xs = list(range(N))
        ys = [
            xs[0] for i in xs[: N // 2]
        ] + [
            xs[N // 2] for i in xs[N // 2 :]
        ]

        dsu = DSU(xs)

        for x, y in zip(xs, ys):
            dsu.union(x, y)

        dsu.union(xs[N // 2 - 1], xs[-1])

        for i, j in product(range(N), range(N)):
            assert dsu.find(i) == dsu.find(j)


class TestDisjointSetUnion(CheckDisjointSetUnion):
    def __init__(self):
        self.DSUS = [dsu]

    def test_empty_find(self):
        for DSU in self.DSUS:
            yield self.check_empty_find, DSU

    def test_empty_union(self):
        for DSU in self.DSUS:
            yield self.check_empty_union, DSU

    def test_all_distinct(self):
        for DSU in self.DSUS:
            yield self.check_xs_ys, DSU

    def test_all_the_same(
            self, xs=range(10), ys=[0 for i in range(10)]
    ):
        for DSU in self.DSUS:
            yield self.check_xs_ys, DSU, xs, ys

    def test_random(self, ns=range(1, 100)):
        for DSU, n in product(self.DSUS, ns):
            yield self.check_random, DSU, n

    def test_transitive_union(self, ns=range(2, 50)):
        for DSU, n in product(self.DSUS, ns):
            yield self.check_transitive_union, DSU, n