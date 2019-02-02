import sys;

fileName = input("Enter a file ");
try:
    file = open(fileName, "w");
    file.write("Hey Sandesh, how are you");
    file.close();
except IOError:
    sys.exit();

	
file_name = input("Enter a file to read");
try : 
   fileR = open(file_name, "r");
   file_text = fileR.read();
   print(file_text);
except IOError :
	print("Error");
 
