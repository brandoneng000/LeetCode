from collections import defaultdict

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1

        indexes = defaultdict(list)

        for i, c in enumerate(s):
            indexes[c].append(i)
        
        for c in indexes:
            if len(indexes[c]) > 1:
                res = max(res, indexes[c][-1] - (indexes[c][0] + 1))
        
        return res

    # def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    #     if len(s) == 1:
    #         return -1
        
    #     s_dict = {}
    #     longest = -1

    #     for index, letter in enumerate(s):
    #         s_dict[letter] = s_dict.get(letter, []) + [index]

    #     for key in s_dict:
    #         if len(s_dict[key]) >= 2:
    #             longest = max(longest, s_dict[key][-1] - (s_dict[key][0] + 1))

    #     return longest

def main():
    sol = Solution()
    print(sol.maxLengthBetweenEqualCharacters("aa"))
    print(sol.maxLengthBetweenEqualCharacters("abca"))
    print(sol.maxLengthBetweenEqualCharacters("cbzxy"))
    print(sol.maxLengthBetweenEqualCharacters("adfgahjkla"))
    print(sol.maxLengthBetweenEqualCharacters("rimkibmvpnhlgtdkazshyilqmywn"))

if __name__ == '__main__':
    main()