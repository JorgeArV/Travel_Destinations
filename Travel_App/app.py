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
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine, func)
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pickle

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Database Setup
#################################################

# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import func

# engine=create_engine('postgres://otkchevrhnqetc:72eab30a1c38706e21ea18fbe562411992be9da86472c052eab1300cd9fd5261@ec2-52-71-161-140.compute-1.amazonaws.com:5432/d1tptl61lsnvca') 

# Base = automap_base()
# Base.prepare(engine, reflect=True)

# #set all tables to variables
# Weather_Data=Base.classes.Weather_Data

# session = Session(engine)

# db = SQLAlchemy(app)

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
       #return ("Variables are " +  var_month + " and " +var_day_start + " and " +var_day_end + " and " +temp_max + " and " +temp_min + humidity)

       model = pickle.load(open("model.pkl", "rb"))
       prediction = model.predict([[temp_max, temp_min, humidity]])
       print(prediction)
       result=str(prediction[0])
    else:
        result='No prediction'
    #    return render_template("index.html", result=result)
    #  return jsonify(str(prediction[0]))
    #  return (str(prediction[0]))
      
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run()
