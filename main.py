from tkinter import *
import random

# Ширина
WIDTH = 600
# Высота
HEIGHT = 400
# Размер головы
SIZ = 10
# Проверка на игру
IN_GAME = True
StartGame = True

"""Обработка всей программы"""


def mains():
    global IN_GAME
    global StartGame
    if IN_GAME:
        s.move()
        tail = 0, 0, 0, 0
        head_coords = c.coords(s.instance)
        x1, y1, x2, y2 = head_coords
        if StartGame:
            Platform()
            StartGame = False
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False
        if head_coords == c.coords(BLOCK):
            tail = head_coords
        else:
            create_tail(tail)
        root.after(100, mains)
    else:
        c.create_text(WIDTH / 2, HEIGHT / 2,
                      text="Игра окончена!",
                      font="Arial 20",
                      fill="red")


def create_tail(head):
    global TAIL
    x1, y1, x2, y2 = head
    TAIL = c.create_oval(x1, y1,
                         x2, y2,
                         fill="red")


"""Отрисовка ячейки платформы"""


class Platform(object):
    def __init__(self):
        global BLOCK
        i = 0
        g = 0
        pl = c.coords(s.instance)
        x1, y1, x2, y2 = pl
        for i in range(0, 9):
            if 0 <= i <= 2:
                BLOCK = c.create_rectangle(x1 + g, y1, x2 + g, y2,
                                           fill="green")
                g = g + 10
            elif 3 <= i <= 5:
                if i == 3:
                    BLOCK = c.create_rectangle(x1, y1 + 10, x2, y2 + 10,
                                               fill="green")
                    y1 += 10
                    y2 += 10
                    g = 0
                else:
                    g = g + 10
                    BLOCK = c.create_rectangle(x1 + g, y1, x2 + g, y2,
                                               fill="green")
            elif 6 <= i <= 8:
                if i == 6:
                    y1 += 10
                    y2 += 10
                    BLOCK = c.create_rectangle(x1, y1, x2, y2,
                                               fill="green")
                    g = 0
                else:
                    g = g + 10
                    BLOCK = c.create_rectangle(x1 + g, y1, x2 + g, y2,
                                               fill="green")


"""Класс головы который отвечает за направление движения и за передвижение"""


class Head(object):
    def __init__(self):
        global HEAD
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0), "None": (0, 0)}
        # initial movement direction
        self.vector = self.mapping["None"]

        posx = SIZ * random.randint(1, (WIDTH-50 - SIZ) / SIZ)
        posy = SIZ * random.randint(1, (HEIGHT-50 - SIZ) / SIZ)
        self.instance = c.create_oval(posx, posy,
                                      posx + SIZ, posy + SIZ,
                                      fill="White")

    def move(self):
        """ перемещает голову с указаным вектором"""
        cel = s.instance

        x1, y1, x2, y2 = c.coords(s.instance)
        if self.mapping == "None":
            c.coords(cel, x1, y1, x2, y2)
        else:
            c.coords(cel, x1 + self.vector[0] * SIZ, y1 + self.vector[1] * SIZ,
                     x2 + self.vector[0] * SIZ, y2 + self.vector[1] * SIZ)

    def change_direction(self, event):
        """ изменяет направление головы """
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]


# запуск формы
root = Tk()
root.title("Test")

"""Класс библиотеки tkinter"""
c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#003330")
c.grid()
c.focus_set()
s = Head()
c.bind('<KeyPress>', s.change_direction)
mains()
root.mainloop()
