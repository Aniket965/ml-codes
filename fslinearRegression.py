from statistics import mean
import numpy as np
import matplotlib.pylab as plt
import random
from matplotlib import style;
xs =np.array([1,2,3,4,5,6],dtype=np.float64);
ys=np.array([5,4,6,5,6,7],dtype=np.float64);
style.use('fivethirtyeight');
# plt.scatter(xs,ys);
# plt.show()
# def create_dataset(hm,variance,step=2,correlation=False):
#     val=1;
#     ys=[];
#     for i in range(hm):
#         y=val+random.randrange(-variance,variance);
#         ys.append(y);
#         if correlation and correlation=='pos'






    # return np.array(xs,dtype=np.float64),np.array(ys,dtype=np.float64)

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
def squared_error(ys_orig,ys_line):
    return sum((ys_line-ys_orig)**2);



def coefficient_of_determination(ys_orign,ys_line):
    y_mean_line = [mean(ys_orign) for y in ys_orign];
    squared_error_regr= squared_error(ys_orign,ys_line);
    squared_error_y_mean= squared_error(ys_orign,y_mean_line);
    return (1 - (squared_error_regr/squared_error_y_mean));
rl = [[m*x]+c for x in xs];
rsquare =coefficient_of_determination(ys,rl);
predic_x= 8;
predict_y=(m*predic_x)+c;
plt.scatter(xs,ys);
plt.plot(xs,rl);
plt.show();

# for one feature only build from complete scratch