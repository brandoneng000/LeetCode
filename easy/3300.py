from typing import List

class Solution:
    def minElement(self, nums: List[int]) -> int:
        def digit_sum(num: int):
            res = 0

            while num:
                num, r = divmod(num, 10)
                res += r
            
            return res

        res = 10 ** 33

        for num in nums:
            res = min(res, digit_sum(num))
        
        return res

    # def minElement(self, nums: List[int]) -> int:
    #     res = 10 ** 33

    #     for num in nums:
    #         total = sum(int(digit) for digit in str(num))
    #         res = min(res, total)
        
    #     return res
        

def main():
    sol = Solution()
    print(sol.minElement([10,12,13,14]))
    print(sol.minElement([1,2,3,4]))
    print(sol.minElement([999,19,199]))

if __name__ == '__main__':
    main()