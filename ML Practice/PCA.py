import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('C:\\Users\\dkirksey\\Downloads\College_Data.csv')
print (data.head(5))
print (data.info())
print (data.describe())

X = data.drop(['Unnamed: 0', 'Private'], axis=1)
X_columns = X.columns
scaler = StandardScaler()
scaled_data = scaler.fit(X)
scaled_data=scaled_data.transform(X)
print (scaled_data)
print(X_columns)

scaled = pd.DataFrame(data=scaled_data,columns=X.columns)

sns.heatmap(data=scaled, cmap='plasma')
plt.show()

from sklearn.decomposition import PCA
pca = PCA(n_components=3)
pca.fit(scaled)
X_pca = pca.transform(scaled)

sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1], hue=data['Private'])
plt.show()

df_comp = pd.DataFrame(pca.components_, columns=X.columns)
sns.heatmap(df_comp, cmap='plasma')
plt.show()


