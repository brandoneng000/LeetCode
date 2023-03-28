class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        if current == correct:
            return 0
        
        cur_hour, cur_min = map(lambda x: int(x), current.split(":"))
        cor_hour, cor_min = map(lambda x: int(x), correct.split(":"))
        operations = [15, 5, 1]
        res = 0
        if cur_min > cor_min:
            minute_diff = (60 - cur_min) + cor_min
            cur_hour += 1
        else:
            minute_diff = cor_min - cur_min
        
        for op in operations:
            num_ops, minute_diff = divmod(minute_diff, op)
            res += num_ops

        if cur_hour > cor_hour:
            res += (24 - cur_hour) + cor_hour
        else:
            res += cor_hour - cur_hour

        return res
        

def main():
    sol = Solution()
    print(sol.convertTime(current = "02:30", correct = "04:35"))
    print(sol.convertTime(current = "11:00", correct = "11:01"))

if __name__ == '__main__':
    main()