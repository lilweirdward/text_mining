from nose.tools import *
from articleanalysis.start import FileReader

def test_reader_pdf_is_useful():
    reader = FileReader()
    assert reader.pdf.getNumPages() > 0

def test_reader_has_words():
    reader = FileReader()
    reader.create_word_list()
    assert len(reader.words) > 0
