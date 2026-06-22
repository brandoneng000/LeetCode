from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        res = count['b']
        res = min(res, count['a'])
        res = min(res, count['l'] // 2)
        res = min(res, count['o'] // 2)
        res = min(res, count['n'])

        return res

    # def maxNumberOfBalloons(self, text: str) -> int:
    #     def letter_count(text: str, char: str) -> int:
    #         count = 0
    #         for letter in text:
    #             if letter == char:
    #                 count += 1
    #         return count
        
    #     res = letter_count['b']
    #     res = min(res, letter_count(text, 'a'))
    #     res = min(res, letter_count(text, 'l') // 2)
    #     res = min(res, letter_count(text, 'o') // 2)
    #     res = min(res, letter_count(text, 'n'))

    #     return res



        
def main():
    sol = Solution()
    print(sol.maxNumberOfBalloons("nlaebolko"))
    print(sol.maxNumberOfBalloons("loonbalxballpoon"))
    print(sol.maxNumberOfBalloons("b"))

if __name__ == '__main__':
    main()