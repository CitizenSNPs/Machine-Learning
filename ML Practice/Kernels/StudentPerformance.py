import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('C:\\Users\\dkirksey\\Downloads\\StudentsPerformance.csv')

print(data.head(5))
print (data.describe())
print(data.info())

scores = ['math score', 'reading score', 'writing score']
# fig=plt.figure(figsize=(10,10))
# ax = plt.axes()
#
# i=1
# for subject in scores:
# 	sns.distplot(data[data['gender'] =='male'][subject], ax=plt.subplot(int('13'+str(i))), kde=False)
# 	sns.distplot(data[data['gender'] =='female'][subject], ax=plt.subplot(int('13'+str(i))), color='red',kde=False)
# 	i+=1
# plt.suptitle('Subject Scores by Gender')
# plt.show()
#
# i=1
# for subject in scores:
# 	sns.boxplot(x=data['gender'], y=data[subject], ax=plt.subplot(int('13'+str(i))))
# 	i+=1
# plt.show()

# def find_all_passes(row):
# 	if row['math score'] > 69 and row['reading score'] > 69 and row['writing score'] > 69:
# 		return True
# 	else:
# 		return False
#
# data['PassAll'] = data.apply(lambda row: find_all_passes(row), axis=1)
#
# sns.countplot(data['PassAll'],hue=data['gender'])
# plt.show()
# i=1
# for subject in scores:
# 	sns.boxplot(x=data['race/ethnicity'], y=data[subject], ax=plt.subplot(int('13'+str(i))))
# 	i+=1
# plt.show()
# i=1
# for subject in scores:
# 	sns.boxplot(x=data['parental level of education'], y=data[subject], ax=plt.subplot(int('13'+str(i))))
# 	i+=1
# plt.show()

# i=1
# for subject in scores:
# 	sns.boxplot(x=data['lunch'], y=data[subject], ax=plt.subplot(int('13'+str(i))))
# 	i+=1
# plt.show()

# def get_grade(row):
# 	avg = (row['math score'] + row['reading score'] + row['writing score'])/3
# 	if avg > 89.0:
# 		return 'A'
# 	elif 90.0 > avg > 79.0:
# 		return 'B'
# 	elif 80.0 > avg > 74.0:
# 		return 'C'
# 	elif 75.0 > avg > 69.0:
# 		return 'D'
# 	elif avg<70.0:
# 		return 'F'
# 	else:
# 		return False
#
# data['grade'] = data.apply(lambda row : get_grade(row), axis=1)
# data['average'] = (data['math score'] + data['writing score'] + data['reading score']) /3
# print(data['grade'].value_counts())
# print(data['average'].max())
# sns.countplot(data['grade'],hue=data['parental level of education'])
# plt.show()

