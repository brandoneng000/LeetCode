from typing import List
import collections

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def time_to_mins(time: str):
            hour, minutes = time.split(":")
            return int(hour) * 60 + int(minutes)

        card_usage = collections.defaultdict(list)
        name_time = sorted((time_to_mins(time), name) for name, time in zip(keyName, keyTime))
        res = set()

        for time, name in name_time:
            if name not in res:
                card_usage[name].append(time)

                if len(card_usage[name]) > 2:
                    if card_usage[name][-1] - card_usage[name][-3] <= 60:
                        res.add(name)
        
        return sorted(res)

def main():
    sol = Solution()
    print(sol.alertNames(keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]))
    print(sol.alertNames(keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]))

if __name__ == '__main__':
    main()