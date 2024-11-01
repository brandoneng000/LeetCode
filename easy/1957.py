from string import ascii_lowercase

class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        res = list(s[:2])

        for i in range(2, n):
            if res[-2] == res[-1] == s[i]:
                continue
            else:
                res.append(s[i])

        return ''.join(res)

    # def makeFancyString(self, s: str) -> str:
    #     triplets = []
    #     for letter in ascii_lowercase:
    #         triplets.append(letter * 3)

    #     for triple in triplets:
    #         while triple in s:
    #             s = s.replace(triple, triple[:2])
        
    #     return s


def main():
    sol = Solution()
    print(sol.makeFancyString("leeetcode"))
    print(sol.makeFancyString("aaabaaaa"))
    print(sol.makeFancyString("aab"))

if __name__ == '__main__':
    main()