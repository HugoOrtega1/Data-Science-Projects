# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:35:06 2021

@author: Hugo
"""

from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from sklearn.utils import check_array
app = Flask(__name__)

model = pickle.load(open('model', 'rb'))



@app.route('/')
def home():
    
    return render_template('Home.html')
   
@app.route('/predict', methods=['POST'])
def predict():
        rea = request.form['ReasonCategory']
        tran = request.form['Transport Expense']
        age = request.form['Age']
        edu = request.form['Education']
        chi = request.form['Children']
        
        
        
        
        
        inp = np.array([[rea, tran, age, edu, chi]])
        prediction = model.predict(inp)
        
        if prediction == 1:
            return render_template('afterno.html')
        
        else:
           return render_template('afteryes.html')
       
           
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)