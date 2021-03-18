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



app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
