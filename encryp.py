from cryptography.fernet import Fernet

text = input("Enter your message: ")

print("\n====================")
print("Original Text: ",text)

key = Fernet.generate_key() #สุ่ม Key(กุญแจที่ใช้เปิด)
print("Key: ",key)

fernet = Fernet(key) #เอา Object ไปเก็บที่ตำแหน่ง *
print("Fernet: ",fernet)

text = fernet.encrypt(text.encode()) #เข้ารหัส(เอาข้อมูลใส่กล้อง แล้วทำการล็อค(Token))
print("====================")
print("Encrypt Text: ",text)
print("====================")

text = fernet.decrypt(text) #เปิดกล่อง
print("Decrypt Text: ",text.decode()) #แปลง Binary
print("====================")

#test
# encrypt เป็นการปกปิด(ปิดกล่อง)
# decrypt เป็นการปล่อย(เปิดกล่อง)

# encode  เป็นกาารแปลงค่าข้อมูลเป็น Binary
# encode  เป็นกาารแปลง Binary เป็นค่าข้อมูล
