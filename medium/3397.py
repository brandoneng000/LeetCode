from typing import List
from collections import Counter

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        res = set()
        cur_smallest = -float('inf')

        for num in sorted(count):
            for x in range(max(cur_smallest, num - k), num + k + 1):
                cur_smallest = x
                if x not in res:
                    res.add(x)
                    count[num] -= 1

                    if count[num] == 0:
                        break

        return len(res)
        
def main():
    sol = Solution()
    print(sol.maxDistinctElements(nums = [1,2,2,3,3,4], k = 2))
    print(sol.maxDistinctElements(nums = [4,4,4,4], k = 1))

if __name__ == '__main__':
    main()