from math import isqrt

class Solution:
    def countTriples(self, n: int) -> int:
        res = 0

        for a in range(1, n + 1):
            for b in range(1, n + 1):
                total = (a * a) + (b * b)
                root = isqrt(total)
                res += total % root == 0 and total // root == root and root <= n
        
        return res

    # def countTriples(self, n: int) -> int:
    #     nums = [num * num for num in range(1, n + 1)]
    #     result = 0

    #     for first_num in nums:
    #         for second_num in nums:
    #             result += first_num + second_num in nums

    #     return result

def main():
    sol = Solution()
    print(sol.countTriples(5))
    print(sol.countTriples(10))
    print(sol.countTriples(250))

if __name__ == '__main__':
    main()