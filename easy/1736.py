class Solution:
    def maximumTime(self, time: str) -> str:
        res = []
        
        if time[0] == '?':
            if time[1] == '?':
                res.append('2')
            else:
                if int(time[1]) < 4:
                    res.append('2')
                else:
                    res.append('1')
        else:
            res.append(time[0])

        if time[1] == '?':
            if res[0] == '2':
                res.append('3')
            else:
                res.append('9')
        else:
            res.append(time[1])
        
        res.append(':')
        if time[3] == '?':
            res.append('5')
        else:
            res.append(time[3])
        
        if time[4] == '?':
            res.append('9')
        else:
            res.append(time[4])

        return "".join(res)

        
def main():
    sol = Solution()
    print(sol.maximumTime("2?:?0"))
    print(sol.maximumTime("0?:3?"))
    print(sol.maximumTime("1?:22"))
    print(sol.maximumTime("?4:03"))

if __name__ == '__main__':
    main()