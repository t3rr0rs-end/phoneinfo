import phonenumbers
from phonenumbers import timezone, carrier, geocoder
import os

print("")
print("UNIX BASED SYSTEMS: Android, Linux, Mac OS")
print("Windows System")
u_or_w = input("Are you running on a Unix based system or windows? (u or w): ").upper()

if u_or_w == "U":
    os.system('clear')
else:
    os.system('cls')

pn1 = input("Enter a phone number in E.164 format (country code included): ")

print("")
print("-"*30)
pn2 = phonenumbers.parse(pn1, None)
print(pn2)

print("Valid Phone Number:", phonenumbers.is_valid_number(pn2))
print("Possible Phone Number:", phonenumbers.is_possible_number(pn2))

print("")

print("National Format:", phonenumbers.format_number(pn2, phonenumbers.PhoneNumberFormat.NATIONAL))
print("International Format:", phonenumbers.format_number(pn2, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
print("E.164 Format:" , phonenumbers.format_number(pn2, phonenumbers.PhoneNumberFormat.E164))

print("")

ch_number = phonenumbers.parse(pn1, "CH")
print("Country or City of Phone Number:", geocoder.description_for_number(ch_number, "en"))

print("")

ro_number = phonenumbers.parse(pn1, "RO")
print("Carrier:", carrier.name_for_number(ro_number, "en"))

print("")

tz_number = phonenumbers.parse(pn1, "GB")
print("Timezone of Phone number:", timezone.time_zones_for_number(tz_number))
print("-"*30, "\n")