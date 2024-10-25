from typing import List

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def update_bits(bits: List[int], num: int, change: int):
            for i in range(32):
                if (num >> i) & 1:
                    bits[i] += change

        def bits_to_num(bits: List[int]):
            res = 0

            for i in range(32):
                if bits[i]:
                    res |= 1 << i
                
            return res

        n = len(nums)
        res = float('inf')
        bits = [0] * 32
        left = 0

        for right in range(n):
            update_bits(bits, nums[right], 1)

            while left <= right and bits_to_num(bits) >= k:
                res = min(res, right - left + 1)
                update_bits(bits, nums[left], -1)
                left += 1

        return res if res != float('inf') else -1


        
def main():
    sol = Solution()
    print(sol.minimumSubarrayLength(nums = [2,1,6,32,86,56], k = 2222))
    print(sol.minimumSubarrayLength(nums = [1,2,3], k = 2))
    print(sol.minimumSubarrayLength(nums = [2,1,8], k = 10))
    print(sol.minimumSubarrayLength(nums = [1,2], k = 0))

if __name__ == '__main__':
    main()