class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        return (arrivalTime + delayedTime) % 24
        
def main():
    sol = Solution()
    print(sol.findDelayedArrivalTime(arrivalTime = 15, delayedTime = 5 ))
    print(sol.findDelayedArrivalTime(arrivalTime = 13, delayedTime = 11))

if __name__ == '__main__':
    main()