from typing import List
from collections import Counter

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)

        if n % 2:
            return []
        
        change_count = Counter(changed)
        res = []

        for num in sorted(change_count):
            if change_count[num]:
                if num == 0:
                    if change_count[num] % 2 == 0:
                        res.extend([num] * (change_count[num] // 2))
                    else:
                        return []
                elif change_count[num] <= change_count[num * 2]:
                    change_count[num * 2] -= change_count[num]
                    res.extend([num] * change_count[num])
                else:
                    return []
        
        return res
        
        
def main():
    sol = Solution()
    print(sol.findOriginalArray([2,1,2,4,2,4]))
    print(sol.findOriginalArray([1,3,4,2,6,8]))
    print(sol.findOriginalArray([6,3,0,1]))
    print(sol.findOriginalArray([1]))

if __name__ == '__main__':
    main()