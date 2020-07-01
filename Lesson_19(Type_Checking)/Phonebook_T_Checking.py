import json
import sys
from typing import List, Dict, Any

print(sys.argv)
if len(sys.argv) < 2:
    print('Please, specify json file name')
    exit()

phonebook_var = sys.argv[1]
phone_book_file = open(phonebook_var)
try:
    main_dict: Any = json.load(phone_book_file)
except json.decoder.JSONDecodeError:
    main_dict = []
phone_book_file.close()


def add_new_record(database: Any) -> None:
    f_name: str = input("Please, input your first name here: ")
    l_name: str = input("Please, input your last name here: ")
    ph_number: str = input("Please, input your phone number: ")
    city: str = input("Please, input your city: ")
    p_dict: Dict[str, str] = {'first_name': f_name, 'last_name': l_name,
                              'full_name': f_name + ' ' + l_name, 'phone_number': ph_number, 'city': city}
    new_record = p_dict.copy()
    database.append(new_record)
    print(new_record)
    return None


search_key: Any = None
search_query: Any = None
search_result: List = []


def search(database: Dict, choice: str) -> List:
    if choice == '2':
        search_key = 'first_name'
        search_query = input("Input the first name which you want to find: ")

    if choice == '3':
        search_key = 'last_name'
        search_query = input("Input the last name which you want to find: ")

    if choice == '4':
        search_key = 'full_name'
        search_query = input("Input the full name which you want to find: ")

    if choice == '5':
        search_key = 'phone_number'
        search_query = input("Input the phone number which you want to find: ")

    if choice == '6':
        search_key = 'city'
        search_query = input("Input the name of the city which you want to find: ")

    for item in database:
        if item[search_key] == search_query:
            print(item[search_key])
            search_result.append(item[search_key])
            if search_query != item[search_key]:
                break
        if search_query == '':
            print("No results found")
    print(len(search_result))
    return search_result


def delete_record_by_number(database: Any) -> None:
    phone_comparison: str = input("Input the phone number here ")
    for item in database:
        if item['phone_number'] == phone_comparison:
            print(item['phone_number'])
            database.remove(item)
            print("The record has been removed by the own phone number")
            break
    else:
        print("This number is not in the database. Please, input the valid number which is in the database\n")
    return None


def update_item_by_phonenumber(database: Any) -> None:
    input_number: str = input("Enter your phone number here: ")
    for item in database:
        if item['phone_number'] == input_number:
            print(item)
            changing: str = input("Do you want to change your record - Yes / No: ").strip().capitalize()
            if changing == 'Yes':
                add_new_record(database)
                database.remove(item)
            if changing == "No":
                break
    return None


menu = print(""" Select the number of the operation which you need:
                1. Add new entries;
                2. Search by first name
                3. Search by last name
                4. Search by full name
                5. Search by telephone number
                6. Search by city
                7. Delete a record for a given telephone number
                8. Update a record for a given telephone number
                9. Exit of the program
""")

try:
    list_search: List = []
    while True:
        choice: str = input("Please, input the number which was chosen: ")
        if choice == '1':
            add_new_record(main_dict)
        if choice == '2' or choice == '3' or choice == '4' \
                or choice == '5' or choice == '6':
            list_search += search(main_dict, choice)
            print(list_search)
        if choice == '7':
            delete_record_by_number(main_dict)
            print(main_dict)
        if choice == '8':
            print(main_dict)
            update_item_by_phonenumber(main_dict)
            print('Your current record is changed now')
            print(main_dict)
        if choice == '9':
            break
except NameError:
    print("Сatched")
except Exception as e:
    print('Unexpected error.')
    print(e)
finally:
    phone_book_file = open(phonebook_var, 'w+')
    json.dump(main_dict, phone_book_file, indent=4)
    phone_book_file.close()
