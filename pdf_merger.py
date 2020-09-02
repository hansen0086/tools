from PyPDF2 import PdfFileMerger
import glob

pdfs = glob.glob("*.pdf")
#pdfs = ['lecture1.pdf', 'lecture2.pdf', 'lecture3.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
