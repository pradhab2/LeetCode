# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
# Return any possible rearrangement of s or return "" if not possible.
# # Example 1:
# Input: s = "aab"
# Output: "aba"
# Example 2:
# Input: s = "aaab"
# Output: ""

from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        c = Counter(s)
        hp = [(-value, key) for key, value in c.items()]
        heapq.heapify(hp)

        pre_a, pre_b = 0, ""
        while hp:
            a, b = heapq.heappop(hp)
            res.append(b)
            a += 1
            if (pre_a < 0):
                heapq.heappush(hp, (pre_a, pre_b))

            pre_a, pre_b = a, b
        return "".join(res) if len(res)== len(s) else ""

if __name__ == '__main__':
    sl=Solution();
    # print(sl.reorganizeString('aaabbbb'))   # Should return blank
    print(sl.reorganizeString('aaab'))   # Should return blank
