import phonenumbers
from test import number

from phonenumbers import geocoder
ch_nmber = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_nmber, "en"))

# Country History = CH => Histori Negara (list negara berdasar no HP)

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))

# Relationship Officer = RO => Provider yang kita ingin tahu 