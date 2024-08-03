import random
letters =['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
numbers =['1','2','3','4','5','6','7','8','9','0']
symbols =['!','@','#','$','%','&','*','(',')','-','+','=','^','{','}','[',']','<','>','?']
print("Welcome to password generator")
n_letters=int(input("How many letters do you want in your password?\n"))
n_symbols=int(input("How many symbols do you want in your password?\n"))
n_numbers=int(input("How many numbers do you want in your password?\n"))
password_list=[]
for i in range(0,n_letters):
    char = random.choice(letters)
    password_list += char
for i in range(0,n_symbols):
    char = random.choice(symbols)
    password_list += char
for i in range(0,n_numbers):
    char  = random.choice(numbers)
    password_list += char
random.shuffle(password_list)
print(password_list)
password=""
for char in password_list:
    password += char
print(password)