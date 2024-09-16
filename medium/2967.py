from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        def check_palindrome(num: str):
            return num == num[::-1]

        n = len(nums)
        nums.sort()
        median = nums[n // 2]

        if check_palindrome(str(median)):
            return sum(abs(median - num) for num in nums)

        smaller = median - 1
        larger = median + 1

        while not check_palindrome(str(smaller)):
            smaller -= 1

        while not check_palindrome(str(larger)):
            larger += 1
        
        return min(sum(abs(smaller - num) for num in nums), sum(abs(larger - num) for num in nums))


        
def main():
    sol = Solution()
    print(sol.minimumCost([1,2,3,4,5]))
    print(sol.minimumCost([10,12,13,14,15]))
    print(sol.minimumCost([22,33,22,33,22]))

if __name__ == '__main__':
    main()