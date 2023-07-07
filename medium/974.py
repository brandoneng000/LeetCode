from typing import List

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        
        remainders = [0] * k
        remainders[0] = 1
        
        for num in nums:
            prefix = (prefix + num % k + k) % k
            res += remainders[prefix]
            remainders[prefix] += 1

        return res

def main():
    sol = Solution()
    print(sol.subarraysDivByK(nums = [4,5,0,-2,-3,1], k = 5))
    print(sol.subarraysDivByK(nums = [5], k = 9))

if __name__ == '__main__':
    main()