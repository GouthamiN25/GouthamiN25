#Anagram Groups 
#Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

#An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return res.values()
