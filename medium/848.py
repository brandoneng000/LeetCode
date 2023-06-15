from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        letters = list(s)
        shift_sum = [0] * (len(shifts) + 1)

        for i in range(len(letters) - 1, -1, -1):
            shift_sum[i] = (shift_sum[i + 1] + shifts[i]) % 26
        
        for i in range(len(letters) - 1, -1, -1):
            letters[i] = chr((ord(letters[i]) - ord('a') + shift_sum[i]) % 26 + ord('a'))
        
        return "".join(letters)
        
def main():
    sol = Solution()
    print(sol.shiftingLetters(s = "bad", shifts = [10,20,30]))
    print(sol.shiftingLetters(s = "abc", shifts = [3,5,9]))
    print(sol.shiftingLetters(s = "aaa", shifts = [1,2,3]))

if __name__ == '__main__':
    main()