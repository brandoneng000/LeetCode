class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 2:
            sum = 3
        else:
            sum = ((len(nums) + 1) // 2) * (len(nums))

        for num in nums:
            sum -= num

        return sum

        
def main():
    sol = Solution()
    print(sol.missingNumber([3, 0, 1]))
    print(sol.missingNumber([0, 1]))
    print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))
    print(sol.missingNumber([8,6,4,2,3,5,7,0,1]))
    print(sol.missingNumber([0, 1, 2]))
    print(sol.missingNumber([0]))
    print(sol.missingNumber([0, 2]))


if __name__ == '__main__':
    main()