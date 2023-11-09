from itertools import groupby

class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 1000000007
        res = 0

        for c, s in groupby(s):
            n = len(list(s))
            res += n * (n + 1) // 2
        
        return res % mod

    # def countHomogenous(self, s: str) -> int:
    #     def sum_of_count(count: int):
    #         return (count + 1) * count // 2
        
    #     mod = 1000000007
    #     res = 0
    #     cur_letter = ''
    #     cur_count = 0

    #     for i, letter in enumerate(s):
    #         if letter == cur_letter:
    #             cur_count += 1

    #         if letter != cur_letter:
    #             res += sum_of_count(cur_count)
    #             cur_letter = letter
    #             cur_count = 1
        
    #     return (res + sum_of_count(cur_count)) % mod

def main():
    sol = Solution()
    print(sol.countHomogenous("abbcccaa"))
    print(sol.countHomogenous("xy"))
    print(sol.countHomogenous("zzzzz"))

if __name__ == '__main__':
    main()