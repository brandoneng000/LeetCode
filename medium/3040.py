from typing import List

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        def dp(l: int, r: int, score: int):
            if l >= r:
                return 0
            
            if (l, r) not in cache:
                ops1 = 1 + dp(l + 2, r, score) if score == nums[l] + nums[l + 1] else 0
                ops2 = 1 + dp(l, r - 2, score) if score == nums[r] + nums[r - 1] else 0
                ops3 = 1 + dp(l + 1, r - 1, score) if score == nums[l] + nums[r] else 0

                cache[(l, r)] = max(ops1, ops2, ops3)
            
            return cache[(l, r)]
        
        n = len(nums)
        cache = {}
        l = 0
        r = n - 1

        ops1 = dp(l + 2, r, nums[l] + nums[l + 1]) + 1
        ops2 = dp(l, r - 2, nums[r] + nums[r - 1]) + 1
        ops3 = dp(l + 1, r - 1, nums[l] + nums[r]) + 1

        return max(ops1, ops2, ops3)


def main():
    sol = Solution()
    print(sol.maxOperations([3,2,1,2,3,4]))
    print(sol.maxOperations([3,2,6,1,4]))

if __name__ == '__main__':
    main()