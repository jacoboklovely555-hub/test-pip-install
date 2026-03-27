#T3 สรุปความยาวประโยค
#โจทย์: รับข้อความหลายประโยค (คั่นด้วย . ? !)
#นับจำนวนประโยค
#หา "ประโยคที่ยาวที่สุด" (วัดจากจำนวนคำ)
#หาค่าเฉลี่ยจำนวนคำต่อประโยค
#ผลลัพธ์: แสดงสถิติ + ประโยคที่ยาวสุด


import re

text = input("กรอกข้อความหลายประโยค:\n")

sentences = re.split(r'[.!?]+', text)
sentences = [s.strip() for s in sentences if s.strip()]

num_sentences = len(sentences)

word_counts = [len(s.split()) for s in sentences]

longest_sentence = sentences[word_counts.index(max(word_counts))]
avg_words = sum(word_counts) / num_sentences

print("จำนวนประโยค:", num_sentences)
print("ค่าเฉลี่ยคำต่อประโยค:", round(avg_words, 2))
print("ประโยคที่ยาวที่สุด:")
print(longest_sentence)



