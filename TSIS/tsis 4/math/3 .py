import math

n_of_sides = int(input("Input number of sides:"))
lenght = int(input("Input the length of a side:"))
deg = 180/n_of_sides
rad = math.radians(deg)

x = ((lenght**2)*n_of_sides)/(4*math.ceil(math.tan(rad))) 
print(f"The area of the polygon is: {x}")