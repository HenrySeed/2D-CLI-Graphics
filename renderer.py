import os
from math import *

#############################    Control Panel   ###############################

#       0    1    2    3    4    5    6    7    8    9    10           #                                                                    ┃
#          .....'''''"""""^^^^^?????*****#####%%%%%@@@@@&&&&&          #
#          .....'''''"""""^^^^^?????*****#####%%%%%@@@@@&&&&&          #
#          .....'''''"""""^^^^^?????*****#####%%%%%@@@@@&&&&&          #

tone = [' ', '.', "'", '"', '^', '?', '*', '#', '%', '@', '&']

border_set_1 = ['━', '┃', '┏', '┓', '┗', '┛']
border_set_2 = ['-', '|', '+', '+', '+', '+']
border_set_3 = ['═', '║', '╔', '╗', '╚', '╝']

################################################################################


class Window():
    def __init__(self, w, h, fill=0, border=0):
        self.w = w
        self.h = h
        self.border = border
        if self.border != 0:
            self.w += 2
            self.h += 2
        self.image = [[tone[fill]] * self.w for n in range(self.h)]
        self.border = border
        self.clear_first = False
        self.objects = []

        if self.border == 1: self.border_set = border_set_1
        if self.border == 2: self.border_set = border_set_2
        if self.border == 3: self.border_set = border_set_3

    def add(self, objects):
        # for obj in objects:
            # print('obj.x:{} obj.y:{}, obj.w:{}, obj.h:{}'.format(obj.x, obj.y, obj.w, obj.h))
            # if obj.__class__.__name__ == 'Rect':
            #     if obj.x+obj.w >= self.w-1:
            #         print("failed because rectangles right edge of {} is bigger than window width of {}-border".format(obj.x+obj.w, self.w))
            #     if obj.x <= 0:
            #         print("failed because x is small")
            #     if obj.y + obj.h >= self.w:
            #         print("failed because y is big")
            #     if obj.y < 0:
            #         print("failed because y is small")

            # elif obj.__class__.__name__ == 'Circle':
            #     if obj.x + obj.r >= self.w: print("failed because x is big")
            #     if obj.x <= 0: print("failed because x is small")
            #     if obj.y + obj.r >= self.w: print("failed because y is big")
            #     if obj.y <= 0: print("failed because y is small")
            #
            # elif obj.__class__.__name__ == 'Text':


        for obj in objects:
            self.objects.append(obj)

    def renpix(self, y, x, char, opac):
        if y < 0 or x < 0:
            return 0
        try:
            if self.border != 0:
                if self.img_buffer[y+1][x+1] != ' ':
                    if opac:
                        if char in border_set_1 + border_set_2 + border_set_3:
                             char = char
                        elif self.img_buffer[y+1][x+1] in border_set_1 + border_set_2 + border_set_3:
                            char = tone[min(2+tone.index(char), 10)]
                        else:
                            char = tone[min(tone.index(self.img_buffer[y+1][x+1])+tone.index(char), 10)]
                    else:
                        char = char
                self.img_buffer[y+1][x+1] = char
            else:
                self.img_buffer[y][x] = char
        except:
            return 0

    def render(self):
        if self.clear_first:
            os.system('clear')

        self.img_buffer = self.image[:]

        for obj in self.objects:
            obj.draw(self)

        if self.border != 0:
            for col in range(0, self.w):
                self.img_buffer[0][col] = self.border_set[0]
                self.img_buffer[self.h-1][col] = self.border_set[0]

            for row in range(0, self.h):
                self.img_buffer[row][0] = self.border_set[1]
                self.img_buffer[row][self.w-1] = self.border_set[1]

            self.img_buffer[0][0] = self.border_set[2]
            self.img_buffer[self.h-1][0] = self.border_set[4]
            self.img_buffer[0][self.w-1] = self.border_set[3]
            self.img_buffer[self.h-1][self.w-1] = self.border_set[5]

        output = ""
        for row in self.img_buffer:
            row_str = ""
            for col in row:
                row_str += col
            output += row_str + "\n"

        print(output)








#
