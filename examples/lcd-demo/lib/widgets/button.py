from colors import *
from utils import font_height

class Button:

    color_line = WHITE
    color_fill = GREY_20
    text_color = WHITE

    font_index = 1
    font_scale = 0

    def __init__(self, lcd, x1, y1, x2, y2, label="Button"):
        self.lcd = lcd
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.label = label

        self.render()

    @property
    def xywh(self):
        return (self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1)

    def render(self):
        # Box
        self.lcd.set_pen(self.color_line, self.color_fill)
        xywh = self.xywh
        self.lcd.rect_interior(*xywh)
        self.lcd.rect(*xywh)

        # Label, center justified
        self.lcd.set_font(
            self.font_index,
            scale=self.font_scale,
            trans=1,
        )
        self.lcd.set_text_color(self.text_color, BLACK)
        height = font_height(self.font_index, self.font_scale)
        label_width = height * len(self.label)
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        self.lcd.set_pos(
            int(center_x - (label_width / 2)),
            int(center_y - (height / 2))
        )
        self.lcd.write(self.label)

    def is_pressed(self, touching=None, x=0, y=0):
        """
        Return if the button is pressed or not.
           >>> btn.is_pressed()  # calls lcd
        alternatively, for multiple buttons
           >>> touch = btn.lcd.get_touch()
           >>> btn1.is_pressed(*touch)
           >>> btn2.is_pressed(*touch)
        :param touching: True if lcd is being touched
        :param x: x coordinate
        :param y: y coordinate
        :return: True if button is being pressed, False otherwise
        """
        if touching is None:
            (touching, x, y) = self.lcd.get_touch()
        if touching:
            if not (self.y1 < y < self.y2):
                return False
            if not (self.x1 < x < self.x2):
                return False
            return True
        return False
