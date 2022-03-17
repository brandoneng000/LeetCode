from typing import List

class Solution:
    
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def threeSum(nums: List[int], target: int):
            nums.sort()
            res = []

            for index, val in enumerate(nums):
                if index > 0 and val == nums[index - 1]:
                    continue
                
                left, right = index + 1, len(nums) - 1
                while left < right:
                    three_sum = val + nums[left] + nums[right]
                    if three_sum > target:
                        right -= 1
                    elif three_sum < target:
                        left += 1
                    else:
                        res.append([val, nums[left], nums[right]])
                        left += 1
                        while nums[left] == nums[left - 1] and left < right:
                            left += 1
            return res
        
        ans = set()
        nums.sort()

        for index, num in enumerate(nums):
            three_list = nums[:index] + nums[index + 1:]
            three_sum_list = threeSum(three_list, target - num)
            # print(three_sum_list)
            for sol in three_sum_list:
                sol += [num]
                sol.sort()
                ans.add(tuple(sol))

        return list(ans)



def main():
    sol = Solution()
    print(sol.fourSum([1,0,-1,0,-2,2], 0))

if __name__ == '__main__':
    main()