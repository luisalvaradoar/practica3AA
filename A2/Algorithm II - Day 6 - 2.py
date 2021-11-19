class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n
        
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            less, more = (ry, rx) if self.size[rx] > self.size[ry] else (rx, ry)
            self.parent[less] = more
            self.size[more] += self.size[less]
            self.count -= 1

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))
        for i, connections in enumerate(isConnected):
            for j, connected in enumerate(connections):
                connected and uf.union(i, j)
        
        return uf.count