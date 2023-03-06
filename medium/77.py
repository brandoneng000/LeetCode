from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def backtrack(combo: List[int], cur_num: int):
            if len(combo) == k:
                result.append(combo.copy())
            
            for index in range(cur_num + 1, n + 1):
                combo.append(index)
                backtrack(combo, index)
                combo.pop()
        
        backtrack([], 0)
        return result

def main():
    sol = Solution()
    print(sol.combine(4, 2))
    print(sol.combine(1, 1))

if __name__ == '__main__':
    main()