class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if numOnes >= k:
            return k
        if numOnes + numZeros >= k:
            return numOnes
        k -= numOnes
        k -= numZeros
        return numOnes - min(k, numNegOnes)

def main():
    sol = Solution()
    print(sol.kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 2))
    print(sol.kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4))

if __name__ == '__main__':
    main()