from typing import List
import collections
import string

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        parent = { a: a for a in string.ascii_lowercase }
        for a, e, _, b in equations:
            if e == '=':
                parent[find(a)] = find(b)

        return not any(e == '!' and find(a) == find(b) for a, e, _, b in equations)
            

    # def equationsPossible(self, equations: List[str]) -> bool:
    #     equals = collections.defaultdict(set)
    #     not_equals = []

    #     for equ in equations:
    #         if equ[1] == '=':
    #             equals[equ[0]].add(equ[3])
    #             equals[equ[3]].add(equ[0])
    #         else:
    #             not_equals.append([equ[0], equ[3]])
        
    #     def traverse(visited: set, start: str, goal: str):
    #         if start == goal:
    #             return True

    #         res = False
    #         visited.add(start)
    #         for node in equals[start]:
    #             if node not in visited:
    #                 res = res or traverse(visited, node, goal)
            
    #         return res

    #     return not any(traverse(set(), start, goal) for start, goal in not_equals)

def main():
    sol = Solution()
    print(sol.equationsPossible(["a==b","c!=a","b==c"]))
    print(sol.equationsPossible(["a==b","b!=a"]))
    print(sol.equationsPossible(["b==a","a==b"]))

if __name__ == '__main__':
    main()