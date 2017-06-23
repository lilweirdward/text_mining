from pyPdf import PdfFileReader

class FileReader(object):
    def __init__(self):
        self.filename = 'docs/FJTurner-Frontier_Significance-1893.pdf'
        self.pdf = PdfFileReader(open(self.filename, "rb"))

    def set_pdf(self, filename):
        self.pdf = PdfFileReader(open(filename, "rb"))

    def page_to_string(self, pagenum=0):
        return self.pdf.pages[pagenum].extractText()

    def create_word_list(self):
        page0 = self.page_to_string()
        self.words = page0.split()

    def create_word_length_dict(self):
        self.word_lens = {}
        for word in self.words:
            self.word_lens[word] = len(word)


if __name__ == '__main__':
    reader = FileReader()
    reader.create_word_list()

    print len(reader.words)

    for i in range(100, 200):
        print reader.words[i],

    reader.create_word_length_dict()
    
    i = 0
    for word, length in reader.word_lens.items():
        print word, length
        i += 1
        if i == 14:
            break;
