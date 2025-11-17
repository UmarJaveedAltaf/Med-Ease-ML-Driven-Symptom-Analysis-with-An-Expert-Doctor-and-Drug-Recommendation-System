
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.naive_bayes import GaussianNB,BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
import numpy as np
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import f1_score, precision_score, accuracy_score, recall_score,confusion_matrix
import pandas as pd

import pickle

def train_ml():

    try:
        
       

        rfc_clf = RandomForestClassifier()
        dt_clf = DecisionTreeClassifier()
        nb_clf = BernoulliNB()

        voting_clf = VotingClassifier(estimators=[('RF', rfc_clf), ('dt', dt_clf), ('nb', nb_clf)], voting='hard')




        data = pd.read_csv("../Disease_Prediction/dataset/trainingset.csv")
    
        y = data[['prognosis','drug','alter_drug']]

        del data['prognosis']
        del data['drug']
        del data['alter_drug']
        X=data    

    
        mul_clf = MultiOutputClassifier(voting_clf)

        mul_clf.fit(X, y)

       

        with open('disease.model', 'wb') as f:
            pickle.dump(mul_clf, f)

        print("Training Completed..!")



    except Exception as e:
        print(e)

    


train_ml()



