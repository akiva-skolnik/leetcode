import itertools
from collections import Counter, defaultdict
from typing import List


# https://leetcode.com/problems/group-anagrams
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Given an array of strings strs, group the anagrams together. You can return the answer in any order.
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
            using all the original letters exactly once."""
        counters_per_length = defaultdict(list)
        output_per_length = defaultdict(list)
        for s in strs:
            length = len(s)
            s_counter = Counter(s)
            if s_counter not in counters_per_length[length]:
                counters_per_length[length].append(s_counter)
                output_per_length[length].append([s])
            else:
                index = counters_per_length[length].index(s_counter)
                output_per_length[length][index].append(s)
        return list(itertools.chain.from_iterable(output_per_length.values()))


def test_solution():
    assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"],
                                                                                    ["tan", "nat"], ["bat"]]
    assert Solution().groupAnagrams([""]) == [[""]]
    assert Solution().groupAnagrams(["a"]) == [["a"]]
    assert Solution().groupAnagrams(["a", "b"]) == [["a"], ["b"]]
