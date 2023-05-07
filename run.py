import pytesseract
from PIL import Image

img = Image.open('test_slide.png')
text = pytesseract.image_to_string(img)
print(text)

print("---------- crop.png -------------")
img = Image.open('crop.png')
text = pytesseract.image_to_string(img)
print(text)

