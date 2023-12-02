from typing import List

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        divisibility = [0] * len(divisors)

        for num in nums:
            for i in range(len(divisors)):
                divisibility[i] += num % divisors[i] == 0
        
        res = float('inf')
        max_count = 0

        for i in range(len(divisors)):
            if divisibility[i] == max_count:
                res = min(res, divisors[i])
                max_count = divisibility[i]
            elif divisibility[i] > max_count:
                res =  divisors[i]
                max_count = divisibility[i]
        
        return res


        
def main():
    sol = Solution()
    print(sol.maxDivScore(nums = [4,7,9,3,9], divisors = [5,2,3]))
    print(sol.maxDivScore(nums = [20,14,21,10], divisors = [5,7,5]))
    print(sol.maxDivScore(nums = [12], divisors = [10,16]))

if __name__ == '__main__':
    main()