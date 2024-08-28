from collections import defaultdict, Counter

def analyze_purchases(purchases: list) -> dict:
    customer_data = defaultdict(lambda: defaultdict(int))
    category_data = defaultdict(Counter)

    for customer_id, category, product in purchases:
        customer_data[customer_id][category] += 1
        category_data[category][product] += 1
    
    # หาสินค้าที่ถูกซื้อบ่อยที่สุดในแต่ละหมวดหมู่
    most_purchased_products = {category: counter.most_common(1)[0][0] for category, counter in category_data.items()}
    
    # รวมข้อมูลทั้งสองแบบในพจนานุกรมเดียว
    result = {**customer_data, **most_purchased_products}
    
    return result

# ตัวอย่างการใช้งาน
purchases = [
    ("cust1", "electronics", "laptop"),
    ("cust2", "groceries", "apple"),
    ("cust1", "electronics", "laptop"),
    ("cust1", "electronics", "mouse"),
    ("cust2", "groceries", "apple"),
    ("cust2", "groceries", "banana"),
    ("cust3", "groceries", "banana"),
    ("cust3", "groceries", "apple"),
    ("cust3", "electronics", "camera")
]

print(analyze_purchases(purchases))
