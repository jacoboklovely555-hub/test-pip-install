#T5: ทำดัชนีค้นหา (Mini Search Engine)
#โจทย์: มีไฟล์ข้อความหลายไฟล์ในโฟลเดอร์
#สร้างดัชนีคำ → รายชื่อไฟล์ที่พบคำนั้น
#ผู้ใช้พิมพ์คำค้น 1 คำ แล้วแสดงรายชื่อไฟล์ที่เกี่ยวข้องผลลัพธ์: แสดงผลแบบ sorted ตามจำนวนครั้งที่พบ

import os
import re
from collections import Counter
def mini_search_engine(folder_path, search_word):
   # 1. สร้าง Dictionary สำหรับเก็บดัชนี (Index)
   # โครงสร้าง: { "파일명": จำนวนที่พบ }
   index_data = {}
   # 2. อ่านไฟล์ทั้งหมดในโฟลเดอร์
   if not os.path.exists(folder_path):
       print("ไม่พบโฟลเดอร์ที่ระบุ")
       return
   files = [f for f in os.listdir(folder_path) if f.endswith('.txt')]
   for filename in files:
       file_path = os.path.join(folder_path, filename)
       with open(file_path, 'r', encoding='utf-8') as f:
           content = f.read().lower() # แปลงเป็นตัวเล็กเพื่อให้อ่านง่าย
           # ใช้ regex หาคำที่ต้องการ (แบบ Case-insensitive)
           # ในที่นี้ใช้ findall เพื่อนับจำนวนครั้งที่ปรากฏ
           matches = re.findall(re.escape(search_word.lower()), content)
           if matches:
               index_data[filename] = len(matches)
   # 3. แสดงผลลัพธ์แบบ Sorted ตามจำนวนครั้งที่พบ (จากมากไปน้อย)
   sorted_results = sorted(index_data.items(), key=lambda x: x[1], reverse=True)
   print(f"\n--- ผลการค้นหาคำว่า: '{search_word}' ---")
   if not sorted_results:
       print("ไม่พบคำที่ค้นหาในไฟล์ใดเลย")
   else:
       for filename, count in sorted_results:
           print(f"ไฟล์: {filename} | พบทั้งหมด: {count} ครั้ง")
# --- วิธีใช้งาน ---
# สมมติว่ามีโฟลเดอร์ชื่อ 'my_docs'
# search_term = input("ป้อนคำที่ต้องการค้นหา: ")
# mini_search_engine('my_docs', search_term)
