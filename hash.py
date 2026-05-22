import hashlib
your_text = input("Enter your word: ") # 1. รับข้อความที่ต้องการนำมาแฮช

text_bytes = your_text.encode() # 2. แปลงข้อความให้เป็น bytes ก่อนนำไปแฮช (คล้ายๆ กับการ .encode() ใน Fernet)

hash_object = hashlib.sha256(text_bytes) # 3. ทำการแฮชด้วยอัลกอริทึม SHA-256

hash_result = hash_object.hexdigest() # 4. ดึงผลลัพธ์ออกมาในรูปแบบตัวเลขฐานสิบหก (Hexadecimal string)

print("--- Result after Hashing ---")
print("Original Text:", your_text)
print("After Hashing (SHA-256):", hash_result)


