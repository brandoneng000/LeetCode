from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix = [0] * (n + 1)

        for start, end, direction in shifts:
            direction = 1 if direction else -1
            prefix[start] += direction
            prefix[end + 1] -= direction

        for i in range(1, n):
            prefix[i] += prefix[i - 1]
        
        return ''.join([chr(((ord(s[i]) - ord('a') + prefix[i]) % 26) + ord('a')) for i in range(n)])


    # def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
    #     n = len(s)
    #     s_list = [ord(letter) - ord('a') for letter in s]
    #     prefix = [0] * (n + 1)

    #     for start, end, direction in shifts:
    #         direction = 1 if direction else -1
    #         prefix[start] += direction
    #         prefix[end + 1] -= direction

    #     for i in range(1, n):
    #         prefix[i] += prefix[i - 1]
        
    #     return ''.join([chr((s_list[i] + prefix[i]) % 26 + ord('a')) for i in range(n)])
        

        
def main():
    sol = Solution()
    print(sol.shiftingLetters(s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]))
    print(sol.shiftingLetters(s = "dztz", shifts = [[0,0,0],[1,1,1]]))

if __name__ == '__main__':
    main()