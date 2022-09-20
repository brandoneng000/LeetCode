class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        res = [''] * len(s)

        for word in s:
            res[int(word[-1]) - 1] = word[:-1]
        
        return " ".join(res)

def main():
    sol = Solution()
    print(sol.sortSentence("is2 sentence4 This1 a3"))
    print(sol.sortSentence("Myself2 Me1 I4 and3"))

if __name__ == '__main__':
    main()