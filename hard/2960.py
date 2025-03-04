from typing import List

class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        res = 0
        battery_usage = 0

        for battery in batteryPercentages:
            if battery - battery_usage > 0:
                res += 1
                battery_usage += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.countTestedDevices([1,1,2,1,3]))
    print(sol.countTestedDevices([0,1,2]))

if __name__ == '__main__':
    main()