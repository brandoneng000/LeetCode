from typing import List
from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        res = 0

        for task in count:
            if count[task] == 1:
                return -1
            res += count[task] // 3 + (1 if count[task] % 3 else 0)
        
        return res
        
def main():
    sol = Solution()
    print(sol.minimumRounds([2,2,3,3,2,4,4,4,4,4]))
    print(sol.minimumRounds([2,3,3]))

if __name__ == '__main__':
    main()