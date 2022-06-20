dict = {'swastik':1, 'abhishek':2, 'arin':3}

usname = input("Enter your username: ")

if usname in dict:
    print('Welcome '+ usname)
    password = int(input('Enter your password: '))
    if (dict[usname] == password):
        print('Login successful')
    if (dict[usname] != password) : 
        print('Invalid password')
        press = int(input('If you want to change your password PRESS 1 else 0 '))
        if (press==1):
            dict[usname] = input()
            print(dict.get(usname))

else : 
    print('Invalid username')
    



