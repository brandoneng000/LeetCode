from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned_nums = set(banned)
        cur = 0
        res = 0
        
        for i in range(1, n + 1):
            if i in banned_nums:
                continue

            if cur + i > maxSum:
                break

            cur += i
            res += 1
        
        return res

        
def main():
    sol = Solution()
    print(sol.maxCount(banned = [1,6,5], n = 5, maxSum = 6))
    print(sol.maxCount(banned = [1,2,3,4,5,6,7], n = 8, maxSum = 1))
    print(sol.maxCount(banned = [11], n = 7, maxSum = 50))

if __name__ == '__main__':
    main()