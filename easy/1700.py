from typing import List
import collections

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        orders = collections.Counter(students)
        i = 0

        while i < n and orders[sandwiches[i]]:
            orders[sandwiches[i]] -= 1
            i += 1
        
        return n - i
        

    # def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    #     count = 0
        
    #     while students:
    #         if students[0] != sandwiches[0]:
    #             students.append(students.pop(0))
    #             count += 1
    #             if count == len(students):
    #                 return count
    #         else:
    #             students.pop(0)
    #             sandwiches.pop(0)
    #             count = 0
        
    #     return count
    
    # def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    #     students = collections.Counter(students)

    #     for sandwich in sandwiches:
    #         if students[sandwich] == 0:
    #             break
    #         students[sandwich] -= 1
        
    #     return students[0] + students[1]
        

def main():
    sol = Solution()
    print(sol.countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1]))
    print(sol.countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))

if __name__ == '__main__':
    main()