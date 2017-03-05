#apple example
# from sklearn import tree 
# features = [[140, 1],[130, 1],[150, 0],[170, 0]]
# labels = [0,0,1,1]
# clf = tree.DecisionTreeClassifier()
# clf = clf.fit(features, labels)
# print clf.predict([[120, 1]]) 

#iris example
import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris
iris = load_iris()
# print iris.feature_names
# print iris.target_names
# print iris.data[0]
# print iris.target[0]
test_idx=[0, 50, 100]

# training
train_target=np.delete(iris.target, test_idx)
train_data=np.delete(iris.data, test_idx, axis=0)

#test
test_target=iris.target[test_idx]
test_data=iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data, train_target)

print test_target
print clf.predict(test_data)

from IPython.display import Image  
dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = pydotplus.graph_from_dot_data(dot_data)  
Image(graph.create_png())  




