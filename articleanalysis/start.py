from pyPdf import PdfFileReader

class FileReader(object):
    def __init__(self):
        self.filename = 'docs/FJTurner-Frontier_Significance-1893.pdf'
        self.pdf = PdfFileReader(open(self.filename, "rb"))

    def set_pdf(self, filename):
        self.pdf = PdfFileReader(open(filename, "rb"))

    def page_to_string(self, pagenum=0):
        return self.pdf.pages[pagenum].extractText()

    def create_word_dict(self):
        page0 = self.page_to_string()
        self.words = page0.split()


if __name__ == '__main__':
    reader = FileReader()

    for pagenum in range(0, reader.pdf.getNumPages() / 4):
        print "Page %d" % pagenum
        print reader.page_to_string(pagenum)
