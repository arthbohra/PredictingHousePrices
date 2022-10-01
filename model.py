import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np 
data = pd.read_csv('house_data.csv')
X = data[['status', 'longitude', 'latitude', 'house_type', 'beds', 'baths', 'sqft', 'lot_sqft', 'full_baths', 'price_reduced', 'new_construction',  'new_listing', 'price_reduced_amount', 'days_since_last_sold', 'days_since_list_date', 'last_sold_prices']]
y = data['list_prices']
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.20, random_state=22)

#Trained the following models to determine which was the most accurate to our dataset
#Decided on a Random Forest Classifier as it resulted in the best accuracy score
models = [linear_model.LinearRegression()]
for model in models:
    fit = model.fit(X_train, y_train)
    y_pred = fit.predict(X_test)
    score=r2_score(y_test,y_pred)
    print('r2 socre is ',score)
    # model evaluation
    mean_squared_errors = mean_squared_error(y_test, y_pred) / y_test
    mean_absolute_errors = mean_absolute_error(y_test, y_pred) / y_test

print (np.mean(mean_absolute_errors))
