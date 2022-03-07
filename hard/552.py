class Solution:
    def checkRecord(self, n: int) -> int:
        not_absent = 2
        not_late = 2
        first_late = 1
        not_late_or_absent = 1
        first_late_not_absent = 1
        all_valid = 3
        mod_val = 10**9 + 7

        for index in range(n - 1):
            add_absent = not_absent
            add_present = all_valid
            all_valid = add_absent + not_late + first_late + add_present

            not_absent, not_late_or_absent, first_late_not_absent = not_absent + not_late_or_absent \
                + first_late_not_absent, not_absent, not_late_or_absent
            not_late, first_late = add_absent + add_present, not_late

        return all_valid  % mod_val
        
        # def record(attendence: str, total: int):
        #     if (attendence.count('A') >= 2 or "LLL" in attendence):
        #         return 0
        #     if len(attendence) == total:
        #         return 1

        #     absent = record(attendence + 'A', total)
        #     late = record(attendence + 'L', total)
        #     present = record(attendence + 'P', total)

        #     return absent + late + present
        
        # absent = record('A', n)
        # late = record('L', n)
        # present = record('P', n)

        # return (absent + late + present) % (10**9 + 7)

def main():
    sol = Solution()
    print(sol.checkRecord(10))
    # print(sol.checkRecord(1))

if __name__ == '__main__':
    main()