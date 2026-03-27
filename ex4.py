#ex4จงหา Library สำหรับทำการดึงข้อมูลจากไฟล์ภาพที่มีตัวอักษรภาษาอังกฤษที่ปรากฏอยู่ในภาพ เรียกการทำนี้ว่า OCR

from PIL import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\STATSCSU\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
os.environ["TESSDATA_PREFIX"] = r"C:\Users\STATSCSU\AppData\Local\Programs\Tesseract-OCR\tessdata"

img = Image.open(r"C:\Users\STATSCSU\Downloads\image.png")

text = pytesseract.image_to_string(img, lang="eng")

print(text)

