import PyPDF2

template = PyPDF2.PdfFileReader(
    open('mainPDF.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(
    open('img.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('merged.pdf', 'wb') as file:
        output.write(file)
