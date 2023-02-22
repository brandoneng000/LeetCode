class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        box = {}

        for balls in range(lowLimit, highLimit + 1):
            balls = sum(int(ball) for ball in list(str(balls)))
            box[balls] = box.get(balls, 0) + 1
        
        return max(box.values())

def main():
    sol = Solution()
    print(sol.countBalls(1, 10))
    print(sol.countBalls(5, 15))
    print(sol.countBalls(19, 28))
    print(sol.countBalls(1, 100000))

if __name__ == '__main__':
    main()