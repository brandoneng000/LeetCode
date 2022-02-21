class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = 0
        final_max = nums[0]
        
        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += num
            final_max = max(final_max, cur_sum)
        
        return final_max


        

def main():
    sol = Solution()
    print(sol.maxSubArray([-2, 1, 3]))
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

if __name__ == '__main__':
    main()