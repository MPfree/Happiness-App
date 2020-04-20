from sklearn import svm
from sklearn.metrics import accuracy_score
import MySQLdb
import pandas as pd
import numpy as np
import math

def perform_logistic_regression(conn):
    data = pd.read_sql("SELECT * FROM TomData", conn)
    names = data.columns
    numColumns = len(names)
    
    x_data = data.iloc[:, 1: (numColumns-1)]
    x_data = x_data.to_numpy()
    y_data = (data.iloc[:, numColumns-1]).tolist()
    y_data = np.array(y_data)
    print(y_data)

    m = len(y_data)
    test_size = math.floor(m*0.2)
    training_size = m - test_size

    X_train = x_data[0:training_size, :]
    X_test = x_data[training_size:m, :]
    y_train = y_data[0:training_size]
    y_test = y_data[training_size:m]

    print(X_test, y_test)

    model = svm.SVC(kernel= 'linear')
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print(accuracy_score(y_test, y_pred))

    print(y_pred == y_test)

    params = model.coef_

    print(params)

    return params
    




