from typing import List
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]

        def compare(first: str, second: str):
            s1 = first + second
            s2 = second + first
            if s1 > s2:
                return 1
            elif s1 < s2:
                return -1
            else:
                return 0

        nums.sort(reverse=True, key=functools.cmp_to_key(compare))
        res = "".join(nums)
        return "0" if res[0] == '0' else res
        
        
def main():
    sol = Solution()
    print(sol.largestNumber([10,2]))
    print(sol.largestNumber([3,30,34,5,9]))
    print(sol.largestNumber([111311, 1113]))

if __name__ == '__main__':
    main()