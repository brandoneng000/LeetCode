from typing import List

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def unjumble(nums: int):
            if nums == 0:
                return mapping[0]

            digits = []

            while nums:
                q, r = divmod(nums, 10)
                digits.append(r)
                nums = q
            
            res = 0
            for i in range(len(digits) - 1, -1, -1):
                res *= 10
                res += mapping[digits[i]]
            
            return res
        
        nums.sort(key=unjumble)

        return nums
        
def main():
    sol = Solution()
    print(sol.sortJumbled(mapping = [9,8,7,6,5,4,3,2,1,0], nums = [0,1,2,3,4,5,6,7,8,9]))
    print(sol.sortJumbled(mapping = [8,9,4,0,2,1,3,5,7,6], nums = [991,338,38]))
    print(sol.sortJumbled(mapping = [0,1,2,3,4,5,6,7,8,9], nums = [789,456,123]))

if __name__ == '__main__':
    main()