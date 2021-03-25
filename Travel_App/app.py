# import necessary libraries
import os
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine, func)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask import (
    Flask,
    render_template,
    url_for,
    json,
    jsonify,
    request,
    redirect)

import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pickle

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

@app.route('/', methods=['POST', 'GET'])
def my_form_post():


    if request.method == "POST":
       temp_max = request.form.get("temp_max")
       temp_min = request.form.get("temp_min")
       humidity = request.form.get("humidity")
       model = pickle.load(open("model.pkl", "rb"))
       prediction = model.predict([[temp_max, temp_min, humidity]])
       print(prediction)
       result=str(prediction[0])
    else:
        result='No prediction'
      
    return render_template("index.html", result=result)

@app.route('/v2', methods=['POST', 'GET'])
def my_form_post2():


    if request.method == "POST":
       price = request.form.get("min_price")
       rating = request.form.get("rating")

       model2 = pickle.load(open("model2.pkl", "rb"))
       prediction2 = model2.predict([[price, rating]])
       print(prediction2)
       result2=str(prediction2[0])
    else:
        result2='No prediction'
      
    return render_template("index.html", result_2=result2)

if __name__ == "__main__":
    app.run()
