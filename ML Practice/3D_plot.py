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
plt.show()