from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.task_priority = {}
        self.task_user = {}
        self.heap = []

        for user, task, priority in tasks:
            heappush(self.heap, (-priority, -task, user))
            self.task_priority[task] = priority
            self.task_user[task] = user
        
    def add(self, userId: int, taskId: int, priority: int) -> None:
        heappush(self.heap, (-priority, -taskId, userId))
        self.task_user[taskId] = userId
        self.task_priority[taskId] = priority

    def edit(self, taskId: int, newPriority: int) -> None:
        heappush(self.heap, (-newPriority, -taskId, self.task_user[taskId]))
        self.task_priority[taskId] = newPriority
        

    def rmv(self, taskId: int) -> None:
        self.task_priority[taskId] = -1
        self.task_user[taskId] = -1
        
    def execTop(self) -> int:
        heap = self.heap

        while heap and (-heap[0][0] != self.task_priority[-heap[0][1]] or heap[0][2] != self.task_user[-heap[0][1]]):
            heappop(heap)

        if not heap:
            return -1
        
        priority, task, user = heappop(heap)
        self.task_priority[-task] = -1
        self.task_user[-task] = -1
        return user
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()