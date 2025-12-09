from typing import List
from collections import Counter

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 1_000_000_007
        pre = Counter()
        post = Counter(nums)
        res = 0

        for num in nums:
            post[num] -= 1
            res = (res + pre[num * 2] * post[num * 2]) % mod
            pre[num] += 1

        return res



def main():
    sol = Solution()
    print(sol.specialTriplets([6,3,6]))
    print(sol.specialTriplets([0,1,0,0]))
    print(sol.specialTriplets([8,4,2,8,4]))

if __name__ == '__main__':
    main()