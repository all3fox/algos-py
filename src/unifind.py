class UnionFind:
    def __init__(self, it=None):
        self.uf = {} if it is None else {i : i for i in it}

        self.count = len(self.uf)

    def __iter__(self):
        return iter(self.uf.keys())

    def __getitem__(self, key):
        return self.uf[key]

    def __setitem__(self, key, val):
        if key is not val:
            raise RuntimeError("key and val must be the same object")

        self.uf[key] = key

class QuickFind(UnionFind):
    def find(self, key):
        return self.uf[key]

    def union(self, key1, key2):
        u1 = self.find(key1)
        u2 = self.find(key2)

        if u1 == u2: return

        for k in self.uf:
            if self.uf[k] == u1:
                self.uf[k] = u2

        self.count -= 1

class QuickUnion(UnionFind):
    def find(self, key):
        while self.uf[key] != key:
            key = self.uf[key]

        return key

    def union(self, key1, key2):
        u1 = self.find(key1)
        u2 = self.find(key2)

        if u1 == u2: return

        self.uf[u1] = u2

        self.count -= 1