class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.name = 'Rectangle'

    def __str__(self) -> str:
        return self.name + '(width=' + str(self.width) + ', height=' + str(self.height) + ')'

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.height*self.width

    def get_perimeter(self):
        return 2*self.width+2*self.height

    def get_diagonal(self):
        return (self.width**2+self.height**2)**.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        
        result = ""
        for row in range(0, self.height, 1):
            result = result + '*' * self.width + '\n'

        return result

    def get_amount_inside(self, minor_shape):
        if minor_shape.height > self.height or minor_shape.width > self.width:
            return 0

        return int(self.get_area()/minor_shape.get_area())
        

class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
        self.name = 'Square'

    def __str__(self) -> str:
        return str(self.name + '(side=' + str(self.width) + ')')

    def set_side(self, side):
        self.width = side
        self.height = side