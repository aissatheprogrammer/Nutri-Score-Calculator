from flask import Flask, render_template, request
from joblib import dump, load

# instancier une application Flask
app = Flask(__name__)

@app.route("/")
def index():
  return render_template("templt.html")

@app.route('/resultat',methods = ['POST'])
def resultat():
  result = request.form
  E = [] 
  if result['Energie'] == "" :    
    E = 0
  else :
    E = result['Energie']
  S = []
  if result['Sucre'] == "" :
    S = 0
  else :
    S = result['Sucre']
  A = []
  if result['Acide_gras'] == "" :
    A = 0
  else :
    A = result['Acide_gras']
  F = []
  if result['Fibre'] == "" : 
    F = 0
  else :
    F = result['Fibre']
  P = []
  if result['Proteine'] == "" :
    P = 0
  else :
    P = result['Proteine']
  Se = []
  if result['Sel'] == "" : 
    Se = 0
  else :
    Se = result['Sel']
  FL = []
  if result['Fruit_legume'] == "" : 
    FL = 0
  else : 
    FL = result['Fruit_legume']
  regr = load('finalized_model.joblib')
  resul = str(regr.predict([[E,A,S,F,P,Se,FL]]))
  print(resul.__class__)
  return render_template("resultat.html", resul = resul[2], E=E, A=A, S=S , F=F, P=P, Se=Se, FL=FL)

@app.route('/info')
def info():
  return render_template("info.html")
