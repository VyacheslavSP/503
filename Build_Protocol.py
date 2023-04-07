import shutil
import time
import win32com.client
import Class


def parse_and_build_date(Instrument):
    tmp_date = Instrument.date_finish
    tmp_date = tmp_date.split('.')
    var_mes = int(tmp_date[1])
    match var_mes:
        case 1:
            tmp_date[1] = "января"
        case 2:
            tmp_date[1] = "февраля"
        case 3:
            tmp_date[1] = "марта"
        case 4:
            tmp_date[1] = "апреля"
        case 5:
            tmp_date[1] = "мая"
        case 6:
            tmp_date[1] = "июня"
        case 7:
            tmp_date[1] = "июля"
        case 8:
            tmp_date[1] = "августа"
        case 9:
            tmp_date[1] = "сентября"
        case 10:
            tmp_date[1] = "октября"
        case 11:
            tmp_date[1] = "ноября"
        case 12:
            tmp_date[1] = "декабря"
    return tmp_date


def main_buld(list_pribors):
    for Instrument_now in list_pribors:
        path_copy = build_prot(Instrument_now)
        path_sample = Instrument_now.Path_sample
        shutil.copyfile(path_sample, path_copy)


def parse_sring_gr(sheet, Instrument):
    tmp_string = sheet.Cells(11, 6).value
    index = tmp_string.find("Госреестр")+12
    tmp_string = tmp_string[:index]+Instrument.gosreestr
    sheet.Cells(11, 6).value = tmp_string


def build_prot(Instrument):
    date_arr = parse_and_build_date(Instrument)
    Excel = win32com.client.Dispatch("Excel.Application")
    wb = Excel.Workbooks.Open(Instrument.Path_sample)
    sheet = wb.ActiveSheet
    parse_sring_gr(sheet, Instrument)
    sheet.Cells(7, 3).value = Instrument.Number_ZK
    sheet.Cells(7, 6).value = Instrument.Number_instr
    sheet.Cells(7, 8).value = date_arr[0]
    sheet.Cells(7, 9).value = date_arr[1]
    sheet.Cells(7, 10).value = date_arr[2]
    sheet.Cells(14, 6).value = Instrument.mp
    sheet.Cells(16, 6).value = Instrument.Etalon.temp_503
    sheet.Cells(17, 6).value = Instrument.Etalon.Hum_503
    sheet.Cells(18, 6).value = Instrument.Etalon.Press_503
    sheet.Cells(19, 6).value = Instrument.EtalonsString
    i = 0
    temp_len = len(Instrument.temp_mes_arr)
    for i in range(Instrument.howManytempRepeet):
        if (i < int(Instrument.howManytempRepeet/temp_len)):
            sheet.Cells(i+24, 1).value = Instrument.Etalon_temp_arr[0]
            sheet.Cells(i+24, 5).value = Instrument.temp_mes_arr[0]
        elif (int(Instrument.howManytempRepeet/temp_len) <= i < int(Instrument.howManytempRepeet/temp_len)*2):
            sheet.Cells(i+24, 1).value = Instrument.Etalon_temp_arr[1]
            sheet.Cells(i+24, 5).value = Instrument.temp_mes_arr[1]
        else:
            sheet.Cells(i+24, 1).value = Instrument.Etalon_temp_arr[2]
            sheet.Cells(i+24, 5).value = Instrument.temp_mes_arr[2]
            i += 1
    i = 0
    for i in range(Instrument.howManyHumRepeet):
        sheet.Cells(i+43, 1).value = Instrument.Etalon_Hum_arr[i]
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
        str(date_arr[2])+'-'+temp_num_instr+'.xls'
    PathToSave = '//fs/Public/448/Пугачев_НЕ_УДАЛЯТЬ/503/'+NameFolder+'/'+NameProtok
    wb.Save()
    time.sleep(0.1)
    wb.Close()
    time.sleep(0.1)
    Excel.Quit()
    time.sleep(0.1)
    return PathToSave
