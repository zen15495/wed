def find_single_occurrence_numbers(numbers: list) -> list:
   
    numbers1 = set(numbers)#สร้างเซ็ตของตัวเลขที่มีอยู่ในรายการ
    
    single_occurrence = []#สร้างรายการเก็บตัวเลขที่ปรากฏเพียงครั้งเดียว
    
 
    for number in numbers1:#วนลูปผ่านทุกตัวเลขในเซ็ต numbers1
       
        if numbers.count(number) == 1:#ตรวจสอบว่าตัวเลขปรากฏเพียงครั้งเดียวหรือไม่

            single_occurrence.append(number)#เพิ่มตัวเลขที่ปรากฏเพียงครั้งเดียวในรายการผลลัพธ์
    
    return single_occurrence#ส่งคืนรายการของตัวเลขที่ปรากฏเพียงครั้งเดียว



print(find_single_occurrence_numbers([4, 5, 6, 4, 7, 5, 8])) 
print(find_single_occurrence_numbers([1, 2, 2, 3, 3, 4, 4])) 
print(find_single_occurrence_numbers([1, 2, 3, 4, 5, 6])) 
print(find_single_occurrence_numbers([1, 1, 1, 1, 1]))
 