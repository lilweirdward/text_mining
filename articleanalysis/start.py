from pyPdf import PdfFileReader

def get_pdf(filename):
    return PdfFileReader(open(filename, "rb"))

def page_to_string(pdf, pagenum=0):
    return pdf.pages[pagenum].extractText()


pdf = get_pdf('docs/FJTurner-Frontier_Significance-1893.pdf')

for pagenum in range(0, pdf.getNumPages() / 4):
    print "Page %d" % pagenum
    print page_to_string(pdf, pagenum)
