""" We use topological sort to find the op.
First we build the adjanceny list
Second the Indegree list(increase the count by 1 if any letter is pointing to it e.g. t->f)
Third , using BFS , put the nodes with Indegree 0 and traverse the children of those nodes.
Descrease the Indegree of the neghbor by 1 and if it is 0 add to the queue

Time Complexity: O(V+E).

For indegree list, take two words ata time for comparison, find the min length of the two words.

if at any index the characters are diffreent, then we put first char-> secon_char (t -> f)

adjList[first_char].add(second_char)  and indegreeList[second_char]+=1

["wrt",
 "wrf",
 "er",
 "ett",
 "rftt"]
"""

from collections import deque
class Solution:
    def alienOrder(self, words: [str]) -> str:
        # Initialize and build the Adjacency list and the Indegree List
        adjList = {}
        inDegree = [0 for _ in range(26)]

        for word in words:
            for c in word:
                if c not in adjList:
                    adjList[c] = set()

        for i in range(1, len(words)):
            firstWord = words[i - 1]
            secondWord = words[i]
            if len(firstWord) > len(secondWord) and firstWord.startswith(secondWord):
                return ''
            for j in range(min(len(firstWord), len(secondWord))):
                first_char = firstWord[j]
                second_char = secondWord[j]

                if first_char != second_char:
                    if second_char not in adjList[first_char]:
                        adjList[first_char].add(second_char)
                        inDegree[ord(second_char) - ord('a')] += 1
                    break

            # else:
            #     if len(firstWord) > len(secondWord):
            #         return ''

        # BFS to get the result
        print("indegree:",inDegree)
        q = deque([c for c in adjList if inDegree[ord(c) - ord('a')] == 0])
        print(q)
        res = ""
        while q:
            c = q.popleft()
            res += c
            for neighbor in adjList[c]:
                inDegree[ord(neighbor) - ord('a')] -= 1
                if inDegree[ord(neighbor) - ord('a')] == 0:
                    q.append(neighbor)
        print(adjList)
        print(res)
        return res if len(res) == len(adjList) else ''

sl=Solution()
# Input: words = ["wrt","wrf","er","ett","rftt"]
# Output: "wertf"

words = ["wrt","wrf","er","ett","rftt"]
sl.alienOrder(words)









