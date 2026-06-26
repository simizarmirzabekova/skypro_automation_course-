from smartphone import Smartphone

catalog = [
    Smartphone(brand="Apple", model="iPhone 15 Pro", phone_number="+79123456789"),
    Smartphone(brand="Samsung", model="Galaxy S23 Ultra", phone_number="+79876543210"),
    ...
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
    