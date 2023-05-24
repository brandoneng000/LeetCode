from typing import List
import heapq
import collections
import string

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = list(collections.Counter(tasks).values())
        max_freq = max(freq)
        max_freq_count = freq.count(max_freq)
        
        res = (max_freq - 1) * (n + 1) + max_freq_count
        return max(res, len(tasks))

    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     task_counter = collections.Counter(tasks)
    #     max_freq = max(task_counter.values())
    #     freq = list(task_counter.values())
    #     max_freq_letter = 0
    #     i = 0
    #     while i < len(freq):
    #         if freq[i] == max_freq:
    #             max_freq_letter += 1
    #         i += 1
        
    #     res = (max_freq - 1) * (n + 1) + max_freq_letter
    #     return max(res, len(tasks))
    
    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     heap = []
    #     task_counter = collections.Counter(tasks)
    #     size = len(tasks)
    #     cooldown = { letter: 0 for letter in string.ascii_uppercase }
    #     res = 0
    #     temp = []
        
    #     for key in task_counter:
    #         heapq.heappush(heap, (-task_counter[key], key))
    #         cooldown[key] = n
    #         temp.append(key)
        
    #     for key in temp:
    #         task_counter[key] -= 1
    #         if task_counter[key] == 0:
    #             task_counter.pop(key)

    #     while size > 0:
    #         temp = []
    #         if heap:
    #             val, letter = heapq.heappop(heap)
    #             cooldown[letter] = n + 1
    #             size -= 1
    #             res += 1
    #         elif not heap:
    #             res += 1
    #         for key in task_counter:
    #             if cooldown[key] > 0:
    #                 cooldown[key] -= 1
    #             if cooldown[key] == 0:
    #                 temp.append(key)
    #         for key in temp:
    #             heapq.heappush(heap, (-task_counter[key], key))
    #             task_counter[key] -= 1
    #             if task_counter[key] == 0:
    #                 task_counter.pop(key)
        
    #     return res

def main():
    sol = Solution()
    print(sol.leastInterval(tasks = ["A","A","A","B","B","B"], n = 2))
    print(sol.leastInterval(tasks = ["A","A","A","B","B","B"], n = 0))
    print(sol.leastInterval(tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2))

if __name__ == '__main__':
    main()