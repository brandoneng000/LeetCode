import collections

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = ord(t[0])

        for i, j in zip(s, t[1:]):
            res ^= ord(i)
            res ^= ord(j)

        return chr(res)
    
    # def findTheDifference(self, s: str, t: str) -> str:
    #     return list((collections.Counter(t) - collections.Counter(s)).keys())[0]

    # def findTheDifference(self, s: str, t: str) -> str:
    #     char = {}

    #     for letter in t:
    #         if letter not in char:
    #             char[letter] = 1
    #         else:
    #             char[letter] += 1
        
    #     for letter in s:
    #         char[letter] -= 1
    #         if char[letter] == 0:
    #             del char[letter]

    #     return list(char.keys())[0]

def main():
    sol = Solution()
    print(sol.findTheDifference("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", "abcdefghijdklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"))
    print(sol.findTheDifference("abcd", "abcde"))
    print(sol.findTheDifference("", "y"))
    print(sol.findTheDifference("a", "aa"))

if __name__ == '__main__':
    main()