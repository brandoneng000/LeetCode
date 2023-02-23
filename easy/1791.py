from typing import List
import collections

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # connections = collections.defaultdict(list)

        # for edge in edges:
        #     connections[edge[0]].append(edge[1])
        #     connections[edge[1]].append(edge[0])

        # return max(connections.items(), key=lambda x:len(x[1]))[0]

        if edges[0][0] in edges[1]:
            return edges[0][0]
        return edges[0][1]

def main():
    sol = Solution()
    print(sol.findCenter([[1,2],[2,3],[4,2]]))
    print(sol.findCenter([[1,2],[5,1],[1,3],[1,4]]))

if __name__ == '__main__':
    main()