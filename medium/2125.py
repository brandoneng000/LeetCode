from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        res = 0

        for r in bank:
            cur = r.count('1')
            res += prev * cur
            if cur > 0:
                prev = cur
        
        return res
        
def main():
    sol = Solution()
    print(sol.numberOfBeams(["011001","000000","010100","001000"]))
    print(sol.numberOfBeams(["000","111","000"]))

if __name__ == '__main__':
    main()