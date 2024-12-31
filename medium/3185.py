from typing import List

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        day = [0] * 24
        res = 0

        for hour in hours:
            day[hour % 24] += 1
        
        for h in range(1, 12):
            res += day[h] * day[24 - h]
        
        res += day[0] * (day[0] - 1) // 2
        res += day[12] * (day[12] - 1) // 2

        return res
        
def main():
    sol = Solution()
    print(sol.countCompleteDayPairs([12,12,30,24,24]))
    print(sol.countCompleteDayPairs([72,48,24,3]))

if __name__ == '__main__':
    main()