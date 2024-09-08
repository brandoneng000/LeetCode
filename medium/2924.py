from typing import List

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        visited = set()

        for u, v in edges:
            visited.add(v)
        
        res = set(range(n)) - visited
        
        if len(res) > 1:
            return -1
        
        return res.pop()
        
        
def main():
    sol = Solution()
    print(sol.findChampion(n = 3, edges = [[0,1],[1,2]]))
    print(sol.findChampion(n = 4, edges = [[0,2],[1,3],[1,2]]))

if __name__ == '__main__':
    main()