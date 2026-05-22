from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def find_divisor(num1: int, num2: int):
            for i in range(2, num1 + 1):
                if num2 % i == 0:
                    return i
            
            return -1

        n = len(nums)
        res = 0

        for i in range(n - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                nums[i - 1] = find_divisor(nums[i], nums[i - 1])

                if nums[i - 1] == -1:
                    return -1
                
                res += 1
        
        return res

        
def main():
    sol = Solution()
    print(sol.minOperations([25,7]))
    print(sol.minOperations([7,7,6]))
    print(sol.minOperations([1,1,1,1]))

if __name__ == '__main__':
    main()