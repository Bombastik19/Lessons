# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?



num = 1
small = 1
big = 0
while True:
    if num%2 == 0 and num%3 == 0 and num%4 == 0 and num%5 == 0 and num%6 == 0 and num%7 == 0 and num%8 == 0 and num%9 == 0 and num%10 == 0 and num%11 == 0 and num%12 == 0 and num%13 == 0 and num%14 == 0 and num%15 == 0 and num%16 == 0 and num%17 == 0 and num%18 == 0 and num%19 == 0 and num%20 == 0:
        big = num
        break
    else:
        num+=1
print(num)


#               ANSWER is : 232792560
