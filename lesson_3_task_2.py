from smartphone import Smartphone

catalog = [
    Smartphone(brand="Apple", model="iPhone 15 Pro", phone_number="+79123456789"),
    Smartphone(brand="Samsung", model="Galaxy S23 Ultra", phone_number="+79876543210"),
<<<<<<< HEAD
    Smartphone(brand="Samsung", mobel="Galaxy S21",phone_number="+79123456789"), 
    Smartphone(brand="Apple", mobel="iPhone 12",phone_number="+79198765432"),
    Smartphone(brand="Xiaomi", mobel="Mi 11", phone_number="+79987654321"),
=======
>>>>>>> 98662cd8ee6ec10a5b6e7c7aab40ec958e21202a
]
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
    
