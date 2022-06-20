usname = input()

name = {'swastik': 'Swastik Sharma',
            'abhishek': 'Abhishek Raj',
            'arin': 'Arin'}
age = {'swastik': 'Age : 18',
            'abhishek': 'Age : 18',
            'arin': 'Age : 19'}

dob = {'swastik': 'DOB : 10/08/2003',
            'abhishek': 'DOB : 27/07/2003',
            'arin': 'DOB : 26/05/2002'}

status = {'swastik': 'Relationship status : Single',
            'abhishek': 'Relationship status : Commited',
            'arin': 'Relationship status : Commited'}

key = {'swastik': 2001,
            'abhishek': 2003,
            'arin': 2002}

change = int(input('If you want to change any details press 1 : '))

if (change == 1) : 
    i = input('Enter what you want to change : ')
    if(i == "name" ):
        new_name = input('Enter new name : ')
        name[usname] = new_name
        print('Name is changed to ' + name.get(usname))
        print(name)
    if(i == "age"):
        new_age = input('Enter new age : ')
        age[usname] = new_age
        print('Age is changed to ' + age.get(usname))
        print(age)
    if(i == "dob"):
        new_dob = input('Enter new DOB : ')
        dob[usname] = new_dob
        print('DOB is changed to ' + dob.get(usname))
        print(dob)
    if(i == "status"):
        new_status = input('Enter new status : ')
        status[usname] = new_status
        print('Status is changed to ' + status.get(usname))
        print(status)
    if(i == "key"):
        new_key = input('Enter new key : ')
        key[usname] = new_key
        print('Key is changed to ' + key.get(usname))
        print(key)