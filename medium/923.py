from typing import List
import collections
import math

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        triples = []
        arr_count = collections.Counter(arr)
        res = 0
        mod = 1000000007

        for index, val in enumerate(arr):
            if index > 0 and val == arr[index - 1]:
                continue
            left, right = index + 1, len(arr) - 1
            while left < right:
                three_sum = val + arr[left] + arr[right]
                if three_sum > target:
                    right -= 1
                elif three_sum < target:
                    left += 1
                else:
                    triples.append((val, arr[left], arr[right]))
                    left += 1
                    while arr[left] == arr[left - 1] and left < right:
                        left += 1
        
        for triple in triples:
            tri_counter = collections.Counter(triple)
            combo = 1
            for val in tri_counter:
                combo *= math.comb(arr_count[val], tri_counter[val])
            res += combo

        return res % mod

def main():
    sol = Solution()
    print(sol.threeSumMulti(arr = [1,1,2,2,3,3,4,4,5,5], target = 8))
    print(sol.threeSumMulti(arr = [1,1,2,2,2,2], target = 5))
    print(sol.threeSumMulti(arr = [2,1,3], target = 6))

if __name__ == '__main__':
    main()