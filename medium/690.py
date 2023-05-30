from typing import List
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_db = {}
        for employee in employees:
            employee_db[employee.id] = (employee.importance, employee.subordinates)
        
        def dfs(id: int):
            imp, subs = employee_db[id]
            for sub in subs:
                imp += dfs(sub)
            
            return imp

        return dfs(id)