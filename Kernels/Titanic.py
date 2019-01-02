import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import math

sns.set_style('whitegrid')
train_data = pd.read_csv('C:\\Users\\dkirksey\\Downloads\\Titanic\\train.csv')
test_data = pd.read_csv('C:\\Users\\dkirksey\\Downloads\\Titanic\\test.csv')
print(train_data.head(5))
print(train_data.describe())
print(train_data.info())

sns.heatmap(train_data.drop('Survived',axis=1).corr())
plt.show()
fig = plt.figure(figsize=(10,10))
ax=plt.axes()
sns.distplot(train_data[train_data['Survived']==1]['Age'].dropna(),ax=ax,color='blue')
sns.distplot(train_data[train_data['Survived']==0]['Age'].dropna(),ax=ax,color='orange')
plt.show()

sns.countplot(train_data['Survived'], hue=train_data['Sex'])
plt.show()
#a larger percentage of women survived than men
sns.countplot(train_data['Embarked'], hue=train_data['Survived'])
plt.show() #passenger chance of survival: c>Q>S

train_data['FamilySize'] = train_data['SibSp'] + train_data['Parch'] +1
sns.countplot(train_data['FamilySize'], hue=train_data['Survived'])
plt.show()

sns.boxplot(train_data['Survived'],train_data['Fare'])
plt.show() #passengers with higher fares more likely to survive

sns.countplot(train_data['Pclass'], hue=train_data['Survived'])
# plt.show()
# print(train_data['Ticket'])
#
# sns.boxplot(train_data['Pclass'], train_data['Age'], hue=train_data['Survived'])
# plt.show()
cleaned_data = train_data.drop(['Cabin','PassengerId','Name','Ticket'], axis=1)

cleaned_data['Sex']=pd.get_dummies(cleaned_data['Sex'])
cleaned_data['Embarked']=pd.get_dummies(cleaned_data['Embarked'])
cleaned_data['Age'] = pd.Series(cleaned_data['Age'].values)
print (train_data['Age'].mean())
def impute_age(row):
	if math.isnan(row['Age']):
		return cleaned_data['Age'].mean()
	else:
		return row['Age']

cleaned_data['Age']=cleaned_data.apply(lambda row : impute_age(row),axis=1)
print (cleaned_data['Age'])
cleaned_data = cleaned_data.dropna()

X = cleaned_data.drop('Survived', axis=1)
y= cleaned_data['Survived']

logreg=LogisticRegression()
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))