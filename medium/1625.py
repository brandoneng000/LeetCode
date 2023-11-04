import collections

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        q = collections.deque([s])
        visited = set()
        res = s

        while q:
            node = q.popleft()

            if node in visited:
                continue
            
            visited.add(node)
            res = min(res, node)
            q.append(node[b:] + node[:b])
            cur = list(node)

            for i in range(1, n, 2):
                cur[i] = str((int(cur[i]) + a) % 10)
            
            q.append("".join(cur))
        
        return res

def main():
    sol = Solution()
    print(sol.findLexSmallestString(s = "5525", a = 9, b = 2))
    print(sol.findLexSmallestString(s = "74", a = 5, b = 1))
    print(sol.findLexSmallestString(s = "0011", a = 4, b = 2))

if __name__ == '__main__':
    main()