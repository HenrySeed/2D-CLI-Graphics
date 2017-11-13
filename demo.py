from renderer import *
from objects import *



window = Window(w=98, h=40, fill=0, border=0)
window.clear_first = True


window.add([Circle(x=5, y=5, r=10, fill=2),
            Rect(x=23, y=6, w=20, h=10, fill=5, border=1, opac=True),
            Rect(x=60, y=3, w=22, h=9, fill=2, border=2, opac=False),
            Rect(x=6, y=22, w=30, h=6, fill=0, border=1),
            Rect(x=56, y=14, w=28, h=14, fill=6, border=3),
            Text(x=10, y=24, text='Hello World'),
            Text(x=10, y=25, text='This is some words'),
            Circle(x=49, y=16, r=7, fill=3, opac=True)
            ])
#
# window.add([Text(5, 3, "ASCII Gradient"),
#             Rect(0,  10, 5, 5, 0), Text(2, 8, "0"),
#             Rect(5,  10, 5, 5, 1), Text(7, 8, "1"),
#             Rect(10, 10, 5, 5, 2), Text(12, 8, "2"),
#             Rect(15, 10, 5, 5, 3), Text(17, 8, "3"),
#             Rect(20, 10, 5, 5, 4), Text(22, 8, "4"),
#             Rect(25, 10, 5, 5, 5), Text(27, 8, "5"),
#             Rect(30, 10, 5, 5, 6), Text(32, 8, "6"),
#             Rect(35, 10, 5, 5, 7), Text(37, 8, "7"),
#             Rect(40, 10, 5, 5, 8), Text(42, 8, "8"),
#             Rect(45, 10, 5, 5, 9), Text(47, 8, "9"),
#             Rect(50, 10, 5, 5, 10), Text(52, 8, "10"),
#             ])


window.render()







#
