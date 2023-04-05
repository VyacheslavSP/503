from tkinter import *
from tkinter import ttk


class Etalon:
    def __init__(self, temp_et_arr, Hum_et_arr, temp_503, Hum_503, Press_503):
        self.temp_et_arr = temp_et_arr
        self.Hum_et_arr = Hum_et_arr
        self.temp_503 = temp_503
        self.Hum_503 = Hum_503
        self.Press_503 = Press_503

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


class Instrument:
    poz_ferst_cell = [12, 1]

    def __init__(self, Number_instr, Number_ZK, Poveritel, temp_mes_arr, Hum_mes_arr, Model):
        self.Number_instr = Number_instr
        self.Number_ZK = Number_ZK
        self.Poveritel = Poveritel
        self.temp_mes_arr = temp_mes_arr
        self.Hum_mes_arr = Hum_mes_arr
        self.Model = Model

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


def create_frame(label_text, how_many_rows):
    frame = ttk.Frame(borderwidth=1, relief=SOLID, padding=[8, 10])
    # добавляем на фрейм метку
    label = ttk.Label(frame, text=label_text)
    label.pack(anchor=NW)
    # добавляем на фрейм текстовое поле
    i = 0
    for i in range(how_many_rows):
        entry = ttk.Entry(frame)
        entry.pack(anchor=NW)
    # возвращаем фрейм из функции
    return frame


def click_button():
    tmp_list_cond = (conditions_frame.children)
    temp_503 = tmp_list_cond.get('!entry').get()
    Hum_503 = tmp_list_cond.get('!entry2').get()
    press_503 = tmp_list_cond.get('!entry3').get()
    tmp_temp = []
    tmp_list_temp = (temp_frame.children.keys())
    for key in tmp_list_temp:
        if key != "!label":
            tmp_temp.append(temp_frame.children.get(key).get())
    tmp_hum = []
    tmp_list_hum = (hum_frame.children.keys())
    for key in tmp_list_hum:
        if key != "!label":
            tmp_hum.append(hum_frame.children.get(key).get())
    global now_Etalon
    global PriborWindows
    now_Etalon = Etalon(tmp_temp, tmp_hum, temp_503, Hum_503, press_503)
    root.destroy()

    return now_Etalon


def click_button_exit():
    global hasNext
    hasNext = False
    PriborWindows.destroy()
    return hasNext


def click_button_next():
    pass


now_Etalon = None
PriborWindows = None
hasNext = True
list_pribors = []
root = Tk()
root.title("Эталонные данные")
root.geometry("275x450")

conditions_frame = create_frame("Введите условия поверки (т,вл,давл)", 3)
conditions_frame.pack(anchor=NW, fill=X, padx=5, pady=5)

temp_frame = create_frame("Введите эталонную температуру(5 точек)", 5)
temp_frame.pack(anchor=NW, fill=X, padx=5, pady=5)
hum_frame = create_frame("Введите эталонную влажность (5 точек)", 5)
hum_frame.pack(anchor=E, fill=X, padx=5, pady=5)
btn = ttk.Button(text="Заполнить", command=click_button)
btn.pack()
root.mainloop()

while (hasNext):
    PriborWindows = Tk()
    PriborWindows.title("Окно прибора")
    PriborWindows.geometry("275x450")
    conditions_frame = create_frame("Введите условия поверки (т,вл,давл)", 3)
    conditions_frame.pack(anchor=NW, fill=X, padx=5, pady=5)
    temp_frame = create_frame("Введите эталонную температуру(5 точек)", 5)
    temp_frame.pack(anchor=NW, fill=X, padx=5, pady=5)
    hum_frame = create_frame("Введите эталонную влажность (5 точек)", 5)
    hum_frame.pack(anchor=E, fill=X, padx=5, pady=5)
    btnExit = ttk.Button(text="Finish", command=click_button_exit)
    btnExit.pack(side=LEFT)
    btnNext = ttk.Button(text="Next", command=click_button_next)
    btnNext.pack(side=RIGHT)
    PriborWindows.mainloop()
