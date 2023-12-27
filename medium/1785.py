from typing import List

class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        total = sum(nums)
        difference = goal - total
        
        if difference < 0:
            difference = -difference

        q, r = divmod(difference, limit)
        return q + (1 if r else 0)
        
        
def main():
    sol = Solution()
    print(sol.minElements(nums = [1,-1,1], limit = 3, goal = -4))
    print(sol.minElements(nums = [1,-10,9,1], limit = 100, goal = 0))
    print(sol.minElements(nums = [1,-10,9,1], limit = 100, goal = 1))

if __name__ == '__main__':
    main()