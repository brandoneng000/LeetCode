from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        cur = 1
        for _ in range(n):
            res.append(cur)
            if cur * 10 <= n:
                cur *= 10
            elif (cur % 10 != 9 and cur + 1 <= n):
                cur += 1
            else:
                while (cur // 10) % 10 == 9:
                    cur //= 10
                cur = cur // 10 + 1
        
        return res
    
        # res = []

        # for i in range(1, n + 1):
        #     res.append(str(i))
        
        # res.sort()
        # return [int(val) for val in res]
        
def main():
    sol = Solution()
    print(sol.lexicalOrder(33))
    print(sol.lexicalOrder(13))
    print(sol.lexicalOrder(2))

if __name__ == '__main__':
    main()