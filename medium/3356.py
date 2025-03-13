from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        total_sum = 0
        res = 0
        prefix = [0] * (n + 1)

        for i in range(n):
            while total_sum + prefix[i] < nums[i]:
                res += 1

                if res > m:
                    return -1
                
                left, right, val = queries[res - 1]

                if right >= i:
                    prefix[max(left, i)] += val
                    prefix[right + 1] -= val
            
            total_sum += prefix[i]
        
        return res

    # def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
    #     def check_zero_array(nums: List[int], queries: List[List[int]], middle: int):
    #         n = len(nums)
    #         prefix = [0] * n

    #         for i in range(middle):
    #             left, right, val = queries[i]
    #             prefix[left] += val
    #             if right + 1 < n:
    #                 prefix[right + 1] -= val
            
    #         for i in range(1, n):
    #             prefix[i] += prefix[i - 1]
            
    #         return all(a <= b for a, b in zip(nums, prefix))

    #     n = len(queries)
    #     left = 0
    #     right = n

    #     while left < right:
    #         middle = (left + right) // 2

    #         if check_zero_array(nums, queries, middle):
    #             right = middle
    #         else:
    #             left = middle + 1
        
    #     return left if check_zero_array(nums, queries, left) else -1

        
def main():
    sol = Solution()
    print(sol.minZeroArray(nums = [7,6,8], queries = [[0,0,2],[0,1,5],[2,2,5],[0,2,4]]))
    print(sol.minZeroArray(nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]))
    print(sol.minZeroArray(nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]))

if __name__ == '__main__':
    main()