class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def set_width(self,width):  
        self.width = width
    def set_height(self,height): 
        self.height = height
    def get_area(self):
        area = self.width * self.height 
        return area
    def get_perimeter(self):
        per = 2 * (self.width + self.height) 
        return per
    def get_diagonal(self):
        diag = ((self.width)**2 + (self.height)**2) ** 0.5
        return diag
    def get_picture(self):
        if self.width > 50 or self.height > 50:   
            return "Too big for picture."
        else:
            pic = "*" * self.width
            new_pic = (pic + "\n") * self.height
            return new_pic
    def get_amount_inside(self,shape):
        area_1 = self.width * self.height
        area_2 = shape.side * shape.side
        num = area_1 // area_2
        return num
class Square(Rectangle): 
    def __init__(self,side):
        Rectangle.__init__(self,side,side)
        self.side = side
    def set_side(self,new): 
        Rectangle.__init__(self,new,new)
        self.side = new
