class Solution:
    def rotatedDigits(self, n: int) -> int:
        cache = { '0':'0', '1':'1', '8':'8', '2':'5', '5':'2', '6':'9', '9':'6' }
        res = set()
        for i in range(1, n + 1):
            temp = ""
            for index, d in enumerate(str(i)):
                if d in cache:
                    temp = temp + cache[d]
                else:
                    break
                if index == len(str(i)) - 1 and i != int(temp):
                    res.add(temp)
        
        return len(res)


def main():
    sol = Solution()
    print(sol.rotatedDigits(10))
    print(sol.rotatedDigits(1))
    print(sol.rotatedDigits(2))

if __name__ == '__main__':
    main()