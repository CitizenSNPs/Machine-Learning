import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('C:\\Users\\dkirksey\\Downloads\\BlackFriday.csv')
data = data.loc[:10000, :]
sns.set_style('darkgrid')
sns.set_palette('Pastel1')
print(data.head(5))
print(data.info())
print(data.describe())
data = data.drop('Product_Category_2', axis=1)
num_features = ['Stay in Current Years', 'Purchase']
cat_features = ['Age','Gender', 'Occupation', 'City_Category', 'Marital_Status', 'Product_Category_1', 'Product_Category_2',
				'Product_Category_3']
#
# sns.pairplot(data.drop(['Product_Category_2', 'Product_Category_3','User_ID','Product_ID'], axis=1), hue='Gender')
# plt.show()

# sns.countplot(data['Age'])
# plt.show()
#
# sns.boxplot(data['Age'], data['Purchase'], ax=plt.subplot(131))
# sns.boxplot(data['Gender'], data['Purchase'],ax=plt.subplot(132))
# sns.boxplot(data['Marital_Status'], data['Purchase'],ax=plt.subplot(133))
# plt.show()
#
# sns.boxplot(data['Occupation'],data['Purchase'])
# plt.show()
fig=plt.figure(figsize=(20,20))
ax = fig.add_axes()
sns.jointplot(x=data['Product_Category_1'], y=data['Purchase'], kind='hex',ax=plt.subplot(131))
plt.show()

sns.jointplot(x=data['Product_Category_2'].dropna(), y=data['Purchase'], kind='hex',ax=plt.subplot(132))
plt.show()

sns.jointplot(x=data['Product_Category_3'].dropna(), y=data['Purchase'], kind='hex',ax=plt.subplot(133))
plt.show()