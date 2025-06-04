class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        n = len(word)
        substring_size = n - numFriends + 1
        res = ""

        for i in range(n):
            res = max(res, word[i: i + substring_size])

        return res

def main():
    sol = Solution()
    print(sol.answerString(word = "dbca", numFriends = 2))
    print(sol.answerString(word = "gggg", numFriends = 4))

if __name__ == '__main__':
    main()