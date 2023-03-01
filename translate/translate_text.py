# add encoding to avoid unicode error during writing the translated file

from translate import Translator

text = input("Enter Text: ")
# Write
try:
    with open("../translate/read_file.txt", mode="w") as write_to_read_file:
        write = write_to_read_file.write(text)
        print(write)
except:
    raise FileNotFoundError("File Path Error")


# Translate
translate_text = Translator(to_lang="ja",from_lang="en")
try:
    with open("../translate/read_file.txt", mode="r") as file_read:
        text = file_read.read()
        translated  = translate_text.translate(text)
        print(translated)
        with open("../translate/translated_text.txt", mode="w", encoding="utf-8") as translate_file:        
            translate_file.write(translated)
except:
    raise FileNotFoundError("File Path Error")