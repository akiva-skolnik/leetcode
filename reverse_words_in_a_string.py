# https://leetcode.com/problems/reverse-words-in-a-string
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(w.strip() for w in reversed(s.split()))


def test():
    s = Solution()
    assert s.reverseWords("the sky is blue") == "blue is sky the"
    assert s.reverseWords("  hello world!  ") == "world! hello"
    assert s.reverseWords("a good   example") == "example good a"
    assert s.reverseWords("  Bob    Loves  Alice   ") == "Alice Loves Bob"
    assert s.reverseWords("Alice does not even like bob") == "bob like even not does Alice"
