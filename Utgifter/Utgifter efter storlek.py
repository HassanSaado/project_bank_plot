import pandas as pd
import csv
''''''
# df = pd.read_csv('transaktioner2021.csv', encoding='ISO-8859-1', usecols=['Radnummer']) #ta ut den data du behover, gör en ny csv och spara där

belopp_lista = []
meddelande_lista = []
meddelande_lista_ny = []
tuple_data = []
dict = {}

with open('lf_data.csv', encoding='utf-8') as data:
    datan = csv.DictReader(data, delimiter=';')

    test_list = []
    meddelande_belopp = []

    for row in datan:  # spara datan från varje rads dict i två olika listor, eller spara båda värderna som tuple
        row_val = row["Belopp"]
        row_val2 = row["Meddelande"]
        row_val = row_val.lstrip("-")
        row_val = row_val.replace(" ", "")
        row_val = row_val.replace(",", ".")
        belopp_lista.append(float(row_val))
        meddelande_lista.append(row_val2)
    # print(len(belopp_lista))
    # print(len(meddelande_lista))


for i in range(len(meddelande_lista)):
    x = meddelande_lista[i].lower()
    x = x.replace(" ", "")
    x = x.replace(",", "")
    x = x.replace("*", "")
    x = x.replace("", "")
    x = x.replace("-", "")
    x = x.replace(".", "")
    meddelande_lista_ny.append(x)


tuple_data = list(zip(meddelande_lista_ny, belopp_lista))


for i in range(len(belopp_lista)):
    meddelande_belopp.append(meddelande_lista_ny[i])
    meddelande_belopp.append(belopp_lista[i])

for x in tuple_data:
    dict.update({(x)})
# print(dict)


"""
for key, value in dict.items():
    new_d.setdefault(key, 0)
    #new_d[key] += value
"""

#new_d = {key: sum(value) for key, value in dict.items()}


new_d = {}

# Iterate over the keys and values in the dictionary
for key, value in dict.items():
    # If the key exists in the new dictionary, add the value to the existing value for the key
    # Otherwise, create a new key-value pair with the key and value
    if key in new_d:
        new_d[key] += value
    else:
        new_d[key] = value

print(len(new_d))
print(len(dict))
