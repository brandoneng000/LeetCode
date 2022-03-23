from typing import List
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            log_data = log.split(" ", maxsplit=1)
            if log_data[1].replace(" ", "").isalpha():
                letter_logs.append(log)
            else:
                digit_logs.append(log)
        
        letter_logs.sort(key= lambda x: x.split()[0])
        letter_logs.sort(key= lambda x: x.split()[1:])
        return letter_logs + digit_logs
        

def main():
    sol = Solution()
    print(sol.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))

if __name__ == '__main__':
    main()