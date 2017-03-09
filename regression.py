import pandas as pd;
import quandl,math;
import numpy as np;
from sklearn import preprocessing,cross_validation,svm;
from sklearn.linear_model import LinearRegression;
# takes data from quandl of google stock prices
dataset = quandl.get("WIKI/GOOGL");
# head function works with top 5 
#print(dataset.head())
# take only valuable data from dataset remove reduntant data so that inv of matrix not become zero 
dataset = dataset[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']];
dataset['HL_PCT'] = (dataset['Adj. High'] - dataset['Adj. Low']) / dataset['Adj. Close'] * 100.0;
dataset['PCT_change'] = (dataset['Adj. Close'] - dataset['Adj. Open']) / dataset['Adj. Open'] * 100.0;
dataset = dataset[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
forecast_col = 'Adj. Close'
dataset.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(dataset)))
dataset['label'] = dataset[forecast_col].shift(-forecast_out)
dataset.dropna(inplace=True);
X = np.array(dataset.drop(['label'],1));
y = np.array(dataset['label']);
X= preprocessing.scale(X);
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2);
# clf = svm.SVR();
# clf.fit(X_train,y_train);
# confidence = clf.score(X_test,y_test);
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
print(confidence)





