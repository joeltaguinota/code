#READ TEXT FILE
print ("NAME : Red Rubio")
print ("-----------------------")
print (" ACTIVITY C ")
print ("-----------------------")

dict={ }

print (dict)
for key in dict:
    print(dict[key])
listcontact=[]
while True:

    dict1 = {}

    print('1. Add a Contact')
    print('2. Search a Contact')
    print('3. List Down')

    select = input('Select: ')

    if select == '1':

        FIRST_NAME = input("Enter first name:")
        dict1["fn"] = FIRST_NAME
        LAST_NAME= input("Enter last name:")
        dict1["ln"] = LAST_NAME
        AGE= int(input("Enter age:"))
        dict1["ag"] = AGE
        CONTACT_NUMBER= int(input("Enter Contact Number:"))
        dict1["cn"] = CONTACT_NUMBER

        listcontact.append(dict1)
        print()

    elif select == '2':

        search = input ('\nSearch: ' )
        for contact in listcontact:
            print(contact)
    elif select == '3':
        f = open("contactlist.txt", "w")
        for list in listcontact:
            f.write(str(list))
        f.close()
        print()
        print(FIRST_NAME)
        print(LAST_NAME)
        print(AGE)
        print(CONTACT_NUMBER)
        print()

    else:
        print('\nInvalid Selection')
