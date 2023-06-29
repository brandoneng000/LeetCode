import collections

class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 1000000007
        moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

        count = collections.Counter([0,1,2,3,4,5,6,7,8,9])
        res = 0

        for _ in range(n - 1):
            next = collections.Counter()
            for key in count:
                for move in moves[key]:
                    next[move] += count[key]
            count = next
        
        return sum(count.values()) % mod



def main():
    sol = Solution()
    print(sol.knightDialer(1))
    print(sol.knightDialer(2))
    print(sol.knightDialer(3131))

if __name__ == '__main__':
    main()