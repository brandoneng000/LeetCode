from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        def original(n: List[int]):
            rob1, rob2 = 0, 0

            for index in range(len(n)):
                temp = max(rob1 + n[index], rob2)
                rob1 = rob2
                rob2 = temp

            return rob2
        
        return max(nums[0], original(nums[:-1]), original(nums[1:]))

def main():
    sol = Solution()
    print(sol.rob([2,3,2]))
    print(sol.rob([1,2,3,1]))
    print(sol.rob([200,3,140,20,10]))
    print(sol.rob([1,2,1,1]))


if __name__ == '__main__':
    main()