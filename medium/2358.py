from typing import List

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        res = 0

        while n >= res + 1:
            res += 1
            n -= res

        return res
        
def main():
    sol = Solution()
    print(sol.maximumGroups([10,6,12,7,3,5]))
    print(sol.maximumGroups([8,8]))

if __name__ == '__main__':
    main()