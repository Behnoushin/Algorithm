# Assign Cookies
# - Given two integer arrays `g` (children’s greed factors) and `s` (cookie sizes).  
# - Each child can receive at most one cookie.  
# - A child i is content if there exists a cookie j such that `s[j] >= g[i]`.  
# - Return the maximum number of content children.  

from typing import List

def findContentChildren(g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()

    i = 0  
    for cookie in s:
        if i >= len(g):
            break
        if cookie >= g[i]:
            i += 1 
    return i
