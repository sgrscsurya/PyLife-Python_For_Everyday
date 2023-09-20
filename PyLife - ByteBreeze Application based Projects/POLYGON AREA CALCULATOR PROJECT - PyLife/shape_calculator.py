# POLYGON AREA CALCULATOR

""" The main motive of this program is to implement object-oriented programming principles by defining classes for Rectangles and Squares """

""" The program facilitates shape manipulation and computation based on defined rules and user input """

# Let's dive into the Program,
# Here Let's define a New class named "Rectangle". We here construct an Initilizer for the "Rectangle" class.
class Rectangle:
    def __init__(self, width, height):
        self.width = width   #Assigns the width parameter
        self.height = height  # Assigns the height parameter

# Let's define a method named "set_width" that allows setting the width of the rectangle.
    def set_width(self, width):
        self.width = width

# Similarly define a method named "set_height" that allows setting the height of the rectangle.
    def set_height(self, height):
        self.height = height

#We know that Area of a Rectangle equals to (width * Height) Hence we define a method named "get_area" to find the Area od the Rectangle.
    def get_area(self):
        return self.width * self.height
      
#Similarly, The Perimeter of a Rectangle equals to 2 * (width + Height) Hence we define a method named "get_perimeter" to find the Perimeter od the Rectangle.
    def get_perimeter(self):
        return 2 * (self.width + self.height)

# Similarly, we use The formula for diagonal for the Rectangle and define a class "get_diagonal".
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

# Here! We need to make a Picture using "*" symbol, with the given width and height data. Hence, we use "get_picture" function to get the Shape of the Polygon.
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            picture = ""
            for i in range(self.height):
                picture += "*" * self.width + "\n"
            return picture
    # Let's Breal the code and understand this, From above data. If width=8 and Height=4,
      # The Picture obtained will be,
            """ ******** 
                ********
                ********
                ******** """

# The purpose of the "get_amount_inside" method is to calculate how many times the specified shape (with a known area) can fit into the current rectangle. It does this by comparing the area of the current rectangle (calculated using self.get_area()) with the area of the given shape (calculated using "shape.get_area()").
  
    def get_amount_inside(self, shape):
        return int(self.get_area() / shape.get_area())

  #Here, we define a string representation of the "Rectangle" class.
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})" # returns the width and height of the Rectangle as strings.

""" Now, Let us define a class for (square) which comes from (Rectangle) class """
class Square(Rectangle):
    def __init__(self, side_length):
      # super() is used to call the constructor of the superclass (Rectangle in this case). "super().__init__(side_length, side_length)" calls the __init__ method of the Rectangle class, passing side_length as the width and height parameters.
        super().__init__(side_length, side_length)

  # Now, Let's set a side length of the Square : Here, we define a function named "set_side" with equal width and height (Property of Square) 
    def set_side(self, side_length):
        self.width = side_length
        self.height = side_length

  # Similarly as before, Let's define a String representation to the "Square" class also.
  # Finally, return back the String representing the "Square" with it's side length.
    def __str__(self):
        return f"Square(side={self.width})"

""" Hence, The Code for Calculating an Area of Polygons/ Polygon Area Calculator has been successfully executed """