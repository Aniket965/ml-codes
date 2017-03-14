from sklearn.datasets import load_iris
from sklearn import cross_validation;
from sklearn import tree;
import numpy as np
iris = load_iris();
# print iris.feature_names;
# print iris.target_names;
# print iris.data;
X_train,X_test,y_train,y_test = cross_validation.train_test_split(iris.data,iris.target,test_size=0.2);
clf = tree.DecisionTreeClassifier();
clf.fit(X_train,y_train);

print y_test;
print clf.predict(X_test);

