from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_index = {}
        res = float('inf')

        for i, val in enumerate(cards):
            if val in last_index:
                res = min(res, i - last_index[val] + 1)
            last_index[val] = i
        
        return res if res != float('inf') else -1
        
def main():
    sol = Solution()
    print(sol.minimumCardPickup([3,4,2,3,4,7]))
    print(sol.minimumCardPickup([1,0,5,3]))

if __name__ == '__main__':
    main()