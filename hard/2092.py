from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        time_meeting = defaultdict(list)

        for x, y, t in meetings:
            time_meeting[t].append((x, y))

        visited = [False] * n
        visited[0] = True
        visited[firstPerson] = True

        for t in sorted(time_meeting):
            meetings = time_meeting[t]

            graph = defaultdict(list)

            for x, y in meetings:
                graph[x].append(y)
                graph[y].append(x)

            start = set()

            for x, y in meetings:
                if visited[x]:
                    start.add(x)
                if visited[y]:
                    start.add(y)

            q = deque(start)

            while q:
                person = q.popleft()

                for next_person in graph[person]:
                    if not visited[next_person]:
                        visited[next_person] = True
                        q.append(next_person)
        
        return [i for i in range(n) if visited[i]]

    # def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    #     secrets = set([0, firstPerson])
    #     time_map = {}

    #     for src, dst, t in meetings:
    #         if t not in time_map:
    #             time_map[t] = defaultdict(list)
            
    #         time_map[t][src].append(dst)
    #         time_map[t][dst].append(src)
        
    #     def dfs(src, adj):
    #         if src in visit:
    #             return
            
    #         visit.add(src)
    #         secrets.add(src)

    #         for nei in adj[src]:
    #             dfs(nei, adj)
            

    #     for t in sorted(time_map.keys()):
    #         visit= set()

    #         for src in time_map[t]:
    #             if src in secrets:
    #                 dfs(src, time_map[t])

    #     return list(secrets)
        
        
def main():
    sol = Solution()
    print(sol.findAllPeople(n = 5, meetings = [[1,4,3],[0,4,3]], firstPerson = 3))
    print(sol.findAllPeople(n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1))
    print(sol.findAllPeople(n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3))
    print(sol.findAllPeople(n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1))

if __name__ == '__main__':
    main()