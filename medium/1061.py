import string

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def find(letter: str):
            if letter != data[letter]:
                data[letter] = find(data[letter])
            return data[letter]

        data = { a: a for a in string.ascii_lowercase }

        for l1, l2 in zip(s1, s2):
            key1, key2 = find(l1), find(l2)
            data[key1] = data[key2] = min(key1, key2)
                
        return "".join(find(letter) for letter in baseStr)


def main():
    sol = Solution()
    print(sol.smallestEquivalentString(s1 = "parker", s2 = "morris", baseStr = "parser"))
    print(sol.smallestEquivalentString(s1 = "hello", s2 = "world", baseStr = "hold"))
    print(sol.smallestEquivalentString(s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"))

if __name__ == '__main__':
    main()