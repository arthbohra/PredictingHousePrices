import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, ConfusionMatrixDisplay
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.linear_model import LogisticRegression
import math
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

data = pd.read_csv('house_data.csv')
X = data[['status', 'longitude', 'latitude', 'house_type', 'beds', 'baths', 'sqft', 'lot_sqft', 'full_baths', 'price_reduced', 'new_construction',  'new_listing', 'price_reduced_amount', 'days_since_last_sold', 'days_since_list_date', 'last_sold_prices']]
y = data['list_prices']
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.15, random_state=49)

#Trained the following models to determine which was the most accurate to our dataset
#Decided on a Random Forest Classifier as it resulted in the best accuracy score
models = [DecisionTreeClassifier(),LogisticRegression(), KNeighborsClassifier(), GaussianNB(), RandomForestClassifier()]
for model in models:
    average = 0.0
    for i in range(100):
        fit = model.fit(X_train, y_train)
        y_pred = fit.predict(X_test)
        confusionMatrix = confusion_matrix(y_test, y_pred, labels=fit.classes_)
        average = average + float(accuracy_score(y_test, y_pred))
    print(str(model) + ' Average Accuracy Score: ' + str(average/100))
    display = ConfusionMatrixDisplay(confusion_matrix=confusionMatrix, display_labels=fit.classes_)
    display.plot()
    plt.show()
    print(str(model) + ' f1 Score: ' + str(f1_score(y_test, y_pred, average=None, zero_division=0)) + '\n')