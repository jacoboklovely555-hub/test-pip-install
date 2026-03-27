#T1 นับคำและความถี่คำ (Word Frequency)
#โจทย์: รับข้อความ 1 ย่อหน้า แล้วหาว่า
#มีทั้งหมดกี่คำ   คำที่พบบ่อยสุด 10 อันดับแรก (ไม่สนใจตัวพิมพ์ใหญ่-เล็ก)
#เงื่อนไขเพิ่ม: ตัดเครื่องหมายวรรคตอนออก (,1?.;")
#ผลลัพธ์: แสดงตารางคำกับจำนวน

import re
from collections import Counter

def text_processing_demo(text):
    # ลบอักขระพิเศษและ Emoji (ใช้ regex) [cite: 10]
    clean_text = re.sub(r'[^\w\s\.]', '', text) 
    # แปลงเป็น lowercase และลบช่องว่างซ้ำ [cite: 9]
    clean_text = " ".join(clean_text.lower().split())
    
    #T1 Word Frequency 
    # ตัดเครื่องหมายวรรคตอนออกเพิ่มเติมสำหรับนับคำ [cite: 6]
    words = re.findall(r'\b\w+\b', clean_text)
    word_count = len(words) # [cite: 5]
    freq = Counter(words).most_common(10) # 10 อันดับแรก [cite: 6]
    
    print(f"ข้อความหลังทำความสะอาด: {clean_text}")
    print(f"จำนวนคำทั้งหมด: {word_count} คำ")
    print("10 อันดับคำที่พบบ่อย:")
    for word, count in freq:
        print(f"{word}: {count}")



