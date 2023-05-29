class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a not in b:
            if b in a:
                return 1
            elif b in a + a:
                return 2
            else:
                return -1
        else:
            repeats = b.count(a)
            if a * repeats in b:
                temp = b.split(a * repeats)
                check_b_start = a.endswith(temp[0])
                check_b_end = a.startswith(temp[1])
                if not check_b_start or not check_b_end:
                    return -1
                
                repeats += check_b_start and len(temp[0]) != 0
                repeats += check_b_end and len(temp[1]) != 0
            else:
                return -1
        
        return repeats

def main():
    sol = Solution()
    print(sol.repeatedStringMatch(a = "abc", b = "aabcbabcc"))
    print(sol.repeatedStringMatch(a = "abc", b = "cabcabca"))
    print(sol.repeatedStringMatch(a = "abcd", b = "cdabcdab"))
    print(sol.repeatedStringMatch(a = "a", b = "aa"))

if __name__ == '__main__':
    main()