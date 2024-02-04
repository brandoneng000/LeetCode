from typing import List

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        cur = 0
        res = 0

        for r in rungs:
            if cur + dist < r:
                diff = r - cur
                add_rung = (diff - 1) // dist
                res += add_rung
            cur = r
        
        return res

        
def main():
    sol = Solution()
    print(sol.addRungs(rungs = [1,3,5,10], dist = 2))
    print(sol.addRungs(rungs = [3,6,8,10], dist = 3))
    print(sol.addRungs(rungs = [3,4,6,7], dist = 2))

if __name__ == '__main__':
    main()