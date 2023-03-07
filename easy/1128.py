from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        domino_count = {}
        result = 0

        for domino in dominoes:
            d = (min(domino), max(domino))
            domino_count[d] = domino_count.get(d, 0) + 1
        
        n = max(domino_count.values()) - 1
        for count in domino_count.values():
            n = count - 1
            result += n * (n + 1) // 2
        return result
        

def main():
    sol = Solution()
    print(sol.numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
    print(sol.numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))
    print(sol.numEquivDominoPairs([[1,1],[2,2],[1,1],[1,2],[1,2],[1,1]]))

if __name__ == '__main__':
    main()