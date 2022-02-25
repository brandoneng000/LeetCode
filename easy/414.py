from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        num_set = set(nums)

        if len(num_set) < 3:
            return max(num_set)

        num_set.remove(max(num_set))
        num_set.remove(max(num_set))
        
        return max(num_set)

def main():
    sol = Solution()
    print(sol.thirdMax([3,2,1]))
    print(sol.thirdMax([2,1]))
    print(sol.thirdMax([2,2,3,1]))
    print(sol.thirdMax([1,1,2]))

if __name__ == '__main__':
    main()