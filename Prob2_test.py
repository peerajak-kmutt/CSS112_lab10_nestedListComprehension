import Prob2 as p2;

def test_1():
    atext='The split method is used to split the strings and store them in the list. The built-in method returns a list of the words in the string, using the “delimiter” as the delimiter string. If a delimiter is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace.'
    ans = 'xxx split method is used to split xxx strings and store them in xxx list. xxx built-in method returns a list of xxx words in xxx string, using xxx “delimiter” as xxx delimiter string. If a delimiter is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and xxx result will contain no empty strings at xxx start or end if xxx string has leading or trailing whitespace.'
    assert p2.Problem2(atext) == ans

