import collections
import heapq

class Solution:
    def largestInteger(self, num: int) -> int:
        evens = []
        odds = []
        temp = num
        res = 0

        while temp:
            remainder = temp % 10
            if remainder % 2:
                odds.append(-remainder)
            else:
                evens.append(-remainder)
            temp //= 10
        heapq.heapify(evens)
        heapq.heapify(odds)

        for digit in list(str(num)):
            res *= 10
            if int(digit) % 2:
                res += -heapq.heappop(odds)
            else:
                res += -heapq.heappop(evens)
        
        return res
        

def main():
    sol = Solution()
    print(sol.largestInteger(1234))
    print(sol.largestInteger(65875))

if __name__ == '__main__':
    main()