class Solution:
    def maxPower(self, s: str) -> int:
        power = 0
        count = 0
        cur = ""

        for letter in s:
            if letter == cur:
                count += 1
            else:
                cur = letter
                count = 1

            if count > power:
                power = count
            
        return power
        
def main():
    sol = Solution()
    print(sol.maxPower("leetcode"))

if __name__ == '__main__':
    main()