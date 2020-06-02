from ocr_tesseract import *

########### EXPORT RESULTS INTO TEXT DOCUMENT ###########
with open('test2.txt', mode='w', encoding='utf-8') as file:
    file.write(result)
    file.write("\n")
    file.write(translated)
    file.close()
    print("Ready!")