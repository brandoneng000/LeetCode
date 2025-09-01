from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        res = 0

        for i in range(n):
            res += colors[i - 1] != colors[i] != colors[(i + 1) % n]
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.numberOfAlternatingGroups([1,1,1]))
    print(sol.numberOfAlternatingGroups([0,1,0,0,1]))

if __name__ == '__main__':
    main()