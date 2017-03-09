# k nearest neighbours
# k = odd number(constant number)
# for (2n+1) we need atleast 2n+2 where n = natural number
# euclidian distance for measuring distance
#  directly proportional to dataset size

import numpy as np;
from sklearn import preprocessing,cross_validation,neighbors;
import pandas as pd;
df=pd.read_csv('breast-cancer-wisconsin.data');
df.replace('?',-99999,inplace=True);
print(df);
#droping the useless coloumns
df.drop(['id'],1,inplace=True);
X= np.array(df.drop(['class'],1));
y= np.array(df['class']);
# splits the data for training and testing
X_train,X_test,y_train,y_test = cross_validation.train_test_split(X,y,test_size=0.2);
clf= neighbors.KNeighborsClassifier();
clf.fit(X_train,y_train);
accuracy = clf.score(X_test,y_test);
print(accuracy);

#prediction

example= np.array([4,2,1,1,1,2,3,2,1]);
# for reshaping the array 
example = example.reshape(len(example),-1);
prediction = clf.predict(example);
print(prediction);
# prediction 97.80%

