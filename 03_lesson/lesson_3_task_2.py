from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "17 pro", "+798230065777"),
    Smartphone("Samsung", "S25 ultra", "+79301234567899"),
    Smartphone("Nokia", "2220", "+79103336666"),
    Smartphone("Poco", "X3 pro", "=79209518588"),
    Smartphone("Xiaomi", "MIX Flip", "+79294294580")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")