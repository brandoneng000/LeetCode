from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        positions = [index for index, char in enumerate(s) if char == c]
        distance = []

        for index in range(len(s)):
            distance.append(min([abs(pos - index) for pos in positions]))

        return distance

        
def main():
    sol = Solution()
    print(sol.shortestToChar("loveleetcode", "e"))

if __name__ == '__main__':
    main()