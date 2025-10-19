import collections
from math import gcd

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add_op(s):
            res = list(s)

            for i in range(1, n, 2):
                res[i] = incremented[s[i]]

            return ''.join(res)

        def rotate_ops(s):
            return s[b:] + s[:b]
        
        def dfs(s):
            if s in seen:
                return 
            
            seen.add(s)
            dfs(add_op(s))
            dfs(rotate_ops(s))

        n = len(s)
        incremented = { str(n): str((n + a) % 10) for n in range(10) }
        seen = set()
        dfs(s)

        return min(seen)

    # def findLexSmallestString(self, s: str, a: int, b: int) -> str:
    #     n = len(s)
    #     res = s
    #     s = s + s
    #     g = gcd(b, n)

    #     for i in range(0, n, g):
    #         for j in range(10):
    #             k_limit = 0 if b % 2 == 0 else 9

    #             for k in range(k_limit + 1):
    #                 t = list(s[i: i + n])

    #                 for p in range(1, n, 2):
    #                     t[p] = str((int(t[p]) + j * a) % 10)
    #                 for p in range(0, n, 2):
    #                     t[p] = str((int(t[p]) + k * a) % 10)
    #                 t_str = ''.join(t)

    #                 if t_str < res:
    #                     res = t_str
            
    #     return res


    # def findLexSmallestString(self, s: str, a: int, b: int) -> str:
    #     n = len(s)
    #     q = collections.deque([s])
    #     visited = set()
    #     res = s

    #     while q:
    #         node = q.popleft()

    #         if node in visited:
    #             continue
            
    #         visited.add(node)
    #         res = min(res, node)
    #         q.append(node[b:] + node[:b])
    #         cur = list(node)

    #         for i in range(1, n, 2):
    #             cur[i] = str((int(cur[i]) + a) % 10)
            
    #         q.append("".join(cur))
        
    #     return res

def main():
    sol = Solution()
    print(sol.findLexSmallestString(s = "5525", a = 9, b = 2))
    print(sol.findLexSmallestString(s = "74", a = 5, b = 1))
    print(sol.findLexSmallestString(s = "0011", a = 4, b = 2))

if __name__ == '__main__':
    main()