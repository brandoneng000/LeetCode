from typing import List

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return 0
        
        res = 0
        for i in range(len(nums) - 1, 1, -1):
            for j in range(i - 1, 0, -1):
                for k in range(j - 1, -1, -1):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                        res += 1
        
        return res


def main():
    sol = Solution()
    print(sol.unequalTriplets([4,4,2,4,3]))
    print(sol.unequalTriplets([1,1,1,1,1]))

if __name__ == '__main__':
    main()