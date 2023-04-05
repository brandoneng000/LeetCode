class Solution:
    def repeatedCharacter(self, s: str) -> str:
        # str_set = set()
        # size = 0

        # for letter in s:
        #     str_set.add(letter)
        #     if size + 1 != len(str_set):
        #         return letter
        #     size += 1
        str_dict = {}
        for letter in s:
            str_dict[letter] = str_dict.get(letter, 0) + 1
            if str_dict[letter] == 2:
                return letter


def main():
    sol = Solution()
    print(sol.repeatedCharacter("abccbaacz"))
    print(sol.repeatedCharacter("abcdd"))

if __name__ == '__main__':
    main()