import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('C:\\Users\\dkirksey\\Downloads\\Ecommerce Customers.csv')

print(data.head(5))
print (data.describe())
print (data.info())

sns.jointplot(data = data, x='Time on App', y='Length of Membership', kind='hex')
plt.show()

sns.pairplot(data.drop(['Email', 'Address', 'Avatar'], axis=1))
plt.show()

sns.lmplot(data=data, x='Length of Membership', y='Yearly Amount Spent')
plt.show()

y = data['Yearly Amount Spent']
X = data[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]
lm = LinearRegression()
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=101)
lm.fit(X_train, y_train)

print(lm.intercept_)
print(lm.coef_)

y_pred = lm.predict(X_test)
sns.scatterplot(x=y_pred, y=y_test)
plt.show()

print(pd.DataFrame(data=lm.coef_, index=X.columns, columns=['Coefficients']))
