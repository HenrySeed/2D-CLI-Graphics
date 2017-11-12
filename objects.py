from renderer import *

class Rect():
    def __init__(self, x, y, w, h, fill=10, border=0, opac=False):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.fill = fill
        self.opac = opac

        self.border = border
        if self.border == 1: self.border_set = border_set_1
        if self.border == 2: self.border_set = border_set_2
        if self.border == 3: self.border_set = border_set_3

    def draw(self, w):
        for row in range(self.y, self.y + self.h):
            for col in range(self.x, self.x + self.w):
                w.renpix(row, col, tone[self.fill], self.opac)

        if self.border != 0:
            for col in range(self.x, self.x + self.w):
                w.renpix(self.y, col, self.border_set[0], self.opac)
                w.renpix(self.y+self.h-1, col, self.border_set[0], self.opac)

            for row in range(self.y, self.y + self.h):
                w.renpix(row, self.x, self.border_set[1], self.opac)
                w.renpix(row, self.x+self.w-1, self.border_set[1], self.opac)

            w.renpix(self.y, self.x, self.border_set[2], self.opac)
            w.renpix(self.y+self.h-1, self.x, self.border_set[4], self.opac)
            w.renpix(self.y, self.x+self.w-1, self.border_set[3], self.opac)
            w.renpix(self.y+self.h-1, self.x+self.w-1, self.border_set[5], self.opac)

class Circle():
    def __init__(self, x, y, r, fill=10, opac=False):
        self.x = x
        self.y = y
        self.r = r
        self.fill = fill
        self.opac = opac

    def draw(self, w):
        rad = self.r;
        size = rad*3
        circ = [[' '] * size for n in range(size)]

        y_offset = floor(rad*3/4*-1)
        x_offset = floor(rad/13) * -1 + -1

        for i in range(0, size):
            for j in range(0, size):
                if(sqrt((j-(size)/2)*(j-(size)/2)/2 + (i-(size)/2)*(i-(size)/2)*2) <= rad):
                    circ[i+y_offset][j+x_offset] = "#"

        for row in range(len(circ)):
            for col in range(len(circ[0])):
                if circ[row][col] == '#':
                    w.renpix(row+self.y, col+self.x, tone[self.fill], self.opac)

class Text():
    def __init__(self, x, y, text=''):
        self.x = x
        self.y = y
        self.text = text

    def draw(self, w):
        for char in range(0, len(self.text)):
            w.renpix(self.y, self.x+char, self.text[char], 10)
