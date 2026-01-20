from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        cache = { 2: -1 }
        max_num = max(nums)

        for i in range(1, max_num):
            val = i | (i + 1)
            if val not in cache:
                cache[val] = i

        return [cache[num] for num in nums]
        
def main():
    sol = Solution()
    print(sol.minBitwiseArray([2,3,5,7]))
    print(sol.minBitwiseArray([11,13,31]))

if __name__ == '__main__':
    main()