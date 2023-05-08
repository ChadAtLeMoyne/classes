from shapes import Shape, Triangle, Square

t = Triangle(500, 500)
s = Square()
square_sides = [5, 5, 5, 5]
s.set_side_lengths(square_sides)
print(f'Square area: {s.get_area()}')

if s > t:
    print('Square is greater')
else:
    print('Triangle is greater')
