from typing import List
import collections

class Solution:
    def union(self, a, b):
        self.parent[(self.find(a))] = self.find(b)

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        
        return self.parent[a]

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.parent = list(range(len(s)))
        
        for a, b in pairs:
            self.union(a, b)

        groups = collections.defaultdict(lambda: ([], []))
        for i, c in enumerate(s):
            parent = self.find(i)
            groups[parent][0].append(i)
            groups[parent][1].append(c)
        
        res = [''] * len(s)
        for indexes, chars in groups.values():
            for i, c in zip(sorted(indexes), sorted(chars)):
                res[i] = c
        
        return "".join(res)

    # def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
    #     disjointed_sets = collections.defaultdict(set)
    #     q = collections.deque()
    #     visited = set()
    #     res = list(s)

    #     for a, b in pairs:
    #         disjointed_sets[a].add(b)
    #         disjointed_sets[b].add(a)

    #     for key in disjointed_sets:
    #         if key in visited:
    #             continue

    #         q.append(key)
    #         visited.add(key)
    #         indexes = []

    #         while q:
    #             size = len(q)

    #             for _ in range(size):
    #                 letter = q.popleft()
    #                 indexes.append(letter)

    #                 for c in disjointed_sets[letter]:
    #                     if c not in visited:
    #                         q.append(c)
    #                         visited.add(c)
            
    #         characters = [s[i] for i in indexes]
    #         for i, c in zip(sorted(indexes), sorted(characters)):
    #             res[i] = c

    #     return "".join(res)

def main():
    sol = Solution()
    print(sol.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2]]))
    print(sol.smallestStringWithSwaps(s = "dcab", pairs = [[0,3],[1,2],[0,2]]))
    print(sol.smallestStringWithSwaps(s = "cba", pairs = [[0,1],[1,2]]))

if __name__ == '__main__':
    main()