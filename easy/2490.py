class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        n = len(sentence)

        for i in range(n - 1, -1, -1):
            if sentence[i][-1] != sentence[(i + 1) % n][0]:
                return False
        
        return True


    # def isCircularSentence(self, sentence: str) -> bool:
    #     n = len(sentence)

    #     for i in range(n):
    #         if sentence[i] == ' ' and sentence[i - 1] != sentence[i + 1]:
    #             return False
    #         elif i == n - 1 and sentence[i] != sentence[0]:
    #             return False
        
    #     return True

    # def isCircularSentence(self, sentence: str) -> bool:
    #     sentence = sentence.split()
    #     cur_word = sentence[0]

    #     for i in range(len(sentence) - 1, -1, -1):
    #         if cur_word[0] != sentence[i][-1]:
    #             return False
    #         cur_word = sentence[i]

    #     return True

def main():
    sol = Solution()
    print(sol.isCircularSentence("leetcode exercises sound delightful"))
    print(sol.isCircularSentence("eetcode"))
    print(sol.isCircularSentence("Leetcode is cool"))

if __name__ == '__main__':
    main()