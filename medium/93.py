from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # Have 12 digits max per IP Address
        # Digits are between 0 and 255 inclusive
        # No leading 0s
        def check(ip: str) -> bool:
            if len(ip) > 3 or not ip:
                return False
            if len(ip) > 1 and ip[0] == '0':
                return False
            if len(ip) and int(ip) > 255:
                return False
            return True

        def ip_address(result: List[str], address: str, s: str, index: int, dots: int):
            if dots == 3:
                if check(s[index:]):
                    result.append(address + s[index:])
                return
            for i in range(index, min(index + 3, len(s))):
                if check(s[index: i+1]):
                    new_address = address + s[index: i+1] + '.'
                    ip_address(result, new_address, s, i+1, dots+1)
        
        result = []
        ip_address(result, "", s, 0, 0)
        return result


def main():
    sol = Solution()
    print(sol.restoreIpAddresses("25525511135"))
    print(sol.restoreIpAddresses("0000"))
    print(sol.restoreIpAddresses("101023"))

if __name__ == '__main__':
    main()