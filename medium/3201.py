from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        parity = nums[0] % 2
        odd = even = both = 0

        for num in nums:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1

            if num % 2 == parity:
                both += 1
                parity = 1 - parity
        
        return max(odd, even, both)

    # def maximumLength(self, nums: List[int]) -> int:
    #     res = 0

    #     for pattern in [[0, 0], [0, 1], [1, 0], [1, 1]]:
    #         count = 0
            
    #         for num in nums:
    #             if num % 2 == pattern[count % 2]:
    #                 count += 1
            
    #         res = max(res, count)
        
    #     return res

    # def maximumLength(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     parity = [num % 2 for num in nums]
    #     res = max(parity.count(1), parity.count(0))
    #     odd_even = 0
    #     odd_even_cur = 1
    #     even_odd = 0
    #     even_odd_cur = 0

    #     for i in range(n):
    #         if parity[i] == 0:
    #             if odd_even_cur == parity[i]:
    #                 odd_even += 1
    #                 odd_even_cur = 1
                
    #             if even_odd_cur == parity[i]:
    #                 even_odd += 1
    #                 even_odd_cur = 1
    #         else:
    #             if odd_even_cur == parity[i]:
    #                 odd_even += 1
    #                 odd_even_cur = 0
                
    #             if even_odd_cur == parity[i]:
    #                 even_odd += 1
    #                 even_odd_cur = 0

    #     return max(res, even_odd, odd_even)
        
def main():
    sol = Solution()
    print(sol.maximumLength([1,2,3,4]))
    print(sol.maximumLength([1,2,1,1,2,1,2]))
    print(sol.maximumLength([1,3]))

if __name__ == '__main__':
    main()