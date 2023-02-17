import sys
sys.path.append('.')
import shared as sh
import pytest

def test_clean_string():
    test_str = " This! is      a ,test string  "

    assert "This is a test string" == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)


def test_1_equals_1():
    assert 1 == 1, "How does 1 not equal 1?"


def test_space_compress_no_change():
    test_str = "word word word"

    assert "word word word" == sh.space_compress(test_str), "String <{}> not compressed as expected".format(test_str)

def test_space_compress_no_extra_space():
    test_str = "word  word  word"

    assert "word word word" == sh.space_compress(test_str), "String <{}> not compressed as expected".format(test_str)


def test_space_compress_multiline():
    test_str = """word word word
                    second line
                    third line   extra   spaces  
                """

    assert "word word word second line third line extra spaces" == sh.space_compress(test_str), "String <{}> not compressed as expected".format(test_str)

@pytest.mark.xfail
def test_force_fail():
    assert False

@pytest.mark.xfail
def test_space_compress_int():
    test_str = 5
    assert "5" == sh.space_compress(test_str), "Failed"

@pytest.mark.skip(reason="skip intentionally")
def test_skip():
    skip = True
    assert not skip


@pytest.mark.skipif(sys.platform == 'charles', reason = "requires platform other than 'charles' ")
def test_platform():
    print("My platform is", sys.platform)
    assert False
    
    
