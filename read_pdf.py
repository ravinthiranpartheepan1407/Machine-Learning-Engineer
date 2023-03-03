from PyPDF2 import PdfReader, PdfWriter

def read_page_index():
    with open('./pdf/food.pdf', mode='rb') as file:
        read_file = PdfReader(file)
        page = read_file.pages[0]
        text = page.extract_text()
        print(text)

def rotate_page():
    with open("./pdf/food.pdf", mode='rb') as file:
        read_file = PdfReader(file)
        read_page = read_file.pages[0]
        rotate_pdf = read_page.rotate(90)
        write_file = PdfWriter()
        with open("./pdf/rotated-file.pdf", mode='wb') as rotated_file:
            write_file.write(rotated_file)

read_page_index()
rotate_page()
