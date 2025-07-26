from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        right = [[] for _ in range(n + 1)]
        res = 0

        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))
        
        left = [0, 0]
        bonus = [0] * (n + 1)

        for r in range(1, n + 1):
            for l in right[r]:
                if l > left[0]:
                    left = [l, left[0]]
                elif l > left[1]:
                    left = [left[0], l]
            
            res += r - left[0]

            if left[0] > 0:
                bonus[left[0]] += left[0] - left[1]
        
        return res + max(bonus)
        
def main():
    sol = Solution()
    print(sol.maxSubarrays(n = 4, conflictingPairs = [[2,3],[1,4]]))
    print(sol.maxSubarrays(n = 5, conflictingPairs = [[1,2],[2,5],[3,5]]))
    print(sol.maxSubarrays(n = 25, conflictingPairs = [[2,22],[7,21],[17,8]]))

if __name__ == '__main__':
    main()