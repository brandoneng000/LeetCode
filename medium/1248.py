from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(k: int):
            res = i = 0

            for j in range(len(nums)):
                k -= nums[j] % 2
                while k < 0:
                    k += nums[i] % 2
                    i += 1
                res += j - i + 1
            
            return res

        return helper(k) - helper(k - 1)

def main():
    sol = Solution()
    print(sol.numberOfSubarrays(nums = [1,1,2,1,1], k = 3))
    print(sol.numberOfSubarrays(nums = [2,4,6], k = 1))
    print(sol.numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))

if __name__ == '__main__':
    main()