from typing import List

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        start = 0
        res = []
        
        for i in range(1, n + 1):
            start ^= i
        
        cur = 0
        for en in encoded:
            cur ^= en
            start ^= cur
        
        res.append(start)
        for en in encoded:
            res.append(en ^ res[-1])
        
        return res


def main():
    sol = Solution()
    print(sol.decode([3,1]))
    print(sol.decode([6,5,4,6]))

if __name__ == '__main__':
    main()