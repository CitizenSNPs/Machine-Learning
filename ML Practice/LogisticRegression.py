import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
sns.set_style('darkgrid')
ad_data = pd.read_csv('C:\\Users\\dkirksey\\Downloads\\advertising.csv')
print(ad_data.head(10))
ad_data.info()
ad_data.describe()
print(ad_data.columns)
#
# sns.distplot(ad_data['Age'])
# plt.show()

# sns.jointplot(data=ad_data, x='Daily Time Spent on Site', y='Age', kind='hex')
# plt.show()
#
# sns.pairplot(ad_data.drop(['Ad Topic Line','City','Country'],axis=1),hue='Clicked on Ad',diag_kind='hist')
# #diag_kind = hist to avoid singular matrix error
# plt.show()
logreg = LogisticRegression()
X=ad_data[['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Male']]
y=ad_data['Clicked on Ad']

X_train, X_test,y_train,y_test = train_test_split(X,y,test_size=0.33)

logreg.fit(X_train, y_train)
print (pd.DataFrame(data=logreg.coef_, columns=['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage', 'Male']
, index=['Coefficients']))

y_pred = logreg.predict(X_test)
print (confusion_matrix(y_test, y_pred))
