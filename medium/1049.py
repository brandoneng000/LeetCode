from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        total = sum(stones)
        for w in stones:
            next_set = set()
            for cur_set in dp:
                if w + cur_set < total / 2:
                    next_set.add(w + cur_set)
                elif w + cur_set == total / 2:
                    return 0
            dp |= next_set
        
        return min(abs(total - (2 * i)) for i in dp)

def main():
    sol = Solution()
    print(sol.lastStoneWeightII([2,7,4,1,8,1]))
    print(sol.lastStoneWeightII([31,26,33,21,40]))

if __name__ == '__main__':
    main()