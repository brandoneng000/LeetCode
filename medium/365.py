class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        def GCD(num1, num2):
            while num2:
                temp = num2
                num2 = num1 % num2
                num1 = temp
            return num1
        
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        if jug1Capacity == targetCapacity or jug2Capacity == targetCapacity or jug2Capacity + jug1Capacity == targetCapacity:
            return True
        
        return targetCapacity % GCD(jug1Capacity, jug2Capacity) == 0

    
def main():
    sol = Solution()
    print(sol.canMeasureWater(3, 5, 4))
    print(sol.canMeasureWater(2, 6, 5))
    print(sol.canMeasureWater(1, 2, 3))
    print(sol.canMeasureWater(1, 1, 9))

if __name__ == '__main__':
    main()