from typing import List

class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod = 1000000007
        stack = [(-1, 0)]
        res = 0
        cur_sum = 0
        nums.append(0)

        for num in nums:
            while stack[-1][0] >= num:
                min_val, _ = stack.pop()
                res = max(res, min_val * (cur_sum - stack[-1][1]))
            cur_sum += num
            stack.append((num, cur_sum))
        
        return res % mod

        
def main():
    sol = Solution()
    print(sol.maxSumMinProduct([1,2,3,2]))
    print(sol.maxSumMinProduct([2,3,3,1,2]))
    print(sol.maxSumMinProduct([3,1,5,6,4,2]))

if __name__ == '__main__':
    main()