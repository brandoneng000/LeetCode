from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 + 32]

def main():
    sol = Solution()
    print(sol.convertTemperature(36.50))
    print(sol.convertTemperature(122.11))

if __name__ == '__main__':
    main()