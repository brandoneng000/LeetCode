from typing import List

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        left = min(bloomDay)
        right = max(bloomDay)

        while left < right:
            middle = (left + right) // 2
            
            flowers = bouq = 0

            for f in bloomDay:
                flowers = 0 if f > middle else flowers + 1
                if flowers >= k:
                    flowers = 0
                    bouq += 1
                    if bouq == m:
                        break
            
            if bouq == m:
                right = middle
            else:
                left = middle + 1
        
        return left


        
def main():
    sol = Solution()
    print(sol.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1))
    print(sol.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 2))
    print(sol.minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3))

if __name__ == '__main__':
    main()