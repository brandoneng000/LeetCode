from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        result = 0

        for index in range(len(startTime)):
            result += startTime[index] <= queryTime <= endTime[index]
        
        return result

def main():
    sol = Solution()
    print(sol.busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4))
    print(sol.busyStudent(startTime = [4], endTime = [4], queryTime = 4))

if __name__ == '__main__':
    main()