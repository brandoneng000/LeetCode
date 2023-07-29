from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        one_delete = arr[0]
        no_delete = arr[0]
        res = arr[0]

        for i in range(1, n):
            one_delete = max(one_delete + arr[i], no_delete)
            no_delete = max(no_delete + arr[i], arr[i])
            res = max(res, one_delete, no_delete)

        return res

def main():
    sol = Solution()
    print(sol.maximumSum([1,0,3]))
    print(sol.maximumSum([1,-2,0,3]))
    print(sol.maximumSum([1,-2,-2,3]))
    print(sol.maximumSum([-1,-1,-1,-1]))

if __name__ == '__main__':
    main()