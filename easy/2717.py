from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        index_first = nums.index(1)
        index_last = nums.index(n)

        return index_first + ((n - 1) - index_last) - (1 if index_first > index_last else 0)
        

        
        
def main():
    sol = Solution()
    print(sol.semiOrderedPermutation([2,1,4,3]))
    print(sol.semiOrderedPermutation([2,4,1,3]))
    print(sol.semiOrderedPermutation([1,3,4,2,5]))

if __name__ == '__main__':
    main()