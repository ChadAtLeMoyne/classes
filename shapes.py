# Declare a class to use for Shapes
class Shape():
    def __init__(self, sides) -> None:
        self.set_sides(sides)
        self.side_lengths = []
    
    # Accessor
    def get_sides(self) -> int:
        return self.sides

    def set_sides(self, sides) -> None:
        if sides <= 0:
            raise ValueError(f"Sides must be > 0. {sides} given")
        self.sides = sides
    
    def get_side_lengths(self):
        return self.side_lengths

    def set_side_lengths(self, side_lengths) -> None:
        if len(side_lengths) != self.get_sides():
            raise ValueError(f'Mismatched sides and lengths')
        if min(side_lengths) <= 0:
            raise ValueError(f'Side lengths must be > 0')

        self.side_lengths = side_lengths

    def get_perimeter(self):
        p = 0
        for i in self.get_side_lengths():
            p += i
        
        return p

    def get_area(self):
        return None

    def __eq__(self, other) -> bool:
        return self.get_area() == other.get_area()

    def __gt__(self, other) -> bool:
        return self.get_area() > other.get_area()

class Triangle(Shape):
    def __init__(self, height, width) -> None:
        super().__init__(3)
        self.set_height(height)
        self.set_width(width)

    def set_height(self, height):
        self.height = height
    def set_width(self, width):
        self.width = width
    def get_height(self):
        return self.height
    def get_width(self):
        return self.width

    def get_area(self):
        return (self.get_height() * self.get_width()) / 2
    
    def set_sides(self, sides) -> None:
        if sides != 3:
            raise ValueError(f'Triangles have 3 sides')
        super().set_sides(sides)

class Square(Shape):
    def __init__(self) -> None:
        super().__init__(4)
    
    def get_area(self):
        return self.side_lengths[0] ** 2
    
    def set_sides(self, sides) -> None:
        if sides != 4:
            raise ValueError(f'Squares have 4 sides')
        return super().set_sides(sides)

    def set_side_lengths(self, side_lengths) -> None:
        for i in range(len(side_lengths)):
            if i == 0:
                previous = side_lengths[0]
            else:
                if side_lengths[i] != previous:
                    raise ValueError('Sqaures have equal sides')

        return super().set_side_lengths(side_lengths)