from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        used = set()
        res = 0

        for i in range(n):
            cur = 0
            temp = []
            for j in range(i, n):
                cur += nums[j] % p == 0
                temp.append(nums[j])
                if cur > k:
                    break
                temp_tup = tuple(temp)
                if temp_tup not in used:
                    used.add(temp_tup)
                    res += 1
        
        return res
        
def main():
    sol = Solution()
    print(sol.countDistinct(nums = [2,3,3,2,2], k = 2, p = 2))
    print(sol.countDistinct(nums = [1,2,3,4], k = 4, p = 1))

if __name__ == '__main__':
    main()