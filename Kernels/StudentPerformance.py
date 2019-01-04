import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('C:\\Users\\dkirksey\\Downloads\\StudentsPerformance.csv')
sns.set_style('darkgrid')

print(data.head(5))
print (data.describe())
print(data.info())

scores = ['math score', 'reading score', 'writing score']
fig=plt.figure(figsize=(10,10))
ax = plt.axes()

i=1
for subject in scores:
	sns.distplot(data[data['gender'] =='male'][subject], ax=plt.subplot(int('13'+str(i))), kde=False)
	sns.distplot(data[data['gender'] =='female'][subject], ax=plt.subplot(int('13'+str(i))), color='red',kde=False)
	i+=1
plt.suptitle('Subject Scores by Gender', fontsize=16)
plt.show()

i=1
for subject in scores:
	sns.boxplot(x=data['gender'], y=data[subject], ax=plt.subplot(int('13'+str(i))))
	i+=1
	plt.suptitle('Student Scores by Gender')
plt.show()

def find_all_passes(row):
	if row['math score'] > 59 and row['reading score'] > 59 and row['writing score'] > 59:
		return True
	else:
		return False

data['PassAll'] = data.apply(lambda row: find_all_passes(row), axis=1)

sns.countplot(data['PassAll'],hue=data['gender'])
plt.title('Students Who Passed All Subjects ')
plt.show()
i=1
for subject in scores:
	sns.boxplot(x=data['race/ethnicity'], order=['group A', 'group B', 'group C', 'group D', 'group E'],y=data[subject], ax=plt.subplot(int('13'+str(i))))
	i+=1
plt.suptitle('Scores by Race/Ethnicity')
plt.show()
i=1

for subject in scores:
	plot=sns.boxplot(x=data['parental level of education'], y=data[subject], ax=plt.subplot(int('13'+str(i))))
	plt.xticks(rotation=45)
	i+=1
plt.suptitle('Scores by Parental Level of Education',fontsize=16)
plt.show()

i=1
for subject in scores:
	sns.boxplot(x=data['lunch'], y=data[subject], ax=plt.subplot(int('13'+str(i))))
	i+=1
plt.suptitle('Scores by Lunch Type', fontsize=16)
plt.show()

def get_grade(row):
	avg = (row['math score'] + row['reading score'] + row['writing score'])/3
	if avg >= 90:
		return 'A'
	elif 89 >= avg >= 80:
		return 'B'
	elif 79 >= avg >= 70:
		return 'C'
	elif 69>= avg >= 60:
		return 'D'
	else:
		return 'F'

data['grade'] = data.apply(lambda row : get_grade(row), axis=1)
data['average'] = (data['math score'] + data['writing score'] + data['reading score']) /3
print(data['grade'].value_counts())
print(data['average'].max())
sns.countplot(data['grade'],hue=data['parental level of education'], order=['A','B','C','D','F'])
plt.suptitle('Student Grades by Parental Level of Education', fontsize=16)
plt.show()

i=1
for subject in scores:
	sns.boxplot(x=data['test preparation course'], y=data[subject], ax=plt.subplot(int('13'+str(i))))
	i+=1
plt.suptitle('Student Scores by Test Prep Completion', fontsize=16)
plt.show()
