import matplotlib.pyplot as plt

def graficaBarras(indices, valores):
  
  figura, eje = plt.subplots() #esta función devuelve dos valores. La figura y el eje.
  eje.bar(list(indices),valores)
  plt.show() #muestra el gráfico

def graficaPastel(labels, values): 
  labels = list(labels)
  figura, eje = plt.subplots()
  eje.pie(values, labels=labels) #grafico de torta
  eje.axis('equal')
  plt.show()


def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  plt.show()


if __name__ == '__main__':
  
  indices = ['a','b','c']
  valores = [100,200,35]
  graficaBarras(indices, valores)
  graficaPastel(indices,valores)