# -*- coding: utf-8 -*-
"""Homework 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lE5bgtlDpBxZbrS77lBpgEEhO4TeFpVy

###Homework 3: solve your problem with KNN algorithm and compare the outcomes of decision tree and KNN, comment about the success rates.
"""

import pandas as pd

"""##2. Join both files into a single data frame."""

df1 = pd. read_excel("dataframe1.xlsx")
df2= pd. read_excel("dataframe2.xlsx")

df_joined = df1.merge(df2, left_on ='Student ID', 
                       right_on = 'Student ID',
                       how = 'right')

"""### I used entropy in here. There is not a huge difference between Gini and Entropy. Entropy tends to produce a more balanced tree, while Gini tends to decompose the class with higher frequency."""

from sklearn.tree import DecisionTreeClassifier
dtc = DecisionTreeClassifier(criterion='entropy', max_depth = 2)

X = df_joined[['Midterm','Final','Project Grades']]
y = df_joined['Gender']

dtc.fit(X,y)
ypred = dtc.predict(X)

print(ypred)

"""###Desicion Tree;"""

from sklearn import tree
tree.plot_tree(dtc)

"""## I used p=2 for euclidian distance"""

from sklearn.neighbors import KNeighborsClassifier
knn= KNeighborsClassifier(n_neighbors = 3, p = 2)
knn.fit(X,y)
ypred2 = knn.predict(X)

print(ypred2)

"""### So in my codes, I tried to predict the gender of the students based on the data of the students' midterm, final and project grades. At first, I was trying to estimate the project based on the midterm and final grades, but I thought that there might be big changes in the estimates because the number of data is large. I also added a gender option to my first data frame in order to see the prediction made by the program more easily. When we look at the actual data, we see that the data goes as;

 ### ['f' 'm' 'm' 'f' 'm' 'm' 'f' 'f' 'm' 'f' 'f' 'm' 'm' 'm' 'm' 'f' 'm' 'f' 'f' 'm']. But programs prediction is 
 
 ### ['f' 'm' 'm' 'f' 'm' 'm' 'f' 'f' 'm' 'f' 'f' 'm' 'm' 'm' 'm' 'm' 'm' 'm' 'f' 'f'].

##Actually it is quite close.
"""