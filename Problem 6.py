# The sum of the squares of the first ten natural numbers is,
#
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
#
# 3025 - 385 = 2640
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


sum_of_the_squares = 0

sum_of_20 = 0

# sum_of_the_squares = 1^2 + 2^2 + 3^2 ... + 20^2 ++++++++++++++++++++++++++

# square of the sum = ( 1 + 2 + 3 ... + 20 )^2

for i in range(101):
    sum_of_the_squares +=  i**2

for i in range(101):
    sum_of_20+=i
square_of_the_sum = sum_of_20**2


difference = square_of_the_sum - sum_of_the_squares
print(difference)


#                   ABSWER is : 25164150
