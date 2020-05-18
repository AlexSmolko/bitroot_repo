import json
import sys

print(sys.argv)
if len(sys.argv) < 2:
    print('Please, specify json file name')
    exit()

phonebook_var = sys.argv[1]
phone_book_file = open(phonebook_var)
try:
    main_dict = json.load(phone_book_file)
except json.decoder.JSONDecodeError:
    main_dict = []
phone_book_file.close()


def add_new_record(database):
    f_name = input("Please, input your first name here: ")
    l_name = input("Please, input your last name here: ")
    ph_number = input("Please, input your phone number: ")
    city = input("Please, input your city: ")
    p_dict = {'first_name': f_name, 'last_name': l_name,
              'full_name': f_name + ' ' + l_name, 'phone_number': ph_number,
              'city': city}
    new_record = p_dict.copy()
    database.append(new_record)
    print(new_record)
    # print_all_base = input("Do you wish print all database: input Y or N ").strip().upper()
    # if print_all_base == 'Y':
    #     print(database)


search_key = None
search_query = None
search_result = []


def search(database, choice):
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
            break
    if item[search_key] != search_query:
            print("You input the wrong data")
    print(len(search_result))
    return search_result


def delete_record_by_number(database):
    phone_comparison = input("Input the phone number here ")
    for item in database:
        if item['phone_number'] == phone_comparison:
            print(item['phone_number'])
            database.remove(item)
            print("The record has been removed by the own phone number")
            break
    else:
        print("This number is not in the database. Please, input the valid number which is in the database\n")


def update_item_by_phonenumber(database):
    input_number = input("Enter your phone number here: ")
    for item in database:
        if item['phone_number'] == input_number:
            print(item)
            changing = input("Do you want to change your record - Yes / No: ").strip().capitalize()
            if changing == 'Yes':
                u_rec = add_new_record(database)
                database.remove(item)
                return u_rec
            if changing == "No":
                break
            message = print('Your current record is changed now')
            return message

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
    list_search = []
    while True:
        choice = input("Please, input the number which was chosen: ")
        if choice == '1':
            add_new_record(main_dict)
        if choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6':
            list_search += search(main_dict, choice)
            print(list_search)
        if choice == '7':
            delete_record_by_number(main_dict)
            print(main_dict)
        if choice == '8':
            print(main_dict)
            update_item_by_phonenumber(main_dict)
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
