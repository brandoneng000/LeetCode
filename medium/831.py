class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            name, domain = s.split('@')
            return f'{name[0].lower()}*****{name[-1].lower()}@{domain.lower()}'
        else:
            phone = []
            for digit in s:
                if digit.isdigit():
                    phone.append(digit)

            phone = "".join(phone)
            country = '*' * (len(phone) - 10)
            return f'{"+" + country + "-" if country else ""}***-***-{phone[-4:]}'

def main():
    sol = Solution()
    print(sol.maskPII("LeetCode@LeetCode.com"))
    print(sol.maskPII("AB@qq.com"))
    print(sol.maskPII("1(234)567-890"))
    print(sol.maskPII("12(234)567-890"))

if __name__ == '__main__':
    main()