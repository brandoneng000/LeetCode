from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = { str(i):0 for i in range(n) }
        stack = [logs[0].split(':')[0]]
        prev_time = 0

        for log in logs[1:]:
            prog, status, time = log.split(':')
            if status == "start":
                if stack:
                    times[stack[-1]] += int(time) - prev_time
                stack.append(prog)
                prev_time = int(time)
            elif status == "end":
                times[prog] += int(time) - prev_time + 1
                stack.pop()
                prev_time = int(time) + 1

        return [times[key] for key in times]

def main():
    sol = Solution()
    print(sol.exclusiveTime(n = 3, logs = ["0:start:0","0:end:0","1:start:1","1:end:1","2:start:2","2:end:2","2:start:3","2:end:3"]))
    print(sol.exclusiveTime(n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]))
    print(sol.exclusiveTime(n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))
    print(sol.exclusiveTime(n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))

if __name__ == '__main__':
    main()