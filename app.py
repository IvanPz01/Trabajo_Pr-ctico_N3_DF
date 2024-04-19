import pandas as pd

data = [
    "19",
    "29",
    "19",
    "22",
    "23",
    "19",
    "30",
    "19",
    "19",
    "19",
    "20",
    "20",
    "20",
    "18",
    "22",
    "19",
    "34",
    "34",
    "21",
    "21",
    "22",
    "28",
    "29",
    "19",
    "20",
    "19",
    "25",
    "28",
    "21",
    "22",
]

def analisis_estadistico(data):

    dict_numer = {}
    data_number = []
    if data == []:
        return 'No hay datos en el archivo'
    for i in data:
        if i.isdigit():
            data_number.append(int(i))
        else:
            return 'Los datos no son numericos'

    for i in data:
        if i in dict_numer:
            dict_numer[i] += 1
        else:
            dict_numer[i] = 1
    
    data_frame = pd.DataFrame(dict_numer.items(), columns=['Edad', 'fi'])
    data_frame.sort_values(by='Edad', inplace=True)
    data_frame.reset_index(drop=True, inplace=True)


    
    data_frame['Fi'] = data_frame['fi'].cumsum()
    data_frame['ri'] = data_frame['fi'] / data_frame['fi'].sum()
    data_frame['Ri'] = data_frame['ri'].cumsum()
    data_frame['pi%'] = data_frame['ri'] * 100
    data_frame['Pi%'] = data_frame['pi%'].cumsum()
    return data_frame


data_resul = analisis_estadistico(data)

print(data_resul)

