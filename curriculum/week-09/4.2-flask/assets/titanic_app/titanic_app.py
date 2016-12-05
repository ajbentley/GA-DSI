import flask
app = flask.Flask(__name__)

#----------MODEL GOES HERE---------------#
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("~/GA-DSI-ajb/curriculum/week-09/4.2-flask/assets/datasets/titanic.csv")
include = ['Pclass','Sex','Age','Fare','SibSp','Survived']

# create dummies and drop NaNs
df['Sex'] = df['Sex'].apply(lambda x: 0 if x == 'male' else 1)
df = df[include].dropna()

X = df[['Pclass','Sex','Age','Fare','SibSp']]
y = df['Survived']

PREDICTOR = RandomForestClassifier(n_estimators=100).fit(X,y)
#----------ROUTES GO HERE----------------#

@app.route('/predict', methods=["GET"])
def predict():
    pclass = flask.request.args['pclass']
    sex = flask.request.args['sex']
    age = flask.request.args['age']
    fare = flask.request.args['fare']
    sibsp = flask.request.args['sibsp']

    item = [pclass, sex, age, fare, sibsp]
    score = PREDICTOR.predict_proba(item)
    results = {'survival chances': score[0,1], 'death chances': score [0,0]}
    return flask.jsonify(results)



if __name__ == '__main__':
  '''Connects to the server'''

HOST = '127.0.0.1'
PORT = '4000'
app.run(HOST,PORT)

#------------ CREATING AN API, METHOD 2 --------------#

#This method takes input via an HTML page
@app.route('page')
def page():
  with open("page.html", 'r') as viz_file:
    return viz_file.read()

@app.route('/result', methods=['POST', 'GET'])
def result():
  '''Gets prediction using the HTML form'''
  if flask.request.method == 'POST':

    inputs = flask.requests.form

    pclass = inputs['pclass'][0]
    sex = inputs['sex'][0]
    age = inputs['age'][0]
    fare = inputs['fare'][0]
    sipsp = inputs['sibsp'][0]

    item = np.array([pclass, sex, age, fare, sibsp])
    score = PREDICTOR.predict_proba(item)
    results = {'survival chances': score[0,1], 'death chances': score [0,0]}
    return flask.jsonify(results)
