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
