from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_con = 0
        cur_con = 0
        for num in nums:
            cur_con += num
            if cur_con > max_con:
                max_con = cur_con
            if num == 0:
                cur_con = 0

        return max_con 

def main():
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))

if __name__ == '__main__':
    main()