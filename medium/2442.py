from typing import List

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        num_set = set(nums)

        for num in nums:
            num_set.add(int(str(num)[::-1]))
        
        return len(num_set)
        
def main():
    sol = Solution()
    print(sol.countDistinctIntegers([1,13,10,12,31]))
    print(sol.countDistinctIntegers([2,2,2]))

if __name__ == '__main__':
    main()