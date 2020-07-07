import pandas as pd
import numpy as np
malware=pd.read_csv("C:\\Users\\hp\\Desktop\\MalwareData.csv",sep="|")
df=malware[["md5","legitimate"]]

#preprocessing 
from sklearn.preprocessing import LabelEncoder
l=LabelEncoder()
df['md5']= l.fit_transform(df['md5']) 
df['md5'].unique() 
newdf=pd.DataFrame(columns=['md5'])
newdf.md5=['45917DCE4F43BD81BD4162BE50138921','81051BCC2CF1BEDF378224B0A93E2877']#here we want to convert the hash value into numeric value,so we use label encoder
newdf.md5=l.fit_transform(newdf['md5'])

all_data=pd.concat([df['md5'],newdf.md5])
all_data=l.fit_transform(all_data)
df['md5']=all_data[:len(df)]
newdf.md5=all_data[-len(newdf):]



x1=df.iloc[:,:1]
y=df['legitimate']

from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=1).fit(x1,y)
#Predicting new values
model.predict(newdf)