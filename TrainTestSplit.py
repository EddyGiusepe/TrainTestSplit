'''
Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro
Link de estudo: https://www.youtube.com/watch?v=8Jfc1w8wwII
'''

# Importamos as nossas bibliotecas:
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd

# importamos nossos Dados:
iris = load_iris()
print(iris)
# iris_df = pd.DataFrame(iris.data)
# print(iris_df)
print("Apresentamos a nossas feature_names (sepal length - sepal width - petal length - petal width) :")
print(iris.data.shape)
print(iris.data)
print("Mostramos, agora, nossas etiquetas - target: ")
print(iris.target.shape)
print(iris.target)

print("Escrevemos nossos Dados de train e test: ")
# y_train, são nossas labels as quais por default são embaralhadas
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target)
print("Escrevemos o shape de nossos Dados para ver como foi feito a divisão: ")
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

print("y_train, embaralhada será: ", y_train)

print("Manipulando mais um pouco nossos Dados: ")
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.30)
# Também podemos colocar:  test_size=50 --> A quantidade para teste
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)














