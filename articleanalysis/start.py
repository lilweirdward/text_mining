from PdfTextMining import PdfTextMining
from PyPDF2 import PdfFileReader

def PdfToString():
    filename = 'docs/FJTurner-Frontier_Significance-1893.pdf'
    pdf = PdfFileReader(open(filename, "rb"))
    pagenum = 0
    page0 = pdf.pages[pagenum].extractText()
    words = page0.split()
    return words

words = PdfToString()
reader = PdfTextMining(words)

print "Total number of words: %d\n" % len(words)

print "Here is a sampling of words from the first page:"
for i in range(100, 200):
    print words[i],
print "\n"

print "A few words and their length..."
i = 0
for word, length in reader.word_lens.items():
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
