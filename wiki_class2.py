class Shape:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.description = "This shape has not been described yet"
		self.author = "Nobody has claimed to have made this shape yet"
	def area(self):
		return self.x * self.y
	def perimeter(self):
		return 2 * self.x + 2 * self.y
	def describe(self, text):
		self.description = text
	def authorName(self, text):
		self.author = text
	def scaleSize(self, scale):
		self.x *= scale
		self.y *= scale
		
class Square(Shape):
	def __init__(self,x):
		self.x = x
		self.y = x
		
# The shape looks like this:
#  ___________
# |     |     |
# |     |     |
# |_____|_____|
class DoubleSquare(Square):
	def __init__(self,y):
		self.x = 2 * y
		self.y = y
		self.author = "Double Square Man"
	def perimeter(self):
		return 3 * self.x + 2 * self.y
		
# First, we create a dictionary
dictionary = {}

# Then, create some instances of classes in the dictionary
dictionary["DoubleSquare 1"] = DoubleSquare(5)
dictionary["Long Rectangle"] = Shape(600,45)

# You can now use them like a normal class:
print dictionary["Long Rectangle"].area()

dictionary["DoubleSquare 1"].authorName("The Gingerbread Man")
print dictionary["DoubleSquare 1"].author

# playing around with dictionaries
another_dictionary = {"DSq": DoubleSquare(3), "Rectangle": Shape(8,90)}

#another_dictionary["DSq"].authorName("Beavis")
print another_dictionary["Rectangle"].author


# class equalities: both names point to the same class instance
Square1 = Square(4)
Square2 = Square1
Square2.authorName("Peter Pan")
print Square1.author