from PyPDF2 import PdfWriter, PdfReader

class Merge_Pdfs:
    merge_writer = PdfWriter()
    def merge_pdf(self):
        pdf_list = ["./pdf/food.pdf", "./pdf/food_1.pdf"]
        merge = PdfWriter()
        for i in pdf_list:
            print(i)
            merge.append(i)
        merge.write("./pdf/merged_pdf.pdf")

class rotate_pdfs:
    def rotate_pdf(self):
        with open("./pdf/merged_pdf.pdf", mode='rb') as file:
            read_file = PdfReader(file)
            write_file = Merge_Pdfs.merge_writer
            read_pages = read_file.pages[1]
            read_pages.rotate(90)
            with open("./pdf/merged_rotate_index_1.pdf", mode="wb") as rotated_index_1:
                write_file.write(rotated_index_1)

merge_obj = Merge_Pdfs()
rotated_obj = rotate_pdfs()

merge_obj.merge_pdf()
rotated_obj.rotate_pdf()

