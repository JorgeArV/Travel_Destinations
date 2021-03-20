# import necessary libraries
import os
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import (create_engine, func)
from flask import (
    Flask,
    render_template,
    url_for,
    json,
    jsonify,
    request,
    redirect)

#from MlTest_ulisses import city_predictor
#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

engine=create_engine('postgres://otkchevrhnqetc:72eab30a1c38706e21ea18fbe562411992be9da86472c052eab1300cd9fd5261@ec2-52-71-161-140.compute-1.amazonaws.com:5432/d1tptl61lsnvca') 

Base = automap_base()
Base.prepare(engine, reflect=True)

#set all tables to variables
Weather_Data=Base.classes.Weather_Data

session = Session(engine)

db = SQLAlchemy(app)

# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")
    #get variables from index

    #user_var1, user_var2


    #use model predict
    # output = city_predictor(user_var1, user_var2)

    return jsonify(output)
if __name__ == "__main__":
    app.run()
