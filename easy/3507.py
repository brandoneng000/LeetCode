from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        res = 0

        while sorted(nums) != nums:
            min_sum = 100000
            index = [-1, -1]

            for i in range(1, len(nums)):
                total = nums[i - 1] + nums[i]
                if total < min_sum:
                    min_sum = total
                    index = [i - 1, i]
            nums[index[0]] = min_sum
            nums.pop(index[1])

            res += 1
        
        return res
        

def main():
    sol = Solution()
    print(sol.minimumPairRemoval([-2,1,2,-1,-1,-2,-2,-1,-1,1,1]))
    print(sol.minimumPairRemoval([5,2,3,1]))
    print(sol.minimumPairRemoval([1,2,2]))

if __name__ == '__main__':
    main()