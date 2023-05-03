from shapes import Shape, Triangle

t = Triangle(3, 5)
print(t.get_sides())
print(t.get_area())
sl = [3, 4, 5]
t.set_side_lengths(sl)
print(t.get_perimeter())
