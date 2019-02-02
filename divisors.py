# size of list
number = int(input('Input a number to find the divisors\t'))

for i in range(2, int(number+1/2)):
    #print ("Range number - ", i)
    if ( number % i == 0 ) :
                print (i)


#### Approach #
print ("-------- Approach #2 --------")
numbers = range(2, int(number+1/2))
for j in numbers:
    if ( number % j == 0 ) :
                print (j)

