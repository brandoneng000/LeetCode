class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ipv4 = queryIP.split('.')
        if len(ipv4) == 4:
            for index, val in enumerate(ipv4):
                if not val.isdigit():
                    break
                elif val[0] == '0' and (int(val) != 0 or len(val) != 1):
                    break
                elif int(val) < 0 or int(val) > 255:
                    break

                if index == len(ipv4) - 1:
                    return "IPv4"
        else:
            ipv6 = queryIP.split(':')
            if len(ipv6) == 8:
                for index, q in enumerate(ipv6):
                    if len(q) == 0 or len(q) > 4:
                        break
                    try:
                        int(q, 16)
                    except:
                        break
                    
                    if index == len(ipv6) - 1:
                        return "IPv6"

        return "Neither"
        

def main():
    sol = Solution()
    print(sol.validIPAddress("172.16.254.1"))
    print(sol.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
    print(sol.validIPAddress("256.256.256.256"))

if __name__ == '__main__':
    main()