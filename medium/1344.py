class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = (hour * 30) % 360 + (minutes / 60 * 30)
        minute_angle = minutes * 6

        return min(abs(hour_angle - minute_angle), 360 - abs(hour_angle - minute_angle))

def main():
    sol = Solution()
    print(sol.angleClock(hour = 1, minutes = 57))
    print(sol.angleClock(hour = 12, minutes = 30))
    print(sol.angleClock(hour = 3, minutes = 30))
    print(sol.angleClock(hour = 3, minutes = 15))

if __name__ == '__main__':
    main()