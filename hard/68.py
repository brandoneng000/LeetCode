from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        cur = []
        res = []

        for word in words:
            if cur and len(" ".join(cur)) + len(word) + 1 > maxWidth:
                lines.append(cur.copy())
                cur = [word]
            else:
                cur.append(word)
        if cur:
            lines.append(cur.copy())

        for index, line in enumerate(lines):
            cur_length = len("".join(line))
            spaces = maxWidth - cur_length
            if len(line) >= 2 and index != len(lines) - 1:
                s, r = divmod(spaces, len(line) - 1)
                cur = []
                for word in line:
                    cur.append(word)
                    cur.append(' ' * s)
                    if r > 0:
                        cur.append(' ')
                        r -= 1
                res.append("".join(cur).rstrip())
            else:
                cur = " ".join(line)
                res.append(cur + (' ' * (maxWidth - len(cur))))
        
        return res


def main():
    sol = Solution()
    print(sol.fullJustify(words = ["Listen","to","many,","speak","to","a","few."], maxWidth = 6))
    print(sol.fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))
    print(sol.fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16))
    print(sol.fullJustify(words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20))

if __name__ == '__main__':
    main()