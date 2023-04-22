from typing import List
import collections

class Solution:
    WHITE = 1
    GRAY = 2
    BLACK = 3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = collections.defaultdict(list)
        for c, p in prerequisites:
            adj_list[p].append(c)
        
        taken = []
        self.not_cycle = True

        color = { k: Solution.WHITE for k in range(numCourses)}
        def dfs(node):
            if not self.not_cycle:
                return
            color[node] = Solution.GRAY

            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                        self.not_cycle = False
            color[node] = Solution.BLACK
            taken.append(node)
        
        for course in range(numCourses):
            if color[course] == Solution.WHITE:
                dfs(course)
        
        return taken[::-1] if self.not_cycle else []



def main():
    sol = Solution()
    print(sol.findOrder(numCourses = 2, prerequisites = [[1,0]]))
    print(sol.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))
    print(sol.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2],[2,3]]))
    print(sol.findOrder(numCourses = 1, prerequisites = []))

if __name__ == '__main__':
    main()