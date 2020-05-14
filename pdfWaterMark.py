import PyPDF2
import sys
#* Takes 2 files: a pdf file which will be watermarked and the other pdf file is a watermark file

files = sys.argv[1:]
pdf_file = files[0]
wtr_file = files[1]

def user_input():
    print('What is the name of the file you want to save the new pdf?')
    new_pdf = input()
    return new_pdf

def pdf_watermarker(new_pdf):
    pdf = PyPDF2.PdfFileReader(open(pdf_file, 'rb'))
    wtr = PyPDF2.PdfFileReader(open(wtr_file, 'rb'))
    output = PyPDF2.PdfFileWriter()
    num_pages = pdf.getNumPages()
    
    for i in range(num_pages):
        pdf_page = pdf.getPage(i)
        wtr_page = wtr.getPage(0)
        pdf_page.mergePage(wtr_page)
        output.addPage(pdf_page)

    output.write(open(new_pdf,'wb'))    


def main():
    new_pdf = user_input()
    pdf_watermarker(new_pdf)
    print('All Done')

main()