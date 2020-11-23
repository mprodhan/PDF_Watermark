import PyPDF2
import sys

template = PyPDF2.PdfFileReader(open('./pdf_files/super.pdf', 'rb'))
# this variable reads the super.pdf file.
watermark = PyPDF2.PdfFileReader(open('./pdf_files/wtr.pdf', 'rb'))
# this variable is used in the for loop to then access the file and merger
# merge them with super.pdf, which is the combination of all other pdfs
# not mentioned.
output = PyPDF2.PdfFileWriter()
# this variable is used in writing the output on the for loop to get
# the new file from that loop, as watermarked.pdf.

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    # this method is taking the watermark from the file and binding it
    # to super.pdf, so that all pages contain the watermakr.
    output.addPage(page)

    with open('watermarked_output.pdf', 'wb') as f:
        output.write(f)