#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:57:42 2019

@author: pkostakos #Draft
"""

import urllib.request
import pandas as pd 
url = 'http://apps.start.umd.edu/gtd/downloads/dataset/globalterrorismdb_0718dist.xlsx'
urllib.request.urlretrieve(url, "terror.xlsx")
df = pd.read_excel("data2.xlsx")
df.to_csv("./data.csv", sep=",")


#Create a two way table #Country.name, #Success


ratio = pd.crosstab(df.country_txt, df.success)

X = ratio.iloc[:, [0,1]].values

#Find out the optimal number of clasters using the elbow method
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

wcss= []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 900, n_init = 100, random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11), wcss)
plt.title("Using the Elbow method")
plt.xlabel("NUmber of clusters")
plt.ylabel("WCSS")
plt.show()
    

#Apply kmeans to the Ratio dataset. 

kmeans= KMeans(n_clusters = 5, init = 'k-means++', max_iter = 350, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(X)

#Viz the clusters

plt.scatter(X[y_kmeans== 0, 0], X[y_kmeans== 0, 1], s =100, c= 'red', label = "Cluster1")
plt.scatter(X[y_kmeans== 1, 0], X[y_kmeans== 1, 1], s = 100, c= 'blue', label = "Cluster2")
plt.scatter(X[y_kmeans== 2, 0], X[y_kmeans== 2, 1], s = 100, c= 'pink', label = "Cluster3")
plt.scatter(X[y_kmeans== 3, 0], X[y_kmeans== 3, 1], s = 100, c= 'cyan', label = "Cluster4")


plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:, 1], s=10, c = 'yellow', label = 'Centroids')
plt.title ('Cluster of Countries responding to terrorist events')
plt.xlabel('Attacks that have been successful')
plt.ylabel("Attacks that have been unsuccessful")
plt.legend()
plt.show()
