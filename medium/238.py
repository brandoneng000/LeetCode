from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)

        pre = 1
        for num in range(len(nums)):
            products[num] = pre
            pre *= nums[num]
            
        post = 1
        for num in range(len(nums) - 1, -1, -1):
            products[num] = products[num] * post
            post *= nums[num]
            
        return products



def main():
    sol = Solution()
    nums_one = [1,2,3,4]
    nums_two = [-1,1,0,-3,3]
    print(sol.productExceptSelf(nums_one))
    print(sol.productExceptSelf(nums_two))
    

if __name__ == '__main__':
    main()