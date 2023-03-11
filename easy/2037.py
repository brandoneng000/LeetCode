from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        result = 0

        for index in range(len(seats)):
            result += abs(seats[index] - students[index])

        return result
            

def main():
    sol = Solution()
    print(sol.minMovesToSeat(seats = [3,1,5], students = [2,7,4]))
    print(sol.minMovesToSeat(seats = [4,1,5,9], students = [1,3,2,6]))
    print(sol.minMovesToSeat(seats = [2,2,6,6], students = [1,3,2,6]))

if __name__ == '__main__':
    main()