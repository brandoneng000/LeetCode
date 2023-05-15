from typing import List
import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        heaters.append(float('inf'))
        houses.sort()
        res = heater_index = 0
        for house in houses:
            while house >= sum(heaters[heater_index: heater_index + 2]) / 2:
                heater_index += 1
            
            res = max(res, abs(heaters[heater_index] - house))
        
        return res
    
def main():
    sol = Solution()
    print(sol.findRadius(houses = [1,2,3], heaters = [2]))
    print(sol.findRadius(houses = [1,2,3,4], heaters = [1,4]))
    print(sol.findRadius(houses = [1,5], heaters = [2]))
    print(sol.findRadius(houses = [1,1,1,1,1,1,999,999,999,999,999], heaters = [499, 500, 501]))

if __name__ == '__main__':
    main()