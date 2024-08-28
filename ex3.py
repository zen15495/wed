def word_frequency(text: str) -> dict:
    # แปลงข้อความทั้งหมดให้เป็นตัวพิมพ์เล็ก
    text = text.lower()
    
    # แยกข้อความออกเป็นคำโดยใช้ space เป็นตัวแบ่ง
    words = text.split()
    
    # สร้างพจนานุกรมสำหรับเก็บจำนวนครั้งที่พบคำแต่ละคำ
    frequency = {}
    
    # นับจำนวนครั้งที่พบคำแต่ละคำในข้อความ
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

# ตัวอย่างการใช้งาน
print(word_frequency("Hello world! Hello everyone."))   
print(word_frequency("This is a test. This test is easy."))  
print(word_frequency("Python is fun. Fun fun fun!"))   
print(word_frequency("One word, one word."))   