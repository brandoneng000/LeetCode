from typing import List
from collections import deque

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = deque(['0', '1'])

        for _ in range(n - 1):
            size = len(res)

            for _ in range(size):
                cur = res.popleft()

                if cur[-1] == '0':
                    res.append(cur + '1')
                else:
                    res.append(cur + '0')
                    res.append(cur + '1')
        
        return res
        
def main():
    sol = Solution()
    print(sol.validStrings(3))
    print(sol.validStrings(1))

if __name__ == '__main__':
    main()