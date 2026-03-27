#ex3 จงหา Library สำหรับทำการดึงข้อมูลเกียวกับไฟร DF ที่สนใจทั้งขนาดของไฟล์ จำนวนหน้า
#ประเภทของเอกสาร รวมทั้งการดึงข้อมูล Text และภาพแยกออกจากกันจากไฟล์ตระกูล PDF

import fitz   
import os

pdf_file = "dev-example.pdf"


file_size = os.path.getsize(pdf_file) / 1024
print("ขนาดไฟล์:", round(file_size,2), "KB")

file_type = os.path.splitext(pdf_file)[1]
print("ประเภทไฟล์:", file_type)

doc = fitz.open(pdf_file)

print("จำนวนหน้า:", doc.page_count)

all_text = ""

for page_num in range(doc.page_count):
    page = doc.load_page(page_num)
    text = page.get_text()
    all_text += text

with open("text_output.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("บันทึกข้อความลง text_output.txt เรียบร้อย")


image_count = 0

for page_num in range(doc.page_count):
    page = doc.load_page(page_num)
    images = page.get_images()

    for img in images:
        xref = img[0]
        base_image = doc.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]

        image_name = f"image_{image_count}.{image_ext}"

        with open(image_name, "wb") as img_file:
            img_file.write(image_bytes)

        image_count += 1

print("จำนวนภาพที่ดึงออก:", image_count)
