# https://leetcode.com/problems/word-pattern
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """Given a pattern and a string s, find if s follows the same pattern (i.e., if there's a letter-to-word mapping)."""
        words = s.split()
        if len(pattern) != len(words):
            return False

        mapping = {}
        for i in range(len(words)):
            if pattern[i] not in mapping:
                if words[i] in mapping.values():  # alternative: add another mapping
                    return False
                mapping[pattern[i]] = words[i]
            elif mapping[pattern[i]] != words[i]:
                return False
        return True


def test_solution():
    assert Solution().wordPattern("abba", "dog cat cat dog") is True
    assert Solution().wordPattern("abba", "dog cat cat fish") is False
    assert Solution().wordPattern("aaaa", "dog cat cat dog") is False
    assert Solution().wordPattern("abba", "dog dog dog dog") is False
    assert Solution().wordPattern("ab", "dog dog") is False
    assert Solution().wordPattern("ab", "dog cat") is True
    assert Solution().wordPattern("ab", "dog dog") is False
