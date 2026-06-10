# Inserting elements into a list

motorcycles = ["Honda", "Yamaha", "Suzuki"]
print(motorcycles)


motorcycles.append("Zundapp")
print(motorcycles)

motorcycles.insert(0, "Ducati")
print(motorcycles)

del motorcycles[1]
print(motorcycles)

colors = ["Red", "Green", "Blue", "Yellow"]

new_color = colors.pop()
print(new_color)
print(colors)

colors.remove("Green")
print(colors)

cars = ["Toyota", "Honda", "Ford", "BMW"]
print(cars)
cars.sort() # Sorts the list in alphabetical order permanently
print(cars) 

cars.sort(reverse=True) # Sorts the list in reverse alphabetical order permanently
print(cars)

cars = ["Toyota", "Honda", "Ford", "BMW"]
print(sorted(cars)) # Sorts the list in alphabetical order temporarily
print(cars) # Original list remains unchanged

cars = ["Toyota", "Honda", "Ford", "BMW"]
print(cars) 
cars.reverse() # Reverses the order of the list permanently
print(cars)

cars = ["Toyota", "Honda", "Ford", "BMW"]
print(len(cars)) # Returns the number of items in the list