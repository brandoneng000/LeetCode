from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = set(range(0, n))

        for u, v in edges:
            res.discard(v)
        
        return res

    # def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
    #     in_degree = [0] * n

    #     for u, v in edges:
    #         in_degree[v] += 1
        
    #     return [i for i in range(n) if in_degree[i] == 0]


        
def main():
    sol = Solution()
    print(sol.findSmallestSetOfVertices(n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]))
    print(sol.findSmallestSetOfVertices(n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]))

if __name__ == '__main__':
    main()