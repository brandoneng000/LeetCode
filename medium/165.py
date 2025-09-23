class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        m, n = len(v1), len(v2)

        for i in range(max(m, n)):
            cur1 = int(v1[i]) if i < m else 0
            cur2 = int(v2[i]) if i < n else 0

            if cur1 < cur2:
                return -1
            elif cur1 > cur2:
                return 1
        
        return 0


    # def compareVersion(self, version1: str, version2: str) -> int:
    #     version1 = version1.split('.')
    #     version2 = version2.split('.')

    #     while len(version1) != len(version2):
    #         if len(version1) < len(version2):
    #             version1.append('0')
    #         else:
    #             version2.append('0')

    #     for index in range(len(version1)):
    #         if int(version1[index]) < int(version2[index]):
    #             return -1
    #         elif int(version1[index]) > int(version2[index]):
    #             return 1

    #     return 0

def main():
    sol = Solution()
    print(sol.compareVersion(version1 = "1.2", version2 = "1.10"))
    print(sol.compareVersion(version1 = "1.01", version2 = "1.001"))
    print(sol.compareVersion(version1 = "1.0", version2 = "1.0.0"))
    print(sol.compareVersion(version1 = "0.1", version2 = "1.1"))

if __name__ == '__main__':
    main()