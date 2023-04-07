from tkinter import *
from tkinter import ttk
from Build_Protocol import main_buld


class ModelIfo:
    def __init__(self, howManyTemp, howManyHum, dopusk_temp, Name, dopusk_hum, gosreestr, MP, path_to_sample, howManytempRepeet, howManyHumRepeet):
        self.howManyTemp = howManyTemp
        self.howManyHum = howManyHum
        self.dopusk_temp = dopusk_temp
        self.dopusk_hum = dopusk_hum
        self.gosreestr = gosreestr
        self.MP = MP
        self.Name = Name
        self.path_to_sample = path_to_sample
        self.howManytempRepeet = howManytempRepeet
        self.howManyHumRepeet = howManyHumRepeet

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


class Etalon:
    def __init__(self, temp_et_arr, Hum_et_arr, temp_503, Hum_503, Press_503):
        self.temp_et_arr = temp_et_arr
        self.Hum_et_arr = Hum_et_arr
        self.temp_503 = temp_503
        self.Hum_503 = Hum_503
        self.Press_503 = Press_503

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


class EtalonsString:
    stringEtalon = None

    def __init__(self, name_model_for_search, Poveritel):
        dict_etalonString = {'Testo 608-Н1': {'Ю.А. Иванова': 'Гигрометр Rotronic, модификация HygroLog NT, исполнение HL-NT3-D, Госреестр № 64196-16, зав.№ 61693572, 2Р. Термометр сопротивления платиновый вибропрочный эталонный ПТСВ-1-2, Госреестр № 32777-06, зав.№ 381, 2Р. Измеритель-регулятор температуры многоканальный прецизионный, тип МИТ8, мод. МИТ8.10, Госреестр № 19736-05, зав.№ 248, 3Р.', 'Е.Д. Зайцева ': 'Гигрометр Rotronic, модификация HygroLog NT, исполнение HL-NT3-D, Госреестр № 64196-16, зав.№ 61693572, 2Р. Термометр сопротивления платиновый вибропрочный эталонный ПТСВ-1-2, Госреестр № 32777-06, зав.№ 381, 2Р. Измеритель-регулятор температуры многоканальный прецизионный, тип МИТ8, мод. МИТ8.10, Госреестр № 19736-05, зав.№ 248, 3Р.', 'А.В. Бутягин': 'Гигрометр Rotronic, модификация HygroLog NT, исполнение HL-NT3-D, Госреестр № 64196-16, зав.№ 61693572, 2Р. Термометр сопротивления платиновый вибропрочный эталонный ПТСВ-1-2, Госреестр № 32777-06, зав.№ 381, 2Р. Измеритель-регулятор температуры многоканальный прецизионный, тип МИТ8, мод. МИТ8.10, Госреестр № 19736-05, зав.№ 248, 3Р.'}, 'Testo 608-Н2': {
            'Ю.А. Иванова': 'Гигрометр Rotronic, модификация HygroLog NT, исполнение HL-NT3-D, Госреестр № 64196-16, зав.№ 61693572, 2Р. Термометр сопротивления платиновый вибропрочный эталонный ПТСВ-1-2, Госреестр № 32777-06, зав.№ 381, 2Р. Измеритель-регулятор температуры многоканальный прецизионный, тип МИТ8, мод. МИТ8.10, Госреестр № 19736-05, зав.№ 248, 3Р.', 'Е.Д. Зайцева ': 'Гигрометр Rotronic, модификация HygroLog NT, исполнение HL-NT3-D, Госреестр № 64196-16, зав.№ 61693572, 2Р. Термометр сопротивления платиновый вибропрочный эталонный ПТСВ-1-2, Госреестр № 32777-06, зав.№ 381, 2Р. Измеритель-регулятор температуры многоканальный прецизионный, тип МИТ8, мод. МИТ8.10, Госреестр № 19736-05, зав.№ 248, 3Р.', 'А.В. Бутягин': 'Гигрометр Rotronic, модификация HygroLog NT, исполнение HL-NT3-D, Госреестр № 64196-16, зав.№ 61693572, 2Р. Термометр сопротивления платиновый вибропрочный эталонный ПТСВ-1-2, Госреестр № 32777-06, зав.№ 381, 2Р. Измеритель-регулятор температуры многоканальный прецизионный, тип МИТ8, мод. МИТ8.10, Госреестр № 19736-05, зав.№ 248, 3Р.'}, 'Test_TKA_PKM': {'Ю.А. Иванова': 'что то другое для ПКМ', 'Е.Д. Зайцева ': 'что то для ПКМ', 'А.В. Бутягин': 'третий набор эталонов для ТКА'}}
        for key_model in dict_etalonString:
            if (key_model == name_model_for_search):
                tmp_dicst = dict_etalonString.get(key_model)
                for kee_pover in tmp_dicst:
                    if (kee_pover == Poveritel):
                        stringEtalon = dict_etalonString.get(
                            key_model).get(kee_pover)
                        self.stringEtalon = stringEtalon

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


class Instrument:
    poz_ferst_cell = [12, 1]
    Number_instr = None
    Number_ZK = None
    Poveritel = None
    temp_mes_arr = []
    Hum_mes_arr = []
    Model = None
    Etalon_temp_arr = []
    Etalon_Hum_arr = []
    date_finish = None
    gosreestr = None
    mp = None
    Etalon = None
    EtalonsString = None
    Path_sample = None
    howManytempRepeet = None
    howManyHumRepeet = None

    def __init__(*args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


def create_from_grid(Name, howManyRows, howManyColum, model, Start_row):
    Label(text=Name).grid(row=Start_row+1, column=0)
    i = 0
    j = 0
    for j in range(howManyColum):
        for i in range(howManyRows):
            entry = Entry()
            entry.grid(row=i+1+1+Start_row, column=j, sticky=E)
            if (Name == "температура(что должно быть,эталон,измеренное)"):
                if (j == 0):
                    tmp_str = str(model.dopusk_temp[i][0]) + \
                        "..."+str(model.dopusk_temp[i][1])
                    entry.insert(0, tmp_str)
                elif (j == 1):
                    dopusk_ot = model.dopusk_temp[i][0]
                    dopusk_do = model.dopusk_temp[i][1]
                    etalon_arr = now_Etalon.temp_et_arr
                    for k in range(len(etalon_arr)):
                        if (dopusk_ot <= float(etalon_arr[k]) <= dopusk_do):
                            entry.insert(
                                i+Start_row, float(etalon_arr[k]))
                            break
            elif (Name == "Влажность(что должно быть,эталон,измеренное)"):
                if (j == 0):
                    tmp_str = str(model.dopusk_hum[i][0]) + \
                        "..."+str(model.dopusk_hum[i][1])
                    entry.insert(0, tmp_str)
                elif (j == 1):
                    dopusk_ot = model.dopusk_hum[i][0]
                    dopusk_do = model.dopusk_hum[i][1]
                    etalon_arr = now_Etalon.Hum_et_arr
                    for k in range(len(etalon_arr)):
                        if (dopusk_ot <= float(etalon_arr[k]) <= dopusk_do):
                            entry.insert(
                                i+Start_row, float(etalon_arr[k]))
                            break
    return howManyColum+3+Start_row


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


def delete_frame():
    list_frame = PriborWindows.children
    tmp_list_deleted = []
    for key in list_frame.keys():
        if (key.find("!entry") != -1):
            tmp_list_deleted.append(list_frame.get(key))
    i = 0
    array_size = len(tmp_list_deleted)
    for i in range(array_size):
        tmp_list_deleted[i].destroy()
        i += 1
    return


def clear_combobox():
    # Создайте функцию для очистки поля со списком
    combobox_model.set('')


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


def try_build_instrument():
    global list_pribors
    global now_instrument
    now_instrument = Instrument()
    count = 0
    hum_start = MODEL.howManyTemp*2+MODEL.howManyTemp
    hum_stop = hum_start+MODEL.howManyHum*2+MODEL.howManyHum
    tmp_et_arr_temp = []
    tmp_et_hum_arr = []
    tmp_instrum_arr_temp = []
    tmp_instrum_hum_temp = []
    tmp_number_instrument = None
    tmp_number_ZK = None
    tmp_date = None
    for key in PriborWindows.children.keys():
        if (key.find("!entry") != -1):
            if (MODEL.howManyTemp <= count < MODEL.howManyTemp*2):
                tmp_et_arr_temp.append(PriborWindows.children.get(key).get())
            elif (MODEL.howManyTemp*2 <= count < hum_start):
                tmp_instrum_arr_temp.append(
                    PriborWindows.children.get(key).get())
            elif (hum_start+MODEL.howManyHum <= count < hum_start+MODEL.howManyHum*2):
                tmp_et_hum_arr.append(
                    PriborWindows.children.get(key).get())
            elif (hum_start+MODEL.howManyHum*2 <= count < hum_stop):
                tmp_instrum_hum_temp.append(
                    PriborWindows.children.get(key).get())
            elif (count == hum_stop):
                tmp_number_instrument = PriborWindows.children.get(key).get()
            elif (count == hum_stop+1):
                tmp_number_ZK = PriborWindows.children.get(key).get()
            elif (count == hum_stop+2):
                tmp_date = PriborWindows.children.get(key).get()
            count += 1
    tmp_pover = PriborWindows.children.get(
        '!combobox2').get()  # жестко второй комбобокс
    now_Etalon.temp_et_arr = tmp_et_arr_temp
    now_Etalon.Hum_et_arr = tmp_et_hum_arr
    now_instrument.Etalon = now_Etalon
    now_instrument.Etalon_temp_arr = tmp_et_arr_temp
    now_instrument.Etalon_Hum_arr = tmp_et_hum_arr
    now_instrument.Hum_mes_arr = tmp_instrum_hum_temp
    now_instrument.Model = MODEL.Name
    now_instrument.Poveritel = tmp_pover
    now_instrument.temp_mes_arr = tmp_instrum_arr_temp
    now_instrument.Number_instr = tmp_number_instrument
    now_instrument.Number_ZK = tmp_number_ZK
    now_instrument.date_finish = tmp_date
    now_instrument.mp = PriborWindows.children.get(
        '!combobox4').get()
    now_instrument.gosreestr = PriborWindows.children.get(
        '!combobox3').get()
    now_instrument.EtalonsString = tmpStringEtalon.stringEtalon
    now_instrument.Path_sample = MODEL.path_to_sample
    now_instrument.howManytempRepeet = MODEL.howManytempRepeet * \
        len(now_instrument.temp_mes_arr)
    now_instrument.howManyHumRepeet = MODEL.howManyHumRepeet * \
        len(now_instrument.Hum_mes_arr)
    list_pribors.append(now_instrument)
    return list_pribors


def click_button_exit():
    global hasNext
    hasNext = False
    PriborWindows.destroy()
    return hasNext


def callback_gr(*arg):
    if (arg != ('',)):
        combobox_MP['values'] = MODEL.MP[var_gr.get()]


def callback_pover(*arg):
    if (arg != ('',)):
        global tmpStringEtalon
        StringEtalonsentry.delete(0, 'end')
        tmpStringEtalon = EtalonsString(MODEL.Name, combobox_pover.get())
        StringEtalonsentry.insert(0, tmpStringEtalon.stringEtalon)


def callback(*arg):
    global MODEL
    match str(var.get()):
        case "Testo 608-Н1":
            MODEL = Testo_608_Н1
        case "Testo 608-Н2":
            MODEL = Testo_608_Н2
        case "Test_TKA_PKM":
            MODEL = Test_TKA_PKM

        case _:
            print("Code not found")
    delete_frame()
    global combobox_MP
    global StringEtalonsentry
    global combobox_pover

    text = "температура(что должно быть,эталон,измеренное)"
    start_row = create_from_grid(text, MODEL.howManyTemp, 3, MODEL, 0)
    text = "Влажность(что должно быть,эталон,измеренное)"
    start_row = create_from_grid(text, MODEL.howManyHum, 3, MODEL, start_row)
    Label(text="Поверитель").grid(row=start_row+1, column=1, sticky=W)
    var_mp = StringVar()
    combobox_pover = ttk.Combobox(PriborWindows, textvariable=var_pover)
    combobox_pover['values'] = Poveritel_list
    combobox_pover['state'] = 'readonly'
    combobox_pover.grid(row=start_row+2, column=1, sticky=W)
    Label(text="№ прибора").grid(row=start_row+3, column=0, sticky=E)
    Label(text="№ з/к").grid(row=start_row+3, column=1, sticky=E)
    Label(text="Дата оформления").grid(
        row=start_row+3, column=2, sticky=E)
    number_instrument = Entry()
    number_ZK = Entry()
    date_prot = Entry()
    StringEtalonsentry = Entry()
    number_instrument.grid(row=start_row+4, column=0, sticky=E)
    number_ZK.grid(row=start_row+4, column=1, sticky=E)
    date_prot.grid(row=start_row+4, column=2, sticky=E)
    # если бубут нужны поля госреестр,методика,эталоны- влючать сюда
    Label(text="Госреестр").grid(row=start_row+5, column=0, sticky=W)
    Label(text="МП").grid(row=start_row+5, column=1, sticky=W)
    Label(text="Эталоны").grid(row=start_row+5, column=2, sticky=W)
    combobox_gr = ttk.Combobox(PriborWindows, textvariable=var_gr)
    combobox_gr['values'] = MODEL.gosreestr
    combobox_gr['state'] = 'readonly'
    combobox_gr.grid(row=start_row+6, column=0, sticky=W)
    combobox_MP = ttk.Combobox(PriborWindows, textvariable=var_mp)
    combobox_MP['values'] = MODEL.MP[MODEL.gosreestr[0]]
    combobox_MP['state'] = 'readonly'
    combobox_MP.grid(row=start_row+6, column=1, sticky=W)
    StringEtalonsentry.grid(row=start_row+6, column=2, sticky=W)
    btnExit = ttk.Button(text="Exit", command=click_button_exit)
    btnExit.grid(row=100, column=0, sticky=S+E)
    btnNext = ttk.Button(text="Next", command=click_button_next)
    btnNext.grid(row=100, column=1, sticky=S+W)


def build_PriborWindows():
    global PriborWindows
    global combobox_model
    global var
    global var_gr
    global var_pover
    PriborWindows = Tk()
    PriborWindows.title("Окно прибора")
    PriborWindows.geometry("600x400")
    PriborWindows.resizable(0, 0)
    PriborWindows.overrideredirect(1)
    var = StringVar()
    var_gr = StringVar()
    var_pover = StringVar()
    combobox_model = ttk.Combobox(PriborWindows, textvariable=var)
    combobox_model['values'] = Model
    combobox_model['state'] = 'readonly'
    combobox_model.grid(row=0, column=0)
    combobox_model.current(0)
    var.trace('w', callback)
    var_gr.trace('w', callback_gr)
    var_pover.trace('w', callback_pover)
    PriborWindows.mainloop()


def click_button_next():
    try_build_instrument()
    PriborWindows.destroy()
    pass
# структура модели в части гр и МП:
# госреестр это список со стрингами;МП это словарь, ключ-стринга ГР,значение список методик


Testo_608_Н1 = ModelIfo(3, 5, [[0, 3], [20, 30], [
    40, 50]], 'Testo 608-Н1', [[15, 19], [28, 32], [48, 52], [73, 77], [81, 85]], ['53505-13'], {'53505-13': ['МП РТ 1868-2013 с изменением №1 "Приборы комбинированные Testo 608-H1, Testo 608-H1, Testo 610, Testo 622, Testo 623", согл. ФБУ «Ростест-Москва» 16.02.2022 г.']}, '//fs/Public/448/Пугачев_НЕ_УДАЛЯТЬ/503/608_H1_sample.xls', 5, 1)
Testo_608_Н2 = ModelIfo(3, 5, [[-10, -9], [20, 30], [60, 70]],
                        'Testo 608-Н2', [[15, 19], [28, 32], [48, 52], [73, 77], [81, 85]], ['53505-13'], {'53505-13': ['МП РТ 1868-2013 с изменением №1 "Приборы комбинированные Testo 608-H1, Testo 608-H1, Testo 610, Testo 622, Testo 623", согл. ФБУ «Ростест-Москва» 16.02.2022 г.']}, '//fs/Public/448/Пугачев_НЕ_УДАЛЯТЬ/503/608_H2_sample.xls', 5, 1)
Test_TKA_PKM = ModelIfo(5, 2, [[-10, -9], [20, 30], [10, 20],
                               [60, 70], [80, 90]], 'Test_TKA_PKM', [[15, 19], [21, 25]], ['24248-09', '24240-04'], {'24248-09': ['МП 9 года', 'МП16 Года'], '24240-04': ['методика 4 года']}, '//fs/Public/448/Пугачев_НЕ_УДАЛЯТЬ/503/TEST_TKA_sample.xls', 5, 1)
Model = (Testo_608_Н1.Name, Testo_608_Н2.Name,
         Test_TKA_PKM.Name)
now_Etalon = None
hasNext = True
MODEL = None

StringEtalonValue = None
Poveritel_list = ("Ю.А. Иванова", "Е.Д. Зайцева ", "А.В. Бутягин")
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
# testEtalon_string = EtalonsString(Test_TKA_PKM.Name, Poveritel_list[0])
# print(testEtalon_string.stringEtalon)
while (hasNext):
    build_PriborWindows()

main_buld(list_pribors)
