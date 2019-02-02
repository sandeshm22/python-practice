# print a pyramid

for i in range(0,5):
    for j in range (0,int(i+1)):
        print ('*', end='')
    print()



print ("--------------------------------------------------------------------------")

for i in range (0,5) : 
    for k in range (i, 4) :
        print(" ", end = '')
    for j in range (0, int(i+1)) :
        print("*",  end = '')
    print( )

	
print ("--------------------------------------------------------------------------")

for i in range (0,5) : 
    for j in range (int(i+1), 0,-1) :
        print("*",  end = '')
    print( )
