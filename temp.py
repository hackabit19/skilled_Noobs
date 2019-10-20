import os
from flask import Flask,jsonify,request,render_template
from config import Config
app=Flask(__name__,static_url_path='',static_folder='static/dashboard')

APP_ROOT=os.path.dirname(os.path.abspath(__file__))
import time
# import sys
# sys.path.append('/home/agni/Downloads/facets-master/facets_overview/python')
import pandas as pd

# template_dir = os.path.abspath('./templates/examples')

# from generalized import *

@app.route("/",methods=["POST","GET"])
def index():
    # file=request.files["file"]
    # print(file)
    # nation=os.path.join(target,file.filename)
    # print(destination)
    # d = nation
    return render_template("examples/dashboard.html")

@app.route("/t",methods=["POST","GET"])
def index1():
    target=os.path.join(APP_ROOT,"/home/aayushi/ml-simu")
    # print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    file=request.files["file"]
    # print(file)
    destination1=os.path.join(target,file.filename)
    print(destination1)

    #!/usr/bin/env python
    # coding: utf-8
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    # from app import *


    # location = input('Enter data location: ')
    data = pd.read_csv(destination1)

    type(data['LoanAmount'][0])


    #extract numerical data columns
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    newdf = data.select_dtypes(include=numerics)


    #FIll missing values
    for i in data.columns:
        data[i].fillna(data[i].mode()[0], inplace=True)



    #One hot encoding
    from sklearn.preprocessing import LabelEncoder,OneHotEncoder
    labelencoder = LabelEncoder()
    for i in data.columns:
        if(isinstance(data[i][0],str)):
            data[i] = labelencoder.fit_transform(data[i])




    X = data.iloc[:,1:-1].values
    y = data.iloc[:, -1].values



    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)


    #


    from sklearn import model_selection
    from sklearn.linear_model import LogisticRegression
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    from sklearn.linear_model import LinearRegression
    from sklearn.cluster import AgglomerativeClustering
    from sklearn.ensemble import RandomForestRegressor


    #


    models = []
    models.append(('LR', LogisticRegression()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC()))
    models.append(('LiR',LinearRegression()))
    models.append(('RF',RandomForestRegressor()))


    #


    results = []
    names = []
    seed = 7
    dict = {}
    scoring = 'accuracy'
    for name, model in models:
        kfold = model_selection.KFold(n_splits=20, random_state=seed)
        cv_results = model_selection.cross_val_score(model, X, y, cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        dict[name]=cv_results.mean()
        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
        print(dict[name])
    time.sleep(3)

    return render_template("examples/dashboard.html",link=destination1,msg=msg,knn=dict['KNN']
                            ,nb=dict['NB'],svm=dict['SVM'],lr=dict['LR'],cart=dict['CART'],lir=dict['LiR'],rf=dict['RF'])



@app.route("/Upload",methods=["POST",'GET'])
def Upload():
    target=os.path.join(APP_ROOT,"/home/aayushi/ml-simu")
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    file=request.files["file"]
    print(file)
    nation=os.path.join(target,file.filename)
    print(nation)
    file.save(nation)
    data = pd.read_csv(nation)
    return render_template("upload.html",data=protostr1)

@app.route("/tables",methods=["POST",'GET'])
def tables():
    return render_template("examples/tables.html")

@app.route("/tables1",methods=['POST','GET'])
def tables1():
    target=os.path.join(APP_ROOT,"/home/aayushi/ml-simu")
    # print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    file=request.files["file"]
    # print(file)
    destination=os.path.join(target,file.filename)
    print(destination)
    # d = destination
    file.save(destination)
    data = pd.read_csv(destination)
    from facets_overview.generic_feature_statistics_generator import GenericFeatureStatisticsGenerator
    import base64

    gfsg = GenericFeatureStatisticsGenerator()
    proto = gfsg.ProtoFromDataFrames([{'name': 'train', 'table': data}])
    protostr1 = base64.b64encode(proto.SerializeToString()).decode("utf-8")
    # print(protostr1)

    return render_template("examples/tables.html",data=protostr1)

# @app.route("/upload",methods=["POST",'GET'])
# def upload():
#     target=os.path.join(APP_ROOT,"/home/aayushi/ml-simu")
#     # print(target)

#     if not os.path.isdir(target):
#         os.mkdir(target)

#     file=request.files["file"]
#     # print(file)
#     destination=os.path.join(target,file.filename)
#     print(destination)
#     file.save(destination)
#     data = pd.read_csv(destination)
#     return render_template("upload.html",data=protostr1)
if __name__=='__main__':
    app.run(port=4003,debug=True)
