class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        TEN_FOUR = 10000
        TEN_NINE = 1000000000
        volume = length * height * width
        bulky = volume >= TEN_NINE or length >= TEN_FOUR or height >= TEN_FOUR or width >= TEN_FOUR
        heavy = mass >= 100

        if bulky and heavy:
            return 'Both'
        elif bulky or heavy:
            return 'Bulky' if bulky else 'Heavy'
        else:
            return 'Neither'

        

def main():
    sol = Solution()
    print(sol.categorizeBox(length = 1000, width = 35, height = 700, mass = 300))
    print(sol.categorizeBox(length = 200, width = 50, height = 800, mass = 50))

if __name__ == '__main__':
    main()