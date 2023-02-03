from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        from collections import Counter
        result = 0
        num_count = Counter(nums)
        num_ordered = sorted(num_count.keys())
        print(num_ordered)
        for index in range(len(num_ordered) - 1):
            if num_ordered[index + 1] - num_ordered[index] == 1:
                result = max(result, num_count[num_ordered[index]] + num_count[num_ordered[index] + 1])

        return result



def main():
    sol = Solution()
    print(sol.findLHS([1,3,2,2,5,2,3,7]))
    print(sol.findLHS([1,2,3,4]))
    print(sol.findLHS([1,1,1,1]))

if __name__ == '__main__':
    main()