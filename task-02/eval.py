from PIL import Image
import pytesseract
img = Image.open("expression_1.png")
extracted_text = pytesseract.image_to_string(img)
expression = extracted_text.strip()
try:
    result = eval(expression)
    print(f"The result of '{expression}' is: {result}")
except Exception as e:
    print(f"Error: {e}")
