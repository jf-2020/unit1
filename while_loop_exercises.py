# while_loop_exercises.py - this prgm answers the while loop exercises in schoology
#
# jf - 4/17

from math import floor
import time


############################
### WHILE LOOP EXERCISES ###
############################


### 1 to 10 ###

# count1 = 1

# while count1 <= 10:
#     print(count1)
#     count1 += 1


### N to M ###

# n = int(input("Give me a start number: "))
# m = int(input("Give me an end number: "))

# while n <= m:
#     print(n)
#     n += 1


### Odd Numbers ###

# count2 = 1

# while count2 <= 10:
#     if count2 % 2 == 0:
#         print(count2)
    
#     count2 += 1


### How many coins? ###

# coins = 0

# print("You have %d coins." % coins)

# while True:

#     yes = input("Do you want another coin? (yes/no) ")

#     if yes == "yes":
#         coins += 1
#         print("You have %d coins." % coins)
#     else:
#         print("Bye")
#         break


### Print a Square ###

# for i in range(5):
#     print("*"*5)


### Print a Square II ###

# n = int(input("How big is the square? "))

# for i in range(n):
#     print("*"*n)


### Print a Box ###

# width = int(input("Width? "))
# height = int(input("Height? "))

# print("*"*width)

# for i in range(height-2):
#     print("*" + " "*(width-2) + "*")

# print("*"*width)


### Print a Triangle ###

# lines = 4
# count = 1

# while lines > 0:
#     print(((lines-1)*" " ) + ( "*"*count))
#     count += 2
#     lines -= 1


### Print a Triangle II ###

# height = int(input("Height? "))
# count = 1

# while height > 0:
#     print(((height-1)*" " ) + ( "*"*count))
#     count += 2
#     height -= 1


### Multiplication Table ###

# fstring = "{} X {} = {}"
# i, j = 1, 1

# while i <= 10:
    
#     j = 1

#     while j <= 10:

#         pstring = fstring.format(i, j, i*j)

#         print(pstring)

#         j += 1

#     i += 1


### Bonus: Print a Banner ###

# str = input("Text? ")
# str_len = len(str)

# count = 3

# while count > 0:

#     if count == 3 or count == 1:
#         print("*"*(str_len+4))
#         count -= 1
#     else:
#         print("* " + str + " *")
#         count -= 1


### Bonus: Triangle Numbers ###

# count = 1

# while count <= 100:
#     print("T(" + str(count) + ") = %d" % ((count * (count + 1)/2)))
#     count += 1


### Bonus: Factor a Number ###

# n = int(input("Give me a number, not too large: "))

# divisor = 1

# fstring = ""

# while divisor <= floor(n/2):

#     if n % divisor == 0:
        
#         if fstring:

#             fstring += ", %d" % divisor

#         else:

#             fstring += str(divisor)

#         print(fstring)

#     divisor += 1

# print(fstring + ", " + str(n))


#######################################
### Additional While Loop Exercises ###
#######################################


### BLASTOFF 1 ###

# count = 10

# while count >= 0:
#     print(count)
#     count -= 1


### BLASTOFF 2 ###

# count = 10

# while count >= 0:
    
#     if count != 0: 
#         print(count)
        
#     else:
#         print("Custom Message")

#     count -= 1


### BLASTOFF 3 ###

# n = int(input("Time til BLASTOFF? "))

# while n >= 0:
#     print(n)
#     n -= 1


### BLASTOFF 4 ###

# n = int(input("Enter a number less than 20 but greater than or equal to 0: "))

# if n < 0 or n > 20:
#     print("You didn't listen.")
# else:

#     while n >= 0:
#         print(n)
#         n-=1


### BLASTOFF 5 ###

# n = int(input("Provide a time til BLASTOFF: "))

# while n >= 0:

#     print(n)
#     time.sleep(1)

#     n -= 1


#####################################
### Yet Another Bonus Exercise :) ###
#####################################

