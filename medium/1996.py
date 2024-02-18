from typing import List
from collections import defaultdict

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        res = 0

        for attack, defense in properties:
            while stack and defense > stack[-1]:
                stack.pop()
                res += 1
            stack.append(defense)
        
        return res

        
def main():
    sol = Solution()
    print(sol.numberOfWeakCharacters([[5,5],[6,3],[3,6]]))
    print(sol.numberOfWeakCharacters([[2,2],[3,3]]))
    print(sol.numberOfWeakCharacters([[1,5],[10,4],[4,3]]))

if __name__ == '__main__':
    main()