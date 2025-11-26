print("Welcome to the Interactive personal Data collector!");

name=input("Please enter your name: ");
age = int(input("Please enter your age: "));
height = float(input("Please enter your Height:"));
fav_num = int(input("Please enter your Favourite Number: "));


print("Thank you! Here is the information we collected:")

print(name, type(name), id(name));
print(age, type(age), id(age));
print(height, type(height), id(height));
print(fav_num, type(fav_num), id(fav_num));
print("");
print("Your birth year is approximately :", 2025 - age ,"(based on your age of",age,")");

print("Thank you for using the personal Data Collector. Goodbye!");
