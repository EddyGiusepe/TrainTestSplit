# TrainTestSplit
Neste pequeno Script, lembraremos como dividir um conjunto de Dados em ``train`` e ``test``.
É importante fazer isto porque um algoritmo de Machine Learning precisa ser treinado e
logo avaliado com Dados que nunca viu (que seria nossos Dados de test). Não podemos 
utilizar todos nossos Dados apenas para treinamento, porque causariamos um *overfit*.


Aqui vamos a utilizar a biblioteca ``sklearn`` e o Dataset do iris.