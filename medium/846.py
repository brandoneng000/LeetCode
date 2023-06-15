from typing import List
import collections

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand_count = collections.Counter(hand)
        for i in sorted(hand_count):
            if hand_count[i] > 0:
                for j in range(1, groupSize):
                    hand_count[i + j] -= hand_count[i]
                    if hand_count[i + j] < 0:
                        return False
        
        return True
    # def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    #     n = len(hand)
    #     if n % groupSize != 0:
    #         return False
    #     hand_count = collections.Counter(hand)

    #     while hand_count:
    #         stack = []
    #         cards = sorted(hand_count.keys())
    #         for card in cards:
    #             stack.append(card)
    #             hand_count[card] -= 1
    #             if hand_count[card] == 0:
    #                 hand_count.pop(card)

    #             if len(stack) == groupSize:
    #                 break

    #         if len(stack) != groupSize:
    #             return False

    #         for i in range(groupSize - 1):
    #             if stack[i] + 1 != stack[i + 1]:
    #                 return False
        
    #     return True


def main():
    sol = Solution()
    print(sol.isNStraightHand(hand = [1,1,2,2,3,3], groupSize = 2))
    print(sol.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))
    print(sol.isNStraightHand(hand = [1,2,3,4,5], groupSize = 4))

if __name__ == '__main__':
    main()