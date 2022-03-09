from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        end_width = 0

        for letter in s:
            end_width += widths[ord(letter) - ord('a')]
            if end_width > 100:
                lines += 1
                end_width = widths[ord(letter) - ord('a')]

        return [lines, end_width]
        
def main():
    sol = Solution()
    print(sol.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,
        10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz"))
    print(sol.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,
        10,10,10,10,10,10,10,10,10,10,10,10,10,10], "bbbcccdddaaa"))

if __name__ == '__main__':
    main()