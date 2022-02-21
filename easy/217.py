from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums_set = set(nums)
        # return len(nums_set) < len(nums)
        num_sets = set()
        for num in nums:
            if num not in num_sets:
                num_sets.add(num)
            else:
                return True
        return False



def main():
    sol = Solution()
    nums_one = [1,2,3,1]
    nums_two = [1,2,3,4]
    nums_three = [1,1,1,3,3,4,3,2,4,2]
    print(sol.containsDuplicate(nums_one))
    print(sol.containsDuplicate(nums_two))
    print(sol.containsDuplicate(nums_three))
    

if __name__ == '__main__':
    main()