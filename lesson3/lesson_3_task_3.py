from address import Address
from mailing import Mailing

from_address = Address(344000, 'Rostov', 'Pushkinskaya', '1', '1')
to_address = Address(100330, 'Moscow', 'Pushkina', '2/3', '5')
mailing = Mailing(to_address, from_address, 20000, 'ksdjfkj55465')

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city},"
      f" {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}."
      f"Стоимость {mailing.cost} рублей.")