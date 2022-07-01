from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # res = [0] * (n + 1)

        # for index in range(1, len(res)):
        #     res[index] = str(bin(index)).count("1")

        # return res

        # all numbers are either 2N(evens) or 2N+1(odds)
        # doubling a number appends an additional "0" to the end
        # adding "1" is when an additional 1 is appended
        res = [0]

        for index in range(1, n + 1):
            res.append(res[index // 2] + index % 2)
        
        return res


        
def main():
    sol = Solution()
    print(sol.countBits(2))
    print(sol.countBits(5))

if __name__ == '__main__':
    main()