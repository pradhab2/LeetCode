def read_data(file_name):
    data = []
    with open(file_name) as file:
        headers = next(file)  # skip the first line
        for line in file:
            record = make_record(line)
            data.append(record)
    return data


def make_record(line):
    # What one would be the efficient way to represent a row of data
    # tuple? Dict? Class ?
    parts = line.split(',')
    # return line
    # Option 1: Make a tuple (163 MB)
    return (parts[0], parts[1], parts[2], int(parts[3]))

    # Option 2 : Make a Dict (465MB)

    # return {'route': parts[0],
    #         'date': parts[1],
    #         'dayType': parts[2],
    #         'rides': parts[3]}

    # Option 3 : Make an instance of some class (530MB)
    #  Using slots :
#     return Record(parts[0], parts[1], parts[2], int(parts[3]))
#
#
# class Record:
#     __slots__ = ('route','date','dayType','rides')
#     def __init__(self, route, date, dayType, rides):
#         self.route = route
#         self.date = date
#         self.dayType = dayType
#         self.rides = rides


import tracemalloc  # Debugging module for memory utilization

tracemalloc.start()
data = read_data('ctabus.csv')  # 15MB file
print(tracemalloc.get_traced_memory())

# (57955151, 57968155)  Fist one is Peak memory and 2nd one is Current memory use
# (163672851, 163685708)  : with tuple
# (465310613, 465323982)  : with Dictionary
# (530120970, 530134403)  : With Class
# (386294207, 553305425)  : Class using slots method
print(data[0])
print(data[1])
