import curses
from typing import List, Tuple
from shapes import Canvas, HorizontalLine, Rectangle, Shape, Square, Triangle, VerticalLine


def main(stdscr):
    curses.curs_set(False)  # Get rid of blinking cursor (not reliable)
    initialize_colors()
    canvas = CursesCanvas(stdscr)
    shapes = create_shapes()
    selected_shape_index = 0
    should_quit = False
    while not should_quit:
        draw_menu(stdscr)
        draw_shapes(canvas, shapes, selected_shape_index)
        stdscr.refresh()
        key = stdscr.getch()
        should_quit, selected_shape_index = handle_key_press(key, selected_shape_index, shapes)


def initialize_colors() -> None:
    if curses.has_colors():
        curses.init_pair(1, curses.COLOR_BLUE, 0)
        curses.init_pair(2, curses.COLOR_CYAN, 0)


def create_shapes() -> List[Shape]:
    return [
        Square(2, 2, 3),
        Triangle(14, 4, 4),
        Rectangle(30, 2, 4, 3),
        VerticalLine(31, 3, 1),
        HorizontalLine(12, 8, 16),
    ]


def draw_menu(stdscr) -> None:
    stdscr.clear()
    stdscr.attrset(curses.color_pair(2))
    stdscr.addstr(0, 0, "TAB: select next shape. ARROW KEYS: move selected shape. Q: quit.")


def draw_shapes(canvas: Canvas, shapes: List[Shape], selected_shape_index: int) -> None:
    selected_shape = shapes[selected_shape_index]
    for shape in shapes:
        if shape is selected_shape:
            canvas.set_color(1)
        else:
            canvas.set_color(0)
        shape.draw(canvas)


def handle_key_press(key: int, selected_shape_index: int, shapes: List[Shape]) -> Tuple[bool, int]:
    should_quit = False
    if chr(key) in "Qq":
        should_quit = True
    elif key == ord("\t"):
        selected_shape_index += 1
        if selected_shape_index >= len(shapes):
            selected_shape_index = 0
    else:
        selected_shape = shapes[selected_shape_index]
        if key == curses.KEY_RIGHT:
            selected_shape.move(delta_x=1)
        elif key == curses.KEY_LEFT:
            selected_shape.move(delta_x=-1)
        elif key == curses.KEY_UP:
            selected_shape.move(delta_y=-1)
        elif key == curses.KEY_DOWN:
            selected_shape.move(delta_y=1)
    return should_quit, selected_shape_index


class CursesCanvas(Canvas):
    def __init__(self, curses_window) -> None:
        self.__curses_window = curses_window

    def draw_backslash(self, x: int, y: int) -> None:
        self.__draw_character("\\", x, y)

    def draw_upper_left_corner(self, x: int, y: int) -> None:
        self.__draw_character(curses.ACS_ULCORNER, x, y)

    def draw_upper_right_corner(self, x: int, y: int) -> None:
        self.__draw_character(curses.ACS_URCORNER, x, y)

    def draw_lower_left_corner(self, x: int, y: int) -> None:
        self.__draw_character(curses.ACS_LLCORNER, x, y)

    def draw_lower_right_corner(self, x: int, y: int) -> None:
        self.__draw_character(curses.ACS_LRCORNER, x, y)

    def draw_vertical_line(self, x: int, y: int, length: int) -> None:
        for i in range(length):
            self.__draw_character(curses.ACS_VLINE, x, y + i)

    def draw_horizontal_line(self, x: int, y: int, length: int) -> None:
        for i in range(length):
            self.__draw_character(curses.ACS_HLINE, x + i, y)

    def set_color(self, color_index: int) -> None:
        self.__curses_window.attrset(curses.color_pair(color_index))

    def __draw_character(self, character: str, x: int, y: int) -> None:
        try:
            self.__curses_window.addch(y, x, character)
        except curses.error:
            pass  # ignore out-of-screen errors


if __name__ == "__main__":
    curses.wrapper(main)
