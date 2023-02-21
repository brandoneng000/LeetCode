class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        
        nums = {}

        nums[0] = 0
        nums[1] = 1

        for index in range(2, n + 1):
            if index % 2:
                i = (index - 1) // 2
                nums[index] = nums[i] + nums[i + 1]
            else:
                nums[index] = nums[index // 2]

        return max(nums.values())

def main():
    sol = Solution()
    print(sol.getMaximumGenerated(7))
    print(sol.getMaximumGenerated(2))
    print(sol.getMaximumGenerated(3))
    print(sol.getMaximumGenerated(100))

if __name__ == '__main__':
    main()