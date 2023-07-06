from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        first = []
        second = []
        res = set()
        val = 1

        while val <= bound:
            first.append(val)
            val *= x
            if x == 1:
                break
            
        val = 1
        while val <= bound:
            second.append(val)
            val *= y
            if y == 1:
                break
            
        for i in first:
            for j in second:
                if i + j <= bound:
                    res.add(i + j)
                else:
                    break
        
        return list(res)

def main():
    sol = Solution()
    print(sol.powerfulIntegers(x = 2, y = 3, bound = 10))
    print(sol.powerfulIntegers(x = 3, y = 5, bound = 15))

if __name__ == '__main__':
    main()