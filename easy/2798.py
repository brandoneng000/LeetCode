from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum(h >= target for h in hours)
        
def main():
    sol = Solution()
    print(sol.numberOfEmployeesWhoMetTarget(hours = [0,1,2,3,4], target = 2))
    print(sol.numberOfEmployeesWhoMetTarget(hours = [5,1,4,2,2], target = 6))

if __name__ == '__main__':
    main()