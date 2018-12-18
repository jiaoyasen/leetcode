
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        result = self.dfs(employees,id)
        return result
    def dfs(self,employees,id):
        result = 0
        for i in range(len(employees)):
            if employees[i].id == id:
                result += employees[i].importance
                if len(employees[i].subordinates) != 0:
                    for j in employees[i].subordinates:
                        result += self.dfs(employees, j)
        return result


test = Solution()
employees = [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]]
id = 1
print(test.getImportance(employees,id))


