from typing import List
from collections import Counter, defaultdict

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        def count_nodes(node: int):
            p, s = 1, 0

            for child in graph[node]:
                res = count_nodes(child)
                p *= res
                s += res
            
            p *= max(1, n - 1 - s)
            total[p] += 1
            return s + 1
            
        
        n = len(parents)
        total = Counter()
        graph = defaultdict(list)

        for i, p in enumerate(parents):
            graph[p].append(i)
        
        count_nodes(0)
        return total[max(total)]
        
        
def main():
    sol = Solution()
    print(sol.countHighestScoreNodes([-1,2,0,2,0]))
    print(sol.countHighestScoreNodes([-1,2,0]))

if __name__ == '__main__':
    main()