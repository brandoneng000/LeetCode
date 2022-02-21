from calendar import c


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_min, cur_max = 1, 1
        res = max(nums)

        for num in nums:
            if num == 0:
                cur_min, cur_max = 1, 1
                continue
            temp_max = cur_max
            cur_max = max(num * cur_max, num * cur_min, num)
            cur_min = min(num * temp_max, num * cur_min, num)
            res = max(cur_max, res)
        
        return res


        # def calcProd(nums, index, prod, max_prod):
        #     if prod > max_prod:
        #         max_prod = prod
        #     if index == len(nums):
        #         return prod
            

        #     left = calcProd(nums, index+1, prod*nums[index], max_prod)
        #     right = calcProd(nums, index+1, nums[index], max_prod)

        #     return max(left, right, max_prod)

        # return calcProd(nums, 1, nums[0], nums[0])

        

def main():
    sol = Solution()
    print(sol.maxProduct([2,3, -2, 4]))
    print(sol.maxProduct([-2, 0, -1]))
    print(sol.maxProduct([1,3,1,-1,-3,-2,-3,6,0,1,4,-1,3,-3,-1,0,6,5,1,-4]))
    print(sol.maxProduct([2,-5,-2,-4,3]))

if __name__ == '__main__':
    main()