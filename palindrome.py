# palindrome string
str = input("Enter a string")

length = len(str)

for i in range(0, length) :
    ithChar = str[i : i+1]
    jthChar = str[length -i : length-i+1]
    
    if ( jthChar != ithChar ) :
        print ('Not a palindrome')
        break;


print ("---------- Approach #2--------------")
def reverse(s):
    return s[::-1]
 
def isPalindrome(s):
    # Calling reverse function
    rev = reverse(s)
 
    # Checking if both string are equal or not
    if (s == rev):
        return True
    return False
 
 
# Driver code
s = "malayalam"
ans = isPalindrome(str)
 
if ans == 1:
    print("Yes")
else:
    print("No")
    
