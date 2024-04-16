from flask import Flask,render_template,request,redirect
import os
from model.entity.barra import Barra

app = Flask(__name__, template_folder=os.path.abspath('view/templates'), static_folder=os.path.abspath("view/static"))


def Total_peso_linear(lista_barras):
    total_peso_linear = 0
    for barra in lista_barras:
        total_peso_linear+=barra.peso_linear
    
    return total_peso_linear * 0.03937



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
        
        qts_fios_de_macarrao = int(qts_fios_de_macarrao) + 1

  
        barra = Barra(len(lista_barras) + 1,tipo,esforco_interno,comprimento,qts_fios_de_macarrao) 
        print(barra)         

        lista_barras.append(barra)

        
        
    return render_template('index.html',lista_barras = lista_barras,total_peso_linear = Total_peso_linear(lista_barras))

    
@app.route("/<id>",methods = ['GET','POST'])
def deletar(id):
    cont = 0
    for barra in lista_barras:
        if barra.identificador == int(id):
    
            lista_barras.remove(barra)

    for barra in lista_barras:
        cont+=1
        barra.identificador = cont       

    return redirect('/')

@app.route("/imprimir",methods = ['GET','POST'])
def imprimir():
    
    return render_template('imprimir.html',lista_barras = lista_barras,total_peso_linear = Total_peso_linear(lista_barras))


    
    