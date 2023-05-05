class Solution:
    def lastRemaining(self, n: int) -> int:
        # res = set()
        # for i in range(1, n + 1):
        #     res.add(i)
        
        # left_to_right = True
        # start = 1
        # end = n + 1
        # increments = 2
        # while len(res) != 1:
        #     for i in range(start, end, increments):
        #         res.remove(i)
        #     increments *= -2
        #     left_to_right = not left_to_right

        #     if left_to_right:
        #         start = min(res)
        #         end = max(res) + 1
        #     else:
        #         start = max(res)
        #         end = min(res) - 1
        
        # return res.pop()

        left_to_right = True
        remaining = n
        increment = 1
        head = 1
        while remaining > 1:
            if left_to_right or remaining % 2 == 1:
                head += increment
            remaining //= 2
            increment *= 2
            left_to_right = not left_to_right
        
        return head


def main():
    sol = Solution()
    print(sol.lastRemaining(9))
    print(sol.lastRemaining(1))

if __name__ == '__main__':
    main()