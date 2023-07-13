from typing import List

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        odd = 0
        even = 0
        state = True

        while n:
            if state:
                even += (n & 1)
            else:
                odd += (n & 1)
            state = not state
            n >>= 1
        
        return [even, odd]
        

def main():
    sol = Solution()
    print(sol.evenOddBit(17))
    print(sol.evenOddBit(2))

if __name__ == '__main__':
    main()