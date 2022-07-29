import phonenumbers as pn
from phonenumbers  import geocoder, timezone, carrier

number = input("What phone number do you want to locate(with country code)? ")

ro_number = pn.parse(number, "RO")
print(carrier.name_for_number(ro_number, "en"))

parsed_number = pn.parse(number, "CH")
print(geocoder.description_for_number(parsed_number, "en"))

zone_number = pn.parse(number, "GB")
print(timezone.time_zones_for_number(zone_number))

valid_check = pn.is_valid_number(parsed_number)
print(f"Number Valid: {valid_check}")
