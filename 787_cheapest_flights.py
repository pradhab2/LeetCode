#
#
# # Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
#
# from collections import defaultdict
# def cheapest_flight_wo_k(n,flights,src,dst):
#
#     price_list= {i:float('inf') for i in range(n+1)}
#     print("Price_list",price_list)
#     graph=defaultdict(list)
#     for city1,city2,price in flights:
#         graph[city1].append((city2,price))
#     print(graph)
#
#     q=[(src,0)]
#     while q:
#         new_src,cost=q.pop(0)
#         if new_src == dst:
#             continue
#         for neighbor_city,price in graph[new_src]:
#             new_price=cost+price
#             if new_price < price_list[neighbor_city]:
#                 price_list[neighbor_city]=new_price
#                 q.append((neighbor_city,new_price))
#
#     return price_list[dst] if price_list[dst] < float('inf') else -1
#
#
# print(cheapest_flight_wo_k(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3))
# print(cheapest_flight_wo_k(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],2,1))
#
#




# Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1

# from collections import defaultdict
# import heapq
# def cheapest_flight_wo_k(n,flights,src,dst):
#
#     price_list= {i:float('inf') for i in range(n+1)}
#     print("Price_list",price_list)
#     graph=defaultdict(list)
#     for city1,city2,price in flights:
#         graph[city1].append((city2,price))
#     print(graph)
#
#     q=[(src,0)]
#     while q:
#         new_src,cost=heapq.heappop(q)
#         if new_src == dst:
#             continue
#         for neighbor_city,price in graph[new_src]:
#             new_price=cost+price
#             if new_price < price_list[neighbor_city]:
#                 price_list[neighbor_city]=new_price
#                 heapq.heappush(q,((neighbor_city,new_price)))
#
#     return price_list[dst] if price_list[dst] < float('inf') else -1
#
#
# print(cheapest_flight_wo_k(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3))
# print(cheapest_flight_wo_k(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],2,1))


from collections import defaultdict
def cheapest_flight_K_stop(n,flights,src,dst,K):

    price_dict = {i:float('inf') for i in range(n)}
    # price_list = defaultdict(lambda: float('inf'))
    print("Price_list",price_list)
    graph=defaultdict(list)
    for city1,city2,price in flights:
        graph[city1].append((city2,price))
    print(graph)
    stop=0
    q=[(src,0)]
    while q:

        for _ in range(len(q)):
            new_src,cost = q.pop(0)
            if new_src == dst and stop <= K:
                continue
            for neighbor_city,price in graph[new_src]:

                if cost+price < price_list[neighbor_city]:
                    price_dict[neighbor_city]=cost+price
                    q+=[(neighbor_city,cost+price)]
        stop +=1


    return price_list[dst] if price_list[dst] < float('inf') else -1

print(cheapest_flight_K_stop(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1))

# print(cheapest_flight_K_stop(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,50],[2,3,200]],0,3,2))
# print(cheapest_flight_K_stop(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],2,1,1))

