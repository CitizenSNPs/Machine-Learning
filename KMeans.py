import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from mpl_toolkits import mplot3d

college_data = pd.read_csv('C:\\Users\\dkirksey\\Downloads\College_Data.csv')

print(college_data.head(5))
print(college_data.info())
print(college_data.describe())

college_data=college_data.set_index('Unnamed: 0')
#Cazenovia college has a grad rate >100%
college_data.loc['Cazenovia College']['Grad.Rate'] = 100


sns.scatterplot(x=college_data['Grad.Rate'], y=college_data['Room.Board'], hue = college_data['Private'])
plt.show()

sns.scatterplot(x=college_data['F.Undergrad'], y=college_data['Outstate'], hue = college_data['Private'])
plt.show()

fig = plt.figure(figsize=(20,20))
ax = plt.axes(projection='3d')

ax.scatter(college_data['F.Undergrad'], college_data.Outstate, college_data['Grad.Rate'])
plt.xlabel('F.Undergrad')
plt.ylabel('Outstate')
plt.show()

km = KMeans(n_clusters=2)
km.fit(college_data.drop('Private', axis=1))
print (km.cluster_centers_)
print(km.labels_)
print(km.labels_)
