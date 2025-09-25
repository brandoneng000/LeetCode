from typing import List

class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        double_digits = 0
        single_digits = 0

        for num in nums:
            if num < 10:
                single_digits += num
            else:
                double_digits += num
        
        return single_digits != double_digits
        
def main():
    sol = Solution()
    print(sol.canAliceWin([1,2,3,4,10]))
    print(sol.canAliceWin([1,2,3,4,5,14]))
    print(sol.canAliceWin([5,5,5,25]))

if __name__ == '__main__':
    main()