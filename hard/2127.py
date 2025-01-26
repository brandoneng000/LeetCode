from typing import List
from collections import defaultdict, deque

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        def bfs(start: int, visited: set, graph: defaultdict):
            q = deque([(start, 0)])
            max_dist = 0

            while q:
                cur_node, cur_dist = q.popleft()

                for nei in graph[cur_node]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    q.append((nei, cur_dist + 1))
                    max_dist = max(max_dist, cur_dist + 1)
            
            return max_dist


        n = len(favorite)
        graph = defaultdict(list)

        for i in range(n):
            graph[favorite[i]].append(i)

        longest_cycle = 0
        two_cycle_invitation = 0
        visited = [False] * n

        for person in range(n):
            if not visited[person]:
                visited_persons = {}
                cur_person = person
                dist = 0

                while True:
                    if visited[cur_person]:
                        break

                    visited[cur_person] = True
                    visited_persons[cur_person] = dist
                    dist += 1
                    next_person = favorite[cur_person]

                    if next_person in visited_persons:
                        cycle_len = dist - visited_persons[next_person]
                        longest_cycle = max(longest_cycle, cycle_len)
                        
                        if cycle_len == 2:
                            visited_nodes = {cur_person, next_person}
                            two_cycle_invitation += (
                                2
                                + bfs(next_person, visited_nodes, graph)
                                + bfs(cur_person, visited_nodes, graph)
                                
                            )
                        break
                    cur_person = next_person
        
        return max(longest_cycle, two_cycle_invitation)
        
def main():
    sol = Solution()
    print(sol.maximumInvitations([2,2,1,2]))
    print(sol.maximumInvitations([1,2,0]))
    print(sol.maximumInvitations([3,0,1,4,1]))

if __name__ == '__main__':
    main()