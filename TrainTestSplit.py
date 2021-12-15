'''
Data Scientist Jr.: Dr.Eddy Giusepe Chirinos Isidro
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










