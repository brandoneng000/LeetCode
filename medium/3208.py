from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        res = 0
        cur = -1
        count = 0

        for i in range(n + k - 1):
            if cur != colors[i % n]:
                count += 1
            else:
                count = 1
            
            if count >= k:
                res += 1
            
            cur = colors[i % n]
        
        return res


def main():
    sol = Solution()
    print(sol.numberOfAlternatingGroups(colors = [0,1,0,1,0], k = 3))
    print(sol.numberOfAlternatingGroups(colors = [0,1,0,0,1,0,1], k = 6))
    print(sol.numberOfAlternatingGroups(colors = [1,1,0,1], k = 4))

if __name__ == '__main__':
    main()