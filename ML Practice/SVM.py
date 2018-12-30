
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV

iris = sns.load_dataset('iris')
print(iris.head(5))
sns.pairplot(iris, hue='species')
plt.show()

setosa = iris[iris['species']=='setosa']
sns.kdeplot(setosa['sepal_width'], setosa['sepal_length'], cmap='plasma')
plt.show()
X=iris.drop('species', axis=1)
y=iris.species
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)
svc = SVC()
svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

param_grid = {'C':[0.01,0.1,1,10,100,100], 'gamma':[.0001, .001,.01,1,10,100,1000]}

grid = GridSearchCV(param_grid=param_grid, estimator=SVC(),refit=True, verbose=2)
grid.fit(X_train, y_train)
best_params = grid.best_params_
print(best_params) #C:1, gamma:1
grid_pred=grid.predict(X_test)
print(confusion_matrix(y_test, grid_pred))
print(classification_report(y_test, grid_pred))

