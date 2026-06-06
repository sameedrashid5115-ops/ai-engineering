# TIY 2-3
name = input("What is your name? ")
print(f"Hello, {name}! This is the start of the AI Engineering journey")

# TIY 2-4
name = input("What is your name? ")
print(name.upper())
print(name.lower())
print(name.title())

# TIY 2-5
print('David said "Wow this is amazing!"')

# TIY 2-6
name = "David"
print(f'{name} said "Wow this is amazing!"')

name1 = "    David "
print(name1)
print(name1.strip()) # Both sides

name2 = "David    " 
print(name2)
print(name2.rstrip()) # Right side

name3 = "\nDavid\n" 
print(name3)
print(name3.strip()) # Both sides  

name4 = "\tDavid" 
print(name4)
print(name4.lstrip()) # Left side  


