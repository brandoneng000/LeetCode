from typing import List
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_taken = [False] * numCourses
        rec_stack = [False] * numCourses
        classes = collections.defaultdict(list)
        for course, prereq in prerequisites:
            classes[prereq].append(course)
        
        def check_courses(course: int, courses_taken: List[bool], rec_stack: List[bool], classes: dict):
            courses_taken[course] = True
            rec_stack[course] = True

            for c in classes[course]:
                if not courses_taken[c]:
                    if check_courses(c, courses_taken, rec_stack, classes):
                        return True
                elif rec_stack[c]:
                    return True
            
            rec_stack[course] = False
            return False
        
        for c in range(numCourses):
            if not courses_taken[c]:
                if check_courses(c, courses_taken, rec_stack, classes):
                    return False
        
        return True
            

        
def main():
    sol = Solution()
    print(sol.canFinish(numCourses = 2, prerequisites = [[1,0]]))
    print(sol.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))

if __name__ == '__main__':
    main()