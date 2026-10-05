# Read and operate a file most efficiently
# One idea is to put column of data into a list
# Use Datetime.date format to store date attributes
# caching

def _cached(obj,cache={}):
    return cache.setdefault(obj,obj)

import datetime
def read_file(filename):

    route=[]
    dates=[]
    dayType=[]
    rides=[]
    with open('ctabus.csv') as file:
        hdr=next(file)
        for line in file:
            record=line.split(',')
            route.append(_cached(record[0]))
            # If we store Data values in Date(datetime.date) format rather in String format, it consumes less memory
            mon, day, year=record[1].split('/')
            dates.append(_cached(datetime.date(int(year),int(mon),int(day))))
            #dates.append(record[1])
            dayType.append(record[2])
            rides.append(int(record[3]))
    return(route,dates,dayType,rides)

import tracemalloc
tracemalloc.start()
data=read_file('ctabus.csv')
print(tracemalloc.get_traced_memory())

print(data[0][0],data[1][0],data[2][0],data[3][0])


# Storing in columns (143187641, 143200965) : 143 MB
# Date being stored in date format (123303418, 123316657): 123 MB
# Using Object caching for routes and Dates (44629818, 44643809) : 44 MB

# Using Pandas



