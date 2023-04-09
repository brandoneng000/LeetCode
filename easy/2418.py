from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = [(height, name) for name, height in zip(names, heights)]
        res.sort(reverse=True)
        return [name for height, name in res]

def main():
    sol = Solution()
    print(sol.sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))
    print(sol.sortPeople(names = ["Alice","Bob","Bob"], heights = [155,185,150]))

if __name__ == '__main__':
    main()