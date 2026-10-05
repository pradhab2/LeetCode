
import unittest
def isIsomorphic( s: str, t: str) -> bool:
    d = {}
    visited = set()

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] in d:
            if d[s[i]] != t[i]:
                return False
        else:
            if t[i] in visited:
                return False
            d[s[i]] = t[i]
            visited.add(t[i])
    return True

# If we can check the first occurrence of the each character in both the strings are equal
# then the strings are Isomorphic

def isIsomorphic2(s:str,t:str) -> bool:
    return list(map(s.find,s))==list(map(t.find,t))

def isIsomorphic3(s:str,t:str) -> bool:  # Here in find(c) gives the index of the character c
    return [s.find(c) for c in s]==[t.find(c) for c in t]


assert isIsomorphic("egg","add")== True
assert isIsomorphic2("egg","add")== True
assert isIsomorphic3("egg","add")== True