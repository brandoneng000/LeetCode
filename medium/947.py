from typing import List
import collections

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph_x = collections.defaultdict(list)
        graph_y = collections.defaultdict(list)
        visited = set()

        for x, y in stones:
            graph_x[x].append(y)
            graph_y[y].append(x)
        
        def traverse(x, y):
            visited.add((x, y))
            for cur_y in graph_x[x]:
                if (x, cur_y) not in visited:
                    traverse(x, cur_y)
            
            for cur_x in graph_y[y]:
                if (cur_x, y) not in visited:
                    traverse(cur_x, y)
        
        res = 0

        for x, y in stones:
            if (x, y) not in visited:
                res += 1
                traverse(x, y)
        
        return len(stones) - res


def main():
    sol = Solution()
    print(sol.removeStones([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]))
    print(sol.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))
    print(sol.removeStones([[0,0]]))

if __name__ == '__main__':
    main()