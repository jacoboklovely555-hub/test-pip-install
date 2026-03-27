#ex1 จงหา Library สำหรับทำการดึงข้อมูล Text จากหน้าเว็บไซต์ที่เราต้องการ www.sc.su.ac.th
import requests

url = "https://www.sc.su.ac.th"
response = requests.get(url)

print(response.text)
