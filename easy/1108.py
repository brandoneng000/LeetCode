class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
        
def main():
    sol = Solution()
    print(sol.defangIPaddr("1.1.1.1"))

if __name__ == '__main__':
    main()