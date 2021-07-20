#  n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

list = [i for i in range(1,101)]
mult = 1
for elem in list:
    mult*=elem


mult = str(mult)
list = [i for i in mult]
sum = 0
for elem in list:
    sum += int(elem)

print(sum)


######################################################### SECOND VERSION ##########################################################
# import math
#print(sum(int(elem) for elem in list(str(math.factorial(100)))))

###################################################################################################################################

#ANSWER ---- 648
