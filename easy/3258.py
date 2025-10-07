class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        left = 0
        count_zero = 0
        count_one = 0
        res = 0

        for right in range(n):
            if s[right] == '0':
                count_zero += 1
            elif s[right] == '1':
                count_one += 1
        
            while count_zero > k and count_one > k:
                if s[left] == '0':
                    count_zero -= 1
                elif s[left] == '1':
                    count_one -= 1
                left += 1
            
            res += right - left + 1
        
        return res

def main():
    sol = Solution()
    print(sol.countKConstraintSubstrings(s = "10101", k = 1))
    print(sol.countKConstraintSubstrings(s = "1010101", k = 2))
    print(sol.countKConstraintSubstrings(s = "11111", k = 1))

if __name__ == '__main__':
    main()