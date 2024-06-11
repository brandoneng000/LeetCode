from typing import List
from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_count = Counter(arr1)
        res = []

        for num in arr2:
            res.extend([num] * arr1_count[num])
            arr1_count[num] = 0
        
        res.extend(sorted(arr1_count.elements()))

        return res

    # def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    #     result = []

    #     for num in arr2:
    #         while num in arr1:
    #             result.append(num)
    #             arr1.remove(num)

    #     arr1.sort()
    #     return result + arr1

def main():
    sol = Solution()
    print(sol.relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))
    print(sol.relativeSortArray(arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]))

if __name__ == '__main__':
    main()