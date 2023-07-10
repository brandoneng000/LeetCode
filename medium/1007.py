from typing import List
import collections

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        for val in [tops[0], bottoms[0]]:
            if all(val in domino for domino in zip(tops, bottoms)):
                return len(tops) - max(tops.count(val), bottoms.count(val))
        
        return -1

    # def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
    #     dominos = collections.defaultdict(list)

    #     for i in range(len(tops)):
    #         dominos[tops[i]].append(bottoms[i])
    #         if tops[i] != bottoms[i]:
    #             dominos[bottoms[i]].append(tops[i])
        
    #     if len(max(dominos.values(), key=len)) != len(tops):
    #         return -1
        
    #     key = max(dominos.items(), key=lambda x: len(x[1]))[0]
    #     top_count = 0
    #     bottom_count = 0
    #     for top, bot in zip(tops, bottoms):
    #         if top != key:
    #             top_count += 1
    #         if bot != key:
    #             bottom_count += 1
        
    #     return min(top_count, bottom_count)
        

def main():
    sol = Solution()
    print(sol.minDominoRotations([1,2,1,1,1,2,2,2], bottoms = [2,1,2,2,2,2,2,2]))
    print(sol.minDominoRotations(tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]))
    print(sol.minDominoRotations(tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]))

if __name__ == '__main__':
    main()