class Rectangle:
    def __init__(self, width,height)-> None:
        self.width = width
        self.height = height
    def get_area(self):
        area = self.width * self.height
        return area
    def set_width(self,width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_perimeter(self):
        perimeter = 2*self.width + 2 * self.height
        return perimeter
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal
    def get_picture(self):
        if(self.height > 50 or self.width > 50):
            return 'Too big for picture.'
        picture = ''
        for times in range(0,self.height):
            for length in range(0,self.width):
                picture = picture + '*'
            picture = picture + "\n"
        return picture
    def get_amount_inside(self, sq):
        rectHt = self.height
        rectWid = self.width
        htTimes = 0
        wdTimes = 0
        while rectHt >= sq.height:
            rectHt = rectHt -sq.height
            htTimes = htTimes + 1
        while rectWid >= sq.width:
            rectWid = rectWid - sq.width
            wdTimes = wdTimes + 1
        return htTimes * wdTimes
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side)-> None:
        self.width = side
        self.height = side
    def get_area(self):
        area = self.width * self.height
        return area
    def set_width(self,width):
        self.width = width
        self.height = width
    def set_height(self, height):
        self.height = height
        self.width = height
    def get_perimeter(self):
        perimeter = 2*self.width + 2 * self.height
        return perimeter
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal
    def get_picture(self):
        if(self.height > 50 or self.width > 50):
            return 'Too big for picture.'
        picture = ''
        for times in range(0,self.height):
            for length in range(0,self.width):
                picture = picture + '*'
            picture = picture + "\n"
        return picture
    def get_amount_inside(self, sq):
        rectHt = self.height
        rectWid = self.width
        htTimes = 0
        wdTimes = 0
        while rectHt >= sq.height:
            rectHt = rectHt -sq.height
            htTimes = htTimes + 1
        while rectWid >= sq.width:
            rectWid = rectWid - sq.width
            wdTimes = wdTimes + 1
        return htTimes * wdTimes
    def set_side(self, side):
        self.width = side
        self.height = side
    def __str__(self):
        return f'Square(side={self.width})'