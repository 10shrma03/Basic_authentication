empid = [1, 2, 3]

id = int(input('Enter your employee id : '))

for i in empid:
    if(i == id):
        print('Welcome')

dict = {'swastik': 1, 'abhishek': 2, 'arin': 3}

usname = input("Enter your username: ")

if usname in dict:
    print('Welcome ' + usname)
    password = int(input('Enter your password: '))
    if (dict[usname] == password):
        print('Login successful')
    if (dict[usname] != password):
        print('Invalid password')
        press = int(
            input('If you want to change your password PRESS 1 else 0 '))
        if (press == 1):
            dict[usname] = input('Enter new password: ')
            print('Your new password is ' + dict.get(usname))

else:
    print('Invalid username')


detail_1 = {'swastik': 'Full name : Swastik Sharma',
            'abhishek': 'Full name: Abhishek Raj',
            'arin': 'Full name : Arin'}
detail_2 = {'swastik': 'Age : 18',
            'abhishek': 'Age : 18',
            'arin': 'Age : 19'}

detail_3 = {'swastik': 'DOB : 10/08/2003',
            'abhishek': 'DOB : 27/07/2003',
            'arin': 'DOB : 26/05/2002'}

detail_4 = {'swastik': 'Relationship status : Single',
            'abhishek': 'Relationship status : Commited',
            'arin': 'Relationship status : Commited'}

print(detail_1.get(usname))
print(detail_2.get(usname))
print(detail_3.get(usname))
print(detail_4.get(usname))
