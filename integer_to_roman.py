# https://leetcode.com/problems/integer-to-roman
class Solution:
    def intToRoman(self, num: int) -> str:
        roman_mapping = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        subtractive_forms = {4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
        result = []
        i = 0
        while num > 0:
            num, last_digit = divmod(num, 10)
            if last_digit in (4, 9):
                result.append(subtractive_forms[last_digit * 10 ** i])
            elif last_digit != 0:
                last_digit *= 10 ** i
                temp_result = []
                for n, c in reversed(roman_mapping.items()):
                    if last_digit >= n:
                        temp_result.extend([c] * (last_digit // n))
                        last_digit -= n * (last_digit // n)
                        if last_digit == 0:
                            break
                result.extend(temp_result[::-1])
            i += 1
        return "".join(reversed(result))


def test():
    assert Solution().intToRoman(3) == "III"
    assert Solution().intToRoman(4) == "IV"
    assert Solution().intToRoman(40) == "XL"
    assert Solution().intToRoman(3749) == "MMMDCCXLIX"
    assert Solution().intToRoman(58) == "LVIII"
    assert Solution().intToRoman(1994) == "MCMXCIV"
