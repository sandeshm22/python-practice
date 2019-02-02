#statements example 
days=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'];
print(days)
print(len(days));
print(days[1]);
print(days[1:3]);

print("***************************");
print("Dictionary");

dictionary = {};

for i in range(0,7):
	dictionary[i] = days[i];
print(dictionary);
print(dictionary.keys())   # Prints all the keys
print (dictionary.values()) # Prints all the values


tuple_var = tuple(dictionary);
tuple_var1 = tuple(days[1]);
tuple_var2 = repr(days[1]);
tuple_var3 = ord(days[1][1]);
hex_var = hex(ord(days[1][1]));
print(tuple_var);
print(tuple_var1);
print(tuple_var2);
print(tuple_var3);
print(hex_var);