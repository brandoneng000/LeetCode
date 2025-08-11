from typing import List
from collections import Counter

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hours = [h % 24 for h in hours]
        count_hours = Counter()
        res = 0

        for h in hours:
            res += count_hours[(24 - h) % 24]
            count_hours[h] += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.countCompleteDayPairs([12,12,30,24,24]))
    print(sol.countCompleteDayPairs([72,48,24,3]))

if __name__ == '__main__':
    main()