import string

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        code = {}
        alpha_index = 0
        res = []

        for letter in key:
            if letter not in code and letter != ' ':
                code[letter] = string.ascii_lowercase[alpha_index]
                alpha_index += 1

        for letter in message:
            if letter == ' ':
                res.append(' ')
            else:
                res.append(code[letter])

        return ''.join(res)

def main():
    sol = Solution()
    print(sol.decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"))
    print(sol.decodeMessage(key = "eljuxhpwnyrdgtqkviszcfmabo", message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"))

if __name__ == '__main__':
    main()