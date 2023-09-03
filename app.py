from flask import Flask, request
from vans import *
app = Flask(__name__)        
@app.route('/insert/arg=<name>&<lat>&<lon>', methods =['GET'])
def insert(name,lat,lon):
    insert_van(name, lat, lon)
    display()
    return {"res": "true"}
    
@app.route('/update/arg=<name>&<lat>&<lon>', methods =['GET'])
def update(name,lat,lon):
    update_van(name, lat, lon)
    display()
    return {"res": "true"}
@app.route('/delete=<name>', methods =['GET'])
def delete(name):
    delete_van(name)
    display()
    return {"res": "true"}
@app.route('/get=<name>', methods =['GET'])
def get(name):
    res = get_van(name)[0]
    response = {
            "name" : res[0],
            "lat" : res[1],
            "lon" : res[2]
            }
    return response  
app.run(debug = True, host='0.0.0.0')
