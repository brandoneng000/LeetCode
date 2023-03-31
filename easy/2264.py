class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""

        for index in range(len(num) - 2):
            triplet = num[index: index + 3]
            if len(set(triplet)) == 1:
                res = max(res, triplet)

        return res

def main():
    sol = Solution()
    print(sol.largestGoodInteger("6777133339"))
    print(sol.largestGoodInteger("2300019"))
    print(sol.largestGoodInteger("42352338"))

if __name__ == '__main__':
    main()