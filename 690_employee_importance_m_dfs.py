"""
You have a data structure of employee information, including the employee's unique ID, importance value, and direct subordinates' IDs.

You are given an array of employees employees where:

employees[i].id is the ID of the ith employee.
employees[i].importance is the importance value of the ith employee.
employees[i].subordinates is a list of the IDs of the direct subordinates of the ith employee.
Given an integer id that represents an employee's ID, return the total importance value of this employee and all their direct and indirect subordinates.

Example 1:

                  (ID = 1, Importance = 5)
                  /                     \
    (ID = 2, Importance = 3)     (ID = 3, Importance = 3)

Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
Output: 11
Explanation: Employee 1 has an importance value of 5 and has two direct subordinates: employee 2 and employee 3.
They both have an importance value of 3.
Thus, the total importance value of employee 1 is 5 + 3 + 3 = 11.

"""
from typing import List
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        emp_dict = {emp.id:emp for emp in employees}

        def helper(id:int):
            emp = emp_dict[id]
            total_importance = emp.importance
            for subordinate in emp.subordinates:
                total_importance += helper(subordinate)
            return total_importance

        return helper(id)


e1=Employee(1,5,[2,3])
e2=Employee(2,3,[])
e3=Employee(3,3,[])

sl=Solution()
print(sl.getImportance([e1,e2,e3],1))
# print(sl.getImportance([e1,e2,e3],2))



