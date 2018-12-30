import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

iris = sns.load_dataset('iris')
iris = iris.drop('sepal_length', axis=1)

print (iris.columns)
print (iris['species'].value_counts())

setosa = iris[iris['species']=='setosa']
virginica = iris[iris['species']=='virginica']
versicolor = iris[iris['species']=='versicolor']

fig = plt.figure()
ax=plt.axes(projection='3d')

ax.scatter(setosa.petal_length, setosa.petal_width,setosa.sepal_width,c='red')
ax.scatter(virginica.petal_length, virginica.petal_width,virginica.sepal_width,c='blue')
ax.scatter(versicolor.petal_length, versicolor.petal_width,versicolor.sepal_width,c='green')

plt.title('Iris Data Set')
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.show()