from typing import List
from heapq import heappush, heappop

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        res = []
        positive = set(positive_feedback)
        negative = set(negative_feedback)

        for r, id in zip(report, student_id):
            cur = 0

            for word in r.split():
                if word in positive:
                    cur += 3
                
                if word in negative:
                    cur -= 1
                
            heappush(res, (cur, -id))

            if len(res) > k:
                heappop(res)
        
        return [-id for score, id in sorted(res, reverse=True)]

        
def main():
    sol = Solution()
    print(sol.topStudents(positive_feedback = ["fkeofjpc","qq","iio"], negative_feedback = ["jdh","khj","eget","rjstbhe","yzyoatfyx","wlinrrgcm"], 
                          report = ["rjstbhe eget kctxcoub urrmkhlmi yniqafy fkeofjpc iio yzyoatfyx khj iio","gpnhgabl qq qq fkeofjpc dflidshdb qq iio khj qq yzyoatfyx","tizpzhlbyb eget z rjstbhe iio jdh jdh iptxh qq rjstbhe","jtlghe wlinrrgcm jnkdbd k iio et rjstbhe iio qq jdh","yp fkeofjpc lkhypcebox rjstbhe ewwykishv egzhne jdh y qq qq","fu ql iio fkeofjpc jdh luspuy yzyoatfyx li qq v","wlinrrgcm iio qq omnc sgkt tzgev iio iio qq qq","d vhg qlj khj wlinrrgcm qq f jp zsmhkjokmb rjstbhe"], 
                          student_id = [1,2,3,4,5,6,7,8], k = 3))
    print(sol.topStudents(positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is studious","the student is smart"], student_id = [1,2], k = 2))
    print(sol.topStudents(positive_feedback = ["smart","brilliant","studious"], negative_feedback = ["not"], report = ["this student is not studious","the student is smart"], student_id = [1,2], k = 2))

if __name__ == '__main__':
    main()