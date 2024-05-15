from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def helper(node: int, edges: List[int], dist: List[int]):
            cur_dist = 0
            while node != -1 and dist[node] == -1:
                dist[node] = cur_dist
                cur_dist += 1
                node = edges[node]
        
        n = len(edges)
        res = -1
        min_dist = float('inf')
        distance1 = [-1] * n
        distance2 = [-1] * n

        helper(node1, edges, distance1)
        helper(node2, edges, distance2)

        for i in range(n):
            if min(distance1[i], distance2[i]) >= 0 and max(distance1[i], distance2[i]) < min_dist:
                min_dist = max(distance1[i], distance2[i])
                res = i
        
        return res
        
def main():
    sol = Solution()
    print(sol.closestMeetingNode(edges = [4,3,0,5,3,-1], node1 = 4, node2 = 0))
    print(sol.closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1))
    print(sol.closestMeetingNode(edges = [1,2,-1], node1 = 0, node2 = 2))

if __name__ == '__main__':
    main()