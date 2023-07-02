from typing import List
import collections

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr_count = collections.Counter(arr)
        arr_sorted = sorted(set(arr))
        size = len(arr) // 2
        count = 0

        for val in arr_sorted:
            if arr_count[val] > 0 and 2 * val in arr_count:
                if val == 0:
                    count += arr_count[val] // 2
                    arr_count[val] = 0
                else:
                    temp = min(arr_count[val], arr_count[2 * val])
                    count += temp
                    arr_count[2 * val] -= temp
                    arr_count[val] -= temp
                
        return count == size


def main():
    sol = Solution()
    print(sol.canReorderDoubled([1,2,1,-8,8,-4,4,-4,2,-2]))
    print(sol.canReorderDoubled([-8,-4,-2,-1,0,0,1,2,4,8]))
    print(sol.canReorderDoubled([3,1,3,6]))
    print(sol.canReorderDoubled([2,1,2,6]))
    print(sol.canReorderDoubled([4,-2,2,-4]))

if __name__ == '__main__':
    main()