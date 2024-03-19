from flask import Flask,render_template,request
import os
from model.entity.barra import Barra
import json
import jsonify

app = Flask(__name__, template_folder=os.path.abspath('view/templates'), static_folder=os.path.abspath("view/static"))

lista_barras = []  
@app.route("/",methods = ['GET','POST'])
def index():
    
       
    if request.method == "POST":
        esforco_interno = float(request.form['esforco_interno'])
        comprimento = float(request.form['comprimento'])
        tipo = request.form['tipo']        
             

       
        if tipo == 'C' :
            qts_fios_de_macarrao= ((esforco_interno*(comprimento * 10)**2) /27906*1**4)**0.5
            

        elif tipo == 'T':
            qts_fios_de_macarrao = esforco_interno/42.67

        else:
            qts_fios_de_macarrao = 0

        barra = {
            "esforco_interno" : str(esforco_interno),
            "comprimento" : str(comprimento),
            "tipo" : tipo,
            "qtd_fios" : qts_fios_de_macarrao
        }

        barra_JSON = json.dumps(barra)

        lista_barras.append(barra_JSON)
        print(lista_barras)
        

        return lista_barras
    return render_template('index.html',lista_barras = None)

    
        
   




    
    