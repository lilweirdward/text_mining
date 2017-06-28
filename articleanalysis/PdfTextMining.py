class PdfTextMining:
    """ Class for doing text mining on a given string """
    def __init__(self, words):
        self.word_lens = {}
        if len(words) != 0:
            for word in words:
                self.word_lens[word] = len(word)

            self.lens = self.word_lens.values()

    def set_word_lens(self, words):
        self.word_lens = {}
        for word in words:
            self.word_lens[word] = len(word)

        self.lens = self.word_lens.values()

    def biggest_word(self):
        bw_len = max(self.lens)
        bw = self.word_lens.keys()[self.word_lens.values().index(bw_len)]

        return bw, bw_len

    def smallest_word(self):
        sw_len = min(self.lens)
        sw = self.word_lens.keys()[self.word_lens.values().index(sw_len)]

        return sw, sw_len

    def average_words(self):
        avg_len = sum(self.lens) / len(self.lens)
        
        avg_words = []
        for word, length in self.word_lens.items():
            if length == avg_len:
                avg_words.append(word)

        return avg_words, avg_len
