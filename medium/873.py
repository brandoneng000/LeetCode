from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        dp = [[0 for j in range(n)] for i in range(n)]

        value_to_index = { num: index for index, num in enumerate(arr) }

        for cur in range(n):
            for prev in range(cur):
                diff = arr[cur] - arr[prev]
                prev_index = value_to_index.get(diff, -1)

                dp[prev][cur] = dp[prev_index][prev] + 1 if diff < arr[prev] and prev_index >= 0 else 2
                res = max(res, dp[prev][cur])
        
        return res if res > 2 else 0

    # def lenLongestFibSubseq(self, arr: List[int]) -> int:
    #     arr_set = set(arr)
    #     res = 0
    # 
    #     for i in range(len(arr)):
    #         for j in range(i + 1, len(arr)):
    #             val = arr[j]
    #             val2 = arr[i] + arr[j]
    #             size = 2
    #             while val2 in arr_set:
    #                 val, val2 = val2, val + val2
    #                 size += 1
    #             res = max(res, size)
        
    #     return res if res >= 3 else 0

def main():
    sol = Solution()
    print(sol.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
    print(sol.lenLongestFibSubseq([1,3,7,11,12,14,18]))

if __name__ == '__main__':
    main()