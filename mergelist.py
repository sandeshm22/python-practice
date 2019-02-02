# merge two sorted lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


length1 = len(a)
length2 = len(b)
print(length1)
print(length2)

maxIterations = length1
if ( maxIterations < length2) :
    maxIterations = length2

j = int(0)
for i in  range (0, maxIterations) :
    if( i < length1 ) :
        if(a[i] < a[j]) :
            print(" ",a[j], end='')
            j= j+1
        if(a[i] == a[j]) :
            print(" ",a[i], end='')
            print(" ",a[j], end='')
            j= j+1


print ("-----------")
i=0
j=0
while ( i < length1 and j < length2) :
    
    if(a[i] < a[j]):
        print (a[i],' ', end =' ')
        i =  i+1
    else :
        print (a[j], ' ' ,end ='')
        j = j+1
