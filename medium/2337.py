from typing import List
from collections import defaultdict

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        def count_left_right(string: str):
            letters = defaultdict(list)

            for i in range(n):
                letters[string[i]].append(i)
            
            return letters

        n = len(start)
        start_letters = count_left_right(start)
        target_letters = count_left_right(target)

        if start.replace('_', '') != target.replace('_', ''):
            return False

        for i, j in zip(start_letters['L'], target_letters['L']):
            if j <= i:
                pass
            else:
                return False
        
        for i, j in zip(start_letters['R'], target_letters['R']):
            if i <= j:
                pass
            else:
                return False 
        
        return True


def main():
    sol = Solution()
    print(sol.canChange(start = "_L__R__R_", target = "L______RR"))
    print(sol.canChange(start = "R_L_", target = "__LR"))
    print(sol.canChange(start = "_R", target = "R_"))

if __name__ == '__main__':
    main()