class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        login_hour, login_min = int(loginTime[:2]), int(loginTime[3:])
        logout_hour, logout_min = int(logoutTime[:2]), int(logoutTime[3:])
        
        login_time = login_hour * 60 + login_min
        logout_time = logout_hour * 60 + logout_min

        if 0 <= logout_time - login_time < 15:
            return 0
        
        return logout_time // 15 - (login_time + 14) // 15 + (login_time > logout_time) * 96


def main():
    sol = Solution()
    print(sol.numberOfRounds(loginTime = "23:46", logoutTime = "00:01"))
    print(sol.numberOfRounds(loginTime = "00:01", logoutTime = "00:00"))
    print(sol.numberOfRounds(loginTime = "09:31", logoutTime = "10:14"))
    print(sol.numberOfRounds(loginTime = "21:30", logoutTime = "03:00"))

if __name__ == '__main__':
    main()        