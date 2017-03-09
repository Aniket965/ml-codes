from statistics import mean
import numpy as np
import matplotlib.pylab as plt
from matplotlib import style;
xs =np.array([1,2,3,4,5,6],dtype=np.float64);
ys=np.array([5,4,6,5,6,7],dtype=np.float64);
style.use('fivethirtyeight');
# plt.scatter(xs,ys);
# plt.show()
def bestfit(xs,ys):
    m=(((mean(xs)*mean(ys))-mean(xs*ys))/ 
     ((mean(xs)*mean(xs))-mean(xs*xs)));
    return m
m = bestfit(xs,ys);
print(m);
def yintercept(xs,ys,m):
     c=mean(ys)-(m*mean(xs));
     return c;
c= yintercept(xs,ys,m);
print(c)
predic_x= 8;
predict_y=(m*predic_x)+c;
print(predict_y)
rl = [[m*x]+c for x in xs];
plt.scatter(xs,ys)
plt.plot(xs,rl);
plt.show();