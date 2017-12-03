from tkinter import *
import random

# Ширина
WIDTH = 600
# Высота
HEIGHT = 400
# Размер головы
OVAL = 10
# Проверка на игру
IN_GAME = True

"""Обработка всей программы"""


def mains():
    global IN_GAME
    if IN_GAME:

        s.move()

        head = c.coords(s.cell[-1].instance)
        x1, y1, x2, y2 = head
        if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
            IN_GAME = False
        root.after(200, mains)
    else:
        c.create_text(WIDTH / 2, HEIGHT / 2,
                      text="Игра окончена!",
                      font="Arial 20",
                      fill="red")


""" Отрисовка головы"""


class Cell(object):

    def __init__(self):
        posx = OVAL * random.randint(1, (WIDTH - OVAL) / OVAL)
        posy = OVAL * random.randint(1, (HEIGHT - OVAL) / OVAL)
        self.instance = c.create_oval(posx, posy,
                                      posx + OVAL, posy + OVAL,
                                      fill="white")


"""Отрисовка ячейки платформы"""


class Platform(object):
    def __init__(self):
        posx = OVAL * random.randint(1, (WIDTH - OVAL) / OVAL)
        posy = OVAL * random.randint(1, (HEIGHT - OVAL) / OVAL)
        self.instance = c.create_rectangle(posx, posy,
                                           posx + OVAL, posy + OVAL,
                                           fill="green")



"""Класс головы который отвечает за направление движения и за передвижение"""


class Head(object):
    def __init__(self, cell):
        self.cell = cell
        self.mapping = {"Down": (0, 1), "Right": (1, 0),
                        "Up": (0, -1), "Left": (-1, 0), "None": (0, 0)}
        # initial movement direction
        self.vector = self.mapping["None"]

    def move(self):
        """ перемещает голову с указаным вектором"""
        for index in range(len(self.cell)):
            cel = self.cell[index].instance

            x1, y1, x2, y2 = c.coords(self.cell[index].instance)
            if self.mapping == "None":
                c.coords(cel, x1, y1, x2, y2)
            else:
                c.coords(cel, x1 + self.vector[0] * OVAL, y1 + self.vector[1] * OVAL,
                         x2 + self.vector[0] * OVAL, y2 + self.vector[1] * OVAL)

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

plat = [Platform()]
cell = [Cell()]
s = Head(cell)
c.bind('<KeyPress>', s.change_direction)
mains()
root.mainloop()
