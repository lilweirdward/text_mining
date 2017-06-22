import pyPdf

pdf = pyPdf.PdfFileReader(open("docs/FJTurner-Frontier_Significance-1893.pdf", "rb"))

for i, page in enumerate(pdf.pages):
    print "Page %d" % i
    print page.extractText()
