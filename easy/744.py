from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        result = float('inf')

        while left <= right:
            middle = (left + right) // 2
            if letters[middle] > target:
                result = min(result, middle)
                right = middle - 1
            else:
                left = middle + 1
        
        return letters[result] if result != float('inf') else letters[0]

def main():
    sol = Solution()
    print(sol.nextGreatestLetter(letters = ["c","f","j"], target = "a"))
    print(sol.nextGreatestLetter(letters = ["c","f","j"], target = "c"))
    print(sol.nextGreatestLetter(letters = ["x","x","y","y"], target = "z"))

if __name__ == '__main__':
    main()