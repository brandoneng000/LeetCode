from math import log

class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def price(num: int):
            left_most_bit = int(log(num, 2) + 1)
            num += 1
            res = 0

            for i in range(x, left_most_bit + 1, x):
                block_size = 2 ** i
                num_blocks = num // block_size
                full_blocks_one = num_blocks * (block_size // 2)
                remainder_ones = max(0, (num % block_size) - (block_size // 2))
                res += full_blocks_one + remainder_ones
            
            return res
        
        left = 1
        right = 10 ** 15
        
        while left <= right:
            middle = (left + right) // 2

            if price(middle) <= k:
                left = middle + 1
            else:
                right = middle - 1
        
        return left - 1

        
def main():
    sol = Solution()
    print(sol.findMaximumNumber(k = 9, x = 1))
    print(sol.findMaximumNumber(k = 7, x = 2))

if __name__ == '__main__':
    main()