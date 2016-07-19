import os

from PyPDF2 import PdfFileMerger, PdfFileReader

merger = PdfFileMerger()

files = [x for x in os.listdir('pdfs') if x.endswith('.pdf')]
for fname in sorted(files):
    merger.append(PdfFileReader(open(os.path.join('pdfs', fname), 'rb')))

merger.write("output.pdf")
