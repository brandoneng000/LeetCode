from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        cache = {}
        res = 1

        for val in arr:
            prev = cache.get(val - difference, 0)
            cache[val] = prev + 1
            res = max(res, cache[val])
        
        return res

    # def longestSubsequence(self, arr: List[int], difference: int) -> int:
    #     cache = {}
    #     res = [1]

    #     for i in range(len(arr) - 1, -1, -1):
    #         if arr[i] + difference in cache:
    #             res.append(cache[arr[i] + difference] + 1)
    #         cache[arr[i]] = cache.get(arr[i] + difference, 0) + 1
        
    #     return max(res)

    # def longestSubsequence(self, arr: List[int], difference: int) -> int:
    #     prefix = [1] * len(arr)

    #     for i in range(len(arr)):
    #         next = arr[i] + difference
    #         for j in range(i + 1, len(arr)):
    #             if arr[j] == next:
    #                 prefix[j] = max(prefix[j], prefix[i] + 1)
        
    #     return max(prefix)

def main():
    sol = Solution()
    print(sol.longestSubsequence(arr = [1,2,3,4], difference = 1))
    print(sol.longestSubsequence(arr = [1,3,5,7], difference = 1))
    print(sol.longestSubsequence(arr = [1,5,7,8,5,3,4,2,1], difference = -2))

if __name__ == '__main__':
    main()