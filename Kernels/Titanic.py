import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

train_data = pd.read_csv('C:\\Users\\dkirksey\\Downloads\\Titanic\\train.csv')
test_data = pd.read_csv('C:\\Users\\dkirksey\\Downloads\\Titanic\\test.csv')
print(train_data.head(5))
print(train_data.describe())
print(train_data.info())

# sns.heatmap(train_data.drop('Survived',axis=1).corr())
# plt.show()

# sns.countplot(train_data['Survived'], hue=train_data['Sex'])
# plt.show()
#a larger percentage of women survived than men
sns.countplot(train_data['Embarked'], hue=train_data['Survived'])
plt.show() #passenger chance of survival: c>Q>S

train_data['FamilySize'] = train_data['SibSp'] + train_data['Parch'] +1
sns.countplot(train_data['FamilySize'], hue=train_data['Survived'])
plt.show()

sns.boxplot(train_data['Survived'],train_data['Fare'])
plt.show()



