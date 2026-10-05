"""Given a log of website requests, where each line contains an entry with the following fields (time,
customerId, pageVisited) in it represents a request made by customer at time T to one of the website's
pages, write algorithm to find the top 3-page sequence visited given a list of log entries.
For example, given the following log file containing:
T0,C1,A
T0,C2,E
T1,C1,B
T1,C2,B
T2,C1,C
T2,C2,C
T3,C1,D
T3,C2,D
T4,C1,E
T5,C2,A
We can see that we have two customers, and we know that customer C1 visited the pages
A -> B -> C -> D -> E (visiting order matters) and customer C2 visited
E -> B -> C -> D -> A, then we can tell that the overall most visited sequence of 3
pages is is B -> C -> D because it occurs twice. If there is more than one solution,
return the alphabetically smallest such 3-sequence.

// input is an array of strings where each line is a string
input = ["T0,C1,A","T0,C2,E","T1,C1,B","T1,C2,B","T2,C1,C","T2,C2,C","T3,C1,D","T3,C2,D","T4,C1,E","T5,C2,A"]
"""
from collections import defaultdict
def small_page_seq(input):
    cust_dict=defaultdict(list)
    for rec in input:
        tm,cust,pg=rec.split(",")
        cust_dict[cust].append(pg)
    # print(cust_dict)
    new_dict=defaultdict(lambda:0)
    for rec in cust_dict.values():
        for i in range(len(rec)-2):
            new_list=(rec[i],rec[i+1],rec[i+2])
            new_dict[new_list] += 1

    res=[]
    for key,val in new_dict.items():
        if val > 1:
            res.append(key)
    print(res)


input = ["T0,C1,A","T0,C2,E","T1,C1,B","T1,C2,B","T2,C1,C","T2,C2,C","T3,C1,D","T3,C2,D","T4,C1,E","T5,C2,A"]
small_page_seq(input)



