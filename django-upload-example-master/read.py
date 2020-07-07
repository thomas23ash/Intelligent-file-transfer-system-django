import pandas as pd
data = pd.read_csv('url',sep='|')
x=data.loc[data['md5']=="93RltTeyNXmvTKYgscaLEG5AGYZkRhVqLhQTYUY1"]
print(x)
r=