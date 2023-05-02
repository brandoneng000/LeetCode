from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        if a == 1:
            return 1
        if len(b) == 1 and b[0] == 0:
            return 1
        
        vals = []
        check = set()
        product = 1 

        while True:
            product *= a
            num = product % 1337
            if num in check:
                break
            else:
                check.add(num)
                vals.append(num)
        b = int("".join([str(x) for x in b]))

        return vals[(b % len(vals)) - 1]



def main():
    sol = Solution()
    print(sol.superPow(a = 2, b = [3]))
    print(sol.superPow(a = 2, b = [1,0]))
    print(sol.superPow(a = 1, b = [4,3,3,8,5,2]))
    print(sol.superPow(a = 78267, b = [4,3,3,8,5,2]))

if __name__ == '__main__':
    main()