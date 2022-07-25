from typing import List

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        longest = releaseTimes[0]
        letter = keysPressed[0]
        
        for index in range(1, len(keysPressed)):
            temp = releaseTimes[index] - releaseTimes[index - 1]
            if temp > longest:
                longest = temp
                letter = keysPressed[index]
            elif temp == longest:
                letter = max(letter, keysPressed[index])
        
        return letter

        
def main():
    sol = Solution()
    print(sol.slowestKey([9,29,49,50], "cbcd"))
    print(sol.slowestKey([12,23,36,46,62], "spuda"))
    print(sol.slowestKey([23,34,43,59,62,80,83,92,97], "qgkzzihfc"))

if __name__ == '__main__':
    main()