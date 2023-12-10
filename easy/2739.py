class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        return (mainTank + min((mainTank - 1) // 4, additionalTank)) * 10
    
    # def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
    #     if mainTank < 5 or additionalTank == 0:
    #         return mainTank * 10
        
    #     used_fuel, extra_fuel = divmod(mainTank, 5)
    #     additional_fuel = min(used_fuel, additionalTank)

    #     return used_fuel * 5 * 10 + self.distanceTraveled(extra_fuel + additional_fuel, additionalTank - additional_fuel)
        
def main():
    sol = Solution()
    print(sol.distanceTraveled(mainTank = 5, additionalTank = 10))
    print(sol.distanceTraveled(mainTank = 1, additionalTank = 2))

if __name__ == '__main__':
    main()