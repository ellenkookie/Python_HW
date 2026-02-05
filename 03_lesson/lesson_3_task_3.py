from address import Address
from mailing import Mailing

to_address = Address("123456", "Москва", "Шишкова", "10", "15")
from_address = Address("654321", "Санкт-Петербург", "Пушкина", "5", "3")

mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=500,
    track="TRACK123477"
)

print(f"Отправление {mailing.track} из {mailing.from_address.index}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} в "
      f"{mailing.to_address.index}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} - "
      f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")