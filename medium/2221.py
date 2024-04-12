from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        cur = nums.copy()

        for i in range(n - 1, 0, -1):
            next = [0] * i

            for j in range(len(cur) - 1):
                next[j] = cur[j] + cur[j + 1] 
            
            cur = next
        
        return cur[0] % 10

def main():
    sol = Solution()
    print(sol.triangularSum([1,2,3,4,5]))
    print(sol.triangularSum([5]))

if __name__ == '__main__':
    main()