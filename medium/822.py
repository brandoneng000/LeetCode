from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = set()
        different = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                same.add(fronts[i])

        for i in range(len(fronts)):
            if fronts[i] not in same:
                different.add(fronts[i])
            if backs[i] not in same:
                different.add(backs[i])
        
        if not different:
            return 0

        return min(n for n in different if n not in same)

def main():
    sol = Solution()
    print(sol.flipgame(fronts = [1,2,4,4,7], backs = [1,3,4,1,3]))
    print(sol.flipgame(fronts = [1], backs = [1]))

if __name__ == '__main__':
    main()