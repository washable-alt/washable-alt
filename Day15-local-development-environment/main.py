from data import contacts,data

try:
    # Access a dictionary of dictionaries
    print(contacts["James"]["email"])

    # Access a list of dictionaries
    print(data[0]["name"])

    # Enumerate method for accessing a list of dictionaries
    for index, element in enumerate(data):
        print(index)
        print(element)
        if element['name'] == 'Jenny':
            print(element['phone_number'])

except Exception as e:
    print(e)