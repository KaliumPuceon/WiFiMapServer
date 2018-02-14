from flask import Flask
from flask import request
from flask import url_for
import json
app = Flask(__name__)

@app.route("/respond", methods = ['GET', 'POST'])
def respond():
    if request.method == 'GET':

        """return the information for <user_id>"""
        return("GET requests will return nothing, please POST a JSON of your MAC data. The JSON format spec can be found at ((link here))")

    if request.method == 'POST':

        """modify/update the information"""
        data = "JSON Message: " + json.dumps(request.json) # a multidict containing POST data
        return(data)

    else:
        return("Invalid method in use")
