def find_repeated_substrings(s: str) -> list:
    substring_count = {}
    
    # ตรวจสอบอักขระย่อยทั้งหมดในสตริง
    for i in range(len(s)):
        for j in range(i + 2, len(s) + 1):
            substring = s[i:j]
            if substring in substring_count:
                substring_count[substring] += 1
            else:
                substring_count[substring] = 1
    
    # เก็บเฉพาะอักขระย่อยที่ซ้ำกัน (มีจำนวนครั้งที่พบมากกว่า 1)
    repeated_substrings = [substring for substring, count in substring_count.items() if count > 1]
    
    return repeated_substrings
   
print(find_repeated_substrings("banana"))
print(find_repeated_substrings("abcdefg")) 
print(find_repeated_substrings("abcabcabc")) 
print(find_repeated_substrings("aaaa"))  