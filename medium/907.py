from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        mod = 1000000007
        stack = []

        for i in range(len(arr) + 1):
            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                right = i

                count = (mid - left) * (right - mid)
                res += (count * arr[mid])
            stack.append(i)
        
        return res % mod

    # def sumSubarrayMins(self, arr: List[int]) -> int:
    #     res = sum(arr)
    #     mod = 1000000007
        

    #     for size in range(len(arr) - 1, 0, -1):
    #         for i in range(size):
    #             arr[i] = min(arr[i], arr[i + 1])
    #             res += arr[i]
        
    #     return res % mod


def main():
    sol = Solution()
    print(sol.sumSubarrayMins([3,1,2,4]))
    print(sol.sumSubarrayMins([11,81,94,43,3]))

if __name__ == '__main__':
    main()