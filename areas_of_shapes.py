print('"Areas and Shapes!"')
#Area of a square
side_square = float(input("What is the length of a side of square?"))
area_1 = side_square ** 2
print("the area of the square is: "+ str(area_1))

#Area of a rectangle
length = float(input( "What is the length of th rectangle?"))
width = float(input("What is the width of a rectangle?"))
area_2 = length * width
print(" The rectangle area is:" + str(area_2))

#Area of a circle
radius = float(input("What is the radius of the circle?"))
area_3 = 3.14 * (radius ** 2)
print("The area of a circle is: " + str(area_3)) 

#Area of Circle using PI
import math
radius = float(input("What is the radius of the circle?"))
area_3 = math.pi * (radius ** 2)
print("The area of a circle is: " + str(area_3))


# radius = float(input("What is the radius of the circle?"))
# area_3 = 3.14159 * (radius ** 2)
# print("The area of a circle is: " + str(area_3))