class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')

        while len(version1) != len(version2):
            if len(version1) < len(version2):
                version1.append('0')
            else:
                version2.append('0')

        for index in range(len(version1)):
            if int(version1[index]) < int(version2[index]):
                return -1
            elif int(version1[index]) > int(version2[index]):
                return 1

        return 0

def main():
    sol = Solution()
    print(sol.compareVersion(version1 = "1.01", version2 = "1.001"))
    print(sol.compareVersion(version1 = "1.0", version2 = "1.0.0"))
    print(sol.compareVersion("0.1", version2 = "1.1"))

if __name__ == '__main__':
    main()