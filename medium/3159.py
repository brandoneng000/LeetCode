from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        n = len(nums)
        index = []
        res = []

        for i in range(n):
            if nums[i] == x:
                index.append(i)

        n = len(index)
        for q in queries:
            if q - 1< n:
                res.append(index[q - 1])
            else:
                res.append(-1)

        return res
        
            
        
def main():
    sol = Solution()
    print(sol.occurrencesOfElement(nums = [1,3,1,7], queries = [1,3,2,4], x = 1))
    print(sol.occurrencesOfElement(nums = [1,2,3], queries = [10], x = 5))

if __name__ == '__main__':
    main()