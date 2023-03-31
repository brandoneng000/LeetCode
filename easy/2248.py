from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        nums_count = {}
        res = []

        for num in nums:
            for n in num:
                nums_count[n] = nums_count.get(n, 0) + 1

        for num in nums_count:
            if nums_count[num] == len(nums):
                res.append(num)
        
        return sorted(res)

def main():
    sol = Solution()
    print(sol.intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
    print(sol.intersection([[1,2,3],[4,5,6]]))

if __name__ == '__main__':
    main()