from abc import ABC, abstractmethod


class Canvas(ABC):
    @abstractmethod
    def draw_backslash(self, x: int, y: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_upper_left_corner(self, x: int, y: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_upper_right_corner(self, x: int, y: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_lower_left_corner(self, x: int, y: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_lower_right_corner(self, x: int, y: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_vertical_line(self, x: int, y: int, length: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def draw_horizontal_line(self, x: int, y: int, length: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def set_color(self, color_index: int) -> None:
        raise NotImplementedError

# Add your shape classes below
class Shape:
    def __init__(self, x, y , width=1, height=1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y


class VerticalLine(Shape):
    def __init__(self, pos_x, pos_y, length=1):
        self.shape = Shape(pos_x, pos_y, width=length)

    def draw(self, canvas: Canvas):
        canvas.draw_vertical_line(self.pos_x, self.pos_y, self.shape.width)

class HorizontalLine(Shape):
    def __init__(self, pos_x, pos_y, length):
        Shape(pos_x, pos_y, height=length)

    def draw(self, canvas: Canvas):
        canvas.draw_vertical_line(self.pos_x, self.pos_y, self.shape.height)

class Rectangle(Shape):
    def __init__(self, pos_x, pos_y, width, height):
        Shape(pos_x, pos_y, height=height, width=width)

    def draw(self, canvas: Canvas):
        canvas.draw_upper_left_corner(pos_x, pos_y)
        canvas.draw_upper_right_corner()
        canvas.draw_lower_left_corner()
        canvas.draw_lower_right_corner()
        canvas.draw_horizontal_line()
        canvas.draw_vertical_line()
class Square(Rectangle):
    def __init__(self, pos_x, pos_y, size):
        Rectangle(pos_x, pos_y, width=size, height=size)

class Triangle(Shape):
    def __init__(self, pos_x, pos_y, size):
        pass

