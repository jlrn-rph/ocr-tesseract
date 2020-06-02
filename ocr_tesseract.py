# importing necessary libraries 
# adds image processing capabilities
from PIL import Image

# convert image to text string
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# translates into preferred language
from googletrans import Translator

########### EXTRACTING IMAGE AND PROCESS TEXT EXTRACTION ###########

# assign image from a source path
img = Image.open('img/fitzgerald.png')

# convert image and save to result variable
result = pytesseract.image_to_string(img)

########### CONVERT IT TO ANOTHER LANGUAGE ###########
translate = Translator()

# translates text into French
translate_to_french = translate.translate(result, dest='chinese')

# converts the result into string
translated = str(translate_to_french.text)