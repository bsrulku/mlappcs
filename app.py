import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
from utilities import prediction
import os


app = Flask(__name__)
# ToDo Len data kısmını loan id çıktıktan sonra tekrar kontrol et.
@app.post('/predict')
def predict():
    data = request.json
    if len(data) < 11: 
        return jsonify({"Error":"Eksik Oznitelik Alindi"})
    elif len(data) >11 :
        return jsonify({"Error":"Fazla Oznitelik Alindi"})
    else:
        try:
            result =prediction(data)
            return jsonify(str(result))
        except:
            return jsonify({"Error":"Verdiğiniz Değerleri Kontrol Ediniz! "})

@app.get('/list')
def listLogs():
    try:
        logs = pd.read_csv('past_loans.csv')
        return logs.to_json(orient="index")
    except:
        return jsonify({"Condition" : "No log available"})

@app.get('/clean')
def cleanLogs():
    f = open("past_loans.csv", "w")
    f.truncate()
    f.close()   
    return jsonify({"Success" : "All logs deleted"})


if __name__== "__main__":
    app.run(host='0.0.0.0',debug=True)

