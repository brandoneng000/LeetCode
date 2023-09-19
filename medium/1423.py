from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        res = right = sum(cardPoints[:k])

        for l in range(-1, -(k + 1), -1):
            right -= cardPoints[l + k]
            left += cardPoints[l]

            res = max(res, left + right)

        return res
        
    # def maxScore(self, cardPoints: List[int], k: int) -> int:
    #     def find_max_window(cards: List[int], window: int):
    #         cur = res = sum(cards[:window])
    #         left = 0

    #         for right in range(window, len(cards)):
    #             cur -= cards[left]
    #             cur += cards[right]
    #             res = max(res, cur)
    #             left += 1

    #         return res

    #     n = len(cardPoints)
    #     if k >= n:
    #         return sum(cardPoints)

    #     left_cards = cardPoints[-k:] + cardPoints[:k]
    #     right_cards = cardPoints[n - k:] + cardPoints[:(k - 1)]

    #     return max(find_max_window(left_cards, k), find_max_window(right_cards, k))
        



def main():
    sol = Solution()
    print(sol.maxScore(cardPoints = [1,1000,1], k = 1))
    print(sol.maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3))
    print(sol.maxScore(cardPoints = [2,2,2], k = 2))
    print(sol.maxScore(cardPoints = [9,7,7,9,7,7,9], k = 7))

if __name__ == '__main__':
    main()