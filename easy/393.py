from typing import List

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        ONE_BYTE = 0b10000000
        TWO_BYTE = 0b11100000
        THREE_BYTE = 0b11110000
        FOUR_BYTE = 0b11111000
        N_BYTES = 0b11000000
        count = 0

        for byte in data:
            if (byte & ONE_BYTE) == 0b00000000 and count == 0:
                continue
            elif (byte & N_BYTES) == 0b10000000 and count != 0:
                count -= 1
            elif (byte & TWO_BYTE) == 0b11000000 and count == 0:
                count = 1
            elif (byte & THREE_BYTE) == 0b11100000 and count == 0:
                count = 2
            elif (byte & FOUR_BYTE) == 0b11110000 and count == 0:
                count = 3
            else:
                return False
        
        return count == 0


def main():
    sol = Solution()
    print(sol.validUtf8([197,130,1]))
    print(sol.validUtf8([235,140,4]))
    print(sol.validUtf8([255]))

if __name__ == '__main__':
    main()