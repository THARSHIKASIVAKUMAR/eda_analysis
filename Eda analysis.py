import pandas as pd
df = pd.read_csv("C:\Users\kanis\Downloads\archive\insurance.csv")
df.shape
df.describe()
df.shape
df.info()
df.describe().T
df.isnull().sum()
# Print the count of non-empty values for each feature
print('age: ' + str(df.age.count()))
print('sex: ' + str(df.sex.count()))
print('bmi: ' + str(df.bmi.count()))
print('children: ' + str(df.children.count()))
print('smoker: ' + str(df.smoker.count()))
print('region: ' + str(df.region.count()))
print('charges: ' + str(df.charges.count()))

print('\n')

# Print the number of unique values for each feature
print('age: ' + str(df.age.nunique()))
print('sex: ' + str(df.sex.nunique()))
print('bmi: ' + str(df.bmi.nunique()))
print('children: ' + str(df.children.nunique()))
print('smoker: ' + str(df.smoker.nunique()))
print('region: ' + str(df.region.nunique()))
print('charges: ' + str(df.charges.nunique()))

df.median()
df.mode()
df.head()

