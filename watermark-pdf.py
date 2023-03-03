from PyPDF2 import PdfReader, PdfWriter

def watermark_pdf():
    with open("./pdf/merged_pdf.pdf", mode="rb") as file:
        read_file = PdfReader(file)
        watermark = PdfReader(open("./pdf/watermark.pdf", "rb"))
        output = PdfWriter()

        for i in range(len(read_file.pages)):
            page = read_file.pages[i]
            page.merge_page(watermark.pages[0])
            output.add_page(page)
            
            with open("./pdf/watermarked_pdf.pdf", mode='wb') as watermarkd_pdf:
                output.write(watermarkd_pdf)

watermark_pdf()