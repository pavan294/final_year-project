import pickle
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
df=pd.read_csv('whisky.csv')
df.head()
import seaborn as sns
corm=df.corr()
sns.heatmap(corm)
from sklearn.cluster import KMeans
SS = []
NC = range(1,20)
for k in NC:
    km = KMeans(n_clusters=k)
    km = km.fit(df.iloc[:,2:14])
    SS.append(km.inertia_)
plt.plot(NC,SS)
plt.xlabel('k')
plt.ylabel('SS')
plt.show()
from sklearn.cluster.bicluster import SpectralCoclustering
flavour=df.iloc[:,2:14] 
corr_whisky=pd.DataFrame.corr(flavour.transpose())
print(corr_whisky)
plt.figure(figsize=(8,8))
plt.pcolor(corr_whisky)
import pandas as pd
plt.colorbar()
model=SpectralCoclustering(n_clusters=5,random_state=45)
x=df["Distillery"]
df["disteliries_group"]=pd.Series(x,index=df.index)

cluster=list(zip(df.iloc[:,1],df.iloc[:,13]))

cluster=sorted(cluster, key=lambda x: x[1])

print("the resultant grouped classified whiskey based on their flavour")
print("\n")

c=pd.DataFrame(cluster)
print(c)
model1=pickle.dump(cluster,open('model1.pkl','wb'))

       
