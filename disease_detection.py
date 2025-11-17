
from symptoms_list import symptoms
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.naive_bayes import GaussianNB,BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.multioutput import MultiOutputClassifier
import pandas as pd
import sys
import pickle
def prediction(selected_symptoms):

    try:
        symptomslist=symptoms()
        testingsymptoms = []
        # append zero in all coloumn fields...
        for x in range(0, len(symptomslist)):
            testingsymptoms.append(0)

        # update 1 where symptoms gets matched...
        for k in range(0, len(symptomslist)):
            for z in selected_symptoms:
                if z == symptomslist[k]:
                    testingsymptoms[k] = 1

        X_test = [testingsymptoms]
        print(X_test)

        model = open('..\Disease_Prediction\disease.model', 'rb')
        voting_clf = pickle.load(model)

        predicted=voting_clf.predict(X_test).tolist()


        print("res2=", voting_clf.predict(X_test).tolist())



        predicted_disease=predicted[0][0]

        #Specializations list

        Rheumatologist = ['Osteoarthristis', 'Arthritis']

        Cardiologist = ['Heart attack', 'Bronchial Asthma', 'Hypertension ']

        ENT_specialist = ['(vertigo) Paroymsal  Positional Vertigo', 'Hypothyroidism']


        Neurologist = ['Varicose veins', 'Paralysis (brain hemorrhage)', 'Migraine', 'Cervical spondylosis']

        Allergist_Immunologist = ['Allergy', 'Pneumonia','AIDS', 'Common Cold', 'Tuberculosis', 'Malaria', 'Dengue', 'Typhoid']

        Urologist = ['Urinary tract infection',
                     'Dimorphic hemmorhoids(piles)']

        Dermatologist = ['Acne', 'Chicken pox', 'Fungal infection', 'Psoriasis', 'Impetigo']

        Gastroenterologist = ['Peptic ulcer diseae', 'GERD', 'Chronic cholestasis', 'Drug Reaction', 'Gastroenteritis',
                              'Hepatitis E',
                              'Alcoholic hepatitis', 'Jaundice', 'hepatitis A',
                              'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Diabetes ', 'Hypoglycemia']


        if predicted_disease in Rheumatologist:
            consultdoctor = "Rheumatologist"

        elif predicted_disease in Cardiologist:
            consultdoctor = "Cardiologist"

        elif predicted_disease in ENT_specialist:
            consultdoctor = "ENT specialist"

        elif predicted_disease in Neurologist:
            consultdoctor = "Neurologist"

        elif predicted_disease in Allergist_Immunologist:
            consultdoctor = "Allergy"

        elif predicted_disease in Urologist:
            consultdoctor = "Urologist"

        elif predicted_disease in Dermatologist:
            consultdoctor = "Dermatologist"

        elif predicted_disease in Gastroenterologist:
            consultdoctor = "Gastroenterologist"
        else:
            consultdoctor = "other"



        return consultdoctor,predicted

    except Exception as e:
        print(e)
        tb = sys.exc_info()[2]
        print(tb.tb_lineno)


'''selected_symptoms=["chest_pain","fast_heart_rate"]

print(prediction(selected_symptoms))'''







    






