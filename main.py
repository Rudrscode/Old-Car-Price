from flask import Flask,render_template,request
import pandas as pd
import pickle
import numpy as np
app=Flask(__name__)
model=pickle.load(open("LinearRegressionModel.pkl",'rb'))
car=pd.read_csv("cleaned car.csv")
@app.route('/')
def index():
    companies=sorted(car['company'].unique())
    car_models=sorted(car['name'].unique())
    year=sorted(car['year'].unique(),reverse=True)
    fuel_type=car['fuel_type'].unique()
    companies.insert(0,"Select Company")
    return render_template('index.html',companies=companies,car_models=car_models,years=year,fuel_types=fuel_type)
@app.route('/predict',methods=['POST'])
def predict():
    company=request.form.get('company')
    car_model=request.form.get("car_models")
    year=int(request.form.get('year'))
    fuel_type=request.form.get('fuel_type')
    kms_driven=int(request.form.get('kilo_driven'))
    prediction=model.predict(pd.DataFrame([[car_model,company,year,kms_driven,fuel_type]],columns=['name','company','year','kms_driven','fuel_type']))
    return str(np.round(prediction[0],2))




