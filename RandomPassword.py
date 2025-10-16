import random
Password = ''
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(8):
    choice1 = random.randint(0,10)
    if choice1 > 6:
        #Integer
        newint = str(random.randrange(0,9))
        Password = Password + newint
    else:
        #Character
        newchar = alphabet[random.randrange(0,51)]
        Password = Password + newchar
print(Password)