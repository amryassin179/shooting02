#import modules
#store all characters(upper lower digits and puncituations)
#take number 
#number must >=6
#shuffle all lists
#make 30% and 20%
#60% litters and 40% digits and puncs


import string
import random

s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

number = input("please inter a number for the passwsord: ")

while True:
   try:
     number = int(number)
     if number < 6 :
       print("the number must be 6 or higher")
       number = input("please inter a number for the passwsord: ")
     else:
        break
   except:
     print("please inter numbers only")
     number = input("please inter a number for the passwsord: ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part1 = round(number * 30/100)
part2 = round(number * 20/100)

password = []

for i in range(part1):
  password.append(s1[i])
  password.append(s2[i])

for i in range(part2):
  password.append(s3[i])
  password.append(s4[i])

random.shuffle(password)
password = "".join(password[0:])
print(password)
