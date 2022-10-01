import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np 
from sklearn import linear_model
import os

data = pd.read_csv('house_data.csv')
X = data[['status', 'longitude', 'latitude', 'house_type', 'beds', 'baths', 'sqft', 'lot_sqft', 'full_baths', 'price_reduced', 'new_construction',  'new_listing', 'price_reduced_amount', 'days_since_last_sold', 'days_since_list_date', 'last_sold_prices']]
y = data['list_prices']
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.12, random_state=31)
model = linear_model.LinearRegression().fit(X_train, y_train)
fit = model.fit(X_train, y_train)

check = True;
while(check) :
    x = []
    
    x.append(float(input("Enter if your house is on sale. (1 = Yes, 0 = No)\n")))
    x.append(float(input("Enter your house longitude\n")))
    x.append(float(input("Enter your house latitude\n")))
    x.append(float(input("Enter your house type. (0 = other, 1 = single_family, 2 = townhomes, 3 = condos)\n")))
    x.append(float(input("Enter the number of beds\n")))
    x.append(float(input("Enter the number of bathrooms\n")))
    x.append(float(input("Enter your house square feet\n")))
    x.append(float(input("Enter your house lot size\n")))
    x.append(float(input("Enter the number of full bathrooms\n")))
    x.append(float(input("Enter if your house has had the price reduced. (0 = No, 1 = Yes)\n")))
    x.append(float(input("Enter if your house is a new construction. (0 = No, 1 = Yes)\n")))
    x.append(float(input("Enter if your house is a new listing. (0 = No, 1 = Yes)\n")))
    x.append(float(input("Enter the amount your house price has been reduced by.\n")))
    x.append(float(input("Enter the number of days since the house was last sold.\n")))
    x.append(float(input("Enter the number of days since the house was listed.\n")))
    x.append(float(input("Enter the last sold price of your price.\n")))
    
    print("\n")
    print("\n")
    print("\n")
    
    print("Calculating result...\n")
    x = np.reshape(x, (1, -1))
    prediction = model.predict(x)
    os.system('clear')
    print('\n')
    print('\n')
    print("We are able to predict that the price of your house will be within plus or minus 7.89%"+ " of "+ '$'+str(round(prediction[0], 2))+"( "+str(round(prediction[0], 2)-round(prediction[0], 2)*.0789)+" - "+str(round(prediction[0], 2)+.0789*round(prediction[0], 2))+" )")
    print('\n')
    y = (int(input("Would you like to run the program again? (0 = Yes, 1 = No)\n")))
    os.system('clear')
    if y==1:
        check=False
