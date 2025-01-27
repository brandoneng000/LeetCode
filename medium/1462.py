from typing import List
from collections import defaultdict, deque
# import collections


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def bfs(num_courses: int, graph: defaultdict, courses_prereq: List[List[bool]]):
            for i in range(num_courses):
                q = deque([i])

                while q:
                    node = q.popleft()

                    for nei in graph[node]:
                        if not courses_prereq[i][nei]:
                            courses_prereq[i][nei] = True
                            q.append(nei)


        course_graph = defaultdict(set)
        courses_prereq = [[False] * numCourses for _ in range(numCourses)]

        for a, b in prerequisites:
            course_graph[a].add(b)

        bfs(numCourses, course_graph, courses_prereq)

        return [courses_prereq[a][b] for a, b in queries]


    # def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    #     courses = [[False] * numCourses for i in range(numCourses)]

    #     for a, b in prerequisites:
    #         courses[a][b] = True
        
    #     for k in range(numCourses):
    #         for i in range(numCourses):
    #             for j in range(numCourses):
    #                 courses[i][j] = courses[i][j] or (courses[i][k] and courses[k][j])
        
    #     return [courses[i][j] for i, j in queries]


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