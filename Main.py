import time
import win32com.client
import shutil
import win32timezone


def build_value_general(path_of_excell):
    Excel = win32com.client.Dispatch("Excel.Application")
    wb = Excel.Workbooks.Open(path_of_excell)
    sheet = wb.ActiveSheet
    temp_et_arr = []
    Hum_et_arr = []
    for i in range(3):
        temp_et_arr.append(sheet.Cells(i+3, 1).value)
        i += 1
    i = 0
    for i in range(5):
        Hum_et_arr.append(sheet.Cells(i+7, 1).value)
        i += 1
    temp_503 = sheet.Cells(3, 2).value
    Hum_503 = sheet.Cells(5, 2).value
    Press_503 = sheet.Cells(7, 2).value
    # как много протоколов и даты-отдельная переменная не входящая в класс эталон
    How_many_prot = sheet.Cells(7, 6).value
    date_num = sheet.Cells(2, 3).value
    dete_moun = sheet.Cells(1, 10).value
    value_general = [temp_et_arr, Hum_et_arr, temp_503,
                     Hum_503, How_many_prot, date_num, dete_moun, Press_503]
    time.sleep(0.1)
    wb.Save()
    time.sleep(0.1)
    wb.Close()
    time.sleep(0.1)
    Excel.Quit()
    time.sleep(0.1)
    return value_general


def build_instrumet(path_of_excell, count_instr):
    Excel = win32com.client.Dispatch("Excel.Application")
    wb = Excel.Workbooks.Open(path_of_excell)
    sheet = wb.ActiveSheet
    temp_mes_arr = []
    Hum_mes_arr = []
    ferst_col = Instrument.poz_ferst_cell[1]
    ferst_row = Instrument.poz_ferst_cell[0]
    Number_instr = sheet.Cells(ferst_row+1, ferst_col+1+(count_instr*4)).value
    Number_ZK = sheet.Cells(ferst_row+1, ferst_col+2+(count_instr*4)).value
    Poveritel = sheet.Cells(ferst_row+1, ferst_col+3+(count_instr*4)).value
    for i in range(3):
        temp_mes_arr.append(sheet.Cells(
            ferst_row+2+i, 1+(count_instr*4)).value)
        i += 1
    i = 0
    for i in range(5):
        Hum_mes_arr.append(sheet.Cells(ferst_row+6+i, 1+(count_instr*4)).value)
        i += 1
    Model = "test"
    now_instrument = Instrument(
        Number_instr, Number_ZK, Poveritel, temp_mes_arr, Hum_mes_arr, Model)
    time.sleep(0.1)
    wb.Save()
    time.sleep(0.1)
    wb.Close()
    time.sleep(0.1)
    Excel.Quit()
    time.sleep(0.1)
    return now_instrument


class Instrument:
    poz_ferst_cell = [12, 1]
    

    def __init__(self, Number_instr, Number_ZK, Poveritel, temp_mes_arr, Hum_mes_arr, Model):
        self.Number_instr = Number_instr
        self.Number_ZK = Number_ZK
        self.Poveritel = Poveritel
        self.temp_mes_arr = temp_mes_arr
        self.Hum_mes_arr = Hum_mes_arr
        self.Model = Model


class Etalon:
    def __init__(self, temp_et_arr, Hum_et_arr, temp_503, Hum_503, Press_503):
        self.temp_et_arr = temp_et_arr
        self.Hum_et_arr = Hum_et_arr
        self.temp_503 = temp_503
        self.Hum_503 = Hum_503
        self.Press_503 = Press_503


def build_prot(Instrument, value_general):
    path_of_excell = Instrument.Path_sample
    Excel = win32com.client.Dispatch("Excel.Application")

    wb = Excel.Workbooks.Open(path_of_excell)
    sheet = wb.ActiveSheet
    sheet.Cells(7, 3).value = Instrument.Number_ZK
    sheet.Cells(7, 6).value = Instrument.Number_instr
    sheet.Cells(7, 8).value = value_general[5].day
    sheet.Cells(7, 9).value = value_general[6]
    sheet.Cells(7, 10).value = value_general[5].year
    sheet.Cells(16, 6).value = value_general[2]
    sheet.Cells(17, 6).value = value_general[3]
    sheet.Cells(18, 6).value = value_general[7]
    i = 0
    for i in range(15):
        if (i < 5):
            sheet.Cells(i+24, 1).value = value_general[0][0]
            sheet.Cells(i+24, 5).value = Instrument.temp_mes_arr[0]
        elif (5 <= i < 10):
            sheet.Cells(i+24, 1).value = value_general[0][1]
            sheet.Cells(i+24, 5).value = Instrument.temp_mes_arr[1]
        else:
            sheet.Cells(i+24, 1).value = value_general[0][2]
            sheet.Cells(i+24, 5).value = Instrument.temp_mes_arr[2]
            i += 1
    i = 0
    for i in range(5):
        sheet.Cells(i+43, 1).value = value_general[1][i]
        sheet.Cells(i+43, 5).value = Instrument.Hum_mes_arr[i]
    sheet.Cells(74, 5).value = Instrument.Poveritel
    NameFolder = Instrument.Poveritel.split('.')[2]
    NameFolder = NameFolder.split()[0]
    temp_num_instr = str(Instrument.Number_instr)
    pos1 = temp_num_instr.find('/')
    pos2 = temp_num_instr.find('\\')
    if (pos1 != -1):
        temp_num_instr = temp_num_instr[:pos1] + '_' + temp_num_instr[pos1+1:]
    elif (pos2 != -1):
        temp_num_instr = temp_num_instr[:pos2] + '_' + temp_num_instr[pos2+1:]
    NameProtok = "448-"+Instrument.Number_ZK+"-" + \
        str(value_general[5].year)+'-'+temp_num_instr+'.xls'
    PathToSave = 'Y:/Пугачев_НЕ_УДАЛЯТЬ/503/'+NameFolder+'/'+NameProtok
    wb.Save()
    time.sleep(0.1)
    wb.Close()
    time.sleep(0.1)
    Excel.Quit()
    time.sleep(0.1)

    return PathToSave


generalExcellPath = 'Y:/Пугачев_НЕ_УДАЛЯТЬ/503/main_file.xlsm'
generalPathsample = 'Y:/Пугачев_НЕ_УДАЛЯТЬ/503/608_sample.xls'
general = build_value_general(generalExcellPath)
i = 0
while i < general[4]:
    tmp = build_instrumet(generalExcellPath, i)
    tmpPath = build_prot(tmp, general)
    shutil.copyfile(generalPathsample, tmpPath)
    i += 1
