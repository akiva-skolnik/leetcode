from collections import Counter


# https://www.algoexpert.io/questions/generate-document
def generateDocument(characters: str, document: str) -> bool:
    """returns True if the characters can generate the document"""
    return not Counter(document) - Counter(characters)


def test():
    tests = [{'characters': 'Bste!hetsi ogEAxpelrt x ',
              'document': 'AlgoExpert is the Best!',
              'expected': True},
             {'characters': 'A', 'document': 'a', 'expected': False},
             {'characters': 'a', 'document': 'a', 'expected': True},
             {'characters': 'a hsgalhsa sanbjksbdkjba kjx',
              'document': '',
              'expected': True},
             {'characters': ' ', 'document': 'hello', 'expected': False},
             {'characters': '     ', 'document': '     ', 'expected': True},
             {'characters': 'aheaollabbhb', 'document': 'hello', 'expected': True},
             {'characters': 'aheaolabbhb', 'document': 'hello', 'expected': False},
             {'characters': 'estssa', 'document': 'testing', 'expected': False},
             {'characters': 'Bste!hetsi ogEAxpert',
              'document': 'AlgoExpert is the Best!',
              'expected': False},
             {'characters': 'helloworld ', 'document': 'hello wOrld', 'expected': False},
             {'characters': 'helloworldO', 'document': 'hello wOrld', 'expected': False},
             {'characters': 'helloworldO ', 'document': 'hello wOrld', 'expected': True},
             {'characters': '&*&you^a%^&8766 _=-09     docanCMakemthisdocument',
              'document': 'Can you make this document &',
              'expected': True},
             {'characters': 'abcabcabcacbcdaabc',
              'document': 'bacaccadac',
              'expected': True}]

    for test in tests:
        characters, document, expected = test['characters'], test['document'], test['expected']
        r = generateDocument(characters, document)
        assert r == expected, f"expected {expected} but got {r}"
