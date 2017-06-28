from nose.tools import *
from articleanalysis.PdfTextMining import PdfTextMining

testpage = "this is a test string for testing a complicated process"
words = testpage.split()

def test_mining_creates_array():
    reader = PdfTextMining(words)
    assert len(reader.word_lens.items()) > 0

def test_biggest_word():
    reader = PdfTextMining(words)
    biggest_word, bw_length = reader.biggest_word()
    assert biggest_word == "complicated"
    assert bw_length == 11

def test_smallest_word():
    reader = PdfTextMining(words)
    smallest_word, sw_length = reader.smallest_word()
    assert smallest_word == "a"
    assert sw_length == 1

def test_biggest_gt_smallest():
    reader = PdfTextMining(words)
    biggest_word, bw_length = reader.biggest_word()
    smallest_word, sw_length = reader.smallest_word()
    assert bw_length > sw_length
