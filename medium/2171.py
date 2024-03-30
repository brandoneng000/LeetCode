from typing import List

class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        return sum(beans) - max((len(beans) - i) * b for i, b in enumerate(sorted(beans)))

        
def main():
    sol = Solution()
    print(sol.minimumRemoval([4,1,6,5]))
    print(sol.minimumRemoval([2,10,3,2]))

if __name__ == '__main__':
    main()