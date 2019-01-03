import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import math
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

sns.set_style('whitegrid')
sns.set_palette('Pastel1')

train_data = pd.read_csv('C:\\Users\\dkirksey\\Downloads\\Titanic\\train.csv')
test_data = pd.read_csv('C:\\Users\\dkirksey\\Downloads\\Titanic\\test.csv')

print(train_data.head(5))
print(train_data.describe())
print(train_data.info())

sns.heatmap(train_data.drop('Survived',axis=1).corr())
plt.show()

fig = plt.figure(figsize=(10,10))
ax=plt.axes()

#age vs survival
sns.distplot(train_data[train_data['Survived']==1]['Age'].dropna(),ax=ax,color='blue')
sns.distplot(train_data[train_data['Survived']==0]['Age'].dropna(),ax=ax,color='orange')
plt.suptitle('Distribution of Passengers by Age', fontsize=16)
plt.legend(['Survived','Did not Survive'])
plt.show()

#sex vs survival
sns.countplot(train_data['Sex'], hue=train_data['Survived'])
plt.suptitle('Passenger Survivals by Sex', fontsize=16)
plt.show()
#significatly larger percentage of women survived than men

sns.countplot(train_data['Embarked'], hue=train_data['Survived'])
plt.suptitle('Passenger Survivals by Embark Location', fontsize=16)
plt.show() #passenger chance of survival: c>Q>S

train_data['FamilySize'] = train_data['SibSp'] + train_data['Parch'] +1
sns.countplot(train_data['FamilySize'], hue=train_data['Survived'])
plt.suptitle('Passenger Survivals by Family Size', fontsize=16)
plt.show()

sns.boxplot(train_data['Survived'],train_data['Fare'])
plt.suptitle('Passenger Survival vs Ticket Fare', fontsize=16)
plt.show() #passengers with higher fares more likely to survive

sns.countplot(train_data['Pclass'], hue=train_data['Survived'])
plt.suptitle('Passenger Survival by Passenger Class', fontsize=16)
plt.show()


sns.boxplot(train_data['Pclass'], train_data['Age'], hue=train_data['Survived'])
plt.suptitle('Passenger Age vs Pclass', fontsize=16)
plt.show()

cleaned_data = train_data.drop(['Cabin','PassengerId','Name','Ticket'], axis=1)
cleaned_data['Sex']=pd.get_dummies(cleaned_data['Sex'])
cleaned_data['Embarked']=pd.get_dummies(cleaned_data['Embarked'])

def impute_age(row):
	if math.isnan(row['Age']):
		return cleaned_data['Age'].mean()
	else:
		return row['Age']

cleaned_data['Age']=cleaned_data.apply(lambda row : impute_age(row),axis=1)
cleaned_data = cleaned_data.dropna()

X = cleaned_data.drop('Survived', axis=1)
y= cleaned_data['Survived']

logreg=LogisticRegression()
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(logreg.intercept_)
print (pd.DataFrame(logreg.coef_, index=['Coefficients'], columns=X.columns))

svc = SVC()
svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

param_grid = {'C':[0.01,0.1,1,10,100,1000], 'gamma':[.0001, .001,.01,1,10,100,1000]}

grid = GridSearchCV(param_grid=param_grid, estimator=SVC(),refit=True, verbose=2)
grid.fit(X_train, y_train)
best_params = grid.best_params_
print(best_params) #C:1000, gamma:.0001

svc2 = SVC(C=1000, gamma=.0001)
svc2.fit(X_train, y_train)
y_pred = svc2.predict(X_test)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
#svm yields similar results to logreg
