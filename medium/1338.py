from typing import List
import collections

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr_count = collections.Counter(arr)
        size = len(arr)
        goal = size // 2

        for index, a in enumerate(sorted(arr_count, key=lambda x: -arr_count[x])):
            size -= arr_count[a]
            if size <= goal:
                return index + 1
            

def main():
    sol = Solution()
    print(sol.minSetSize([3,3,3,3,5,5,5,2,2,7]))
    print(sol.minSetSize([7,7,7,7,7,7]))

if __name__ == '__main__':
    main()