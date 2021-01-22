import tkinter as tk
import tkinter.ttk as ttk
from math import sqrt, degrees, acos

# словарь цветов для групп виджетов GUI
color_style = {"Label": "gray75",
               "Canvas": "gray10",
               "Frame": "gray16",
               "Notebook": "gray25",
               "NotebookTabOff": "black",
               "NotebookTabOn": "gray25",
               "NotebookHeadline": "gray20",
               "Radiobutton": "gray90"}

Text = (" На плоскости дано множество точек. "
        "Найти такой треугольник \n с вершинами в этих "
        "в этих точках, у которого угол, образованный высотой\n "
        "и медианой, исходящих из одной вершины, минимален.")


class Vector(object):
    def __init__(self, dot1, dot2):
        self.vec = list()

        x = dot2[0] - dot1[0]
        y = dot2[1] - dot1[1]
        self.vec.append(x)
        self.vec.append(y)

    def module(self):

        # находит модуль вектора

        return sqrt(self.vec[0]*self.vec[0] + self.vec[1]*self.vec[1])

    def normalize(self):

        # находит нормаль вектора

        normal = list()
        module = self.module()

        x = self.vec[0] / module
        y = self.vec[1] / module

        normal.append(x)
        normal.append(y)
        return normal

    def multiply(self, vec1):

        # скалярное произведение векторов
        return self.vec[0]*vec1[0] + self.vec[1]*vec1[1]


class Triangle(object):
    def __init__(self, p1, p2, p3):
        self.p = (p1, p2, p3)  # точки треугольника

    def is_triangle(self):
        if ((self.p[1][1] - self.p[0][1]) * (self.p[2][0] - self.p[0][0]) !=
                (self.p[1][0] - self.p[0][0]) * (self.p[2][1] - self.p[0][1])):
            return True
        return False

    def get_median(self, p):

        # Находит медиану
        # p - вершина из которой исходит медиана

        i = (p + 1) % 3
        j = (p + 2) % 3

        x = (self.p[i][0] + self.p[j][0]) / 2
        y = (self.p[i][1] + self.p[j][1]) / 2

        return [x, y]

    def get_height(self, p):

        # Находит высоту по заданным точкам
        # j - вершина из которой исходит высота

        i = (p + 1) % 3
        j = (p + 2) % 3

        points = self.p
        vec1 = Vector(points[j], points[p])
        vec2 = Vector(points[j], points[i])

        mult = vec1.multiply(vec2.vec)
        module = vec2.module()
        k = mult / module
        normal = vec2.normalize()

        x = points[j][0] + normal[0] * k
        y = points[j][1] + normal[1] * k
        return [x, y]

    def get_angle(self, p):

        # нахождение угла

        i = (p + 1) % 3
        j = (p + 2) % 3

        points = self.p
        vec1 = Vector(points[p], points[j])
        vec2 = Vector(points[p], points[i])

        mult = vec1.multiply(vec2.vec)
        module1 = vec1.module()
        module2 = vec2.module()
        angle = mult / (module1*module2)

        return degrees(acos(angle))


class GUI(tk.Frame):

    def __init__(self):
        super().__init__()

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        w, h = get_geometry(sw, sh)
        self.bord = 30

        # Объявление виджетов

        self.entry_x = None  # виджеты слева
        self.entry_y = None

        # ----------------------------

        self.canvas = None  # виджеты посередине

        # ----------------------------

        self.nb = None
        self.f1 = None  # виджеты с вкладками(снизу)
        self.f2 = None
        self.f3 = None

        # ----------------------------

        self.list = []  # список точек(в формате строки)
        self.counter = 0  # счетчик точек
        self.listbox = None  # виджеты справа
        self.r_var = None
        self.entry_num = None
        self.entry_x1 = None
        self.entry_y1 = None
        self.entry_info = None

        # ----------------------------
        # Создание окна

        self.set_screen(sw, sh, w, h)
        self.generate_coord_widgets(w)  # справа
        self.generate_note_widgets(h)
        self.generate_point_widgets(w)  # слева
        self.generate_canvas_widgets(w)

    def set_screen(self, sw, sh, w, h):

        # устанавливает параметры экрана

        x = int((sw - w) / 2)
        y = int((sh - h) / 2)

        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.master.resizable(False, False)
        self.master.title('lab_01')

        self.pack(fill=tk.BOTH, expand=1)

    def generate_point_widgets(self, w):

        # создание виджетов для ввода параметров точки
        # расположение слева

        w = int(w/5)
        frame = tk.Frame(self,
                         width=w)
        frame.pack(side=tk.LEFT, fill=tk.Y)

        lbl = tk.Label(frame,
                       text="Введите координаты",
                       width=25,
                       bg=color_style["Label"])
        lbl_x = tk.Label(frame,
                         text="X: ",
                         bg=color_style["Label"])
        lbl_y = tk.Label(frame,
                         text="Y: ",
                         bg=color_style["Label"])
        lbl.grid(row=0, column=0, columnspan=2, sticky='swne')
        lbl_x.grid(row=1, column=0, sticky='wesn')
        lbl_y.grid(row=2, column=0, sticky='wesn')

        self.entry_x = tk.Entry(frame)
        self.entry_y = tk.Entry(frame)

        self.entry_x.grid(row=1, column=1, sticky='wesn')
        self.entry_y.grid(row=2, column=1, sticky='wesn')

        add_button = tk.Button(frame,
                               text="Добавить точку",
                               command=self.set_point)
        add_button.grid(row=3, column=0, columnspan=2, sticky="wesn")

        space_lbl = tk.Label(frame,
                             height=17,
                             bg=color_style["Frame"])  # да, тут косяк, я не хочу это исправлять
        space_lbl.grid(columnspan=2, sticky='wesn', pady=2)

        clr_all_butt = tk.Button(frame,
                                 text='Очистить все',
                                 command=self.clear_all)
        do_task_butt = tk.Button(frame,
                                 text='Решить',
                                 command=self.do_task)
        clr_all_butt.grid(columnspan=2, sticky='wen')
        do_task_butt.grid(columnspan=2, sticky='wen')

    def generate_canvas_widgets(self, w):
        frame = tk.Frame(self,
                         bg=color_style["Frame"],
                         width=3*w/5)
        frame.pack(side=tk.LEFT, fill=tk.Y)

        self.canvas = tk.Canvas(frame,
                                width=3*w/2,
                                bg=color_style["Canvas"],
                                relief='raised')
        self.canvas.pack(expand=1, fill=tk.Y)

    def generate_note_widgets(self, h):

        # создание окна вкладок для отображения
        # ошибок, задания, результата работы программы
        # расположение снизу

        h = int(h/4)

        frame = tk.Frame(self,
                         height=h)
        frame.pack(side=tk.BOTTOM, fill=tk.X)

        self.nb = ttk.Notebook(frame,
                               style="mystyle.TNotebook",
                               height=h)
        self.nb.pack(fill=tk.X)

        self.f1 = tk.Text(frame,
                          bg='gray25',
                          relief="flat",
                          font="Arial 10",
                          fg="White",
                          state=tk.DISABLED)
        generate_scrollbar(self.f1)

        self.f2 = tk.Text(frame,
                          bg='gray25',
                          relief="flat",
                          font="Arial 10",
                          fg="White")
        self.f2.insert(tk.INSERT, Text)
        self.f2.config(state=tk.DISABLED)

        generate_scrollbar(self.f2)

        self.f3 = tk.Text(frame,
                          bg='gray25',
                          relief="flat",
                          font="Arial 10",
                          fg="White",
                          state=tk.DISABLED)
        generate_scrollbar(self.f3)

        self.nb.add(self.f1, text='Ошибки')
        self.nb.add(self.f2, text='Задание')
        self.nb.add(self.f3, text='Результат')

    def generate_coord_widgets(self, w):

        # создание виджетов для хранения точек
        # виджеты для удаления/изменения точек
        # расположение справа

        frame = tk.Frame(self,
                         bg=color_style["Frame"],
                         width=w/5)
        frame.pack(side=tk.RIGHT, fill=tk.Y)

        lbl = tk.Label(frame,
                       text="Введнные точки",
                       width=25,
                       bg=color_style["Label"])
        lbl.grid(row=0, column=0, columnspan=2, sticky='swne')

        self.listbox = tk.Listbox(frame,
                                  height=15,
                                  selectmode=tk.SINGLE,
                                  font=('monospace', 10),
                                  selectbackground='black',
                                  selectforeground='white')
        self.listbox.grid(row=1, column=0, columnspan=2, sticky='swne')
        self.listbox.bind("<Button-1>", self.update_point_entries)
        chng_frame = tk.Frame(frame)
        chng_frame.grid(row=2, column=0, columnspan=2, sticky="wesn")

        self.r_var = tk.BooleanVar()
        self.r_var.set(0)
        clr_button = tk.Radiobutton(chng_frame,
                                    text='Удалить точку  ',
                                    variable=self.r_var,
                                    value=0,
                                    bg=color_style["Radiobutton"])
        chng_button = tk.Radiobutton(chng_frame,
                                     text='Изменить точку',
                                     variable=self.r_var,
                                     value=1,
                                     bg=color_style["Radiobutton"])
        clr_button.grid(column=0, sticky='we', columnspan=2)
        chng_button.grid(column=0, sticky='we', columnspan=2)
        chng_button.bind("<Button-1>", self.change_state)

        lbl = tk.Label(chng_frame,
                       text="Введите параметры точки",
                       width=25,
                       height=2,
                       bg=color_style["Label"])
        lbl.grid(row=2, column=0, columnspan=2, sticky='swne')

        lbl_num = tk.Label(chng_frame,
                           text="№: ",
                           bg=color_style["Label"])
        lbl_x = tk.Label(chng_frame,
                         text="X  : ",
                         bg=color_style["Label"])
        lbl_y = tk.Label(chng_frame,
                         text="Y  : ",
                         bg=color_style["Label"])
        lbl_num.grid(row=3, column=0, sticky='we')
        lbl_x.grid(row=4, column=0, sticky='we')
        lbl_y.grid(row=5, column=0, sticky='we')

        self.entry_num = tk.Entry(chng_frame,
                                  state=tk.DISABLED,
                                  disabledforeground='black')  # Возможно объединить?
        self.entry_x1 = tk.Entry(chng_frame,
                                 state=tk.DISABLED,
                                 disabledforeground='black')
        self.entry_y1 = tk.Entry(chng_frame,
                                 state=tk.DISABLED,
                                 disabledforeground='black')

        self.entry_num.grid(row=3, column=1, sticky='wesn')
        self.entry_x1.grid(row=4, column=1, sticky='wesn')
        self.entry_y1.grid(row=5, column=1, sticky='wesn')

        do_button = tk.Button(chng_frame,
                              text="Выполнить",
                              command=self.point_control)
        do_button.grid(row=6, columnspan=2, sticky='wesn', pady=1)

        self.entry_info = tk.Entry(chng_frame,
                                   state=tk.DISABLED,
                                   justify=tk.CENTER,
                                   disabledbackground=color_style["Label"],
                                   disabledforeground='black')
        self.entry_info.grid(row=7, columnspan=2, sticky='wesn', pady=1)

    # работа с точками в listbox
    # ------------------------------------------------------
    def set_point(self):

        # переносит значение точки в listbox

        point = get_coord(self.counter, self.entry_x, self.entry_y)
        if point:
            self.counter += 1
            self.list.append(point)
            self.listbox.insert(tk.END, point)

            self.clear_points()
            self.entry_x.focus_set()
        else:
            self.clear_points()
            self.set_error(self.f1, ('Некорректный ввод!\n'
                           'Введенные данные должны быть вещественными числами!\n\n'))

    def update_point_entries(self, event):

        # при двойном нажатии на точку в listbox
        # значения entry будут обновлены в соответствии
        # с координатами выбранной точки

        self.clear_coord()

        selected = self.listbox.curselection()
        if len(selected) == 2 or len(selected) == 0:
            return

        point = self.listbox.get(selected[0])
        num, x, y = get_split_line(point)

        fill_entry(self.entry_num, num)
        fill_entry(self.entry_x1, x)
        fill_entry(self.entry_y1, y)

        if self.r_var.get() == 1:
            # если radiobutton установлена на удаление координаты
            change_state(self.entry_x1, self.entry_y1, 'normal')

    def point_control(self):

        # В зависимости от значения radiobutton
        # Удаляеет или изменяет координаты точки в Listbox

        selected = self.listbox.curselection()
        if len(selected) == 2 or len(selected) == 0:
            self.set_error(self.f1, "Невозможно обработать элемент! Точка не была выбрана.\n\n")
            return

        if self.r_var.get() == 1:
            self.change_point(selected[0])
        else:
            self.delete_point(selected[0])

    def delete_point(self, selected):

        # удаляет выбранную точку из listbox

        self.listbox.delete(selected)
        self.clear_coord()
        self.clear_canvas()

        fill_entry(self.entry_info, 'Выполнено!')
        self.update_listbox()
        self.do_task()

    def change_point(self, selected):

        # Изменяет координаты точки

        point = get_coord(selected, self.entry_x1, self.entry_y1)
        if point is not None:
            self.delete_point(selected)
            self.listbox.insert(selected, point)
            change_state(self.entry_x1, self.entry_y1, 'disabled')
            self.do_task()
        else:
            self.set_error(self.f1, ('Некорректный ввод!\n'
                           'Введенные данные должны быть вещественными числами!\n\n'))
            self.clear_coord()
            change_state(self.entry_x1, self.entry_y1, 'normal')
            fill_entry(self.entry_info, 'Ошибка!')

    def change_state(self, event):
        change_state(self.entry_x1, self.entry_y1, 'normal')

    def update_listbox(self):

        points = self.listbox.get(0, tk.END)
        self.clear_listbox()
        amount = len(points)

        for i in range(amount):

            dot_pos = points[i].index('.')
            point = str(i+1) + points[i][dot_pos:]

            self.listbox.insert(tk.END, point)
        self.counter = amount

    # Функции очистки виджетов
    # -----------------------------------------------------
    def clear_points(self):

        # Очищает поля в левом frame

        self.entry_x.delete(0, tk.END)
        self.entry_y.delete(0, tk.END)

    def clear_coord(self):

        # Очищает поля в правом frame

        self.entry_x1['state'] = tk.NORMAL
        self.entry_y1['state'] = tk.NORMAL
        self.entry_num['state'] = tk.NORMAL

        self.entry_x1.delete(0, tk.END)
        self.entry_y1.delete(0, tk.END)
        self.entry_num.delete(0, tk.END)

        self.entry_x1['state'] = tk.DISABLED
        self.entry_y1['state'] = tk.DISABLED
        self.entry_num['state'] = tk.DISABLED

    def clear_tab(self, f):

        # очищает вкладку f в нижнем фрейме

        self.nb.select(f)
        f.config(state=tk.NORMAL)
        f.delete('1.0', tk.END)
        f.config(state=tk.DISABLED)

    def clear_notebook(self):

        # Очищает все вкладки в нижнем фрейме

        self.clear_tab(self.f1)
        self.clear_tab(self.f3)
        self.nb.select(self.f2)

    def clear_listbox(self):
        self.listbox.delete(0, tk.END)
        self.counter = 0

    def clear_canvas(self):
        self.canvas.delete("all")

    def clear_all(self):

        # очищает все данные с экранов

        self.clear_points()
        self.clear_coord()
        self.clear_notebook()
        self.clear_listbox()
        self.entry_x.focus_set()
        self.clear_canvas()

    # обработка результатов
    #  ----------------------------------------------------
    def set_error(self, f, message):
        # помещает текст ошибки в нужную вкладку
        self.nb.select(f)
        f.config(state=tk.NORMAL)
        f.insert(tk.INSERT, message)
        f.config(state=tk.DISABLED)

    def set_result(self, tr, angle, ind):

        # выводит результат работы программы

        median = tr.get_median(ind)
        height = tr.get_height(ind)

        self.nb.select(self.f3)

        self.f3.config(state=tk.NORMAL)
        message = ('   РЕЗУЛЬТАТ: \n'
                   '1) Треугольник: \t\t\t(%.1f, %.1f) U  (%.1f, %.1f) U (%.1f, %.1f)\n'
                   '2) Угол:  \t\t\t%.1f°\n'
                   '3) Медиана:\t\t\t(%.1f, %.1f) U  (%.1f, %.1f)\n'
                   '4) Высота: \t\t\t(%.1f, %.1f) U  (%.1f, %.1f)\n' %
                   (tr.p[0][0], tr.p[0][1], tr.p[1][0], tr.p[1][1],
                    tr.p[2][0], tr.p[2][1], angle, tr.p[ind][0],
                    tr.p[ind][1], median[0], median[1], tr.p[ind][0],
                    tr.p[ind][1], height[0], height[1]))
        message += '\n\n'
        self.f3.insert(tk.INSERT, message)
        self.f3.config(state=tk.DISABLED)

    # функции для Canvas
    # -----------------------------------------------------
    def do_task(self):

        lst = self.listbox.get(0, tk.END)
        if len(lst) >= 3:
            coords = set_float_coord(lst)  # приведение координат к float
            min_angle, tr, ind = get_triangle(coords)  # поиск треугольника

            if min_angle is not None:
                self.draw_triangle(tr, ind)
                self.set_result(tr, min_angle, ind)
            else:
                self.set_error(self.f1, 'Треугольник не был найден!'
                                        'Фигура вырождена.\n')
        else:
            self.set_error(self.f1, 'Ошибка! Введено недостаточно точек. \n'
                           'Для построение треугольника необходимо 3.\n')

    def draw_triangle(self, tr, ind):

        # рисует треугольник

        # найти координаты высоты и медианы
        median = tr.get_median(ind)
        height = tr.get_height(ind)

        # масштабировать координаты теругольника медианы и высоты

        scale = self.get_scale_params(median, height, tr)

        sc_tr = list()
        for i in range(3):
            p = self.scale(tr.p[i], scale)
            sc_tr.append(p)

        sc_m = self.scale(median, scale)
        sc_h = self.scale(height, scale)
        
        # отрисовка
        self.canvas.create_line(sc_tr[0], sc_tr[1], fill="white")
        self.canvas.create_line(sc_tr[0], sc_tr[2], fill="white")
        self.canvas.create_line(sc_tr[1], sc_tr[2], fill="white")
        self.canvas.create_line(sc_tr[ind], sc_m, fill='red')
        self.canvas.create_line(sc_tr[ind], sc_h, fill='red')
        self.canvas.create_line(sc_m, sc_h, fill='white')

        self.canvas.create_oval(sc_m[0] + 3, sc_m[1] + 3,
                                sc_m[0] - 3, sc_m[1] - 3,
                                fill="red")
        self.canvas.create_oval(sc_h[0] + 3, sc_h[1] + 3,
                                sc_h[0] - 3, sc_h[1] - 3,
                                fill="red")

        self.canvas.create_text(sc_m[0], sc_m[1] + 14,
                                text='M',
                                fill='white')
        self.canvas.create_text(sc_h[0]+5, sc_h[1] + 14,
                                text='H',
                                fill='white')

        for i in range(3):
            self.canvas.create_oval(sc_tr[i][0] + 3, sc_tr[i][1] + 3,
                                    sc_tr[i][0] - 3, sc_tr[i][1] - 3,
                                    fill="red")

            self.canvas.create_text(sc_tr[i][0], sc_tr[i][1]+14,
                                    text='(%.1f, %.1f)' % (tr.p[i][0], tr.p[i][1]),
                                    fill='white')

    def get_scale_params(self, median, height, tr):

        # находит коэфициенты масшитабирования

        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()

        min_x = min(median[0], height[0], tr.p[0][0],
                    tr.p[1][0], tr.p[2][0])
        max_x = max(median[0], height[0], tr.p[0][0],
                    tr.p[1][0], tr.p[2][0])
        min_y = min(median[1], height[1], tr.p[0][1],
                    tr.p[1][1], tr.p[2][1])
        max_y = max(median[1], height[1], tr.p[0][1],
                    tr.p[1][1], tr.p[2][1])

        kx = (w - 2*self.bord) / (max_x - min_x)
        ky = (h - 2*self.bord) / (max_y - min_y)

        k = min(kx, ky)

        return [min_x, min_y, k]

    def scale(self, point, sc_p):

        # sc_p - scale_parameters
        # масштабирует точку по обеим координатам

        h = self.canvas.winfo_height()

        x = (point[0] - sc_p[0]) * sc_p[2] + self.bord
        y = h - (point[1] - sc_p[1]) * sc_p[2] - self.bord
        return [x, y]

    # -----------------------------------------------------


# функции, которым не нашлось места в классе
# ---------------------------------------------------------

def generate_scrollbar(f):

    # прикручивает scroll к виджету

    scrollbar = tk.Scrollbar(f)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    f.config(yscrollcommand=scrollbar.set)


def fill_entry(entry, text):

    # записывает в entry значение

    entry['state'] = tk.NORMAL
    entry.delete(0, tk.END)
    entry.insert(0, text)
    entry['state'] = tk.DISABLED


def change_state(entry_x, entry_y, state):
    entry_x['state'] = state
    entry_y['state'] = state


# работа со строкой
# ---------------------------------------------------------
def check_input(coord):

    # провека введенной пользователем строки
    # на корректность ввода

    result = 1
    try:
        float(coord)
    except ValueError:
        result = 0
    return result


def fix_string(coord):

    # убирает из строки лишние знаки, типа "+"
    # На вход подается проверенная строка

    return str(float(coord))


def make_dot_str(num, x, y):

    #  приводит координаты к виду для заполнения
    #  listbox, формат: "позиция. (x, y)"

    return str(num) + '. ' + \
           '(' + x + ', ' + y + ')'


def get_coord(counter, entry_x, entry_y):

    # принимает из индекс и параметры точки
    # проверяет корректность их ввода
    # преобразует в виду "позиция. (x, y)"

    point_x = entry_x.get()
    point_y = entry_y.get()

    if check_input(point_x) and check_input(point_y):
        counter += 1
        point_x = fix_string(point_x)  # удаляет из строки + (если есть)
        point_y = fix_string(point_y)
        point = make_dot_str(counter, point_x, point_y)  # создает строку для записи в листбокс
    else:
        point = None
    return point


def get_split_line(point):

    # преобразует строку из формата "позиция. (x, y)"
    # в формат "позиция", "x", "y"

    num = point[0]
    xend = point.index(',')

    x = point[4: xend]
    y = point[xend+2:-1]

    return num, x, y


def set_float_coord(points):

    # приводит координаты к типу int

    coords = list()
    for i in range(len(points)):
        num, x, y = get_split_line(points[i])
        c = list()
        c.append(float(x))
        c.append(float(y))
        coords.append(c)

    return coords
# ----------------------------------------------


# Поиск треугольника
# ----------------------------------------------
def get_triangle(points):

    # Получает на вход координаты точек(float)
    # Ищет треугольник с наименьшим углом

    amount = len(points)
    triangle = list()
    min_angle = None
    ind = None  # индекс вершины из которой исходят высота и медиана

    for i in range(amount):
        for j in range(i+1, amount):
            for k in range(j+1, amount):

                tr = Triangle(points[i], points[j], points[k])

                if tr.is_triangle():
                    angle, tmp_ind = get_angle(tr)

                    if min_angle is None or min_angle > angle:
                        min_angle, ind = angle, tmp_ind
                        triangle = tr
    return min_angle, triangle, ind


def get_angle(triangle):

    # находит наименьший угол между медианой и высотой

    min_angle = None
    ind = None
    for i in range(3):
        median = triangle.get_median(i)
        height = triangle.get_height(i)

        tr = Triangle(triangle.p[i], median, height)
        angle = tr.get_angle(0)

        if not min_angle or min_angle > angle:
            min_angle = angle
            ind = i
    return min_angle, ind


# ----------------------------------------------
def get_geometry(sw, sh):

    # получение параметров окна в зависимости от
    # параметров экрана

    w = sw / 3 * 2
    h = sh / 3 * 2
    return int(w), int(h)


def main():
    root = GUI()

    # определение нового стиля для виджетов ttk(Notebook)

    style = ttk.Style()
    style.theme_create("MyStyle", parent="clam", settings={
        "TNotebook": {"configure": {"tabmargins": [0, 0, 0, 0], "background": "gray20"}},
        "TNotebook.Tab": {
            "configure": {"padding": [45, 4], "background": "gray5", "foreground": "white"},
            "map": {"background": [("selected", "gray25")],
                    "foreground": [("selected", "white")],
                    "expand": [("selected", [0, 0, 0, 0])]}}})
    style.theme_use("MyStyle")
    style.layout("mystyle.TNotebook", [('mystyle.TNotebook', {'sticky': 'nswe'})])

    root.mainloop()


if __name__ == '__main__':
    main()
