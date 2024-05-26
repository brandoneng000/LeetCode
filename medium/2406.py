from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        n = max(right for left, right in intervals)
        prefix = [0] * (n + 2)

        for left, right in intervals:
            prefix[left] += 1
            prefix[right + 1] -= 1

        for i in range(1, n + 1):
            prefix[i] += prefix[i - 1]
        
        prefix.pop()
        return max(prefix)
        
def main():
    sol = Solution()
    print(sol.minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))
    print(sol.minGroups([[1,3],[5,6],[8,10],[11,13]]))

if __name__ == '__main__':
    main()