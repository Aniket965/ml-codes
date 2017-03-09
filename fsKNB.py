#from scracth K NB
import numpy as np
from math import sqrt
import warnings;
import matplotlib.pyplot as plt;
from matplotlib import style;
from collections import Counter;
style.use('fivethirtyeight');
dataset={'k':[[1,2],[2,3],[3,1]],'r':[[6,5],[7,7],[8,6]]};
# [[plt.scatter(j[0],j[1],s=100,color=i) for j in dataset[i]] for i in dataset];

# plt.show();
def k_nearest_neighbor(data,predict,k=3):
    if len(data)>=k:
        warnings.warn('badass');
    distances= []
    for group in data:
        for features in data[group]:
            euclidean_distance= np.linalg.norm(np.array(features)-np.array(predict));
            distances.append([[euclidean_distance],group])
    votes =[ i[1]  for i in sorted(distances)[:k] ];
    print(Counter(votes).most_common(1))
    vote_Result = Counter(votes).most_common(1)[0][0];
    return vote_Result;
result = k_nearest_neighbor(dataset,[5,7],k=3);
print(result);