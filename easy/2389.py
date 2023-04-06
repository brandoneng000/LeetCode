from typing import List

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()

        for i in range(len(queries)):
            sum_nums = 0
            count = 0
            for n in nums:
                if sum_nums + n <= queries[i]:
                    count += 1
                    sum_nums += n
            queries[i] = count
                    
        return queries

def main():
    sol = Solution()
    print(sol.answerQueries(nums = [4,5,2,1], queries = [3,10,21]))
    print(sol.answerQueries(nums = [2,3,4,5], queries = [1]))

if __name__ == '__main__':
    main()