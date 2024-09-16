from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        return [i for i, (a, b, c, m) in enumerate(variables) if pow(pow(a, b, 10), c, m) == target]
        
def main():
    sol = Solution()
    print(sol.getGoodIndices(variables = [[2,3,3,10],[3,3,3,1],[6,1,1,4]], target = 2))
    print(sol.getGoodIndices(variables = [[39,3,1000,1000]], target = 17))

if __name__ == '__main__':
    main()