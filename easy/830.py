from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        current = s[0]
        length = [0]
        count = 0
        s += "A"

        for index, letter in enumerate(s):
            if current != letter:
                if count > 2:
                    length.append(index - 1)
                    result.append(length)
                length = [index]
                current = letter
                count = 1
            else:
                count += 1

        return result

def main():
    sol = Solution()
    print(sol.largeGroupPositions("aa"))
    print(sol.largeGroupPositions("abbxxxxzzy"))
    print(sol.largeGroupPositions("abc"))
    print(sol.largeGroupPositions("abcdddeeeeaabbbcd"))
    print(sol.largeGroupPositions("abcdddeeeeaabbbcddddddd"))

if __name__ == '__main__':
    main()