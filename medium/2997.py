from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        for num in nums:
            k ^= num
        
        return k.bit_count()

    # def minOperations(self, nums: List[int], k: int) -> int:
    #     bit_count = [0] * 20
    #     res = 0

    #     for num in nums:
    #         for bit in range(20):
    #             bit_count[bit] += (num >> bit) & 1
        
    #     k_bits = f'{k:020b}'[::-1]

    #     for c, b in zip(bit_count, k_bits):
    #         res += (c % 2) != int(b)
        
    #     return res
        
        
def main():
    sol = Solution()
    print(sol.minOperations(nums = [2,1,3,4], k = 1))
    print(sol.minOperations(nums = [2,0,2,0], k = 0))

if __name__ == '__main__':
    main()