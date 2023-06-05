# KNN example
"""
# i/p data should be numeric
# i/p data can be numeric or string

# package name : sklearn
# module name : neighbors
# function name :KNeighborsClassifier

"""
from sklearn.neighbors import KNeighborsClassifier
x1=[7,7,3,1]
y1=[7,4,4,4]
target=["BAD","BAD","GOOD","GOOD"]
features=list(zip(x1,y1))
print(features)
# create an object of  KNeighborsClassifier is knn
knn=KNeighborsClassifier(n_neighbors=3)
# model creation
knn.fit(features,target)
# model predict
print(knn.predict([[3,7]]))
