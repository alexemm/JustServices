import sys

import cv2
import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D

class Picture():
    
    def __init__(self,file = None):
        if file is not None:
        #read image
            tmp_img = cv2.imread(file)
        
        self.height, self.width, self.channels = tmp_img.shape
        #convert to RGB
        self.img = cv2.cvtColor(tmp_img, cv2.COLOR_BGR2RGB)
        self.rgb = {}
        self.rgb['r'],self.rgb['g'],self.rgb['b'] = cv2.split(self.img)
        
    

        #plotting
    def plot(self):
        for key,value in self.rgb.items():
            self.rgb['plot_'+key] = value.flatten()
        fig = plt.figure();
        ax = Axes3D(fig);
        ax.scatter(self.rgb['plot_r'], self.rgb['plot_g'], self.rgb['plot_b']);
        plt.show();
        
class Clustering():
    
    def __init__(self, pic = None, n = 3):
        if pic is None:
            raise Error
        self.original = pic
        self.clusters = n
        
    def cluster(self):
        #list of pixels
        self.img = self.original.img.reshape((self.original.img.shape[0] * self.original.img.shape[1], 3))
        
        #kmeans
        model = KMeans(n_clusters = self.clusters)
        model.fit(self.img)
        
        self.dominant_colors = model.cluster_centers_.astype(int)
        self.labels = model.labels_
        self.new = []
        for i in model.predict(self.img):
            self.new.append(self.dominant_colors[i])
        self.new =  np.array(self.new).reshape(self.original.height,self.original.width,3)
        
        
        return self.new

    
    def plot(self):
        plt.imshow(self.new)
        plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
        plt.show()
     

n_clusters = 5
FILE = 'oh.jfif'
     

if len(sys.argv) > 1:
    print(sys.argv)
    if len(sys.argv) == 3:
        FILE = sys.argv[1]
        n_clusters = int(sys.argv[2])
    else:
        try:
            test = int(sys.argv[1])
            n_clusters = test
        except Exception:
            FILE = sys.argv[1]

        
print(n_clusters)    
test = Picture(FILE)
obj = Clustering(test, n = n_clusters)
obj.cluster()
obj.plot()
    #print(Clustering(test, n = 5).cluster())
    
