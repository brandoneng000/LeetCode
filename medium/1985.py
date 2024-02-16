from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums_val = sorted([int(num) for num in nums], reverse=True)
        return str(nums_val[k - 1])
        
def main():
    sol = Solution()
    print(sol.kthLargestNumber(nums = ["3","6","7","10"], k = 4))
    print(sol.kthLargestNumber(nums = ["2","21","12","1"], k = 3))
    print(sol.kthLargestNumber(nums = ["0","0"], k = 2))

if __name__ == '__main__':
    main()