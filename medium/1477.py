from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        prefix = [float('inf')] * n
        res = float('inf')
        left = cur = 0

        for right in range(n):
            cur += arr[right]
            while cur > target and left <= right:
                cur -= arr[left]
                left += 1
            
            if cur == target:
                res = min(res, prefix[left - 1] + right - left + 1)
                prefix[right] = min(prefix[right - 1], right - left + 1)
            else:
                prefix[right] = prefix[right - 1]

        return -1 if res == float('inf') else res

def main():
    sol = Solution()
    print(sol.minSumOfLengths(arr = [3,2,2,4,3], target = 3))
    print(sol.minSumOfLengths(arr = [7,3,4,7], target = 7))
    print(sol.minSumOfLengths(arr = [4,3,2,6,2,3,4], target = 6))

if __name__ == '__main__':
    main()