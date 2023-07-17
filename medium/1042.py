from typing import List
import collections

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        res = [0] * n
        graph = [[] for i in range(n)]

        for x, y in paths:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)
        
        for i in range(n):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in graph[i]}).pop()
        
        return res

    # def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
    #     RED, GREEN, BLUE, BLACK = 1, 2, 3, 4
    #     garden_paths = collections.defaultdict(list)
    #     q = collections.deque()
    #     flowers = [-1] * n

    #     for x, y in paths:
    #         garden_paths[x - 1].append(y - 1)
    #         garden_paths[y - 1].append(x - 1)
        
    #     for i in range(n):
    #         if flowers[i] == -1:
    #             q.append(i)

    #         while q:
    #             garden = q.popleft()
    #             available = { RED, GREEN, BLUE, BLACK }

    #             for adj in garden_paths[garden]:
    #                 if flowers[adj] != -1:
    #                     available -= { flowers[adj] }
    #                 else:
    #                     q.append(adj)
                
    #             flowers[garden] = available.pop()
        
    #     return flowers

def main():
    sol = Solution()
    print(sol.gardenNoAdj(n = 3, paths = [[1,2],[2,3],[3,1]]))
    print(sol.gardenNoAdj(n = 4, paths = [[1,2],[3,4]]))
    print(sol.gardenNoAdj(n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]))

if __name__ == '__main__':
    main()