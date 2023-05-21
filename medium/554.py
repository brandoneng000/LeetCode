from typing import List
import collections

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges = collections.defaultdict(int)

        for row in wall:
            edge = 0
            for brick in row[:-1]:
                edge += brick
                edges[edge] += 1

        return len(wall) - max(edges.values(), default=0)

        
def main():
    sol = Solution()
    print(sol.leastBricks([[1,1],[2],[1,1]]))
    print(sol.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
    print(sol.leastBricks([[1],[1],[1]]))

if __name__ == '__main__':
    main()