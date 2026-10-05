import csv
import tracemalloc
tracemalloc.start()
from operator import itemgetter

#with open('/Users/balarampradhan/Desktop/Portfolio.tab', 'r') as infile:
with open('ctabus.csv', 'r') as infile:
    hdr = next(infile)
    # data = [tuple(line) for line in csv.reader(file, delimiter=',')]
    data = csv.reader(infile, delimiter=',')
    print(type(data))
    #sort = sorted(data, key=itemgetter(2))
    #sort = sorted(data, key=lambda item: (int(item[3]), int(item[2])))
    sort = sorted(data, reverse=True, key=lambda item: (int(item[3]), item[2]))
    print(type(sort))
    #print(sort)
    infile.close()
    print(tracemalloc.get_traced_memory())


with open('/Users/balarampradhan/Desktop/CTAsortedOut.txt', 'w') as ofile:
    for ln in sort:
        ofile.write(','.join(ln) + '\n')
    print(tracemalloc.get_traced_memory())
ofile.close()

