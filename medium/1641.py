from math import comb

class Solution:
    def countVowelStrings(self, n: int) -> int:
        return comb(n + 4, 4)
    
    # def countVowelStrings(self, n: int) -> int:
    #     def helper(size: int, index: int):
    #         if size == n:
    #             self.res += 1
    #             return

    #         for i in range(index, 5):
    #             helper(size + 1, i)

    #     self.res = 0
    #     helper(0, 0)

    #     return self.res
        
def main():
    sol = Solution()
    print(sol.countVowelStrings(1))
    print(sol.countVowelStrings(2))
    print(sol.countVowelStrings(33))

if __name__ == '__main__':
    main()