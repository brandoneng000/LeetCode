import collections

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_dict = collections.Counter(s)
        target_dict = collections.Counter(target)
        res = 1000

        for letter in target_dict:
            res = min(res, s_dict[letter] // target_dict[letter])

        return res


def main():
    sol = Solution()
    print(sol.rearrangeCharacters(s = "ilovecodingonleetcode", target = "code"))
    print(sol.rearrangeCharacters(s = "abcba", target = "abc"))
    print(sol.rearrangeCharacters(s = "abbaccaddaeea", target = "aaaaa"))

if __name__ == '__main__':
    main()