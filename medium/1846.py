from typing import List

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        res = 1

        for i in range(1, n):
            if arr[i] >= res + 1:
                res += 1
        
        return res

    # def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
    #     n = len(arr)
    #     arr.sort()
    #     arr[0] = 1
        
    #     for i in range(1, n):
    #         arr[i] = min(arr[i], arr[i - 1] + 1)
        
    #     return arr[-1]

        
def main():
    sol = Solution()
    print(sol.maximumElementAfterDecrementingAndRearranging([2,2,1,2,1]))
    print(sol.maximumElementAfterDecrementingAndRearranging([100,1,1000]))
    print(sol.maximumElementAfterDecrementingAndRearranging([1,2,3,4,5]))

if __name__ == '__main__':
    main()