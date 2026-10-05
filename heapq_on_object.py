import heapq

# class definition
class employee:

    # constructor
    def __init__(self, n, d, yos, s):
        self.name = n
        self.des = d
        self.yos = yos
        self.sal = s

    # function for customized printing
    def print_me(self):
        print("Name :", self.name)
        print("Designation :", self.des)
        print("Years of service :", str(self.yos))
        print("salary :", str(self.sal))

    # override the comparison operator
    def __lt__(self, nxt):
        return self.yos > nxt.yos and nxt.name >self.name


# creating objects
e1 = employee('Anish', 'manager', 3, 24000)
e2 = employee('kathy', 'programmer', 2, 15000)
e3 = employee('Rina', 'Analyst', 5, 30000)
e4 = employee('Vinay', 'programmer', 1, 10000)
e5 = employee('Bina', 'Analyst', 5, 30000)

# list of employee objects
emp = [e1, e2, e3, e4, e5]

# converting to min-heap
# based on yos
heapq.heapify(emp)

# printing the results
for i in range(0, len(emp)):
    heapq.heappop(emp).print_me()
    print()
