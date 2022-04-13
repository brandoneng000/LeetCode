class Solution:
    def maxScore(self, s: str) -> int:
        zeroes = 0
        ones = 0
        score = {}

        for index in range(len(s) - 1):
            zeroes += 1 if s[index] == '0' else 0
            score[index] = zeroes

        for index in range(len(s) - 2, -1, -1):
            ones += 1 if s[index + 1] == '1' else 0
            score[index] += ones

        return max(score.values())

def main():
    sol = Solution()
    print(sol.maxScore("011101"))
    # print(sol.maxScore("00111"))
    # print(sol.maxScore("1111"))

if __name__ == '__main__':
    main()