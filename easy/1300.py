from typing import List

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort(reverse=True)
        largest_val = arr[0]
        while arr and target >= arr[-1] * len(arr):
            target -= arr.pop()

        return int(round((target - 0.0001) / len(arr))) if arr else largest_val

    # def findBestValue(self, arr: List[int], target: int) -> int:
    #     def sum_mutated_array(arr: List[int], val: int) -> int:
    #         return sum(min(n, val) for n in arr)

    #     left, right = 0, max(arr)

    #     while left < right:
    #         middle = (left + right) // 2
    #         cur = sum_mutated_array(arr, middle)
    #         if cur >= target:
    #             right = middle
    #         else:
    #             left = middle + 1
        
    #     return min(left - 1, left, left + 1, key=lambda x: abs(sum_mutated_array(arr, x) - target))

def main():
    sol = Solution()
    print(sol.findBestValue(arr = [4,9,3], target = 10))
    print(sol.findBestValue(arr = [2,3,5], target = 10))
    print(sol.findBestValue(arr = [60864,25176,27249,21296,20204], target = 56803))

if __name__ == '__main__':
    main()