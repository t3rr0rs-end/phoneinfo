import os

wl = input("Windows or linux based (android included in linux) (w or l): ").upper()

if wl == "W":
    os.system('cls')

elif wl == "L":
    os.system('clear')


country_code = input("Enter a country code (+ included, eg. +1 for US +33 for france): ")
number = input("Enter a phone number: ")


if number[0] == "0":
    number = number.lstrip("0")
    number = country_code + number
    print("\nE.164 formatted number:", number)
    print("")

elif number[0] != "0":
    number = country_code + number
    print("\nE.164 Formatted number:", number)
    print("")
