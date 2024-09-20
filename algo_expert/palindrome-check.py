# https://www.algoexpert.io/questions/palindrome-check
def isPalindrome(string):
    return string == string[::-1]


def test():
    tests = [{'expected': True, 'string': 'abcdcba'},
             {'expected': True, 'string': 'a'},
             {'expected': False, 'string': 'ab'},
             {'expected': True, 'string': 'aba'},
             {'expected': False, 'string': 'abb'},
             {'expected': True, 'string': 'abba'},
             {'expected': True, 'string': 'abcdefghhgfedcba'},
             {'expected': True, 'string': 'abcdefghihgfedcba'},
             {'expected': False, 'string': 'abcdefghihgfeddcba'}]

    for test in tests:
        assert isPalindrome(test['string']) == test['expected']
