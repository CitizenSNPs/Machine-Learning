import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

knn_data = pd.read_csv('C:\\Users\\dkirksey\\Downloads\\KNN_Project_Data.csv')

print(knn_data.head(10))

sns.pairplot(knn_data, hue='TARGET CLASS', diag_kind='hist',palette='Pastel1')
plt.show()

scaler = StandardScaler()
scaler.fit(knn_data.drop('TARGET CLASS', axis=1))
model=scaler.transform(knn_data.drop('TARGET CLASS', axis=1))

scaled_df = pd.DataFrame(data=model, columns=knn_data.columns[:-1])
print(scaled_df.head())

X_train, X_test, y_train, y_test = train_test_split(scaled_df,knn_data['TARGET CLASS'],test_size=0.3)
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

#Choosing K
error_rate = []

for i in range(1,40):
	knn = KNeighborsClassifier(n_neighbors=i)
	knn.fit(X_train, y_train)
	pred_i = knn.predict(X_test)
	error_rate.append(np.mean(pred_i != y_test))
	print(pred_i)
print(error_rate)

plt.figure(figsize=(20,20))
plt.plot(range(1,40), error_rate, marker='o')
plt.show()
#minimum ~=30 or 40

knn = KNeighborsClassifier(n_neighbors=30)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))






