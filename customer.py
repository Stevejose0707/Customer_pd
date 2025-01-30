import pandas as pd
df=pd.read_csv("C:/Users/Steve Jose/Desktop/customer1.txt",sep=',',header=None)
df.columns=['id','fname','lname','age','prof','loc']
print(df)
print("*"*100)
# # print(df.head(50))
# # print("*"*100)
# #
# # df2=df[['id','fname','lname','age','prof','loc']].tail(30)
# # print(df2)
# # print("*"*100)
# # df1=df[['fname','lname','age','loc']]
# # print(df1[9:49])
# x=df.iloc[:,:-1]
# print(x)
# y=df.iloc[:,-1]
# print(y)
# #total number of missing value
# print(df.isna().sum())
# #fill na ---used to fill missing value
#1
df1=df.fillna('india')
print(df1.isna().sum())
print('*'*100)
#2. fname,lname,age,prof,loc
df2=df1.loc[df1['loc']=='india'] [['fname','lname','age','prof','loc']]
print(df2)
print('*'*100)
#Age mxm 5 emp fname, lname, age, prof
df3=df1.sort_values(by='age',ascending=False) [['fname','lname','age','prof']].head(5)
print(df3)
print('*'*100)
#Age minimum 3 emp fname,lname,age,prof
df4=df1.sort_values(by='age') [['fname','lname','age','prof']].head(3)
print(df4)
print('*'*100)
#5. Age above 50 fname,lname,age
df5=df1.loc[df1['age']>50] [['fname','lname','age',]]
print(df5)
print('*'*100)
df6=df1.loc[df1['age']<30] [['fname','lname','age','prof']]
print(df6)
print('*'*100)
#7. india work fname,lname,age,prof
df7=df1.loc[df1['loc']=='india'] [['fname','lname','age','prof']]
print(df7)
print('*'*100)
#8. india work and age above 50 fname,lname,age
df8=df1.loc[(df1['age']>50)&(df1['loc']=='india')] [['fname','lname','age']]
print(df8)
print('*'*100)
#9. uk work fname,lname,age,prof
df9=df1.loc[df1['loc']=='uk'] [['fname','lname','age','prof']]
print(df9)
print('*'*100)
#india work and prof Doctor fname,lname,age
df10=df1.loc[(df1['loc']=='india')&(df1['prof']=='Doctor')] [['fname','lname','age']]
print(df10)
print('*'*100)
#11. india work, age mxm 3 employee fname,lname,age
df11=df1.loc[df1['loc']=='india'].sort_values(by='age',ascending=False)[['fname','lname','age']].head(3)
print(df11)
print('*'*100)
#12. india wok ,age min 2 emp fname,lname,ag
df12=df1.loc[df1['loc']=='india'].sort_values(by='age',ascending=False)[['fname','lname','age']].tail(2)
print(df12)
print('*'*100)
#13. Pilot prof, age mxm 1 emp fname,lname,age,location
df13=df1.loc[df1['prof']=='pilot'].sort_values(by='age',ascending=False)[['fname','lname','age']].head(1)
print(df13)
print('*'*100)
#14. Pilot prof, age minim 3 emp fname,lname,age
df14=df1.loc[df1['prof']=='pilot'].sort_values(by='age',ascending=True)[['fname','lname','age']].head(3)
print(df14)
print('*'*100)
#15. uk work ,age minum 10 emp fname,lname,prof
df15=df1.loc[df1['loc']=='uk'].sort_values(by='age',ascending=True) [['fname','lname','prof']].head(10)
print(df15)
print('*'*100)
df16=df1.groupby('prof') ['prof'].count()
print(df16)
print('*'*100)
df17=df1.loc[df1['loc']=='india'].groupby('prof') ['prof'].count().sort_values(ascending=False)
print(df17)
print('*'*100)
df18=df1.loc[(df1['loc']=='india')&(df1['age']>50)].groupby('prof') ['prof'].count().sort_values(ascending=False)
print(df18)
print('*'*100)
df19=df.groupby('prof') ['age'].max().sort_values(ascending=False)
print(df19)
print('*'*100)
df20=df.groupby('prof') ['age'].min().sort_values(ascending=False)
print(df20)
print('*'*100)
df21=df.groupby('prof') ['age'].mean().sort_values(ascending=False)
print(df21)






