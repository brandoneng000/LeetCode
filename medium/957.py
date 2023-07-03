from typing import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        def list_to_int(bits: List[int]) -> int:
            out = 0
            for bit in bits:
                out = (out << 1) | bit
            
            return out
        
        if n == 0:
            return cells
        dp = []

        while n:
            n -= 1
            temp = [0]
            for i in range(1, 7):
                temp.append(1 if (cells[i - 1] and cells[i + 1]) or (not cells[i - 1] and not cells[i + 1]) else 0)
            temp.append(0)
            cells = temp
            if list_to_int(cells) in dp:
                break
            dp.append(list_to_int(temp))
        
        return [int(bit) for bit in list(format(dp[n % len(dp)], '08b'))] if n > 0 else cells



def main():
    sol = Solution()
    print(sol.prisonAfterNDays(cells = [0,1,0,1,1,0,0,1], n = 7))
    print(sol.prisonAfterNDays(cells = [1,0,0,1,0,0,1,0], n = 1000000000))

if __name__ == '__main__':
    main()