from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        digits = "123456789"

        for size in range(len(str(low)), len(str(high)) + 1):
            for i in range(len(digits) - size + 1):
                num = int(digits[i:i + size])
                if low <= num <= high:
                    res.append(num)
                elif num > high:
                    break
        
        return res
                

def main():
    sol = Solution()
    print(sol.sequentialDigits(100, 300))
    print(sol.sequentialDigits(1000, 13000))

if __name__ == '__main__':
    main()