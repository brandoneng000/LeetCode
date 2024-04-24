from typing import List

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        if bottom not in special:
            special.append(bottom - 1)
        if top not in special:
            special.append(top + 1)
        special.sort()
        n = len(special)
        res = 0

        for i in range(1, n):
            res = max(res, special[i] - special[i - 1] - 1)
        
        return res

        
def main():
    sol = Solution()
    print(sol.maxConsecutive(bottom = 2, top = 9, special = [4,6]))
    print(sol.maxConsecutive(bottom = 6, top = 8, special = [7,6,8]))

if __name__ == '__main__':
    main()