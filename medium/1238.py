from typing import List

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        def gray_code(n: int):
            return n ^ (n >> 1)
        
        res = [gray_code(i) for i in range(2 ** n)]
        index = res.index(start)

        return res[index:] + res[:index]

    # def circularPermutation(self, n: int, start: int) -> List[int]:
    #     return [start ^ i ^ i >> 1 for i in range(2 ** n)]
        


def main():
    sol = Solution()
    print(sol.circularPermutation(n = 2, start = 3))
    print(sol.circularPermutation(n = 3, start = 2))

if __name__ == '__main__':
    main()