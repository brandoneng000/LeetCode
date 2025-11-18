from typing import List

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        i = 0

        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1
        
        return i == n - 1
        

    # def isOneBitCharacter(self, bits: List[int]) -> bool:
    #     bits_string = "".join(str(bit) for bit in bits)

    #     bits_string = bits_string.replace('11', '2')
    #     bits_string = bits_string.replace('10', '2')
        
    #     return bits_string[-1] == '0'

def main():
    sol = Solution()
    print(sol.isOneBitCharacter([1,0,0]))
    print(sol.isOneBitCharacter([1,1,1,0]))
    print(sol.isOneBitCharacter([0,0,0,0,0,0,1,0,0,0]))

if __name__ == '__main__':
    main()