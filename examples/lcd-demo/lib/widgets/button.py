from colors import *

class Button:

    def __init__(self, lcd, x1, y1, x2, y2, label="Button"):
        self.lcd = lcd
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.label = label

        self.color_line = lcd.rgb(*WHITE)
        self.color_fill = lcd.rgb(*GREY_20)

        self.render()

    @property
    def xywh(self):
        return (self.x1, self.y1, self.x2 - self.x1, self.y2 - self.y1)

    def render(self):
        self.lcd.set_pen(self.color_line, self.color_fill)
        xywh = self.xywh
        self.lcd.rect_interior(*xywh)
        self.lcd.rect(*xywh)

    def is_pressed(self, touching, x, y):
        """
        Return if the button is pressed or not.
           >>> btn.is_pressed(*btn.lcd.get_touch())
        :param x: x coordinate
        :param y: y coordinate
        :return: True if button is being pressed, False otherwise
        """
        if touching:
            if not (self.y1 < y < self.y2):
                return False
            if not (self.x1 < x < self.x2):
                return False
            return True
        return False
