<<<<<<< HEAD
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
=======
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

iris = sns.load_dataset('iris')
iris = iris.drop('sepal_length', axis=1)

print (iris.columns)
fig = plt.figure()
ax=plt.axes(projection='3d')
ax.scatter(iris.petal_length, iris.petal_width,iris.sepal_width,cmap='plasma')
plt.xlabel('petal length')
plt.ylabel('petal width')
>>>>>>> 14a6c32569e77e87b7c2b340fe1497d42e3ab140
plt.show()