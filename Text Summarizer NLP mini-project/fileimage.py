from PIL import Image
from pytesseract import pytesseract

def displaytext(image_path1):
    # Defining paths to tesseract.exe
    # and the image we would be using
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    # image_path = r'C:\Users\Admin\Downloads\ximg.png';

    # Opening the image & storing it in an image object
    img = Image.open(image_path1, mode='r')
    
    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract

    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img)

    # Displaying the extracted text
    return text[:-1]

