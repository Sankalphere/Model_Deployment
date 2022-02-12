import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

def heart_pred(df):

    dt = pd.read_csv('heartdisease.csv')

    X = dt.drop(columns = 'target' , axis =1)
    Y = dt['target']


    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X)


    classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski' , p=2)
    classifier.fit(X_train, Y)

    return(classifier.predict(df).astype(int))