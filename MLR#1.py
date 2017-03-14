from sklearn import tree;
features = [[100,0,1],[90,0,1],[140,1,0],[150,1,0]];
labels    = [0,0,1,1];
clf = tree.DecisionTreeClassifier();
clf = clf.fit(features,labels);
print clf.predict([95,0,1]);




