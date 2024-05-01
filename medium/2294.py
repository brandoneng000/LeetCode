from typing import List
from collections import Counter

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        cur_cap = -1
        res = 0

        for num in sorted(count):
            if num > cur_cap:
                res += 1
                cur_cap = num + k
        
        return res

        
def main():
    sol = Solution()
    print(sol.partitionArray(nums = [3,6,1,2,5], k = 2))
    print(sol.partitionArray(nums = [1,2,3], k = 1))
    print(sol.partitionArray(nums = [2,2,4,5], k = 0))

if __name__ == '__main__':
    main()