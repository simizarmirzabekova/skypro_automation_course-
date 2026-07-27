from lesson1.smartphone import Smartphone

catalog = [
    Smartphone(brand="Apple", model="iPhone 15 Pro", phone_number="+79123456789"),
    Smartphone(brand="Samsung", model="Galaxy S23 Ultra", phone_number="+79876543210"),

    Smartphone(brand="Samsung", mobel="Galaxy S21",phone_number="+79123456789"), 
    Smartphone(brand="Apple", mobel="iPhone 12",phone_number="+79198765432"),
    Smartphone(brand="Xiaomi", mobel="Mi 11", phone_number="+79987654321")

]
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
    
