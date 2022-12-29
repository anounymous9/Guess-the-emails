import random,string
email = [
    '@gmail.com',
    '@yahoo.com',
    '@outlook.com',
    '@hotmail.com',
    '@hotmail.fr'
    ]
f = open('users.txt','r').readlines()
count = 0
while (count < len(f)):
    for i in f :
        print(i.strip() +str(random.randint(1000,99999)) + random.choice(email) )
    count += 1


