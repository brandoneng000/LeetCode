from typing import List

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        cur_time = 0
        workers = { -1: -1}
        ID = 0
        TIME = 1
        res_id = -1

        for log in logs:
            workers[log[ID]] = max(workers.get(log[ID], 0), (log[TIME] - cur_time))
            cur_time = log[TIME]
        
        for id in workers:
            if workers[id] > workers[res_id]:
                res_id = id
            elif workers[id] == workers[res_id]:
                res_id = min(res_id, id)

        return res_id
        

def main():
    sol = Solution()
    print(sol.hardestWorker(n = 10, logs = [[0,3],[2,5],[0,9],[1,15]]))
    print(sol.hardestWorker(n = 26, logs = [[1,1],[3,7],[2,12],[7,17]]))
    print(sol.hardestWorker(n = 2, logs = [[0,10],[1,20]]))
    print(sol.hardestWorker(n = 2, logs = [[1,10],[0,20]]))

if __name__ == '__main__':
    main()