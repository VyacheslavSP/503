value = 'Прибор комбинированный Testo 608-Н1,                                        Госреестр № 53505-13'
index = value.find("Госреестр")+12
value = value[:index]+"TEST"
print(value)
