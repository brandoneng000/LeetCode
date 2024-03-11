from string import ascii_lowercase
import collections

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count_alphabet = {}

        for letter in order:
            count_alphabet[letter] = 0
        
        for letter in ascii_lowercase:
            if letter in count_alphabet:
                continue
            count_alphabet[letter] = 0
        
        for letter in s:
            count_alphabet[letter] += 1
        
        return "".join((letter * count_alphabet[letter]) for letter in count_alphabet)

    # def customSortString(self, order: str, s: str) -> str:
    #     count_s = collections.Counter(s)
    #     res = []
    #     for c in order:
    #         if c in count_s:
    #             res.extend([c] * count_s[c])
    #             count_s.pop(c)

    #     for c in count_s:
    #         res.extend([c] * count_s[c])
        
    #     return "".join(res)

    # def customSortString(self, order: str, s: str) -> str:
    #     custom_order = { c: i for i, c in enumerate(order) }
        
    #     return "".join(sorted(s, key=lambda x: custom_order.get(x, 27)))

def main():
    sol = Solution()
    print(sol.customSortString(order = "cba", s = "abcd"))
    print(sol.customSortString(order = "cbafg", s = "abcd"))

if __name__ == '__main__':
    main()