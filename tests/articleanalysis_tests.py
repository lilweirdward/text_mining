from nose.tools import *
from articleanalysis.start import FileReader

def test_basic():
    reader = FileReader()
    assert reader.pdf.getNumPages() > 0
