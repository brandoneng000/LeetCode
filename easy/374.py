# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            middle = (low + high) // 2
            check = guess(middle)

            if check == 0:
                return middle
            elif check == -1:
                high = middle - 1
            elif check == 1:
                low = middle + 1