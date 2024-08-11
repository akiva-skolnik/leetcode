from typing import List


# https://leetcode.com/problems/text-justification
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line = words[0]
        for word in words[1:]:
            if len(line) + len(word) < maxWidth:
                line += (" " + word) if line else word
            else:
                if " " in line:
                    spaces = len(line.replace(" ", ""))
                    n = (maxWidth - spaces) // line.count(" ")
                    if n > 1:
                        line = line.replace(" ", " " * n)
                    line = line.replace(" " * n, " " * (n + 1), maxWidth - len(line))
                else:
                    line += " " * (maxWidth - len(line))
                lines.append(line)
                line = word

        while "  " in line:
            line = line.replace("  ", " ")
        line += " " * (maxWidth - len(line))
        lines.append(line)
        return lines


def test_1():
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    assert Solution().fullJustify(words, maxWidth) == [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]


def test_2():
    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    assert Solution().fullJustify(words, maxWidth) == [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]


def test_3():
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
             "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
    maxWidth = 20
    assert Solution().fullJustify(words, maxWidth) == [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    ]
