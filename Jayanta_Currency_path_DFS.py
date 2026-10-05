# from collections import defaultdict
# class findPathExist():
#
#     def genAdjecentList(self,currencies)->dict():
#         res=defaultdict(list)
#         for currency in currencies:
#             res[currency[0]].append((currency[1],currency[2]))
#         return res
#
#     def findExistence(self, currencies, srcCur, dstCur):
#         adjList=self.genAdjecentList(currencies)
#         return self.dfs(adjList,srcCur,dstCur,set())
#
#     # def dfs(self, adjList, srcCur, dstCur, visited):
#     #     if dstCur == srcCur:
#     #         return True
#     #     if srcCur not in adjList:
#     #         return False
#     #     elif srcCur not in visited:
#     #         visited.add(srcCur)
#     #         for rec in adjList[srcCur]:
#     #             return self.dfs(adjList, rec[0], dstCur, visited)
#     #
#     #     # return False
#
#     def dfs(self,adjList, srcCur, dstCur, visited):
#         if dstCur == srcCur:
#             return True
#         if srcCur not in adjList:
#             return False
#         elif srcCur not in visited:
#             visited.add(srcCur)
#             for rec in adjList[srcCur]:
#                 boolFlg = self.dfs(adjList,rec[0],dstCur,visited)
#                 if boolFlg:
#                     return True
#         return boolFlg   # return False
#
#
# obj=findPathExist()
# currencies=[('USD','JPY',10),
#             ('JPY','ZAR',30),
#             ('USD','GBP',20),
#             ('GBP','CAD',40),
#             ('JPY','NGN',60),
#             ('NGN','INR',20)]
# print(obj.findExistence(currencies,'USD','CAD'))
# print(obj.findExistence(currencies,'NGN','CAD'))
# print(obj.findExistence(currencies,'GBP','INR'))



        # Given list of cities and the travel cost.
# cities = [
#   ("SFO", "MIA", "10"),
#   ("SFO", "SEA", "30"),
#   ("SFO", "LAX", "10"),
#   ("LAX", "HOU", "10"),
#   ("SEA", "HOU", "20")]
#
#   Find the path which incur minimum travel cost.
#   If there is no path exists return ["No path exists"]
#
#   Case1:
#   find_min_path(cities,"SFO","HOU")
#   expected output  ["SFO","LAX","HOU"]
#
#   Case2:
#   find_min_path(cities,"SFO","JFW")
#   expected output  ["No path exists"]
#
#   Case3:
#   find_min_path(cities,"SEA","HOU")
#   expected output  ["SEA","HOU"]
import collections
from collections import defaultdict

import heapq
class Solution():

    # def path_exists(self, cities, src, dst):
    #     adj_list = defaultdict(list)
    #     for rec in cities:
    #         adj_list[rec[0]].append(rec[1])
    #         # adj_list[rec[1]].append(rec[0])
    #
    #     def dfs(cities, src, dst, visited, path):
    #         if src == dst:
    #             return True, path + '->' + src
    #         if src not in visited:
    #             visited.add(src)
    #
    #         for city in adj_list[src]:
    #             if city not in visited:
    #                 res, final_path = dfs(cities, city, dst, visited, path + '->' + src)
    #                 if res:
    #                     return "Path exists", final_path.lstrip('->')
    #         return False, "Path dos not exists"
    #
    #     return dfs(cities, src, dst, set(), '')

    def min_cost_travel_heap(self,cities,src,dst):
        graph = collections.defaultdict(dict)
        for city1, city2, price in cities:
            graph[city1][city2] = price
        print(graph) # {'SFO': {'MIA': 10, 'SEA': 30, 'LAX': 10}, 'LAX': {'HOU': 10}, 'SEA': {'HOU': 20}})
        path=src
        q=[(0,src,path)]

        while q:
            # print(q)
            cost,nxt_src,path=heapq.heappop(q)
            if nxt_src == dst:
                return cost,path
            for neighbor in graph[nxt_src]:
                    heapq.heappush(q, (cost + graph[nxt_src][neighbor], neighbor, path +'-'+neighbor))

        return -1,''

    def min_cost_travel_dijkstra(self,cities,src,dst):
        graph = collections.defaultdict(list)
        price_dict=collections.defaultdict(lambda: float('inf'))  # will keep {destination: min cost} for each connecting city from source
        for city1, city2, price in cities:
            graph[city1] += [(city2,price)]
        # print(graph) #  {'SFO': [('MIA', 10), ('SEA', 30), ('LAX', 10)], 'LAX': [('HOU', 10)], 'SEA': [('HOU', 20)]})
        path = src
        q=[(0,src,path)]
        while q:
            # print(q)
            cost,nxt_src,path=q.pop(0)
            if nxt_src == dst:
                continue
            for neighbor, p in graph[nxt_src]:
                if cost+p >= price_dict[neighbor]:
                    continue
                else:
                    price_dict[neighbor] = cost+p
                    q+= [(cost + p, neighbor, path +'-'+neighbor)]
        # print("price dict:", price_dict)
        return price_dict[dst],path if price_dict[dst] < float('inf') else -1

# cities = [
#     ("SFO", "MIA", "10"),
#     ("SFO", "SEA", "30"),
#     ("SFO", "LAX", "10"),
#     ("LAX", "HOU", "10"),
#     ("SEA", "HOU", "20")]
# sl = Solution()
# print(sl.path_exists(cities, 'SFO', 'HOU'))
# print(sl.path_exists(cities, 'LAX', 'SEA'))
cities = [
    ("SFO", "MIA", 10),
    ("SFO", "SEA", 30),
    ("SFO", "LAX", 10),
    ("LAX", "HOU", 10),
    ("SEA", "HOU", 20)]

sl = Solution()
# print(sl.min_cost_travel_heap(cities, 'SFO', 'HOU'))
# print(sl.min_cost_travel(cities, 'SEA', 'MIA'))

print(sl.min_cost_travel_dijkstra(cities, 'SFO', 'HOU'))
# print(sl.min_cost_travel_dijkstra(cities, 'SEA', 'MIA'))
