from flask import Flask,render_template,request
import os
from model.entity.tabela import *

app = Flask(__name__, template_folder=os.path.abspath('view/templates'), static_folder=os.path.abspath("view/static"))

lista_barras = [] 
@app.route("/",methods = ['GET','POST'])
def index():
    
       
    if request.method == "POST":
        if not request.form['esforco_interno']:
            esforco_interno = 0
        else:
            esforco_interno = float(request.form['esforco_interno'])

        if not request.form['comprimento']:
            comprimento = 0
        else:
            comprimento = float(request.form['comprimento'])

        
        tipo = request.form['tipo']        
             

       
        if tipo == 'C' :
            qts_fios_de_macarrao= ((esforco_interno*(comprimento * 10)**2) /27906*1**4)**0.5
            

        elif tipo == 'T':
            qts_fios_de_macarrao = esforco_interno/42.67

        else:
            qts_fios_de_macarrao = 0

  
        
        lista_barras.append(Barra(len(lista_barras) + 1,tipo,esforco_interno,comprimento,qts_fios_de_macarrao))        
        

        return monta_tabela(lista_barras) 
    return render_template('index.html',lista_barras = None)

    
        
def monta_tabela(lista_barras):    
    table = ItemTable(lista_barras)
    table.classes.append("table")
    table.classes.append("table-striped")
    table.classes.append("table-hover")   
        

    return table.__html__()




    
    