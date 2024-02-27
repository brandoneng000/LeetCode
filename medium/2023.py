from typing import List
from collections import Counter

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        nums_count = Counter(nums)
        res = 0

        for num in nums_count:
            if target.startswith(num):
                goal = target[len(num):]
                if goal == num:
                    res += nums_count[num] * (nums_count[goal] - 1)
                else:
                    res += nums_count[num] * nums_count[goal]
        
        return res
        
def main():
    sol = Solution()
    print(sol.numOfPairs(nums = ["777","7","77","77"], target = "7777"))
    print(sol.numOfPairs(nums = ["123","4","12","34"], target = "1234"))
    print(sol.numOfPairs(nums = ["1","1","1"], target = "11"))

if __name__ == '__main__':
    main()