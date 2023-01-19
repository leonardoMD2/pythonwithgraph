import csv, graficos

def lecturaCol(path):
    numbers=[]
    countries = []
    with open(path, 'r') as datos:
        reader = csv.reader(datos,delimiter=',')
        next(reader) 
        for item in reader:
            numbers.append(float(item[-1]))
            countries.append(item[2])
            grupo = zip(countries, numbers)
            dict = {key:value for key, value in grupo}
            
        return dict


res = lecturaCol('data.csv')
graficos.graficaPastel(res.keys(),res.values())
graficos.graficaBarras(res.keys(),res.values())