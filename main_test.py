import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # June 10.10, July 11.20, August 13.20 -> avg 11.50
    content = open('result1.txt').read()
    print(content)
    regex_test([r'June', r'July', r'August', r'11\.50'], content)

@pytest.mark.T2
def test_main_2():
    # Jan 10, Feb 20, Mar 30 -> avg 20.00
    content = open('result2.txt').read()
    print(content)
    regex_test([r'Jan', r'Feb', r'Mar', r'20\.00'], content)

@pytest.mark.T3
def test_main_3():
    # Mar 50, Apr 60, June 70 -> avg 60.00
    content = open('result3.txt').read()
    print(content)
    regex_test([r'Mar', r'Apr', r'June', r'60\.00'], content)

@pytest.mark.T4
def test_main_4():
    # Sep 5.5, Oct 8.5, Nov 12.0 -> avg 8.67
    content = open('result4.txt').read()
    print(content)
    regex_test([r'Sep', r'Oct', r'Nov', r'8\.67'], content)
