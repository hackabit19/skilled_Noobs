import os
from flask import Flask,jsonify,request,render_template
from config import Config

APP_ROOT=os.path.dirname(os.path.abspath(__file__))

import sys
sys.path.append('/home/agni/Downloads/facets-master/facets_overview/python')
import pandas as pd




@app.route("/")
def index():
     return "DONE"

@app.route("/tables")
def tables():
    return "Hello world"

if __name__=='__main__':
    app.run(port=4003,debug=True)
