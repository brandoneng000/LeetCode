class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        cur_word = sentence[0]

        for i in range(len(sentence) - 1, -1, -1):
            if cur_word[0] != sentence[i][-1]:
                return False
            cur_word = sentence[i]

        return True

def main():
    sol = Solution()
    print(sol.isCircularSentence("leetcode exercises sound delightful"))
    print(sol.isCircularSentence("eetcode"))
    print(sol.isCircularSentence("Leetcode is cool"))

if __name__ == '__main__':
    main()