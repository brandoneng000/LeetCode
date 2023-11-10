from typing import List
from collections import defaultdict, deque

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacents = defaultdict(list)
        visited = set()
        res = []

        for x, y in adjacentPairs:
            adjacents[x].append(y)
            adjacents[y].append(x)

        for num in adjacents:
            if len(adjacents[num]) == 1:
                start = num
                break
        
        q = deque([start])

        while q:
            node = q.popleft()
            
            for num in adjacents[node]:
                if num not in visited:
                    q.append(num)

            visited.add(node)
            res.append(node)

        return res

        
def main():
    sol = Solution()
    print(sol.restoreArray([[2,1],[3,4],[3,2]]))
    print(sol.restoreArray([[4,-2],[1,4],[-3,1]]))
    print(sol.restoreArray([[100000,-100000]]))

if __name__ == '__main__':
    main()