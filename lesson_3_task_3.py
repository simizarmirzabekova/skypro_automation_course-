from address import Address
from mailing import Mailing

sender = Address(
    index="123456",
    city="Москва",
    street="Ленина",
    house="10",
    apartment="1"
)

recipient = Address(
    index="654321",
    city="Санкт-Петербург",
    street="Невский проспект",
    house="20",
    apartment="2"
)

mail = Mailing(to_address=recipient, from_address=sender, cost=500, track="TRACK12345")

print(
    f"""
Отправление {mail.track} из {mail.from_address.index},
    {mail.from_address.city}, {mail.from_address.street}, {mail.from_address.house} -
    {mail.from_address.apartment} в {mail.to_address.index},
    {mail.to_address.city}, {mail.to_address.street}, {mail.to_address.house} -
    {mail.to_address.apartment}. Стоимость {mail.cost} рублей.
"""
)
