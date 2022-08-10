class Solution:
    def secondHighest(self, s: str) -> int:
        largest = -1
        second = -1
        
        for char in set(s):
            if char.isnumeric():
                check = int(char)
                if check > largest:
                    second = largest
                    largest = check
                elif check > second:
                    second = check
        
        return second
        
        
def main():
    sol = Solution()
    print(sol.secondHighest("dfa12321afd"))
    print(sol.secondHighest("abc1111"))
    print(sol.secondHighest("1234567890"))

if __name__ == '__main__':
    main()