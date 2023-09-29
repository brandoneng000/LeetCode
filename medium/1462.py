from typing import List
import collections

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        courses = [[False] * numCourses for i in range(numCourses)]

        for a, b in prerequisites:
            courses[a][b] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    courses[i][j] = courses[i][j] or (courses[i][k] and courses[k][j])
        
        return [courses[i][j] for i, j in queries]


    # def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    #     def bfs(start: int, end: int) -> bool:
    #         q = collections.deque([start])
    #         taken = set()

    #         while q:
    #             node = q.popleft()

    #             if node == end:
    #                 return True

    #             for c in courses[node]:
    #                 if c not in taken:
    #                     taken.add(c)
    #                     q.append(c)
            
    #         return False
        
    #     courses = collections.defaultdict(set)

    #     for a, b in prerequisites:
    #         courses[a].add(b)
        
    #     return [bfs(u, v) for u, v in queries]

        
def main():
    sol = Solution()
    print(sol.checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]))
    print(sol.checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]))
    print(sol.checkIfPrerequisite(numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]))

if __name__ == '__main__':
    main()