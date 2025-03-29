from typing import List
from collections import deque

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        def sieve(size: int):
            prime_nums = [True] * (size + 1)
            prime_nums[0] = False
            prime_nums[1] = False

            for i in range(2, size):
                if prime_nums[i]:
                    for j in range(i * i, size + 1, i):
                        prime_nums[j] = False
            
            return [i for i in range(size + 1) if prime_nums[i]]

        def prime(num: int, prime_nums: List[int]):
            factors = 0

            for p in prime_nums:
                if p * p > num:
                    break
                
                if num % p != 0:
                    continue

                factors += 1
                while num % p == 0:
                    num //= p
                
            if num > 1:
                factors += 1
            
            return factors

        mod = 1000000007
        n = len(nums)
        prime_nums = sieve(max(nums))
        prime_scores = [0] * n
        res = 1

        for i in range(n):
            prime_scores[i] = prime(nums[i], prime_nums)

        next_dominant = [n] * n
        prev_dominant = [-1] * n
        decreasing_prime_score_stack = deque()

        for i in range(n):

            while decreasing_prime_score_stack and prime_scores[decreasing_prime_score_stack[-1]] < prime_scores[i]:
                top_index = decreasing_prime_score_stack.pop()
                next_dominant[top_index] = i
            
            if decreasing_prime_score_stack:
                prev_dominant[i] = decreasing_prime_score_stack[-1]
            
            decreasing_prime_score_stack.append(i)
        
        num_of_subarrays = [(next_dominant[i] - i) * (i - prev_dominant[i]) for i in range(n)]
        sorted_array = sorted(enumerate(nums), key=lambda x: -x[1])
        processing_index = 0

        while k > 0:
            index, num = sorted_array[processing_index]
            processing_index += 1

            operations = min(k, num_of_subarrays[index])

            res = (res * pow(num, operations, mod)) % mod

            k -= operations

        return res

        
def main():
    sol = Solution()
    print(sol.maximumScore(nums = [8,3,9,3,8], k = 2))
    print(sol.maximumScore(nums = [19,12,14,6,10,18], k = 3))

if __name__ == '__main__':
    main()