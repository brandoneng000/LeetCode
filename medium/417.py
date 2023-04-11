from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # pacific = (0, 0)
        # atlantic = (len(heights) - 1, len(heights[0]) - 1)
        # visited = set()
        # res = []
        # cache_pacific = {}
        # cache_atlantic = {}

        # def to_ocean(heights: List[List[int]], visited: set, ocean: tuple, x: int, y: int) -> bool:
        #     if x == ocean[0] or y == ocean[1]:
        #         return True
        #     if ocean == pacific and (x, y) in cache_pacific:
        #         return cache_pacific[(x, y)]
        #     elif ocean == atlantic and (x, y) in cache_atlantic:
        #         return cache_atlantic[(x, y)]
            
        #     reach_ocean = False
        #     visited.add((x, y))
        #     for dir_x, dir_y in directions:
        #         visiting_x = x + dir_x
        #         visiting_y = y + dir_y
        #         if (-1 < visiting_x < len(heights) and -1 < visiting_y < len(heights[0])) \
        #             and (visiting_x, visiting_y) not in visited and heights[visiting_x][visiting_y] <= heights[x][y]:

        #             reach_ocean = to_ocean(heights, visited, ocean, visiting_x, visiting_y)
        #             if reach_ocean:
        #                 break

        #     visited.remove((x, y))
        #     return reach_ocean
        
        # for r in range(len(heights)):
        #     for c in range(len(heights[0])):

        #         cache_pacific[(r, c)] = to_ocean(heights, visited, pacific, r, c)
        #         cache_atlantic[(r, c)] = to_ocean(heights, visited, atlantic, r, c)

        #         if cache_pacific[(r, c)] and cache_atlantic[(r, c)]:
        #             res.append([r, c])
        
        # return res
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(heights), len(heights[0])
        visited_pacific = set()
        visited_atlantic = set()

        def dfs(visited: set, x: int, y: int):
            visited.add((x, y))
            for dir_x, dir_y in directions:
                visit_x, visit_y = x + dir_x, y + dir_y
                if -1 < visit_x < m and -1 < visit_y < n \
                    and (visit_x, visit_y) not in visited \
                    and heights[visit_x][visit_y] >= heights[x][y]:

                    dfs(visited, visit_x, visit_y)
        
        for i in range(m):
            dfs(visited_pacific, i, 0)
            dfs(visited_atlantic, i, n - 1)
        
        for j in range(n):
            dfs(visited_pacific, 0, j)
            dfs(visited_atlantic, m - 1, j)
        
        return list(visited_atlantic.intersection(visited_pacific))
        

def main():
    sol = Solution()
    print(sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
    print(sol.pacificAtlantic([[1]]))

if __name__ == '__main__':
    main()