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
        return page0.split()

    def create_word_length_dict(self):
        words = self.create_word_list()
        word_lens = {}
        for word in words:
            word_lens[word] = len(word)

        return word_lens

    def biggest_word(self):
        word_lens = self.create_word_length_dict()
        lens = word_lens.values()
        bw_len = max(lens)
        bw = word_lens.keys()[word_lens.values().index(bw_len)]

        return bw, bw_len

    def smallest_word(self):
        word_lens = self.create_word_length_dict()
        lens = word_lens.values()
        sw_len = min(lens)
        sw = word_lens.keys()[word_lens.values().index(sw_len)]

        return sw, sw_len

    def average_words(self):
        word_lens = self.create_word_length_dict()
        lens = word_lens.values()

        avg_len = sum(lens) / len(lens)
        
        avg_words = []
        for word, length in word_lens.items():
            if length == avg_len:
                avg_words.append(word)

        return avg_words, avg_len


if __name__ == '__main__':
    reader = FileReader()

    words = reader.create_word_list()
    print "Total number of words: %d\n" % len(words)

    print "Here is a sampling of words from the first page:"
    for i in range(100, 200):
        print words[i],
    print "\n"

    word_lens = reader.create_word_length_dict()
    
    print "A few words and their length..."
    i = 0
    for word, length in word_lens.items():
        print word, length
        i += 1
        if i == 14:
            print "\n"
            break;

    biggest_word, biggest_word_length = reader.biggest_word()
    print "The biggest word in the first page - %s - has %d characters.\n" % (biggest_word, biggest_word_length)

    smallest_word, smallest_word_length = reader.smallest_word()
    print "The smallest word in the first page - %s - has %d characters.\n" % (smallest_word, smallest_word_length)

    average_words, average_word_length = reader.average_words()
    print "The average length of words in the first page is %d" % average_word_length
    print "Each of the following words has a length of %d:" % average_word_length
    for word in average_words:
        print word,
