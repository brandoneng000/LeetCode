import collections

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def helper(key: str):
            cur = collections.deque()
            res = 0
            flips = 0
            for ans in answerKey:
                if ans == key:
                    cur.append(ans)
                else:
                    while cur and flips == k:
                        if cur.popleft() != key:
                            flips -= 1
                    cur.append(ans)
                    flips += 1
                res = max(res, len(cur))
            
            return res

        return max(helper('T'), helper('F'))


def main():
    sol = Solution()
    print(sol.maxConsecutiveAnswers(answerKey = "FTFFTFTFTTFTTFTTFFTTFFTTTTTFTTTFTFFTTFFFFFTTTTFTTTTTTTTTFTTFFTTFTFFTTTFFFFFTTTFFTTTTFTFTFFTTFTTTTTTF", k = 32))
    print(sol.maxConsecutiveAnswers(answerKey = "TTFF", k = 2))
    print(sol.maxConsecutiveAnswers(answerKey = "TFFT", k = 1))
    print(sol.maxConsecutiveAnswers(answerKey = "TTFTTFTT", k = 1))

if __name__ == '__main__':
    main()