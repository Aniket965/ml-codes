import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot');
import numpy as np;
from sklearn.cluster import KMeans
X = np.array([[1,2],
            [1.5,1.8],
            [5,8],
            [8,8],
            [1,0.6],
            [9,11]]);
plt.scatter(X[:,0],X[:,1],s=150,linewidths=5);
plt.show()
colors=["g.","r.","c.","b.","k.","y."];
class K_Means:
    def __init__(self,k=2,tol=0.001,max_iter=300):
        self.k = k;
        self.tol =tol;
        self.max_iter = max_iter;
    def fit(self,data):
        self.centroids= {}
        for i in range(self.k):
            self.centroids[i]=data[i];

        for i in range(self.max_iter):
            self.classifications={}

            for i in range(self.k):
                self.classification[i] =[];
            
            for features in data:
                distances =[np.linalg.norm(features-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances));
                self.classifications[classification].append(features);
            prev_centroids = dict(self.centroids)
            for classification in self.classifications:
                self.centroids[classification]=np.average(self.classifications[classification],axis=0)
            optimized =True;
            for c in self.centroids:
                original_centroid = prev_centroids[c];
                current_centroid = self.centroids[c];
                if np.sum(((current_centroid-original_centroid)/original_centroid)*100)> self.tol:
                     optimized =False;
            if optimized:
                 break;   


    def predic(seltf,data):
       distances =[np.linalg.norm(data-self.centroids[centroid]) for centroid in self.centroids]
       classification = distances.index(min(distances));
       return classification;
clf = K_Means();
clf.fit(X);
for centroid in clf.centroids:
    plt.scatter(clf.centroids[centroid][0],clf.centroids[centroid][1],marker='o',color="k",s=150,linewidths=5);
print clf.classifications
for classfication in clf.classifications:
    color = colors[classfication]
    print color
    for features in clf.classifications[classification]:
        
        plt.scatter(features[0],features[1],marker="x",color=color,s=150,linewidths=5);
plt.show();