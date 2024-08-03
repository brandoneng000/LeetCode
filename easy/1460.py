from typing import List
import collections

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)

    # def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
    #     return collections.Counter(target) == collections.Counter(arr)

def main():
    sol = Solution()
    print(sol.canBeEqual(target = [1,2,3,4], arr = [2,4,1,3]))
    print(sol.canBeEqual(target = [7], arr = [7]))
    print(sol.canBeEqual(target = [3,7,9], arr = [3,7,11]))

if __name__ == '__main__':
    main()